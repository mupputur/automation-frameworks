import matplotlib.pyplot as plt
from sys_mem_utils import get_sys_mem_info

def show_bar_graph(xargs, yargs):
    plt.bar(xargs, yargs)
    plt.show()


if __name__ == "__main__":
   mem_list = get_sys_mem_info()
   print(mem_list)
   y_axis = mem_list
   x_axis = ['Total', 'Used', 'Free']
   show_bar_graph(x_axis, y_axis)
   

