import argparse
import os
import traceback

import redis
import csv
import glob

def main(db_path, script=False, auto=False, verbose=False, clean=False):
    # gets the name of the directory where the script is, to allow
    # executing the script from anywhere.
    directory = os.path.dirname(os.path.realpath(__file__))

    #DATABASE IMPORT TO REDIS
    csv_files = [f for f in glob.glob(os.path.join(db_path, "*.csv"))]
    elem_id = 0
    output_filename = os.path.join(directory, "import_db.redis")

    if clean:
        if os.path.exists(output_filename):
            print(f"removing {output_filename}")
            os.remove(output_filename)
        else:
            print("no .redis file to remove... Skipping.")

    if not script and not auto:
        print("nothing to do... Aborting.")
        return

    if auto: #Open Redis DBM
        r = redis.Redis() #host='localhost', port=6379, db=0, password=None, socket_timeout=None
    if script:
        redis_script = open(output_filename, "w")

    for csv_file in csv_files:
        #Read CSV File
        try:
            csvfile = open(csv_file, newline='')
            csvreader = csv.reader(csvfile, delimiter=',')

            first_row = True
            for row in csvreader:
                if first_row == True:
                    headers = row
                    headers[0] = headers[0][1:]
                    first_row = False
                else: #Add to Redis                 #TODO: add an xtra field for csv file of origin
                    if auto: #Import directly 
                        line = {f"{'_'.join(header.split(' '))}" : value.replace('\n', ';') for header, value in list(zip(headers, row))}
                        r.hmset(f'{elem_id}', line)
                        if verbose:
                            print(r.hgetall(f'{elem_id}'))

                    if script: #Create redis script: ex: HMSET elem_id field1 "Hello" field2 "World"
                        line = " ".join(f"{'_'.join(header.split(' '))} " + value.replace('\n', ';') for header, value in list(zip(headers, row)) )
                        redis_line = f'HMSET {elem_id} {line}\n'
                        redis_script.write(redis_line)
                        if verbose:
                            print(redis_line)

                    elem_id +=1 #at the end so we keep python index notation

            csvfile.close()
        except:
            print(traceback.format_exc())

    if script:
        redis_script.close()


if __name__ == "__main__":
    # create a parser to change behaviour from outside.
    parser = argparse.ArgumentParser()
    parser.add_argument("tables", type=str, nargs=1,
            help="the location of the tables, from the execution location (is required).")
    parser.add_argument('-s', "--script", default=False, action="store_true",
            help="if raised, the execution will generate a redis import script (defaults to False).")
    parser.add_argument('-a', "--auto", default=False, action="store_true",
            help="allows the script to automatically load the database inside a redis server. make sure a redis server is activated before hand. (defaults to False).")
    parser.add_argument('-v', "--verbose", default=False, action="store_true",
            help="turns on verbose (defaults to False).")
    parser.add_argument('-c', "--clean", default=False, action="store_true",
            help="cleans the workspace from generated .redis file (defaults to False).")

    args = parser.parse_args()

    #EXECUTION PARAMETERS
    script = args.script
    auto = args.auto
    verbose = args.verbose
    db_path = args.tables[0]
    clean = args.clean

    # the actual redis database generation.
    main(db_path, script=script, auto=auto, verbose=verbose, clean=clean)
