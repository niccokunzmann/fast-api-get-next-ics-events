#/usr/bin/python3
from fastapi import FastAPI
import recurring_ical_events
import icalendar
import requests


app = FastAPI()

@app.get("/next/{event_count}")
async def root(ics_url : str):
    return {"message": "Hello World"}
