#coding=utf-8

# def read_xl_(filename,book_name):
#     import xlrd
#     file = xlrd.open_workbook(filename)
#     sheet = file.sheet_by_name(book_name)
#     print sheet
#     return sheet
#     nr = sheet.nrows()
#     for i in range(1,nr):
#         list = sheet.row_values(i)
#         key,data,position = list[2],list[3],list[4]
#         print key,data,position

# def read_data_(filename, book_name,n):
#     sheet = read_xl_(filename, book_name)
# #     n = sheet.nrows()
#     for i in range(1,n):
#         list = sheet.row_values(i)
#         print list[2]

class Readxl():
#     def __init__(self,filename,book_name):
#         self.filename = filename
#         self.book_name = book_name
    def read_xl_(self,filename,book_name):
        import xlrd
        file = xlrd.open_workbook(filename)
        sheet = file.sheet_by_name(book_name)
        print sheet
        return sheet
    
    def read_data_(self,filename, book_name):
        sheet = self.read_xl_(filename, book_name)
        nr = sheet.nrows
#         print nr
        for i in range(1,nr):
            list = sheet.row_values(i)
            print list

rx = Readxl()
list = rx.read_data_("E:/keyword/testcase.xls", "booking")
print list














