#!/bin/bash
cd "$(C:\Users\Arthur\documents\github\jornada_python\One-Billion-Row-Challenge-Python\src\ "$0")"
source .venv/Scripts/activate
for i in {1..5}; do
    echo "Run $i pandas"
    python using_pandas.py
done

for i in {1..5}; do
    echo "Run $i duckdb"
    python using_duckdb.py
done

for i in {1..5}; do
    echo "Run $i python"
    python using_python.py
done

for i in {1..5}; do
    echo "Run $i duckdb_parquet"
    python using_duckdb_parquet.py
done

