import threading as thd
import time

def fn():
    print("click")
    thd.Timer(180,fn).start()
    
fn()