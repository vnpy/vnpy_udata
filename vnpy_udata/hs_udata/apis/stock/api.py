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
    "stock_list",
    "trading_calendar",
    "ipo_list",
    "company_profile",
    "stock_Info",
    "leader_profile",
    "st_stock_list",
    "shszhk_stock_list",
    
    "stock_quote_daily",
    "stock_quote_weekly",
    "stock_quote_monthly",
    "stock_quote_yearly",
    "money_flow",
    "suspension_list",
    "shareholder_top10",
    "float_shareholder_top10",
    "lh_daily",
    "lh_stock",
    "stock_quote_minutes",
    "shszhk_capitalflow",
    "shszhk_deal_top10",
    "shszhk_distribution",
    "shszhk_change_top10",
    "quote_stocklist",
    
    "industry_category",
    "index_constituent",
    "org_hold",
    "holder_num",
    "restricted_schedule",
    "holder_pledge",
    "holder_increase",
    "pledge_repo",
    "stock_pledge",
    "block_trade",
    "margin_trading",
    "interval_margin_trading",
    "margin_trade_detail",
    "margin_trade_total",
    "stock_dividend",
    "stock_additional",
    "stock_additional_all",
    "stock_allotment",
    "stock_asforecastabb",
    "stock_asunderweight",
    "stock_asoverweight",
    "stock_asrighttransfer",
    "stock_asraising",
    
    "schedule_disclosure",
    "stock_key_indicator",
    "accounting_data",
    "financial_cashflow",
    "financial_income",
    "financial_balance",
    "financial_gene_qincome",
    "financial_bank_qincome",
    "financial_secu_qincome",
    "financial_insu_qincome",
    "financial_gene_qcashflow",
    "financial_bank_qcashflow",
    "financial_secu_qcashflow",
    "financial_insu_qcashflow",
    "performance_forecast",
    "performance_letters",
    "performance_letters_q",
    "main_composition",
    "trading_parties",
    "audit_opinion",
    "per_share_index",
    "profitability",
    "growth_capacity",
    "du_pont_analysis",
    "deri_fin_indicators",
    "q_financial_indicator",
    "valuation_info",
    "corporation_value",
    
    "star_ipodeclare",
    "star_companyprofile",
    
    "neeq_basic",
    "neeq_company",
    "neeq_leader",
    "neeq_leader_num",
    "neeq_industry",
    
    "fund_list",
    "fund_manager_company",
    "fund_manager",
    "fund_profile",
    "fund_institutions",
    "fund_etf",
    "fund_size",
    "fund_charge_rate",
    "fund_index",
    "fund_type",
    "fund_style",
    "fund_holder_public",
    
    "fund_quote_daily_history",
    "fund_quote_daily",
    "fund_quote_weekly",
    "fund_quote_monthly",
    "fund_quote_yearly",
    "fund_net_value",
    "moneyfund_performance",
    "fund_stock_detail",
    "fund_asset",
    "fund_holder",
    "fund_rangerise",
    "fund_rank",
    
    "fut_basic",
    "fut_quote_minute",
    "fut_list",
    "fut_count_rank",
    "fut_holding_lh",
    "fut_contract_type",
    
    "con_price",
    "con_time",
    "con_detail",
    "con_calender",
    
    "hk_list",
    "hk_ipo",
    "hk_company",
    "hk_secu",
    "hk_leader",
    
    "hk_daily_quote",
    "hk_weekly_quote",
    "hk_monthly_quote",
    "hk_yearly_quote",
    "hk_section_quote",
    "hk_daily_quote_short",
    "hk_weekly_quote_short",
    "hk_monthly_quote_short",
    "hk_yearly_quote_short",
    "hk_section_quote_short",
    "hk_minutes_hkscclist",
    "hk_minutes_hkscc",
    
    "hk_share_stru",
    "hk_exgindustry",
    "hk_cap_structure",
    "hk_profit_ability",
    "hk_per_share_index",
    "hk_solvency",
    "hk_mainincomestru",
    "hk_dividend",
    "hk_buyback",
    
]


