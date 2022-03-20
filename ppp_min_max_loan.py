import pandas as pd

ppp_data = pd.read_csv('public_150k_plus_recent.csv')

print(ppp_data['CurrentApprovalAmount'].min())
print(ppp_data['CurrentApprovalAmount'].max())