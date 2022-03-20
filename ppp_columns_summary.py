import pandas as pd

ppp_data = pd.read_csv('public_150k_plus_recent.csv')

print(ppp_data.value_counts('LoanStatus'))
print(sum(ppp_data.value_counts('LoanStatus')))

print(ppp_data.value_counts('Gender'))
print(sum(ppp_data.value_counts('Gender')))

print(ppp_data['BorrowerAddress'].isna().sum())