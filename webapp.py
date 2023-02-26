import backend
import streamlit as st

items = backend.getItems()

def change():
    if 'newItem' not in st.session_state:
        st.write('Nobody Home, dawg')
    else:
        line = st.session_state['newItem']
        st.write(line)
        st.write(type(line))
        st.write(type(items))
        items.append(line)
        backend.writeItems(items)


st.title("Web App Title")
st.subheader("Subheader")
st.write("Checkboxes:")

for index, item in enumerate(items):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        items.pop(index)
        print(items)
        backend.writeItems(items)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="Label", placeholder="Placeholder value",
              key='newItem', on_change=change)
