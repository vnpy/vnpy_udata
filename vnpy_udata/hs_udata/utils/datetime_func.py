# -*- coding: utf-8 -*-
import datetime


def convert_date(dt, now=True):
    # if dt == "":    #时间为空时返回当前时间或19900101
    #     if now:
    #         return datetime.datetime.now().date().strftime("%Y%m%d")
    #     else:
    #         return "19900101""19900101"
    if dt == None:
        return

    if isinstance(dt, datetime.datetime):       #datetime类型数据进行数据转换成固定格式
        return dt.date().strftime("%Y%m%d")

    if isinstance(dt, datetime.date):          #datetime.date数据类型转换为固定格式
        return dt.strftime("%Y%m%d")

    if isinstance(dt, str):
        from dateutil.parser import parse
        return parse(dt).date().strftime("%Y%m%d")    #用parse进行格式转换，变成数据类型

    if hasattr(dt, "to_pydatetime"):                  #判断一个对象里面是否有"to_pydatetime"属性或者"to_pydatetime"方法
        return dt.to_pydatetime().date().strftime("%Y%m%d")

    if hasattr(dt, "dtype") and dt.dtype.char == "M":    #M表示带分钟的dtype类型
        from dateutil.parser import parse
        return parse(dt).date().strftime("%Y%m%d")

    raise ValueError("转换日期格式异常，实参为[{}]".format(dt))        #不在上述所列类型抛出异常