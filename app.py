#/usr/bin/python3
from fastapi import FastAPI
import recurring_ical_events
from icalendar import Calendar, Event
import requests
import datetime


DEFAULT_REQUEST_HEADERS = {
  "user-agent": "open-web-calendar",
}


def get_text_from_url(url):
    """Return the text from a url."""
    return requests.get(url, headers=DEFAULT_REQUEST_HEADERS).content


def event_to_json(event : Event):
    """Turn an event into JSON."""
    return {
        "start": event["DTSTART"].to_ical().decode(),
        "summary" : event.get("SUMMARY"),
        "description" : event.get("DESCRIPTION"),
    }

app = FastAPI()

@app.get("/next/{event_count}")
async def root(event_count : int, ics_url : str):
    calendar_text = get_text_from_url(ics_url)
    calendars = Calendar.from_ical(calendar_text, multiple=True)
    first_calendar = calendars[0] # TODO add other events into calendar 0
    now = datetime.datetime.now()
    events = []
    result = {
        "events" : events
    }
    for event in recurring_ical_events.of(first_calendar).after(now):
        events.append(event_to_json(event))
        if len(events) >= event_count:
            break
    return result
