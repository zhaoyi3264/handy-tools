import streamlit as st

def color_picker():
    st.color_picker('Pick a Color', key='color')
    def on_rgb_change():
        s = '#'
        for c in 'RGB':
            h = hex(int(st.session_state[c]))
            s += h[2:].rjust(2, '0')
        st.session_state['color'] = s
    cols = st.columns(3)
    for i, (col, c) in enumerate(zip(cols, 'RGB')):
        color = st.session_state['color'][1:]
        h = int(color[i*2:i*2+2], 16)
        with col:
            st.slider(c, 0, 255, h, 1, key=c, on_change=on_rgb_change)
    st.text(f'RGB: {st.session_state.R},{st.session_state.G},{st.session_state.B}')
    st.text(f'Hex: {st.session_state.color}')
