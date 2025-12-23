import requests

def get_weather(city, unit):
    print(f"Checking weather for {city}...")
    
    #API
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        data = response.json()

        #get data from json
        current_condition = data['current_condition'][0]
        temp_c = current_condition['temp_C']
        temp_f = current_condition["temp_F"]
        desc = current_condition['weatherDesc'][0]['value']
        humidity = current_condition['humidity']

        print(f"\n--- Weather in {city.capitalize()} ---")

        if unit == "F":
            print(f"Temperature: {temp_f}°F")
        else: 
            print(f"Temperature: {temp_c}°C")

        print(f"Condition: {desc}")
        print(f"Humidity: {humidity}%")

    except Exception:
        print("Error fetching data. Check city name or internet connection")


city_input = input("Enter a city name: ")
unit_input = input("Choose temperature unit (C or F): ").upper()

if unit_input not in ["C", "F"]:
    print("Invalid choice. Defaulting to Celsius.")
    unit_input = "C"

get_weather(city_input, unit_input)
