import duckdb
import time

def create_duckdb():
    duckdb.sql("""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'})
        GROUP BY station
        ORDER BY station
    """).show()

if __name__ == "__main__":
    import time
    import utils
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    file_size_processed = utils.get_file_size(filename)
    #cpu_speed = utils.get_processor_speed()
    save_benchmark_results = utils.benchmark_mark_time(__file__,file_size_processed, took, cpu_speed)
    print(f"Duckdb Took: {took:.2f} sec")