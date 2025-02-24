import streamlit as st

st.title('Hello World')
st.caption('This is a caption')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a text')
st.markdown('This is a markdown')
image = st.camera_input('This is a camera input');
st.balloons()
st.error('This is an error')
st.warning('This is a warning')
st.info('This is an info')
st.success('This is a success')
st.exception('This is an exception')
st.write('This is a write')
container = st.container()
if image:
    container.image(image)