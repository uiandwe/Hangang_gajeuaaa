# -*- coding: utf-8 -*-
import datetime
import re

def remove_special_character(str_param):
    return ''.join(e for e in str_param if e.isalnum())


def valid_str_date_format(str_date):
    length = len(str_date)
    if length == 8 or length == 6 or length == 4:
        return True
    return False


def reg_sub_date_format(str_date):
    length = len(str_date)

    if length == 8:
        return re.sub(r'(\d{4})(\d{2})(\d{2})', r'\1-\2-\3', str_date)
    elif length == 6:
        return re.sub(r'(\d{4})(\d{2})', r'\1-\2', str_date)
    else:
        return str_date


def str_to_datetime(str_date):
    return datetime.datetime.strptime(str_date, "%Y-%m-%d").date()
