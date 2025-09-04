def transform_files(measurement_file_name: str) -> str:
    import duckdb
    file_path = '../data/'
    measurement_file_path_and_name = file_path + measurement_file_name 
    result = ""
    measurement_file_name_result = str(measurement_file_name).split(".")[0]
    measurement_file_name_result = measurement_file_name_result + '.parquet'
    try:
        duckdb.sql(f"""COPY
                        (SELECT * FROM read_csv('{measurement_file_path_and_name}'))
                        TO '{file_path}{measurement_file_name_result}'
                        (FORMAT parquet);""")
        result = "Success, file transformed."
        return result
    except ValueError as e:
        result = f"Failed, check the error: {e}"
        return result

import os
import glob
from pathlib import Path

root_folder = os.path.dirname(os.path.dirname(__file__))
data_folder = root_folder + '/data'
files_paths = glob.glob(os.path.join(data_folder,'*.txt'))

for file in files_paths:
    file_name = file.split("\\")[-1]
    result_message = transform_files(file_name)
    print(result_message)

