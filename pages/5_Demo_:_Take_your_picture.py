import streamlit as st


st.title("Let's try it!")
st.header("#1 Take your best selfie 📸")

img_file_buffer = st.camera_input("say cheeeese")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
    hola = str(img_file_buffer).split(",")[1].split("=")[1]

#st.write(hola)


st.header("#2 How do you feel today? 🫥")

st.slider('Positive feelings 🙂', -1.00, 1.00)
st.slider('Neutral feelings 😶', -1.00, 1.00)
st.slider('Negative feelings 🙁', -1.00, 1.00)


st.header("#3 Choose a movement or artist 👩🏻‍🎨")

if st.button("Movement"):
    st.write("hola")


if st.button("Artist"):
    st.write("dew")





select = st.radio('whats your favourite color?', options=('Movement', 'Artist'))
if select == "Movement":
    st.write("ola")
if select == "Artist":
    st.write("dew")



st.header("#4 result?")