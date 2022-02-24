import csv
filename = "ghcnd-stations"

source_file = open(filename+".txt", "r")
stations_list = source_file.readlines()


output_file = open(filename+".csv","w")
output_writer = csv.writer(output_file)
headers = ["ID","LATITUDE","LONGITUDE","ELEVATION","STATE","NAME","GSN_FLAG",
 "HCNCRN_FLAG","WMO_ID"]

output_writer.writerow(headers)

for line in stations_list:
    new_row = []

    # ID: positions 1-11
    new_row.append(line[0:11])
    # LATITUDE: positions 13-20
    new_row.append(line[12:20])
    # LONGITUDE: positions 22-30
    new_row.append(line[21:30])
    # ELEVATION: positions 32-37
    new_row.append(line[31:37])
    # STATE: positions 39-40
    new_row.append(line[38:40])
    # NAME: positions 42-71
    new_row.append(line[41:71])
    # GSN_FLAG: positions 73-75
    new_row.append(line[72:75])
    # HCNCRN_FLAG: positions 77-79
    new_row.append(line[76:79])
    # WMO_ID: positions 81-85
    new_row.append(line[80:85])


 

    output_writer.writerow(new_row)

output_file.close()