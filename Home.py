import streamlit as st
from cards import roadmap_card, doubt_clearing_card, mock_test_card, one_on_one_card

st.set_page_config(page_title="SikshaSathi", layout="wide")
st.markdown("""
<div style='text-align: center;'>
    <img src="https://ik.imagekit.io/o0nppkxow/73c93ce6-c422-4ae5-a93f-b172563faf46.png?updatedAt=1751602343395" alt="SikshaSathi Banner" width = "500" />
    <h1 style='text-align: center;'> SikshaSathi - ଶିକ୍ଷାସାଥୀ </h1>
    <h3 style='color: gray;'> From Boards to Big Dreams — SikshaSathi Stands By You!! </h3>
    <br />
    <div style='margin-top: 10px;'>
        <a href='https://github.com/OmmDevgoswami/SikshaSathi---Odia-Gen-AI-Hackathon' target='_blank' style='text-decoration: none; margin: 0 10px;'>🔗 SikshaSathi GitHub</a>
        <p style='color: gray;'> Built using Python - Streamlit, Educhain LLM and Sutra-multilingual model </p>
    </div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(2)
with cols[0].container(height = 380):
    roadmap_card()
with cols[1].container(height = 380):
    doubt_clearing_card()
with cols[0].container(height = 380):
    mock_test_card()
with cols[1].container(height = 380):
    one_on_one_card()