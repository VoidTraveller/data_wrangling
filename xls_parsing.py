from black import out
import xlrd
import csv

source_workbook = xlrd.open_workbook("fredgraph.xls")

for sheet_name in source_workbook.sheet_names():
    current_sheet = source_workbook.sheet_by_name(sheet_name)
    print(sheet_name)
    output_file = open("xls_"+sheet_name+".csv","w")
    output_writer = csv.writer(output_file)

    for row_num, row in enumerate(current_sheet.get_rows()):
        output_writer.writerow(current_sheet.row_values(row_num))
    
    output_file.close()
