from datetime import date, datetime, time
from enum import Enum, auto

from dateutil.relativedelta import relativedelta
import streamlit as st

MAX_INT = 1 << 53 - 1
DATE_FIELDS = ['years', 'months', 'days']
DATE_DELTA_FIELDS = ['years', 'months', 'weeks', 'days']
TIME_FIELDS = ['hours', 'minutes', 'seconds']

class Mode(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()
    
    SPAN = auto()
    OFFSET = auto()

class Op(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()
    
    ADD = auto()
    SUBTRACT = auto()

def date_time_calculator():
    mode = st.selectbox('Mode', [e.value for e in list(Mode)])
    col1, col2 = st.columns(2)
    with col1:
        include_date = st.checkbox('Date', value=True)
    with col2:
        include_time = st.checkbox('Time')
    def layout_input(date_input, time_input):
        if include_date and include_time:
            with col1:
                date_input()
            with col2:
                time_input()
        elif include_date:
            date_input()
        elif include_time:
            time_input()
    
    if mode == Mode.SPAN.value:
        def date_input():
            st.date_input('Start Date', key='start_date')
            st.date_input('End Date', key='end_date')
        def time_input():
            st.time_input('Start Time', key='start_time')
            st.time_input('End Time', key='end_time')
        layout_input(date_input, time_input)
        
        start_date = st.session_state.get('start_date', date.min)
        end = st.session_state.get('end_date', date.min)
        start_time = st.session_state.get('start_time', time.min)
        end_time = st.session_state.get('end_time', time.min)

        start = datetime.combine(start_date, start_time)
        end = datetime.combine(end, end_time)
        diff = relativedelta(end, start)
        diff_str = 'Difference: '
        def format_relativedelta(fields):
            s = ''
            for field in fields:
                s += f'{getattr(diff, field)} {field.title()} '
            return s
        if include_date:
            diff_str += format_relativedelta(DATE_FIELDS)
        if include_time:
            diff_str += format_relativedelta(TIME_FIELDS)
        st.text(diff_str)
    elif mode == Mode.OFFSET.value:
        def date_input():
            st.date_input('Date', key='date')
        def time_input():
            st.time_input('Time', key='time')
        layout_input(date_input, time_input)

        op = st.selectbox('Add/Subtract', [e.value for e in list(Op)])
        def add_input(fields):
            cols = st.columns(len(fields))
            for col, field in zip(cols, fields):
                with col:
                    st.number_input(field.title(), 0, MAX_INT, 0, 1, key=field)
        if include_date:
            add_input(DATE_DELTA_FIELDS)
        if include_time:
            add_input(TIME_FIELDS)
        
        start_date = st.session_state.get('date', date.min)
        start_time = st.session_state.get('time', time.min)
        start = datetime.combine(start_date, start_time)
        fields = dict.fromkeys(DATE_DELTA_FIELDS + TIME_FIELDS)
        for k in fields:
            fields[k] = st.session_state.get(k, 0)
        delta = relativedelta(**fields)
        
        if op == Op.SUBTRACT.value:
            delta *= -1
        end = start + delta
        format = ''
        if include_date:
            format += '%Y-%m-%d '
        if include_time:
            format += '%H:%M:%S'
        st.text(end.strftime(format))
