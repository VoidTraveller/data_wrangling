import pandas as pd

ppp_data = pd.read_csv('public_150k_plus_recent.csv')
ppp_data['DateApproved'] = pd.to_datetime(ppp_data['DateApproved'], format='%m/%d/%Y')

print(ppp_data['DateApproved'].min())
print(ppp_data['DateApproved'].max())