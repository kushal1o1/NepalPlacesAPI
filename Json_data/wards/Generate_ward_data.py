import requests
from bs4 import BeautifulSoup
import json

# URLs
districts_url = 'https://en.wikipedia.org/wiki/List_of_municipalities_of_Nepal'
city_base_url = 'https://en.wikipedia.org/wiki/'

# Fetch the list of municipalities
response = requests.get(districts_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract city names from the relevant section
cities = []
for link in soup.select('table.wikitable tbody tr td a'):
    city_name = link.text.split(' ')[0]  # Take only the first word of each city name
    cities.append(city_name)

wards_data = []

for city in cities:
    city_url = city_base_url + city.replace(" ", "_")
    city_response = requests.get(city_url)
    city_soup = BeautifulSoup(city_response.content, 'html.parser')
    
    # Find the specific table for wards
    table = city_soup.find('table', {'class': 'wikitable floatright', 'style': 'width:25%;text-align:center'})
    
    if table:
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) >= 2:
                ward_no = columns[0].text.strip()
                ward_name = columns[1].text.strip()
                wards_data.append({
                    "city": city,
                    "ward_no": ward_no,
                    "name": ward_name
                })

# Save the data to a JSON file
with open('Wards_from_all_cities_in_Nepal.json', 'w', encoding='utf-8') as json_file:
    json.dump(wards_data, json_file, ensure_ascii=False, indent=4)

print('Successfully saved data to Wards_from_all_cities_in_Nepal.json')
