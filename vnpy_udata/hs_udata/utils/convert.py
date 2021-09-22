# -*- coding: utf-8 -*-


def convert_param(_type, param):
    if param is None:
        return _type()              #返回该类型空值

    return param


def convert_fields(field):
    if field is None:
        return []

    if isinstance(field, list):
        return field

    if isinstance(field, str):
        return [field]

    raise ValueError("字段[{}]类型转换失败，支持[None, str, list]类型，实参类型为[{}]".format(field, type(field)))
