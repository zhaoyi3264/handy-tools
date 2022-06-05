import importlib

import streamlit as st

from tool import TOOLS

format_func = lambda name: name.replace('_', ' ').title()
tool_name = st.sidebar.radio('Tool', TOOLS, format_func=format_func)
st.title(format_func(tool_name))

try:
    mod = importlib.import_module(f'tool.{tool_name}')
    tool_func = getattr(mod, tool_name)
    tool_func()
except Exception as ex:
    st.warning(ex)
