import threading
import time

exitFlag = 0

def main():
    time.sleep(1)


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, ):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print(f"Starting thread: {str(self.threadID)}")

        main()

        print(f"Exiting threadL {str(self.threadID)}")


# 创建新线程
thread1 = myThread(1)
thread2 = myThread(2)
thread3 = myThread(3)
# 开启线程
thread1.start()
thread2.start()
thread3.start()
print("Exiting Main Thread\n")