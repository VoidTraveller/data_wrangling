import requests
from FRED_credentials import my_api_key

FRED_endpoint = "https://api.stlouisfed.org/fred/series/observations?"
FRED_parameters = "series_id=U6RATE&file_type=json"
complete_data_URL = FRED_endpoint + FRED_parameters + "&api_key=" + my_api_key

FRED_output_file = open('FRED_API_data.json', 'w')
FRED_data = requests.get(complete_data_URL)

FRED_output_file.write(FRED_data.text)
FRED_output_file.close()

