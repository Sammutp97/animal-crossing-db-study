# Databases Study: Redis vs PostGreSQL
This project is a study on the Database Management System Redis and PostGreSQL. 
The database used in the study is the animal-crossing database found in Kaggle (link).

## Import Database into PostGreSQL (Create the recipes database):
After installing postgre on your computer, run the following commands to create a new data base and a new *recipes* table:  
```bash
createdb animal-crossing
psql -d animal-crossing -f create-animal-crossing-tables.sql -v recipes_path="'/path/to/animal-crossing-db-study/tables/recipes.csv'"
```

## Import Database into Redis:
After installing redis server, and redis-py on your computer. And making sure the redis server is running. Execute the python file to generate a redis script.
Or enter into the file, and modify the AUTO variable to True to also import the db directly to redis.
