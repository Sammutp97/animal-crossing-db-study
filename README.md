# Databases Study: Redis vs PostGreSQL
This project is a study on the Database Management System Redis and PostGreSQL. 
The database used in the study is the animal-crossing database found in Kaggle (link).

## Import Database into PostGreSQL (Create the recipes database):
After installing postgre on your computer, run the following commands to create a new data base and a new *recipes* table:  
```bash
createdb animal-crossing
./import_db_scripts/create /path/to/import_db_scripts/tables
```
or
```bash
./import_db_scripts/create $(readlink -f import_db_scripts/tables)
```

## Import Database into Redis:
After installing redis server, and redis-py on your computer. And making sure the redis server is running. Execute the python file to generate a redis script.
Or enter into the file, and modify the AUTO variable to True to also import the db directly to redis.
