from enum import Flag
import xlrd
import csv
from numbers import Number
from datetime import datetime

source_workbook = xlrd.open_workbook('fredgraph.xls')
source_workbook_metadata = open('fredgraph_metadata.txt', 'w')

for sheet_name in source_workbook.sheet_names():
    current_sheet = source_workbook.sheet_by_name(sheet_name)
    output_file = open('xls_' + sheet_name + '_dates.csv', 'w')
    output_writer = csv.writer(output_file)
    
    is_table_data = False
    
    for row_num, row in enumerate(current_sheet.get_rows()):
        first_entry = current_sheet.row_values(row_num)[0]
        
        if first_entry == 'observation_date':
            is_table_data = True
        
        if is_table_data:
            the_date_num = current_sheet.row_values(row_num)[0]
            U6_value = current_sheet.row_values(row_num)[1]
            new_row = [the_date_num, U6_value]
            
            if isinstance(the_date_num, Number):
                the_date_num = xlrd.xldate.xldate_as_datetime(the_date_num, source_workbook.datemode)
                
                new_row[0] = the_date_num.strftime('%m/%d/%Y')
            
            output_writer.writerow(new_row)
        
        else:
            for item in current_sheet.row(row_num):
                source_workbook_metadata.write(str(item.value))
                source_workbook_metadata.write('\t')
            
            source_workbook_metadata.write('\n')
    
    output_file.close()
    source_workbook_metadata.close()    
                
        
    