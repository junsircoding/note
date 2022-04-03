import datetime
import schedule
import time


def func():
    """
    打印执行函数的时间
    """
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)


def func2():
    """
    打印执行函数的时间
    """
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time :', ts)


def tasklist():
    schedule.clear()
    schedule.every(1).seconds.do(func2)
    for i in range(10):
        schedule.run_pending()
        time.sleep(1)


tasklist()
