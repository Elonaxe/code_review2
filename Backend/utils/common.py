# -*- coding: utf-8 -*-
from flask import jsonify

def get_response(code, data, msg=None):
    """
    :param code: 字段 resp_code: 响应状态码
    :param data: 字段 data: 返回结果，格式为字典
    :param msg: 字段 resp_msg: 响应消息文本，返回成功默认设置为"ok"
    """
    res = {
        'resp_code': code,
        'resp_msg': msg if msg else 'ok',
        'data': data
    }
    return jsonify(res)