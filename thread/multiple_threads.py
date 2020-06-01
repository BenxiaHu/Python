import threading
import time

##如果子线程不加join，则主线程也会执行打印，但是主线程不会结束，还是需要待非守护子线程结束之后，主线程才结束
def say(name):
    print('你好%s at %s' %(name,time.ctime()))
    time.sleep(2)
    print("结束%s at %s" %(name,time.ctime()))

def listen(name):
    print('你好%s at %s' % (name,time.ctime()))
    time.sleep(4)
    print("结束%s at %s" % (name,time.ctime()))

if __name__ == '__main__':
    t1 = threading.Thread(target=say,args=('tony',))  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
    t1.start() #线程执行
    t2 = threading.Thread(target=listen, args=('simon',)) #这里就是创建了一个线程对象t2
    t2.start()
    print("程序结束=====================")



##主线程print最后执行，并且主线程退出
import threading
import time

def say(name):
    print('你好%s at %s' %(name,time.ctime()))
    time.sleep(2)
    print("结束%s at %s" %(name,time.ctime()))

def listen(name):
    print('你好%s at %s' % (name,time.ctime()))
    time.sleep(4)
    print("结束%s at %s" % (name,time.ctime()))

if __name__ == '__main__':
    t1 = threading.Thread(target=say,args=('tony',))  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
    t1.start() #线程执行
    t2 = threading.Thread(target=listen, args=('simon',)) #这里就是创建了一个线程对象t2
    t2.start()
    t1.join() #join等t1子线程结束，主线程打印并且结束
    t2.join() #join等t2子线程结束，主线程打印并且结束
    print("程序结束=====================")



import threading
import time
num = 10
def fun_sub(ID):
    global num
    lock.acquire()
    num2 = num
    time.sleep(0.001)
    num = num2-1
    print('num2=%s' %num2)
    print('----%s----' %ID)
    lock.release()


if __name__ == '__main__':
    print('开始测试同步锁 at %s' % time.ctime())
    lock = threading.Lock() #创建一把同步锁
    thread_list = []
    for thread in range(num):
        t = threading.Thread(target=fun_sub, args=('小明',))
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print('num is %d' % num)
    print('结束测试同步锁 at %s' % time.ctime())