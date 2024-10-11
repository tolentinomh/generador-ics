import streamlit as st
from ics import Calendar, Event
from datetime import datetime
from zoneinfo import ZoneInfo
import io

def create_ics_file(title, description, start_datetime, end_datetime, location):
    # Create a calendar
    c = Calendar()

    # Create an event
    e = Event()
    e.name = title
    e.begin = start_datetime
    e.end = end_datetime
    e.description = description
    e.location = location

    # Add the event to the calendar
    c.events.add(e)

    # Set calendar properties
    c.creator = "Streamlit ICS Generator"
    c.method = "PUBLISH"

    # Serialize the calendar
    return c.serialize()

st.title("Generador de ficheros ICS")

# Input fields
title = st.text_input("Event Title", "Mago pintuchiando")
description = st.text_area("Event Description", "lorem")
location = st.text_input("Event Location", "zamora")
start_date = st.date_input("Start Date")
start_time = st.time_input("Start Time")
end_date = st.date_input("End Date")
end_time = st.time_input("End Time")

if st.button("Generar archivo ICS"):
    # Combine date and time
    start_datetime = datetime.combine(start_date, start_time, tzinfo=ZoneInfo("Europe/Berlin"))
    end_datetime = datetime.combine(end_date, end_time, tzinfo=ZoneInfo("Europe/Berlin"))

    # Generate ICS content
    ics_content = create_ics_file(title, description, start_datetime, end_datetime, location)

    # Create a download button
    st.download_button(
        label="Descargar Archivo ICS",
        data=ics_content,
        file_name="event.ics",
        mime="text/calendar"
    )

st.info("Despues de generar el archivo ICS, haz clic en 'Descargar archivo ICS' para guardarlo.")
