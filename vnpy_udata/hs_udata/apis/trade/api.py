# -*- coding: UTF-8 -*-
import warnings
import pandas as pd
import datetime
import time

from hs_udata.apis.base import get_data
from hs_udata.utils.datetime_func import convert_date
from hs_udata.utils.decorators import args_check, check
from hs_udata.utils.convert import convert_param, convert_fields


__all__ = [
    "trading_calendar1",
]


@args_check(
    check("secu_market").is_instance((str, None.__class__)),
    check("if_trading_day").is_instance((str, None.__class__)),
    check("if_week_end").is_instance((str, None.__class__)),
    check("if_month_end").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__))
)
def trading_calendar1(secu_market="83", if_trading_day=None, if_week_end=None, if_month_end=None, start_date=datetime.datetime.now().replace(year=datetime.datetime.now().year-1).date().strftime("%Y%m%d"), end_date=datetime.datetime.now().date().strftime("%Y%m%d")):
    """
    交易日历

    输入参数：
    :param str secu_market : 证券市场，默认"83"
    :param str if_trading_day : 是否交易日
    :param str if_week_end : 是否周末
    :param str if_month_end : 是否月末
    :param str start_date : 开始日期，默认"last_year_today"
    :param str end_date : 截止日期，默认"now"

    输出参数：
    :param str if_trading_day : 是否交易日,
    :param str if_week_end : 是否周末,
    :param str if_month_end : 是否月末,
    :param str secu_market : 证券市场,
    :param str trading_date : 日期,

    代码调用:
        from hs_udata import trading_calendar
trading_calendar() 

    结果输出:
         if_trading_day if_week_end  if_month_end \
0 是 否 否
1 是 否 否
...
    """

    int_param =[]
    float_param =[]
    params = {
        "secu_market": secu_market,
        "if_trading_day": if_trading_day,
        "if_week_end": if_week_end,
        "if_month_end": if_month_end,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("trading_calendar1", **params)


