

class ConnectionException(Exception):
    pass


class ConnectionTimeOut(Exception):
    pass


class RequestTimeOut(Exception):
    pass


class RequestException(Exception):
    pass


class ServerException(Exception):
    pass


class GatewayException(Exception):
    pass


class ArgumentsVaildError(Exception):
    pass


class InvalidArgument(Exception):
    pass


ERROR_CHANNEL_BASE = 9100
GATEWAY_ERROR_DICT = {
    ERROR_CHANNEL_BASE + 1: "no timestamp field",
    ERROR_CHANNEL_BASE + 2: "error timestamp format",
    ERROR_CHANNEL_BASE + 3: "error timestamp",
    ERROR_CHANNEL_BASE + 4: "no signature head",
    ERROR_CHANNEL_BASE + 5: "unkown HTTP method",
    ERROR_CHANNEL_BASE + 6: "resty_sm3:new() failed",
    ERROR_CHANNEL_BASE + 7: "sm3:update() failed",
    ERROR_CHANNEL_BASE + 8: "error packet",
    ERROR_CHANNEL_BASE + 9: "no appkey head",
    ERROR_CHANNEL_BASE + 10: "redis not config, please check...",
    ERROR_CHANNEL_BASE + 11: "no getinfo_byself.lua or no get_secret_byself function in getinfo_byself.lua",
    ERROR_CHANNEL_BASE + 12: "no app_secret in redis or hget from redis timeout",
    ERROR_CHANNEL_BASE + 13: "authentication failure,no client_key in clients",
    ERROR_CHANNEL_BASE + 14: "authentication failure,ip not in whitelist",
    ERROR_CHANNEL_BASE + 15: "authentication failure,ip in blacklist",
    ERROR_CHANNEL_BASE + 16: "authentication failure,app_auth_type is nil",
    ERROR_CHANNEL_BASE + 17: "no client_id in body",
    ERROR_CHANNEL_BASE + 18: "no client_id in args",
    ERROR_CHANNEL_BASE + 19: "error client id",
    ERROR_CHANNEL_BASE + 20: "no client_id head",
    ERROR_CHANNEL_BASE + 21: "error packet,no data_value with get request",
    ERROR_CHANNEL_BASE + 22: "must json type",
    ERROR_CHANNEL_BASE + 23: "error packet,not data_value in post_args",
    ERROR_CHANNEL_BASE + 24: "error packet,not data_value in header or args"
}

ERROR_SERVER_BASE = 100000
SERVER_ERROR_DICT = {
    ERROR_SERVER_BASE + 0: "发生异常",
    ERROR_SERVER_BASE + 1: "参数[{0}]解析失败!",
    ERROR_SERVER_BASE + 2: "请求方式不符,该api为{0}请求",
    ERROR_SERVER_BASE + 3: "参数[{0}]类型转换失败",
    ERROR_SERVER_BASE + 4: "数据库连接失败[{0}]",
    ERROR_SERVER_BASE + 5: "该语句不包含select关键字!",
    ERROR_SERVER_BASE + 6: "执行模式错误!",
    ERROR_SERVER_BASE + 7: "该数据库类型不支持!",
    ERROR_SERVER_BASE + 8: "查询失败:[{0}]",
    ERROR_SERVER_BASE + 9: "该引擎不支持!",
    ERROR_SERVER_BASE + 10: "查询失败",
    ERROR_SERVER_BASE + 11: "参数[{0}]不能为空",
    ERROR_SERVER_BASE + 12: "驱动找不到,{0}",
    ERROR_SERVER_BASE + 13: "该数据库不支持统一分页,请自行使用sql语句分页",
    ERROR_SERVER_BASE + 14: "数据推送失败{0}",
    ERROR_SERVER_BASE + 15: "暂不支持get请求",
    ERROR_SERVER_BASE + 16: "csv文件写入失败",
    ERROR_SERVER_BASE + 17: "ftp文件上传失败",
    ERROR_SERVER_BASE + 18: "暂不支持该输出通道",
    ERROR_SERVER_BASE + 19: "kerberos认证失败[{0}]",
    ERROR_SERVER_BASE + 20: "kerberos认证失败,文件[{0}]不存在",
    ERROR_SERVER_BASE + 24: "ftp文件上传失败,登录失败!",
    ERROR_SERVER_BASE + 25: "ftp连接失败!",
    ERROR_SERVER_BASE + 26: "通知发送失败!",
    ERROR_SERVER_BASE + 27: "请求格式错误",
    ERROR_SERVER_BASE + 28: "ftp创建文件夹[{}]失败!",
    ERROR_SERVER_BASE + 29: "数据源{0}下的数据表{1}不存在"
}

