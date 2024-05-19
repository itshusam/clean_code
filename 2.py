class WeatherFetcher:
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city, {})

class WeatherParser:
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data.get("city", "Unknown City") 
        temperature = data.get("temperature", "Unknown")
        condition = data.get("condition", "Unknown")
        humidity = data.get("humidity", "Unknown")
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

def main():
    weather_fetcher = WeatherFetcher()
    weather_parser = WeatherParser()

    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        data = weather_fetcher.fetch_weather_data(city)
        if detailed == 'yes':
            forecast = weather_parser.parse_weather_data(data)
        else:
            forecast = weather_fetcher.fetch_weather_data(city)
        print(forecast)

if __name__ == "__main__":
    main()