#%%
import duckdb
import time

def create_duckdb():
    duckdb.sql("""
        SELECT column0,
            MIN(column1) AS min_temperature,
            CAST(AVG(column1) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(column1) AS max_temperature
        FROM read_parquet("../data/measurements_one_million.parquet")
        GROUP BY column0
        ORDER BY column0
    """).show()

if __name__ == "__main__":
    import time
    import utils_benchmark
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    filename = '../data/measurements_one_million.parquet'
    file_size_processed = utils_benchmark.get_file_size(filename)
    cpu_speed = utils_benchmark.get_processor_speed()
    current_mem_available = utils_benchmark.get_mem_installed()
    save_benchmark_results = utils_benchmark.benchmark_mark_time(__file__,file_size_processed, took, cpu_speed, current_mem_available)
    #print(__file__.split("\\")[-1])
    print(f"Duckdb Took: {took:.2f} sec")