# -*- coding: utf-8 -*-
import requests
import pandas as pd
import time
import six
import abc
import warnings
import os


from hs_udata.utils.common import (
    ConnectionStatus,
    ERROR_NO,
    ERROR_INFO,
    DATA
)
from hs_udata.utils.error import (
    ConnectionException,
    ConnectionTimeOut,
    RequestTimeOut,
    RequestException,
    GatewayException,
    ServerException,
    GATEWAY_ERROR_DICT,
    SERVER_ERROR_DICT,
)


class AbstractConnection(six.with_metaclass(abc.ABCMeta)):
    """
    连接抽象类
    """
    def create(self, *args, **kwargs):
        """
        创建连接对象
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def connect(self, timeout=5):
        """
        启动连接
        :param timeout:
        :return:
        """
        raise NotImplementedError

    def set_timeout(self, timeout):
        """
        设置超时时间
        :param timeout:
        :return:
        """
        raise NotImplementedError

    def send(self, *args, **kwargs):
        """
        同步发送数据
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def async_send(self, *args, **kwargs):
        """
        异步发送数据
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def receive(self, *args, **kwargs):
        """
        接收数据
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def status(self):
        """
        连接状态
        :return:
        """
        raise NotImplementedError

    def check(self):
        """
        检查连接是否可用
        :return:
        """
        raise NotImplementedError

    def error(self):
        """
        连接错误信息
        :return:
        """
        raise NotImplementedError

    def close(self):
        """
        关闭链接
        :return:
        """
        raise NotImplementedError


class Connection(object):
    """
    连接工厂类
    """
    @classmethod   #classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    def get_connection(cls, config):
        from hs_udata.utils.common import Protocol
        protocol = config.get("protocol")
        conn_timeout = config.get("connect_timeout")
        try:
            with ConnectionContext(conn_timeout):
                return globals()[Protocol[protocol].value]().create(config)
        except KeyError:
            raise RuntimeError("创建链接对象失败,请检查配置信息是否正确？config={}".format(config))


