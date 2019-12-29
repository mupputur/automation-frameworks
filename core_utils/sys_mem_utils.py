# Get system memory details
import os
import psutil

def get_sys_mem_info():
    vm = psutil.virtual_memory()
    return (vm.total, vm.used, vm.free)

def get_sys_free_mem():
    mem_info = get_mem_info()
    return mem_info[-1]

def get_sys_used_mem():
    mem_info = get_mem_info()
    return mem_info[1]

def get_sys_total_mem():
    mem_info = get_mem_info()
    return mem_info[0]

if __name__ == "__main__":
    total_mem = get_sys_mem_info()
    print(total_mem)



