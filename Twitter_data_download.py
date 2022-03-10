from email.headerregistry import HeaderRegistry
from os import access
from Twitter_credentials import auth_ready_key
import requests
import json

auth_url = 'https://api.twitter.com/oauth2/token'

auth_headers = {
 'Authorization': 'Basic '+ auth_ready_key,
 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
 'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
 

access_token = auth_resp.json()['access_token']
 

search_headers = { 
    'Authorization': 'Bearer ' + access_token  
}

search_url = 'https://api.twitter.com/2/tweets/search/recent'
search_params = {
 'query': 'Python',
 'max_results': 10,
}

search_resp = requests.get(search_url, headers=search_headers, params=search_params)
Twitter_data = search_resp.json()

with open("Twitter_search_results.json", 'w') as filename:
    json.dump(Twitter_data, filename)
        
 

 

for a_Tweet in Twitter_data['data']:
    print(a_Tweet['text'] + '\n')
