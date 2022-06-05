from datetime import date, datetime, time
from enum import Enum, auto

import streamlit as st

MAX_INT = 1 << 53 - 1

class Mode(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()
    
    SPAN = auto()
    OFFSET = auto()

def date_time_calculator():
    mode = st.selectbox('Mode', [e.value for e in list(Mode)])
    col1, col2 = st.columns(2)
    with col1:
        include_date = st.checkbox('Date', value=True)
    with col2:
        include_time = st.checkbox('Time')
    if mode == Mode.SPAN.value:
        def date_input():
            st.date_input('Start Date', key='start_date')
            st.date_input('End Date', key='end_date')
        def time_input():
            st.time_input('Start Time', key='start_time')
            st.time_input('End Time', key='end_time')
        if include_date and include_time:
            with col1:
                date_input()
            with col2:
                time_input()
        elif include_date:
            date_input()
        elif include_time:
            time_input()
    elif mode == Mode.OFFSET.value:
        def date_input():
            st.date_input('Date', key='date')
        def time_input():
            st.time_input('Time', key='time')
        if include_date and include_time:
            with col1:
                date_input()
            with col2:
                time_input()
        elif include_date:
            date_input()
        elif include_time:
            time_input()
        op = st.selectbox('Add/Subtract', ['Add', 'Subtract'])
        col1, col2, col3 = st.columns(3)
        with col1:
            if include_date:
                st.number_input('Years', 0, MAX_INT, 0, 1, key='years')
            if include_time:
                st.number_input('Hours', 0, MAX_INT, 0, 1, key='hours')
        with col2:
            if include_date:
                months = st.number_input('Months', 0, MAX_INT, 0, 1)
            if include_time:
                st.number_input('Minutes', 0, MAX_INT, 0, 1, key='minutes')
        with col3:
            if include_date:
                days = st.number_input('Days', 0, MAX_INT, 0, 1)
            if include_time:
                st.number_input('Seconds', 0, MAX_INT, 0, 1, key='seconds')
