import re

import streamlit as st

WS = r'\s+'

def word_counter():
    if 'chars' not in st.session_state:
        st.session_state['chars'] = 0
        st.session_state['words'] = 0
        st.session_state['lines'] = 0
    def on_change():
        text = st.session_state.get('text', '').strip()
        chars = len(text)
        st.session_state['chars'] = chars
        st.session_state['words'] = len(re.split(WS, text)) if chars else 0
        st.session_state['lines'] = len(text.splitlines())
    st.text_area('Text', height=300, on_change=on_change, key='text')
    st.text(f'Characters: {st.session_state.chars}')
    st.text(f'Words: {st.session_state.words}')
    st.text(f'Lines: {st.session_state.lines}')
