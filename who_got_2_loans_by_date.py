import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

ppp_data = pd.read_csv('public_150k_plus_borrower_fingerprint_a.csv')
ppp_data['DateApproved'] = pd.to_datetime(ppp_data['DateApproved'])

second_round_start = pd.to_datetime('2021-01-13')
todays_date = pd.to_datetime('today')
program_start = pd.to_datetime('2020-01-01')

loan_round = pd.cut(ppp_data.DateApproved,
                    bins=[program_start,second_round_start,todays_date],
                    labels=['first_round', 'maybe_second'])
ppp_data.insert(2,'Loan Round',loan_round)

loan_count = ppp_data.pivot_table(index=['BorrowerNameFingerprint'], aggfunc='size')
loan_count_df = loan_count.to_frame('Loan Count')
print("Description of duplicate borrower table:")
print(loan_count_df.describe())

sorted_loan_counts = loan_count_df.sort_values(by='Loan Count', ascending=False)
more_than_two = sorted_loan_counts[sorted_loan_counts['Loan Count']>2]

print("Businesses that seem to have gotten more than 2 loans:")
print(more_than_two.shape)

print("Number of businesses that appear to have gotten precisely 2 loans:")
precisely_two = sorted_loan_counts[sorted_loan_counts['Loan Count'] == 2]
print(precisely_two.shape)

pps_loans = ppp_data[ppp_data['ProcessingMethod'] == 'PPS']
print("Number of loans labeled as second round:")
print(pps_loans.shape)

ppp_data_w_lc = pd.merge(ppp_data, loan_count_df,on=['BorrowerNameFingerprint'], how='left')
matched_two_loans = ppp_data_w_lc[(ppp_data_w_lc['Loan Count'] == 2)]
maybe_round2_2M = matched_two_loans[(matched_two_loans[ 'CurrentApprovalAmount'] == 2000000.00) & 
                                    (matched_two_loans['Loan Round'] =='maybe_second')]
print("Derived $2M second-round loans:")
print(maybe_round2_2M.shape)

pps_got_2M = pps_loans[pps_loans['CurrentApprovalAmount'] == 2000000.00]
print("Actual $2M second-round loans:")
print(pps_got_2M.shape)

