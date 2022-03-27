from statistics import median
from turtle import color
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ppp_data = pd.read_csv('public_150k_plus_recent.csv')
sns.set_theme(style='whitegrid')

mean = ppp_data['CurrentApprovalAmount'].mean()
median = ppp_data['CurrentApprovalAmount'].median()
 
approvad_loan_plot = sns.histplot(data=ppp_data, x='CurrentApprovalAmount')
y_axis_range = approvad_loan_plot.get_ylim()

approvad_loan_plot.vlines(mean, 0, y_axis_range[1], color='crimson', ls=':')
approvad_loan_plot.vlines(median, 0, y_axis_range[1], color='green', ls='-')
 
plt.show()