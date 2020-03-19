# -*- coding: utf-8 -*-
from interactor import remove_special_character, valid_str_date_format, reg_sub_date_format


class Valid:
    def __init__(self):
        pass

    def date_format(self, str_date):
        str_date = str(str_date)

        str_date = remove_special_character(str_date)

        assert valid_str_date_format(str_date)

        return reg_sub_date_format(str_date)
