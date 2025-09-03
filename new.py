import requests

API_KEY = "7fe2c15cf5eb2d288713cb719412f231"

city = input("City / Region: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

# print(data)

if response.status_code == 200 and "main" in data:
    print(f"Temperature in {city}: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description'].title()}")
    print (f"Feels Like: {data['main']['feels_like']}°C")
    print (f"Humidity: {data['main']['humidity']}%")

else:
    print ("Error:", data.get("message", "something went wrong"))
