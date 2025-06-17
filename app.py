import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="Madhu Portfolio", page_icon="💻", layout="wide")

# --- Custom CSS for Enhanced Styling ---
custom_css = """
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .header-title {
        color: #4CAF50;
        text-align: center;
        font-size: 3em;
        margin-bottom: 0.5em;
    }
    .section-header {
        color: #333333;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
    }
    .subheader {
        color: #4CAF50;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        font-size: 0.9em;
        margin-top: 2em;
        color: #777777;
    }
    .container {
        margin: 0 auto;
        max-width: 900px;
        padding: 0 2em;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    try:
        profile_pic = Image.open("images/profile.jpg")
        st.image(profile_pic, width=150)
    except Exception as e:
        st.write("Profile image not found.")
    st.title("Madhu")
    st.markdown("**B.Tech CSE | AI/ML Intern | Web Developer**")
    st.write("---")
    st.write("📧 madhu21kaushik@gmail.com")
    st.write("📞 +91 9650194508")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/madhu-kaushik2003)")
    st.write("💻 [GitHub](https://github.com/madhukaushik03)")

# --- Main Content ---

# Header
st.markdown("<h1 class='header-title'>🚀 Welcome to My Portfolio</h1>", unsafe_allow_html=True)

# --- About Me ---
with st.container():
    st.markdown("<h2 class='section-header'>👩‍💻 About Me</h2>", unsafe_allow_html=True)
    st.write("""
    Hi, I'm **Madhu** – a driven B.Tech CSE student from Guru Gobind Singh Indraprastha University, Delhi with a passion for Artificial Intelligence, Machine Learning, and Full Stack Development.  
    I have excelled as an AI/ML Intern by developing and deploying machine learning models and enjoyed mentoring over 5000 students as a Teaching Assistant, resolving more than 900 doubts.  
    I thrive on merging technical expertise with creativity to build interactive dashboards and robust applications.
    """)

# --- Skills ---
with st.container():
    st.markdown("<h2 class='section-header'>🛠️ Skills</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Languages & Tools")
        st.write("• C/C++, Python, Java")
        st.write("• HTML, CSS, JavaScript")
        st.write("• Git, GitHub, Postman")
    
    with col2:
        st.markdown("### Frameworks & Libraries")
        st.write("• React.js, Flask, Streamlit")
        st.write("• Pandas, NumPy, Matplotlib, Seaborn")
        st.write("• SQLAlchemy")
    
    st.markdown("#### Databases")
    st.write("MySQL, SQLite")
    
    st.markdown("#### Core Competencies")
    st.write("• Object-Oriented Programming (OOP) in C++")
    st.write("• Data Structures & Algorithms in Java")
    st.write("• DBMS")

# --- Experience ---
with st.container():
    st.markdown("<h2 class='section-header'>💼 Experience</h2>", unsafe_allow_html=True)

    st.markdown("#### 🔹 AI/ML Intern — ShadowFox Technologies (Apr 2025)")
    st.write("""
    • Developed and deployed ML models such as **Loan Approval** and **Boston House Price Prediction**.  
    • Managed end-to-end data pipelines including preprocessing, exploratory data analysis (EDA), and evaluation using metrics like accuracy and confusion matrices.  
    • Designed interactive Streamlit dashboards for real-time prediction visualization.
    """)
    
    st.markdown("#### 🔹 Teaching Assistant — Java & DSA (May 2024 – Sept 2024)")
    st.write("""
    • Assisted over 5000 students and resolved more than 900 doubts, maintaining a **5-star** average rating.  
    • Guided learners on core DSA concepts and Java best practices, enhancing problem-solving skills.
    """)

# --- Projects ---
with st.container():
    st.markdown("<h2 class='section-header'>📂 Projects</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 💸 AI-Powered Financial Manager")
        st.write("""
        • Full-stack web application for tracking expenses, setting budgets, and forecasting spending using machine learning.  
        • Features include user authentication, ML-driven predictions, and interactive graphs.  
        • **Stack:** React.js (Frontend), Flask & Python (Backend), SQLite (Database).
        [GitHub Repo](https://github.com/madhukaushik03/financial-management-app)
        """)
    with col2:
        st.markdown("#### 🏠 Loan Approval Predictor")
        st.write("""
        • Predictive app assessing loan approval chances through a clean UI and robust model evaluation.  
        • **Stack:** Python, Streamlit, Scikit-learn.
        """)
        
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("#### 🏡 Boston House Price Prediction")
        st.write("""
        • Regression model to forecast house prices with visualization via Streamlit dashboards.
        """)
    with col4:
        st.markdown("#### 🤖 Jarvis Assistant")
        st.write("""
        • Python-based personal assistant project integrating speech recognition and text-to-speech.  
        • Automates routine tasks and simulates a conversational assistant experience.  
        • **Stack:** Python, Speech Recognition libraries, Text-to-Speech engines.  
        • [GitHub Repo](https://github.com/madhukaushik03/PYTHON-PROJECT-JARVIS)
        """)

# --- Education ---
with st.container():
    st.markdown("<h2 class='section-header'>🎓 Education</h2>", unsafe_allow_html=True)
    st.write("""
    • **B.Tech in Computer Science & Engineering**, Guru Gobind Singh Indraprastha University, Delhi  
      *CGPA: 9.08 | 2023–Present*  
    • **Class XII – CBSE (Science Stream)**, Kendriya Vidyalaya, Sector 8 Rohini, Delhi  
      *Score: 90.0% | 2022*  
    • **Class X – CBSE**, Panacea National Public School, Delhi  
      *Score: 89.0% | 2020*
    """)

# --- Footer ---
st.markdown("<div class='footer'>Made with ❤️ by Madhu Kaushik</div>", unsafe_allow_html=True)
