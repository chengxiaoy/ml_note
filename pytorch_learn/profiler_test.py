from memory_profiler import profile
import numpy as np
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    c = np.random.randn(1024,256,4)
    del b
    del c
    return a

if __name__ == '__main__':
    my_func()