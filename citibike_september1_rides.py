import csv


import csv

from numpy import source

source_file = open('202009CitibikeTripdataExample.csv', 'r')
output_file = open('2020-09-01-citibike-tripdata.csv', 'w')

citibike_reader = csv.DictReader(source_file)
output_writer = csv.DictWriter(output_file, fieldnames=citibike_reader.fieldnames)

output_writer.writeheader()

for a_row in citibike_reader:
    start_timestamp = a_row['starttime']
    timelist = start_timestamp.split(" ")
    the_date = timelist[0]
    
    if the_date == '2020-09-01':
        output_writer.writerow(a_row)


output_file.close()

