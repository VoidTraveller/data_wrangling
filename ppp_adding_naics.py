import csv
import pandas as pd 

ppp_data = pd.read_csv('public_150k_plus_fingerprints.csv', dtype='string')

sba_naics_data = pd.read_csv('SBA-NAICS-data.csv', dtype='string',encoding='utf-8',sep=';')

ppp_data['NAICSCode'] = ppp_data['NAICSCode'].fillna('None')

merged_data = pd.merge(ppp_data, sba_naics_data, how='left',
                       left_on=['NAICSCode'], right_on=['NAICS Codes'], indicator=True)

merged_data_file = open('ppp-fingerprints-and-naics.csv', 'w', encoding='utf-8')
merge_result = merged_data.to_csv(encoding='utf-8')
merged_data_file.write(merge_result)

print(merged_data.value_counts('_merge'))

unmathed_values = merged_data[merged_data['_merge'] == 'left_only']
unmatched_values_file = open('ppp-unmatched-naics-codes.csv', 'w', encoding='utf-8')

unmatched_values_file.write(unmathed_values.value_counts('NAICSCode').to_csv(encoding='utf-8'))

merged_data_file.close()
unmatched_values_file.close()

