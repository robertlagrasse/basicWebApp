import backend
import streamlit as st
from PIL import Image

items = backend.getItems()
st.set_page_config(layout="centered")
# st.set_page_config(layout="wide")

def change():
    if 'newItem' not in st.session_state:
        st.write('Nobody Home, dawg')
    else:
        line = st.session_state['newItem']
        items.append(line)
        backend.writeItems(items)


st.title("Basic Web App")
st.subheader("Subheader")
st.write("Checkboxes:")

for index, item in enumerate(items):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        items.pop(index)
        backend.writeItems(items)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="Text_input box label", placeholder="Placeholder value",
              key='newItem', on_change=change)

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")