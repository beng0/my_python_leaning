#coding=utf-8

#1.导入excel读取的模块
import xlrd
#导入浏览器操作的页面
from runBrower import *
r = Browser_()

def readExcel(sname):
    #2.定位到测试用例文档的位置
    filename = "E:/keyword/testcase.xls"
    #3.使用模块打开这个文档
    file = xlrd.open_workbook(filename)
    #4.在表格中打开需要操作的页面,sname就是子页面的名字
    sheet = file.sheet_by_name(sname)
    #5.查看该页面中现在有多少行数据
    nr = sheet.nrows
    #6.遍历这个页面，循环的去读取每一行的值
    for i in range(1,nr):
        #row_values(index) 根据行号去读取行的数据，一个格子是列表的一个元素
        list = sheet.row_values(i)
        #key是操作动作，data是数据，position是元素的位置
        key,data,position=list[2],list[3],list[4]
        print key,data,position
        #判断当前行的操作是什么，根据不同的动作来调用不同的浏览器操作方法
        if key == "open":
            r.open_(data)
        elif key == "click":
            r.click_(position)
        elif key == "input":
            r.input_(position, data)
        elif key == "js":
            r.js_(data)
        elif key == "upload":
            r.upload_(data, position)
        elif key == "frame":
            r.frame_(data, position)
        elif key == "sleep":
            r.sleep_(data)
        elif key == "random":
            r.random_(position)
        elif key == "check":
            ele = r.check_(position)
            return ele
        else:
            print "没有这个关键字"








