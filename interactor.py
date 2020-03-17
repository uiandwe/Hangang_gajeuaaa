# -*- coding: utf-8 -*-
import datetime

def remove_special_character(str_param):
    return ''.join(e for e in str_param if e.isalnum())


def str_to_datetime(str_date):
    return datetime.datetime.strptime(str_date, "%Y-%m-%d").date()
