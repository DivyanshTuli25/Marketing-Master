import streamlit as st
from streamlit_option_menu import option_menu
import subprocess
import datetime
import os
import requests
import json
from concurrent.futures import ThreadPoolExecutor
# from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
import streamlit as st
import os
# from crewai import Crew, Process, Agent, Task

from langchain_groq import ChatGroq
# from crewai_tools import SerperDevTool
from streamlit_option_menu import option_menu


# Define functions to run each file

st.set_page_config(page_title="HyperGrowth.AI", page_icon=":robot_face:", layout="wide")

# Load environment variables
load_dotenv()

# Set API keys
# os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY_2')
# os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the LLM
llm = ChatGroq(temperature=0.2, model_name="llama3-70b-8192")

class LeadSearchTools:

    @tool('search_facebook_groups')
    def search_facebook_groups(query: str) -> str:
        """Search Facebook groups. This tool returns 5 results from Facebook groups."""
        return LeadSearchTools.search(f"site:facebook.com/groups {query}", limit=5)

    @tool('search_news')
    def search_news(query: str) -> str:
        """Search news articles. This tool returns 5 results from news sources."""
        return LeadSearchTools.search(f"site:news.google.com {query}", limit=5)

    @tool('search_justdial')
    def search_justdial(query: str) -> str:
        """Search JustDial. This tool returns 5 results from JustDial."""
        return LeadSearchTools.search(f"site:justdial.com {query}", limit=10)

    @tool('search_indiamart')
    def search_indiamart(query: str) -> str:
        """Search IndiaMart. This tool returns 5 results from IndiaMart."""
        return LeadSearchTools.search(f"site:indiamart.com {query}", limit=10)

    @tool('open_page')
    def open_page(url: str) -> str:
        """Open a webpage and get the content."""
        loader = WebBaseLoader(url)
        return loader.load()

    def search(query, limit=5):
        url = "https://google.serper.dev/search"
        payload = json.dumps({
            "q": query,
            "num": limit,
        })
        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY"),
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=10)
            response.raise_for_status()
            results = response.json().get('organic', [])
            if not results:
                return "No results found."

            results_list = []
            for result in results:
                results_list.append(f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n")

            return f"Search results for '{query}':\n\n" + "\n".join(results_list)
        except requests.Timeout:
            return "The request timed out. Please try again."
        except requests.RequestException as e:
            return f"An error occurred: {str(e)}"


# Define the Lead Generation Agent
# lead_generator = Agent(
#     role='Lead Generator',
#     goal='Identify and list potential leads from various online sources relevant to the product or business. Focus on finding buyers, sellers, dealers or groups and connections where potential customers or business partners might be active.',
#     backstory=(
#         "With expertise in social and professional networks, you excel at identifying potential leads within various online sources. Your ability to find relevant buyers and partners makes you invaluable for generating business leads."
#     ),
#     tools=[
#         LeadSearchTools.search_justdial,
#         LeadSearchTools.search_indiamart,
#         LeadSearchTools.search_facebook_groups,
#         LeadSearchTools.search_news,
#         LeadSearchTools.open_page
#     ],
#     llm=llm,
#     allow_delegation=True
# )

# Define the lead generation task
# lead_generation_task = Task(
#     description="""Identify and list potential leads from various online sources relevant to the product or business. Focus on finding groups and connections where potential customers or business partners might be active.
#
#     Current date: {current_date}
#
#     Description of the product or business for which you are doing this research:
#     <BUSINESS_DESCRIPTION>{business_description}</BUSINESS_DESCRIPTION>
#
#     Find the most relevant dealers, groups and connections for generating business leads.
# """,
#     expected_output='A report with the most relevant leads that you found, including links to groups and profiles, and any other information that could be useful for the sales team.',
#     tools=[],
#     agent=lead_generator,
# )

# def execute_lead_generation_task(inputs):
    # Initialize and run the crew with the lead generation task
    # crew = Crew(
    #     agents=[lead_generator],
    #     tasks=[lead_generation_task],
    #     process=Process.sequential,
    # )
    # result = crew.kickoff(inputs=inputs)
    # return result
def run_file1():
    st.title("💬 HyperGrowth.ai")
    st.markdown("### Delivering Superior Generative AI Marketing Services To Small Businesses Worldwide")
    st.markdown("### Grow your business with HyperGrow - LeadGen")

    # st.title('Lead Generation Task Executor')

    business_description = st.text_input('Enter a description of the product or business:')
    current_date = st.date_input('Enter the current date:', datetime.date.today())

    if st.button('Execute Lead Generation Task'):
        st.write("This is HyperGrowAI agent, for Lead Generation")
        # with st.spinner('Generating strategy...'):
        #     crew.kickoff(inputs=inputs)

        # Read and display the content of market_research.md
        #

        # if business_description:
        #     inputs = {
        #         'current_date': current_date.strftime('%Y/%m/%d'),
        #         'business_description': business_description,
        #     }
        #     # with st.spinner('Executing task...'):
        #     #     result = execute_lead_generation_task(inputs)
        #     # st.markdown(result)
    # else:
    #     st.write("This is HyperGrowAI agent, for Lead Generation")




# second one
# os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY_1')
# os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the LLM
llm = ChatGroq(temperature=0.2, model_name="llama3-70b-8192")


# --------- Tools ---------#
class SearchTools:

    @tool('search internet')
    def search_internet(query: str) -> str:
        """
        Use this tool to search the internet for information. This tools returns 5 results from Google search engine.
        """
        return SearchTools.search(query, limit=5)

    @tool('search instagram')
    def search_instagram(query: str) -> str:
        """
        Use this tool to search Instagram. This tools returns 5 results from Instagram pages.
        """
        return SearchTools.search(f"site:instagram.com {query}", limit=5)

    @tool('open page')
    def open_page(url: str) -> str:
        """
        Use this tool to open a webpage and get the content.
        """
        loader = WebBaseLoader(url)
        return loader.load()

    def search(query, limit=5):
        url = "https://google.serper.dev/search"
        payload = json.dumps({
            "q": query,
            "num": limit,
        })
        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY"),
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['organic']

        string = []
        for result in results:
            string.append(f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n")

        return f"Search results for '{query}':\n\n" + "\n".join(string)


# --------- Defining Agents ---------#

# Define the Instagram Market Researcher agent
# market_researcher = Agent(
#     role='Instagram Market Researcher',
#     goal='Analyze industry trends, competitor activities, and popular hashtags on Instagram. Perform research on the latest trends, hashtags, and competitor activities on Instagram using your Search tools.',
#     backstory=(
#         "Armed with a keen eye for digital trends and a deep understanding of the Instagram landscape, you excel at uncovering actionable insights from social media data. "
#         "Your analytical skills are unmatched, providing a solid foundation for strategic decisions in content creation. You are great at identifying the latest trends and the best hashtags for a given campaign."
#     ),
#     tools=[
#         SearchTools.search_internet,
#         SearchTools.search_instagram,
#         SearchTools.open_page,
#     ],
#     llm=llm,
#     #max_iter=4,
#     max_rpm=4000,
#     allow_delegation=True
# )

# Define the Instagram Content Strategist agent
# content_strategist = Agent(
#     role='Instagram Content Strategist',
#     goal='Develop a content calendar based on market research findings, incorporating trends, optimal posting times, and strategic content themes for next three days.',
#     backstory=(
#         "As a master planner with a creative spirit, you have a talent for envisioning a cohesive content strategy that resonates with audiences. "
#         "Your expertise in aligning content with brand voice and audience interests has consistently driven engagement and growth."
#     ),
#     tools=[],
#     max_iter=4,
#     max_rpm=4000,
#     llm=llm,
#     allow_delegation=True
# )

# Define the Instagram Copywriter agent
# writer = Agent(
#     role='Instagram Copywriter',
#     goal='Craft engaging and relevant copy for each Instagram post, complementing the visual content and adhering to the strategic content themes.',
#     backstory=(
#         "With a flair for storytelling and a persuasive pen, you create narratives that captivate and engage the audience. Your words are the bridge between the brand and its followers, embodying the brand's voice in every caption and call to action. "
#         "Your writing is not only engaging but also incorporates all the SEO techniques, such as seamlessly using top keywords given to you and adding the best hashtags that are trending at the moment."
#     ),
#     tools=[],
#     llm=llm,
#     #max_iter=4,
#     max_rpm=4000,
#     allow_delegation=True
# )

# ---------- Defining task ----------#

# market_research = Task(
#     description="""Investigate the latest trends, hashtags, and competitor activities on Instagram specific to the industry of this Instagram account. Focus on gathering data that reveals what content performs well in the current year, identifying patterns, preferences, and emerging trends.
#
#     Current date: {current_date}
#
#     Description of the instagram account for which you are doing this research:
#     <INSTAGRAM_ACCOUNT_DESCRIPTION>{instagram_description}</INSTAGRAM_ACCOUNT_DESCRIPTION>
#
#     Based on your research, determine and suggest the most relevant topics, hashtags and trends to use in the posts for 3 DAYS.
#     """,
#     expected_output='A report with the most relevant information that you found, including relevant hashtags for this week\'s content, suggested focus for next week, and all other information that could be useful to the team working on content creation.',
#     tools=[],
#     agent=market_researcher,
#     output_file="market_research.md",
# )

# content_strategy = Task(
#     description="""Based on the market research findings, develop a detailed schedule for posting Instagram posts over the next three days. The schedule should include the theme for each day, DETAILED CONTENT IDEA, and the most relevant hashtags to use for each post. Focus on what will improve customer engagement, including optimal posting times and strategies to increase interaction.
#
#     The schedule should cover:
#     - Themes and post ideas for each day
#     - Detailed description of content
#     - Best hashtags to use for each post
#     - Suggested posting times
#     """,
#     expected_output='A detailed schedule formatted as markdown, covering the next three days. Each day should include the theme, content ideas, hashtags, and suggested posting times to improve engagement.',
#     tools=[],
#     agent=content_strategist,
# )

# writing = Task(
#     description="""Write captivating and relevant copy for each Instagram post of the week, aligning to the strategic themes of the content calendar. The copy should engage the audience, embody the brand's voice, and encourage interaction. The copy should also be SEO-friendly and incorporate the relevant keywords and hashtags contained in the content schedule.
#
#     Consider the following guidelines when writing the copy:
#     - Keep the copy concise and engaging.
#     - Include a call to action where appropriate.
#     - Use relevant keywords and hashtags.
#     - Ensure the copy aligns with the brand's voice and tone.
#     """,
#     expected_output='A document formatted as markdown, with several sections. Each section should contain the copy for a single Instagram post, along with the relevant hashtags and calls to action. The copy should be engaging, on-brand, and aligned with the content calendar.',
#     tools=[],
#     agent=writer,
# )
#
# crew = Crew(
#     agents=[market_researcher,writer],
#     tasks=[market_research, writing],
#     process=Process.sequential,
# )
def run_file2():
    # Streamlit UI
    st.title("💬 HyperGrowth.ai")
    st.markdown("### Delivering Superior Generative AI Marketing Services To Small Businesses Worldwide")
    st.markdown("### Build a Killer Brand with HyperGrow - Content Strategist")

    instagram_description = st.text_input('Instagram Account Description')
    current_date = st.date_input('Current Date', datetime.date.today())

    if st.button('Generate Strategy'):
        inputs = {
            'current_date': current_date.strftime('%Y/%m/%d'),
            'instagram_description': instagram_description
        }
        print("This is HyperGrowAI agent, for Instagram Marketing Strategy Generation")

        # with st.spinner('Generating strategy...'):
        #     crew.kickoff(inputs=inputs)

        # Read and display the content of market_research.md
        #
    else:
        print("This is HyperGrowAI agent, for Instagram Marketing Generation")



def run_file3():
    st.write("Marketing Roadmap Generator AI")
    # tool = SerperDevTool()

#     # Page Configuration
#     # st.set_page_config(page_title="Zyper.ai", page_icon="💬", layout="wide")
#
#     # Title and Description
    st.title("💬 HyperGrowth.ai")
    st.markdown("### Delivering Superior Generative AI Marketing Services To Small Businesses Worldwide")
#
#     # Sidebar for Navigation
#     # with st.sidebar:
#     #     selected = option_menu(
#     #         "Main Menu",
#     #         ["Home", "About", "Contact"],
#     #         icons=["house", "info-circle", "envelope"],
#     #         menu_icon="cast",
#     #         default_index=0,
#     #     )
#
#
#     # if selected == "Home":
#         # Initialize the tool for internet searching capabilities
#     tool = SerperDevTool()

    # os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')
    llm3 = ChatGroq(temperature=0.2, model_name="llama3-70b-8192")

    avators = {
            "Writer": "https://cdn-icons-png.flaticon.com/512/320/320336.png",
            "Reviewer": "https://cdn-icons-png.freepik.com/512/9408/9408201.png"
        }

    # industry_researcher = Agent(
    #         name="Industry Researcher",
    #         role="Research",
    #         goal="Provide comprehensive research on the specific industry of the client",
    #         backstory=f"Designed to gather up-to-date and relevant information to help tailor the marketing strategy to industry trends and benchmarks",
    #         verbose=True,
    #         llm=llm,
    #         allow_delegation=True,
    #         tools=[tool],
    #         # max_iter = 7,
    #         # max_rpm = 4000
    #     )

        # Define the Marketing Roadmap Agent
    # roadmap_creator = Agent(
    #         name="Roadmap Creator",
    #         role="Marketing",
    #         goal="Develop a detailed and actionable marketing roadmap based on the client's industry, size, budget, and team capacity",
    #         backstory="An expert marketer with extensive knowledge in crafting strategies that align with business goals and market dynamics",
    #         verbose=True,
    #         llm=llm,
    #         allow_delegation=False,
    #         tools=[],
    #         # max_iter=7,
    #         # max_rpm=4000
    #
    #     )

    st.markdown("#### HyperGrow - Marketing Roadmap - Your roadmap to business grwoth")

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

    # if st.button("Submit Details"):
    #         st.session_state["details"] = {
    #             "business_goals": business_goals,
    #             "competitors": competitors,
    #             "keywords": keywords,
    #             "marketing_budget": marketing_budget,
    #             "location": location
    #         }

    st.markdown("### Details Submitted")
    # st.write(st.session_state["details"])

    # if "details" in st.session_state:
    prompt = st.text_area("Enter your business overview:")

    if st.button("Submit Overview"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

            # Define the tasks
        # gather_industry_insights = Task(
        #             description=f"Collect detailed information about the specific {prompt} industry, including current trends, benchmarks,competitor research on {competitors} and best practices specific for the location - {location} by using the following keywords {keywords}.",
        #             agent=industry_researcher,
        #             expected_output="""
        #                 "industry_trends": "A report on current industry trends",
        #                 "benchmarks": "Benchmark data for the industry",
        #                 "best_practices": "List of best practices relevant to the industry"
        #             """
        #         )
        #
        # develop_marketing_strategy = Task(
        #             description=f"Use the gathered insights to create a comprehensive marketing strategy for {prompt} based on the business goals of -  {business_goals},and provided marketing budget of {marketing_budget}. Make the business plan relevant to the location - {location} provided."
        #     "Also provide a marketing budget allocation ",
        #             agent=roadmap_creator,
        #             expected_output=
        #             """
        #                 "marketing_goals": "A list of measurable and time-bound marketing goals based on the industry and user needs",
        #                 "initiatives": "Detailed description of marketing initiatives",
        #                 "schedule": "Chronological schedule of marketing activities",
        #                 "activities": "List of marketing activities",
        #                 "status_tracking": "Method for tracking the status of goals, initiatives, and activities"
        #             """
        #         )
        # crew = Crew(
        #             agents=[industry_researcher, roadmap_creator],
        #             tasks=[gather_industry_insights, develop_marketing_strategy],
        #             process=Process.sequential,
        #         )



        with st.spinner('Generating strategy...'):
            st.write("This is HyperGrowAI agent, for Marketing Strategy & Roadmap Generation")
        #     crew.kickoff(inputs=inputs)

        # Read and display the content of market_research.md
        #

        # final = crew.kickoff()
        #
        # result = f"## Here is the Final Result \n\n {final}"
        #
        #         # Display result in beautiful format
        # st.markdown("## Analysis Result")
        # st.write(result)

    # elif selected == "About":
    #     st.markdown("### About Zyper.ai")
    #     st.write(
    #         "HyperGrowth.ai is an AI-first digital marketing agency that provides superior generative AI-based marketing solutions. Our mission is to deliver comprehensive and customized marketing strategies that align with your business goals.")
    #
    # elif selected == "Contact":
    #     st.markdown("### Contact Us")
    #     st.write("For any inquiries, please reach out to us at: support@zyper.ai")




# Streamlit UI

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
import streamlit as st
from PIL import Image

# Load images (Replace these with actual file paths or URLs)
founder1_img = Image.open("LinkedIn Photo Divyansh.jpg")
founder2_img = Image.open("1716045696197.jpg")


# Home page
if selected == "Home":
    st.title("Welcome to HyperGrow AI")
    st.write("Select one of the options from the sidebar to run the corresponding module or to learn more about us.")

    st.subheader("What We Offer")
    st.markdown("""
        - *AI-Powered Lead Generation*: Harness the power of AI to identify and nurture leads.
        - *Social Media Content Creation*: Generate engaging content for your social media platforms.
        - *Workflow Automation*: Streamline your business processes with our AI tools.
    """)

    st.subheader("Why Choose Us?")
    st.write("""
        At HyperGrow AI, we are committed to providing cutting-edge AI solutions that enhance productivity and drive business growth. Our platform is user-friendly, highly customizable, and designed to meet the specific needs of your business.
    """)

# About page
elif selected == "About":
    st.title("About HyperGrow AI")

    st.subheader("Our Mission")
    st.write(
        "To leverage AI technologies to simplify and optimize business operations, empowering businesses to achieve their full potential.")

    st.subheader("Our Vision")
    st.write("To be a global leader in AI-powered business solutions, making AI accessible and beneficial for all.")

    st.subheader("Our Team")
    st.write("Meet the people behind HyperGrow AI.")

    # Team section with images and descriptions
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <style>
            .img-circle {
                border-radius: 50px;
                width: 100px;
                height: 100px;
                object-fit: cover;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            '<img src="data:image/png;base64,{}" class="img-circle" alt="Divyansh Tuli">'.format(
                st.image(founder1_img, use_column_width=False, width=100)
            ),
            unsafe_allow_html=True
        )
        st.write(
            "Divyansh Tuli is passionate about Artificial Intelligence and is currently pursuing a degree in Electronics and Communication Engineering (ECE) from Delhi Technological University. Connect with Divyansh on [LinkedIn](#) and [Twitter](#).")

    with col2:
        st.markdown(
            '<img src="data:image/png;base64,{}" class="img-circle" alt="Hardik Yadav">'.format(
                st.image(founder2_img, use_column_width=False, width=100)
            ),
            unsafe_allow_html=True
        )
        st.write(
            "Hardik Yadav is passionate about Artificial Intelligence and is currently pursuing a degree in Electronics and Communication Engineering (ECE) from Delhi Technological University. Connect with Hardik on [LinkedIn](#) and [Twitter](#).")

# Contact Us page
elif selected == "Contact Us":
    st.title("Contact Us")
    st.write("We'd love to hear from you! Fill out the form below or reach out to us via email or phone.")

    # Contact form
    st.subheader("Contact Form")
    contact_form = st.form(key="contact_form")
    name = contact_form.text_input("Name")
    email = contact_form.text_input("Email")
    message = contact_form.text_area("Message")
    submit_button = contact_form.form_submit_button(label="Submit")

    if submit_button:
        st.success(f"Thank you {name}! We have received your message and will get back to you soon.")

    st.subheader("Other Contact Methods")
    st.write("*Email:* reway.ewm@gmail.com")
    st.write("*Phone:* +91 7290908877 | +91 9899115560")




# Run Lead Gen
elif selected == "Run Lead Gen":
    # st.title("Run Lead Gen Module")
    run_file1()
    st.write("Lead Gen module is running...")

# Run Insta Content
elif selected == "Run Insta Content":
    # st.title("Run Instagram Content Module")
    run_file2()
    st.write("Instagram Content module is running...")

# Run File 3
elif selected == "Marketing Roadmap":
    # st.title("")
    run_file3()
    st.write("Marketing Roadmap Creator is running...")

# Footer
st.markdown("---")
st.markdown("© 2024 HyperGrowth.ai All rights reserved.")