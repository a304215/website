import xlrd
import xlwt
filename_input = 'input.xls'
book = 











input_list = []
list_store_data = []
filename_output = 'output.xls'
book = xlwt.Workbook()
sheet1 = book.add_sheet('KID')
for i in input_list:
    input_str = i
    input_leagth = len(input_str)
    disance = 9-input_leagth
    plus_zero = "0" * disance
    final_str = plus_zero + input_str
    sheet1.write(0,0,final_str)
book.save(filename_output)
