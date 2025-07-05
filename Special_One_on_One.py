import streamlit as st
import random 
from datetime import datetime, timedelta

def mentor_slot(special_mentor, _):
    with st.expander(f"📘 Meet {special_mentor}"):
        st.markdown(f"""
        <div class='mentor-card'>
            <img src='{mentor_dict[special_mentor]}' alt='mentor face' width='150' />
            <h3>{special_mentor}</h3>
            <h4>Subject: {random.choice(subjects)}</h4>
            <h4>Level: Expert — {random.choice(Levels)}</h4>
            <p>“Helping you crack concepts, one formula at a time!”</p>
        </div>
        """, unsafe_allow_html=True)

        # Generate slots only once per mentor
        if special_mentor not in st.session_state.mentor_slots:
            start_time = datetime.strptime("09:00", "%H:%M")
            slots = [start_time + timedelta(minutes=30 * i) for i in range(4, 12)]
            st.session_state.mentor_slots[special_mentor] = random.sample(slots, k=3)

        time_slots = st.session_state.mentor_slots[special_mentor]
        time_labels = [t.strftime("%I:%M %p") for t in sorted(time_slots)]

        # Selectbox instead of multiple buttons
        selected_time = st.selectbox(f"Available Slots with {special_mentor}:", ["Select a Time"] + time_labels, key=f"slot_{special_mentor}")

        if selected_time != "Select a Time":
            if st.button("📅 Book This Slot", key=f"book_{special_mentor}"):
                st.session_state.booking_info = {"mentor": special_mentor, "time": selected_time}
                st.session_state.show_dialog = True
                st.rerun()
                               

st.markdown("""
<div style='text-align: center;'>
    <h1 style='text-align: center;'> SikshaSathi - ଶିକ୍ଷାସାଥୀ </h1>
    <br />
    <h2> GuruTalks </h2>
    <h3> From Questions to Confidence — Your Personal Mentor Awaits !! </h3>
</div>
""", unsafe_allow_html=True)

mentor_list = ["Dharmeshwar Mehta", "Shalini Kapur", "Kritivya", "Arvindesh Kumar", "Rishabh Dhanraj", "Vishwajeet Patil", "Shivanik Sharma", "Ananya Talwar", "Vedant Rane", "Sunil Rao"]

mentor_dict = {
    "Dharmeshwar Mehta" : "https://ik.imagekit.io/o0nppkxow/Faces/per1.jpeg?updatedAt=1751628636578" ,
    "Shalini Kapur" : "https://ik.imagekit.io/o0nppkxow/Faces/per2.jpeg?updatedAt=1751628636578",
    "Kritivya" : "https://ik.imagekit.io/o0nppkxow/Faces/per3.jpeg?updatedAt=1751628636578",
    "Arvindesh Kumar" : "https://ik.imagekit.io/o0nppkxow/Faces/per4.jpeg?updatedAt=1751628636578",
    "Rishabh Dhanraj" : "https://ik.imagekit.io/o0nppkxow/Faces/per5.jpeg?updatedAt=1751628636578",
    "Vishwajeet Patil" : "https://ik.imagekit.io/o0nppkxow/Faces/per6.jpeg?updatedAt=1751628636578",
    "Shivanik Sharma" : "https://ik.imagekit.io/o0nppkxow/Faces/per7.jpeg?updatedAt=1751628636578",
    "Ananya Talwar" : "https://ik.imagekit.io/o0nppkxow/Faces/per8.jpeg?updatedAt=1751628636578",
    "Vedant Rane" : "https://ik.imagekit.io/o0nppkxow/Faces/per9.jpeg?updatedAt=1751628636578",
    "Sunil Rao" : "https://ik.imagekit.io/o0nppkxow/Faces/per10.jpeg?updatedAt=1751628636578",
}

card_style = """
    <style>
    .mentor-card {
        background-color: #f9f9f9;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        width: 300px;
        margin: 0 auto;
    }
    .mentor-card img {
        border-radius: 50%;
        margin-bottom: 15px;
    }
    .mentor-card h3 {
        margin: 10px 0 5px 0;
        color: #4B0082;
    }
    .mentor-card h4 {
        margin: 5px 0;
        color: #555;
    }
    .mentor-card p {
        margin: 8px 0;
        color: #999;
    }
    </style>
"""

st.markdown(card_style, unsafe_allow_html=True)

exam_choice = st.selectbox("Choose your target exam that you wish to Crack !!",
    ("JEE", "NEET", "UPSC"),
    index = None,
    placeholder = "Entrance Preparation..."    
)

if exam_choice == "JEE":
    subjects = ["Mathematics", "Physics", "Chemistry"]
    Levels = ["Olympiad Medalist (Math/Physics/CS)", "IIT Gold Medalist", "KVPY Scholar", "IIM Graduate", "MIT Research Fellow", "Harvard Certified Educator", "ISRO Scientist — Space & Physics Coach", "IT Gold Medalist & JEE Expert"]
    stored = []
    teachers = random.randint(2, 7)
    cols = st.columns(teachers//2)
    
    for _ in range(0 , teachers//2):
        with cols[_]:
            special_mentor = random.choice(mentor_list)
            if special_mentor not in stored:
                stored.append(special_mentor)
                mentor_slot(special_mentor, _)
                
elif exam_choice == "NEET":
    subjects = ["Biology", "Physics", "Chemistry"]
    Levels = ["Olympiad Medalist (Math/Physics/CS)", "KVPY Scholar", "MIT Research Fellow", "Harvard Certified Educator", "ISRO Scientist — Space & Physics Coach", "NEET Top Ranker", "Cambridge Fellow", "Stanford Graduate"]
    stored = []
    teachers = random.randint(2, 7)
    cols = st.columns(teachers//2)
    
    for _ in range(0 , teachers//2):
        with cols[_]:
            special_mentor = random.choice(mentor_list)
            if special_mentor not in stored:
                stored.append(special_mentor)
                mentor_slot(special_mentor, _)
                
elif exam_choice == "UPSC":
    subjects = ["General Knowledge", "History", "Poltics", "Current Affairs", "Reasoning", "Apptitude"]
    Levels = ["KVPY Scholar", "MIT Research Fellow", "Master Trainer", "Subject Matter Expert (SME)" , "Certified Life Coach"]
    stored = []
    teachers = random.randint(2, 7)
    cols = st.columns(teachers//2)
    
    for _ in range(0 , teachers//2):
        with cols[_]:
            special_mentor = random.choice(mentor_list)
            if special_mentor not in stored:
                stored.append(special_mentor)
                mentor_slot(special_mentor, _)
