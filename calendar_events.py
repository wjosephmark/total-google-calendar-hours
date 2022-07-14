import os
import requests
from dotenv import load_dotenv, find_dotenv
import datetime

load_dotenv(find_dotenv())

api_key = os.getenv('API_KEY')
calendar_id = os.getenv('CALENDAR_ID')


def get_calendar_events():
    calenders_api_response = requests.get(f'https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events?key={api_key}')

    return calenders_api_response.json()

def sort_calendar_events(events_dict):
    relevant_events = []
    total_hours_dict = {}
    response_array = []
    for event in events_dict:
        # IF EVENT HAS TITLE
        if 'summary' in event:
            if 'Test' in event['summary']:
                relevant_events.append(event)

    for event in relevant_events:
        summary = event['summary']

        # SET UTC TIMESTAMPS TO VARIABLES
        start_timestamp = event['start']['dateTime']
        end_timestamp= event['end']['dateTime']

        # CONVERT UTC TIMESTAMP TO DATETIME STRING
        start_datetime = datetime.datetime.strptime(start_timestamp, '%Y-%m-%dT%H:%M:%S%z')
        end_datetime = datetime.datetime.strptime(end_timestamp, '%Y-%m-%dT%H:%M:%S%z')

        # EXTRACT HOURS AND MINUTES FROM DATETIME STRINGS
        start_hour = start_datetime.hour
        end_hour = end_datetime.hour
        start_minute = start_datetime.minute
        end_minute = end_datetime.minute

        # FIND DIFFERENCE IN HOURS AND MINUTES
        hour_diff = end_hour-start_hour
        minute_diff = end_minute-start_minute

        if summary not in total_hours_dict:
            formatted_dict = {'summary': summary, 'hours': hour_diff, 'minutes': minute_diff}
            total_hours_dict[summary] = formatted_dict
        else:
            total_hours_dict[summary]['hours'] = total_hours_dict[summary]['hours'] + hour_diff
            total_hours_dict[summary]['minutes'] = total_hours_dict[summary]['minutes'] + minute_diff

    for client in total_hours_dict:
        client_info = total_hours_dict[client]
        #TODO: ADD LOGIC TO DETERMINE USE CORRECT VARIATION OF MINUTES/HOURS
        response_array.append(f"{client_info['summary']} owes for {client_info['hours']} hours and {client_info['minutes']} minutes")

    return response_array

def main():
    reponse_dict = get_calendar_events()
    events_dict = reponse_dict['items']
    client_hours_array = sort_calendar_events(events_dict)

if __name__ == '__main__':
    main()
