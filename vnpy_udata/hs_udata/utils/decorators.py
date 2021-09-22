# -*- coding: utf-8 -*-
import time
import inspect
from functools import wraps


def retry(count, exp_name, time_delta=1.0):
    def decorate(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            assert count
            exec_count = 1
            while exec_count < count:
                try:
                    return func(*args, **kwargs)
                except exp_name as ex:       #返回func时异常
                    exec_count += 1
                    if exec_count == count:
                        raise ex
                    print("Retry because %s", ex)
                    if time_delta:
                        time.sleep(time_delta)

        return wrap

    return decorate


functions = []


def lru_cache(*args, **kwargs):
    from functools import lru_cache as _lru_cache

    def decorator(func):
        func = _lru_cache(*args, **kwargs)(func)    #用_lru_cache进行缓存
        functions.append(func)      #将函数及其参数寸在列表中
        return func

    return decorator


def args_check(*checks):      #装饰器函数返回其子函数decorator
    def decorator(func):      #函数执行时再调用内层子函数
        @wraps(func)
        def wrap(*args, **kwargs):    #函数的参数传给wrap
            call_args = None
            for check in checks:          #逐步执行args_check中每一个参数
                if call_args is None:
                    call_args = inspect.getcallargs(get_original_func(func), *args, **kwargs)  #使用inspect模块的getcallargs方法返回一个将参数名字和值作为键值对的字典(按照形参和实际传入参数的位置形成键值对)

                check.check(func.__name__, call_args.get(check.arg_name, check.arg_name), kwargs)

            return func(*args, **kwargs)
        return wrap

    return decorator


def get_original_func(func):
    func_wrapped = getattr(func, "__wrapped__", None)          #获取函数__wrapped__属性，默认None
    while func_wrapped:                                        #通过循环获取最内层函数属性并最终返回
        func = func_wrapped
        func_wrapped = getattr(func, "__wrapped__", None)

    return func


class ArgumentChecker(object):

    def __init__(self, args_name):
        self._args_name = args_name
        self._functions = []
        self._required_func = None

    def is_instance(self, _types):
        from hs_udata.utils.error import InvalidArgument

        def warp(func, value):
            if not isinstance(value, _types):      #检查值是否是某一特定类型
                raise InvalidArgument("函数[{}] 参数类型异常，参数[{}]有效类型为[{}]，实参类型为[{}]".format(
                    func, self._args_name, _types, type(value)))

        self._functions.append(warp)          #调外层函数时将函数及其值存入，等内层函数执行时判断
        return self

    def is_required(self):
        from hs_udata.utils.error import InvalidArgument

        assert self.arg_name
        if not isinstance(self.arg_name, (tuple, list)):
            raise InvalidArgument("必填项装饰器，参数的有效类型为元组或数组，实参类型为[{}]".format(type(self._args_name)))

        def warp(func, value):
            checkd = False
            for name in self.arg_name:
                if name in value.keys() and value[name]:
                    checkd = True
                    break

            if not checkd:
                raise InvalidArgument("函数[{}] 必填项参数异常，参数[{}]至少填其中一个，实参传入为{}".format(
                    func, self._args_name, list(value.keys())))

        self._required_func = warp
        return self

    def check(self, func, value, kwargs):            #取出_functions内容进行检查
        if self._required_func:
            self._required_func(func, kwargs)
            return

        for check_func in self._functions:
            check_func(func, value)

    @property
    def arg_name(self):
        return self._args_name


def check(arg_name):      #在调用此函数时再调用ArgumentChecker类
    return ArgumentChecker(arg_name)

