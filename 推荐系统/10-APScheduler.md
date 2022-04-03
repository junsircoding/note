# APScheduler

advanceded python scheduler

定时任务

文档地址 <https://apscheduler.readthedocs.io/en/latest/userguide.html#starting-the-scheduler>



特点：

* 不依赖于Linux系统的crontab系统定时，独立运行

* 可以动态添加新的定时任务，如

  下单后30分钟内必须支付，否则取消订单，就可以借助此工具（每下一单就要添加此订单的定时任务）

* 对添加的定时任务可以做持久保存



### 1. 安装

```shell
pip install apscheduler
```

### 2. 概念

* 触发器 triggers
* 任务存储  job stores
* 执行器 executors
* 调度器 schedulers

### 3. Trigger 触发器

#### 1） date 在特定的时间日期执行

```python
from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

def my_job(text):
    print(text)

# The job will be executed on November 6th, 2009
sched.add_job(my_job, 'date', run_date=date(2009, 11, 6), args=['text'])
sched.add_job(my_job, 'date', run_date=datetime(2009, 11, 6, 16, 30, 5), args=['text'])
sched.add_job(my_job, 'date', run_date='2009-11-06 16:30:05', args=['text'])
sched.add_job(my_job, args=['text'])  # 立即执行
sched.start()
```

#### 2） interval 经过指定的时间间隔执行

- **weeks** ([*int*](https://docs.python.org/3/library/functions.html#int)) – number of weeks to wait
- **days** ([*int*](https://docs.python.org/3/library/functions.html#int)) – number of days to wait
- **hours** ([*int*](https://docs.python.org/3/library/functions.html#int)) – number of hours to wait
- **minutes** ([*int*](https://docs.python.org/3/library/functions.html#int)) – number of minutes to wait
- **seconds** ([*int*](https://docs.python.org/3/library/functions.html#int)) – number of seconds to wait
- **start_date** (*datetime|str*) – starting point for the interval calculation
- **end_date** (*datetime|str*) – latest possible date/time to trigger on
- **timezone** (*datetime.tzinfo|str*) – time zone to use for the date/time calculations
- **jitter** (*int|None*) – advance or delay the job execution by `jitter` seconds at most.

```python
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(job_function, 'interval', hours=2)

sched.start()

```

```python
# The same as before, but starts on 2010-10-10 at 9:30 and stops on 2014-06-15 at 11:00
sched.add_job(job_function, 'interval', hours=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')
```

####  3）  cron 按指定的周期执行

- **year** (*int|str*) – 4-digit year
- **month** (*int|str*) – month (1-12)
- **day** (*int|str*) – day of the (1-31)
- **week** (*int|str*) – ISO week (1-53)
- **day_of_week** (*int|str*) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
- **hour** (*int|str*) – hour (0-23)
- **minute** (*int|str*) – minute (0-59)
- **second** (*int|str*) – second (0-59)
- **start_date** (*datetime|str*) – earliest possible date/time to trigger on (inclusive)
- **end_date** (*datetime|str*) – latest possible date/time to trigger on (inclusive)
- **timezone** (*datetime.tzinfo|str*) – time zone to use for the date/time calculations (defaults to scheduler timezone)
- **jitter** (*int|None*) – advance or delay the job execution by `jitter` seconds at most.

```python
from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print "Hello World"

sched = BlockingScheduler()

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

sched.start()

```

```python
# Runs from Monday to Friday at 5:30 (am) until 2014-05-30 00:00:00
sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2014-05-30')
```

### 4. 任务存储 job stores

* MemoryJobStore  默认 内存

* MongoDBJobStore

  ```python
  from apscheduler.jobstores.mongodb import MongoDBJobStore
  
  MongoDBJobStore(database='apscheduler', collection='jobs', client=None, **connect_arg)
  ```

* RedisJobStore

  ```python
  from apscheduler.jobstores.redis import RedisJobStore
  
  RedisJobStore(db=0, jobs_key='apscheduler.jobs', run_times_key='apscheduler.run_times', **connect_arg)
  ```

* SQLAlchemyJobStore

  ```python
  from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
  
  SQLAlchemyJobStore(url=None, engine=None, tablename='apscheduler_jobs', metadata=None, tableschema=None, engine_options=None)
  
  SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
  ```

### 5. 执行器 executors

* ThreadPoolExecutor

  ```python
  ThreadPoolExecutor(max_workers)  
  ThreadPoolExecutor(20) # 最多20个线程同时执行
  ```

* ProcessPoolExecutor

  ```python
  ProcessPoolExecutor(max_workers)
  ProcessPoolExecutor(5) # 最多5个进程同时执行
  ```

### 6. Scheduler 调度器

- [`BlockingScheduler`](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/blocking.html#apscheduler.schedulers.blocking.BlockingScheduler):  作为独立进程时使用
- [`BackgroundScheduler`](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/background.html#apscheduler.schedulers.background.BackgroundScheduler):  在除了以下框架之外的框架工具中使用
- [`AsyncIOScheduler`](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/asyncio.html#apscheduler.schedulers.asyncio.AsyncIOScheduler): use if your application uses the asyncio module
- [`GeventScheduler`](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/gevent.html#apscheduler.schedulers.gevent.GeventScheduler): use if your application uses gevent
- [`TornadoScheduler`](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/tornado.html#apscheduler.schedulers.tornado.TornadoScheduler): use if you’re building a Tornado application
- [`TwistedScheduler`](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/twisted.html#apscheduler.schedulers.twisted.TwistedScheduler): use if you’re building a Twisted application
- `QtScheduler`: use if you’re building a Qt application

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
```

### 7. 配置

#### 方法1 

```python
rom pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
```

#### 方法2

```python
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor


jobstores = {
    'mongo': {'type': 'mongodb'},
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': {'type': 'threadpool', 'max_workers': 20},
    'processpool': ProcessPoolExecutor(max_workers=5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler()

# .. do something else here, maybe add jobs etc.

scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
```

#### 方法3

```python
from apscheduler.schedulers.background import BackgroundScheduler


# The "apscheduler." prefix is hard coded
scheduler = BackgroundScheduler({
    'apscheduler.jobstores.mongo': {
         'type': 'mongodb'
    },
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///jobs.sqlite'
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': 'UTC',
})
```

### 8. 启动

```python
scheduler.start()
```

* 对于BlockingScheduler ，程序会阻塞在这，防止退出
* 对其与其他scheduler，程序会立即返回，后台运行

### 9. 任务管理

方式1

```python
job = scheduler.add_job(myfunc, 'interval', minutes=2)  # 添加任务
job.remove()  # 删除任务
job.pause() # 暂定任务
job.resume()  # 恢复任务
```

方式2

```python
scheduler.add_job(myfunc, 'interval', minutes=2, id='my_job_id')  # 添加任务	
scheduler.remove_job('my_job_id')  # 删除任务
scheduler.pause_job('my_job_id')  # 暂定任务
scheduler.resume_job('my_job_id')  # 恢复任务
```

### 10. 调整任务

```python
job.modify(max_instances=6, name='Alternate name')

scheduler.reschedule_job('my_job_id', trigger='cron', minute='*/5')
```

### 11. 停止

```python
scheduler.shutdown()
```

