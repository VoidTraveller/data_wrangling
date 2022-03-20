import pandas as pd
import fingerprints

ppp_data = pd.read_csv('public_150k_plus_recent.csv')

unique_names = ppp_data['OriginatingLender'].unique()
print(len(unique_names))

fingerprint_list = []

for name in unique_names:
    fingerprint_list.append(fingerprints.generate(name))

fingerprint_set = set(fingerprint_list)
print(len(fingerprint_set))
    