@args_check(
    check("listed_state").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_list(listed_state=None, fields=None):
    """
    记录A股上市、退市股票交易代码、股票名称、上市状态等信息；

    输入参数：
    :param str listed_state : 上市状态
    :param str fields : 字段集合

    输出参数：
    :param str secu_abbr : 证券简称,
    :param str chi_name : 中文名称,
    :param str listed_state : 上市状态,
    :param str secu_code : 证券代码,
    :param str secu_market : 证券市场,
    :param str listed_sector : 上市板块,
    :param str hs_code : HS代码,

    代码调用:
        from hs_udata import stock_list
stock_list() 

    结果输出:
         secu_abbr chi_name  listed_state \
0 平安银行 平安银行股份有限公司 上市
1 万科Ａ 万科企业股份有限公司 上市
…
    """

    int_param =[]
    float_param =[]
    params = {
        "listed_state": listed_state,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_list", url_path="basic_data", **params)

@args_check(
    check("secu_market").is_instance((str, None.__class__)),
    check("if_trading_day").is_instance((str, None.__class__)),
    check("if_week_end").is_instance((str, None.__class__)),
    check("if_month_end").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def trading_calendar(secu_market=None, if_trading_day=None, if_week_end=None, if_month_end=None, start_date=None, end_date=None, fields=None):
    """
    交易日信息，包括每个日期是否是交易日，是否周、月最后一个交易日；最大可返回1年的交易日信息；

    输入参数：
    :param str secu_market : 证券市场，默认"83"
    :param str if_trading_day : 是否交易日
    :param str if_week_end : 是否周末
    :param str if_month_end : 是否月末
    :param str start_date : 开始日期，默认"last_year_today"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

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
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("trading_calendar", url_path="basic_data", **params)

@args_check(
    check("start_date").is_instance((str, None.__class__)),
    check("secu_market").is_instance((str, None.__class__)),
    check("listed_sector").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def ipo_list(start_date=None, secu_market=None, listed_sector=None, fields=None):
    """
    提供已上市新股代码，名称，发行数量、申购和配售等新股信息；

    输入参数：
    :param str start_date : 开始日期，默认"now"
    :param str secu_market : 上市市场
    :param str listed_sector : 上市板块
    :param str fields : 字段集合

    输出参数：
    :param str prod_name : 产品名称,
    :param str prod_code : 产品代码,
    :param str secu_code : 证券代码,
    :param str secu_market : 证券市场,
    :param str secu_abbr : 证券简称,
    :param str prospectus_date : 发行日期,
    :param str listed_date : 上市日期,
    :param float issue_price : 发行价(元),
    :param float diluted_pe_ratio : 发行市盈率(全面摊薄),
    :param float allot_max : 申购上限(股),
    :param int lot_rate_online : 发行中签率,
    :param float worth_value : 市值,
    :param float issue_vol : 发行数量(股),
    :param str indurstry : 所属行业,
    :param float naps : 每股净资产(元),
    :param int issue_amount : 发行数量,
    :param float lucky_rate : 配售中签率,
    :param float valid_apply_vol_online : 网上发行有效申购总量(股),
    :param int valid_apply_num_online : 网上发行有效申购户数(户),
    :param float valid_apply_vol_lp : 配售有效申购总量(股),
    :param int valid_apply_num_lp : 配售有效申购户数(户),
    :param float over_subs_times_online : 网上发行超额认购倍数(倍),
    :param float over_subs_times_lp : 配售超额认购倍数(倍),
    :param float listed_sector : 上市板块,
    :param float secu_category : 证券类型,
    :param str allocation_date : 中签号公布日,
    :param float esti_allot_max : 预估申购上限,
    :param float allot_min : 申购下限,
    :param float esti_issue_price : 预估发行价,
    :param float naps_after : 每股净资产(元),
    :param int issue_system_type : 发行制度类型,

    代码调用:
        from hs_udata import ipo_list
ipo_list() 

    结果输出:
        
    """

    int_param =['lot_rate_online', 'issue_amount', 'valid_apply_num_online', 'valid_apply_num_lp', 'issue_system_type']
    float_param =['issue_price', 'diluted_pe_ratio', 'allot_max', 'worth_value', 'issue_vol', 'naps', 'lucky_rate', 'valid_apply_vol_online', 'valid_apply_vol_lp', 'over_subs_times_online', 'over_subs_times_lp', 'listed_sector', 'secu_category', 'esti_allot_max', 'allot_min', 'esti_issue_price', 'naps_after']
    params = {
        "start_date": convert_date(start_date),
        "secu_market": secu_market,
        "listed_sector": listed_sector,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("ipo_list", url_path="basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def company_profile(en_prod_code=None, fields=None):
    """
    获取公司的基本信息，包含公司名称、注册信息、公司属性、所在城市、联系电话、实际控制人等内容；

    输入参数：
    :param str en_prod_code : 股票代码，默认"600570.SH"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 股票代码,
    :param str chi_name : 公司中文名称,
    :param str eng_name : 公司英文名称,
    :param str company_pro : 公司属性,
    :param str establishment_date : 成立日期,
    :param str legal_repr : 法定代表人,
    :param str city_code : 城市,
    :param str reg_addr : 公司注册地址,
    :param str officeaddress : 公司办公地址,
    :param str officezip : 邮编,
    :param str tel : 联系电话,
    :param str email : 电子邮件,
    :param str website : 公司网址,
    :param str secu_affairs_repr : 公司披露人,
    :param str business_reg_number : 工商登记号,
    :param int regcapital : 注册资本,
    :param str state : 省份,
    :param str fax : 传真,
    :param str uniform_social_credit_code : 统一社会信用代码,
    :param int employee_sum : 员工总数,
    :param str controller_name : 实际控制人,

    代码调用:
        from hs_udata import company_profile
company_profile() 

    结果输出:
        
    """

    int_param =['regcapital', 'employee_sum']
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("company_profile", url_path="basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_Info(en_prod_code=None, trading_date=None, fields=None):
    """
    获取股票的基本信息，包含股票交易代码、股票简称、上市时间、上市状态、所属概念板块等信息；

    输入参数：
    :param str en_prod_code : 内部编码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 股票代码,
    :param str secu_abbr : 股票简称,
    :param str eng_name_abbr : 股票英文名称,
    :param str list_date : 上市时间,
    :param str secu_market : 上市地点,
    :param int par_value : 股票面值,
    :param str isin_code : ISIN代码,
    :param str hstock_code : 同公司H股代码,
    :param str hshare_abbr : 同公司H股简称,
    :param str bstock_code : 同公司B股代码,
    :param str bshare_abbr : 同公司B股简称,
    :param str secu_code : 证券编码,
    :param str listed_sector : 上市板块,
    :param str concept_board : 所属概念板块,
    :param str change_type : 证券存续状态,
    :param int sh_hk_flag : 是否沪港通标的,
    :param int sz_hk_flag : 是否深港通标的,
    :param str en_prod_code : 股票代码,

    代码调用:
        from hs_udata import stock_Info
stock_Info() 

    结果输出:
        
    """

    int_param =['par_value', 'sh_hk_flag', 'sz_hk_flag']
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_Info", url_path="basic_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("position_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def leader_profile(secu_code=None, position_type=None, fields=None):
    """
    高管基本信息，高管领导人简介、姓名、学历、职位、年度报酬等（包括科创板）；

    输入参数：
    :param str secu_code : 证券代码，默认"600570"
    :param str position_type : 职位类型，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 股票代码,
    :param str secu_abbr : 股票简称,
    :param str secu_market : 证券市场,
    :param str position_type : 职位类型,
    :param str leader_name : 领导人姓名,
    :param int position : 职位,
    :param str begin_date : 任职起始日,
    :param str birthday : 出生年月,
    :param str leader_degree : 学历程度,
    :param str newest_hold : 最新持股数,
    :param str shareholding_ratio : 持股比例,
    :param str end_date : 年度报酬报告期,
    :param int annual_reward : 年度报酬,

    代码调用:
        from hs_udata import leader_profile
leader_profile() 

    结果输出:
        
    """

    int_param =['position', 'annual_reward']
    float_param =[]
    params = {
        "secu_code": secu_code,
        "position_type": position_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("leader_profile", url_path="basic_data", **params)

@args_check(
    check("secu_market").is_instance((str, None.__class__)),
    check("secu_category").is_instance((str, None.__class__)),
    check("listed_sector").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def st_stock_list(secu_market=None, secu_category=None, listed_sector=None, fields=None):
    """
    当前ST及*ST的股票代码列表

    输入参数：
    :param str secu_market : 证券市场
    :param str secu_category : 证券类型
    :param str listed_sector : 上市板块
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str chi_name : 公司名称,
    :param str secu_market : 证券市场,
    :param str secu_category : 证券类型,
    :param str listed_sector : 上市板块,

    代码调用:
        from hs_udata import st_stock_list
st_stock_list() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "secu_market": secu_market,
        "secu_category": secu_category,
        "listed_sector": listed_sector,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("st_stock_list", url_path="basic_data", **params)

@args_check(
    check("etfcomponent_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def shszhk_stock_list(etfcomponent_type=None, fields=None):
    """
    ‘沪股通’和‘港股通（沪）’各自的成分股。 “深股通”和“港股通（深）”各自的成分股。 更新频率： 不定时更新 

    输入参数：
    :param str etfcomponent_type : 成分股类别，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str etfcomponent_type : 成分股类别,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_category : 证券类别,
    :param str secu_market : 证券市场,
    :param str select_time : 入选股票时间,

    代码调用:
        from hs_udata import shszhk_stock_list
shszhk_stock_list() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "etfcomponent_type": etfcomponent_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("shszhk_stock_list", url_path="basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance(int),
    check("fields").is_instance((str, None.__class__))
)
def stock_quote_daily(en_prod_code=None, trading_date=None, adjust_way=0, fields=None):
    """
    沪深日行情，包含昨收价、开盘价、最高价、最低价、收盘价、成交量、成交金额等数据；

    输入参数：
    :param str en_prod_code : 证券代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"now"
    :param int adjust_way : 复权方式，默认0
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证券代码,
    :param str trading_date : 交易日期,
    :param float prev_close_price : 前收盘价,
    :param float open_price : 开盘价,
    :param float high_price : 最高价,
    :param float low_price : 最低价,
    :param float close_price : 收盘价,
    :param str avg_price : 变动均价,
    :param float px_change : 价格涨跌,
    :param float px_change_rate : 涨跌幅,
    :param float turnover_ratio : 换手率,
    :param float business_balance : 成交额,
    :param float turnover_deals : 成交笔数,
    :param float amplitude : 振幅,
    :param float issue_price_change : 相对发行价涨跌,
    :param float issue_price_change_rate : 相对发行价涨跌幅（%）,
    :param str recently_trading_date : 最近交易日期,
    :param float ratio_adjust_factor : 复权因子,
    :param float business_amount : 成交数量,
    :param str up_down_status : 涨跌停状态,
    :param str turnover_status : 交易状态,

    代码调用:
        from hs_udata import stock_quote_daily
stock_quote_daily() 

    结果输出:
        
    """

    int_param =[]
    float_param =['prev_close_price', 'open_price', 'high_price', 'low_price', 'close_price', 'px_change', 'px_change_rate', 'turnover_ratio', 'business_balance', 'turnover_deals', 'amplitude', 'issue_price_change', 'issue_price_change_rate', 'ratio_adjust_factor', 'business_amount']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "adjust_way": adjust_way,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_quote_daily", url_path="market_info", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance(int),
    check("fields").is_instance((str, None.__class__))
)
def stock_quote_weekly(en_prod_code=None, trading_date=None, adjust_way=0, fields=None):
    """
    沪深周行情，包含上周收价、周开盘价、周最高价、周最低价、周收盘价、周成交量、周成交金额等数据；

    输入参数：
    :param str en_prod_code : 证券代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"now"
    :param int adjust_way : 复权方式，默认0
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float week_prev_close_price : 周前收盘价,
    :param float week_open_price : 周开盘价,
    :param float week_high_price : 周最高价,
    :param float week_low_price : 周最低价,
    :param float week_close_price : 周收盘价,
    :param float week_max_close_price : 周最高收盘价,
    :param float week_min_close_price : 周最低收盘价,
    :param float week_avg_close_price : 周均价,
    :param float week_avg_business_balance : 周日均成交额,
    :param float week_avg_business_amount : 周日均成交量,
    :param float week_px_change : 周涨跌,
    :param float week_px_change_rate : 周涨跌幅（%）,
    :param float week_turnover_ratio : 周换手率（%）,
    :param float week_avg_turnover_ratio : 周日平均换手率（%）,
    :param float week_business_amount : 周成交量,
    :param float week_business_balance : 周成交额,
    :param float week_amplitude : 周振幅（%）,
    :param str week_high_price_date : 周最高价日,
    :param str week_low_price_date : 周最低价日,
    :param str week_max_close_price_date : 周最高收盘价日,
    :param str week_min_close_price_date : 周最低收盘价日,

    代码调用:
        from hs_udata import stock_quote_weekly
stock_quote_weekly() 

    结果输出:
        
    """

    int_param =[]
    float_param =['week_prev_close_price', 'week_open_price', 'week_high_price', 'week_low_price', 'week_close_price', 'week_max_close_price', 'week_min_close_price', 'week_avg_close_price', 'week_avg_business_balance', 'week_avg_business_amount', 'week_px_change', 'week_px_change_rate', 'week_turnover_ratio', 'week_avg_turnover_ratio', 'week_business_amount', 'week_business_balance', 'week_amplitude']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "adjust_way": adjust_way,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_quote_weekly", url_path="market_info", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance(int),
    check("fields").is_instance((str, None.__class__))
)
def stock_quote_monthly(en_prod_code=None, trading_date=None, adjust_way=0, fields=None):
    """
    沪深月行情，包含月前收盘价、月开盘价、月最高价、月最低价、月收盘价、月成交量、月成交金额等数据；

    输入参数：
    :param str en_prod_code : 证券代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"now"
    :param int adjust_way : 复权方式，默认0
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float month_prev_close_price : 月前收盘价,
    :param float month_open_price : 月开盘价,
    :param float month_high_price : 月最高价,
    :param float month_low_price : 月最低价,
    :param float month_close_price : 月收盘价,
    :param float month_max_close_price : 月最高收盘价,
    :param float month_min_close_price : 月最低收盘价,
    :param float month_avg_close_price : 月均价,
    :param float month_avg_business_balance : 月日均成交额,
    :param float month_avg_business_amount : 月日均成交量,
    :param float month_px_change : 月涨跌,
    :param float month_px_change_rate : 月涨跌幅（%）,
    :param float month_turnover_ratio : 月换手率（%）,
    :param float month_avg_turnover_ratio : 月日平均换手率（%）,
    :param float month_business_amount : 月成交量,
    :param float month_business_balance : 月成交额,
    :param float month_amplitude : 月振幅（%）,
    :param str month_high_price_date : 月最高价日,
    :param str month_low_price_date : 月最低价日,
    :param str month_max_close_price_date : 月最高收盘价日,
    :param str month_min_close_price_date : 月最低收盘价日,

    代码调用:
        from hs_udata import stock_quote_monthly
stock_quote_monthly() 

    结果输出:
        
    """

    int_param =[]
    float_param =['month_prev_close_price', 'month_open_price', 'month_high_price', 'month_low_price', 'month_close_price', 'month_max_close_price', 'month_min_close_price', 'month_avg_close_price', 'month_avg_business_balance', 'month_avg_business_amount', 'month_px_change', 'month_px_change_rate', 'month_turnover_ratio', 'month_avg_turnover_ratio', 'month_business_amount', 'month_business_balance', 'month_amplitude']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "adjust_way": adjust_way,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_quote_monthly", url_path="market_info", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance(int),
    check("fields").is_instance((str, None.__class__))
)
def stock_quote_yearly(en_prod_code=None, trading_date=None, adjust_way=0, fields=None):
    """
    沪深年行情信息，包含年前收盘价、年最高价、年最低价、年日均成交量、年涨跌幅等数据；

    输入参数：
    :param str en_prod_code : 证券代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"now"
    :param int adjust_way : 复权方式，默认0
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float year_prev_close_price : 年前收盘价,
    :param float year_open_price : 年开盘价,
    :param float year_high_price : 年最高价,
    :param float year_low_price : 年最低价,
    :param float year_close_price : 年收盘价,
    :param float year_max_close_price : 年最高收盘价,
    :param float year_min_close_price : 年最低收盘价,
    :param float year_avg_close_price : 年均价,
    :param float year_avg_business_balance : 年日均成交额,
    :param float year_avg_business_amount : 年日均成交量,
    :param float year_px_change : 年涨跌,
    :param float year_px_change_rate : 年涨跌幅（%）,
    :param float year_turnover_ratio : 年换手率（%）,
    :param float year_avg_turnover_ratio : 年日平均换手率（%）,
    :param float year_business_amount : 年成交量,
    :param str year_business_balance : 本年金额,
    :param float year_amplitude : 年振幅（%）,
    :param str year_high_price_date : 年最高价日,
    :param str year_low_price_date : 年最低价日,
    :param str year_max_close_price_date : 年最高收盘价日,
    :param str year_min_close_price_date : 年最低收盘价日,

    代码调用:
        from hs_udata import stock_quote_yearly
stock_quote_yearly() 

    结果输出:
        
    """

    int_param =[]
    float_param =['year_prev_close_price', 'year_open_price', 'year_high_price', 'year_low_price', 'year_close_price', 'year_max_close_price', 'year_min_close_price', 'year_avg_close_price', 'year_avg_business_balance', 'year_avg_business_amount', 'year_px_change', 'year_px_change_rate', 'year_turnover_ratio', 'year_avg_turnover_ratio', 'year_business_amount', 'year_amplitude']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "adjust_way": adjust_way,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_quote_yearly", url_path="market_info", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def money_flow(en_prod_code=None, trading_date=None, fields=None):
    """
    获取单个交易日，沪深股票在不同单笔成交金额区间的累计主买、主卖金额及成交量数据；

    输入参数：
    :param str en_prod_code : 证券代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证券代码,
    :param str trading_date : 交易日期,
    :param float turnover_in : 流入成交额,
    :param float turnover_out : 流出成交额,
    :param float net_turnover_in : 资金净流入额,
    :param float amount_in : 流入成交量,
    :param float amount_out : 流出成交量,
    :param float net_amount_in : 净流入量,
    :param float super_in : 超大单流入,
    :param float super_amount_in : 主动买入特大单成交量,
    :param float large_in : 大单流入,
    :param float large_amount_in : 主动买入大单成交量,
    :param float medium_in : 中单流入,
    :param float medium_amount_in : 主动买入中单成交量,
    :param float little_in : 小单流入,
    :param float little_amount_in : 主动买入小单成交量,
    :param float super_out : 超大单流出,
    :param float super_amount_out : 主动卖出特大单成交量,
    :param float large_out : 大单流出,
    :param float large_amount_out : 主动卖出大单成交量,
    :param float medium_out : 中单流出,
    :param float medium_amount_out : 主动卖出中单成交量,
    :param float little_out : 小单流出,
    :param float little_amount_out : 主动卖出小单成交量,

    代码调用:
        from hs_udata import money_flow
money_flow() 

    结果输出:
        
    """

    int_param =[]
    float_param =['turnover_in', 'turnover_out', 'net_turnover_in', 'amount_in', 'amount_out', 'net_amount_in', 'super_in', 'super_amount_in', 'large_in', 'large_amount_in', 'medium_in', 'medium_amount_in', 'little_in', 'little_amount_in', 'super_out', 'super_amount_out', 'large_out', 'large_amount_out', 'medium_out', 'medium_amount_out', 'little_out', 'little_amount_out']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("money_flow", url_path="market_info", **params)

@args_check(
    check("suspensiondate").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def suspension_list(suspensiondate=None, fields=None):
    """
    上市公司股票停牌复牌信息；

    输入参数：
    :param str suspensiondate : 停牌日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 股票代码,
    :param str secu_abbr : 股票简称,
    :param str suspend_date : 停牌日期,
    :param str suspend_time : 停牌时间,
    :param str resumption_date : 复牌日期,
    :param str resumption_time : 复牌时间,
    :param str suspend_reason : 停牌原因,

    代码调用:
        from hs_udata import suspension_list
suspension_list() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "suspensiondate": suspensiondate,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("suspension_list", url_path="market_info", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def shareholder_top10(secu_code=None, start_date=None, end_date=None, fields=None):
    """
    获取公司十大股东相关数据，包括主要股东构成及持股数量比例、持股性质；

    输入参数：
    :param str secu_code : 证券代码，默认"600570"
    :param str start_date : 开始日期，默认"last_year_today"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str secu_market : 证券市场,
    :param str secu_code : 证券代码,
    :param float secu_abbr : 证券简称,
    :param float trading_date : 交易日期,
    :param float info_source : 信息来源,
    :param float hold_vols : 合计持有股份总数（万股）,
    :param float total_rates : 合计占总股本比例（%）,
    :param float controller_name : 实际控制人,
    :param float serial_number : 股东序号,
    :param float stock_holder_name : 股东名称,
    :param float stock_holder_kind : 股东性质,
    :param float share_character_statement : 股本性质,
    :param float hold_vol : 持股份总数（万股）,
    :param float total_rate : 占总股本比例(%),
    :param float hold_vol_change : 较上期持股变动股数(万股),
    :param float total_rate_change : 较上期变动比例(%),
    :param float aas_change_type : 变动类别,

    代码调用:
        from hs_udata import shareholder_top10
shareholder_top10() 

    结果输出:
        
    """

    int_param =[]
    float_param =['secu_abbr', 'trading_date', 'info_source', 'hold_vols', 'total_rates', 'controller_name', 'serial_number', 'stock_holder_name', 'stock_holder_kind', 'share_character_statement', 'hold_vol', 'total_rate', 'hold_vol_change', 'total_rate_change', 'aas_change_type']
    params = {
        "secu_code": secu_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("shareholder_top10", url_path="market_info", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def float_shareholder_top10(secu_code=None, start_date=None, end_date=None, fields=None):
    """
    获取公司十大流通股东相关数据，包括主要股东构成及持股数量比例、持股性质；

    输入参数：
    :param str secu_code : 证券代码，默认"600570"
    :param str start_date : 开始日期，默认"last_year_today"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str secu_market : 证券市场,
    :param str secu_code : 证券代码,
    :param float secu_abbr : 证券简称,
    :param float trading_date : 交易日期,
    :param float info_source : 信息来源,
    :param float hold_vols : 合计持有流通股总数(万股),
    :param float float_rates : 合计占总流通股本比例(%),
    :param float controller_name : 实际控制人,
    :param float serial_number : 股东序号,
    :param float stock_holder_name : 股东名称,
    :param float stock_holder_kind : 股东性质,
    :param float share_character_statement : 股本性质,
    :param float hold_vol : 持流通股总数(万股),
    :param float float_rate : 占总流通股比例(%),
    :param float hold_vol_change : 较上期持股变动股数(万股),
    :param float total_rate_change : 较上期变动比例(%),
    :param float aas_change_type : 变动类别,

    代码调用:
        from hs_udata import float_shareholder_top10
float_shareholder_top10() 

    结果输出:
        
    """

    int_param =[]
    float_param =['secu_abbr', 'trading_date', 'info_source', 'hold_vols', 'float_rates', 'controller_name', 'serial_number', 'stock_holder_name', 'stock_holder_kind', 'share_character_statement', 'hold_vol', 'float_rate', 'hold_vol_change', 'total_rate_change', 'aas_change_type']
    params = {
        "secu_code": secu_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("float_shareholder_top10", url_path="market_info", **params)

@args_check(
    check("trading_day").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def lh_daily(trading_day=None, fields=None):
    """
    每日龙虎榜上榜股票的股票代码、成交金额、净买入额等数据；

    输入参数：
    :param str trading_day : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str closing_price : 最新价(元),
    :param str price_change_ratio : 涨跌幅,
    :param float stock_total : 最近一年上榜次数,
    :param float close_price : 昨收价(元),
    :param float business_balance : 成交金额(元),
    :param float business_amount : 成交量(股),
    :param float secu_abbr : 股票简称,
    :param float secu_code : 证券代码,
    :param float trading_day : 交易日期,
    :param float net_balance : 净买入额(元),
    :param float mark : 标签,

    代码调用:
        from hs_udata import lh_daily
lh_daily() 

    结果输出:
        
    """

    int_param =[]
    float_param =['stock_total', 'close_price', 'business_balance', 'business_amount', 'secu_abbr', 'secu_code', 'trading_day', 'net_balance', 'mark']
    params = {
        "trading_day": trading_day,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("lh_daily", url_path="market_info", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("trading_day").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def lh_stock(secu_code=None, trading_day=None, fields=None):
    """
    获取个股龙虎榜详情，包括成交数据、营业部买入和卖出数据等；

    输入参数：
    :param str secu_code : 证券代码，默认"600570.SH"
    :param str trading_day : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str trading_date : 交易日期,
    :param str secu_abbr : 证券简称,
    :param str stock_total : 最近一年上榜次数,
    :param str buy_total_rate : 买入总占比,
    :param str sale_total_rate : 卖出总占比,
    :param float net_balance : 净买入金额,
    :param str net_rate : 净买入占比,
    :param float business_balance : 成交金额,
    :param int business_amount : 成交数量,
    :param str abnormal_type : 上榜类型简称,
    :param str abnormal_code : 上榜类型对应代码,
    :param str type : 席位,
    :param float buy_rate : 买入金额占总金额比,
    :param float buy_balance : 买入金额,
    :param float sale_rate : 卖出金额占总金额比,
    :param float sale_balance : 卖出金额,
    :param str sales_department_name : 营业部简称,
    :param str list_date : 近十次上榜日期,

    代码调用:
        from hs_udata import lh_stock
lh_stock() 

    结果输出:
        
    """

    int_param =['business_amount']
    float_param =['net_balance', 'business_balance', 'buy_rate', 'buy_balance', 'sale_rate', 'sale_balance']
    params = {
        "secu_code": secu_code,
        "trading_day": trading_day,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("lh_stock", url_path="market_info", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("begin_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_quote_minutes(en_prod_code=None, begin_date=None, end_date=None, fields=None):
    """
    取得上市股票列表，用于股票行情查询；

    输入参数：
    :param str en_prod_code : 聚源代码，默认"600570.SH"
    :param str begin_date : 起始日期，默认"lastday"
    :param str end_date : 结束日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str date : 日期,
    :param str time : 发生时间,
    :param float open : 开盘价(元),
    :param float high : 最高价(元),
    :param float low : 最低价(元),
    :param float close : 收盘价(元),
    :param float turnover_volume : 成交量,
    :param float turnover_value : 成交额,
    :param float change : 涨跌幅(元),
    :param float change_pct : 涨跌幅(%),

    代码调用:
        from hs_udata import stock_quote_minutes
stock_quote_minutes() 

    结果输出:
        
    """

    int_param =[]
    float_param =['open', 'high', 'low', 'close', 'turnover_volume', 'turnover_value', 'change', 'change_pct']
    params = {
        "en_prod_code": en_prod_code,
        "begin_date": convert_date(begin_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_quote_minutes", url_path="market_info", **params)

@args_check(
    check("exchange_kind").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def shszhk_capitalflow(exchange_kind=None, start_date=None, end_date=None, fields=None):
    """
    统计时间范围内沪港通、深港通等资金流向数据，以及领涨领跌股，涨跌幅，资金余额等数据信息。数据每日更新。包括科创板；

    输入参数：
    :param str exchange_kind : 市场类型，默认"1"
    :param str start_date : 开始日期，默认"five days ago"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str trade_date : 交易日期,
    :param float surplus_quota : 剩余额度,
    :param float now_capital_inflow : 当日资金流入（元）,
    :param float sum_capital_inflow : 历史累计流入(亿元),
    :param float now_net_purchase_balance : 当日成交净买额（百万）,
    :param float buy_balance : 买入金额,
    :param float sell_balance : 卖出金额,
    :param str led_stock_code : 领涨股代码,
    :param str led_stock_name : 领涨股名称,
    :param str secu_market : 证券市场,
    :param float led_stock_chg : 领涨股涨跌幅(%),
    :param float currency : 货币单位,

    代码调用:
        from hs_udata import shszhk_capitalflow
shszhk_capitalflow() 

    结果输出:
        
    """

    int_param =[]
    float_param =['surplus_quota', 'now_capital_inflow', 'sum_capital_inflow', 'now_net_purchase_balance', 'buy_balance', 'sell_balance', 'led_stock_chg', 'currency']
    params = {
        "exchange_kind": exchange_kind,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("shszhk_capitalflow", url_path="market_info", **params)

@args_check(
    check("exchange_kind").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def shszhk_deal_top10(exchange_kind=None, start_date=None, end_date=None, fields=None):
    """
    

    输入参数：
    :param str exchange_kind : 市场类型，默认"1"
    :param str start_date : 开始日期，默认"five days ago"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_market : 证券市场,
    :param str trade_date : 交易日期,
    :param float rank : 排名,
    :param float buy_balance : 买入金额(元),
    :param float sell_balance : 卖出金额(元),
    :param float net_purchase_balance : 净买额（元）,
    :param float currency : 货币单位,
    :param float close_price : 收盘价,
    :param float px_change_rate : 涨跌幅,
    :param float business_balance : 成交金额,

    代码调用:
        from hs_udata import shszhk_deal_top10
shszhk_deal_top10() 

    结果输出:
        
    """

    int_param =[]
    float_param =['rank', 'buy_balance', 'sell_balance', 'net_purchase_balance', 'currency', 'close_price', 'px_change_rate', 'business_balance']
    params = {
        "exchange_kind": exchange_kind,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("shszhk_deal_top10", url_path="market_info", **params)

@args_check(
    check("exchange_kind").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def shszhk_distribution(exchange_kind=None, start_date=None, end_date=None, fields=None):
    """
    展示沪港通、深港通的股票涨跌分布。数据每日更新。包括科创板；

    输入参数：
    :param str exchange_kind : 市场类型，默认"1"
    :param str start_date : 开始日期，默认"five days ago"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str trade_date : 交易日期,
    :param float up_count : 上涨个数,
    :param float flat_count : 平盘家数,
    :param float down_count : 下跌个数,

    代码调用:
        from hs_udata import shszhk_distribution
shszhk_distribution() 

    结果输出:
        
    """

    int_param =[]
    float_param =['up_count', 'flat_count', 'down_count']
    params = {
        "exchange_kind": exchange_kind,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("shszhk_distribution", url_path="market_info", **params)

@args_check(
    check("exchange_kind").is_instance((str, None.__class__)),
    check("trading_data").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def shszhk_change_top10(exchange_kind=None, trading_data=None, fields=None):
    """
    按交易日统计沪港通、深港通等十大涨幅股列表，成交金额，换手率，涨跌幅数据等；

    输入参数：
    :param str exchange_kind : 市场类型，默认"1"
    :param str trading_data : 开始日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str trading_data : 交易日,
    :param str rank : 排名,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_market : 证券市场,
    :param float close_price : 收盘价,
    :param float px_change_rate : 涨跌幅,
    :param float turnover_value : 成交额,
    :param float turnover_ratio : 换手率,
    :param float total_mv : A股总市值,
    :param float pe_lyr : 市盈率,
    :param float float_value : A股流通市值(元),
    :param float pe_ttm : 滚动市盈率,

    代码调用:
        from hs_udata import shszhk_change_top10
shszhk_change_top10() 

    结果输出:
        
    """

    int_param =[]
    float_param =['close_price', 'px_change_rate', 'turnover_value', 'turnover_ratio', 'total_mv', 'pe_lyr', 'float_value', 'pe_ttm']
    params = {
        "exchange_kind": exchange_kind,
        "trading_data": trading_data,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("shszhk_change_top10", url_path="market_info", **params)

@args_check(
    check("fields").is_instance((str, None.__class__))
)
def quote_stocklist(fields=None):
    """
    股票代码列表(用于行情查询)

    输入参数：
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证券代码(带后缀),
    :param str secu_code : 证券代码(不带后缀),
    :param str secu_abbr : 证券简称,

    代码调用:
        from hs_udata import quote_stocklist
quote_stocklist() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("quote_stocklist", url_path="market_info", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("level").is_instance(int),
    check("fields").is_instance((str, None.__class__))
)
def industry_category(en_prod_code=None, level=0, fields=None):
    """
    股票在证监会行业、标普行业、中信行业等多个行业信息；

    输入参数：
    :param str en_prod_code : 证券代码，默认"600570.SH"
    :param int level : 交易日期，默认0
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 股票代码,
    :param int level : 等级,
    :param str industry_name_csrc : 证监会行业名称,
    :param str industry_code_csrc : 证监会行业代码,
    :param str industry_name_gics : GICS行业行业名称,
    :param str industry_code_gics : GICS行业行业代码,
    :param str industry_name_sw : 申万行业名称,
    :param str industry_code_sw : 申万行业代码,
    :param str industry_name_citic : 中信行业名称,
    :param str industry_code_citic : 中信行业代码,

    代码调用:
        from hs_udata import industry_category
industry_category() 

    结果输出:
        
    """

    int_param =['level']
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "level": level,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("industry_category", url_path="market_data", **params)

@args_check(
    check("index_stock_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def index_constituent(index_stock_code=None, fields=None):
    """
    主要指数的成份构成情况，包括成份证券的市场代码、入选日期等数据；

    输入参数：
    :param str index_stock_code : 指数代码，默认"399300"
    :param str fields : 字段集合

    输出参数：
    :param str index_stock_code : 指数代码,
    :param str index_secu_abbr : 指数简称,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_market : 成份股市场,
    :param str secu_category : 证券类别,
    :param str in_date : 入选日期,

    代码调用:
        from hs_udata import index_constituent
index_constituent() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "index_stock_code": index_stock_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("index_constituent", url_path="market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("org_type").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def org_hold(secu_code=None, org_type=None, end_date=None, fields=None):
    """
    根据报告期查询个股机构持仓明细与加仓数据；

    输入参数：
    :param str secu_code : 证券代码，默认"600570"
    :param str org_type : 机构类型
    :param str end_date : 报告期查询日，默认"2021-03-31"
    :param str fields : 字段集合

    输出参数：
    :param str secu_market : 证券市场,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str end_date : 报告期,
    :param str sh_name : 股东名称,
    :param str org_type : 机构类型,
    :param str hold_a_sum : 持流通A股数量(万股),
    :param str hold_a_sum_rate : 占流通A股比例(%),
    :param float a_shares_rate : 占A股比例(%),
    :param str hold_a_sum_up : 加仓数量(万股),
    :param str hold_a_sum_up_rate : 加仓比例(%),
    :param str hold_a_sum_up_type : 加仓类型,
    :param float market_value : 市值(万元),

    代码调用:
        from hs_udata import org_hold
org_hold() 

    结果输出:
        
    """

    int_param =[]
    float_param =['a_shares_rate', 'market_value']
    params = {
        "secu_code": secu_code,
        "org_type": org_type,
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("org_hold", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def holder_num(en_prod_code=None, report_date=None, fields=None):
    """
    公司股东户数的基本情况，包括股东户数，户均持股数量，户均持股比例等数据；

    输入参数：
    :param str en_prod_code : 证券代码，默认"600570.SH"
    :param str report_date : 报告期，默认"2021-03-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 内部编码,
    :param str report_date : 申报日期,
    :param str sh_num : 股东总户数,
    :param int average_hold_sum : 户均持股数量,
    :param float average_hold_sum_proportion : 户均持股比例,
    :param float proportion_change : 相对上一报告期户均持股比例差值,
    :param float avg_hold_sum_gr_quarter : 户均持股数季度增长率,
    :param float proportion_gr_quarter : 户均持股比例季度增长率,
    :param float avg_hold_sum_gr_half_a_year : 户均持股数年增长率,
    :param float proportion_gr_half_a_year : 户均持股比例年增长率,

    代码调用:
        from hs_udata import holder_num
holder_num() 

    结果输出:
        
    """

    int_param =['average_hold_sum']
    float_param =['average_hold_sum_proportion', 'proportion_change', 'avg_hold_sum_gr_quarter', 'proportion_gr_quarter', 'avg_hold_sum_gr_half_a_year', 'proportion_gr_half_a_year']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("holder_num", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("query_direction").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def restricted_schedule(en_prod_code=None, trading_date=None, query_direction=None, fields=None):
    """
    收录上市公司因为股权分置改革、定向增发、公开增发等原因所限售的股票的具体解禁时间及相关明细数据；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"now"
    :param str query_direction : 查询方向，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param str start_date_for_circulating : 限售解禁日期,
    :param float new_circulation_a_shares : 新增流通A股数量,
    :param float new_circulation_a_shares_rate : 新增流通A股占已流通A股比例,
    :param float accu_circulation_a_shares : 已流通A股数量,
    :param float non_circulation_a_shares : 未流通A股数量,
    :param str new_circulation_a_shares_type : 新增流通A股类型,

    代码调用:
        from hs_udata import restricted_schedule
restricted_schedule() 

    结果输出:
        
    """

    int_param =[]
    float_param =['new_circulation_a_shares', 'new_circulation_a_shares_rate', 'accu_circulation_a_shares', 'non_circulation_a_shares']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "query_direction": query_direction,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("restricted_schedule", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("serial_number").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def holder_pledge(en_prod_code=None, trading_date=None, serial_number=None, fields=None):
    """
    统计股东股权质押明细，包括质押股东名称、质押股数、占总股本比例等字段，支持同时输入多个股票代码；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"now"
    :param str serial_number : 股东序号
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param str pledge_stock_holder_name : 质押股东名称,
    :param float pledge_involved_sum : 质押涉及股数,
    :param float pct_of_frozen_pledger : 占冻结质押方持股数比例,
    :param float pct_of_total_shares : 占总股本比例,
    :param str publ_date : 股权质押公告日期,

    代码调用:
        from hs_udata import holder_pledge
holder_pledge() 

    结果输出:
        
    """

    int_param =[]
    float_param =['pledge_involved_sum', 'pct_of_frozen_pledger', 'pct_of_total_shares']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "serial_number": serial_number,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("holder_pledge", url_path="market_data", **params)

@args_check(
    check("date_type").is_instance((str, None.__class__)),
    check("symbols").is_instance((str, None.__class__)),
    check("listed_sector").is_instance((str, None.__class__)),
    check("secu_market").is_instance((str, None.__class__)),
    check("share_holder_type").is_instance((str, None.__class__)),
    check("state_type").is_instance((float, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def holder_increase(date_type=None, symbols=None, listed_sector=None, secu_market=None, share_holder_type=None, state_type=None, start_date=None, end_date=None, fields=None):
    """
    统计上市公司董事、监事、高级管理人员、股东持有本公司股份变动情况分析，可与高管持股进行合并；

    输入参数：
    :param str date_type : 日期范围类型，默认"1"
    :param str symbols : 股票代码
    :param str listed_sector : 上市板块
    :param str secu_market : 市场类型
    :param str share_holder_type : 股东类型
    :param float state_type : 增减持类型
    :param str start_date : 公告日开始日期，默认"last_year_today"
    :param str end_date : 公告日查询截止日期，默认"now"
    :param str fields : 输出字段集合

    输出参数：
    :param str id : 记录ID,
    :param str holder_name : 股东姓名,
    :param str leader_name : 领导人姓名,
    :param float involved_vol : 变动数量(股),
    :param float pct_chan_ratio : 变动后持股占总股本比例,
    :param float pct_of_total_shares : 变动数量占总股本比例(%),
    :param float price_change_ratio : 累计涨跌幅(%),
    :param str publ_date : 公告日期,
    :param str secu_abbr : 股票简称,
    :param str secu_market : 交易市场,
    :param str secu_code : 股票代码,
    :param float state_type : 增持类型,
    :param float trade_price : 交易价格,
    :param float trade_balance : 交易金额(单位：元),
    :param str listed_sector : 上市板块,
    :param str tran_date : 股权正式变动日期/过户日期（变动截止日）,
    :param str holder_type : 股东类别,
    :param str relation_description : 与领导人关系,
    :param float involved_chan_vol : 变动后持股数量(股),

    代码调用:
        from hs_udata import holder_increase
holder_Increase() 

    结果输出:
        
    """

    int_param =[]
    float_param =['involved_vol', 'pct_chan_ratio', 'pct_of_total_shares', 'price_change_ratio', 'state_type', 'trade_price', 'trade_balance', 'involved_chan_vol']
    params = {
        "date_type": date_type,
        "symbols": symbols,
        "listed_sector": listed_sector,
        "secu_market": secu_market,
        "share_holder_type": share_holder_type,
        "state_type": state_type,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("holder_increase", url_path="market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def pledge_repo(secu_code=None, end_date=None, fields=None):
    """
    1.本表记录的证券范围包括Ａ股股票，不含基金、债券；质押数量包括场内质押和场外质押，深市不包括场内股票质押式回购交易
    成功申报违约处置后对应交易的质押证券数量。 2.数据范围：2016.11-至今 3.信息来源：中国证券登记结算有限责任公司；

    输入参数：
    :param str secu_code : 股票代码，默认"600570"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param float pledge_ratio : 质押比例(%),
    :param str secu_code : 股票代码,
    :param str secu_abbr : 证券简称,
    :param str end_date : 截止日期,
    :param float non_pled_volume : 无限售股份质押数量(万股),
    :param float res_pled_volume : 有限售股份质押数量(万股),
    :param float total_share_a : A股总股本(万股),
    :param float pledge_num : 质押笔数,

    代码调用:
        from hs_udata import pledge_repo
pledge_repo() 

    结果输出:
        
    """

    int_param =[]
    float_param =['pledge_ratio', 'non_pled_volume', 'res_pled_volume', 'total_share_a', 'pledge_num']
    params = {
        "secu_code": secu_code,
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("pledge_repo", url_path="market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_pledge(secu_code=None, start_date=None, end_date=None, fields=None):
    """
    获取个股股权质押解押明细数据汇总以及所占总股本比例。提供2010-01-01起数据；

    输入参数：
    :param str secu_code : 证券代码
    :param str start_date : 开始日期，默认"half year ago"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_market : 证券市场,
    :param str info_publ_date : 公告日期,
    :param float involved_sum_br_count : 涉及股数_前复权汇总,
    :param float proportion_totalshares : 占总股本比例,

    代码调用:
        from hs_udata import stock_pledge
stock_pledge() 

    结果输出:
        
    """

    int_param =[]
    float_param =['involved_sum_br_count', 'proportion_totalshares']
    params = {
        "secu_code": secu_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_pledge", url_path="market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def block_trade(secu_code=None, start_date=None, end_date=None, fields=None):
    """
    上市公司最新股本结构变动情况数据，展示大宗交易明细，可返回列表数据，可以通过股票代码集查询；

    输入参数：
    :param str secu_code : 证券代码，默认"600570"
    :param str start_date : 开始日期，默认"yesterday"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_market : 证券市场,
    :param str listed_sector : 上市板块,
    :param str secu_category : 证券类型,
    :param str info_source : 信息来源,
    :param str trade_date : 交易日期,
    :param float close_price : 昨收盘,
    :param float premium_ratio : A股溢价率(%),
    :param float trade_price : 成交价单位元/股,
    :param float involved_vol : 成交量单位万/股,
    :param str receiver_name : 买方营业部,
    :param str transferer_name : 卖方营业部,

    代码调用:
        from hs_udata import block_trade
block_trade() 

    结果输出:
        
    """

    int_param =[]
    float_param =['close_price', 'premium_ratio', 'trade_price', 'involved_vol']
    params = {
        "secu_code": secu_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("block_trade", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def margin_trading(en_prod_code=None, trading_date=None, fields=None):
    """
    统计交易所公布的融资融券每日详细数据，包括融券余额、融资余额、融资买入额、融资偿还额、融券偿还额、融券偿还量等指标，
    支持同时输入多个股票代码；

    输入参数：
    :param str en_prod_code : 内部编码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 内部编码,
    :param str trading_date : 交易日期,
    :param float finance_balance : 融资余额,
    :param float security_balance : 融券余额,
    :param float finance_buy_balance : 融资买入额,
    :param float finance_refund_balance : 融资偿还额,
    :param float security_buy_balance : 融券卖出额,
    :param float security_refund_balance : 融券偿还额,
    :param float security_sell_amount : 融券卖出量,
    :param float security_refund_amount : 融券偿还量,
    :param float security_amount : 融券余量,
    :param float finance_security_balance : 融资融券余额,

    代码调用:
        from hs_udata import margin_trading
margin_trading() 

    结果输出:
        
    """

    int_param =[]
    float_param =['finance_balance', 'security_balance', 'finance_buy_balance', 'finance_refund_balance', 'security_buy_balance', 'security_refund_balance', 'security_sell_amount', 'security_refund_amount', 'security_amount', 'finance_security_balance']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("margin_trading", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("begin_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def interval_margin_trading(en_prod_code=None, begin_date=None, end_date=None, fields=None):
    """
    统计交易所公布的融资融券某个时间区间的数据，包含区间融资买入额、区间融资偿还额、区间融券偿还量、区间融券卖出额、区间
    融券偿还额等指标，支持同时；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str begin_date : 起始日期，默认"five years ago"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str begin_date : 起始日期,
    :param str end_date : 截止日期,
    :param float inter_finance_buy_balance : 区间融资买入额,
    :param float inter_finance_refund_balance : 区间融资偿还额,
    :param float inter_avg_finance_balance : 区间融资余额均值,
    :param float inter_security_sell_amount : 区间融券卖出量,
    :param float inter_security_refund_amount : 区间融券偿还量,
    :param float inter_security_buy_balance : 区间融券卖出额,
    :param float inter_security_refund_balance : 区间融券偿还额,
    :param float inter_avg_security_amount : 区间融券余量均值,
    :param float inter_avg_security_balance : 区间融券余额均值,
    :param float avg_finance_security_balance : 区间融资融券余额均值,

    代码调用:
        from hs_udata import interval_margin_trading
interval_margin_trading() 

    结果输出:
        
    """

    int_param =[]
    float_param =['inter_finance_buy_balance', 'inter_finance_refund_balance', 'inter_avg_finance_balance', 'inter_security_sell_amount', 'inter_security_refund_amount', 'inter_security_buy_balance', 'inter_security_refund_balance', 'inter_avg_security_amount', 'inter_avg_security_balance', 'avg_finance_security_balance']
    params = {
        "en_prod_code": en_prod_code,
        "begin_date": convert_date(begin_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("interval_margin_trading", url_path="market_data", **params)

@args_check(
    check("symbols").is_instance((str, None.__class__)),
    check("date_type").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def margin_trade_detail(symbols=None, date_type=None, start_date=None, end_date=None, fields=None):
    """
    查询股票代码范围内的融资融券历史交易明细统计，包括融资买入，卖出，偿还等基本详细数据；

    输入参数：
    :param str symbols : 股票代码，默认"600570.SH"
    :param str date_type : 日期类型，默认"1"
    :param str start_date : 开始日期，默认"last_year_today"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 输出字段集合

    输出参数：
    :param str secu_abbr : 证券简称,
    :param str secu_code : 证券代码,
    :param str trading_date : 交易日期,
    :param float trading_balance : 融资融券交易总金额（元）,
    :param float secu_in_total_rate : 融券占交易所融券余额比（%）,
    :param float security_net_amount : 融券净卖出,
    :param float security_refund_amount : 融券偿还量（股）,
    :param float security_sell_amount : 融券卖出量（股）,
    :param float security_balance : 融券余额（元）,
    :param float security_amount : 融券余量（股）,
    :param float fina_in_float_rate : 融资余额占流通市值比例(%),
    :param float secu_in_float_rate : 融券余额占流通市值比例(%),
    :param float fina_in_total_rate : 融资占交易所融资余额比（%）,
    :param float finance_buy_balance : 融资买入额（元）,
    :param float finance_net_balance : 融资净买入,
    :param float finance_refund_balance : 融资偿还额（元）,
    :param float finance_balance : 融资余额（元）,

    代码调用:
        from hs_udata import margin_trade_detail
margin_trade_detail() 

    结果输出:
        
    """

    int_param =[]
    float_param =['trading_balance', 'secu_in_total_rate', 'security_net_amount', 'security_refund_amount', 'security_sell_amount', 'security_balance', 'security_amount', 'fina_in_float_rate', 'secu_in_float_rate', 'fina_in_total_rate', 'finance_buy_balance', 'finance_net_balance', 'finance_refund_balance', 'finance_balance']
    params = {
        "symbols": symbols,
        "date_type": date_type,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("margin_trade_detail", url_path="market_data", **params)

@args_check(
    check("date_type").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def margin_trade_total(date_type=None, start_date=None, end_date=None, fields=None):
    """
    按市场以及融资融券的4钟类型进行交易历史总量统计，包含融资余额统计信息、融资买入额统计信息、融券余额统计信息、融资融
    券余额统计信息；

    输入参数：
    :param str date_type : 日期类型，默认"1"
    :param str start_date : 开始日期，默认"last_year_today"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 输出字段集合

    输出参数：
    :param str trading_date : 交易日期,
    :param float sh_finance_balance : 沪融资余额,
    :param float sh_finance_buy_balance : 沪融资买入额,
    :param float sh_security_balance : 沪融券余额,
    :param float sh_trading_balance : 沪融资融券余额,
    :param float sz_finance_balance : 深融资余额,
    :param float sz_finance_buy_balance : 深融资买入额,
    :param float sz_security_balance : 深融券余额,
    :param float sz_trading_balance : 深融资融券余额,
    :param float tol_finance_balance : 沪深融资余额,
    :param float tol_finance_buy_balance : 沪深融资买入额,
    :param float tol_security_balance : 沪深融券余额,
    :param float tol_trading_balance : 沪深融资融券余额,

    代码调用:
        from hs_udata import margin_trade_total
margin_trade_total() 

    结果输出:
        
    """

    int_param =[]
    float_param =['sh_finance_balance', 'sh_finance_buy_balance', 'sh_security_balance', 'sh_trading_balance', 'sz_finance_balance', 'sz_finance_buy_balance', 'sz_security_balance', 'sz_trading_balance', 'tol_finance_balance', 'tol_finance_buy_balance', 'tol_security_balance', 'tol_trading_balance']
    params = {
        "date_type": date_type,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("margin_trade_total", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_dividend(en_prod_code=None, report_date=None, fields=None):
    """
    统计上市公司历次分红基本信息，包括每股送转，每股转增股本、每股股利等指标，支持同时输入多个股票代码或报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param float per_ending_original_cost : 每股送转,
    :param float per_bonus_share_ratio : 每股送股比例,
    :param float per_tran_add_share_ratio : 每股转增股比例,
    :param float cash_divi_rmb : 派现(含税/人民币元),
    :param float actual_cash_divi_rmb : 实派(税后/人民币元),
    :param str pre_disclosure_date : 预披露公告日,
    :param str advance_date : 预约日期,
    :param str announcement_date : 决案公告日,
    :param str divi_impl_date : 分红实施公告日,
    :param str right_reg_date : 股权登记日,
    :param str ex_divi_date : 除权除息日,
    :param str bonus_share_list_date : 送转股上市日,
    :param str payout_date : 股息到帐日期/红利发放日,
    :param str final_trade_date : 最后交易日,
    :param str procedure_desc : 分红方案进度,
    :param str divi_object : 分红对象,
    :param str if_dividend : 是否分红,

    代码调用:
        from hs_udata import stock_dividend
stock_dividend() 

    结果输出:
        
    """

    int_param =[]
    float_param =['per_ending_original_cost', 'per_bonus_share_ratio', 'per_tran_add_share_ratio', 'cash_divi_rmb', 'actual_cash_divi_rmb']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_dividend", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("year").is_instance((str, None.__class__)),
    check("issue_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_additional(en_prod_code=None, year=None, issue_type=None, fields=None):
    """
    统计公司历次增发明细信息，包括增发方案内容、进程、实施进度、承销商等信息，支持同时输入多个股票代码或查询年度；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str year : 年度，默认"2021"
    :param str issue_type : 认购方式，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str year : 年度,
    :param str spo_event_procedure : 事件进程,
    :param str issue_purpose : 增发目的,
    :param str issue_price : 增发价格,
    :param float issue_vol : 增发数量,
    :param float ipo_proceeds : 增发新股募集资金总额,
    :param float net_proceeds : 增发新股募集资金净额,
    :param str advance_date : 预约日期,
    :param str shareholders_publ_date : 股东大会公告日,
    :param str prospectus_publ_date : 增发公告日,
    :param str sasac_approval_publ_date : 国资委通过公告日,
    :param str csrc_approval_publ_date : 证监会批准公告日,
    :param str list_announce_date : 增发新股上市公告日期,
    :param str price_adjusted_date : 最新发行价调整日,
    :param str online_issue_date : 上网公开发行日期,
    :param str otc_date : 向网下增发日期,
    :param str sni_list_date : 增发股份上市日期,
    :param str orig_holder_preferred_date : 老股东优先配售日期,
    :param str result_date : 发行结果公示日,
    :param str scheme_change_publ_date : 方案变动公告日,
    :param str scheme_change_statement : 方案变动说明,
    :param str scheme_change_type : 方案变动类型,
    :param float issue_price_ceiling : 发行价格上限,
    :param float issue_price_floor : 发行价格下限,
    :param float adjusted_issue_price : 调整后发行价格下降,
    :param float referring_price : 承销商指导价格,
    :param float underwriting_fee : 承销费用,
    :param float pe_ratio_before_issue : 增发市盈率（按增发前总股本）,
    :param float tailored_issue_vol_legal_person : 法人定向配售股数,
    :param float staq_net_issue_vol : STAQ/NET定向配售股数,
    :param float fund_issue_vol : 投资基金配售股数,
    :param float main_income_forecast : 主营业务收入预测,
    :param float net_profit_forecast : 净利润预测,
    :param float diluted_eps_forecast : 全面摊薄每股盈利预测,

    代码调用:
        from hs_udata import stock_additional
stock_additional() 

    结果输出:
        
    """

    int_param =[]
    float_param =['issue_vol', 'ipo_proceeds', 'net_proceeds', 'issue_price_ceiling', 'issue_price_floor', 'adjusted_issue_price', 'referring_price', 'underwriting_fee', 'pe_ratio_before_issue', 'tailored_issue_vol_legal_person', 'staq_net_issue_vol', 'fund_issue_vol', 'main_income_forecast', 'net_profit_forecast', 'diluted_eps_forecast']
    params = {
        "en_prod_code": en_prod_code,
        "year": year,
        "issue_type": issue_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_additional", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("spo_process").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_additional_all(en_prod_code=None, trading_date=None, spo_process=None, fields=None):
    """
    统计股票上市以来增发概况，包括增发总次数、成功次数、失败次数、累计募集资金总额等指标；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"2020-12-31"
    :param str spo_process : 增发进程，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float spo_num : 增发总次数,
    :param float spo_num_success : 增发已成功次数,
    :param float spo_num_fail : 增发已失败次数,
    :param float spo_num_going : 增发进行中次数,
    :param float accu_ipo_proceeds : 增发累计募集资金总额,
    :param float accu_net_proceeds : 增发累计募集资金净额,
    :param float accu_issue_cost : 增发累计费用总额,

    代码调用:
        from hs_udata import stock_additional_all
stock_additional_all() 

    结果输出:
        
    """

    int_param =[]
    float_param =['spo_num', 'spo_num_success', 'spo_num_fail', 'spo_num_going', 'accu_ipo_proceeds', 'accu_net_proceeds', 'accu_issue_cost']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "spo_process": spo_process,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_additional_all", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("year").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_allotment(en_prod_code=None, year=None, fields=None):
    """
    统计公司历次配股方案信息，支持同时输入多个股票代码和查询年度。 

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str year : 年度，默认"2020"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str year : 年度,
    :param float actual_allot_ratio : 实际配股比例(10配X),
    :param float allot_price : 每股配股价格,
    :param float actual_allot_vol : 实际配股数量,
    :param float ipo_proceeds : 募集资金总额,
    :param str issue_cost : 发行费用总额,
    :param float allot_price_ceiling : 配股价格上限,
    :param float allot_price_floor : 配股价格下限,
    :param float base_vol : 配股股本基数,
    :param float transfer_allot_ratio : 转配比(10转配X),
    :param float planned_allot_ratio : 计划配股比例（10配X),
    :param float planned_allot_vol : 计划配股数量,
    :param float advance_date : 预约日期,
    :param str shareholders_publ_date : 股东大会公告日期,
    :param str allot_prospectus_publ_date : 配股公告日期,
    :param str right_reg_date : 股权登记日,
    :param str ex_right_date : 除权日,
    :param str allot_start_date : 配股交款起始日,
    :param str allot_end_date : 配股交款截止日,
    :param str fund_to_account_date : 资金到帐日,
    :param str allot_list_date : 配股上市日,

    代码调用:
        from hs_udata import stock_allotment
stock_allotment() 

    结果输出:
        
    """

    int_param =[]
    float_param =['actual_allot_ratio', 'allot_price', 'actual_allot_vol', 'ipo_proceeds', 'allot_price_ceiling', 'allot_price_floor', 'base_vol', 'transfer_allot_ratio', 'planned_allot_ratio', 'planned_allot_vol', 'advance_date']
    params = {
        "en_prod_code": en_prod_code,
        "year": year,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_allotment", url_path="market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("forcast_type").is_instance((str, None.__class__)),
    check("forecast_object").is_instance((str, None.__class__)),
    check("egrowth_rate_floor").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_asforecastabb(secu_code=None, forcast_type=None, forecast_object=None, egrowth_rate_floor=None, fields=None):
    """
    业绩预增列表

    输入参数：
    :param str secu_code : 证券代码
    :param str forcast_type : 业绩预计类型，默认"4"
    :param str forecast_object : 预告对象，默认"10,13"
    :param str egrowth_rate_floor : 预计幅度起始(%)大于，默认"20"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str end_date : 截止日期,
    :param str forcast_type : 业绩预计类型,
    :param str forecast_object : 预告对象,
    :param str forcast_content : 业绩预计内容描述,
    :param str egrowth_rate_floor : 变动幅度下限,
    :param str egrowth_rate_ceiling : 变动幅度上限,
    :param str eprofit_floor : 预计净利润下限,
    :param str eprofit_ceiling : 预计净利润上限,
    :param float eearning_floor : 预计收入起始(元),
    :param float eearning_ceiling : 预计收入截止(元),

    代码调用:
        from hs_udata import stock_asforecastabb
stock_asforecastabb() 

    结果输出:
        
    """

    int_param =[]
    float_param =['eearning_floor', 'eearning_ceiling']
    params = {
        "secu_code": secu_code,
        "forcast_type": forcast_type,
        "forecast_object": forecast_object,
        "egrowth_rate_floor": egrowth_rate_floor,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_asforecastabb", url_path="market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_asunderweight(secu_code=None, fields=None):
    """
    首次减持计划列表

    输入参数：
    :param str secu_code : 证劵代码
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str sh_name : 股东名称,
    :param str serial_number : 股东序号,
    :param str event_info : 事件描述,
    :param str initial_info_publ_date : 首次信息发布日期,

    代码调用:
        from hs_udata import stock_asunderweight
stock_asunderweight() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "secu_code": secu_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_asunderweight", url_path="market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_asoverweight(secu_code=None, fields=None):
    """
    统计公司历次配股方案信息，支持同时输入多个股票代码和查询年度。 

    输入参数：
    :param str secu_code : 证劵代码
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str initial_info_publ_date : 首次信息发布日期,
    :param str sh_name : 股东名称,
    :param str serial_number : 股东序号,
    :param str add_hold_time : 增持时间描述,
    :param float add_hold_term : 增持实施期限,
    :param str end_date : 截止日期,
    :param str add_hold_price_statement : 增持价格描述,
    :param float add_hold_share_ceiling : 增持股份数量上限,
    :param float add_hold_ratio_ceiling : 增持比例上限-占总股本,
    :param float add_hold_share_min : 增持股份数量下限,
    :param float add_hold_ratio_min : 增持比例下限-占总股本,
    :param str add_hold_statement : 增持计划说明,

    代码调用:
        from hs_udata import stock_asoverweight
stock_asoverweight() 

    结果输出:
        
    """

    int_param =[]
    float_param =['add_hold_term', 'add_hold_share_ceiling', 'add_hold_ratio_ceiling', 'add_hold_share_min', 'add_hold_ratio_min']
    params = {
        "secu_code": secu_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_asoverweight", url_path="market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("year").is_instance((str, None.__class__)),
    check("tran_mode").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_asrighttransfer(secu_code=None, year=None, tran_mode=None, fields=None):
    """
    股权转让列表

    输入参数：
    :param str secu_code : 证券代码
    :param str year : 年度
    :param str tran_mode : 股权转让方式
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str info_publ_date : 发布日期,
    :param str tran_mode : 股权转让方式,
    :param float deal_price : 交易价格(元/股),
    :param float pledge_involved_sum : 涉及股数(股),
    :param float pct_of_total_shares : 占总股本比例(%),
    :param str transferer_name : 股权出让方名称,
    :param str tran_date : 过户日期,
    :param str receiver_name : 股权受让方名称,
    :param str if_snafter_tran : 是否第1大股东变更,

    代码调用:
        from hs_udata import stock_asrighttransfer
stock_asrighttransfer() 

    结果输出:
        
    """

    int_param =[]
    float_param =['deal_price', 'pledge_involved_sum', 'pct_of_total_shares']
    params = {
        "secu_code": secu_code,
        "year": year,
        "tran_mode": tran_mode,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_asrighttransfer", url_path="market_data", **params)

@args_check(
    check("tran_mode").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_asraising(tran_mode=None, fields=None):
    """
    举牌列表

    输入参数：
    :param str tran_mode : 股权转让方式
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str end_date : 截止日期,
    :param float after_rece : 举牌方持股比例,
    :param str receiver_name : 举牌方,
    :param str start_date : 开始日期,
    :param str date_rang : 周期,
    :param float pledge_involved_sum : 周期内累计交易股数(股),
    :param float pct_of_total_shares : 周期内累计占比,

    代码调用:
        from hs_udata import stock_asraising
stock_asraising() 

    结果输出:
        
    """

    int_param =[]
    float_param =['after_rece', 'pledge_involved_sum', 'pct_of_total_shares']
    params = {
        "tran_mode": tran_mode,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_asraising", url_path="market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def schedule_disclosure(en_prod_code=None, report_date=None, fields=None):
    """
    统计上市公司定期报告的预计披露日期与实际披露日期，支持同时输入多个股票代码或报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param str actual_date : 定期报告实际披露日期,
    :param str plan_date : 计划执行日期,

    代码调用:
        from hs_udata import schedule_disclosure
schedule_disclosure() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("schedule_disclosure", url_path="finance_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("report_types").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def stock_key_indicator(secu_code=None, start_date=None, end_date=None, report_types=None, fields=None):
    """
    获取财务数据的关键指标信息，营业收入，市盈率、市净率、总资产等。（无数值科目不出参）包括科创板；

    输入参数：
    :param str secu_code : 证券代码，默认"600570.SH"
    :param str start_date : 开始日期，默认"two days ago"
    :param str end_date : 截止日期，默认"now"
    :param str report_types : 财报类型
    :param str fields : 字段集合

    输出参数：
    :param str secu_market : 证券市场,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str end_date : 报告期,
    :param float operating_revenue : 营业收入(元),
    :param float total_asset : 总资产(元),
    :param float total_shareholder_equity : 股东权益(元),
    :param float se_without_mi : 归属母公司股东权益(元),
    :param float net_profit : 净利润(元),
    :param float np_parent_company_owners : 归属母公司股东的净利润(元),
    :param float net_profit_cut : 扣除非经常性损益后的净利润,
    :param float basic_eps : 每股收益(元),
    :param float roe_weighted : 净资产收益率_加权(%),
    :param float roe : 净资产收益率_摊薄(%),
    :param float net_asset_ps : 每股净资产(元),
    :param float basic_eps_cut : 扣非每股收益(元),
    :param float undivided_profit : 每股未分配利润(元),
    :param float pb_ttm : 市净率,
    :param float capital_surplus_fund_ps : 每股资本公积金(元),
    :param float accumulation_fund_ps : 每股公积金,
    :param float cash_flow_ps : 每股现金流净额(元),
    :param float net_oper_cash_flowps : 每股经营活动产生的现金流量净额(元),
    :param float gross_income_ratio : 销售毛利率(%),
    :param float inventory_trate : 存货周转率(次),
    :param float net_profit_yoy : 净利润同比增长率(%),
    :param float operating_revenue_grow_rate : 营业收入同比增长率(%),
    :param float debt_assets_ratio : 资产负债率(%),
    :param float pe_ttm : 市盈率(%),

    代码调用:
        from hs_udata import stock_key_indicator
stock_key_indicator() 

    结果输出:
        
    """

    int_param =[]
    float_param =['operating_revenue', 'total_asset', 'total_shareholder_equity', 'se_without_mi', 'net_profit', 'np_parent_company_owners', 'net_profit_cut', 'basic_eps', 'roe_weighted', 'roe', 'net_asset_ps', 'basic_eps_cut', 'undivided_profit', 'pb_ttm', 'capital_surplus_fund_ps', 'accumulation_fund_ps', 'cash_flow_ps', 'net_oper_cash_flowps', 'gross_income_ratio', 'inventory_trate', 'net_profit_yoy', 'operating_revenue_grow_rate', 'debt_assets_ratio', 'pe_ttm']
    params = {
        "secu_code": secu_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "report_types": report_types,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("stock_key_indicator", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def accounting_data(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    反映上市公司的主要指标，收录同一公司在报告期末的四种财务报告，即未调整的合并报表、未调整的母公司报表、调整后的合并报
    表以及调整后的母公司报表，同一报告期每种类型报表当有多次调整时，展示最新的一条记录；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float basic_eps : 每股收益EPS-基本,
    :param float diluted_eps : 每股收益EPS-稀释,
    :param float basic_eps_cut : 每股收益EPS-扣除／基本,
    :param float diluted_eps_cut : 每股收益EPS-扣除／稀释,
    :param float np_parent_company_owners_t : 每股收益EPS-期末股本摊薄,
    :param float new_np_parent_company_owners_t : 每股收益EPS-最新股本摊薄,
    :param float net_profit_cut_t : 每股收益EPS-扣除/期末股本摊薄,
    :param float new_net_profit_cut_t : 每股收益EPS-扣除/最新股本摊薄,
    :param float eps_ttm : 每股收益EPS（TTM）,
    :param float roe : 净资产收益率ROE-摊薄（公布值）,
    :param float roe_weighted : 净资产收益率ROE-加权（公布值）,
    :param float roe_avg : 净资产收益率-平均,
    :param float roe_cut : 净资产收益率_扣除,摊薄,
    :param float roe_cut_weighted : 净资产收益率（扣除-加权）,
    :param float roe_cut_avg : 净资产收益率ROE（扣除-平均）,
    :param float roe_avg_year : 净资产收益率-年化,
    :param float net_profit_cut_sewi : 净资产收益率ROE-增发条件,
    :param float total_operating_revenue : 营业总收入,
    :param float invest_income : 投资收益,
    :param float financial_expense : 财务费用,
    :param float fair_value_change_income : 公允价值变动净收益,
    :param float operating_profit : 营业利润,
    :param float non_operating_income : 营业外收入,
    :param float non_operating_expense : 营业外支出,
    :param float total_profit : 利润总额,
    :param float income_tax_cost : 所得税费用,
    :param float uncertained_investment_losses : 未确认的投资损失,
    :param float net_profit : 净利润,
    :param float np_parent_company_owners : 归属于母公司所有者的净利润,
    :param float minority_profit : 少数股东损益,
    :param float net_operate_cash_flow : 经营活动产生的现金流量净额,
    :param float net_operate_cash_flow_ps : 每股经营活动产生的现金流量净额,
    :param float net_operate_cash_flow_ps_ttm : 每股经营活动产生的现金流量净额_TTM,
    :param float net_invest_cash_flow : 投资活动产生的现金流量净额,
    :param float net_finance_cash_flow : 筹资活动产生的现金流量净额,
    :param float cash_equivalent_increase : 现金及现金等价物净增加额,
    :param float exchan_rate_change_effect : 汇率变动对现金及现金等价物的影响,
    :param float end_period_cash_equivalent : 期末现金及现金等价物余额,
    :param float cash_equivalents : 货币资金,
    :param float trading_assets : 交易性金融资产,
    :param float interest_receivable : 应收利息,
    :param float dividend_receivable : 应收股利,
    :param float account_receivable : 应收账款,
    :param float other_receivable : 其他应收款,
    :param float inventories : 存货,
    :param float total_current_assets : 流动资产合计,
    :param float hold_for_sale_assets : 可供出售金融资产,
    :param float hold_to_maturity_investments : 持有至到期投资,
    :param float investment_property : 投资性房地产,
    :param float longterm_equity_invest : 长期股权投资,
    :param float intangible_assets : 无形资产,
    :param float total_non_current_assets : 非流动资产合计,
    :param float total_assets : 资产总计,
    :param float shortterm_loan : 短期借款,
    :param float trading_liability : 交易性金融负债,
    :param float salaries_payable : 应付职工薪酬,
    :param float dividend_payable : 应付股利,
    :param float taxs_payable : 应交税费,
    :param float other_payable : 其他应付款,
    :param float non_current_liability_in_one_year : 一年内到期的非流动负债,
    :param float total_current_liability : 流动负债合计,
    :param float total_non_current_liability : 非流动负债合计,
    :param float total_liability : 负债合计,
    :param float paidin_capital : 实收资本（或股本）,
    :param float capital_reserve_fund : 资本公积,
    :param float surplus_reserve_fund : 盈余公积,
    :param float retained_profit : 未分配利润,
    :param float se_without_mi : 归属母公司股东权益合计,
    :param float minority_interests : 少数股东权益,
    :param float total_shareholder_equity : 所有者权益合计,
    :param float total_liability_and_equity : 负债和所有者权益（或股东权益）总计,
    :param float naps : 每股净资产BPS,
    :param float se_without_mi_t : 每股净资产BPS（最新股本摊薄）,

    代码调用:
        from hs_udata import accounting_data
accounting_data() 

    结果输出:
        
    """

    int_param =[]
    float_param =['basic_eps', 'diluted_eps', 'basic_eps_cut', 'diluted_eps_cut', 'np_parent_company_owners_t', 'new_np_parent_company_owners_t', 'net_profit_cut_t', 'new_net_profit_cut_t', 'eps_ttm', 'roe', 'roe_weighted', 'roe_avg', 'roe_cut', 'roe_cut_weighted', 'roe_cut_avg', 'roe_avg_year', 'net_profit_cut_sewi', 'total_operating_revenue', 'invest_income', 'financial_expense', 'fair_value_change_income', 'operating_profit', 'non_operating_income', 'non_operating_expense', 'total_profit', 'income_tax_cost', 'uncertained_investment_losses', 'net_profit', 'np_parent_company_owners', 'minority_profit', 'net_operate_cash_flow', 'net_operate_cash_flow_ps', 'net_operate_cash_flow_ps_ttm', 'net_invest_cash_flow', 'net_finance_cash_flow', 'cash_equivalent_increase', 'exchan_rate_change_effect', 'end_period_cash_equivalent', 'cash_equivalents', 'trading_assets', 'interest_receivable', 'dividend_receivable', 'account_receivable', 'other_receivable', 'inventories', 'total_current_assets', 'hold_for_sale_assets', 'hold_to_maturity_investments', 'investment_property', 'longterm_equity_invest', 'intangible_assets', 'total_non_current_assets', 'total_assets', 'shortterm_loan', 'trading_liability', 'salaries_payable', 'dividend_payable', 'taxs_payable', 'other_payable', 'non_current_liability_in_one_year', 'total_current_liability', 'total_non_current_liability', 'total_liability', 'paidin_capital', 'capital_reserve_fund', 'surplus_reserve_fund', 'retained_profit', 'se_without_mi', 'minority_interests', 'total_shareholder_equity', 'total_liability_and_equity', 'naps', 'se_without_mi_t']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("accounting_data", url_path="finance_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("merge_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_cashflow(secu_code=None, start_date=None, end_date=None, merge_type=None, fields=None):
    """
    现金流量表主要是反映出资产负债表中各个项目对现金流量的影响，可用于分析一家机构在短期内有没有足够现金去应付开销。1.
    经营活动、2.投资活动、3.筹资活动、4.现金及现金等价物、5.等价物增加、6.将净利润调节为经营活动现金流量、7.不涉及现金收支的投资和筹资活动、8.现金及现金等价物净变动情况；

    输入参数：
    :param str secu_code : 证券代码，默认"600570.SH"
    :param str start_date : 开始日期，默认"two days ago"
    :param str end_date : 截止日期，默认"now"
    :param str merge_type : 合并类型，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str secu_market : 证券市场,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str company_type : 公司类型,
    :param str end_date : 截止日期,
    :param str report_type : 报告类型,
    :param str publ_date : 公告日期,
    :param float net_deposit_in_cb_and_ib : 存放中央银行和同业款项净增加额,
    :param float other_operate_cash_paid : 支付的其他与经营活动有关的现金,
    :param float original_compensation_paid : 支付原保险合同赔付款项的现金,
    :param float net_loan_and_advance_increase : 客户贷款及垫款净增加额,
    :param float net_deal_trading_assets : 处置交易性金融资产净增加额,
    :param float net_cash_for_reinsurance : 支付再保业务现金净额,
    :param float net_operate_cash_flow : 经营活动产生的现金流量净额,
    :param float policy_dividend_cash_paid : 支付保单红利的现金,
    :param float tax_levy_refund : 收到的税费返还,
    :param float interest_and_commission_cashin : 收取利息、手续费及佣金的现金,
    :param float all_taxes_paid : 支付的各项税款,
    :param float net_insurer_deposit_investment : 保户储金及投资款净增加额,
    :param float goods_and_services_cash_paid : 购买商品、接受劳务支付的现金,
    :param float other_cashin_related_operate : 收到其他与经营活动有关的现金,
    :param float subtotal_operate_cash_outflow : 经营活动现金流出小计,
    :param float staff_behalf_paid : 支付给职工以及为职工支付的现金,
    :param float commission_cash_paid : 支付手续费及佣金的现金,
    :param float net_original_insurance_cash : 收到原保险合同保费取得的现金,
    :param float net_deposit_increase : 客户存款和同业存放款项净增加额,
    :param float net_buy_back : 回购业务资金净增加额,
    :param float net_reinsurance_cash : 收到再保业务现金净额,
    :param float goods_sale_service_render_cash : 销售商品、提供劳务收到的现金,
    :param float net_lend_capital : 拆出资金净增加额,
    :param float net_borrowing_from_central_bank : 向中央银行借款净增加额,
    :param float net_borrowing_from_finance_co : 向其他金融机构拆入资金净增加额,
    :param float subtotal_operate_cash_inflow : 经营活动现金流入小计,
    :param float invest_cash_paid : 投资支付的现金,
    :param float other_cash_from_invest_act : 收到其他与投资活动有关的现金,
    :param float net_invest_cash_flow : 投资活动产生的现金流量净额,
    :param float subtotal_invest_cash_inflow : 投资活动现金流入小计,
    :param float invest_withdrawal_cash : 收回投资收到的现金,
    :param float subtotal_invest_cash_outflow : 投资活动现金流出小计,
    :param float invest_proceeds : 取得投资收益收到的现金,
    :param float net_cash_from_sub_company : 取得子公司及其他营业单位支付的现金净额,
    :param float fix_intan_other_asset_dispo_cash : 处置固定资产、无形资产和其他长期资产而收回的现金净额,
    :param float fix_intan_other_asset_acqui_cash : 购建固定资产、无形资产和其他长期资产所支付的现金,
    :param float other_cash_to_invest_act : 支付其他与投资活动有关的现金,
    :param float net_cash_deal_sub_company : 处置子公司及其他营业单位收到的现金净额,
    :param float impawned_loan_net_increase : 质押贷款净增加额,
    :param float subtotal_finance_cash_outflow : 筹资活动现金流出小计,
    :param float other_finance_act_payment : 支付的其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_inflow : 筹资活动现金流入小计,
    :param float cash_from_bonds_issue : 发行债券收到的现金,
    :param float net_finance_cash_flow : 筹资活动产生的现金流量净额,
    :param float dividend_interest_payment : 分配股利、利润或偿付利息支付的现金,
    :param float borrowing_repayment : 偿还债务所支付的现金,
    :param float cash_from_invest : 吸收投资收到的现金,
    :param float cash_from_borrowing : 取得借款收到的现金,
    :param float other_finance_act_cash : 收到其他与筹资活动有关的现金,
    :param float exchan_rate_change_effect : 汇率变动对现金的影响,
    :param float end_period_cash_equivalent : 现金等价物的期末余额,
    :param float cash_equivalent_increase : 现金及现金等价物净增加额,
    :param float begin_period_cash : 减：货币资金的期初余额,
    :param float operate_payable_increase : 经营性应付项目的增加,
    :param float fixed_asset_depreciation : 固定资产折旧,
    :param float net_profit : 净利润,
    :param float assets_depreciation_reserves : 加:资产减值准备,
    :param float accrued_expense_added : 预提费用的增加（减：减少）,
    :param float minority_profit : 少数股东损益,
    :param float fix_intanther_asset_dispo_loss : 处置固定资产、无形资产和其他长期资产的损失,
    :param float invest_loss : 投资损失(减：收益),
    :param float others : 其他,
    :param float financial_expense : 财务费用,
    :param float operate_receivable_decrease : 经营性应收项目的减少（减：增加）,
    :param float deferred_expense_decreased : 待摊费用的减少（减：增加）,
    :param float defered_tax_asset_decrease : 递延所得税资产减少,
    :param float deferred_expense_amort : 长期待摊费用的摊销,
    :param float defered_tax_liability_increase : 递延所得税负债增加,
    :param float net_operate_cash_flow_notes : (附注)经营活动产生的现金流量净额,
    :param float intangible_asset_amortization : 无形资产摊销,
    :param float inventory_decrease : 存货的减少(减：增加),
    :param float fixed_asset_scrap_loss : 固定资产报废损失(减：收益),
    :param float loss_from_fair_value_changes : 公允价值变动损失,
    :param float fixed_assets_finance_leases : 融资租入固定资产,
    :param float debt_to_captical : 债务转为资本,
    :param float cbs_expiring_within_one_year : 一年内到期的可转换公司债券,
    :param float net_incr_in_cash_and_equivalents : (附注)现金及现金等价物净增加额,
    :param float cash_equivalents_at_beginning : 减:现金等价物的期初余额,
    :param float cash_at_beginning_of_year : 减:现金的期初余额,
    :param float cash_equivalents_at_end_of_year : 加:现金等价物的期末余额,
    :param float cash_at_end_of_year : 现金的期末余额,

    代码调用:
        from hs_udata import financial_cashflow
financial_cashflow() 

    结果输出:
        
    """

    int_param =[]
    float_param =['net_deposit_in_cb_and_ib', 'other_operate_cash_paid', 'original_compensation_paid', 'net_loan_and_advance_increase', 'net_deal_trading_assets', 'net_cash_for_reinsurance', 'net_operate_cash_flow', 'policy_dividend_cash_paid', 'tax_levy_refund', 'interest_and_commission_cashin', 'all_taxes_paid', 'net_insurer_deposit_investment', 'goods_and_services_cash_paid', 'other_cashin_related_operate', 'subtotal_operate_cash_outflow', 'staff_behalf_paid', 'commission_cash_paid', 'net_original_insurance_cash', 'net_deposit_increase', 'net_buy_back', 'net_reinsurance_cash', 'goods_sale_service_render_cash', 'net_lend_capital', 'net_borrowing_from_central_bank', 'net_borrowing_from_finance_co', 'subtotal_operate_cash_inflow', 'invest_cash_paid', 'other_cash_from_invest_act', 'net_invest_cash_flow', 'subtotal_invest_cash_inflow', 'invest_withdrawal_cash', 'subtotal_invest_cash_outflow', 'invest_proceeds', 'net_cash_from_sub_company', 'fix_intan_other_asset_dispo_cash', 'fix_intan_other_asset_acqui_cash', 'other_cash_to_invest_act', 'net_cash_deal_sub_company', 'impawned_loan_net_increase', 'subtotal_finance_cash_outflow', 'other_finance_act_payment', 'subtotal_finance_cash_inflow', 'cash_from_bonds_issue', 'net_finance_cash_flow', 'dividend_interest_payment', 'borrowing_repayment', 'cash_from_invest', 'cash_from_borrowing', 'other_finance_act_cash', 'exchan_rate_change_effect', 'end_period_cash_equivalent', 'cash_equivalent_increase', 'begin_period_cash', 'operate_payable_increase', 'fixed_asset_depreciation', 'net_profit', 'assets_depreciation_reserves', 'accrued_expense_added', 'minority_profit', 'fix_intanther_asset_dispo_loss', 'invest_loss', 'others', 'financial_expense', 'operate_receivable_decrease', 'deferred_expense_decreased', 'defered_tax_asset_decrease', 'deferred_expense_amort', 'defered_tax_liability_increase', 'net_operate_cash_flow_notes', 'intangible_asset_amortization', 'inventory_decrease', 'fixed_asset_scrap_loss', 'loss_from_fair_value_changes', 'fixed_assets_finance_leases', 'debt_to_captical', 'cbs_expiring_within_one_year', 'net_incr_in_cash_and_equivalents', 'cash_equivalents_at_beginning', 'cash_at_beginning_of_year', 'cash_equivalents_at_end_of_year', 'cash_at_end_of_year']
    params = {
        "secu_code": secu_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "merge_type": merge_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_cashflow", url_path="finance_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("merge_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_income(secu_code=None, start_date=None, end_date=None, merge_type=None, fields=None):
    """
    利润表是反映企业在一定会计期间经营成果的报表，包含1.X营业利润、2.X综合收益总额、3.X营业支出、4.X营业收入
    、每股收益、6.X特别收益/收入、7.X利润总额、8.X净利润，8大模块组成。（无数值科目不出参）包括科创板；

    输入参数：
    :param str secu_code : 证券代码，默认"600570"
    :param str start_date : 开始日期，默认"two days ago"
    :param str end_date : 截止日期，默认"now"
    :param str merge_type : 合并类型，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str secu_market : 证券市场,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str company_type : 公司类型,
    :param str end_date : 截止日期,
    :param str report_type : 报告类型,
    :param str publ_date : 公告日期,
    :param float operating_profit : 营业利润,
    :param float non_operating_income : 加:营业外收入,
    :param float non_current_assetss_deal_loss : 其中：非流动资产处置净损失,
    :param float non_operating_expense : 减:营业外支出,
    :param float ci_parent_company_owners : 归属于母公司所有者的综合收益总额,
    :param float ci_minority_owners : 归属于少数股东的综合收益总额,
    :param float total_composite_income : 综合收益总额,
    :param float operating_tax_surcharges : 营业税金及附加,
    :param float operating_payout : 营业总支出,
    :param float amortization_premium_reserve : 减:摊回保险责任准备金,
    :param float financial_expense : 财务费用,
    :param float other_operating_cost : 其他业务成本,
    :param float operating_expense : 销售费用,
    :param float amortization_expense : 减:摊回赔付支出,
    :param float amortization_reinsurance_cost : 减:摊回分保费用,
    :param float administration_expense : 管理费用,
    :param float refunded_premiums : 退保金,
    :param float operating_cost : 营业成本,
    :param float premium_reserve : 提取保险责任准备金,
    :param float policy_dividend_payout : 保单红利支出,
    :param float asset_impairment_loss : 资产减值损失,
    :param float total_operating_cost : 营业总成本,
    :param float compensation_expense : 赔付支出,
    :param float reinsurance_cost : 分保费用,
    :param float insurance_commission_expense : 保险手续费及佣金支出,
    :param float premiums_income : 保险业务收入,
    :param float unearned_premium_reserve : 提取未到期责任准备金,
    :param float premiums_earned : 已赚保费,
    :param float total_operating_revenue : 营业总收入,
    :param float reinsurance : 减：分出保费,
    :param float net_subissue_secu_income : 其中：证券承销业务净收入,
    :param float other_operating_revenue : 其他营业收入,
    :param float operating_revenue : 营业收入,
    :param float net_proxy_secu_income : 其中：代理买卖证券业务净收入,
    :param float reinsurance_income : 其中:分保费收入,
    :param float net_commission_income : 手续费及佣金净收入,
    :param float net_interest_income : 利息净收入,
    :param float interest_income : 其中：利息收入,
    :param float commission_income : 其中：手续费及佣金收入,
    :param float interest_expense : 其中：利息支出,
    :param float commission_expense : 其中：手续费及佣金支出,
    :param float net_trust_income : 其中：受托客户资产管理业务净收入,
    :param float diluted_eps : 稀释每股收益,
    :param float basic_eps : 基本每股收益,
    :param float other_net_revenue : 非营业性收入,
    :param float invest_income_associates : 其中：对联营合营企业的投资收益,
    :param float invest_income : 投资净收益,
    :param float fair_value_change_income : 公允价值变动净收益,
    :param float exchange_income : 汇兑收益,
    :param float income_tax_cost : 减：所得税费用,
    :param float total_profit : 利润总额,
    :param float minority_profit : 少数股东损益,
    :param float net_profit : 净利润,
    :param float np_parent_company_owners : 归属于母公司所有者的净利润,

    代码调用:
        from hs_udata import financial_income
financial_income() 

    结果输出:
        
    """

    int_param =[]
    float_param =['operating_profit', 'non_operating_income', 'non_current_assetss_deal_loss', 'non_operating_expense', 'ci_parent_company_owners', 'ci_minority_owners', 'total_composite_income', 'operating_tax_surcharges', 'operating_payout', 'amortization_premium_reserve', 'financial_expense', 'other_operating_cost', 'operating_expense', 'amortization_expense', 'amortization_reinsurance_cost', 'administration_expense', 'refunded_premiums', 'operating_cost', 'premium_reserve', 'policy_dividend_payout', 'asset_impairment_loss', 'total_operating_cost', 'compensation_expense', 'reinsurance_cost', 'insurance_commission_expense', 'premiums_income', 'unearned_premium_reserve', 'premiums_earned', 'total_operating_revenue', 'reinsurance', 'net_subissue_secu_income', 'other_operating_revenue', 'operating_revenue', 'net_proxy_secu_income', 'reinsurance_income', 'net_commission_income', 'net_interest_income', 'interest_income', 'commission_income', 'interest_expense', 'commission_expense', 'net_trust_income', 'diluted_eps', 'basic_eps', 'other_net_revenue', 'invest_income_associates', 'invest_income', 'fair_value_change_income', 'exchange_income', 'income_tax_cost', 'total_profit', 'minority_profit', 'net_profit', 'np_parent_company_owners']
    params = {
        "secu_code": secu_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "merge_type": merge_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_income", url_path="finance_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("merge_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_balance(secu_code=None, start_date=None, end_date=None, merge_type=None, fields=None):
    """
    资产负债表亦称财务状况表，表示企业在一定日期的财务状况，包含1.X金融类资产、2.X金融类负债、3.X流动资金、4.
    X流动负债、5.X非流动资产、6.X非流动负债、7.X所有者权益（或股东权益）7大模块组成 。（无数值科目不出参）包括科创板；

    输入参数：
    :param str secu_code : 证券代码，默认"600570"
    :param str start_date : 开始日期，默认"two days ago"
    :param str end_date : 截止日期，默认"now"
    :param str merge_type : 合并类型，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_market : 证券市场,
    :param str company_type : 公司类型,
    :param str end_date : 截止日期,
    :param str report_type : 报告类型,
    :param str publ_date : 公告日期,
    :param float total_assets : 资产总计,
    :param float total_liability : 负债合计,
    :param float total_liability_and_equity : 负债和股东权益总计,
    :param float settlement_provi : 结算备付金,
    :param float client_provi : 客户备付金,
    :param float deposit_in_interbank : 存放同业款项,
    :param float r_metal : 贵金属,
    :param float lend_capital : 拆出资金,
    :param float derivative_assets : 衍生金融资产,
    :param float bought_sellback_assets : 买入返售金融资产,
    :param float loan_and_advance : 发放贷款和垫款,
    :param float insurance_receivables : 应收保费,
    :param float receivable_subrogation_fee : 应收代位追偿款,
    :param float reinsurance_receivables : 应收分保账款,
    :param float receivable_unearned_r : 应收分保未到期责任准备金,
    :param float receivable_claims_r : 应收分保未决赔款准备金,
    :param float receivable_life_r : 应收分保寿险责任准备金,
    :param float receivable_lt_health_r : 应收分保长期健康险责任准备金,
    :param float insurer_impawn_loan : 保户质押贷款,
    :param float fixed_deposit : 定期存款,
    :param float refundable_capital_deposit : 存出资本保证金,
    :param float refundable_deposit : 存出保证金,
    :param float independence_account_assets : 独立账户资产,
    :param float other_assets : 其他资产,
    :param float borrowing_from_centralbank : 向中央银行借款,
    :param float deposit_of_interbank : 同业及其他金融机构存放款项,
    :param float borrowing_capital : 拆入资金,
    :param float derivative_liability : 衍生金融负债,
    :param float sold_buyback_secu_proceeds : 卖出回购金融资产款,
    :param float deposit : 吸收存款,
    :param float proxy_secu_proceeds : 代理买卖证券款,
    :param float sub_issue_secu_proceeds : 代理承销证券款,
    :param float deposits_received : 存入保证金,
    :param float advance_insurance : 预收保费,
    :param float commission_payable : 应付手续费及佣金,
    :param float reinsurance_payables : 应付分保账款,
    :param float compensation_payable : 应付赔付款,
    :param float policy_dividend_payable : 应付保单红利,
    :param float insurer_deposit_investment : 保户储金及投资款,
    :param float unearned_premium_reserve : 未到期责任准备金,
    :param float outstanding_claim_reserve : 未决赔款准备金,
    :param float life_insurance_reserve : 寿险责任准备金,
    :param float lt_health_insurance_lr : 长期健康险责任准备金,
    :param float independence_liability : 独立账户负债,
    :param float other_liability : 其他负债,
    :param float cash_equivalents : 货币资金,
    :param float client_deposit : 客户资金存款,
    :param float trading_assets : 交易性金融资产,
    :param float bill_receivable : 应收票据,
    :param float dividend_receivable : 应收股利,
    :param float interest_receivable : 应收利息,
    :param float account_receivable : 应收账款,
    :param float other_receivable : 其他应收款,
    :param float advance_payment : 预付帐款,
    :param float inventories : 存货,
    :param float non_current_asset_in_one_year : 一年内到期的非流动资产,
    :param float other_current_assets : 其他流动资产,
    :param float total_current_assets : 流动资产合计,
    :param float shortterm_loan : 短期借款,
    :param float impawned_loan : 质押借款,
    :param float trading_liability : 交易性金融负债,
    :param float notes_payable : 应付票据,
    :param float accounts_payable : 应付账款,
    :param float advance_peceipts : 预收款项,
    :param float salaries_payable : 应付职工薪酬,
    :param float dividend_payable : 应付股利,
    :param float taxs_payable : 应交税费,
    :param float interest_payable : 应付利息,
    :param float other_payable : 其他应付款,
    :param float non_current_liability_in_one_year : 一年内到期的非流动负债,
    :param float other_current_liability : 其他流动负债,
    :param float total_current_liability : 流动负债合计,
    :param float hold_for_sale_assets : 可供出售金融资产,
    :param float hold_to_maturity_investments : 持有至到期投资,
    :param float investment_property : 投资性房地产,
    :param float longterm_equity_invest : 长期股权投资,
    :param float longterm_receivable_account : 长期应收款,
    :param float fixed_assets : 固定资产,
    :param float construction_materials : 工程物资,
    :param float constru_in_process : 在建工程,
    :param float fixed_assets_liquidation : 固定资产清理,
    :param float biological_assets : 生产性生物资产,
    :param float oil_gas_assets : 油气资产,
    :param float intangible_assets : 无形资产,
    :param float seat_costs : 交易席位费,
    :param float development_expenditure : 开发支出,
    :param float good_will : 商誉,
    :param float long_deferred_expense : 长期待摊费用,
    :param float deferred_tax_assets : 递延所得税资产,
    :param float other_non_current_assets : 其他非流动资产,
    :param float total_non_current_assets : 非流动资产合计,
    :param float longterm_loan : 长期借款,
    :param float bonds_payable : 应付债券,
    :param float longterm_account_payable : 长期应付款,
    :param float long_salaries_pay : 长期应付职工薪酬,
    :param float specific_account_payable : 专项应付款,
    :param float estimate_liability : 预计负债,
    :param float deferred_tax_liability : 递延所得税负债,
    :param float long_defer_income : 长期递延收益,
    :param float other_non_current_liability : 其他非流动负债,
    :param float total_non_current_liability : 非流动负债合计,
    :param float paidin_capital : 实收资本（或股本）,
    :param float other_equityinstruments : 其他权益工具,
    :param float capital_reserve_fund : 资本公积金,
    :param float surplus_reserve_fund : 盈余公积金,
    :param float retained_profit : 未分配利润,
    :param float treasury_stock : 减：库存股,
    :param float other_composite_income : 其他综合收益,
    :param float ordinary_risk_reserve_fund : 一般风险准备金,
    :param float foreign_currency_report_conv_diff : 外币报表折算差额,
    :param float specific_reserves : 专项储备,
    :param float se_without_mi : 归属母公司股东权益合计,
    :param float minority_interests : 少数股东权益,
    :param float total_shareholder_equity : 所有者权益合计,

    代码调用:
        from hs_udata import financial_balance
financial_balance() 

    结果输出:
        
    """

    int_param =[]
    float_param =['total_assets', 'total_liability', 'total_liability_and_equity', 'settlement_provi', 'client_provi', 'deposit_in_interbank', 'r_metal', 'lend_capital', 'derivative_assets', 'bought_sellback_assets', 'loan_and_advance', 'insurance_receivables', 'receivable_subrogation_fee', 'reinsurance_receivables', 'receivable_unearned_r', 'receivable_claims_r', 'receivable_life_r', 'receivable_lt_health_r', 'insurer_impawn_loan', 'fixed_deposit', 'refundable_capital_deposit', 'refundable_deposit', 'independence_account_assets', 'other_assets', 'borrowing_from_centralbank', 'deposit_of_interbank', 'borrowing_capital', 'derivative_liability', 'sold_buyback_secu_proceeds', 'deposit', 'proxy_secu_proceeds', 'sub_issue_secu_proceeds', 'deposits_received', 'advance_insurance', 'commission_payable', 'reinsurance_payables', 'compensation_payable', 'policy_dividend_payable', 'insurer_deposit_investment', 'unearned_premium_reserve', 'outstanding_claim_reserve', 'life_insurance_reserve', 'lt_health_insurance_lr', 'independence_liability', 'other_liability', 'cash_equivalents', 'client_deposit', 'trading_assets', 'bill_receivable', 'dividend_receivable', 'interest_receivable', 'account_receivable', 'other_receivable', 'advance_payment', 'inventories', 'non_current_asset_in_one_year', 'other_current_assets', 'total_current_assets', 'shortterm_loan', 'impawned_loan', 'trading_liability', 'notes_payable', 'accounts_payable', 'advance_peceipts', 'salaries_payable', 'dividend_payable', 'taxs_payable', 'interest_payable', 'other_payable', 'non_current_liability_in_one_year', 'other_current_liability', 'total_current_liability', 'hold_for_sale_assets', 'hold_to_maturity_investments', 'investment_property', 'longterm_equity_invest', 'longterm_receivable_account', 'fixed_assets', 'construction_materials', 'constru_in_process', 'fixed_assets_liquidation', 'biological_assets', 'oil_gas_assets', 'intangible_assets', 'seat_costs', 'development_expenditure', 'good_will', 'long_deferred_expense', 'deferred_tax_assets', 'other_non_current_assets', 'total_non_current_assets', 'longterm_loan', 'bonds_payable', 'longterm_account_payable', 'long_salaries_pay', 'specific_account_payable', 'estimate_liability', 'deferred_tax_liability', 'long_defer_income', 'other_non_current_liability', 'total_non_current_liability', 'paidin_capital', 'other_equityinstruments', 'capital_reserve_fund', 'surplus_reserve_fund', 'retained_profit', 'treasury_stock', 'other_composite_income', 'ordinary_risk_reserve_fund', 'foreign_currency_report_conv_diff', 'specific_reserves', 'se_without_mi', 'minority_interests', 'total_shareholder_equity']
    params = {
        "secu_code": secu_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "merge_type": merge_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_balance", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_gene_qincome(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    1.根据2007年新会计准则制定的一般企业利润表（单季度）模板，收录自公布季报以来公司的单季利润表情况。2.科目的计
    算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float total_operating_revenue : 单季度.营业总收入,
    :param float operating_revenue : 单季度.营业收入,
    :param float interest_income : 单季度.利息收入,
    :param float commission_income : 单季度.手续费及佣金收入,
    :param float premiums_earned : 单季度.已赚保费,
    :param float other_operating_revenue : 单季度.其他营业收入,
    :param float total_operating_cost : 单季度.营业总成本,
    :param float operating_cost : 单季度.营业成本,
    :param float interest_expense : 单季度.利息支出,
    :param float commission_expense : 单季度.手续费及佣金支出,
    :param float operating_expense : 单季度.销售费用,
    :param float administration_expense : 单季度. 管理费用,
    :param float financial_expense : 单季度.财务费用,
    :param float operating_tax_and_surcharges : 单季度.营业税金及附加,
    :param float asset_impairment_loss : 单季度.资产减值损失,
    :param float other_operating_cost : 单季度.其他营业成本,
    :param float invest_income : 单季度.投资收益,
    :param float invest_income_from_associates : 单季度.对联营合营企业的投资收益,
    :param float fair_value_change_income : 单季度.公允价值变动净收益,
    :param float operating_profit : 单季度.营业利润,
    :param float non_operating_income : 单季度.营业外收入,
    :param float non_operating_expense : 单季度.营业外支出,
    :param float non_current_assetss_deal_loss : 单季度. 非流动资产处置净损失,
    :param float total_profit : 单季度.利润总额,
    :param float income_tax_cost : 单季度.所得税费用,
    :param float uncertained_investment_loss : 单季度.未确认的投资损失,
    :param float net_profit : 单季度.净利润,
    :param float np_from_parent_company_owners : 单季度.归属于母公司所有者的净利润,
    :param float minority_profit : 单季度.少数股东损益,

    代码调用:
        from hs_udata import financial_gene_qincome
financial_gene_qincome() 

    结果输出:
        
    """

    int_param =[]
    float_param =['total_operating_revenue', 'operating_revenue', 'interest_income', 'commission_income', 'premiums_earned', 'other_operating_revenue', 'total_operating_cost', 'operating_cost', 'interest_expense', 'commission_expense', 'operating_expense', 'administration_expense', 'financial_expense', 'operating_tax_and_surcharges', 'asset_impairment_loss', 'other_operating_cost', 'invest_income', 'invest_income_from_associates', 'fair_value_change_income', 'operating_profit', 'non_operating_income', 'non_operating_expense', 'non_current_assetss_deal_loss', 'total_profit', 'income_tax_cost', 'uncertained_investment_loss', 'net_profit', 'np_from_parent_company_owners', 'minority_profit']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_gene_qincome", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_bank_qincome(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    1.根据2007年新会计准则制定的商业银行利润表（单季度）模板，收录自公布季报以来公司的单季利润表情况。2.科目的计
    算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）；

#### 基本信息

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float operating_revenue : 单季度.营业收入,
    :param float net_interest_income : 单季度.利息净收入,
    :param float interest_income : 单季度.利息收入,
    :param float interest_expense : 单季度.利息支出,
    :param float net_commission_income : 单季度.手续费及佣金净收入,
    :param float commission_income : 单季度.手续费及佣金收入,
    :param float commission_expense : 单季度.手续费及佣金支出,
    :param float invest_income : 单季度.投资收益,
    :param float invest_income_from_associates : 单季度.对联营合营企业的投资收益,
    :param float fair_value_change_income : 单季度.公允价值变动净收益,
    :param float exchange_income : 单季度.汇兑收益,
    :param float other_operating_income : 单季度.其他业务收入,
    :param float operating_payout : 单季度.营业支出,
    :param float operating_tax_and_surcharges : 单季度.营业税金及附加,
    :param float operating_and_admin_expense : 单季度.业务及管理费,
    :param float asset_impairment_loss : 单季度.资产减值损失,
    :param float other_operating_cost : 单季度.其他营业成本,
    :param float operating_profit : 单季度.营业利润,
    :param float non_operating_income : 单季度.营业外收入,
    :param float non_operating_expense : 单季度.营业外支出,
    :param float total_profit : 单季度.利润总额,
    :param float income_tax_cost : 单季度.所得税费用,
    :param float uncertained_investment_loss :  单季度.未确认的投资损失,
    :param float net_profit : 单季度.净利润,
    :param float np_from_parent_company_owners : 单季度.归属于母公司所有者的净利润,
    :param float minority_profit : 单季度.少数股东损益,

    代码调用:
        from hs_udata import financial_bank_qincome
financial_bank_qincome() 

    结果输出:
        
    """

    int_param =[]
    float_param =['operating_revenue', 'net_interest_income', 'interest_income', 'interest_expense', 'net_commission_income', 'commission_income', 'commission_expense', 'invest_income', 'invest_income_from_associates', 'fair_value_change_income', 'exchange_income', 'other_operating_income', 'operating_payout', 'operating_tax_and_surcharges', 'operating_and_admin_expense', 'asset_impairment_loss', 'other_operating_cost', 'operating_profit', 'non_operating_income', 'non_operating_expense', 'total_profit', 'income_tax_cost', 'uncertained_investment_loss', 'net_profit', 'np_from_parent_company_owners', 'minority_profit']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_bank_qincome", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_secu_qincome(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    1.根据2007年新会计准则制定的证券公司利润表（单季度）模板，收录自公布季报以来公司的单季利润表情况。2.科目的计
    算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float operating_revenue : 单季度.营业收入,
    :param float net_commission_income : 单季度.手续费及佣金净收入,
    :param float net_proxy_secu_income : 单季度.代理买卖证券业务净收入,
    :param float net_sub_issue_secu_income : 单季度.证券承销业务净收入,
    :param float net_trust_income : 单季度.受托客户资产管理业务净收入,
    :param float net_interest_income : 单季度.利息净收入,
    :param float invest_income : 单季度.投资收益,
    :param float invest_income_from_associates : 单季度.对联营合营企业的投资收益,
    :param float fair_value_change_income : 单季度.公允价值变动净收益,
    :param float exchange_income : 单季度.汇兑收益,
    :param float other_operating_income : 单季度.其他业务收入,
    :param float operating_payout : 单季度.营业支出,
    :param float operating_tax_and_surcharges : 单季度.营业税金及附加,
    :param float operating_and_admin_expense : 单季度.业务及管理费,
    :param float asset_impairment_loss : 单季度.资产减值损失,
    :param float other_operating_cost : 单季度.其他营业成本,
    :param float operating_profit : 单季度.营业利润,
    :param float non_operating_income : 单季度.营业外收入,
    :param float non_operating_expense : 单季度.营业外支出,
    :param float total_profit : 单季度.利润总额,
    :param float income_tax_cost : 单季度.所得税费用,
    :param float net_profit : 单季度.净利润,
    :param float np_from_parent_company_owners : 单季度.归属于母公司所有者的净利润,
    :param float minority_profit : 单季度.少数股东损益,

    代码调用:
        from hs_udata import financial_secu_qincome
financial_secu_qincome() 

    结果输出:
        
    """

    int_param =[]
    float_param =['operating_revenue', 'net_commission_income', 'net_proxy_secu_income', 'net_sub_issue_secu_income', 'net_trust_income', 'net_interest_income', 'invest_income', 'invest_income_from_associates', 'fair_value_change_income', 'exchange_income', 'other_operating_income', 'operating_payout', 'operating_tax_and_surcharges', 'operating_and_admin_expense', 'asset_impairment_loss', 'other_operating_cost', 'operating_profit', 'non_operating_income', 'non_operating_expense', 'total_profit', 'income_tax_cost', 'net_profit', 'np_from_parent_company_owners', 'minority_profit']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_secu_qincome", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_insu_qincome(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    1.根据2007年新会计准则制定的保险公司利润表（单季度）模板，收录自公布季报以来公司的单季利润表情况。2.科目的计
    算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param float operating_revenue : 单季度.营业收入,
    :param float premiums_earned : 单季度.已赚保费,
    :param float premiums_income : 单季度.保险业务收入,
    :param float reinsurance_income : 单季度.分保费收入,
    :param float reinsurance : 单季度.分出保费,
    :param float unearned_premium_reserve : 单季度.提取未到期责任准备金,
    :param float invest_income : 单季度.投资收益,
    :param float invest_income_from_associates : 单季度.对联营合营企业的投资收益,
    :param float fair_value_change_income : 单季度.公允价值变动净收益,
    :param float exchange_income : 单季度.汇兑收益,
    :param float other_operating_income : 单季度.其他业务收入,
    :param float operating_payout : 单季度.营业支出,
    :param float refunded_premiums : 单季度.退保金,
    :param float compensation_expense : 单季度.赔付支出,
    :param float amortization_expense : 单季度.摊回赔付支出,
    :param float premium_reserve : 单季度.提取保险责任准备金,
    :param float amortization_premium_reserve : 单季度.摊回保险责任准备金,
    :param float policy_dividend_payout : 单季度.保单红利支出,
    :param float reinsurance_cost : 单季度.分保费用,
    :param float insurance_commission_expense : 单季度.保险手续费及佣金支出,
    :param float operating_tax_and_surcharges : 单季度.营业税金及附加,
    :param float operating_and_admin_expense : 单季度.业务及管理费,
    :param float amortization_reinsurance_cost : 单季度.摊回分保费用,
    :param float asset_impairment_loss : 单季度.资产减值损失,
    :param float other_operating_cost : 单季度.其他营业成本,
    :param float operating_profit : 单季度.营业利润,
    :param float non_operating_income : 单季度.营业外收入,
    :param float non_operating_expense : 单季度.营业外支出,
    :param float total_profit : 单季度.利润总额,
    :param float net_profit : 单季度.净利润,
    :param float np_from_parent_company_owners : 单季度.归属于母公司所有者的净利润,
    :param float minority_profit : 单季度.少数股东损益,

    代码调用:
        from hs_udata import financial_insu_qincome
financial_insu_qincome() 

    结果输出:
        
    """

    int_param =[]
    float_param =['operating_revenue', 'premiums_earned', 'premiums_income', 'reinsurance_income', 'reinsurance', 'unearned_premium_reserve', 'invest_income', 'invest_income_from_associates', 'fair_value_change_income', 'exchange_income', 'other_operating_income', 'operating_payout', 'refunded_premiums', 'compensation_expense', 'amortization_expense', 'premium_reserve', 'amortization_premium_reserve', 'policy_dividend_payout', 'reinsurance_cost', 'insurance_commission_expense', 'operating_tax_and_surcharges', 'operating_and_admin_expense', 'amortization_reinsurance_cost', 'asset_impairment_loss', 'other_operating_cost', 'operating_profit', 'non_operating_income', 'non_operating_expense', 'total_profit', 'net_profit', 'np_from_parent_company_owners', 'minority_profit']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_insu_qincome", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_gene_qcashflow(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    1.根据2007年新会计准则制定的一般企业现金流量表（单季度）模板，收录自公布季报以来公司的单季现金流量表情况。2.
    科目的计算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float goods_sale_and_service_render_cash : 单季度.销售商品、提供劳务收到的现金,
    :param float tax_levy_refund : 单季度.收到的税费返还,
    :param float other_cashin_related_operate : 单季度.收到其他与经营活动有关的现金,
    :param float subtotal_operate_cash_inflow : 单季度.经营活动现金流入小计,
    :param float goods_and_services_cash_paid : 单季度.购买商品、接受劳务支付的现金,
    :param float staff_behalf_paid : 单季度.支付给职工以及为职工支付的现金,
    :param float all_taxes_paid : 单季度.支付的各项税费,
    :param float other_operate_cash_paid : 单季度.支付其他与经营活动有关的现金,
    :param float subtotal_operate_cash_outflow : 单季度.经营活动现金流出小计,
    :param float net_operate_cash_flow : 单季度.经营活动产生的现金流量净额,
    :param float invest_withdrawal_cash : 单季度.收回投资收到的现金,
    :param float invest_proceeds : 单季度.取得投资收益收到的现金,
    :param float fix_intan_other_asset_dispo_cash : 单季度.处置固定资产、无形资产和其他长期资产收回的现金净额,
    :param float net_cash_deal_subcompany : 单季度.处置子公司及其他营业单位收到的现金净额,
    :param float other_cash_from_invest_act : 单季度.收到其他与投资活动有关的现金,
    :param float subtotal_invest_cash_inflow : 单季度.投资活动现金流入小计,
    :param float fix_intan_other_asset_acqui_cash : 单季度.购建固定资产、无形资产和其他长期资产支付的现金,
    :param float invest_cash_paid : 单季度.投资支付的现金,
    :param float net_cash_from_sub_company : 单季度.取得子公司及其他营业单位支付的现金净额,
    :param float impawned_loan_net_increase : 单季度.质押贷款净增加额,
    :param float other_cash_to_invest_act : 单季度.支付其他与投资活动有关的现金,
    :param float subtotal_invest_cash_outflow : 单季度.投资活动现金流出小计,
    :param float net_invest_cash_flow : 单季度.投资活动产生的现金流量净额,
    :param float cash_from_invest : 单季度.吸收投资收到的现金,
    :param float cash_from_bonds_issue : 单季度.发行债券收到的现金,
    :param float cash_from_borrowing : 单季度.取得借款收到的现金,
    :param float other_finance_act_cash : 单季度.收到其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_inflow : 单季度.筹资活动现金流入小计,
    :param float borrowing_repayment : 单季度.偿还债务支付的现金,
    :param float dividend_interest_payment : 单季度.分配股利、利润或偿付利息支付的现金,
    :param float other_finance_act_payment : 单季度.支付其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_outflow : 单季度.筹资活动现金流出小计,
    :param float net_finance_cash_flow : 单季度.筹资活动产生的现金流量净额,
    :param float exchange_rate_change_effect : 单季度.汇率变动对现金及现金等价物的影响,
    :param float cash_equivalent_increase : 单季度.现金及现金等价物净增加额,

    代码调用:
        from hs_udata import financial_gene_qcashflow
financial_gene_qcashflow() 

    结果输出:
        
    """

    int_param =[]
    float_param =['goods_sale_and_service_render_cash', 'tax_levy_refund', 'other_cashin_related_operate', 'subtotal_operate_cash_inflow', 'goods_and_services_cash_paid', 'staff_behalf_paid', 'all_taxes_paid', 'other_operate_cash_paid', 'subtotal_operate_cash_outflow', 'net_operate_cash_flow', 'invest_withdrawal_cash', 'invest_proceeds', 'fix_intan_other_asset_dispo_cash', 'net_cash_deal_subcompany', 'other_cash_from_invest_act', 'subtotal_invest_cash_inflow', 'fix_intan_other_asset_acqui_cash', 'invest_cash_paid', 'net_cash_from_sub_company', 'impawned_loan_net_increase', 'other_cash_to_invest_act', 'subtotal_invest_cash_outflow', 'net_invest_cash_flow', 'cash_from_invest', 'cash_from_bonds_issue', 'cash_from_borrowing', 'other_finance_act_cash', 'subtotal_finance_cash_inflow', 'borrowing_repayment', 'dividend_interest_payment', 'other_finance_act_payment', 'subtotal_finance_cash_outflow', 'net_finance_cash_flow', 'exchange_rate_change_effect', 'cash_equivalent_increase']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_gene_qcashflow", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_bank_qcashflow(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    1.根据2007年新会计准则制定的商业银行现金流量表（单季度）模板，收录自公布季报以来公司的单季现金流量表情况。2.
    科目的计算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float net_deposit_increase : 单季度.客户存款和同业存放款项净增加额,
    :param float net_borrowing_from_central_bank : 单季度.向中央银行借款净增加额,
    :param float net_borrowing_from_finance_co : 单季度.向其他金融机构拆入资金净增加额,
    :param float interest_and_commission_cashin : 单季度.收取利息、手续费及佣金的现金,
    :param float other_cashin_related_operate : 单季度.收到其他与经营活动有关的现金,
    :param float subtotal_operate_cash_inflow : 单季度.经营活动现金流入小计,
    :param float net_loan_and_advance_increase : 单季度.客户贷款及垫款净增加额,
    :param float net_deposit_in_cb_and_ib : 单季度.存放中央银行和同业款项净增加额,
    :param float net_lend_capital : 单季度.拆出资金净增加额,
    :param float commission_cash_paid : 单季度.支付手续费及佣金的现金,
    :param float staff_behalf_paid : 单季度.支付给职工以及为职工支付的现金,
    :param float all_taxes_paid : 单季度.支付的各项税费,
    :param float other_operate_cash_paid : 单季度.支付其他与经营活动有关的现金,
    :param float subtotal_operate_cash_outflow : 单季度.经营活动现金流出小计,
    :param float net_operate_cash_flow : 单季度.经营活动产生的现金流量净额,
    :param float invest_withdrawal_cash : 单季度.收回投资收到的现金,
    :param float invest_proceeds : 单季度.取得投资收益收到的现金,
    :param float fix_intan_other_asset_dispo_cash : 单季度.处置固定资产、无形资产和其他长期资产收回的现金净额,
    :param float net_cash_deal_subcompany : 单季度.处置子公司及其他营业单位收到的现金净额,
    :param float other_cash_from_invest_act : 单季度.收到其他与投资活动有关的现金,
    :param float subtotal_invest_cash_inflow : 单季度.投资活动现金流入小计,
    :param float fix_intan_other_asset_acqui_cash : 单季度.购建固定资产、无形资产和其他长期资产支付的现金,
    :param float invest_cash_paid : 单季度.投资支付的现金,
    :param float net_cash_from_sub_company : 单季度.取得子公司及其他营业单位支付的现金净额,
    :param float other_cash_to_invest_act : 单季度.支付其他与投资活动有关的现金,
    :param float subtotal_invest_cash_outflow : 单季度.投资活动现金流出小计,
    :param float net_invest_cash_flow : 单季度.投资活动产生的现金流量净额,
    :param float cash_from_invest : 单季度.吸收投资收到的现金,
    :param float cash_from_bonds_issue : 单季度.发行债券收到的现金,
    :param float cash_from_borrowing : 单季度.取得借款收到的现金,
    :param float other_finance_act_cash : 单季度.收到其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_inflow : 单季度.筹资活动现金流入小计,
    :param float borrowing_repayment : 单季度.偿还债务支付的现金,
    :param float dividend_interest_payment : 单季度.分配股利、利润或偿付利息支付的现金,
    :param float other_finance_act_payment : 单季度.支付其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_outflow : 单季度.筹资活动现金流出小计,
    :param float net_finance_cash_flow : 单季度.筹资活动产生的现金流量净额,
    :param float exchange_rate_change_effect : 单季度.汇率变动对现金及现金等价物的影响,
    :param float cash_equivalent_increase : 现金及现金等价物净增加额,

    代码调用:
        from hs_udata import financial_bank_qcashflow
financial_bank_qcashflow() 

    结果输出:
        
    """

    int_param =[]
    float_param =['net_deposit_increase', 'net_borrowing_from_central_bank', 'net_borrowing_from_finance_co', 'interest_and_commission_cashin', 'other_cashin_related_operate', 'subtotal_operate_cash_inflow', 'net_loan_and_advance_increase', 'net_deposit_in_cb_and_ib', 'net_lend_capital', 'commission_cash_paid', 'staff_behalf_paid', 'all_taxes_paid', 'other_operate_cash_paid', 'subtotal_operate_cash_outflow', 'net_operate_cash_flow', 'invest_withdrawal_cash', 'invest_proceeds', 'fix_intan_other_asset_dispo_cash', 'net_cash_deal_subcompany', 'other_cash_from_invest_act', 'subtotal_invest_cash_inflow', 'fix_intan_other_asset_acqui_cash', 'invest_cash_paid', 'net_cash_from_sub_company', 'other_cash_to_invest_act', 'subtotal_invest_cash_outflow', 'net_invest_cash_flow', 'cash_from_invest', 'cash_from_bonds_issue', 'cash_from_borrowing', 'other_finance_act_cash', 'subtotal_finance_cash_inflow', 'borrowing_repayment', 'dividend_interest_payment', 'other_finance_act_payment', 'subtotal_finance_cash_outflow', 'net_finance_cash_flow', 'exchange_rate_change_effect', 'cash_equivalent_increase']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_bank_qcashflow", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_secu_qcashflow(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    1.根据2007年新会计准则制定的证券公司现金流量表（单季度）模板，收录公布季报以来公司的单季现金流量表情况。2.科
    目的计算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据，各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float net_deal_trading_assets : 单季度.处置交易性金融资产净增加额,
    :param float interest_and_commission_cashin : 单季度.收取利息、手续费及佣金的现金,
    :param float net_borrowing_from_finance_co : 单季度.拆入资金净增加额,
    :param float other_cashin_related_operate : 单季度.收到其他与经营活动有关的现金,
    :param float subtotal_operate_cash_inflow : 单季度.经营活动现金流入小计,
    :param float commission_cash_paid : 单季度.支付手续费及佣金的现金,
    :param float net_lend_capital : 单季度.拆出资金净增加额,
    :param float staff_behalf_paid : 单季度.支付给职工以及为职工支付的现金,
    :param float all_taxes_paid : 单季度.支付的各项税费,
    :param float other_operate_cash_paid : 单季度.支付其他与经营活动有关的现金,
    :param float subtotal_operate_cash_outflow : 单季度.经营活动现金流出小计,
    :param float net_operate_cash_flow : 单季度.经营活动产生的现金流量净额,
    :param float invest_withdrawal_cash : 单季度.收回投资收到的现金,
    :param float invest_proceeds : 单季度.取得投资收益收到的现金,
    :param float fix_intan_other_asset_dispo_cash : 单季度.处置固定资产、无形资产和其他长期资产收回的现金净额,
    :param float net_cash_deal_subcompany : 单季度.处置子公司及其他营业单位收到的现金净额,
    :param float other_cash_from_invest_act : 单季度.收到其他与投资活动有关的现金,
    :param float subtotal_invest_cash_inflow : 单季度.投资活动现金流入小计,
    :param float fix_intan_other_asset_acqui_cash : 单季度.购建固定资产、无形资产和其他长期资产支付的现金,
    :param float invest_cash_paid : 单季度.投资支付的现金,
    :param float net_cash_from_sub_company : 单季度.取得子公司及其他营业单位支付的现金净额,
    :param float other_cash_to_invest_act : 单季度.支付其他与投资活动有关的现金,
    :param float subtotal_invest_cash_outflow : 单季度.投资活动现金流出小计,
    :param float net_invest_cash_flow : 单季度.投资活动产生的现金流量净额,
    :param float cash_from_invest : 单季度.吸收投资收到的现金,
    :param float cash_from_bonds_issue : 单季度.发行债券收到的现金,
    :param float cash_from_borrowing : 单季度.取得借款收到的现金,
    :param float other_finance_act_cash : 单季度.收到其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_inflow : 单季度.筹资活动现金流入小计,
    :param float borrowing_repayment : 单季度.偿还债务支付的现金,
    :param float dividend_interest_payment : 单季度.分配股利、利润或偿付利息支付的现金,
    :param float other_finance_act_payment : 单季度.支付其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_outflow : 单季度.筹资活动现金流出小计,
    :param float net_finance_cash_flow : 单季度.筹资活动产生的现金流量净额,
    :param float exchange_rate_change_effect : 单季度.汇率变动对现金及现金等价物的影响,
    :param float cash_equivalent_increase : 单季度.现金及现金等价物净增加额,

    代码调用:
        from hs_udata import financial_secu_qcashflow
financial_secu_qcashflow() 

    结果输出:
        
    """

    int_param =[]
    float_param =['net_deal_trading_assets', 'interest_and_commission_cashin', 'net_borrowing_from_finance_co', 'other_cashin_related_operate', 'subtotal_operate_cash_inflow', 'commission_cash_paid', 'net_lend_capital', 'staff_behalf_paid', 'all_taxes_paid', 'other_operate_cash_paid', 'subtotal_operate_cash_outflow', 'net_operate_cash_flow', 'invest_withdrawal_cash', 'invest_proceeds', 'fix_intan_other_asset_dispo_cash', 'net_cash_deal_subcompany', 'other_cash_from_invest_act', 'subtotal_invest_cash_inflow', 'fix_intan_other_asset_acqui_cash', 'invest_cash_paid', 'net_cash_from_sub_company', 'other_cash_to_invest_act', 'subtotal_invest_cash_outflow', 'net_invest_cash_flow', 'cash_from_invest', 'cash_from_bonds_issue', 'cash_from_borrowing', 'other_finance_act_cash', 'subtotal_finance_cash_inflow', 'borrowing_repayment', 'dividend_interest_payment', 'other_finance_act_payment', 'subtotal_finance_cash_outflow', 'net_finance_cash_flow', 'exchange_rate_change_effect', 'cash_equivalent_increase']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_secu_qcashflow", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def financial_insu_qcashflow(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    根据2007年新会计准则制定的保险公司现金流量表（单季度）模板，收录自公布季报以来公司的单季现金流量表情况。2.科目
    的计算方法：第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据）；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float net_original_insurance_cash : 单季度.收到原保险合同保费取得的现金,
    :param float net_reinsurance_cash : 单季度.收到再保业务现金净额,
    :param float net_insurer_deposit_investment : 单季度.保户储金及投资款净增加额,
    :param float tax_levy_refund : 单季度.收到的税费返还,
    :param float other_cashin_related_operate : 单季度.收到其他与经营活动有关的现金,
    :param float subtotal_operate_cash_inflow : 单季度.经营活动现金流入小计,
    :param float commission_cash_paid : 单季度.支付手续费及佣金的现金,
    :param float original_compensation_paid : 单季度.支付原保险合同赔付款项的现金,
    :param float net_cash_for_reinsurance : 单季度.支付再保业务现金净额,
    :param float policy_dividend_cash_paid : 单季度.支付保单红利的现金,
    :param float staff_behalf_paid : 单季度.支付给职工以及为职工支付的现金,
    :param float all_taxes_paid : 单季度.支付的各项税费,
    :param float other_operate_cash_paid : 单季度.支付其他与经营活动有关的现金,
    :param float subtotal_operate_cash_outflow : 单季度.经营活动现金流出小计,
    :param float net_operate_cash_flow : 单季度.经营活动产生的现金流量净额,
    :param float invest_withdrawal_cash : 单季度.收回投资收到的现金,
    :param float invest_proceeds : 单季度.取得投资收益收到的现金,
    :param float fix_intan_other_asset_dispo_cash : 单季度.处置固定资产、无形资产和其他长期资产收回的现金净额,
    :param float net_cash_deal_subcompany : 单季度.处置子公司及其他营业单位收到的现金净额,
    :param float other_cash_from_invest_act : 单季度.收到其他与投资活动有关的现金,
    :param float subtotal_invest_cash_inflow : 单季度.投资活动现金流入小计,
    :param float fix_intan_other_asset_acqui_cash : 单季度.购建固定资产、无形资产和其他长期资产支付的现金,
    :param float invest_cash_paid : 单季度.投资支付的现金,
    :param float net_cash_from_sub_company : 单季度.取得子公司及其他营业单位支付的现金净额,
    :param float impawned_loan_net_increase : 单季度.质押贷款净增加额,
    :param float other_cash_to_invest_act : 单季度.支付其他与投资活动有关的现金,
    :param float subtotal_invest_cash_outflow : 单季度.投资活动现金流出小计,
    :param float net_invest_cash_flow : 单季度.投资活动产生的现金流量净额,
    :param float cash_from_invest : 单季度.吸收投资收到的现金,
    :param float cash_from_bonds_issue : 单季度.发行债券收到的现金,
    :param float cash_from_borrowing : 单季度.取得借款收到的现金,
    :param float other_finance_act_cash : 单季度.收到其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_inflow : 单季度.筹资活动现金流入小计,
    :param float borrowing_repayment : 单季度.偿还债务支付的现金,
    :param float dividend_interest_payment : 单季度.分配股利、利润或偿付利息支付的现金,
    :param float other_finance_act_payment : 单季度.支付其他与筹资活动有关的现金,
    :param float subtotal_finance_cash_outflow : 单季度.筹资活动现金流出小计,
    :param float net_finance_cash_flow : 单季度.筹资活动产生的现金流量净额,
    :param float exchange_rate_change_effect : 单季度.汇率变动对现金及现金等价物的影响,
    :param float cash_equivalent_increase : 单季度.现金及现金等价物净增加额,

    代码调用:
        from hs_udata import financial_insu_qcashflow
financial_insu_qcashflow() 

    结果输出:
        
    """

    int_param =[]
    float_param =['net_original_insurance_cash', 'net_reinsurance_cash', 'net_insurer_deposit_investment', 'tax_levy_refund', 'other_cashin_related_operate', 'subtotal_operate_cash_inflow', 'commission_cash_paid', 'original_compensation_paid', 'net_cash_for_reinsurance', 'policy_dividend_cash_paid', 'staff_behalf_paid', 'all_taxes_paid', 'other_operate_cash_paid', 'subtotal_operate_cash_outflow', 'net_operate_cash_flow', 'invest_withdrawal_cash', 'invest_proceeds', 'fix_intan_other_asset_dispo_cash', 'net_cash_deal_subcompany', 'other_cash_from_invest_act', 'subtotal_invest_cash_inflow', 'fix_intan_other_asset_acqui_cash', 'invest_cash_paid', 'net_cash_from_sub_company', 'impawned_loan_net_increase', 'other_cash_to_invest_act', 'subtotal_invest_cash_outflow', 'net_invest_cash_flow', 'cash_from_invest', 'cash_from_bonds_issue', 'cash_from_borrowing', 'other_finance_act_cash', 'subtotal_finance_cash_inflow', 'borrowing_repayment', 'dividend_interest_payment', 'other_finance_act_payment', 'subtotal_finance_cash_outflow', 'net_finance_cash_flow', 'exchange_rate_change_effect', 'cash_equivalent_increase']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("financial_insu_qcashflow", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("forecast_object").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def performance_forecast(en_prod_code=None, report_date=None, forecast_object=None, fields=None):
    """
    统计上市公司对未来报告期本公司业绩的预计情况，包括业绩预计类型、预计内容、具体预计值等，并收录了实际指标和研究员的一
    致性预测值；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str forecast_object : 预告对象，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param str result_statement : 业绩预告摘要,
    :param str forcast_type : 业绩预告类型,
    :param str publ_date : 业绩预告日期,
    :param str forcast_content : 业绩预告内容,
    :param float eprofit_ceiling : 预计净利润上限,
    :param float eprofit_floor : 预计净利润下限,
    :param float egrowth_rate_ceiling : 变动幅度上限,
    :param float egrowth_rate_floor : 变动幅度下限,
    :param float eeps_ceiling : 预计每股收益上限,
    :param float eeps_floor : 预计每股收益下限,
    :param float basic_eps : 去年同期每股收益,
    :param float np_yoy_consistent_forecast : 一致预期净利润增幅,

    代码调用:
        from hs_udata import performance_forecast
performance_forecast() 

    结果输出:
        
    """

    int_param =[]
    float_param =['eprofit_ceiling', 'eprofit_floor', 'egrowth_rate_ceiling', 'egrowth_rate_floor', 'eeps_ceiling', 'eeps_floor', 'basic_eps', 'np_yoy_consistent_forecast']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "forecast_object": forecast_object,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("performance_forecast", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def performance_letters(en_prod_code=None, report_date=None, fields=None):
    """
    收录上市公司在业绩快报中披露的主要财务数据和指标；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param str period_mark : 业绩快报类型,
    :param str publ_date : 业绩快报披露日,
    :param float operating_revenue : 营业收入,
    :param float operating_profit : 营业利润,
    :param float total_profit : 利润总额,
    :param float np_parent_company_owners : 归属母公司股东的净利润,
    :param float net_profit_cut : 扣除非经常性损益后的净利润,
    :param float net_operate_cash_flow : 经营活动现金流量净额,
    :param float basic_eps : 每股收益-基本,
    :param float roe : 净资产收益率-摊薄,
    :param float roe_weighted : 净资产收益率-加权,
    :param float net_asset_ps : 每股净资产,
    :param float net_operate_cash_flow_ps : 每股经营活动现金流量净额,
    :param float total_assets : 总资产,
    :param float se_without_mi : 归属上市公司股东的所有者权益,
    :param float total_shares : 总股本,
    :param float operating_revenue_yoy : 主营业务收入同比,
    :param float gross_profit_yoy : 主营业务利润同比,
    :param float operating_profit_yoy : 营业利润同比,
    :param float np_parent_company_owners_yoy : 归属母公司净利润同比,
    :param float net_profit_cut_yoy : 扣除非经常性损益后净利润同比,
    :param float basic_eps_yoy : 每股收益(摊薄) 同比,
    :param float roe_weighted_yoy : 净资产收益率(加权) 同比,
    :param float net_asset_ps_to_opening : 每股净资产较期初比,
    :param float total_assets_to_opening : 总资产较期初比,
    :param float se_without_mi_to_opening : 归属母公司股东权益较期初比,

    代码调用:
        from hs_udata import performance_letters
performance_letters() 

    结果输出:
        
    """

    int_param =[]
    float_param =['operating_revenue', 'operating_profit', 'total_profit', 'np_parent_company_owners', 'net_profit_cut', 'net_operate_cash_flow', 'basic_eps', 'roe', 'roe_weighted', 'net_asset_ps', 'net_operate_cash_flow_ps', 'total_assets', 'se_without_mi', 'total_shares', 'operating_revenue_yoy', 'gross_profit_yoy', 'operating_profit_yoy', 'np_parent_company_owners_yoy', 'net_profit_cut_yoy', 'basic_eps_yoy', 'roe_weighted_yoy', 'net_asset_ps_to_opening', 'total_assets_to_opening', 'se_without_mi_to_opening']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("performance_letters", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def performance_letters_q(en_prod_code=None, report_date=None, fields=None):
    """
    通过上市公司在业绩快报中披露的主要财务数据和指标，计算单季度主要财务指标；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float operating_revenue_d : 营业收入（单季度）,
    :param float operating_profit_d : 营业利润（单季度）,
    :param float total_profit_d : 利润总额（单季度）,
    :param float np_parent_company_owners_d : 归属母公司股东的净利润（单季度）,
    :param float net_profit_cut_d : 扣除非经常性损益净利润（单季度）,
    :param float operating_revenue_div : 主营业务收入单季度同比,
    :param float operating_profit_div : 营业利润单季度同比,
    :param float total_profit_div : 利润总额单季度同比,
    :param float np_parent_company_owners_div : 归属母公司股东的净利润单季度同比,
    :param float net_profit_cut_div : 扣除非经常性损益后净利润单季度同比,
    :param float operating_revenue_mom : 主营业务收入单季度环比,
    :param float operating_profit_mom : 营业利润单季度环比,
    :param float total_profit_mom : 利润总额单季度环比,
    :param float np_parent_company_owners_mom : 归属母公司股东的净利润单季度环比,
    :param float net_profit_cut_div_mom : 扣除非经常性损益后净利润单季度环比,

    代码调用:
        from hs_udata import performance_letters_q
performance_letters_q() 

    结果输出:
        
    """

    int_param =[]
    float_param =['operating_revenue_d', 'operating_profit_d', 'total_profit_d', 'np_parent_company_owners_d', 'net_profit_cut_d', 'operating_revenue_div', 'operating_profit_div', 'total_profit_div', 'np_parent_company_owners_div', 'net_profit_cut_div', 'operating_revenue_mom', 'operating_profit_mom', 'total_profit_mom', 'np_parent_company_owners_mom', 'net_profit_cut_div_mom']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("performance_letters_q", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("classification").is_instance((str, None.__class__)),
    check("order").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def main_composition(en_prod_code=None, report_date=None, classification=None, order=None, fields=None):
    """
    按报告期统计上市公司主营业务构成情况，支持同时输入多个股票代码或报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str classification : 分类，默认"0"
    :param str order : 页内记录排序规则，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param str main_oper_income : 主营业务收入金额占比,
    :param str moi_project : 主营构成（按行业）-项目名称,
    :param float moi_main_oper_income : 主营构成（按行业）-项目收入,
    :param float moi_main_oper_cost : 主营构成（按行业）-项目成本,
    :param float moi_moc : 主营构成（按行业）-项目利润,
    :param str mop_project : 主营构成（按产品）-项目名称,
    :param float mop_main_oper_income : 主营构成（按产品）-项目收入,
    :param float mop_main_oper_cost : 主营构成（按产品）-项目成本,
    :param float mop_moc : 主营构成（按产品）-项目利润,
    :param str mor_project : 主营构成（按地区）-项目名称,
    :param float mor_main_oper_income : 主营构成（按地区）-项目收入,
    :param float mor_main_oper_cost : 主营构成（按地区）-项目成本,
    :param float mor_moc : 主营构成（按地区）-项目利润,

    代码调用:
        from hs_udata import main_composition
main_composition() 

    结果输出:
        
    """

    int_param =[]
    float_param =['moi_main_oper_income', 'moi_main_oper_cost', 'moi_moc', 'mop_main_oper_income', 'mop_main_oper_cost', 'mop_moc', 'mor_main_oper_income', 'mor_main_oper_cost', 'mor_moc']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "classification": classification,
        "order": order,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("main_composition", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def trading_parties(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    统计公司向前5名供应商的采购情况及向前5名客户的销售情况等，支持同时输入多个股票代码或报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float operating_revenue_top5_customers : 营业收入-前5名客户,
    :param float operating_revenue_rate_top5_customers : 营业收入占比-前5名客户,
    :param float main_oper_income_rate_top5_customers : 主营业务收入占比-前5名客户,
    :param float purchase_top5_supplier : 采购额-前5名供应商,
    :param float purchase_rate_top5_supplier : 采购额占比-前5名供应商,
    :param float main_oper_cost_rate_top5_supplier : 主营业务成本占比-前5名供应商,

    代码调用:
        from hs_udata import trading_parties
trading_parties() 

    结果输出:
        
    """

    int_param =[]
    float_param =['operating_revenue_top5_customers', 'operating_revenue_rate_top5_customers', 'main_oper_income_rate_top5_customers', 'purchase_top5_supplier', 'purchase_rate_top5_supplier', 'main_oper_cost_rate_top5_supplier']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("trading_parties", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def audit_opinion(en_prod_code=None, report_date=None, fields=None):
    """
    中介机构对公司季度、半年度、年度经营情况的评价，包括公司招股以来的历次纪录，支持同时输入多个股票代码或报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param str accounting_firm : 审计单位,
    :param str signature_accountant : 签字注册会计师,
    :param str audit_opinion_type : 审计意见,

    代码调用:
        from hs_udata import audit_opinion
audit_opinion() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("audit_opinion", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def per_share_index(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    根据报告期公布的财务科目数据衍生而来的每股指标，若某个报告期的数据有多次调整，则该表展示最新合并调整数据；若某报告期
    暂未披露调整后数据，则展示调整前的合并数据，支持同时输入多个股票代码和报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float basic_eps : 每股收益EPS-基本,
    :param float diluted_eps : 每股收益EPS-稀释,
    :param float basic_eps_cut : 每股收益EPS-扣除／基本,
    :param float diluted_eps_cut : 每股收益EPS-扣除／稀释,
    :param float naps : 每股净资产BPS,
    :param float net_operate_cash_flow_ps : 每股经营活动产生的现金流量净额,
    :param float np_parent_company_owners_t : 每股收益EPS-期末股本摊薄,
    :param float new_np_parent_company_owners_t : 每股收益EPS-最新股本摊薄,
    :param float net_profit_cut_t : 每股收益EPS-扣除/期末股本摊薄,
    :param float new_net_profit_cut_t : 每股收益EPS-扣除/最新股本摊薄,
    :param float eps_ttm : 每股收益EPS（TTM）,
    :param float se_without_mi_t : 每股净资产BPS（最新股本摊薄）,
    :param float net_operate_cash_flow_ps_ttm : 每股经营活动产生的现金流量净额_TTM,
    :param float total_operating_revenue_ps : 每股营业总收入,
    :param float operating_revenue_ps : 每股营业收入,
    :param float operating_revenue_ps_ttm : 每股营业收入（TTM）,
    :param float ebit_ps : 每股息税前利润,
    :param float capital_surplus_fund_ps : 每股资本公积,
    :param float surplus_reserve_fund_ps : 每股盈余公积,
    :param float undivided_profit : 每股未分配利润,
    :param float retained_earnings_ps : 每股留存收益,
    :param float cash_flowps : 每股现金流量净额,
    :param float cash_flowps_ttm : 每股现金流量净额（TTM）,
    :param float enterprise_fcf_ps : 每股企业自由现金流量,
    :param float shareholder_fcf_ps : 每股股东自由现金流量,

    代码调用:
        from hs_udata import per_share_index
per_share_index() 

    结果输出:
        
    """

    int_param =[]
    float_param =['basic_eps', 'diluted_eps', 'basic_eps_cut', 'diluted_eps_cut', 'naps', 'net_operate_cash_flow_ps', 'np_parent_company_owners_t', 'new_np_parent_company_owners_t', 'net_profit_cut_t', 'new_net_profit_cut_t', 'eps_ttm', 'se_without_mi_t', 'net_operate_cash_flow_ps_ttm', 'total_operating_revenue_ps', 'operating_revenue_ps', 'operating_revenue_ps_ttm', 'ebit_ps', 'capital_surplus_fund_ps', 'surplus_reserve_fund_ps', 'undivided_profit', 'retained_earnings_ps', 'cash_flowps', 'cash_flowps_ttm', 'enterprise_fcf_ps', 'shareholder_fcf_ps']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("per_share_index", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def profitability(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    根据报告期公布的财务科目数据衍生而来盈利能力相关指标，若某个报告期的数据有多次调整，则该表展示最新合并调整数据；若某
    报告期暂未披露调整后数据，则展示调整前的合并数据，支持同时输入多个股票代码和报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param float roe : 净资产收益率ROE-摊薄（公布值）,
    :param float roe_weighted : 净资产收益率ROE-加权（公布值）,
    :param float roe_avg : 净资产收益率-平均,
    :param float roe_cut : 净资产收益率_扣除,摊薄,
    :param float roe_cut_weighted : 净资产收益率（扣除-加权）,
    :param float roe_cut_avg : 净资产收益率ROE（扣除-平均）,
    :param float roe_avg_year : 净资产收益率-年化,
    :param float net_profit_cut_sewi : 净资产收益率ROE-增发条件,
    :param float total_assets : 总资产报酬率,
    :param float total_assets_year : 总资产报酬率-年化,
    :param float roa : 总资产净利率ROA,
    :param float roa_year : 总资产净利率-年化,
    :param float roic : 投入资本回报率,
    :param float roic_ttm : 投入资本回报率（TTM）,
    :param float rop : 人力投入回报率,
    :param float net_profit_ratio : 销售净利率,
    :param float gross_income_ratio : 销售毛利率,
    :param float sales_cost_ratio : 销售成本率,
    :param float period_costs_rate : 销售期间费用率,
    :param float total_profit_cost_ratio : 成本费用利润率,
    :param float np_to_tor : 净利润／营业总收入,
    :param float operating_profit_to_tor : 营业利润／营业总收入,
    :param float ebit_to_tor : 息税前利润／营业总收入,
    :param float ebitda : 息税折旧摊销前利润,
    :param float t_operating_cost_to_tor : 营业总成本／营业总收入,
    :param float operating_expense_rate : 销售费用／营业总收入,
    :param float admini_expense_rate : 管理费用／营业总收入,
    :param float financial_expense_rate : 财务费用／营业总收入,
    :param float asset_impa_loss_to_tor : 资产减值损失／营业总收入,
    :param float asset_impa_loss_or : 资产减值损失／营业利润,
    :param float roe_ttm : 净资产收益率ROE（TTM）,
    :param float roa_ebit_ttm : 总资产收益率ROA（TTM）,
    :param float roa_ttm : 总资产净利率（TTM）,
    :param float net_profit_ratio_ttm : 销售净利率_TTM,
    :param float gross_income_ratio_ttm : 销售毛利率（TTM）,
    :param float period_costs_rate_ttm : 销售期间费用率_TTM,
    :param float np_to_tor_ttm : 净利润／营业总收入_TTM,
    :param float operating_profit_to_tor_ttm : 营业利润／营业总收入_TTM,
    :param float ebit_to_tor_ttm : 息税前利润／营业总收入_TTM,
    :param float t_operating_cost_to_tor_ttm : 营业总成本／营业总收入_TTM,
    :param float operating_expense_rate_ttm : 销售费用／营业总收入_TTM,
    :param float admini_expense_rate_ttm : 管理费用／营业总收入_TTM,
    :param float financial_expense_rate_ttm : 财务费用／营业总收入_TTM,
    :param float asset_impa_loss_to_tor_ttm : 资产减值损失／营业总收入_TTM,
    :param float asset_impa_loss_or_ttm : 资产减值损失／营业利润（TTM）,

    代码调用:
        from hs_udata import profitability
profitability() 

    结果输出:
        
    """

    int_param =[]
    float_param =['roe', 'roe_weighted', 'roe_avg', 'roe_cut', 'roe_cut_weighted', 'roe_cut_avg', 'roe_avg_year', 'net_profit_cut_sewi', 'total_assets', 'total_assets_year', 'roa', 'roa_year', 'roic', 'roic_ttm', 'rop', 'net_profit_ratio', 'gross_income_ratio', 'sales_cost_ratio', 'period_costs_rate', 'total_profit_cost_ratio', 'np_to_tor', 'operating_profit_to_tor', 'ebit_to_tor', 'ebitda', 't_operating_cost_to_tor', 'operating_expense_rate', 'admini_expense_rate', 'financial_expense_rate', 'asset_impa_loss_to_tor', 'asset_impa_loss_or', 'roe_ttm', 'roa_ebit_ttm', 'roa_ttm', 'net_profit_ratio_ttm', 'gross_income_ratio_ttm', 'period_costs_rate_ttm', 'np_to_tor_ttm', 'operating_profit_to_tor_ttm', 'ebit_to_tor_ttm', 't_operating_cost_to_tor_ttm', 'operating_expense_rate_ttm', 'admini_expense_rate_ttm', 'financial_expense_rate_ttm', 'asset_impa_loss_to_tor_ttm', 'asset_impa_loss_or_ttm']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("profitability", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def growth_capacity(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    获根据报告期公布的财务科目数据衍生出的衡量成长能力的相关指标，主要从同比角度分析，展示同比增长率。若某个报告期的数据
    有多次调整，则该表展示最新合并调整数据；若某报告期暂未披露调整后数据，则展示调整前的合并数据，支持同时输入多个股票代码和报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float basic_eps : 每股收益-基本（同比增长率）,
    :param float diluted_eps : 每股收益-稀释（同比增长率）,
    :param float net_operate_cash_flow_ps : 每股经营活动产生的现金流量净额（同比增长率）,
    :param float total_operating_revenue : 营业总收入（同比增长率）,
    :param float operating_revenue : 营业收入（同比增长率）,
    :param float operating_cost : 营业成本（同比增长率）,
    :param float gross_profit : 毛利（同比增长率）,
    :param float operating_profit : 营业利润（同比增长率）,
    :param float total_profit : 利润总额（同比增长率）,
    :param float net_profit : 净利润（同比增长率）,
    :param float np_parent_company_owners : 归属母公司股东的净利润（同比增长率）,
    :param float np_parent_non_recu : 归属母公司股东的净利润扣除非经常损益（同比增长率）,
    :param float net_operate_cash_flow : 经营活动产生的现金流量净额（同比增长率）,
    :param float roe : 净资产收益率（同比增长率）,
    :param float goods_sale_service_render_cash : 销售商品、提供劳务收到的现金（同比增长率）,
    :param float goods_and_services_cash_paid : 购买商品、接受劳务支付的现金（同比增长率）,
    :param float staff_behalf_paid : 支付给职工以及为职工支付的现金（同比增长率）,
    :param float net_profit_cashcover : 净利润现金含量（同比增长率）,
    :param float se_without_mi : 净资产（同比增长率）,
    :param float total_liability : 总负债（同比增长率）,
    :param float total_assets : 总资产（同比增长率）,
    :param float cash_equivalent_increase : 现金净流量（同比增长率）,

    代码调用:
        from hs_udata import growth_capacity
growth_capacity() 

    结果输出:
        
    """

    int_param =[]
    float_param =['basic_eps', 'diluted_eps', 'net_operate_cash_flow_ps', 'total_operating_revenue', 'operating_revenue', 'operating_cost', 'gross_profit', 'operating_profit', 'total_profit', 'net_profit', 'np_parent_company_owners', 'np_parent_non_recu', 'net_operate_cash_flow', 'roe', 'goods_sale_service_render_cash', 'goods_and_services_cash_paid', 'staff_behalf_paid', 'net_profit_cashcover', 'se_without_mi', 'total_liability', 'total_assets', 'cash_equivalent_increase']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("growth_capacity", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def du_pont_analysis(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    根据报告期公布的财务科目数据，利用杜邦分析方法衍生衡量公司主要财务分析指标，若某个报告期的数据有多次调整，则该表展示
    最新合并调整数据；若某报告期暂未披露调整后数据，则展示调整前的合并数据，支持同时输入多个股票代码和报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float np_parent_sew : 权益净利率ROE,
    :param float net_profit_ratio : 销售净利率,
    :param float operating_ni_to_tp : 净利润/利润总额,
    :param float total_profit_ebit : 利润总额/息税前利润,
    :param float ebit_to_tor : 息税前利润／营业总收入,
    :param float operating_revenue_ta : 资产周转率,
    :param float equity_multipler : 权益乘数,
    :param float np_parent_company_owners_ratio : 归属于母公司股东的净利润占比,

    代码调用:
        from hs_udata import du_pont_analysis
du_pont_analysis() 

    结果输出:
        
    """

    int_param =[]
    float_param =['np_parent_sew', 'net_profit_ratio', 'operating_ni_to_tp', 'total_profit_ebit', 'ebit_to_tor', 'operating_revenue_ta', 'equity_multipler', 'np_parent_company_owners_ratio']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("du_pont_analysis", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def deri_fin_indicators(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    统计由上市公司的主要会计科目（合并报表）衍生出来的数据，三大财务报表中任意报表在某报告期的数据经历调整/修订，则该表
    相关字段展示每个历史调整数据；未经历调整/修订的报表相关字段则沿用未调整数据，支持同时输入多个股票代码和报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float interest_free_curr_liabilities : 无息流动负债,
    :param float interest_free_non_curr_liabilities : 无息非流动负债,
    :param float interest_bear_debt : 带息债务,
    :param float net_debt : 净债务,
    :param float total_paid_in_capital : 全部投入资本,
    :param float working_capital : 营运资本,
    :param float net_working_capital : 净营运资本,
    :param float net_tangible_assets : 有形资产净值,
    :param float retained_earnings : 留存收益,
    :param float non_recurring_profit_loss : 非经常性损益,
    :param float net_profit_cut : 扣除非经常性损益后的净利润,
    :param float gross_profit : 毛利,
    :param float net_income_from_operating : 经营活动净收益,
    :param float net_income_from_value_change : 价值变动净收益,
    :param float ebit : 息税前利润,
    :param float ebitda : 息税折旧摊销前利润,
    :param float total_operating_revenue_ttm : 营业总收入(TTM),
    :param float total_operating_cost_ttm : 营业总成本(TTM),
    :param float operating_revenue_ttm : 营业收入(TTM),
    :param float operating_cost_ttm : 营业成本-非金融类(TTM),
    :param float operating_payout_ttm : 营业支出-金融类(TTM),
    :param float gross_profit_ttm : 毛利(TTM),
    :param float operating_expense_ttm : 销售费用(TTM),
    :param float administration_expense_ttm : 管理费用(TTM),
    :param float financial_expense_ttm : 财务费用(TTM),
    :param float asset_impairment_loss_ttm : 资产减值损失(TTM),
    :param float net_income_from_operating_ttm : 经营活动净收益(TTM),
    :param float net_income_from_value_change_ttm : 价值变动净收益(TTM),
    :param float operating_profit_ttm : 营业利润(TTM),
    :param float net_non_operating_income_ttm : 营业外收支净额(TTM),
    :param float ebit_ttm : 息税前利润(TTM),
    :param float total_profit_ttm : 利润总额(TTM),
    :param float net_profit_ttm : 净利润TTM,
    :param float np_parent_company_owners_ttm : 归属于母公司所有者的净利润TTM,
    :param float free_cash_flow_to_firm : 企业自由现金流量FCFF,
    :param float free_cash_flow_to_equity : 股权自由现金流量FCFE,
    :param float current_accrued_da : 当期计提折旧与摊销,
    :param float sale_service_render_cash_ttm : 销售商品提供劳务收到的现金(TTM),
    :param float net_operate_cash_flow_ttm : 经营活动现金净流量(TTM),
    :param float net_invest_cash_flow_ttm : 投资活动现金净流量(TTM),
    :param float net_finance_cash_flow_ttm : 筹资活动现金净流量(TTM),
    :param float net_cash_flow_ttm : 现金净流量(TTM),

    代码调用:
        from hs_udata import deri_fin_indicators
deri_fin_indicators() 

    结果输出:
        
    """

    int_param =[]
    float_param =['interest_free_curr_liabilities', 'interest_free_non_curr_liabilities', 'interest_bear_debt', 'net_debt', 'total_paid_in_capital', 'working_capital', 'net_working_capital', 'net_tangible_assets', 'retained_earnings', 'non_recurring_profit_loss', 'net_profit_cut', 'gross_profit', 'net_income_from_operating', 'net_income_from_value_change', 'ebit', 'ebitda', 'total_operating_revenue_ttm', 'total_operating_cost_ttm', 'operating_revenue_ttm', 'operating_cost_ttm', 'operating_payout_ttm', 'gross_profit_ttm', 'operating_expense_ttm', 'administration_expense_ttm', 'financial_expense_ttm', 'asset_impairment_loss_ttm', 'net_income_from_operating_ttm', 'net_income_from_value_change_ttm', 'operating_profit_ttm', 'net_non_operating_income_ttm', 'ebit_ttm', 'total_profit_ttm', 'net_profit_ttm', 'np_parent_company_owners_ttm', 'free_cash_flow_to_firm', 'free_cash_flow_to_equity', 'current_accrued_da', 'sale_service_render_cash_ttm', 'net_operate_cash_flow_ttm', 'net_invest_cash_flow_ttm', 'net_finance_cash_flow_ttm', 'net_cash_flow_ttm']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("deri_fin_indicators", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def q_financial_indicator(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    本表收录自公布公司的单季主要财务指标，第一、三季度直接取公布值；第二季度数据＝半年度数据－第一季度数据；第四季度数据
    ＝年度数据－前三季度数据。各期的原始数据均取合并后的最新数据（有调整的为最新调整后数据），支持同时输入多个股票代码和报告期；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float eps : 单季度.每股收益EPS,
    :param float net_profit_cut : 扣除非经常性损益后的净利润,
    :param float net_income_from_operating : 单季度.经营活动净收益,
    :param float net_income_from_value_change : 单季度.价值变动净收益,
    :param float np_f_se_without_mi : 单季度.净资产收益率ROE,
    :param float net_profit_nrp_swe : 单季度.净资产收益率（扣除非经常损益） ,
    :param float roa : 单季度.总资产净利率ROA,
    :param float net_profit_ratio : 单季度.销售净利率,
    :param float gross_income_ratio : 单季度.销售毛利率,
    :param float t_operating_cost_to_tor : 营业总成本／营业总收入,
    :param float operating_profit_to_tor : 营业利润／营业总收入,
    :param float np_to_tor : 单季度.净利润/营业总收入,
    :param float operating_expense_rate : 单季度.销售费用/营业总收入,
    :param float admini_expense_rate : 单季度.管理费用/营业总收入,
    :param float financial_expense_rate : 单季度.财务费用/营业总收入,
    :param float asset_impa_loss_or : 单季度.资产减值损失/营业利润,
    :param float operating_ni_to_tp : 单季度.经营活动净收益/利润总额 ,
    :param float value_change_ni_to_tp : 单季度.价值变动净收益/利润总额,
    :param float np_cut_to_tp : 单季度.扣除非经常损益后的净利润/净利润 ,
    :param float sale_service_cash_to_or : 单季度.销售商品提供劳务收到的现金/营业收入,
    :param float cash_rate_of_sales : 单季度.经营活动产生的现金流量净额/营业收入,
    :param float net_operate_cash_flow_rate : 单季度.经营活动产生的现金流量净额占比,
    :param float net_invest_cash_flow_rate : 单季度.投资活动产生的现金流量净额占比,
    :param float net_finance_cash_flow_rate : 单季度.筹资活动产生的现金流量净额占比,
    :param float oper_cycle : 营业周期,
    :param float inventory_turnover_rate : 存货周转率,
    :param float inventory_turnover_days : 存货周转天数,
    :param float accounts_receivables_turnover_rate : 应收帐款周转率,
    :param float accounts_receivables_turnover_days : 应收帐款周转天数,
    :param float total_asset_turnover_rate : 总资产周转率,
    :param float current_assets_turnover_rate : 流动资产周转率,
    :param float fixed_asset_turnover_rate : 固定资产周转率,
    :param float eps_yoy : 单季度.每股收益EPS同比增长率 ,
    :param float eps_mom : 单季度.每股收益EPS环比增长率 ,
    :param float total_operating_revenue_yoy : 单季度.营业总收入同比增长率,
    :param float total_operating_revenue_mom : 单季度.营业总收入环比增长率,
    :param float operating_revenue_yoy : 单季度.营业收入同比增长率,
    :param float operating_revenue_mom : 单季度.营业收入环比增长率,
    :param float operating_cost_yoy : 单季度.营业成本同比增长率,
    :param float operating_cost_mom : 单季度.营业成本环比增长率,
    :param float gross_profit_yoy : 单季度.毛利同比增长率,
    :param float gross_profit_mom : 单季度.毛利环比增长率,
    :param float operating_profit_yoy : 单季度.营业利润同比增长率 ,
    :param float operating_profit_mom : 单季度.营业利润环比增长率 ,
    :param float net_profit_yoy : 单季度.净利润同比增长率 ,
    :param float net_profit_mom : 单季度.净利润环比增长率 ,
    :param float np_parent_company_cut_yoy : 单季度.归属母公司股东的净利润同比增长率,
    :param float np_parent_company_cut_mom : 单季度.归属母公司股东的净利润环比增长率,
    :param float net_profit_cut_yoy : 单季度.扣除非经常性损益后的净利润同比增长率,
    :param float net_profit_cut_mom : 单季度.扣除非经常性损益后的净利润环比增长率,
    :param float cash_equivalent_increase_yoy : 单季度.现金净流量同比增长率,
    :param float cash_equivalent_increase_mom : 单季度.现金净流量环比增长率,
    :param float net_operate_cash_flow_yoy : 单季度.经营性现金净流量同比增长率,
    :param float net_operate_cash_flow_mom : 单季度.经营性现金净流量环比增长率,

    代码调用:
        from hs_udata import q_financial_indicator
q_financial_indicator() 

    结果输出:
        
    """

    int_param =[]
    float_param =['eps', 'net_profit_cut', 'net_income_from_operating', 'net_income_from_value_change', 'np_f_se_without_mi', 'net_profit_nrp_swe', 'roa', 'net_profit_ratio', 'gross_income_ratio', 't_operating_cost_to_tor', 'operating_profit_to_tor', 'np_to_tor', 'operating_expense_rate', 'admini_expense_rate', 'financial_expense_rate', 'asset_impa_loss_or', 'operating_ni_to_tp', 'value_change_ni_to_tp', 'np_cut_to_tp', 'sale_service_cash_to_or', 'cash_rate_of_sales', 'net_operate_cash_flow_rate', 'net_invest_cash_flow_rate', 'net_finance_cash_flow_rate', 'oper_cycle', 'inventory_turnover_rate', 'inventory_turnover_days', 'accounts_receivables_turnover_rate', 'accounts_receivables_turnover_days', 'total_asset_turnover_rate', 'current_assets_turnover_rate', 'fixed_asset_turnover_rate', 'eps_yoy', 'eps_mom', 'total_operating_revenue_yoy', 'total_operating_revenue_mom', 'operating_revenue_yoy', 'operating_revenue_mom', 'operating_cost_yoy', 'operating_cost_mom', 'gross_profit_yoy', 'gross_profit_mom', 'operating_profit_yoy', 'operating_profit_mom', 'net_profit_yoy', 'net_profit_mom', 'np_parent_company_cut_yoy', 'np_parent_company_cut_mom', 'net_profit_cut_yoy', 'net_profit_cut_mom', 'cash_equivalent_increase_yoy', 'cash_equivalent_increase_mom', 'net_operate_cash_flow_yoy', 'net_operate_cash_flow_mom']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("q_financial_indicator", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("year").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def valuation_info(en_prod_code=None, trading_date=None, year=None, fields=None):
    """
    利用定期报告中披露的财务指标对上市公司做估值分析，主要包括股息率、市净率、市销率、市现率等额指标，支持同时输入多个股
    票代码；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"2020-12-31"
    :param str year : 年度，默认"2020"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float total_market_value : 总市值,
    :param float total_market_value2 : 总市值2,
    :param float total_market_value_zjh : 总市值（证监会算法）,
    :param float pe_ttm : 市盈率PE（TTM）,
    :param float pe_ttm_deduct_non_recurring_profit : 市盈率PE（TTM,扣除非经常性损益）,
    :param float pe_rate_lyr : 市盈率（最新年报，LYR）,
    :param float pb_lf : 市净率PB（最新财报，LF）,
    :param float ps_ttm : 市销率PS（TTM）,
    :param float ps_lyr : 市销率PS（最新年报，LYR）,
    :param float pcf_oper_cashflow_ttm : 市现率PCF（经营现金流TTM）,
    :param float pcf_net_cashflow_ttm : 市现率PCF（现金净流量TTM）,
    :param float pcf_oper_cashflow_lyr : 市现率PCF（经营现金流LYR）,
    :param float pcf_net_cashflow_lyr : 市现率PCF（经营净流量LYR）,
    :param float dividend_rate : 股息率（年初至最新报告期）,
    :param float total_cash_divi_com_rate_rmb : 股息率（近12个月）,
    :param float total_cash_divi_com_rate_rmb2 : 股息率,

    代码调用:
        from hs_udata import valuation_info
valuation_info() 

    结果输出:
        
    """

    int_param =[]
    float_param =['total_market_value', 'total_market_value2', 'total_market_value_zjh', 'pe_ttm', 'pe_ttm_deduct_non_recurring_profit', 'pe_rate_lyr', 'pb_lf', 'ps_ttm', 'ps_lyr', 'pcf_oper_cashflow_ttm', 'pcf_net_cashflow_ttm', 'pcf_oper_cashflow_lyr', 'pcf_net_cashflow_lyr', 'dividend_rate', 'total_cash_divi_com_rate_rmb', 'total_cash_divi_com_rate_rmb2']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "year": year,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("valuation_info", url_path="finance_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def corporation_value(en_prod_code=None, trading_date=None, fields=None):
    """
    统计上市公司A股市值、B股市值、企业价值等指标，支持同时输入多个股票代码；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"600570.SH"
    :param str trading_date : 交易日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float enterprise_value1 : 企业价值（含货币资金）,
    :param float enterprise_value2 : 企业价值（剔除货币资金）,
    :param float enterprise_times : 企业倍数,
    :param float total_market_value : 总市值（不可回测）,
    :param float a_shares_market_value : A股市值（含限售股）,
    :param float a1_shares_market_value : A股市值（不含限售股）,
    :param float b_shares_market_value : B股市值（含限售股，交易币种）,
    :param float b_shares_market_value_rmb : B股市值（含限售股，人民币）,
    :param float b1_shares_market_value : B股市值（不含限售股，交易币种）,
    :param float b1_shares_market_value_rmb : B股市值（不含限售股，人民币）,

    代码调用:
        from hs_udata import corporation_value
corporation_value() 

    结果输出:
        
    """

    int_param =[]
    float_param =['enterprise_value1', 'enterprise_value2', 'enterprise_times', 'total_market_value', 'a_shares_market_value', 'a1_shares_market_value', 'b_shares_market_value', 'b_shares_market_value_rmb', 'b1_shares_market_value', 'b1_shares_market_value_rmb']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("corporation_value", url_path="finance_data", **params)

@args_check(
    check("report_status").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def star_ipodeclare(report_status=None, fields=None):
    """
    

    输入参数：
    :param str report_status : 申报状态，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str accept_date : 受理日期,
    :param str report_status : 申报状态,
    :param str industry_code_csrc : 所属证监会行业代码,
    :param str industry_name_csrc : 所属证监会行业名称,
    :param str sponsor_institution : 保荐机构,
    :param str accounting_firm : 会计师事务所,
    :param str law_firm : 律师事务所,
    :param str page_no : 页面编号,
    :param str page_count : 页内记录数,

    代码调用:
        from hs_udata import star_ipodeclare
star_ipodeclare() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "report_status": report_status,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("star_ipodeclare", url_path="star_market", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def star_companyprofile(secu_code=None, fields=None):
    """
    

    输入参数：
    :param str secu_code : 证券代码，默认"X21398"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str chi_name : 公司名称,
    :param str eng_name : 英文名称,
    :param str establishment_date : 成立日期,
    :param str uniform_social_credit_code : 统一社会信用代码,
    :param str legal_repr : 法人代表,
    :param float regcapital : 注册资本(元),
    :param str reg_addr : 注册地址,
    :param str province : 注册地省份,
    :param str general_manager : 总经理,
    :param str secretary : 董事会秘书,
    :param str contact_tel : 联系电话,
    :param str email : 公司邮箱,
    :param str website : 网址,
    :param str brief_intro : 公司简介,
    :param str industry_name_csrc : 所属证监会行业名称,

    代码调用:
        from hs_udata import star_companyprofile
star_companyprofile() 

    结果输出:
        
    """

    int_param =[]
    float_param =['regcapital']
    params = {
        "secu_code": secu_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("star_companyprofile", url_path="star_market", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def neeq_basic(en_prod_code=None, fields=None):
    """
    

    输入参数：
    :param str en_prod_code : 证劵代码，默认"400002.OC"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_category : 证券类别,
    :param str listed_date : 挂牌日期,
    :param str trans_type : 交易类型,
    :param str listed_state : 上市状态,
    :param str secu_market : 证券市场,
    :param str listed_sector : 上市板块,
    :param str isin_code : ISIN代码,

    代码调用:
        from hs_udata import neeq_basic
neeq_basic() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("neeq_basic", url_path="neeq", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def neeq_company(en_prod_code=None, fields=None):
    """
    

    输入参数：
    :param str en_prod_code : 证劵代码，默认"400002.OC"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str chi_name : 公司中文名称,
    :param str eng_name : 公司英文名称,
    :param str establishment_date : 公司成立日期,
    :param str regcapital : 注册资本,
    :param str legal_repr : 法人代表,
    :param str major_business : 主营业务,
    :param str minor_business : 经营范围-兼营,
    :param str state : 省份,
    :param str city_code : 地级行政区,
    :param str reg_addr : 公司注册地址 公司注册地址,
    :param str reg_zip_code : 公司注册地址邮编,
    :param str offece_addr : 公司办公地址,
    :param str office_zip : 公司办公地址邮编,
    :param str tel : 联系电话,
    :param str fax : 传真,
    :param str email : 电子邮件,
    :param str website : 公司网址,
    :param str disclosure_web : 信息披露网址,
    :param str disclosure_paper : 信息披露报纸,
    :param str business_reg_number : 工商登记号,
    :param str economic_nature : 经济性质,
    :param str company_nature : 企业性质,
    :param str company_cval : 企业属性,
    :param str company_type : 公司类型,
    :param str brief_intro : 公司介绍,
    :param str reg_org : 登记机关,

    代码调用:
        from hs_udata import neeq_company
neeq_company() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("neeq_company", url_path="neeq", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def neeq_leader(en_prod_code=None, fields=None):
    """
    

    输入参数：
    :param str en_prod_code : 证劵代码，默认"400002.OC"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str chairman_current : 董事长(现任),
    :param str chairman_former : 董事长(历任),
    :param str general_manager_current : 总经理(现任),
    :param str general_manager_former : 总经理(历任),
    :param str chief_financial_officer_current : 财务总监(现任),
    :param str chief_financial_officer_former : 财务总监(历任),
    :param str secretary_current : 董事会秘书(现任),
    :param str secretary_former : 董事会秘书(历任),

    代码调用:
        from hs_udata import neeq_leader
neeq_leader() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("neeq_leader", url_path="neeq", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def neeq_leader_num(en_prod_code=None, end_date=None, fields=None):
    """
    

    输入参数：
    :param str en_prod_code : 证劵代码，默认"400005.OC"
    :param str end_date : 截止日期，默认"2015-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str end_date : 截止日期,
    :param float bd_number : 董事会成员数量,
    :param float bs_number : 监事会成员数量,
    :param float manager_number : 高级管理人员数量,

    代码调用:
        from hs_udata import neeq_leader_num
neeq_leader_num() 

    结果输出:
        
    """

    int_param =[]
    float_param =['bd_number', 'bs_number', 'manager_number']
    params = {
        "en_prod_code": en_prod_code,
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("neeq_leader_num", url_path="neeq", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("level").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def neeq_industry(en_prod_code=None, level=None, fields=None):
    """
    

    输入参数：
    :param str en_prod_code : 证劵代码，默认"400001.OC"
    :param str level : 等级，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param float level : 等级,
    :param str industry_code_csrc : 所属证监会行业代码,
    :param str industry_name_csrc : 所属证监会行业名称,
    :param str industry_code : 行业类,
    :param str industry_name : 行业类名称,
    :param str industry_code_neeq_management : 所属三板管理型行业代码,
    :param str industry_name_neeq_management : 所属三板管理型行业名称,
    :param str industry_code_neeq_investment : 所属三板投资型行业代码,
    :param str industry_name_neeq_investment : 所属三板投资型行业名称,

    代码调用:
        from hs_udata import neeq_industry
neeq_industry() 

    结果输出:
        
    """

    int_param =[]
    float_param =['level']
    params = {
        "en_prod_code": en_prod_code,
        "level": level,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("neeq_industry", url_path="neeq", **params)

@args_check(
    check("secu_abbr").is_instance((str, None.__class__)),
    check("symbols").is_instance((str, None.__class__)),
    check("foundation_type").is_instance((str, None.__class__)),
    check("float_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_list(secu_abbr=None, symbols=None, foundation_type=None, float_type=None, fields=None):
    """
    提供所有的分级基金，场内和场外基金列表；

    输入参数：
    :param str secu_abbr : 基金简称
    :param str symbols : 基金代码
    :param str foundation_type : 基金运作方式
    :param str float_type : 发售方式
    :param str fields : 输出字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str foundation_type : 基金运作方式,
    :param str secu_abbr : 证券简称,
    :param str fund_company_name : 基金公司名称,
    :param str float_type : 发售方式,
    :param str fund_company_code : 基金公司代码,
    :param str fund_full_name : 基金全称,
    :param str fund_company_abbr : 基金公司简称,

    代码调用:
        from hs_udata import fund_list
fund_list() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "secu_abbr": secu_abbr,
        "symbols": symbols,
        "foundation_type": foundation_type,
        "float_type": float_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_list", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_manager_company(en_prod_code=None, end_date=None, fields=None):
    """
    提供查询基金的基金经理信息，返回基金经理的名字、任职日、背景等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"960041.OF"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str end_date : 截止日期,
    :param str invest_advisor_abbr_name : 基金管理人简称,
    :param str establishment_date : 基金管理人成立日期,
    :param float regcapital : 基金管理人注册资本(亿元),
    :param str reg_addr : 基金管理人注册地址,
    :param str general_manager : 基金管理人总经理,
    :param str legal_repr : 基金管理人法人代表,
    :param str contact_name : 基金管理人联系人,
    :param str tel : 基金管理人电话,
    :param str fax : 基金管理人传真,
    :param str website : 基金管理人主页,
    :param str email : 基金管理人邮箱,
    :param str contact_address : 基金管理人办公地址,
    :param float fund_number : 旗下基金数量,
    :param float fund_total_nv : 旗下基金总净值(亿元),
    :param str back_ground : 背景介绍,

    代码调用:
        from hs_udata import fund_manager_company
fund_manager_company() 

    结果输出:
        
    """

    int_param =[]
    float_param =['regcapital', 'fund_number', 'fund_total_nv']
    params = {
        "en_prod_code": en_prod_code,
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_manager_company", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("job_status").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_manager(en_prod_code=None, job_status=None, fields=None):
    """
    提供查询基金的基金经理信息，返回基金经理的名字、任职日、背景等；

    输入参数：
    :param str en_prod_code : 基金代码，默认"960041.OF"
    :param str job_status : 任职状态
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 基金代码,
    :param str chinese_name : 姓名,
    :param str gender : 性别,
    :param str nationality : 国籍地区,
    :param str birthday : 出生日期,
    :param str education : 最高学历,
    :param str experience_time : 证券从业经历,
    :param float manager_number : 高级管理人员数量,
    :param str accession_date : 到任日期,
    :param str dimission_date : 离职日期,
    :param float management_time : 任职天数,
    :param float performance : 任职期基金收益率,
    :param str performance_time : 任职年化回报,
    :param str personal_code : 所属人员编码,
    :param str incumbent : 在任与否,

    代码调用:
        from hs_udata import fund_manager
fund_manager() 

    结果输出:
        
    """

    int_param =[]
    float_param =['manager_number', 'management_time', 'performance']
    params = {
        "en_prod_code": en_prod_code,
        "job_status": job_status,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_manager", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_profile(en_prod_code=None, fields=None):
    """
    本接口返回基金概况数据；

    输入参数：
    :param str en_prod_code : 基金代码，默认"960041.OF"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 基金代码,
    :param str chi_name_abbr : 中文名称缩写,
    :param str chi_name : 基金全称,
    :param str establishment_date : 基金成立日,
    :param str invest_advisor_name : 基金管理人,
    :param str trustee_name : 基金托管人,
    :param str invest_target : 投资目标,
    :param str operation : 运作方式,
    :param float nv_value : 最新基金净资产值(元),
    :param str publish_date : 最新基金资产净值披露日期,
    :param str fund_type_code : 证监会基金分类代码,
    :param str fund_type_name : 证监会基金分类,
    :param str invest_field : 投资范围,

    代码调用:
        from hs_udata import fund_profile
fund_profile() 

    结果输出:
        
    """

    int_param =[]
    float_param =['nv_value']
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_profile", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_institutions(en_prod_code=None, fields=None):
    """
    收录基金各类相关机构；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"960041.OF"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str invest_advisor_name : 基金管理人,
    :param str trustee_name : 基金托管人,

    代码调用:
        from hs_udata import fund_institutions
fund_institutions() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_institutions", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_etf(en_prod_code=None, trading_date=None, fields=None):
    """
    记录ETF基金基本资料、ETF上市日期、ETF最小申赎份额、ETF申购份额上限等信息；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"159937.SZ"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str trading_date : 交易日期,
    :param str etf_listed_date : ETF上市日期,
    :param str primary_market_code : ETF一级市场基金代码,
    :param str target_index_code : ETF标的指数代码,
    :param float least_redemption_unit : ETF最小申赎份额,
    :param float purchase_ul : ETF申购份额上限,
    :param float redemption_ul : ETF赎回份额上限,
    :param float nav_pershare : ETF基金份额净值,
    :param float cash_forecasted : ETF申购赎回预估现金部分,
    :param float cash_balance : ETF申购赎回现金差额,
    :param float cash_substitute_proportion : ETF申购赎回现金替代比例上限,

    代码调用:
        from hs_udata import fund_etf
fund_etf() 

    结果输出:
        
    """

    int_param =[]
    float_param =['least_redemption_unit', 'purchase_ul', 'redemption_ul', 'nav_pershare', 'cash_forecasted', 'cash_balance', 'cash_substitute_proportion']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_etf", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_size(en_prod_code=None, trading_date=None, report_date=None, fields=None):
    """
    记录基金份额和基金净值等统计情况；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"000032.OF"
    :param str trading_date : 交易日期，默认"now"
    :param str report_date : 申报日期
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str trading_date : 交易日期,
    :param str report_date : 申报日期,
    :param float net_value : 净值,
    :param float end_shares : 期末份额（份）,
    :param float circulation_shares : 流通A股股本,
    :param float applying_shares : 报告期申购份额,
    :param float redeem_shares : 报告期赎回份额,
    :param float shares_change : 报告期申购赎回净额,
    :param float rate_of_shares_change : 报告期基金份额变化率,
    :param float q_applying_shares : 单季度申购份额,
    :param float q_redeem_shares : 单季度赎回份额,
    :param float q_shares_change : 单季度申购赎回净额,
    :param float q_rate_of_shares_change : 单季度基金份额变化率,

    代码调用:
        from hs_udata import fund_size
fund_size() 

    结果输出:
        
    """

    int_param =[]
    float_param =['net_value', 'end_shares', 'circulation_shares', 'applying_shares', 'redeem_shares', 'shares_change', 'rate_of_shares_change', 'q_applying_shares', 'q_redeem_shares', 'q_shares_change', 'q_rate_of_shares_change']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_size", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("ofund_charge_type").is_instance((str, None.__class__)),
    check("fund_invest_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_charge_rate(en_prod_code=None, ofund_charge_type=None, fund_invest_type=None, fields=None):
    """
    记录基金各种收费比率及标准；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"580001.OF"
    :param str ofund_charge_type : 基金收费方式，默认"1"
    :param str fund_invest_type : 投资类别(资管)，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param float manage_rate : 管理费率,
    :param float trustee_rate : 托管费,
    :param float marketing_rate : 营销费率,
    :param float subscription_fee_rate : 认购费率,
    :param float apply_fee_rate : 申购费率(%),
    :param float redeem_rate : 赎回费率,

    代码调用:
        from hs_udata import fund_charge_rate
fund_charge_rate() 

    结果输出:
        
    """

    int_param =[]
    float_param =['manage_rate', 'trustee_rate', 'marketing_rate', 'subscription_fee_rate', 'apply_fee_rate', 'redeem_rate']
    params = {
        "en_prod_code": en_prod_code,
        "ofund_charge_type": ofund_charge_type,
        "fund_invest_type": fund_invest_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_charge_rate", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_index(en_prod_code=None, fields=None):
    """
    基金上市相关信息，包括基金上市日期、基金上市地点、等资料；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"184695.SZ"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str listed_date : 基金上市日期,
    :param str market_place : 上市地点,
    :param float outstanding_shares : 可流通基金份额,

    代码调用:
        from hs_udata import fund_index
fund_index() 

    结果输出:
        
    """

    int_param =[]
    float_param =['outstanding_shares']
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_index", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_type(en_prod_code=None, fields=None):
    """
    获取基金性质、运作方式、投资类型、投资定位等信息；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"184695.SZ"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str fund_nature : 基金性质,
    :param str operation : 运作方式,
    :param str investment_type : 投资类型,
    :param str investment_location : 投资定位,
    :param str data_name_cx : 晨星,
    :param str data_name_yh : 银河,
    :param str if_initiating_fund : 是否发起式基金,

    代码调用:
        from hs_udata import fund_type
fund_type() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_type", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("parent_node").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_style(en_prod_code=None, parent_node=None, end_date=None, fields=None):
    """
    输入基金代码、风格类别代码、截止日期，获取该日期下基金所属的风格；

    输入参数：
    :param str en_prod_code : 基金代码，默认"184695.SZ"
    :param str parent_node : 风格类别代码，默认"1013"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str fund_style_code : 风格代码,
    :param str fund_style_name : 风格名称,
    :param str fund_style_type_name : 风格类型,

    代码调用:
        from hs_udata import fund_style
fund_style() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "parent_node": parent_node,
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_style", url_path="fund_basic_data", **params)

@args_check(
    check("hold_ratio").is_instance((str, None.__class__)),
    check("serial_number").is_instance((str, None.__class__)),
    check("full_name").is_instance((str, None.__class__)),
    check("secu_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_holder_public(hold_ratio=None, serial_number=None, full_name=None, secu_code=None, fields=None):
    """
    公募基金持有人

    输入参数：
    :param str hold_ratio : 持仓比例
    :param str serial_number : 序号
    :param str full_name : 中文名称
    :param str secu_code : 证券代码
    :param str fields : 字段集合

    输出参数：
    :param str inner_code : 证券内部代码,
    :param str full_name : 中文名称,
    :param str secu_code : 证券代码,
    :param str secu_category : 证券类别,
    :param str invest_advisor_name : 基金管理人名称,
    :param str legal_repr : 法人代表,
    :param str manager : 基金经理,
    :param str serial_number : 股东序号,
    :param str holder_name : 持有人名称,
    :param float hold_amount : 持有数量,
    :param float hold_ratio : 持有比例,
    :param float code_holder_category : 持有人类别,

    代码调用:
        from hs_udata import fund_holder
fund_holder() 

    结果输出:
        
    """

    int_param =[]
    float_param =['hold_amount', 'hold_ratio', 'code_holder_category']
    params = {
        "hold_ratio": hold_ratio,
        "serial_number": serial_number,
        "full_name": full_name,
        "secu_code": secu_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_holder_public", url_path="fund_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_quote_daily_history(en_prod_code=None, trading_date=None, fields=None):
    """
    基金的历史日行情，及行情表现数据；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"150022.SZ"
    :param str trading_date : 交易日期
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str trading_date : 交易日期,
    :param float prev_close_price : 昨收盘价,
    :param float open_price : 开盘价,
    :param float high_price : 最高价,
    :param float low_price : 最低价,
    :param float avg_price : 变动均价,
    :param float close_price : 收盘价,
    :param float px_change : 价格涨跌,
    :param float px_change_rate : 涨跌幅,
    :param float business_amount : 成交数量,
    :param float business_balance : 成交额,
    :param float amplitude : 振幅,
    :param float discount : 贴水,
    :param float discount_ratio : 贴水率,

    代码调用:
        from hs_udata import fund_quote_daily_history
fund_quote_daily_history() 

    结果输出:
        
    """

    int_param =[]
    float_param =['prev_close_price', 'open_price', 'high_price', 'low_price', 'avg_price', 'close_price', 'px_change', 'px_change_rate', 'business_amount', 'business_balance', 'amplitude', 'discount', 'discount_ratio']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_quote_daily_history", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_quote_daily(en_prod_code=None, fields=None):
    """
    基金的最新日行情，及行情表现数据；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"150022.SZ"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param float prev_close_price : 昨收盘价,
    :param float open_price : 开盘价,
    :param float high_price : 最高价,
    :param float low_price : 最低价,
    :param float close_price : 收盘价,
    :param float avg_price : 变动均价,
    :param float px_change : 价格涨跌,
    :param float px_change_rate : 涨跌幅,
    :param float turnover_ratio : 换手率,
    :param float business_amount : 成交数量,
    :param float business_balance : 成交额,
    :param float amplitude : 振幅,
    :param float discount : 贴水,
    :param float discount_ratio : 贴水率,

    代码调用:
        from hs_udata import fund_quote_daily
fund_quote_daily() 

    结果输出:
        
    """

    int_param =[]
    float_param =['prev_close_price', 'open_price', 'high_price', 'low_price', 'close_price', 'avg_price', 'px_change', 'px_change_rate', 'turnover_ratio', 'business_amount', 'business_balance', 'amplitude', 'discount', 'discount_ratio']
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_quote_daily", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_quote_weekly(en_prod_code=None, fields=None):
    """
    基金的最新周行情，及行情表现数据；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"500039.SH"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param float week_prev_close_price : 周成交均价,
    :param float week_open_price : 周开盘价,
    :param float week_high_price : 周最低价,
    :param float week_low_price : 周收盘价,
    :param float week_close_price : 周最高收盘价,
    :param float week_max_close_price : 周最低收盘价,
    :param float week_min_close_price : 周前收盘价,
    :param float week_avg_price : 周最高价,
    :param float week_px_change : 周涨跌,
    :param float week_px_change_rate : 周涨跌幅,
    :param float week_turnover_ratio : 周换手率,
    :param float week_avg_turnover_rate : 周日均换手率,
    :param float week_amplitude : 周振幅,
    :param float week_business_amount : 周成交量,
    :param float week_business_balance : 周成交额,
    :param float week_discount : 周日均贴水,
    :param float week_discount_ratio : 周日均贴水率,
    :param str week_high_price_date : 周最高价日,
    :param str week_low_price_date : 周最低价日,
    :param str week_max_close_price_date : 周最高收盘价日,
    :param str week_min_close_price_date : 周最低收盘价日,
    :param float week_change_pct_index : 周行情相对沪深300指数表现,

    代码调用:
        from hs_udata import fund_quote_weekly
fund_quote_weekly() 

    结果输出:
        
    """

    int_param =[]
    float_param =['week_prev_close_price', 'week_open_price', 'week_high_price', 'week_low_price', 'week_close_price', 'week_max_close_price', 'week_min_close_price', 'week_avg_price', 'week_px_change', 'week_px_change_rate', 'week_turnover_ratio', 'week_avg_turnover_rate', 'week_amplitude', 'week_business_amount', 'week_business_balance', 'week_discount', 'week_discount_ratio', 'week_change_pct_index']
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_quote_weekly", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_quote_monthly(en_prod_code=None, fields=None):
    """
    基金的最新月行情，及行情表现数据；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"500039.SH"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param float month_prev_close_price : 月前收盘价,
    :param float month_open_price : 月开盘价,
    :param float month_high_price : 月最高价,
    :param float month_low_price : 月最低价,
    :param float month_close_price : 月收盘价,
    :param float month_max_close_price : 月最高收盘价,
    :param float month_min_close_price : 月最低收盘价,
    :param float month_avg_price : 月成交均价,
    :param float month_px_change : 月涨跌,
    :param float month_px_change_rate : 月涨跌幅,
    :param float month_turnover_ratio : 月换手率,
    :param float month_avg_turnover_rate : 月日均换手率,
    :param float month_amplitude : 月振幅,
    :param float month_business_amount : 月成交量,
    :param float month_business_balance : 月成交额,
    :param float month_discount : 月日均贴水,
    :param float month_discount_ratio : 月日均贴水率,
    :param str month_high_price_date : 月最高价日,
    :param str month_low_price_date : 月最低价日,
    :param str month_max_close_price_date : 月最高收盘价日,
    :param str month_min_close_price_date : 月最低收盘价日,
    :param float month_change_pct_index : 月行情相对沪深300指数表现,

    代码调用:
        from hs_udata import fund_quote_monthly
fund_quote_monthly() 

    结果输出:
        
    """

    int_param =[]
    float_param =['month_prev_close_price', 'month_open_price', 'month_high_price', 'month_low_price', 'month_close_price', 'month_max_close_price', 'month_min_close_price', 'month_avg_price', 'month_px_change', 'month_px_change_rate', 'month_turnover_ratio', 'month_avg_turnover_rate', 'month_amplitude', 'month_business_amount', 'month_business_balance', 'month_discount', 'month_discount_ratio', 'month_change_pct_index']
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_quote_monthly", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_quote_yearly(en_prod_code=None, fields=None):
    """
    基金的最新年行情，及行情表现数据；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"500039.SH"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param float year_prev_close_price : 年前收盘价,
    :param float year_open_price : 年开盘价,
    :param float year_high_price : 年最高价,
    :param float year_low_price : 年最低价,
    :param float year_close_price : 年收盘价,
    :param float year_max_close_price : 年最高收盘价,
    :param float year_min_close_price : 年最低收盘价,
    :param float year_avg_price : 年成交均价,
    :param float year_px_change : 年涨跌,
    :param float year_px_change_rate : 年涨跌幅,
    :param float year_turnover_rate : 年换手率,
    :param float year_avg_turnover_rate : 年日均换手率,
    :param float year_amplitude : 年振幅,
    :param float year_business_amount : 年成交量,
    :param float year_business_balance : 年成交额,
    :param float year_discount : 年日均贴水,
    :param float year_discount_ratio : 年日均贴水率,
    :param str year_high_price_date : 年最高价日,
    :param str year_low_price_date : 年最低价日,
    :param str year_max_close_price_date : 年最高收盘价日,
    :param str year_min_close_price_date : 年最低收盘价日,
    :param float year_change_pct_index : 年行情相对沪深300指数表现,

    代码调用:
        from hs_udata import fund_quote_yearly
fund_quote_yearly() 

    结果输出:
        
    """

    int_param =[]
    float_param =['year_prev_close_price', 'year_open_price', 'year_high_price', 'year_low_price', 'year_close_price', 'year_max_close_price', 'year_min_close_price', 'year_avg_price', 'year_px_change', 'year_px_change_rate', 'year_turnover_rate', 'year_avg_turnover_rate', 'year_amplitude', 'year_business_amount', 'year_business_balance', 'year_discount', 'year_discount_ratio', 'year_change_pct_index']
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_quote_yearly", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_net_value(en_prod_code=None, trading_date=None, fields=None):
    """
    记录基金每日单位基金净值，基金每周单位基金净值等资料；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"112002.OF"
    :param str trading_date : 交易日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str trading_date : 交易日期,
    :param float unit_nv : 基金单位净值,
    :param float nv_daily_growth_rate : 单位净值日增长率（开放式）,
    :param float nv_weekly_growth_rate : 单位净值周增长率（封闭式）,
    :param float unit_nv_restored : 向后复权单位净值,
    :param float nvr_daily_groth_rate : 复权单位净值日增长率,

    代码调用:
        from hs_udata import fund_net_value
fund_net_value() 

    结果输出:
        
    """

    int_param =[]
    float_param =['unit_nv', 'nv_daily_growth_rate', 'nv_weekly_growth_rate', 'unit_nv_restored', 'nvr_daily_groth_rate']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_net_value", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def moneyfund_performance(en_prod_code=None, trading_date=None, fields=None):
    """
    记录了货币市场基金收益，包括 每万份基金单位日收益、最近7日折算年收益率等信息；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"519999.OF"
    :param str trading_date : 交易日期，默认"2021-05-10"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str trading_date : 交易日期,
    :param float growth_rate_net_value : 万份收益,
    :param float latest_weekly_yield : 7日年化,

    代码调用:
        from hs_udata import moneyfund_performance
moneyfund_performance() 

    结果输出:
        
    """

    int_param =[]
    float_param =['growth_rate_net_value', 'latest_weekly_yield']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("moneyfund_performance", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("rank").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_stock_detail(en_prod_code=None, report_date=None, rank=None, fields=None):
    """
    基金年报、半年报公布股票组合明细信息；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"000001.OF"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str rank : 排名
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str report_date : 申报日期,
    :param float rank : 排名,
    :param float hold_stock_count : 持股个数,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param float secu_net_asset_ratio : 重仓股市值占基金资产净值比,
    :param float stock_a_shares_ratio : 重仓股持仓占流通A股比,
    :param float quarter_px_change_rate : 重仓股季度涨跌幅,
    :param float hold_fund_count : 持有重仓股的基金个数,
    :param float hold_amount : 持有数量,
    :param float hold_value : 持流通A股市值,

    代码调用:
        from hs_udata import fund_stock_detail
fund_stock_detail() 

    结果输出:
        
    """

    int_param =[]
    float_param =['rank', 'hold_stock_count', 'secu_net_asset_ratio', 'stock_a_shares_ratio', 'quarter_px_change_rate', 'hold_fund_count', 'hold_amount', 'hold_value']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "rank": rank,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_stock_detail", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_asset(en_prod_code=None, report_date=None, fields=None):
    """
    基金资产的大类配置情况，包括股票、债券、银行存款和清算备付金、其他资产、买入返售证券、卖出回购证券、国债及货币资金、
    可转换债券等 ；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"001712.OF"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str report_date : 申报日期,
    :param float total_asset : 基金资产总值,
    :param float net_asset : 基金资产净值,
    :param float stock_value : 股票投资市值,
    :param float bond_value : 债券投资市值,
    :param float deposit : 银行存款,
    :param float warrent_value : 权证投资市值,
    :param float fund_value : 基金投资市值,
    :param float other_value : 其他资产市值,
    :param float stock_net_asset_ratio : 股票市值占基金资产净值比例,
    :param float bond_net_asset_ratio : 债券市值占基金资产净值比例,
    :param float deposit_net_asset_ratio : 银行存款占基金资产净值比例,
    :param float warrent_net_asset_ratio : 权证市值占基金资产净值比例,
    :param float fund_net_asset_ratio : 基金市值占基金资产净值比例,
    :param float other_net_asset_ratio : 其他资产占基金资产净值比例,
    :param float stock_total_asset_ratio : 股票市值占基金资产总值比例,
    :param float bond_total_asset_ratio : 债券市值占基金资产总值比例,
    :param float deposit_total_asset_ratio : 银行存款占基金资产总值比例,
    :param float warrent_total_asset_ratio : 权证市值占基金资产总值比例,
    :param float fund_totalt_asset_ratio : 基金市值占基金资产总值比例,
    :param float other_total_asset_ratio : 其他资产占基金资产总值比例,

    代码调用:
        from hs_udata import fund_asset
fund_asset() 

    结果输出:
        
    """

    int_param =[]
    float_param =['total_asset', 'net_asset', 'stock_value', 'bond_value', 'deposit', 'warrent_value', 'fund_value', 'other_value', 'stock_net_asset_ratio', 'bond_net_asset_ratio', 'deposit_net_asset_ratio', 'warrent_net_asset_ratio', 'fund_net_asset_ratio', 'other_net_asset_ratio', 'stock_total_asset_ratio', 'bond_total_asset_ratio', 'deposit_total_asset_ratio', 'warrent_total_asset_ratio', 'fund_totalt_asset_ratio', 'other_total_asset_ratio']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_asset", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_holder(en_prod_code=None, report_date=None, fields=None):
    """
    基金披露的基金场内持有人户数、持有人结构信息；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"240002.OF"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 产品代码,
    :param str report_date : 申报日期,
    :param float holder_account_number : 持有人户数,
    :param float average_hold_shares : 户均持有份额,
    :param float institution_hold_shares : 机构持有份额,
    :param float institution_hold_ratio : 机构持有比例,
    :param float individual_hold_shares : 个人持有份额,
    :param float individual_hold_ratio : 个人持有比例,
    :param float top10_holder_amount : 前十大持有人持有份额合计,
    :param float top10_holders_proportion : 前十大持有人持有比例合计,
    :param float professional_hold_shares : 基金从业人员持有份额,
    :param float professional_hold_ratio : 基金从业人员持有比例,

    代码调用:
        from hs_udata import fund_holder
fund_holder() 

    结果输出:
        
    """

    int_param =[]
    float_param =['holder_account_number', 'average_hold_shares', 'institution_hold_shares', 'institution_hold_ratio', 'individual_hold_shares', 'individual_hold_ratio', 'top10_holder_amount', 'top10_holders_proportion', 'professional_hold_shares', 'professional_hold_ratio']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_holder", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_rangerise(en_prod_code=None, start_date=None, end_date=None, fields=None):
    """
    该接口根据基金类别 返回基金区间涨跌幅信息；

    输入参数：
    :param str en_prod_code : 基金代码，默认"240002.OF"
    :param str start_date : 开始日期，默认"last_year_today"
    :param str end_date : 截至日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str fund_code : 基金代码,
    :param str fund_name : 基金简称,
    :param str trading_day : 交易日,
    :param float a_unit_nv : 单位累计净值,
    :param float daily_yield_rate : 日涨跌幅(%),
    :param float fund_range_yield_rate : 区间基金收益率,
    :param float index_range_yield_rate : 区间基准收益率,
    :param float daily_profit : 单位净值/每万份基金单位当日收益(元),
    :param float latest_weekly_yield : 最近7日折算年收益率(%),
    :param float same_fund_range_yield_rate : 同类基金收益率,
    :param float same_fund_daily_profit : 同类基金每万份基金单位当日收益(元),
    :param float same_fund_latest_weekly_yield : 同类基金最近7日折算年收益率(%),

    代码调用:
        from hs_udata import fund_rangerise
fund_rangerise() 

    结果输出:
        
    """

    int_param =[]
    float_param =['a_unit_nv', 'daily_yield_rate', 'fund_range_yield_rate', 'index_range_yield_rate', 'daily_profit', 'latest_weekly_yield', 'same_fund_range_yield_rate', 'same_fund_daily_profit', 'same_fund_latest_weekly_yield']
    params = {
        "en_prod_code": en_prod_code,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_rangerise", url_path="fund_basic_condition", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fund_rank(en_prod_code=None, fields=None):
    """
    该接口提供基金同类排名信息；

    输入参数：
    :param str en_prod_code : 基金代码，默认"240002.OF"
    :param str fields : 字段集合

    输出参数：
    :param str date_type_name : 日期类型名称,
    :param float pct_change : 基金涨跌幅,
    :param float same_kind_avg_pct_change : 同类基金平均涨跌幅,
    :param float rank : 同类基金排名,
    :param float same_kind_count : 同类基金个数,

    代码调用:
        from hs_udata import fund_rank
fund_rank() 

    结果输出:
        
    """

    int_param =[]
    float_param =['pct_change', 'same_kind_avg_pct_change', 'rank', 'same_kind_count']
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fund_rank", url_path="fund_basic_condition", **params)

@args_check(
    check("option_codes").is_instance((str, None.__class__)),
    check("contract_code").is_instance((str, None.__class__)),
    check("options_type").is_instance((str, None.__class__)),
    check("options_state").is_instance((str, None.__class__)),
    check("real_state").is_instance((str, None.__class__)),
    check("futu_opertype").is_instance((str, None.__class__)),
    check("exchange_type").is_instance((str, None.__class__)),
    check("warrant_way").is_instance((str, None.__class__)),
    check("opt_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fut_basic(option_codes=None, contract_code=None, options_type=None, options_state=None, real_state=None, futu_opertype=None, exchange_type=None, warrant_way=None, opt_type=None, fields=None):
    """
    获取期权品种名称、生效日期、履约方式、交割方式、申报单位等相关信息 ；

    输入参数：
    :param str option_codes : 合约交易代码
    :param str contract_code : 合约代码
    :param str options_type : 期权类型
    :param str options_state : 合约状态
    :param str real_state : 真实状态
    :param str futu_opertype : 操作类型
    :param str exchange_type : 交易类别
    :param str warrant_way : 行权方式
    :param str opt_type : 期权类型
    :param str fields : 字段集合

    输出参数：
    :param str options_type : 期权类型,
    :param str options_abbr : 合约简称,
    :param str trading_time_desc : 交易时间描述,
    :param str littlest_changeunit : 最小变动价位,
    :param str lasttrading_date : 最后交易日期,
    :param str expiration_date : 到期日期,
    :param str contract_month : 合约月份,
    :param str secu_code : 合约标的物,
    :param str secu_attr : 标的名称,
    :param str option_code : 合约交易代码,
    :param str contract_multiplier : 交易单位/合约乘数,
    :param str exchange_type : 交易类别,
    :param str exercise_price : 行权价格,
    :param str warrant_way : 行权方式,
    :param str price_change_ratio : 涨跌停板幅度,
    :param str options_state : 合约状态,
    :param str real_state : 真实状态,
    :param str futu_opertype : 操作类型,
    :param str delivery_date : 交割日期,
    :param str listing_date : 合约挂牌日期,
    :param str listing_price : 开盘参考价,
    :param str listing_day_pre_fall : 挂牌日跌停价,
    :param str listing_day_pre_rise : 挂牌日涨停价,
    :param str price_unit : 价格单位,
    :param str contract_code : 合同代码,
    :param str opt_type : 期权类型,
    :param str exercise_date : 行权日期,
    :param str delisting_date : 合约摘牌日期,
    :param str margin_ratio1 : 保证金计算比例参数一,
    :param str margin_ratio2 : 保证金计算比例参数二,
    :param str lmt_ord_min : 单笔限价申报下限,
    :param str lmt_ord_max : 单笔限价申报上限,
    :param str mkt_ord_min : 单笔市价申报下限,
    :param str mkt_ord_max : 单笔市价申报上限,

    代码调用:
        from hs_udata import fut_basic
fut_basic() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "option_codes": option_codes,
        "contract_code": contract_code,
        "options_type": options_type,
        "options_state": options_state,
        "real_state": real_state,
        "futu_opertype": futu_opertype,
        "exchange_type": exchange_type,
        "warrant_way": warrant_way,
        "opt_type": opt_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fut_basic", url_path="futures_options", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("begin_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fut_quote_minute(en_prod_code=None, begin_date=None, end_date=None, fields=None):
    """
    期货盘后1分钟切片，交易日16：30后提供。接口服务峰值TPS10；

    输入参数：
    :param str en_prod_code : 证券代码，默认"SC2009.INE"
    :param str begin_date : 起始日期，默认"2021-05-15"
    :param str end_date : 结束日期，默认"2021-05-20"
    :param str fields : 字段集合

    输出参数：
    :param str date : 日期,
    :param str time : 时间,
    :param str open : 开盘价(元),
    :param str high : 最高价(元),
    :param str low : 最低价(元),
    :param str close : 收盘价(元),
    :param str turnover_volume : 成交量(股),
    :param str turnover_value : 成交额(元),
    :param str change : 涨跌幅(元),
    :param str change_pct : 涨跌幅(%),
    :param str amount : 持仓量(张/手),

    代码调用:
        from hs_udata import fut_quote_minute
fut_quote_minute() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "begin_date": begin_date,
        "end_date": end_date,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fut_quote_minute", url_path="futures_options", **params)

@args_check(
    check("fields").is_instance((str, None.__class__))
)
def fut_list(fields=None):
    """
    取得上海国际能源交易中心、上海期货交易所、郑州商品交易所、大连商品交易所、中国金融期货交易所，5大期货交易所期货代码
    列表，用于期货行情查询 ；

    输入参数：
    :param str fields : 字段集合

    输出参数：
    :param str gil_code : 聚源代码,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,

    代码调用:
        from hs_udata import fut_list
fut_list() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fut_list", url_path="futures_options", **params)

@args_check(
    check("contract_code").is_instance((str, None.__class__)),
    check("date_type").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fut_count_rank(contract_code=None, date_type=None, start_date=None, end_date=None, fields=None):
    """
    期货合约多空占比总量统计排名，按交易日纬度，合约代码contract_code取自接口fut_contract，仅支
    持沪深300（IF开头）,上证50（IH开头），中证500（IC开头）的合约代码；

    输入参数：
    :param str contract_code : 合同代码，默认"IF1608"
    :param str date_type : 日期类型，默认"1"
    :param str start_date : 开始日期
    :param str end_date : 截止日期
    :param str fields : 输出字段集合

    输出参数：
    :param str trade_date : 交易日期,
    :param str long_positions_amount : 多单量（手）,
    :param str short_positions_amount : 空单量（手）,

    代码调用:
        from hs_udata import fut_count_rank
fut_count_rank() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "contract_code": contract_code,
        "date_type": date_type,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fut_count_rank", url_path="futures_options", **params)

@args_check(
    check("contract_code").is_instance((str, None.__class__)),
    check("indicator_code").is_instance((str, None.__class__)),
    check("contract_type").is_instance((str, None.__class__)),
    check("rank_num").is_instance((str, None.__class__)),
    check("date_type").is_instance((str, None.__class__)),
    check("start_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fut_holding_lh(contract_code=None, indicator_code=None, contract_type=None, rank_num=None, date_type=None, start_date=None, end_date=None, fields=None):
    """
    提供正在交易的期货合约龙虎榜详情，统计期货会员排名的持仓信息，包含多空增减值，指标数量，其中合约代码contract
    _code取自期货合约详情接口fut_contract；

    输入参数：
    :param str contract_code : 合约代码
    :param str indicator_code : 统计类型
    :param str contract_type : 合同代码类别
    :param str rank_num : 自定义活跃营业部关联股票个数
    :param str date_type : 日期类型，默认"1"
    :param str start_date : 开始日期，默认"now"
    :param str end_date : 截止日期，默认"last_year_today"
    :param str fields : 输出字段集合

    输出参数：
    :param str contract_code : 合约代码,
    :param str trade_date : 交易日期,
    :param str contract_type : 合同代码类别,
    :param float rank_number : 排名名次,
    :param float member_abbr : 会员简称,
    :param float indicator_vol : 指标数量,
    :param float change_vol : 增减数量,
    :param float total_vol : 本日合计,
    :param float total_change_vol : 总增减量,

    代码调用:
        from hs_udata import fut_holding_lh
fut_holding_lh() 

    结果输出:
        
    """

    int_param =[]
    float_param =['rank_number', 'member_abbr', 'indicator_vol', 'change_vol', 'total_vol', 'total_change_vol']
    params = {
        "contract_code": contract_code,
        "indicator_code": indicator_code,
        "contract_type": contract_type,
        "rank_num": rank_num,
        "date_type": date_type,
        "start_date": convert_date(start_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fut_holding_lh", url_path="futures_options", **params)

@args_check(
    check("exchange_code").is_instance((str, None.__class__)),
    check("fut_option_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def fut_contract_type(exchange_code=None, fut_option_code=None, fields=None):
    """
    收录国内商品期货品种和金融期货品种的标准合约基本要素信息；

    输入参数：
    :param str exchange_code : 交易所代码
    :param str fut_option_code : 品种合约标的代码标识
    :param str fields : 输出字段集

    输出参数：
    :param str changepct_limit : 品种每日涨跌幅度,
    :param str contract_month : 品种合约月份,
    :param str contract_name : 合约品种全称,
    :param str delivery_date : 品种交割日期,
    :param str delivery_grades : 品种交割等级,
    :param str delivery_method : 品种交割方式,
    :param str exchange_date : 品种交易日期,
    :param str littlest_changeunit : 品种最小变动价位,
    :param str price_unit : 品种价格单位,
    :param str fut_option_code : 品种合约标的代码标识,
    :param str lasttrading_date : 品种最后交易日,
    :param str contract_multiplier : 品种交易单位/合约乘数,

    代码调用:
        from hs_udata import fut_contract_type
fut_contract_type() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "exchange_code": exchange_code,
        "fut_option_code": fut_option_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("fut_contract_type", url_path="futures_options", **params)

@args_check(
    check("inner_code").is_instance((str, None.__class__)),
    check("date_type").is_instance((str, None.__class__)),
    check("begin_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("price_change_type").is_instance((str, None.__class__)),
    check("secu_code").is_instance((str, None.__class__)),
    check("secu_market").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def con_price(inner_code=None, date_type=None, begin_date=None, end_date=None, price_change_type=None, secu_code=None, secu_market=None, fields=None):
    """
    该接口展示了可转债转股价格变动情况，包含价格变动类型、日期、转股价格、比例等情况 ；

    输入参数：
    :param str inner_code : 债券ID
    :param str date_type : 日期筛选类型，默认"1"
    :param str begin_date : 起始日期，默认"now"
    :param str end_date : 筛选日期截止日，默认"now"
    :param str price_change_type : 价格变动类型
    :param str secu_code : 证券代码
    :param str secu_market : 证券市场
    :param str fields : 字段集合

    输出参数：
    :param str inner_code : 债券ID,
    :param str price_change_type : 价格变动类型,
    :param str info_publ_date : 公告日期,
    :param str valid_date : 有效日期,
    :param str convert_price : 转股价格(元),
    :param str convert_ratio : 转股比例(%),
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_market : 证券市场,
    :param str target_secu_code : 标的证券代码,
    :param str target_secu_abbr : 标的证券简称,
    :param str conv_term_start_date : 转股起始日,
    :param str conv_term_end_date : 转股截止日,

    代码调用:
        from hs_udata import con_price
con_price() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "inner_code": inner_code,
        "date_type": date_type,
        "begin_date": convert_date(begin_date),
        "end_date": convert_date(end_date),
        "price_change_type": price_change_type,
        "secu_code": secu_code,
        "secu_market": secu_market,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("con_price", url_path="bond_data", **params)

@args_check(
    check("inner_code").is_instance((str, None.__class__)),
    check("company_code").is_instance((str, None.__class__)),
    check("date_type").is_instance((str, None.__class__)),
    check("begin_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("interval_type_code").is_instance((str, None.__class__)),
    check("secu_code").is_instance((str, None.__class__)),
    check("secu_market").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def con_time(inner_code=None, company_code=None, date_type=None, begin_date=None, end_date=None, interval_type_code=None, secu_code=None, secu_market=None, fields=None):
    """
    该接口展示了可转债转股区间与暂停转股区间，包含对应日期区间、转股价格、比例等情况；

    输入参数：
    :param str inner_code : 债券ID
    :param str company_code : 公司ID
    :param str date_type : 日期筛选类型，默认"1"
    :param str begin_date : 起始日期，默认"now"
    :param str end_date : 截止日期，默认"now"
    :param str interval_type_code : 区间类型代码
    :param str secu_code : 证券代码
    :param str secu_market : 证券市场
    :param str fields : 字段集合

    输出参数：
    :param str inner_code : 债券ID,
    :param str target_secu_code : 标的证券代码,
    :param str target_secu_abbr : 标的证券简称,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str secu_market : 证券市场,
    :param str interval_type_code : 区间类型代码,
    :param str interval_start_date : 区间起始日,
    :param str interval_end_date : 区间截止日,
    :param str interval_type_name : 区间类型描述,
    :param str convert_price : 转股价格(元),
    :param str convert_ratio : 转股比例,
    :param str valid_date : 有效日期,

    代码调用:
        from hs_udata import con_time
con_time() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "inner_code": inner_code,
        "company_code": company_code,
        "date_type": date_type,
        "begin_date": convert_date(begin_date),
        "end_date": convert_date(end_date),
        "interval_type_code": interval_type_code,
        "secu_code": secu_code,
        "secu_market": secu_market,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("con_time", url_path="bond_data", **params)

@args_check(
    check("bond_code").is_instance((str, None.__class__)),
    check("apply_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def con_detail(bond_code=None, apply_code=None, fields=None):
    """
    获取可转债详细信息 ；

    输入参数：
    :param str bond_code : 债券代码
    :param str apply_code : 申购代码
    :param str fields : 字段集合

    输出参数：
    :param str bond_code : 债券代码,
    :param str bond_abbr : 债券简称,
    :param str secu_market : 证券市场,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str sub_code : 认购代码,
    :param str sub_abbr : 认购简称,
    :param str apply_code : 申购代码,
    :param str apply_abbr : 申购简称,
    :param str credit_rate : 信用级别,
    :param str cras : 评级机构,
    :param str convterm_start_date : 转股期起始日,
    :param str convterm_end_date : 转股期结束日,
    :param str actual_issue_size : 发行规模,
    :param str issue_price : 发行价格(元),
    :param str maturit_year : 债券期限年,
    :param str prefalt_rate : 配售比例（％）,
    :param str apply_date : 申请日期,
    :param str list_date : 上市日期,
    :param str offline_lot_rate : 网下配售中签率,
    :param str online_issue_vol : 网上发行数量,
    :param str online_apply_cap : 最大申购数,
    :param str online_apply_min : 最小申购数（张数）,
    :param str interest_item : 票面利率,
    :param str sellback_term : 回售条款,
    :param str redeem_term : 赎回条款,

    代码调用:
        from hs_udata import con_detail
con_detail() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "bond_code": bond_code,
        "apply_code": apply_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("con_detail", url_path="bond_data", **params)

@args_check(
    check("start_date").is_instance((str, None.__class__)),
    check("bond_code").is_instance((str, None.__class__)),
    check("secu_code").is_instance((str, None.__class__)),
    check("apply_code").is_instance((str, None.__class__)),
    check("pref_code").is_instance((str, None.__class__)),
    check("prompt_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def con_calender(start_date=None, bond_code=None, secu_code=None, apply_code=None, pref_code=None, prompt_type=None, fields=None):
    """
    提供申购，待上市，今日可申购，已上市 等状态；

    输入参数：
    :param str start_date : 开始日期
    :param str bond_code : 债券代码
    :param str secu_code : 证券代码
    :param str apply_code : 申购代码
    :param str pref_code : 配售代码
    :param str prompt_type : 状态
    :param str fields : 字段集合

    输出参数：
    :param str bond_code : 债券代码,
    :param str bond_abbr : 债券简称,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str issue_vol_planned : 计划发行量,
    :param str actual_issue_size : 发行规模,
    :param str listed_date : 上市日期,
    :param str close_price : 最新价,
    :param str new_convet_price : 转股价格,
    :param str premium_ratio : 转股溢价率(%),
    :param str a_change : 涨跌幅(%),
    :param str convet_value : 转股价值,
    :param str pref_code : 配售代码,
    :param str pref_name : 配售名称,
    :param str apply_date : 申请日期,
    :param str online_issue_vol : 网上发行数量,
    :param str online_lot_rate : 网上申购中签率,
    :param str online_start_date : 网上发行日,
    :param str offline_lot_rate : 网下配售中签率,
    :param str apply_code : 申购代码,
    :param str apply_name : 申购名称,
    :param str issue_price_change : 发行价格,
    :param str online_apply_cap : 最大申购数,
    :param str online_apply_min : 最小申购数（张数）,
    :param str open_price : 开盘价,
    :param str unsuccessful_earnings : 中签收益(每签),
    :param str secu_market : 证券市场,
    :param str info_publ_date : 公告日期,

    代码调用:
        from hs_udata import con_calender
con_calender() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "start_date": convert_date(start_date),
        "bond_code": bond_code,
        "secu_code": secu_code,
        "apply_code": apply_code,
        "pref_code": pref_code,
        "prompt_type": prompt_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("con_calender", url_path="bond_data", **params)

@args_check(
    check("fields").is_instance((str, None.__class__))
)
def hk_list(fields=None):
    """
    记录港股上市、退市股票交易代码、股票名称等信息，以列表形式展示；

    输入参数：
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str chi_name : 中文名称,
    :param str secu_market : 证券市场,
    :param str listed_sector : 上市板块,
    :param str listed_state : 上市状态,

    代码调用:
        from hs_udata import hk_list
hk_list() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_list", url_path="hk_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_ipo(en_prod_code=None, fields=None):
    """
    获取港股首发IPO的数据，如首发上市日期、每股发行价、发行量 、新股发行数量、股东售股数量 、募集资金总额 、募集资
    金净额等 ；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str listed_date : 首发上市日期,
    :param float total_shares_on_list_date : 首发后总股本_上市日,
    :param float store_share_allotment : 股东售股数量,
    :param float total_net_proceeds : 发行费用,
    :param float over_allotment_proceeds : 超额配售募资总额,
    :param float over_allotment_net_proceeds : 超额配售募资净额,
    :param float issue_vol_planned : 计划发行量,
    :param float proceeds_planned : 计划募集资金总额,
    :param float net_proceeds_planned : 计划募集资金净额,
    :param float issue_cost_planned : 计划发行费用,
    :param float pub_apply_multiple : 首发公众认购倍数,
    :param float allotment_apply_multiple : 首发配售申请倍数,
    :param float issue_pe_diluted : 首发市盈率（摊薄）,
    :param float issue_price_floor : 发行价格下限,
    :param float issue_price_ceiling : 发行价格上限,
    :param float first_underwriter_allotment : 最大承配人配售股数,
    :param float first_5_underwriters_allotment : 前5大承配人配售股数,
    :param float first_10_underwriters_allotment : 前10大承配人配售股数,
    :param float currency_unit : 面值单位,
    :param float issue_vol : 发行量,
    :param float new_share_vol : 新股发行数量,
    :param float total_proceeds : 募集资金总额,
    :param float net_proceeds : 募集资金净额,
    :param str issue_method : 发行方式,
    :param float issue_price_change : 每股发行价,
    :param str issue_object : 发行对象,
    :param float par_value : 面值,

    代码调用:
        from hs_udata import hk_ipo
hk_ipo() 

    结果输出:
        
    """

    int_param =[]
    float_param =['total_shares_on_list_date', 'store_share_allotment', 'total_net_proceeds', 'over_allotment_proceeds', 'over_allotment_net_proceeds', 'issue_vol_planned', 'proceeds_planned', 'net_proceeds_planned', 'issue_cost_planned', 'pub_apply_multiple', 'allotment_apply_multiple', 'issue_pe_diluted', 'issue_price_floor', 'issue_price_ceiling', 'first_underwriter_allotment', 'first_5_underwriters_allotment', 'first_10_underwriters_allotment', 'currency_unit', 'issue_vol', 'new_share_vol', 'total_proceeds', 'net_proceeds', 'issue_price_change', 'par_value']
    params = {
        "en_prod_code": en_prod_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_ipo", url_path="hk_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("year").is_instance((str, None.__class__)),
    check("level").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_company(en_prod_code=None, year=None, level=None, fields=None):
    """
    

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str year : 年度，默认"2021"
    :param str level : 等级，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str company_pro : 公司属性,
    :param str fis_year_after_change : 会计年结日,
    :param str register_currency : 注册资本货币单位,
    :param str secretary : 公司秘书,
    :param str certified_accountant : 合资格会计师,
    :param str brief_introduction : 公司简介,
    :param float employee_sum : 员工总数,
    :param str regoffice : 注册办事处,
    :param str legal_consultant : 法律顾问,
    :param str auditor : 核数师,
    :param str eng_name : 公司英文名称,
    :param str chairman : 主席,
    :param str major_business : 经营范围,
    :param str reg_abbr : 注册地址,
    :param str officeaddress : 总办事处及主要营业地点,
    :param str registrars : 股份过户处(香港),
    :param str email : 邮箱,
    :param str website : 网址,
    :param str industry_chke : 所属行业-港交所,
    :param str industry_chs : 所属行业-恒生,
    :param str chi_name : 公司中文名称,
    :param float regcapital : 注册资本,
    :param str tel : 电话,
    :param str fax : 传真,
    :param str establishment_date : 成立日期,

    代码调用:
        from hs_udata import hk_company
hk_company() 

    结果输出:
        
    """

    int_param =[]
    float_param =['employee_sum', 'regcapital']
    params = {
        "en_prod_code": en_prod_code,
        "year": year,
        "level": level,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_company", url_path="hk_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_secu(en_prod_code=None, trading_date=None, fields=None):
    """
    获取港股的基本信息，包含股票交易代码、股票简称、上市时间、上市状态、上市板块、所属概念板块及可能有的同公司A股、B股
    信息等信息；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"2021-05-20"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float par_value : 股票面值,
    :param str listed_date : 上市日期,
    :param str secu_category : 证券类别,
    :param str chi_spelling : 拼音证券简称,
    :param str secu_code : 证券代码,
    :param str astock_code : 同公司A股简称,
    :param str astock_abbr : 同公司A股代码,
    :param str alias_name : 曾用名,
    :param float trade_unit : 买卖单位,
    :param str currency_unit : 面值单位,
    :param str secu_market : 上市地点,
    :param str listed_sector : 上市板块,
    :param str listed_state : 上市状态,
    :param str sh_hk_flag : 是否沪港通标的,
    :param str sz_hk_flag : 是否深港通标的,
    :param str secu_abbr : 证券简称,

    代码调用:
        from hs_udata import hk_secu
hk_secu() 

    结果输出:
        
    """

    int_param =[]
    float_param =['par_value', 'trade_unit']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_secu", url_path="hk_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_leader(en_prod_code=None, trading_date=None, fields=None):
    """
    

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param str vice_leader_name : 副董事长,
    :param str secretary : 董事会秘书,
    :param str chief_financial_officer : 财务总监,
    :param str vice_general_manager : 副总经理,
    :param str supervisory_board_chairman : 监事会主席,
    :param str leader_name_incumbent : 董事（现任）,
    :param str ind_leader_name_incumbent : 独立董事（现任）,
    :param str supervisor_incumbent : 监事（现任）,
    :param str employee_supervisor_incumbent : 职工监事（现任）,
    :param str general_manager : 总经理,
    :param str in_date_leader_name : 董事长任职日期,
    :param str in_date_general_manager : 总经理任职日期,
    :param str in_date_secretary : 董事会秘书任职日期,
    :param str in_date_chief_fin_officer : 财务总监任职日期,
    :param str in_date_super_board_chairman : 监事会主席任职日期,
    :param str leader_name : 董事长,

    代码调用:
        from hs_udata import hk_leader
hk_leader() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_leader", url_path="hk_basic_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_daily_quote(en_prod_code=None, trading_date=None, adjust_way=None, fields=None):
    """
    获取港股日行情的指标，比如前收盘价、开盘价、最高价、最低价、收盘价、均价、涨跌、涨跌幅等指标；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"2021-05-20"
    :param str adjust_way : 复权方式，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float open_price : 开盘价,
    :param float high_price : 最高价,
    :param float low_price : 最低价,
    :param float close_price : 昨收盘,
    :param float px_change : 价格涨跌,
    :param float px_change_rate : 涨跌幅,
    :param float amplitude : 振幅,
    :param float issue_price_change : 相对发行价涨跌,
    :param str turnover_status : 交易状态,
    :param str currency_name : 货币名称,
    :param str recently_trading_date : 最近交易日期,
    :param float average_price : 平均价,
    :param float turnover_ratio : 换手率,
    :param float business_amount : 成交数量,
    :param float business_balance : 成交金额,
    :param float issue_price_change_rate : 相对发行价涨跌幅（%）,
    :param float ratio_adjust_factor : 复权因子,
    :param float prev_close_price : 前收盘价,

    代码调用:
        from hs_udata import hk_daily_quote
hk_daily_quote() 

    结果输出:
        
    """

    int_param =[]
    float_param =['open_price', 'high_price', 'low_price', 'close_price', 'px_change', 'px_change_rate', 'amplitude', 'issue_price_change', 'average_price', 'turnover_ratio', 'business_amount', 'business_balance', 'issue_price_change_rate', 'ratio_adjust_factor', 'prev_close_price']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "adjust_way": adjust_way,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_daily_quote", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_weekly_quote(en_prod_code=None, trading_date=None, adjust_way=None, fields=None):
    """
    获取港股周行情中的指标，比如周前收盘价、周开盘价、周最高价、周最低价、周收盘价、周均价、周涨跌、周涨跌幅等指标；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"2021-05-20"
    :param str adjust_way : 复权方式，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float week_close_price : 周收盘价,
    :param float week_open_price : 周开盘价,
    :param float week_high_price : 周最高价,
    :param float week_low_price : 周最低价,
    :param float week_average_price : 周均价,
    :param float week_px_change : 周涨跌,
    :param float week_px_change_rate : 周涨跌幅（%）,
    :param float week_amplitude : 周振幅（%）,
    :param float week_max_close_price : 周最高收盘价,
    :param float week_min_close_price : 周最低收盘价,
    :param float week_avg_business_balance : 周日均成交额,
    :param float week_avg_business_amount : 周日均成交量,
    :param float week_turnover_ratio : 周换手率（%）,
    :param float week_avg_turnover_ratio : 周日平均换手率（%）,
    :param float week_business_balance : 周成交额,
    :param float week_business_amount : 周成交量,
    :param str week_high_price_date : 周最高价日,
    :param str week_low_price_date : 周最低价日,
    :param str week_max_close_price_date : 周最高收盘价日,
    :param str week_min_close_price_date : 周最低收盘价日,
    :param float week_prev_close_price : 周前收盘价,

    代码调用:
        from hs_udata import hk_weekly_quote
hk_weekly_quote() 

    结果输出:
        
    """

    int_param =[]
    float_param =['week_close_price', 'week_open_price', 'week_high_price', 'week_low_price', 'week_average_price', 'week_px_change', 'week_px_change_rate', 'week_amplitude', 'week_max_close_price', 'week_min_close_price', 'week_avg_business_balance', 'week_avg_business_amount', 'week_turnover_ratio', 'week_avg_turnover_ratio', 'week_business_balance', 'week_business_amount', 'week_prev_close_price']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "adjust_way": adjust_way,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_weekly_quote", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_monthly_quote(en_prod_code=None, trading_date=None, adjust_way=None, fields=None):
    """
    获取港股月行情中的指标，比如月前收盘价、月开盘价、月最高价、月最低价、月收盘价、月均价、月涨跌、月涨跌幅等指标 ；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"2021-05-20"
    :param str adjust_way : 复权方式，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float month_close_price : 月收盘价,
    :param float month_open_price : 月开盘价,
    :param float month_high_price : 月最高价,
    :param float month_low_price : 月最低价,
    :param float month_average_price : 月均价,
    :param float month_px_change : 月涨跌,
    :param float month_px_change_rate : 月涨跌幅（%）,
    :param float month_amplitude : 月振幅（%）,
    :param float month_max_close_price : 月最高收盘价,
    :param float month_min_close_price : 月最低收盘价,
    :param float month_avg_business_balance : 月日均成交额,
    :param float month_avg_business_amount : 月日均成交量,
    :param float month_turnover_ratio : 月换手率（%）,
    :param float month_avg_turnover_ratio : 月日平均换手率（%）,
    :param float month_business_balance : 月成交额,
    :param float month_business_amount : 月成交量,
    :param str month_high_price_date : 月最高价日,
    :param str month_low_price_date : 月最低价日,
    :param str month_max_close_price_date : 月最高收盘价日,
    :param str month_min_close_price_date : 月最低收盘价日,
    :param float month_prev_close_price : 月前收盘价,

    代码调用:
        from hs_udata import hk_monthly_quote
hk_monthly_quote() 

    结果输出:
        
    """

    int_param =[]
    float_param =['month_close_price', 'month_open_price', 'month_high_price', 'month_low_price', 'month_average_price', 'month_px_change', 'month_px_change_rate', 'month_amplitude', 'month_max_close_price', 'month_min_close_price', 'month_avg_business_balance', 'month_avg_business_amount', 'month_turnover_ratio', 'month_avg_turnover_ratio', 'month_business_balance', 'month_business_amount', 'month_prev_close_price']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "adjust_way": adjust_way,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_monthly_quote", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_yearly_quote(en_prod_code=None, trading_date=None, adjust_way=None, fields=None):
    """
    获取港股年行情中的指标，比如年前收盘价、年开盘价、年最高价、年最低价、年收盘价、年均价、年涨跌、年涨跌幅等指标；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"2021-05-20"
    :param str adjust_way : 复权方式，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float year_average_price : 年均价,
    :param float year_open_price : 年开盘价,
    :param float year_low_price : 年最低价,
    :param float year_close_price : 年收盘价,
    :param float year_high_price : 年最高价,
    :param float year_px_change : 年涨跌,
    :param float year_px_change_rate : 年涨跌幅（%）,
    :param float year_amplitude : 年振幅（%）,
    :param float year_max_close_price : 年最高收盘价,
    :param float year_min_close_price : 年最低收盘价,
    :param float year_avg_business_balance : 年日均成交额,
    :param float year_avg_business_amount : 年日均成交量,
    :param float year_turnover_ratio : 年换手率（%）,
    :param float year_avg_turnover_ratio : 年日平均换手率（%）,
    :param float year_business_balance : 本年金额,
    :param float year_business_amount : 年成交量,
    :param str year_high_price_date : 年最高价日,
    :param str year_low_price_date : 年最低价日,
    :param str year_max_close_price_date : 年最高收盘价日,
    :param str year_min_close_price_date : 年最低收盘价日,
    :param float year_prev_close_price : 年前收盘价,

    代码调用:
        from hs_udata import hk_yearly_quote
hk_yearly_quote() 

    结果输出:
        
    """

    int_param =[]
    float_param =['year_average_price', 'year_open_price', 'year_low_price', 'year_close_price', 'year_high_price', 'year_px_change', 'year_px_change_rate', 'year_amplitude', 'year_max_close_price', 'year_min_close_price', 'year_avg_business_balance', 'year_avg_business_amount', 'year_turnover_ratio', 'year_avg_turnover_ratio', 'year_business_balance', 'year_business_amount', 'year_prev_close_price']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "adjust_way": adjust_way,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_yearly_quote", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("begin_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("adjust_way").is_instance((str, None.__class__)),
    check("index_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_section_quote(en_prod_code=None, begin_date=None, end_date=None, adjust_way=None, index_code=None, trading_date=None, fields=None):
    """
    获取港股区间行情指标，比如区间前收盘价、区间开盘价、区间最高价、区间最低价 、区间收盘价、区间最高收盘价 、区间最低
    收盘价、区间均价等 ；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str begin_date : 起始日期，默认"five days ago"
    :param str end_date : 截止日期，默认"now"
    :param str adjust_way : 复权方式，默认"1"
    :param str index_code : 指数代码，默认"0"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str begin_date : 起始日期,
    :param str end_date : 截止日期,
    :param str index_code : 指数代码,
    :param float interval_average_price : 区间均价,
    :param float interval_close_price : 区间收盘价,
    :param float interval_low_price : 区间最低价,
    :param float interval_open_price : 区间开盘价,
    :param float interval_high_price : 区间最高价,
    :param float interval_px_change : 区间涨跌,
    :param float interval_px_change_rate : 区间涨跌幅,
    :param float interval_amplitude : 区间振幅,
    :param float interval_up_down_index : 相对指数区间涨跌幅,
    :param float interval_trading_day : 区间交易日天数,
    :param float interval_susp_trading_day : 区间停牌天数,
    :param float interval_up_trading_day : 区间上涨天数,
    :param float interval_down_trading_day : 区间下跌天数,
    :param str interval_high_price_date : 区间最高价日,
    :param str interval_low_price_date : 区间最低价日,
    :param str interval_max_close_price_date : 区间最高收盘价日,
    :param str interval_min_close_price_date : 区间最低收盘价日,
    :param float interval_max_close_price : 区间最高收盘价,
    :param float interval_min_close_price : 区间最低收盘价,
    :param float interval_business_balance : 区间成交量,
    :param float interval_business_amount : 区间成交额,
    :param float interval_avg_business_balance : 区间日均成交额,
    :param float interval_avg_business_amount : 区间日均成交量,
    :param float interval_avg_px_change_rate : 区间日均涨跌幅,
    :param float interval_turnover_ratio : 区间换手率,
    :param float interval_avg_turnover_ratio : 区间日均换手率,
    :param float interval_prev_close_price : 区间前收盘价,

    代码调用:
        from hs_udata import hk_section_quote
hk_section_quote() 

    结果输出:
        
    """

    int_param =[]
    float_param =['interval_average_price', 'interval_close_price', 'interval_low_price', 'interval_open_price', 'interval_high_price', 'interval_px_change', 'interval_px_change_rate', 'interval_amplitude', 'interval_up_down_index', 'interval_trading_day', 'interval_susp_trading_day', 'interval_up_trading_day', 'interval_down_trading_day', 'interval_max_close_price', 'interval_min_close_price', 'interval_business_balance', 'interval_business_amount', 'interval_avg_business_balance', 'interval_avg_business_amount', 'interval_avg_px_change_rate', 'interval_turnover_ratio', 'interval_avg_turnover_ratio', 'interval_prev_close_price']
    params = {
        "en_prod_code": en_prod_code,
        "begin_date": convert_date(begin_date),
        "end_date": convert_date(end_date),
        "adjust_way": adjust_way,
        "index_code": index_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_section_quote", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_daily_quote_short(en_prod_code=None, trading_date=None, fields=None):
    """
    获取港股日行情中的卖空指标，比如货币、成交额、成交量等 ；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str en_prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float short_balance : 缺口资金,
    :param float short_amount : 缺口数量,
    :param str currency_name : 货币名称,

    代码调用:
        from hs_udata import hk_daily_quote_short
hk_daily_quote_short() 

    结果输出:
        
    """

    int_param =[]
    float_param =['short_balance', 'short_amount']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_daily_quote_short", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_weekly_quote_short(en_prod_code=None, trading_date=None, fields=None):
    """
    获取港股周行情中的卖空指标，比如货币、周成交额、周成交量等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float week_short_balance : 周成交量,
    :param float week_short_amount : 周成交额,
    :param str currency_name : 货币名称,

    代码调用:
        from hs_udata import hk_weekly_quote_short
hk_weekly_quote_short() 

    结果输出:
        
    """

    int_param =[]
    float_param =['week_short_balance', 'week_short_amount']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_weekly_quote_short", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_monthly_quote_short(en_prod_code=None, trading_date=None, fields=None):
    """
    获取港股月行情中的卖空指标，比如货币、月成交额、月成交量等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float month_short_balance : 月成交额,
    :param float month_short_amount : 月成交量,
    :param str currency_name : 货币名称,

    代码调用:
        from hs_udata import hk_monthly_quote_short
hk_monthly_quote_short() 

    结果输出:
        
    """

    int_param =[]
    float_param =['month_short_balance', 'month_short_amount']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_monthly_quote_short", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_yearly_quote_short(en_prod_code=None, trading_date=None, fields=None):
    """
    获取港股年行情中的卖空指标，比如货币、年成交额、年成交量等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str trading_date : 交易日期,
    :param float year_short_balance : 年成交额,
    :param float year_short_amount : 年成交量,
    :param str currency_name : 货币名称,

    代码调用:
        from hs_udata import hk_yearly_quote_short
hk_yearly_quote_short() 

    结果输出:
        
    """

    int_param =[]
    float_param =['year_short_balance', 'year_short_amount']
    params = {
        "en_prod_code": en_prod_code,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_yearly_quote_short", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("begin_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_section_quote_short(en_prod_code=None, begin_date=None, end_date=None, fields=None):
    """
    获取港股区间行情中的卖空指标，比如货币、区间成交量、区间成交额；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str begin_date : 起始日期，默认"five days ago"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str begin_date : 起始日期,
    :param str end_date : 截止日期,
    :param float interval_short_balance : 区间成交额,
    :param float interval_short_amount : 区间成交量,
    :param str currency_name : 货币,

    代码调用:
        from hs_udata import hk_section_quote_short
hk_section_quote_short() 

    结果输出:
        
    """

    int_param =[]
    float_param =['interval_short_balance', 'interval_short_amount']
    params = {
        "en_prod_code": en_prod_code,
        "begin_date": convert_date(begin_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_section_quote_short", url_path="hk_quotation_data", **params)

@args_check(
    check("comp_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_minutes_hkscclist(comp_type=None, fields=None):
    """
    取得港股通(沪)与港股通(深)代码列表，用于港股通行情查询；

    输入参数：
    :param str comp_type : 成分股类别，默认"1"
    :param str fields : 字段集合

    输出参数：
    :param str gil_code : 聚源代码,
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,

    代码调用:
        from hs_udata import hk_minutes_hkscclist
hk_minutes_hkscclist() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "comp_type": comp_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_minutes_hkscclist", url_path="hk_quotation_data", **params)

@args_check(
    check("gil_code").is_instance((str, None.__class__)),
    check("begin_date").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_minutes_hkscc(gil_code=None, begin_date=None, end_date=None, fields=None):
    """
    港股通盘后1分钟切片，交易日16：30后提供。接口服务峰值TPS10；

    输入参数：
    :param str gil_code : 证券代码，默认"00700.HK"
    :param str begin_date : 起始日期，默认"yesterday"
    :param str end_date : 结束日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str date : 日期,
    :param str time : 发生时间,
    :param float open : 开盘价(元),
    :param float high : 最高价(元),
    :param float low : 最低价(元),
    :param float close : 收盘价(元),
    :param float turnover_volume : 成交量,
    :param float turnover_value : 成交额,
    :param float change : 涨跌幅(元),
    :param float change_pct : 涨跌幅(%),

    代码调用:
        from hs_udata import hk_minutes_hkscc
hk_minutes_hkscc() 

    结果输出:
        
    """

    int_param =[]
    float_param =['open', 'high', 'low', 'close', 'turnover_volume', 'turnover_value', 'change', 'change_pct']
    params = {
        "gil_code": gil_code,
        "begin_date": convert_date(begin_date),
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_minutes_hkscc", url_path="hk_quotation_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_share_stru(en_prod_code=None, end_date=None, fields=None):
    """
    获取港股的具体股本结构信息；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str end_date : 截止日期,
    :param float paid_up_shares_com_share : 普通股,
    :param float paid_up_shares_pre_share : 优先股,
    :param float total_listed_shares : 港股,
    :param float listed_shares_ratio : 港股占普通股比例,
    :param float non_listed_shares_ratio : 非港股占普通股比例,
    :param float authorized_share_ratio : 优先股占总股本比例,
    :param float not_hk_shares : 非港股,
    :param float com_share_ratio : 普通股占总股本比例,
    :param float total_shares : 总股本,

    代码调用:
        from hs_udata import hk_share_stru
hk_share_stru() 

    结果输出:
        
    """

    int_param =[]
    float_param =['paid_up_shares_com_share', 'paid_up_shares_pre_share', 'total_listed_shares', 'listed_shares_ratio', 'non_listed_shares_ratio', 'authorized_share_ratio', 'not_hk_shares', 'com_share_ratio', 'total_shares']
    params = {
        "en_prod_code": en_prod_code,
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_share_stru", url_path="hk_market_data", **params)

@args_check(
    check("standard").is_instance((str, None.__class__)),
    check("secu_code").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_exgindustry(standard=None, secu_code=None, fields=None):
    """
    港股公司行业划分目前共4个，包括：8-GICS行业分类，24-申万行业分类2014版（目前分类范围为陆港通公司），2
    2-证监会行业分类2012版（目前分类范围为陆港通公司），100-恒生行业分类（港交所）；

    输入参数：
    :param str standard : 行业划分标准，默认"100"
    :param str secu_code : 港股代码，默认"00700"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 港股代码,
    :param str secu_abbr : 港股简称,
    :param str standard : 行业划分类型,
    :param str one_industry_name : 一级行业名称,
    :param str two_industry_name : 二级行业名称,
    :param str three_industry_name : 三级行业名称,
    :param str four_industry_name : 四级行业名称,

    代码调用:
        from hs_udata import hk_exgindustry
hk_exgindustry() 

    结果输出:
        
    """

    int_param =[]
    float_param =[]
    params = {
        "standard": standard,
        "secu_code": secu_code,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_exgindustry", url_path="hk_market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_cap_structure(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    获取港股资本结构的指标，如资产负债率、长期资本负债率、权益乘数、流动资产/总资产、非流动资产/总资产、资本固定化比率等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float debt_assets_ratio : 资产负债率,
    :param float t_liability_ar : 剔除预收账款后的资产负债率,
    :param float long_term_capital_liability_ratio : 长期资本负债率,
    :param float equity_multipler : 权益乘数,
    :param float current_assets_to_ta : 流动资产/总资产,
    :param float non_current_assets_to_ta : 非流动资产/总资产,
    :param float total_non_current_liability_ratio : 非流动负债权益比率,
    :param float total_current_liability_ratio : 流动负债权益比率,
    :param float operating_assets : 营运资产/总资产,
    :param float current_liability_to_tl : 流动负债/负债合计,
    :param float non_current_liability_to_tl : 非流动负债/负债合计,
    :param float capital_fix_ratio : 资本固定化比率,

    代码调用:
        from hs_udata import shk_cap_structure
hk_cap_structure() 

    结果输出:
        
    """

    int_param =[]
    float_param =['debt_assets_ratio', 't_liability_ar', 'long_term_capital_liability_ratio', 'equity_multipler', 'current_assets_to_ta', 'non_current_assets_to_ta', 'total_non_current_liability_ratio', 'total_current_liability_ratio', 'operating_assets', 'current_liability_to_tl', 'non_current_liability_to_tl', 'capital_fix_ratio']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_cap_structure", url_path="hk_market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_profit_ability(en_prod_code=None, report_date=None, report_type=None, trading_date=None, fields=None):
    """
    获取港股上市公司的盈利能力的指标，如净资产收益率、总资产报酬率、销售毛利率、净利润/营业总收入、销售费用/营业总收入
    、销售毛利率等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float roe : 净资产收益率ROE(摊薄),
    :param float roe_avg : 净资产收益率ROE(平均/计算值),
    :param float roe_year : 净资产收益率ROE-年化,
    :param float assets_re : 总资产报酬率,
    :param float assets_re_year : 总资产报酬率-年化,
    :param float assets_rate : 总资产净利率,
    :param float assets_rate_year : 总资产净利率-年化,
    :param float net_profit_ratio : 销售净利率,
    :param float gross_income_ratio : 销售毛利率,
    :param float sales_cost_ratio : 销售成本率,
    :param float period_costs_rate : 销售期间费用率,
    :param float np_to_tor : 净利润/营业总收入,
    :param float net_profit_income : 归属母公司股东净利润/营业总收入,
    :param float operating_profit_to_tor : 营业利润／营业总收入,
    :param float ebit_to_tor : 息税前利润／营业总收入,
    :param float operating_expense_rate : 销售费用/营业总收入,
    :param float admini_expense_rate : 管理费用/营业总收入,
    :param float financial_expense_rate : 财务费用/营业总收入,
    :param float asset_impa_loss_to_tor : 资产减值损失/营业总收入,
    :param float loss_profit : 资产减值损失/营业利润,
    :param float roe_ttm : 净资产收益率ROE(TTM),
    :param float roa_ebit_ttm : 总资产报酬率ROA(TTM),
    :param float roa_ttm : 总资产净利率ROA(TTM),
    :param float net_profit_ratio_ttm : 销售净利率_TTM,
    :param float gross_income_ratio_ttm : 销售毛利率(TTM),
    :param float period_costs_rate_ttm : 销售期间费用率_TTM,
    :param float np_to_tor_ttm : 净利润／营业总收入_TTM,
    :param float operating_profit_to_tor_ttm : 营业利润/营业总收入(TTM),
    :param float ebit_to_tor_ttm : 息税前利润/营业总收入(TTM),
    :param float operating_expense_rate_ttm : 销售费用／营业总收入_TTM,
    :param float admini_expense_rate_ttm : 管理费用／营业总收入_TTM,
    :param float financial_expense_rate_ttm : 财务费用／营业总收入_TTM,
    :param float asset_impa_loss_to_tor_ttm : 资产减值损失／营业总收入_TTM,
    :param float loss_profit_ttm : 资产减值损失/营业利润(TTM),

    代码调用:
        from hs_udata import hk_profit_ability
hk_profit_ability() 

    结果输出:
        
    """

    int_param =[]
    float_param =['roe', 'roe_avg', 'roe_year', 'assets_re', 'assets_re_year', 'assets_rate', 'assets_rate_year', 'net_profit_ratio', 'gross_income_ratio', 'sales_cost_ratio', 'period_costs_rate', 'np_to_tor', 'net_profit_income', 'operating_profit_to_tor', 'ebit_to_tor', 'operating_expense_rate', 'admini_expense_rate', 'financial_expense_rate', 'asset_impa_loss_to_tor', 'loss_profit', 'roe_ttm', 'roa_ebit_ttm', 'roa_ttm', 'net_profit_ratio_ttm', 'gross_income_ratio_ttm', 'period_costs_rate_ttm', 'np_to_tor_ttm', 'operating_profit_to_tor_ttm', 'ebit_to_tor_ttm', 'operating_expense_rate_ttm', 'admini_expense_rate_ttm', 'financial_expense_rate_ttm', 'asset_impa_loss_to_tor_ttm', 'loss_profit_ttm']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_profit_ability", url_path="hk_market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("currency_type").is_instance((str, None.__class__)),
    check("trading_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_per_share_index(en_prod_code=None, report_date=None, report_type=None, currency_type=None, trading_date=None, fields=None):
    """
    获取港股上市公司的财务分析指标，包括每股收益、每股净资产、每股经营活动产生的现金流、每股营业总收入、每股息税前利润、
    每股现金流量净额等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str currency_type : 货币种类，默认"0"
    :param str trading_date : 交易日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float basic_eps : 基本每股收益,
    :param float diluted_eps : 每股收益EPS-稀释,
    :param float new_np_parent_company_owners_t : 每股收益EPS-最新股本摊薄,
    :param float eps_ttm : 每股收益EPS(TTM),
    :param float naps : 每股净资产,
    :param float se_without_mi_t : 每股净资产BPS（最新股本摊薄）,
    :param float net_operate_cash_flow_ps : 每股经营活动产生的现金流量净额,
    :param float net_operate_cash_flow_ps_ttm : 每股经营活动产生的现金流量净额_TTM,
    :param float total_operating_revenue_ps : 每股营业总收入,
    :param float operating_revenue_ps : 每股营业收入,
    :param float operating_revenue_ps_ttm : 每股营业收入（TTM）,
    :param float ebit_ps : 每股息税前利润,
    :param float cash_flow_ps : 每股现金净流量,
    :param float cash_flow_ps_ttm : 每股现金流量净额_TTM,
    :param float divid_ps : 每股股息,

    代码调用:
        from hs_udata importhk_per_share_index
hk_per_share_index() 

    结果输出:
        
    """

    int_param =[]
    float_param =['basic_eps', 'diluted_eps', 'new_np_parent_company_owners_t', 'eps_ttm', 'naps', 'se_without_mi_t', 'net_operate_cash_flow_ps', 'net_operate_cash_flow_ps_ttm', 'total_operating_revenue_ps', 'operating_revenue_ps', 'operating_revenue_ps_ttm', 'ebit_ps', 'cash_flow_ps', 'cash_flow_ps_ttm', 'divid_ps']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "currency_type": currency_type,
        "trading_date": convert_date(trading_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_per_share_index", url_path="hk_market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("report_date").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_solvency(en_prod_code=None, report_date=None, report_type=None, fields=None):
    """
    获取港股偿债能力的指标，如流动比率、速动比率、货币资金/流动负债、产权比率、负债净值比率、已获利息倍数、长期负债比率等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str report_date : 申报日期，默认"2020-12-31"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str report_date : 申报日期,
    :param float current_ratio : 流动比率,
    :param float quick_ratio : 速动比率,
    :param float mon_curr_liabily : 货币资金/流动负债,
    :param float cashflow_inter_coverage_ratio : 现金流量利息保障倍数,
    :param float debt_equity_ratio : 产权比率,
    :param float sewmi_to_total_liability : 归属母公司股东的权益/负债合计,
    :param float net_operate_cashflow_tse : 现金与总资产的比率,
    :param float net_debt_equity_ratio : 负债净值比率,
    :param float nocf_to_current_liability : 经营活动产生现金流量净额/流动负债,
    :param float nocf_to_t_liability : 经营活动产生现金流量净额/负债合计,
    :param float interest_earned : 已获利息倍数,
    :param float long_debt_to_working_capital : 长期负债与营运资金比率,
    :param float total_nc_liability_tl : 长期负债占比,

    代码调用:
        from hs_udata import hk_solvency
hk_solvency() 

    结果输出:
        
    """

    int_param =[]
    float_param =['current_ratio', 'quick_ratio', 'mon_curr_liabily', 'cashflow_inter_coverage_ratio', 'debt_equity_ratio', 'sewmi_to_total_liability', 'net_operate_cashflow_tse', 'net_debt_equity_ratio', 'nocf_to_current_liability', 'nocf_to_t_liability', 'interest_earned', 'long_debt_to_working_capital', 'total_nc_liability_tl']
    params = {
        "en_prod_code": en_prod_code,
        "report_date": report_date,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_solvency", url_path="hk_market_data", **params)

@args_check(
    check("secu_code").is_instance((str, None.__class__)),
    check("classification").is_instance((str, None.__class__)),
    check("end_date").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_mainincomestru(secu_code=None, classification=None, end_date=None, fields=None):
    """
    

    输入参数：
    :param str secu_code : 证券代码，默认"01629"
    :param str classification : 分类，默认"20"
    :param str end_date : 截止日期，默认"now"
    :param str fields : 字段集合

    输出参数：
    :param str secu_code : 证券代码,
    :param str secu_abbr : 证券简称,
    :param str end_date : 截止日期,
    :param str period_mark : 日期标志,
    :param float classification : 分类,
    :param float number : 序号,
    :param str items_name : 项目名称,
    :param float subsection_income_f_year : 同期分部收入(元),
    :param float sale_in_dome_mark_inco_f_year : 同期对内销售(元),
    :param float subse_perfor_former_year : 同期分部业绩(元),
    :param float capital_expense_f_year : 同期资本开支(元),
    :param float subsection_asset_at_begi : 期初分部资产(元),
    :param float subsection_owes_at_begi : 期初分部负债(元),
    :param float subsection_income_t_period : 本期分部收入(元),
    :param float sale_in_dome_mark_inco_t_peri : 本期对内销售(元),
    :param float subse_perfo_this_period : 本期分部业绩(元),
    :param float capital_expense_t_period : 本期资本开支(元),
    :param float subsection_asset_at_end : 期末分部资产(元),
    :param float subsection_owes_at_end : 期末分部负债(元),
    :param float f_earning_before_tax : 同期除税前溢利(元),
    :param float t_earning_before_tax : 本期除税前溢利(元),
    :param float currency_unit : 面值单位,

    代码调用:
        from hs_udata import hk_mainincomestru
hk_mainincomestru() 

    结果输出:
        
    """

    int_param =[]
    float_param =['classification', 'number', 'subsection_income_f_year', 'sale_in_dome_mark_inco_f_year', 'subse_perfor_former_year', 'capital_expense_f_year', 'subsection_asset_at_begi', 'subsection_owes_at_begi', 'subsection_income_t_period', 'sale_in_dome_mark_inco_t_peri', 'subse_perfo_this_period', 'capital_expense_t_period', 'subsection_asset_at_end', 'subsection_owes_at_end', 'f_earning_before_tax', 't_earning_before_tax', 'currency_unit']
    params = {
        "secu_code": secu_code,
        "classification": classification,
        "end_date": convert_date(end_date),
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_mainincomestru", url_path="hk_market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("year").is_instance((str, None.__class__)),
    check("report_type").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_dividend(en_prod_code=None, year=None, report_type=None, fields=None):
    """
    获取港股分红的数据，如首次公告日 、事件进程 、方案说明 、每股股息 、每股特别股息(1派X元) 、每股送红股 、每
    股送红利认股证、每股派实物、货币种类 等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str year : 年度，默认"2020"
    :param str report_type : 财报类型，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param str procedure_desc : 事件进程,
    :param float currency_unit : 面值单位,
    :param float warrant_dividend_rate : 派认股证(份),
    :param float physical_dividend_rate : 派发实物(单位),
    :param float total_cash_dividend : 派现总额,
    :param float dividend_base_shares : 派发基准股数,
    :param float total_share_dividend : 红股总股数,
    :param float total_warrant_dividend : 红利认股证总份数,
    :param str statement : 方案说明,
    :param str initial_info_publ_date : 首次公告日,
    :param float cash_dividend_ps : 每股股息,
    :param float special_dividend_ps : 每股特别股息(1派X元),
    :param float stock_dividend_rate : 送股(股),

    代码调用:
        from hs_udata import hk_dividend
hk_dividend() 

    结果输出:
        
    """

    int_param =[]
    float_param =['currency_unit', 'warrant_dividend_rate', 'physical_dividend_rate', 'total_cash_dividend', 'dividend_base_shares', 'total_share_dividend', 'total_warrant_dividend', 'cash_dividend_ps', 'special_dividend_ps', 'stock_dividend_rate']
    params = {
        "en_prod_code": en_prod_code,
        "year": year,
        "report_type": report_type,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_dividend", url_path="hk_market_data", **params)

@args_check(
    check("en_prod_code").is_instance((str, None.__class__)),
    check("year").is_instance((str, None.__class__)),
    check("unit").is_instance((str, None.__class__)),
    check("fields").is_instance((str, None.__class__))
)
def hk_buyback(en_prod_code=None, year=None, unit=None, fields=None):
    """
    获取港股分红的数据，如首次公告日 、事件进程 、方案说明 、每股股息 、每股特别股息(1派X元) 、每股送红股 、每
    股送红利认股证、每股派实物、货币种类 等；

    输入参数：
    :param str en_prod_code : 证劵代码，默认"00700.HK"
    :param str year : 年度，默认"2020"
    :param str unit : 单位，默认"0"
    :param str fields : 字段集合

    输出参数：
    :param str prod_code : 证劵代码,
    :param float high_price : 最高价,
    :param float low_price : 最低价,
    :param float par_value : 面值,
    :param float cumulative_sum_to_ts : 本年累计回购数量占总股本的比例,
    :param str share_type : 份额分类,
    :param float currency_unit : 面值单位,
    :param float buyback_money : 本年累计回购金额,
    :param float buyback_sum : 回购数量,
    :param str end_date : 截止日期,

    代码调用:
        from hs_udata import hk_buyback
hk_buyback() 

    结果输出:
        
    """

    int_param =[]
    float_param =['high_price', 'low_price', 'par_value', 'cumulative_sum_to_ts', 'currency_unit', 'buyback_money', 'buyback_sum']
    params = {
        "en_prod_code": en_prod_code,
        "year": year,
        "unit": unit,
        "fields": fields,
        "int_param": int_param,
        "float_param": float_param
    }
    return get_data("hk_buyback", url_path="hk_market_data", **params)


