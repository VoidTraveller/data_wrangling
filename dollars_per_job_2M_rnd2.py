from operator import le
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

ppp_data = pd.read_csv('public_150k_plus_borrower_fingerprint_a.csv')
print(ppp_data[ppp_data['JobsReported']<=0])
ppp_data.drop(labels=[437083,765398],axis=0)

dollars_per_job = ppp_data['CurrentApprovalAmount']/ppp_data['JobsReported']
ppp_data.insert(3,'Dollars per Job', dollars_per_job)

pps_loans = ppp_data[ppp_data['ProcessingMethod'] == 'PPS']
pps_got_2M = pps_loans[pps_loans['CurrentApprovalAmount'] == 2000000.00]
print("Actual $2M second-round loans:")
print(pps_got_2M.shape)

biz_names = pd.unique(pps_got_2M['BorrowerNameFingerprint'])
biz_names_df = pd.DataFrame(biz_names, columns=['BorrowerNameFingerprint'])

fill_column = np.full((len(biz_names),1), '2Mil2ndRnd')
biz_names_df['GotSecond'] = fill_column

second_round_max = pd.merge(ppp_data, biz_names_df, on=['BorrowerNameFingerprint'])
second_max_all_loans = second_round_max[second_round_max['GotSecond'] == '2Mil2ndRnd']

print('Total # of loans approved for most orgs that got $2M for second round:')
print(second_max_all_loans.shape)
total_funds = second_max_all_loans['CurrentApprovalAmount'].sum()
print("Total funds approved for identified orgs that could have second-round max:")
print(total_funds)

sns.set_theme(style='whitegrid')
fig, ((row1col1)) = plt.subplots(nrows=1, ncols=1)

date_based = sns.histplot(data=second_max_all_loans, x='Dollars per Job',hue='ProcessingMethod', ax=row1col1)
# show the plots!
plt.show()