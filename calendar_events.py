import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key = os.getenv('API_KEY')
calendar_id = os.getenv('CALENDAR_ID')


def get_calendar_events():
    calenders_api_response = requests.get(f'https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events?key={api_key}')

    return calenders_api_response.json()

def sort_calendar_events(events_dict):
    relevant_events = []
    client_info_dict = {}

    for event in events_dict:
        # IF EVENT HAS TITLE
        if 'summary' in event:
            if 'Test' in event['summary']:
                relevant_events.append(event)

    for event in relevant_events:
        summary = event['summary']
        if summary not in client_info_dict.keys():
            client_info_dict[summary] = 1
        else:
            client_info_dict[summary] += 1

    print(client_info_dict)


def main():
    reponse_dict = get_calendar_events()
    events_dict = reponse_dict['items']
    sort_calendar_events(events_dict)

if __name__ == '__main__':
    main()
