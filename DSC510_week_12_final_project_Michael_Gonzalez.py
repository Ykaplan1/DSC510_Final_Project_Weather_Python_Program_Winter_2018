// File: DSC510 Assignment 12 Final Project.py
// Name: Michael Gonzalez
// Date: 2/26/2019
// Course: DSC 510 - Introduction to Programming
// Desc: This program will connect the user to the open weather map database to look for weather information.
//    It will be searched by zip code or city name based in the united states.
// Usage: This program will connect the user to the open weather map database to look for weather information.
//    It will be searched by zip code or city name based in the united states.


import requests


welcome = input("Welcome to the Python Weather Report Program: Press Enter to Continue")

# requesting the weather information by city name.


def by_city():
    city = input('Please Enter Your City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=3cfb3ef209130bbc71e87da6c0f41baf&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for using the program. Good Bye!")
        exit()

# requesting the weather information by zip code.


def by_zip():
    zip_code = int(input('Please Enter Your Zip code: '))
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=3cfb3ef209130bbc71e87da6c0f41baf'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for using the program. Good Bye!")
        exit()

# This will display the weather information for the weather report.


def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))


# defining main function with while loop code to run the program


def main():
    while True:
        answer = input("Want to know the weather? Please type zippy for zip code or hood for city name: ")
        if answer == 'hood':
            try:
                print("Alright, Connection established.")
                by_city()

            except Exception:
                print("hmm, You did not enter a valid name. Try again")
                by_city()

        if answer == 'zippy':
            try:
                print("Alright, Connection established.")
                by_zip()

            except Exception:
                print("hmm, You did not enter a valid zip code numbers. Try again")
                by_zip()

        else:
            print("well, that is not one of the options. Try again.")


main()
