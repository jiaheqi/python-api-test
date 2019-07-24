# -*- coding: UTF-8 -*-
from common.module import excel_module

"""
    将sheet中'Execute']=='Y'的所有行添加在list：r中
"""


class ExcelUtil(object):

    def __init__(self, excelPath):
        self.excel_handle = excel_module.Read_Excel(excelPath)

    def next(self):
        r = []
        for name in self.excel_handle.get_all_sheet_by_name():
            self.sheet = self.excel_handle.get_sheet_by_name(name)

            # get rows number
            self.rowNum = self.excel_handle.get_number_of_rows(self.sheet)

            # get columns number
            self.colNum = self.excel_handle.get_number_of_cols(self.sheet)

            # the current column(当为1时，表示第一行title)
            self.curRowNo = 1
            self.row = self.excel_handle.get_row_values(self.sheet, 0)


            while self.hasNext():
                s = {}
                col = self.excel_handle.get_row_values(self.sheet,self.curRowNo)
                i = self.colNum

                for x in range(i):
                    s[self.row[x]] = col[x].encode('utf8')
                if(s['Execute']=='Y'):
                    r.append(s)
                self.curRowNo += 1
        return r

    def hasNext(self):
        """
        用于判断当前sheet页有没有内容：没有或者只有title则返回false
        :return:
        """
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

