import xlsxwriter
workbook = xlsxwriter.Workbook('c:\\temp\\Welocme.xlsx')
worksheet = workbook.add_worksheet()
cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
cell_format.set_font_size(16)
cell_format.set_underline(2)
cell_format.set_align('center')
cell_format1 = workbook.add_format({'font_color': 'blue'})
cell_format1.set_align('center')
worksheet.write('A1', 'Name', cell_format)
worksheet.write('B1', 'Department', cell_format)
row = 1
col = 0
data = (['Yashar', 'Hi, You are on iYashar.ir'],['Mehdi','How do you get to see a physiotherapist?'],['Mitra', 'I am a student of class 1 in Hafez primary school.'],['Yasaman','Are you a Bank Manager?'],)
worksheet.set_column('B1:B1', 60)
worksheet.set_column('B2:B5',60,cell_format1)
worksheet.set_column('A1:A5', 20,cell_format1)
for name, score in (data):
     worksheet.write(row, col, name)
     worksheet.write(row, col + 1, score)
     row += 1
workbook.close()