Voice Assistant README

Project Description: 

This Python-based Voice Assistant utilizes various APIs and libraries to perform a range of tasks through voice commands. Users can interact with the assistant to retrieve Wikipedia information, browse the web, play music, check the weather, read news headlines, receive daily inspirational quotes, perform currency conversions, and get the current time. The assistant relies on speech recognition to understand user commands and respond accordingly.

**Dependencies: **
- Python 3.x
- pyttsx3
- datetime
- wikipedia
- webbrowser
- os
- random
- requests
- time
- speech_recognition

Setup:
1. Install Python 3.x on your system if not already installed.
2. Install the required dependencies using pip:
     pip install pyttsx3 wikipedia requests speech_recognition
3. Obtain API keys for the News API and the Quotes API. Replace the placeholders `news_api_key` and `quote_api_key` in the script with your respective API keys.
4. Run the Python script `voice_assistant.py`.

Usage: 
1. Upon running the script, the assistant will greet the user according to the time of the day.
2. The user can then give voice commands to perform various tasks supported by the assistant.
3. Supported commands include:
   - Retrieving Wikipedia information (`wikipedia` command)
   - Opening websites like YouTube, Google, Spotify, and Instagram (`open youtube`, `open google`, `open spotify`, `open instagram` commands)
   - Playing music (`play music` command)
   - Checking the current time (`the time` command)
   - Getting weather updates for a specific city (`weather` command)
   - Reading news headlines (`news update`, `read news` commands)
   - Providing daily inspirational quotes (`quote of the day`, `daily quote` commands)
   - Quitting the assistant (`quit` command)

Acknowledgements:
- This project utilizes various APIs and libraries, without which it wouldn't be possible.
- Special thanks to the developers and contributors of pyttsx3, wikipedia, requests, and speech_recognition libraries.

