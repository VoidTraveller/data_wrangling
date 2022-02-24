import imp
from pyexcel_ods3 import get_data
import csv

source_workbook = get_data('fredgraph.ods')

for sheet_name, sheet_data in source_workbook.items():
    print(sheet_name)

    output_file = open("ods_" + sheet_name + ".csv", 'w')
    output_writer = csv.writer(output_file)

    for row in sheet_data:
        output_writer.writerow(row)
    
    output_file.close()