# -*- coding: utf-8 -*-
from collections import deque
from threading import Lock, Semaphore   #Semaphore 是用于控制进入数量的锁，控制同时进行的线程
from contextlib import contextmanager   #上下文管理

from hs_udata.utils.connection import Connection
from hs_udata.utils.decorators import retry


class ConnectionPool(object):
    def __init__(self, config):
        self._config = config.copy()
        self._lock = Lock()
        self._connections = deque()
        self._connect_timeout = config.pop("connect_timeout")
        self._signal = Semaphore(config.pop("pool_size"))

    @property
    def config(self):
        return self._config

    @retry(3, exp_name="RequestTimeOut")
    def send(self, method, **kwargs):
        with self._signal:
            with self._yield_conn() as conn:
                return conn.send(method, **kwargs)

    @contextmanager
    def _yield_conn(self):
        conn = self._get_connection()
        try:
            yield conn                #返回连接
        except Exception as ex:
            conn.close()              #连接异常时关闭连接
            raise ex
        else:
            with self._lock:
                self._connections.append(conn)         #若已加锁则将当前连接加入连接队列

    def _get_connection(self):
        with self._lock:
            while self._connections:
                conn = self._connections.popleft()        #从队列左边取出一个连接
                if conn.check():                          #检查连接是否可用
                    return conn
                else:
                    conn.close()

        return self._cretate_connection()

    @retry(5, exp_name="ConnectTimeout")
    def _cretate_connection(self):
        return Connection.get_connection(self._config)    #创建连接

    def close(self):
        with self._lock:
            for conn in self._connections:       #逐个关闭连接
                conn.close()
            self._connections.clear()            #清空队列
