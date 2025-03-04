import requests


def main():
    location = ['London', 'SVO', 'Череповец']
    url_temp = 'https://wttr.in/{}?nMmTqF&lang=ru'
    for forecast in location:
        url = url_temp.format(forecast)
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    main()