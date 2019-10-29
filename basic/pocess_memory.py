from multiprocessing import Pool, Process, Manager
import numpy as np
import time
import os

print('Global_print', os.getpid())


def compute2(matrix):
    m = np.random.randn(1024, 128)
    # print(size_m_1.shape)
    time.sleep(10.0)
    return matrix.dot(m)


class Demo:
    def __init__(self):
        self.hundred_m = np.random.randn(100, 128, 1024)

    def run_proc(self, size):
        print("run child processid {}:size {}".format(os.getpid(), size))

    def allocate_memory(self, size):
        size_m_1 = np.random.rand(size - 1, 128, 1024)
        self.run_proc(size)
        return self.compute(size_m_1)

    def compute(self, matrix):
        m = np.random.randn(1024, 128)
        # print(size_m_1.shape)
        time.sleep(10.0)
        return matrix.dot(m)

    def test(self, size_list):
        p = Pool(5)
        size_list = [10, 20, 30, 40, 50]

        memory_list = []
        since = time.time()
        extern_memory = []
        for size in size_list:
            extern_memory.append(np.random.randn(size, 128, 1024))
        # future_list = []

        # for i, size in enumerate(size_list):
        #     # res_future = p.apply_async(allocate_memory, args=(size,))
        #     res_future = p.apply_async(compute, args=(extern_memory[i],))
        #     future_list.append(res_future)

        future_list = p.map_async(compute2, extern_memory)

        supply_time = time.time()
        print("supply time :{}".format(supply_time - since))
        p.close()
        p.join()
        future_list = future_list.get()
        for future in future_list:
            print(future.shape)
        print("total cost time:{}".format(time.time() - since))


def getGenerator(n):
    for i in range(n):
        print(i)
        yield i


def getId(n):
    print(id(n))
    print(n.__next__())


if __name__ == '__main__':
    # demo = Demo()
    # demo.test([10, 20, 30, 40, 50])


    generator = getGenerator(10)


    p1 = Process(target=getId, args=(generator,))
    p2 = Process(target=getId, args=(generator,))
    p3 = Process(target=getId, args=(generator,))
    print(id(generator))
    p1.start()
    p2.start()
    p3.start()

    # p = Pool(5)
    # size_list = [10, 20, 30, 40, 50]
    #
    # memory_list = []
    #
    # since = time.time()
    # extern_memory = []
    # for size in size_list:
    #     extern_memory.append(np.random.randn(size, 128, 1024))
    # # future_list = []
    #
    # # for i, size in enumerate(size_list):
    # #     # res_future = p.apply_async(allocate_memory, args=(size,))
    # #     res_future = p.apply_async(compute, args=(extern_memory[i],))
    # #     future_list.append(res_future)
    #
    # future_list = p.map_async(compute, extern_memory)
    #
    # supply_time = time.time()
    # print("supply time :{}".format(supply_time - since))
    # p.close()
    # p.join()
    # future_list = future_list.get()
    # for future in future_list:
    #     print(future.shape)
    # print("total cost time:{}".format(time.time() - since))
