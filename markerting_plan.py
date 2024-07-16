import streamlit as st
import os
from crewai import Crew, Process, Agent, Task
from langchain_core.callbacks import BaseCallbackHandler
from typing import TYPE_CHECKING, Any, Dict, Optional
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool
from streamlit_option_menu import option_menu

tool = SerperDevTool()

# Page Configuration
st.set_page_config(page_title="Zyper.ai", page_icon="💬", layout="wide")

# Title and Description
st.title("💬 Zyper.ai")
st.markdown("### Delivering Superior Generative AI Marketing Services To Small Businesses Worldwide")

# Sidebar for Navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "About", "Contact"],
        icons=["house", "info-circle", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    # Initialize the tool for internet searching capabilities
    tool = SerperDevTool()

    os.environ["GROQ_API_KEY"] = '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'
    llm = ChatGroq(temperature=0.2, model_name="llama3-70b-8192")

    avators = {
        "Writer": "https://cdn-icons-png.flaticon.com/512/320/320336.png",
        "Reviewer": "https://cdn-icons-png.freepik.com/512/9408/9408201.png"
    }

    industry_researcher = Agent(
        name="Industry Researcher",
        role="Research",
        goal="Provide comprehensive research on the specific industry of the client",
        backstory=f"Designed to gather up-to-date and relevant information to help tailor the marketing strategy to industry trends and benchmarks",
        verbose=True,
        llm=llm,
        allow_delegation=True,
        tools=[tool],
        max_iter = 7,
        max_rpm = 4000
    )


    # Define the Marketing Roadmap Agent
    roadmap_creator = Agent(
        name="Roadmap Creator",
        role="Marketing",
        goal="Develop a detailed and actionable marketing roadmap based on the client's industry, size, budget, and team capacity",
        backstory="An expert marketer with extensive knowledge in crafting strategies that align with business goals and market dynamics",
        verbose=True,
        llm=llm,
        allow_delegation=False,
        tools=[],
        max_iter=7,
        max_rpm=4000

    )

    st.markdown("#### Interactive Chat")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "What are you planning to build?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    st.markdown("### Enter Business Details")

    # Get additional inputs from the user
    business_goals = st.multiselect(
        "Select your business goals:",
        ["Lead Generation", "Website Traffic", "App Downloads", "In-store Traffic"]
    )

    competitors = st.text_input("Enter the names of your competitors:")

    keywords = st.text_input("Enter keywords to understand customer persona and business:")

    marketing_budget = st.number_input("Enter your marketing budget ($):", min_value=0)

    location = st.text_input("Enter your business location:")

    if st.button("Submit Details"):
        st.session_state["details"] = {
            "business_goals": business_goals,
            "competitors": competitors,
            "keywords": keywords,
            "marketing_budget": marketing_budget,
            "location": location
        }

        st.markdown("### Details Submitted")
        st.write(st.session_state["details"])

    if "details" in st.session_state:
        prompt = st.text_area("Enter your business overview:")

        if st.button("Submit Overview"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            # Define the tasks
            gather_industry_insights = Task(
                description=f"Collect detailed information about the specific {prompt} industry, including current trends, benchmarks,competitor research on {competitors} and best practices specific for the location - {location} by using the following {keywords}.",
                agent=industry_researcher,
                expected_output="""
                    "industry_trends": "A report on current industry trends",
                    "benchmarks": "Benchmark data for the industry",
                    "best_practices": "List of best practices relevant to the industry"
                """
            )

            develop_marketing_strategy = Task(
                description=f"Use the gathered insights to create a comprehensive marketing strategy for {prompt} based on the business goals of -  {business_goals},and provided marketing budget of {marketing_budget}. Make the business plan relevant to the location - {location} provided.",
                agent=roadmap_creator,
                expected_output=
                """
                    "marketing_goals": "A list of measurable and time-bound marketing goals",
                    "initiatives": "Detailed description of marketing initiatives",
                    "schedule": "Chronological schedule of marketing activities",
                    "activities": "List of marketing activities",
                    "status_tracking": "Method for tracking the status of goals, initiatives, and activities"
                """
            )
            crew = Crew(
                agents=[industry_researcher, roadmap_creator],
                tasks=[gather_industry_insights, develop_marketing_strategy],
                process=Process.sequential,
            )
            final = crew.kickoff()

            result = f"## Here is the Final Result \n\n {final}"

            # Display result in beautiful format
            st.markdown("## Analysis Result")
            st.write(result)

elif selected == "About":
    st.markdown("### About Zyper.ai")
    st.write("Zyper.ai is an AI-first digital marketing agency that provides superior generative AI-based marketing solutions. Our mission is to deliver comprehensive and customized marketing strategies that align with your business goals.")

elif selected == "Contact":
    st.markdown("### Contact Us")
    st.write("For any inquiries, please reach out to us at: support@zyper.ai")

# Footer
st.markdown("---")
st.markdown("© 2024 Zyper.ai. All rights reserved.")