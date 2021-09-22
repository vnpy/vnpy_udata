# -*- coding: utf-8 -*-
import os
import json
import warnings


_CLIENT = None


def get_client():
    global _CLIENT
    if _CLIENT is None:
        init()

    return _CLIENT


def init(username=None, password=None, **kwargs):
    """
    :param str username: 用户名，license模式下为'license'
    :param str password: 用户密码，license模式下为下发的license
    :param str protocol：传输协议，默认HTTP
    :param str url: 数据服务的URL
    :param int connect_timeout: 连接建立超时时间,默认5秒
    :param int request_timeout: 数据传输超时时间，默认300秒
    :param str compressor: 数据传输过程中的压缩算法，默认不使用
    :param int pool_size: 连接池大小，默认10
    :param int page_size: 数据请求分页大小，默认100000
    :return:
    """
    user = username
    pwd = password

    try:
        env = json.loads(os.getenv("hs_udata_CONF"))
    except:
        env = {
            "USERNAME": username,
            "PASSWORD": password
        }
    if user is None:
        user = env.get("USERNAME")
        pwd = env.get("PASSWORD")

    if pwd is None:
        raise KeyError("请设置有效Token值")

    assert user
    assert pwd

    from hs_udata.utils.config import read_config, write_config
    # 获取系统配置
    try:
        conf = read_config()['system']
    except:
        # 读取配置失败，使用默认配置启动
        warnings.warn("读取配置失败，请检查hs_udata.utils.config.yml")
        raise

    url = kwargs.pop("url", None)
    if url is None:
        url = conf.get("url")
    else:
        conf["url"] = url

    assert url

    protocol = kwargs.pop("protocol", None)
    if protocol is None:
        protocol = conf.get("protocol", "HTTP")
    else:
        if protocol != "HTTP":
            warnings.warn("protocol 当前只支持HTTP，设置的{}将不会生效".format(protocol))
        else:
            conf["protocol"] = "HTTP"

    con_timeout = kwargs.pop("connect_timeout", None)
    if con_timeout is None:
        con_timeout = conf.get("connect_timeout", 5)
    else:
        if int(con_timeout) <= 0 or int(con_timeout) > 1000:
            warnings.warn("connect_timeout 有效范围为(0, 1000]，设置的{}将不会生效".format(con_timeout))
        else:
            conf["connect_timeout"] = con_timeout

    timeout = kwargs.pop("request_timeout", None)
    if timeout is None:
        timeout = conf.get("request_timeout", 300)
    else:
        if int(timeout) <= 0 or int(timeout) > 100000:
            warnings.warn("request_timeout 有效范围为(0, 100000]，设置的{}将不会生效".format(timeout))
        else:
            conf["request_timeout"] = timeout

    pool_size = kwargs.pop("pool_size", None)
    if pool_size is None:
        pool_size = conf.get("pool_size", 10)
    else:
        if int(pool_size) <= 0 or int(pool_size) > 100:
            warnings.warn("pool_size 有效范围为(0, 100]，设置的{}将不会生效".format(pool_size))
        else:
            conf["pool_size"] = pool_size

    compressor = kwargs.pop("compressor", None)
    if compressor is None:
        compressor = conf.get("compressor", None)
    else:
        conf["compressor"] = compressor

    page_size = kwargs.pop("page_size", None)
    if page_size is None:
        page_size = conf.get("page_size", 100000)
    else:
        if int(page_size) <= 0 or int(page_size) > 100000:
            warnings.warn("page_size 有效范围为(0, 100000]，设置的{}将不会生效".format(page_size))
        else:
            conf["page_size"] = page_size

    config = {
        "protocol": protocol,
        "auth": {
            "username": user,
            "password": pwd,
        },
        "request_timeout": timeout,
        "connect_timeout": con_timeout,
        "url": url,
        "pool_size": pool_size,
        "compressor": compressor,
        "page_size": page_size
    }
    if protocol == "HTTP":
        from hs_udata.utils.connection_pool import ConnectionPool
        global _CLIENT
        _CLIENT = ConnectionPool(config)
    else:
        raise RuntimeError("传输协议无效，got protocol[{}]".format(protocol))

    # 保存配置文件
    write_config({'system': conf})

    try:
        # 更新用户名和密码
        import operator
        if operator.ne(user, env.get("USERNAME")) or operator.ne(pwd, env.get("PASSWORD")):
            # 更新环境配置信息中的user和pwd
            cmd = r'setx hs_udata_CONF "{\"USERNAME\": \"%s\", \"PASSWORD\": \"%s\"}"' % (user, pwd)
            os.system(cmd)
    except:
        pass

def environ():
    """
    获取环境配置信息
    :return:
    """
    global _CLIENT
    if _CLIENT:
        return _CLIENT.config

    return {}
