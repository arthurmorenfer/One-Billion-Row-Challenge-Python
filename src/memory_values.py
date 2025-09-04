import psutil
mem_installed = psutil.virtual_memory()
total_memory_bytes = mem_installed.total
total_memory_bytes = total_memory_bytes / (1024**3)
print(f"{total_memory_bytes:.2f} GB")