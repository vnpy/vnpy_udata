from enum import Enum

# 服务交互字段定义
ERROR_NO = "error_no"    # 错误代码域
ERROR_INFO = "error_info"  # 错误信息域
DATA = "data"    # 数据域


class ConnectionStatus(Enum):                 #连接代码
    Disconnected = 0x0000       # 未连接
    Connecting = 0x0001,        # 正在连接
    Connected = 0x0002,         # 已连接
    SafeConnecting = 0x0004,    # 正在建立安全连接
    SafeConnected = 0x0008,     # 已建立安全连接
    Registering = 0x0010,       # 正注册
    Registered = 0x0020,        # 已注册
    Rejected = 0x0040           # 被拒绝，将被关闭


class Protocol(Enum):                 #连接类型
    HTTP = "HttpConnection"
    TCP = "TCPConnection"
