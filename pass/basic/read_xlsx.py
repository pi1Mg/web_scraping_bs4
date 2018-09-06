import xlrd as xlrd


#  Open a workbook
workbook = xlrd.open_workbook('test_file.xlsx')

#  Get a sheet - method - sheet_by_index(index parameter)
worksheet = workbook.sheet_by_index(0)

#  Find total numbers of rows - .nrows
rows = worksheet.nrows

#  Read rows - row_values(row number)  - returns a tuple
for row in range(rows):
    first_col, second_col = worksheet.row_values(row)
    print(first_col, '    ', second_col)
