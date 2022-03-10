from bs4 import BeautifulSoup

mta_web_page = open("MTA_turnstiles_index.html", "r")
base_url = "http://web.mta.info/developers/"

soup = BeautifulSoup(mta_web_page, 'html.parser')
data_files_section = soup.find('div', class_='span-84 last')
all_data_links = data_files_section.find_all('a')

mta_data_list = open('MTA_data_index.csv', 'w')

for a_link in all_data_links:
    complete_link = base_url + a_link['href']
    mta_data_list.write(complete_link + '\n')

mta_data_list.close()

