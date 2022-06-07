import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key = os.getenv('API_KEY')
calendar_id = os.getenv('CALENDAR_ID')

def main():
    calnders_api_response = requests.get(f'https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events?key={api_key}')

    events_dictionary = calnders_api_response.text


if __name__ = '__main__':
    main()