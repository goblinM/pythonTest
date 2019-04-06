'''
多进程
'''
import random
import time
from multiprocessing import Process,Pool,Queue
import os

#子进程要执行的代码
def run_proc(name):
    print("Run child process %s (%s)..." %(name,os.getpid()))

def long_time_task(name):
    print("Run task %s (%s)" %(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s runs %0.2f seconds" %(name,(end-start)))

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # print("parent process :", os.getpid())
    # p = Process(target=run_proc,args=("test",))
    # print("Child process will be start")
    # p.start()
    # p.join()
    # print("Child process end.")
    #########################
    # print("Parent process %s" %(os.getpid()))
    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    # print("Wait for all subprocess done ...")
    # p.close()
    # p.join()
    # print("All subprocesses done")
    #########################
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()