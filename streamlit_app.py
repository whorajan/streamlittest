import streamlit as st

st.title('Hello World')
image = st.camera_input('This is a camera input');
st.balloons()
container = st.container()
if image:
    container.image(image)