

def test_read_main(client):
    response = client.get("/next/6?ics_url=https://github.com/niccokunzmann/fast-api-get-next-ics-events/raw/main/test/calendars/endless-recurring-event.ics")
    assert response.status_code == 200
    events = response.json()["events"]
    assert len(events) == 6
    for event in events:
        assert event["summary"] == "A recurring event!"
