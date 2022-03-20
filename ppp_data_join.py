import pandas as pd 

august_ppp_data = pd.read_csv('public_150k_plus_080820.csv')
recent_ppp_data = pd.read_csv('public_150k_plus_recent.csv')

merged_data = pd.merge(august_ppp_data, recent_ppp_data, how='outer', left_on=['BusinessName','Lender','DateApproved'],
                       right_on=['BorrowerName','ServicingLenderName','DateApproved'], indicator=True)

merged_data_no_date = pd.merge(august_ppp_data, recent_ppp_data, how='outer', left_on=['BusinessName','Lender'],
                       right_on=['BorrowerName','ServicingLenderName'], indicator=True)

merger_data_biz_name = pd.merge(august_ppp_data, recent_ppp_data, how='outer', left_on=['BusinessName'],
                       right_on=['BorrowerName'], indicator=True)

print(merged_data.value_counts('_merge'))
print('\n')
print(merged_data_no_date.value_counts('_merge'))
print('\n')
print(merger_data_biz_name.value_counts('_merge'))