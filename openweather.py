import requests

API_KEY = "a0b76d29053dc145b1017bd611e21311"

city = "Kisumu"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

print(data)

print(f"Temperature in {city}: {data['main'] ['temp']}°C")