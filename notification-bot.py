import requests

# -------------------------------
# 🔑 API KEYS & CONFIGURATION
# -------------------------------
OPENWEATHER_API_KEY = "a0b76d29053dc145b1017bd611e21311"  
PAGE_ACCESS_TOKEN = "your_facebook_page_access_token"
RECIPIENT_ID = "24548357528183737"

# -------------------------------
# 📌 STEP 1: Get Weather Data
# -------------------------------
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "main" in data:
        weather = data['weather'][0]['description'].title()
        temp = data['main']['temp']
        return f"Today's weather in {city}: {temp}°C, {weather}"
    else:
        return f"Error fetching weather: {data.get('message', 'Something went wrong')}"

# -------------------------------
# 📌 STEP 2: Send Message via Messenger
# -------------------------------
def send_message(message):
    url = f"https://graph.facebook.com/v12.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": RECIPIENT_ID},
        "message": {"text": message}
    }
    response = requests.post(url, json=payload)
    return response.json()

# -------------------------------
# 📌 STEP 3: Run the Bot
# -------------------------------
def main():
    city = input("Enter city name: ")
    weather_message = get_weather(city)
    print("Weather Update:", weather_message)

    fb_response = send_message(weather_message)
    print("Messenger API Response:", fb_response)

if __name__ == "__main__":
    main()
