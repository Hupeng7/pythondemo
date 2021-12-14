#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlwt

book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('mysheet', cell_overwrite_ok=True)

sheet.write(0, 0, 'myText')
sheet.write(0, 1, 'myText')
sheet.write(0, 2, 'myText')

book.save('D:\\mypic\\test.xls')
