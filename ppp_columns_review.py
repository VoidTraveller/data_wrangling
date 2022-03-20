import pandas as pd

ppp_data_sample = pd.read_csv('recent_sample.csv')

converted_data_sample = ppp_data_sample.convert_dtypes()

transposed_ppp_data_sample = converted_data_sample.transpose()

print(transposed_ppp_data_sample)