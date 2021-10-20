import redis
import csv
import glob

#EXECUTION PARAMETERS
db_path = './tables/*.csv' #Define database path
SCRIPT = True #generate a redis import script
AUTO = False #automatically import db now to redis dbm
DEBUG = False #debugging verbarose


#DATABASE IMPORT TO REDIS
csv_files = [f for f in glob.glob(db_path)]
elem_id = 0

if AUTO: #Open Redis DBM
    r = redis.Redis() #host='localhost', port=6379, db=0, password=None, socket_timeout=None
if SCRIPT:
    redis_script = open("./scripts/import_db.redis", "w")

for csv_file in csv_files:
    #Read CSV File
    try:
        csvfile = open(csv_file, newline='')
        csvreader = csv.reader(csvfile, delimiter=',')

        first_row = True
        for row in csvreader:
            if first_row == True:
                headers = row
                first_row = False
            else: #Add to Redis                 #TODO: add an xtra field for csv file of origin
                if AUTO: #Import directly 
                    dict = {f'{"_".join(header.split(" "))}' : f'{value}' for header, value in list(zip(headers, row))}
                    r.hmset(f'{elem_id}', dict)
                    if DEBUG:
                        print(r.hgetall(f'{elem_id}'))

                if SCRIPT: #Create redis script: ex: HMSET elem_id field1 "Hello" field2 "World"
                    dict = " ".join(f'{"_".join(header.split(" "))} "{value}"' for header, value in list(zip(headers, row)) )
                    redis_line = f'HMSET {elem_id} {dict}\n'
                    redis_script.write(redis_line)
                    if DEBUG:
                        print(redis_line)

                elem_id +=1 #at the end so we keep python index notation

        csvfile.close()
    except:
        print(f'WARNING: the file {csv_file} was not readed correctly. Possibily due to some UTF-8 caracter.')

if SCRIPT:
    redis_script.close()
