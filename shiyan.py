import threading
import time


def sing():
    for i in range(3):
        print("i am sing ooo~")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("i am dance lll~")
        time.sleep(0.5)



sing_thread = threading.Thread(target=sing)
dance_thread = threading.Thread(target=dance)

sing_thread.start()
dance_thread.start()