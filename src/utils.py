#%%
import os
#import psutil

#def get_processor_speed() -> float:
#    import psutil
#    cpu_ghz = psutil.cpu_freq()
#    processor_ghz = cpu_ghz.current:.2f
#    return processor_ghz

def get_file_size(file_path: str) -> float:
    import os
    current_file_size = os.path.getsize(file_path)
    return current_file_size

def benchmark_mark_time(file_language_run: str, file_size: int, time: str, proc_speed: str ) -> str:
    import csv
    results_header = ["file_name","file_size_mb","time_run","cpu_speed_mhz"]
    results_file = 'results.csv'
    result_file_exists = os.path.exists(results_file)
    result = ""
    data_run_results = [file_language_run, file_size, time, proc_speed]
    with open(results_file, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not result_file_exists:
            writer.writerow(results_header)
        writer.writerow(data_run_results)
        result = "Data added"
    return result



#%%
import pandas as pd
import time
start_time = time.time()
results = pd.read_csv('results.csv')
print(results)
took = time.time() - start_time
print(f"Duckdb Took: {took:.2f} sec")