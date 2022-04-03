"""
PostgreSQL 客户端
"""

import psycopg2
import threading


_MAX_RECONNECT_TIMES = 3
_CONNECT_TIME_OUT = 2


class PGClient(object):
    """
    PostgreSQL 客户端
    """
    PG_DB = ""
    PG_HOST = ""
    PG_PORT = ""
    PG_USER = ""
    PG_PASS = ""

    def __init__(
            self, host: str = PG_HOST, port: str = PG_PORT, user: str = PG_USER,
            pwd: str = PG_PASS, db_name: str = PG_DB):
        """
        初始化

        Args:
            host(str): IP 地址
            port(str): 端口号
            user(str): 用户名
            pwd(str): 密码
            db_name(str): 库名
        """
        self.__host = host
        self.__port = port
        self.__user = user
        self.__pwd = pwd
        self.__db_name = db_name
        self.__connection = None
        self.__cursor = None
        self.__lock = threading.Lock()
        self.__is_reconnect = 0

    def __del__(self):
        """
        使用完毕销毁链接
        """
        self.destory()

    def destory(self):
        """
        销毁数据库连接
        """
        try:
            if self.__cursor is not None:
                self.__cursor.close()
        except:
            pass
        try:
            if self.__connection is not None:
                self.__connection.close()
        except:
            pass
        self.__connection = None
        self.__cursor = None

    def reconnect(self):
        """
        重连，仅限在单线程中使用
        """
        self.destory()
        return self.__connect_db()

    def check_conected(self):
        """
        检查数据库是否已经连接
        """
        if self.__connection is None:
            return False
        return True

    def __connect_db(self):
        """
        创建连接
        """
        ret = True
        try:
            self.__connection = psycopg2.connect(
                host=self.__host,
                port=self.__port,
                user=self.__user,
                password=self.__pwd,
                dbname=self.__db_name,
                connect_timeout=_CONNECT_TIME_OUT
            )
            self.__cursor = self.__connection.cursor()
            self.__is_reconnect = 0
        except Exception as e:
            self.__is_reconnect += 1
            self.destory()
            ret = False
            raise Exception(f"connect pg db [{self.__host}] failed, {e}")
        return ret

    def __connect(self):
        """
        连接 PG 库
        """
        self.__lock.acquire()
        while self.__is_reconnect < _MAX_RECONNECT_TIMES:
            # 多进程防止重复登录
            if self.check_conected():
                break
            self.destory()
            if self.__connect_db():
                break
        self.__lock.release()

    def execute(self, sql: str, params=None):
        """
        执行 PGSQL

        Args:
            sql(str): SQL 语句
            params(tuple or dict): 参数元组或参数字典
        """
        self.__connect()
        if params is None:
            self.__cursor.execute(sql)
        else:
            self.__cursor.execute(sql, params)
        self.__connection.commit()

    def execute_in_bulk(self, sql: str, params=None):
        """
        批量执行 PGSQL

        SQL 示例

        ```python
        params = {
            {"first_name":"Mike", "last_name":"Bob"},
            {"first_name":"Mike", "last_name":"Bob"},
            {"first_name":"Mike", "last_name":"Bob"},
        }
        ```

        ```sql
        INSERT INTO bar (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);
        ```

        Args:
            sql(str): SQL 语句
            params(tuple): 参数元组
        """
        self.__connect()
        self.__cursor.executemany(sql, params)
        self.__connection.commit()

    def insert(self, sql: str, params=None):
        """
        插入单行数据
        
        SQL 示例

        ```python
        params = (10, datetime.date(2020, 12, 30), "Mike")
        ```

        ```sql
        INSERT INTO bar (an_int, a_date, s_string) VALUES (%s, %s, %s);
        ```

        或

        ```python
        params = {"first_name":"Mike", "last_name":"Bob"}
        ```

        ```sql
        INSERT INTO some_table (an_int, a_date, s_string) VALUES (%(an_int)s, %(a_date)s, %(s_string)s);

        ```

        Args:
            sql(str): SQL 语句
            params(tuple or dict): 参数元组或参数字典

        """
        self.__connect()
        if params is None:
            self.__cursor.execute(sql)
        else:
            self.__cursor.execute(sql, params)
        self.__connection.commit()
        return int(self.__cursor.lastrowid)

    def select(self, sql: str, params=None):
        """
        执行查询语句，获取 select 结果

        Args:
            sql(str): SQL 语句
            params(tuple): 参数元组
        """
        self.__connect()
        if params is None:
            self.__cursor.execute(sql)
        else:
            self.__cursor.execute(sql, params)
        self.__connection.commit()
        return self.__cursor.fetchall()
