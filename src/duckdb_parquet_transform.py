import duckdb

def transform_files(measurement_file_name: str) -> str:
    result = ""
    measurement_file_name_result = measurement_file_name.split(".")[0]
    measurement_file_name_result = measurement_file_name_result + '.parquet'
    try:
        duckdb.sql("""COPY
                        (SELECT * FROM {measurement_file_name})
                        TO '{measurement_file_name_result}'
                        (FORMAT parquet);""")
        result = "Success, file transformed."
        return result
    except ValueError as e:
        result = f"Failed, check the error: {e}"
        return result