from turtle import color
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ppp_data = pd.read_csv("public_150k_plus_recent.csv")

sns.set_theme(style='whitegrid')

mean = ppp_data['CurrentApprovalAmount'].mean()
median = ppp_data['CurrentApprovalAmount'].median()

Q1 = ppp_data['CurrentApprovalAmount'].quantile(0.25)
Q3 = ppp_data['CurrentApprovalAmount'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)

approved_loan_plot = sns.histplot(data=ppp_data, x='CurrentApprovalAmount')

y_axis_range = approved_loan_plot.get_ylim()

approved_loan_plot.vlines(mean, 0, y_axis_range[1], color='gray', ls='-')
approved_loan_plot.vlines(median, 0, y_axis_range[1], color='black', ls='-')
approved_loan_plot.vlines(lower_bound, 0, y_axis_range[1], colors='black', ls=':')
approved_loan_plot.vlines(Q1, 0, y_axis_range[1], color='black', ls=':')
approved_loan_plot.vlines(Q3, 0, y_axis_range[1], color='red', ls=':')
approved_loan_plot.vlines(upper_bound, 0, y_axis_range[1], color='black', ls=':')

plt.show() 

