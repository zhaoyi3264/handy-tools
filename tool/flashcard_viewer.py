import random

import pandas as pd
import streamlit as st

def flashcard_viewer():
    @st.cache
    def load_data(url):
        return pd.read_excel(url, sheet_name=None)

    url = st.sidebar.text_input('URL', 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS7ZESZs8Hm9rvGsTmO9E8ubztE8n0Ht44n6UQz91RSkAynBjQbgo-rWjahWn9qTdLPk9JcisrDxhIv/pub?output=xlsx')

    sheets = load_data(url)

    sheet_name = st.sidebar.selectbox('Sheet', sheets.keys())

    def find_col(columns, name):
        intersection = set(columns) & set(name)
        return list(columns).index(intersection.pop()) if len(intersection) else 0

    sheet = sheets[sheet_name]
    columns = sheet.columns.to_list()
    columns_with_none = [None] + columns
    term = st.sidebar.selectbox('Term', columns, find_col(columns, ['Name']))
    definition = st.sidebar.selectbox('Definition', columns, find_col(columns, ['Algorithm']))
    image_url = st.sidebar.selectbox('Image URL (Optional)', columns_with_none, find_col(columns_with_none, ['Image URL']))

    state = st.session_state

    if ('index' not in state) or (state['index'] >= len(sheet)):
        state['index'] = random.randint(0, len(sheet)-1)

    if 'show' not in state:
        state['show'] = False

    st.title('Flashcard Viewer')

    if st.button('Next'):
        state['index'] = random.randint(0, len(sheet)-1)
        state['show'] = False

    row = sheet.iloc[state['index']]

    st.markdown(f'{term.capitalize()}: {row[term]}')
    if image_url:
        st.image(row[image_url], width=200)

    if st.button('Show Definition'):
        state['show'] = not state['show']
        if state['show']:
            st.markdown(f'{definition.capitalize()}: {row[definition]}')
