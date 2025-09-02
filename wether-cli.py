import requests

API_KEY = "a0b76d29053dc145b1017bd611e21311"

def get_weather(city):
    """Fetch weather data for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json(), response.status_code

def show_menu():
    """Display the menu options."""
    print("\n--- Weather Info Menu ---")
    print("1. Temperature")
    print("2. Feels Like")
    print("3. Humidity")
    print("4. Wind Speed")
    print("5. Weather Condition")
    print("6. Show All")
    print("0. Exit")

def main():
    city = input("Enter city name: ")
    data, status = get_weather(city)

    if status != 200 or "main" not in data:
        print("Error:", data.get("message", "Something went wrong"))
        return

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Temperature in {city}: {data['main']['temp']}°C")
        elif choice == "2":
            print(f"Feels like: {data['main']['feels_like']}°C")
        elif choice == "3":
            print(f"Humidity: {data['main']['humidity']}%")
        elif choice == "4":
            print(f"Wind speed: {data['wind']['speed']} m/s")
        elif choice == "5":
            print(f"Condition: {data['weather'][0]['description'].title()}")
        elif choice == "6":
            print(f"--- Weather in {city} ---")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Feels like: {data['main']['feels_like']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind speed: {data['wind']['speed']} m/s")
            print(f"Condition: {data['weather'][0]['description'].title()}")
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice! Please enter a number from 0 to 6.")

if __name__ == "__main__":
    main()
