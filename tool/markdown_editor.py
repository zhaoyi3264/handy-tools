import streamlit as st

def markdown_editor():
    col1, col2 = st.columns(2)
    with col1:
        st.text_area('Raw', height=300, key='text')
    with col2:
        st.text('Markdown')
        st.markdown(st.session_state['text'])
    st.download_button('Download raw', st.session_state['text'], 'markdown.md')
    st.caption('Basic Syntax: https://www.markdownguide.org/basic-syntax/')
