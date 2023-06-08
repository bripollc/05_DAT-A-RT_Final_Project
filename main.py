import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title = "Dat(A)rt", page_icon = ":sunglasses:")

st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>DAT(A)RT 🎨</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='font-size: 1.2rem; text-align: center; margin-top: 0; margin-bottom: 1.5rem;'>
        <div style='font-size: 1.5rem; font-weight: bold;'>Can technology be used to explore art by the way it makes us feel?</div>
    </div>
    """,
    unsafe_allow_html=True
)


video_path = "video/video_demo.mov"
st.video(video_path)
