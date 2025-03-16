import os
import requests
import colorama
import threading

def display_thread() -> None:
    print('-' * 10)
    print(f"[{colorama.Fore.GREEN}+{colorama.Fore.RESET}] Current process PID: {os.getpid()}")
    print(f"[{colorama.Fore.GREEN}+{colorama.Fore.RESET}] Thread count: {threading.active_count()}")
    print(f"[{colorama.Fore.GREEN}+{colorama.Fore.RESET}] Active threads:")
    for thread in threading.enumerate():
        print('\t' + str(thread))

def get_weather_info(city:str) -> None:
    API_KEY:str = "<API_KEY>"
    URL:str = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"[{colorama.Fore.GREEN}+{colorama.Fore.RESET}] The temperature of city {city} is {temp} degrees celsius and "
              f"it's weather is {weather}")
    else:
        raise Exception(response.status_code)

def main(cities:list) -> None:
    print(f"[{colorama.Fore.GREEN}+{colorama.Fore.RESET}] Parent process started {os.getpid()}")
    threads = []
    display_thread()
    print(f"[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] Start requesting ...")
    for city in cities:
        threads.append(threading.Thread(target=get_weather_info, args=(city,)))
        threads[-1].start()
    display_thread()

if __name__ == "__main__":
    cities = [
        "Tehran",
        "New york",
        "Sydney",
        "London",
        "Tokyo",
        "Berlin",
        "Rome"
    ]
    main(cities)