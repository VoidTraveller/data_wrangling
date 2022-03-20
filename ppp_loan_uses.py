import pandas as pd

ppp_data = pd.read_csv('public_150k_plus_recent.csv')

print(ppp_data['UTILITIES_PROCEED'].isna().sum())
# print how many rows do not list a value for `PAYROLL_PROCEED`
print(ppp_data['PAYROLL_PROCEED'].isna().sum())
# print how many rows do not list a value for `MORTGAGE_INTEREST_PROCEED`
print(ppp_data['MORTGAGE_INTEREST_PROCEED'].isna().sum())
# print how many rows do not list a value for `RENT_PROCEED`
print(ppp_data['RENT_PROCEED'].isna().sum())
# print how many rows do not list a value for `REFINANCE_EIDL_PROCEED`
print(ppp_data['REFINANCE_EIDL_PROCEED'].isna().sum())
# print how many rows do not list a value for `HEALTH_CARE_PROCEED`
print(ppp_data['HEALTH_CARE_PROCEED'].isna().sum())
# print how many rows do not list a value for `DEBT_INTEREST_PROCEED`
print(ppp_data['DEBT_INTEREST_PROCEED'].isna().sum())

payroll_only = ppp_data[(ppp_data['UTILITIES_PROCEED'].isna()) &
(ppp_data
 ['MORTGAGE_INTEREST_PROCEED'].isna()) &  
 (ppp_data['RENT_PROCEED'].isna()) &
 (ppp_data['REFINANCE_EIDL_PROCEED'].isna()) & (ppp_data
 ['HEALTH_CARE_PROCEED'].isna()) &
(ppp_data['DEBT_INTEREST_PROCEED'].isna())
 ]
# print the length of our "payroll costs only" DataFrame
print(len(payroll_only.index))

