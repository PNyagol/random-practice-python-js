import requests

# Your API key
API_KEY = "a0b76d29053dc145b1017bd611e21311"

# Ask the user for the city
city = input("Enter city name: ")

# Build the API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Make the request
response = requests.get(url)

# Convert the response to a Python dictionary
data = response.json()

# Handle errors safely
if response.status_code == 200 and "main" in data:
    print(f"Temperature in {city}: {data['main']['temp']}°C")
    print(f"Feels like: {data['main']['feels_like']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Condition: {data['weather'][0]['description'].title()}")
else:
    print("Error:", data.get("message", "Something went wrong"))
