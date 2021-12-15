from datetime import datetime, timedelta
from typing import List, Optional
from pytz import timezone

from hs_udata import set_token, fut_quote_minute, stock_quote_minutes
from pandas import DataFrame

from vnpy.trader.setting import SETTINGS
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.object import BarData, HistoryRequest
from vnpy.trader.datafeed import BaseDatafeed
from time import sleep


EXCHANGE_VT2UDATA = {
    Exchange.CFFEX: "CFE",
    Exchange.SHFE: "SHF",
    Exchange.DCE: "DCE",
    Exchange.CZCE: "CZC",
    Exchange.INE: "INE",
    Exchange.SSE: "SH",
    Exchange.SZSE: "SZ"
}

INTERVAL_VT2RQ = {
    Interval.MINUTE: "1m",
    Interval.HOUR: "60m",
    Interval.DAILY: "1d",
}

INTERVAL_ADJUSTMENT_MAP = {
    Interval.MINUTE: timedelta(minutes=1),
    Interval.HOUR: timedelta(hours=1),
    Interval.DAILY: timedelta()         # no need to adjust for daily bar
}

CHINA_TZ = timezone("Asia/Shanghai")


def convert_symbol(symbol: str, exchange: Exchange) -> str:
    """将交易所代码转换为UData代码"""
    exchange_str = EXCHANGE_VT2UDATA.get(exchange, "")
    return f"{symbol.upper()}.{exchange_str}"


class UdataDatafeed(BaseDatafeed):
    """恒生UData数据服务接口"""

    def __init__(self):
        """"""
        self.token: str = SETTINGS["datafeed.password"]

        self.inited: bool = False

    def init(self) -> bool:
        """初始化"""
        set_token(self.token)
        self.inited = True
        return True

    def query_bar_history(self, req: HistoryRequest) -> Optional[List[BarData]]:
        if not self.inited:
            self.init()

        # 只支持分钟线
        if req.interval != Interval.MINUTE:
            return None

        data: List[BarData] = []
        
        end = req.end.date()

        while True:
            # 期货
            if req.exchange in { 
                Exchange.CFFEX,
                Exchange.SHFE,
                Exchange.CZCE,
                Exchange.DCE,
                Exchange.INE
            }:
                temp_data = self.query_futures_bar_history(req)
                
                data.extend(temp_data)
                if temp_data[-1].datetime.date() >= end or len(temp_data) != 10000:
                    break
                req.start = temp_data[-1].datetime
                sleep(3)
            # 股票
            elif req.exchange in {
                Exchange.SSE,
                Exchange.SZSE
            }:
                temp_data = self.query_equity_bar_history(req)
                
                data.extend(temp_data)
                if temp_data[-1].datetime.date() >= end or len(temp_data) != 10000:
                    break
                req.start = temp_data[-1].datetime
                sleep(3)
            # 其他
            else:
                return None
        return data

    def query_futures_bar_history(self, req: HistoryRequest) -> Optional[List[BarData]]:
        """查询期货分钟K线数据"""
        symbol = req.symbol
        exchange = req.exchange
        interval = req.interval
        start = req.start
        end = req.end

        udata_symbol = convert_symbol(symbol, exchange)
        adjustment = timedelta(minutes=1)

        df: DataFrame = fut_quote_minute(
            en_prod_code=udata_symbol,
            begin_date=start.strftime("%Y-%m-%d"),
            end_date=end.strftime("%Y-%m-%d")
        )

        data: List[BarData] = []

        if len(df):
            for _, row in df.iterrows():
                timestr = f"{row.date} {str(row.time).rjust(4, '0')}"
                dt = datetime.strptime(timestr, "%Y-%m-%d %H%M") - adjustment
                dt = CHINA_TZ.localize(dt)

                bar = BarData(
                    symbol=symbol,
                    exchange=exchange,
                    interval=interval,
                    datetime=dt,
                    open_price=row.open,
                    high_price=row.high,
                    low_price=row.low,
                    close_price=row.close,
                    volume=row.turnover_volume,
                    turnover=row.turnover_value,
                    open_interest=row.amount,
                    gateway_name="UDATA"
                )

                data.append(bar)

        return data

    def query_equity_bar_history(self, req: HistoryRequest) -> Optional[List[BarData]]:
        """查询股票分钟K线数据"""
        symbol = req.symbol
        exchange = req.exchange
        interval = req.interval
        start = req.start
        end = req.end

        udata_symbol = convert_symbol(symbol, exchange)
        adjustment = timedelta(minutes=1)

        df: DataFrame = stock_quote_minutes(
            en_prod_code=udata_symbol,
            begin_date=start.strftime("%Y-%m-%d"),
            end_date=end.strftime("%Y-%m-%d")
        )

        data: List[BarData] = []

        if len(df):
            for _, row in df.iterrows():
                timestr = f"{row.date} {str(row.time).rjust(4, '0')}"
                dt = datetime.strptime(timestr, "%Y-%m-%d %H%M") - adjustment
                dt = CHINA_TZ.localize(dt)

                bar = BarData(
                    symbol=symbol,
                    exchange=exchange,
                    interval=interval,
                    datetime=dt,
                    open_price=row.open,
                    high_price=row.high,
                    low_price=row.low,
                    close_price=row.close,
                    volume=row.turnover_volume,
                    turnover=row.turnover_value,
                    gateway_name="UDATA"
                )

                data.append(bar)

        return data


