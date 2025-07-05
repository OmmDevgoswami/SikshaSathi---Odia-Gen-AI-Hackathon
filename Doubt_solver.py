import streamlit as st
import random
from datetime import datetime, timedelta

# Initialize session state keys
if "show_dialog" not in st.session_state:
    st.session_state.show_dialog = False
if "booking_info" not in st.session_state:
    st.session_state.booking_info = None
if "mentor_slots" not in st.session_state:
    st.session_state.mentor_slots = {}

# Dialog always defined ONCE
@st.dialog("📅 Book Session")
def booking_dialog():
    booking = st.session_state.booking_info
    if booking:
        mentor = booking["mentor"]
        time = booking["time"]
        st.write(f"You're about to book a session with **{mentor}** at **{time}**.")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        if st.button("✅ Confirm Booking"):
            st.session_state.booking = {
                "mentor": mentor,
                "time": time,
                "name": name,
                "email": email
            }
            st.success("Booking Confirmed!")
            st.balloons()
            st.session_state.show_dialog = False
            st.session_state.booking_info = None
            st.rerun()

# Show dialog if flag is set, then immediately reset the flag to avoid auto-trigger
if st.session_state.show_dialog:
    booking_dialog()
    st.session_state.show_dialog = False  # Reset immediately ✅

def mentor_slot(special_mentor, _):
    with st.expander(f"📘 Meet {special_mentor}"):
        st.write(f"Subject: Random Subject")

        if special_mentor not in st.session_state.mentor_slots:
            start_time = datetime.strptime("09:00", "%H:%M")
            slots = [start_time + timedelta(minutes=30 * i) for i in range(4, 12)]
            st.session_state.mentor_slots[special_mentor] = random.sample(slots, k=3)

        time_slots = st.session_state.mentor_slots[special_mentor]

        time_cols = st.columns(3)
        for i, t in enumerate(sorted(time_slots)):
            time_label = t.strftime("%I:%M %p")
            with time_cols[i]:
                if st.button(time_label, key=f"{special_mentor}_{time_label}"):
                    st.session_state.booking_info = {"mentor": special_mentor, "time": time_label}
                    st.session_state.show_dialog = True
                    st.rerun()

# Sample mentors to trigger
mentor_slot("Dharmeshwar Mehta", 0)
mentor_slot("Shalini Kapur", 1)



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

        start_time = datetime.strptime("09:00", "%H:%M")
        slots = [start_time + timedelta(minutes=30 * i) for i in range(4, 12)]  
        time_slots = random.sample(slots, k=3)  

        time_cols = st.columns(3)
        for i, t in enumerate(sorted(time_slots)):
            time_label = t.strftime("%I:%M %p")
            with time_cols[i]:
                if st.button(time_label, key=f"{special_mentor}_{time_label}"):
                    st.session_state.booking_info = {"mentor": f"{special_mentor}", "time": f"{time_label}"}
                    booking_dialog()      