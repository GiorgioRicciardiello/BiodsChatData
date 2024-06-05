### Create the sqlite databases from your .sql/csv/xlsx files.


## Input csv 
1. To prepare a SQL DB from your CSV and XLSX files, copy your files in `data/csv_xlsx` and in the terminal, from the project folder, execute:
```
python src/prepare_csv_xlsx_sqlitedb.py
```

This command will create a SQL database named `csv_xlsx_sqldb.db` in the `data` directory.

2. To prepare a vectorDB from your CSV and XLSX files, copy your files in `data/for_upload` and in the terminal, from the project folder, execute:
```
python src/prepare_csv_xlsx_vectordb.py
```
