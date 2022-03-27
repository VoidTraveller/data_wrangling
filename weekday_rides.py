import csv
from datetime import datetime

source_file = open('202009CitibikeTripdataExample.csv', 'r')
output_file = open('202009-citibike-weekday-tripdata.csv', 'w')

citibike_reader = csv.DictReader(source_file)
output_writer = csv.DictWriter(output_file, fieldnames=citibike_reader.fieldnames)
output_writer.writeheader()

for a_row in citibike_reader:
    the_date = datetime.strptime(a_row['starttime'], '%Y-%m-%d %H:%M:%S.%f')
    if the_date.weekday() <= 4:
        output_writer.writerow(a_row)

output_file.close()