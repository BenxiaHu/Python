from multiprocessing import  Process
import os, time
def fun1(name1,name2):
    start = time.time()
    print('test %s %s processes' %(name1,name2))
    end = time.time()
    print('Task runs %0.2f seconds.' % (end - start))

#def fun1(name):
#    print('test %s processes' %name1)

if __name__ == '__main__':
    process_list = []
    for i in range(5):  ##开启5个子进程执行fun1函数
        p = Process(target=fun1,args=('Python','R')) #实例化进程对象
        p.start()
        process_list.append(p)
    for i in process_list:
        p.join()
        print('done')
