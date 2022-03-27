import csv
import fingerprints

ppp_data = open('public_150k_plus_recent.csv', 'r')
ppp_data_reader = csv.DictReader(ppp_data)

augmented_ppp_data = open('public_150k_plus_borrower_fingerprint_a.csv', 'w')
augmented_data_writer = csv.writer(augmented_ppp_data)

header_row = []

for item in ppp_data_reader.fieldnames:
    header_row.append(item)
    
    if item == 'BorrowerName':
        header_row.append('BorrowerNameFingerprint')
        
augmented_data_writer.writerow(header_row)

for row in ppp_data_reader:
    new_row = []
    
    for column_name in ppp_data_reader.fieldnames:
        new_row.append(row[column_name])
        
        if column_name == 'BorrowerName':
            try:
                the_fingerprint = fingerprints.generate(row[column_name]) +" "+ fingerprints.generate(row['BorrowerCity'])+" "+row['BorrowerState']
            except(TypeError):
                the_fingerprint = fingerprints.generate("MISSING") +" "+ fingerprints.generate(row['BorrowerCity'])+" "+row['BorrowerState']
            
            new_row.append(the_fingerprint)
    
    augmented_data_writer.writerow(new_row)

augmented_ppp_data.close()
ppp_data.close()