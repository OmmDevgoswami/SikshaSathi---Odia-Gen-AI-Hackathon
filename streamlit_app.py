import streamlit as st
from cards import roadmap_card, doubt_clearing_card, mock_test_card, one_on_one_card

pages = [
    st.Page(
        "Home.py",
        title="Home",
        icon=":material/home:"
    ),
    st.Page(
        "Roadmap.py",
        title="Roadmap Generator",
        icon=":material/view_timeline:"
    ),
    st.Page(
        "Doubt_solver.py",
        title="Doubt Solver",
        icon=":material/indeterminate_question_box:"
    ),
    st.Page(
        "Mock_test.py",
        title="Mock Test Preparation",
        icon=":material/assignment:"
    ),
    st.Page(
        "Special_One_on_One.py",
        title="Special One-on-One",
        icon=":material/person_raised_hand:"
    )
]

page = st.navigation(pages)
page.run()

with st.sidebar.container(height = 380):
    if page.title == "Roadmap Generator":
        roadmap_card()
    elif page.title == "Doubt Solver":
        doubt_clearing_card()
    elif page.title == "Mock Test Preparation":
        mock_test_card()
    elif page.title == "Special One-on-One":
        one_on_one_card()
    else:
        st.page_link("Home.py", label="Home", icon=":material/home:")
        st.write("Welcome to the SikshaSathi - ଶିକ୍ଷାସାଥୀ!")
        st.markdown("""
        <div style='text-align: center;'>
                <img src="https://ik.imagekit.io/o0nppkxow/73c93ce6-c422-4ae5-a93f-b172563faf46.png?updatedAt=1751602343395" alt="SikshaSathi Banner" width = "200" />
                <h3 style='color: gray;'> From Boards to Big Dreams — SikshaSathi Stands By You!! </h3>
                <br />
                <p style='color: gray;' > Built using Python - Streamlit, Educhain LLM and Sutra-multilingual model </p>
        </div>
        """, unsafe_allow_html=True)

st.caption("Built with passion by Team Asterix 🐦‍🔥🌠")