from xlsxwriter import Workbook


#  Make a workbook
workbook = Workbook('test_file.xlsx')
print('Writing the file: "{}"'.format(workbook.filename))


#  Add a work sheet
worksheet = workbook.add_worksheet()


#  Write a function - parameters - (row, column, value)
for row in range(200):
    worksheet.write(row, 0, 'Row number:')
    worksheet.write(row, 1, row)

#  Always close a workbook
workbook.close()
