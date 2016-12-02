# -*- encoding=utf-8 -*-
from django import template
register = template.Library()

@register.filter
def divide(value, divisor):
    """
    计算除法（浮点数）
    :param value:
    :param divisor:
    :return:
    """
    if not value:return None
    if not divisor:return None
    try:
        return float(value) / float(divisor)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter
def describe(value,dict_str):
    """
    根据key值，返回对应的描述值
    :param value:
    :param dict_str:
    :return:
    """
    dict_items=dict_str.split(",")
    dict={}
    for item in dict_items:
        key_value_pair=item.split(":")
        dict[key_value_pair[0]] = key_value_pair[1]
    try:
        return dict[int(value)]
    except Exception as e:
        try:
            return dict[str(value)]
        except Exception as e:
            try:
                return dict[value]
            except Exception as e:
                return None


@register.filter
def range_pagination_5(curr,end):
    """
    分页用的过滤器，显示5页
    :param curr:
    :param end:
    :return:
    """
    if curr==end:
        if end <= 5:
            result=[i+1 for i in range(end)]
        else:
            result=[curr-4+i for i in range(5)]
            if result.__len__()==0:
                result=[i+1 for i in range(curr)]
    elif curr==1:
        if end > 5:
            result=[curr+i for i in range(5)]
        else:
            result=[curr+i for i in range(end)]
    elif curr==end-1:
        if end <= 5:
            result=[i+1 for i in range(end)]
        else:
            result = [curr - 3 + i for i in range(4)]
            if result==[]:
                result = [i + 1 for i in range(end)]
            else:
                result.append(end)
    elif curr==2:
        result=[curr+i for i in range(4)]
        result.insert(0,1)
    else:
        result=[curr-2,curr-1,curr,curr+1,curr+2]
    return result

