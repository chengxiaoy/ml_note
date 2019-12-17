from memory_profiler import profile
import numpy as np
import time
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    c = np.random.randn(1024,256,256)
    del a
    del b
    del c
    time.sleep(1)


    # return a

if __name__ == '__main__':
    my_func()