

__all__ = [
    "init",
    "environ",
    "get_data"
]


def init(username=None, password=None, **kwargs):
    """
    :param str username: 用户名，license模式下为'license'
    :param str password: 用户密码，license模式下为下发的license
    :param str protocol：传输协议，默认HTTP
    :param str url: 数据服务的URL
    :param int connect_timeout: 连接建立超时时间,默认5秒
    :param int timeout: 数据传输超时时间，默认30秒
    :param str compressor: 数据传输过程中的压缩算法，默认不使用
    :param int max_pool_size: 连接池大小，默认10
    :param int page_size: 数据请求分页大小，默认100000
    :return:
    """
    from hs_udata.utils.client import init as cms_init

    cms_init(username, password, **kwargs)
    return


def environ():
    """
    获取环境配置信息
    :return:
    """
    from hs_udata.utils.client import environ as cms_environ
    return cms_environ()


def get_data(method, **kwargs):
    """
    共用获取数据接口
    :param method:    接口名称
    :param kwargs:    接口参数
    """
    from hs_udata.utils.client import get_client

    return get_client().send(method, **kwargs)
