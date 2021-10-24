# Database Study: Redis vs PostGreSQL
This project is a study on the Redis DataBase Management System (DBMS) and another DBMS, PostGreSQL.  
The goal of this study is to shed light on the common points and the differences between the two above DBMS'.  
The database used in the study is the [animal-crossing database](https://www.kaggle.com/jessicali9530/animal-crossing-new-horizons-nookplaza-dataset) on Kaggle.

## Table Of Content.
- [0  ](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#0-organization-of-the-repository-toc) Organization of the repository
- [1  ](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#1-prerequisites-toc)                  Prerequisites.
- [2  ](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#2-import-the-database-toc)            Import the database...
- [2.1](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#21--into-postgresql-toc)               ... into PostGreSQL.
- [2.2](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#22--into-redis-toc)                    ... into Redis.

## 0. Organization of the repository [[toc](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#table-of-content)]

The repository is organized as follows:  
📦 animal-crossing-db-study  
┣ 📂 [`tables`]  
┃ ┣ 📜 [`accessories.csv`]  
┃ ┣ 📜 [`achievements.csv`]  
┃ ┣ ...  
┃ ┗ 📜 [`wallpaper.csv`]  
┣ 📂 [`scripts`]  
┃ ┣ 📂 [`imports`]  
┃ ┃ ┣ 📜 [`redis_import_main.py`]  
┃ ┃ ┣ 📜 [`import_db.redis`]  
┃ ┃ ┣ 📜 [`cact4p.sql`]  
┃ ┃ ┗ 📜 [`cact4p`]  
┃ ┣ 📜 ...  
┃ ┗ 📜 [`analysis.py`]  
┣ 📜 LICENCE  
┗ 📜 README.md  

## 1. Prerequisites. [[toc](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#table-of-content)]
Install PostGreSQL: [tutorial](https://supaerodatascience.github.io/OBD/0_2_postgres.html#postgresql-installation)  
Install Redis: [tutorial](https://redis.io/)
```bash
pip install redis
```

## 2. Import the database... [[toc](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#table-of-content)]
### 2.1. ... into PostGreSQL. [[toc](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#table-of-content)]

Run the following commands to create a new data base and automatically fill the tables:  
```bash
createdb animal-crossing
```
and then
```bash
./scripts/imports/cact4p /path/to/tables
```
or
```bash
./scripts/imports/cact4p $(readlink -f tables)
```

### 2.2. ... into Redis. [[toc](https://github.com/AntoineStevan/animal-crossing-db-study/tree/main/#table-of-content)]

After installing redis server, and redis-py on your computer. And making sure the redis server is running. Execute the python file to generate a redis script.  
i.e. in one terminal, or in one `tmux`-like tool session:
```bash
redis-server
```
and in a another one:
```bash
python3 scripts/imports/redis_import_main.py tables
```
Use `python3 scripts/imports/redis_import_main.py -h` to learn more about the use of the python script.


[`tables`]: tables
[`accessories.csv`]: tables/accessories.csv
[`achievements.csv`]: tables/achievements.csv
[`wallpaper.csv`]: tables/wallpaper.csv
[`scripts`]: scripts
[`imports`]: scripts/imports
[`redis_import_main.py`]: scripts/imports/redis_import_main.py
[`import_db.redis`]: scripts/imports/import_db.redis
[`cact4p.sql`]: scripts/imports/cact4p.sql
[`cact4p`]: scripts/imports/cact4p
[`analysis.py`]: scripts/analysis.py
