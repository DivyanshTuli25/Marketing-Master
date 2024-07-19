import streamlit as st
from streamlit_option_menu import option_menu
import subprocess


# Define functions to run each file
def run_file1():
    subprocess.run(["streamlit", "run", "lead_gen.py"])


def run_file2():
    subprocess.run(["streamlit", "run", "insta_content.py"])


def run_file3():
    subprocess.run(["streamlit", "run", "marketing_plan.py"])


# Streamlit UI
st.set_page_config(page_title="Crew AI Dashboard", page_icon=":robot_face:", layout="wide")

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "About", "Contact Us", "Run Lead Gen", "Run Insta Content", "Marketing Roadmap"],
        icons=["house", "info", "envelope", "play", "play", "play"],
        menu_icon="cast",
        default_index=0,
    )

# Home page
if selected == "Home":
    st.title("Welcome to Crew AI Dashboard")
    st.write("Select one of the options from the sidebar to run the corresponding module or to learn more about us.")

# About page
elif selected == "About":
    st.title("About Crew AI")
    st.write("""
        Crew AI is a platform designed to provide AI-powered solutions for your business needs.
        We offer various modules to assist with lead generation, social media content creation, and more.
        Our goal is to streamline your workflow and enhance productivity using advanced AI technologies.
    """)

# Contact Us page
elif selected == "Contact Us":
    st.title("Contact Us")
    st.write("""
        We'd love to hear from you! Feel free to reach out to us with any questions or feedback.

        **Email:** reway.ewm@gmail.com
        **Phone:** +91 7290908877 || +91 9899115560  """)


# Run Lead Gen
elif selected == "Run Lead Gen":
    st.title("Run Lead Gen Module")
    run_file1()
    st.write("Lead Gen module is running...")

# Run Insta Content
elif selected == "Run Insta Content":
    st.title("Run Instagram Content Module")
    run_file2()
    st.write("Instagram Content module is running...")

# Run File 3
elif selected == "Run File 3":
    st.title("Run File 3 Module")
    run_file3()
    st.write("Marketing Roadmap Creator is running...")

