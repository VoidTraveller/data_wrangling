import requests
import time
import os

mta_data_links = open('MTA_data_index.csv', 'r')
folder_name = 'turnstiles_data'
headers = {
 'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13597.66.0) ' + \
 'AppleWebKit/537.36 (KHTML, like Gecko) ' + \
 'Chrome/88.0.4324.109 Safari/537.36',
 'From': 'Margulan - margulan.kurmanov@gmail.com'
}

mta_links_list = mta_data_links.readlines()

if os.path.isdir(folder_name) == False:
    target_folder = os.mkdir(folder_name)

for i in range(0, 4):
    data_url = mta_links_list[i].strip()
    data_filename = data_url.split('/')[-1]
    
    turnstile_data_file = requests.get(data_url, headers=headers)
    local_data_file = open(os.path.join(folder_name, data_filename), 'w')
    local_data_file.write(turnstile_data_file.text)
    local_data_file.close()

time.sleep(2)
