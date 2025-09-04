#%%
def get_processor_speed() -> float:
    import psutil
    cpu_ghz = psutil.cpu_freq()
    processor_ghz = f'{cpu_ghz.current:.2f}'
    return processor_ghz

def get_mem_installed() -> str:
    import psutil
    mem_installed = psutil.virtual_memory()
    avail_memory_bytes = mem_installed.available
    avail_memory_bytes = avail_memory_bytes / (1024**3)
    return f"{avail_memory_bytes:.2} GB"
    

def get_file_size(file_path: str) -> float:
    import os
    current_file_size = os.path.getsize(file_path)
    return current_file_size

def benchmark_mark_time(file_language_run: str, file_size: int, time: str, proc_speed: str, mem_availlable: str) -> str:
    import csv
    import os
    results_header = ["file_name","file_size_mb","time_run","cpu_speed_mhz","total_mem_available"]
    results_file = 'results.csv'
    result_file_exists = os.path.exists(results_file)
    result = ""
    file_name_run = file_language_run.split("\\")[-1]
    print(file_name_run)
    data_run_results = [file_name_run, file_size, time, proc_speed, mem_availlable]
    with open(results_file, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not result_file_exists:
            writer.writerow(results_header)
        writer.writerow(data_run_results)
        result = "Data added"
    return result