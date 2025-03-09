import requests

# Define the latitude and longitude for Chattogram
lat = 22.3569
lon = 91.7832
API_key = 'aa40f92708fd76a4d3775579844199fc'

# Construct the API URL using lat and lon
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric'

# Send the request
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    print("Yes, we successfully hit the API!")
    data = response.json()
    print('Chattogram city weather is now have', data["weather"][0]['description'])# Print the response data to verify it
    print('Current temperature is ', data['main']['temp'])
    print('But teh temparature feels like', data['main']['feels_like'])
    print('Current humadity feels like', data['main']['humidity'])




else:
    print(f"Failed to retrieve data: {response.status_code}")
