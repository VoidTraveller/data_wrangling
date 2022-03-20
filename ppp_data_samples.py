import pandas as pd

august_ppp_data = pd.read_csv('public_150k_plus_080820.csv')
ppp_recent = pd.read_csv('public_150k_plus_recent.csv')

august_sample = august_ppp_data.head()
august_sample.to_csv('august_sample.csv', index=False)

recent_sample = ppp_recent.head()
recent_sample.to_csv('recent_sample.csv', index=False)