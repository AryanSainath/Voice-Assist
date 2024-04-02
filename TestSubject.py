import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import requests
import time
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Voice Assist. Please tell me how may I help you sir?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please......")
        return "None"
    return query
def get_weather(c8f255873a7cf0fd4a40549d9e239a20, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': c8f255873a7cf0fd4a40549d9e239a20,
        'units': 'metric' 
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        print(data)

        if response.status_code == 200:
            main_info = data['main']
            weather_info = data['weather'][0]

            temperature = main_info['temp']
            description = weather_info['description']

            return f'The temperature in {city} is {temperature}°C with {description}.'

        else:
            return f'Error: {data["message"]}'

    except Exception as e:
        return f'Error: {str(e)}'
def get_news(api_key):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {'apiKey': api_key, 'country': 'in'}
    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            articles = data['articles']
            for article in articles[:5]:  
                title = article['title']
                speak(title)
                print(title)

        else:
            speak(f"Error: {data['message']}")

    except Exception as e:
        speak(f"Error: {str(e)}")
def get_daily_quote(api_key):
    url = 'https://quotes.rest/qod'
    params = {'category': 'inspire', 'api_key': api_key}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            quote_contents = data['contents']['quotes'][0]
            quote_text = quote_contents['quote']
            quote_author = quote_contents['author']

            speak(f"Here is today's inspirational quote: {quote_text} by {quote_author}")
            print(f"Today's Quote: {quote_text} by {quote_author}")

        else:
            speak(f"Error: {data['error']['message']}")

    except Exception as e:
        speak(f"Error: {str(e)}")
def convert_currency(api_key, from_currency, to_currency, amount):
    url = 'https://v6.exchangeratesapi.io/latest'
    params = {'base': from_currency, 'symbols': to_currency}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            rate = data['rates'][to_currency]
            converted_amount = amount * rate

            speak(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

        else:
            speak(f"Error: {data['error']['info']}")

    except Exception as e:
        speak(f"Error: {str(e)}")

if __name__ == "__main__":
    news_api_key = 'f7ad0343c21b42aa9d034e0d96c64150'
    quote_api_key = 'FXb853P3bLcQajPOVAtCd8SKNwGzzNySf0c0UIL3'
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedi","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            music = 'C:\\Songs'
            songs = os.listdir(music)
            print(songs)
            ran = random.randint(0, 1)
            print(ran)
            os.startfile(os.path.join(music, songs[ran]))
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'quit' in query:
            speak("Thankyou Sir! See you soon")
            exit()
        elif 'weather' in query:
            speak("Which city's weather do you want to know?")
            city = takeCommand()
            weather_info = get_weather('c8f255873a7cf0fd4a40549d9e239a20', city)
            print(weather_info)
            speak(weather_info)
        elif 'news update' in query or 'read news' in query:
            speak("Here are the latest news headlines.")
            get_news(news_api_key)
        
        elif 'quote of the day' in query or 'daily quote' in query:
            speak("Here is today's quote of the day.")
            get_daily_quote(quote_api_key)

            
        
           
            
     
    