class HttpConnection(AbstractConnection):
    """
    HTTP连接对象类
    """
    import requests

    def create(self, config):
        """
        创建连接对象
        :param gateway:
        :param auth:
        :return:
        """
        # 解析config文件中的信息
        url = config.get("url")
        auth = config.get("auth")

        assert url
        assert auth

        self._url = url
        self._user = auth.get("username")
        self._pwd = auth.get("password")
        self._timeout = config.get("request_timeout")
        self._page_size = config.get("page_size")

        assert self._user
        assert self._pwd

        self._conn = requests.Session()            # 创建一个session对象，requests库的session对象还能提供请求方法的缺省数据，通过设置session对象的属性来实现
        self._status = ConnectionStatus.Connected         #调common中的连接状态码，状态设为已连接
        return self

    def set_timeout(self, timeout):
        """
        设置超时时间
        :param timeout:
        :return:
        """
        self._timeout = timeout

    def send(self, method, **kwargs):
        """
        同步发送数据
        :param args:
        :param kwargs:
        :return:
        """
        if self.check():        #已连接状态时
            if self._user == "license":
                url_path = kwargs.get("url_path", "")
                url = "".join((self._url, "/", url_path, "/", method))
            else:
                raise RuntimeError("当前只支持license登录方式")
            header = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Application-Token": self._pwd
            }
            params = kwargs
            try:
                method_data = kwargs.get("method", "GET")
                if method_data.upper() == "POST":
                    response = self._conn.post(url, headers=header, params=params, timeout=self._timeout)
                else:
                    response = self._conn.get(url, headers=header, params=params, timeout=self._timeout)
            except requests.exceptions.ConnectTimeout as ex:
                raise RequestTimeOut(ex)
            if response.status_code == 200:   #状态码200表示请求成功
                rsp = response.json()         #requests获取后直接调用json()方法转变为python字典请求获取HttpResponse对象

                # 从数据服务返回的数据
                if "error_code" in rsp:
                    if int(rsp["error_code"]) == 0:
                        df = pd.DataFrame(rsp["data"]) if rsp.get("data") else pd.DataFrame()
                        df.columns = df.columns.map(lambda x:x.lower())
                        if kwargs.get("rslt_type", 0) == 0:
                            return df
                        else:
                            import numpy as np
                            return np.array(df.to_records())

                    if SERVER_ERROR_DICT.get(int(rsp["error_code"]), None):      #获取error中异常信息
                        # warnings.warn("app_key权限认证失败，请联系管理员，error_info={}".format(rsp["resultMsg"]))
                        # warnings.warn("app_key权限已过期，请重新申请，申请站点：{}".format(rsp["resultMsg"]))
                        warnings.warn("请求异常，异常信息：{}".format(rsp["result_msg"]))
                        raise RequestException(rsp["result_msg"])
                    else:
                        warnings.warn("获取数据异常，path={}，params={}，error_info={}".
                                      format(method, kwargs, rsp["result_msg"]))
                        raise RequestException("请求发生未定义错误，错误信息：{}".format(rsp["result_msg"]))
            elif response.status_code >= 400 and response.status_code < 500:
                rsp = response.json()
                # 从新版网关返回异常
                if ERROR_NO in rsp:
                    if GATEWAY_ERROR_DICT.get(rsp[ERROR_NO], None):      #获取错误代码
                        warnings.warn("网关返回错误，错误信息：{}".format(rsp[ERROR_INFO]))
                        raise GatewayException(rsp[ERROR_INFO])
                    else:
                        raise GatewayException("网关发生未定义错误，错误信息：{}".format(rsp[ERROR_INFO]))
                # 从老版网关返回异常
                elif DATA in rsp:
                    if isinstance(rsp[DATA], list):
                        error_dict = rsp[DATA][0]
                    else:
                        error_dict = rsp[DATA]

                    if GATEWAY_ERROR_DICT.get(error_dict[ERROR_NO], None):
                        warnings.warn("网关返回错误，错误信息：{}".format(error_dict[ERROR_INFO]))
                        raise GatewayException(error_dict[ERROR_INFO])
                    else:
                        raise GatewayException("网关发生未定义错误，错误信息：{}".format(error_dict[ERROR_INFO]))
                else:
                    warnings.warn("网关返回未定义异常，异常信息：{}".format(response.text))
                    raise GatewayException(response.text)

            elif response.status_code >=500 and response.status_code < 601:            #服务错误
                warnings.warn("服务异常，异常信息：{}".format(response.text))
                raise ServerException(response.text)
            else:
                warnings.warn("异常流程，返回信息：{}".format(response.text))          #其他流程错误
                raise Exception(response.text)

        raise ConnectionException("连接已关闭，无法获取数据")          #如果没连接则raise连接异常

    def async_send(self, *args, **kwargs):
        """
        异步发送数据
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError          #尚未实现的方法错误

    def receive(self, *args, **kwargs):
        """
        接收数据
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def status(self):
        """
        连接状态
        :return:
        """
        return self._status

    def check(self):
        return self._status in [ConnectionStatus.Connected, ConnectionStatus.SafeConnected]

    def error(self):
        """
        连接错误信息
        :return:
        """
        raise NotImplementedError

    def close(self):
        """
        关闭链接
        :return:
        """
        self._conn.close()
        self._status = ConnectionStatus.Disconnected


class ConnectionContext(object):     #自定义上下文管理器
    def __init__(self, timeout=5):
        assert timeout
        self.timeout = timeout
        self.start = None

    def __enter__(self):
        self.start = time.time()    #返回当前时间的时间戳（1970纪元后经过的浮点秒数）。

    def __exit__(self, exc_type, exc_val, exc_tb):
        if time.time() - self.start > self.timeout:     #当前花费时间超时
            raise ConnectionTimeOut
