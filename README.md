# animal-crossing-db-study

## Create the recipes data base in PostGreSQL:
After installing postgre on your computer, run the following commands to create a new data base and a new *recipes* table:  
```bash
createdb animal-crossing
psql -d animal-crossing -f create-animal-crossing-tables.sql -v recipes_path="'/path/to/animal-crossing-db-study/tables/recipes.csv'"
```
