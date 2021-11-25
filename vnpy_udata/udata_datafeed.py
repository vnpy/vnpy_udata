from datetime import datetime, timedelta
from typing import List, Optional
from pytz import timezone

from hs_udata import set_token, fut_quote_minute, stock_quote_minutes
from pandas import DataFrame

from vnpy.trader.setting import SETTINGS
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.object import BarData, HistoryRequest
from vnpy.trader.datafeed import BaseDatafeed


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
        """查询K线数据"""
        if not self.inited:
            self.init()

        # 只支持分钟线
        if req.interval != Interval.MINUTE:
            return None

        # 期货
        if req.exchange in {
            Exchange.CFFEX,
            Exchange.SHFE,
            Exchange.CZCE,
            Exchange.DCE,
            Exchange.INE
        }:
            return self.query_futures_bar_history(req)
        # 股票
        elif req.exchange in {
            Exchange.SSE,
            Exchange.SZSE
        }:
            return self.query_equity_bar_history(req)
        # 其他
        else:
            return None

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
                    open_price=float(row.open),
                    high_price=float(row.high),
                    low_price=float(row.low),
                    close_price=float(row.close),
                    volume=float(row.turnover_volume),
                    turnover=float(row.turnover_value),
                    open_interest=float(row.amount),
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
                    open_price=float(row.open),
                    high_price=float(row.high),
                    low_price=float(row.low),
                    close_price=float(row.close),
                    volume=float(row.turnover_volume),
                    turnover=float(row.turnover_value),
                    gateway_name="UDATA"
                )

                data.append(bar)

        return data
