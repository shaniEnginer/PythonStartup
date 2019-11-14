from openpyxl import Workbook


workbook=Workbook()

sheet=workbook.active


sheet['A1']="Data written by Openpyxl"

workbook.save(filename="test.xlsx")