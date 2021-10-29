#! /usr/bin/bash
# performs a timing test on a given psql query.
# the query is represented by a directory name.
# in this directory, there should be two things:
#  - a `question.txt` file: contains a question
#    be displayed.
#  - a `query.psql` file: contains the query.

# some color to make it pretty.
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
LIGHTBLUE='\033[1;34m'
NC='\033[0m'

# extracting the question and the query from
# the two query files.
QUESTION=$(cat $1/question.txt | tr '\n' ' ')
QUERY=$(cat $1/query.psql | tr '\n' ' ')
echo -e "${LIGHTGREEN}question${NC}:"
echo "$QUESTION"
echo -e "${LIGHTBLUE}query${NC}:"
echo "$QUERY"
echo

# using `psql` to get an answer to the query.
ANSWER=$(psql -d animal-crossing -c "$QUERY")
echo -e "${LIGHTRED}answer${NC}:"
echo "$ANSWER"
echo

## timing section.
# to time a psql query, a solution that i found
# was to execute a file with following content:
# \timing   -- enables psql to time the queries.
# do $$
# begin
# 	QUERY   -- needs to start with PERFORM.
# end; $$

# the command file is stored in `.xquery.tmp`.
echo "\\timing" > .xquery.tmp
echo "do \$\$" >> .xquery.tmp
echo "begin" >> .xquery.tmp
echo "$(echo $QUERY | sed 's/^SELECT/PERFORM/;')" >> .xquery.tmp
echo "end; \$\$" >> .xquery.tmp

TIMINGS=()  # stores all the timing for each instance of a query.
n=101
for((i=0;i<$n;i++))
do
	echo -ne "Progress: $[ ($i+1)*100/$n ]%\r";  # the progress 'bar'.
	TIMING=$(psql -d animal-crossing -f .xquery.tmp)  # gives the time.
	# extract the actual time in ms.
	TIMING=$(echo $TIMING | sed 's/Timing is on. DO Time: \(.*\) ms/\1/; ')
	TIMINGS+=($TIMING)  # push to the times.
done;
echo "Progress: 100%"
echo

# compute the total time with awk.
tot=0
for((i=0;i<$n;i++))
do
	tot=$(awk -v a=$tot -v b=${TIMINGS[$i]} 'BEGIN { print  ( a + b ) }')
done;

# divide by number of samples with awk to get the mean.
mean=$(awk -v a="$tot" -v b=${#TIMINGS[@]} 'BEGIN { print  ( a / b ) }')

# compute the total sum of squared errors to the mean.
mse=0
for((i=0;i<$n;i++))
do
	# the error is here the difference between the time and the mean.
	err=$(awk -v a=${TIMINGS[$i]} -v b=$mean  'BEGIN { print  ( a - b ) }')
	# add the square of the error to the total sum of squared errors.
	mse=$(awk -v a=$err -v b=$err 'BEGIN { print  ( a * b ) }')
done;
# divide by the number of sample times to get the variance.
std=$(awk -v a="$mse" -v b=${#TIMINGS[@]} 'BEGIN { print  sqrt( a / b ) }')

echo "tot: $tot ms in ${#TIMINGS[@]} samples"
echo "time: $mean +/- $std ms"
