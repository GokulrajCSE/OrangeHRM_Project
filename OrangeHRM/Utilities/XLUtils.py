from xlrd import *

filepath = r"../excel/OrangeHRM_Login_TestData.xlsx"

def read_locators( sheet_name):
    workbook = open_workbook(filepath)
    sheet = workbook.sheet_by_name(sheet_name)
    count = sheet.nrows
    d = {}
    for i in range(1,count):
        data = sheet.row_values(i)
        d[data[0]] = [data[1],data[2]]
    return d

def read_data(sheet_name):
    workbook = open_workbook(filepath)
    sheet = workbook.sheet_by_name(sheet_name)
    count = sheet.nrows
    d = []
    for i in range(1,count):
        data = sheet.row_values(i)
        d.append(data[3:5])
    return d

# print(read_data("Login_TestData"))