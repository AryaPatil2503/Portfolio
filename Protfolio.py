import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":wave:", layout="wide")

# Custom CSS for dark theme and horizontal tabs
st.markdown("""
<style>
body {
    background-color: #121212;
    color: white;
}
.main {
    background: #121212;
    padding: 20px;
    color: white;
}
.header, .footer {
    background-color: #1f1f2e;
    color: white;
    padding: 10px 0;
}
.header {
    font-size: 2em;
    text-align: center;
}
.footer {
    text-align: center;
    font-size: 0.8em;
}
.section {
    margin-bottom: 40px;
}
.title {
    font-size: 1.5em;
    margin-bottom: 20px;
    color: white;
}
.profile-pic {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 150px;
    border-radius: 50%;
}
.projects, .skills, .experience {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}
.project, .skill, .job {
    background: #1f1f2e;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    color: white;
}
.nav-container {
    margin-top: 48px;
    display: flex;
    justify-content: center;
}
.stRadio > div {
    flex-direction: row;
    gap: 20px;
}
.stRadio > div > label {
    background: #1f1f2e;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    margin: 0;
}
.stRadio > div > label:hover {
    background: #333;
}
.stRadio > div > label[data-baseweb="radio"] {
    border: 2px solid transparent;
}
.stRadio > div > label[data-baseweb="radio"]:hover {
    border-color: #555;
}
.stRadio > div > label[data-baseweb="radio"] > div:first-child {
    display: none;
}
.stRadio > div > label[data-baseweb="radio"]:checked {
    background: #333;
    border-color: #fff;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">My Portfolio</div>', unsafe_allow_html=True)

# Create a div container for the navigation to add margin
st.markdown('<div class="nav-container">', unsafe_allow_html=True)

# Create horizontal tabs using st.radio
tabs = ["About Me", "Education", "Projects", "Internships", "Achievements", "Contact"]
selected_tab = st.radio("", tabs, index=0)

# Close the div container
st.markdown('</div>', unsafe_allow_html=True)

# Content for each tab
if selected_tab == "About Me":
    st.image("Profile.jpeg", width=150, caption="")
    st.markdown("""
    ## Hi, I'm Arya Patil 👋

    Welcome to my portfolio! I'm Enthusiastic and dedicated learner, studying in the field of Electronics and Telecommunication Engineering. Seeking an entry-level data analyst role to improve analytical and problem-solving skills in a dynamic and challenging environment. Proficient in multiple skills with Excellent communication and teamwork skills. A foodie by heart who loves to sing, play chess and interact with new minds..
    """, unsafe_allow_html=True)

elif selected_tab == "Education":
    st.markdown("""
    ## Education

    - **B.Tech Electronics and Telecommunication** - MIT Academy of Engineering, Pune  (2020 - 2024) **CGPA: 8.40**
                                                 
    - **HSC** - Vivek Vardhini Junior College, Pandharpur (2020) **Percentage - 84.62%**

    - **SSC** - Vivekanand Pratishthan B.G.S. Vidyalaya (2018) **Percentage - 94.40%**
    """, unsafe_allow_html=True)

elif selected_tab == "Projects":
    st.markdown("## Projects")
    
    # Project One
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("Concept_Diagram.jpg", caption="Project One")
    with col2:
        st.markdown("""
        ### Anomaly-based Intrusion Detection System for IoT Environment using Machine Learning
        - Simulated an IoT environment with NODE MCU ESP8266, DHT11 sensors, and a wireless router.
        - Implemented an adversarial system for sniffing and poisoning attacks.
        - Captured and labeled sensor data during normal and attack phases.
        - Achieved a high accuracy of 93% using Isolation Forest for anomaly detection. 

        """)
    
    # Project Two
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("Deeplearning.png", caption="Project Two")
    with col2:
        st.markdown("""
        ### Performance Analysis of Model Optimization Techniques using Pre-Trained CNN Models
        - Utilized a pre-trained Inception V3 model with Image data set.
        - Conducted hyper-parameter tuning, experimenting with model optimizers like Adam and Glorot.
        - Explored regularization and weight initialization techniques to identify the optimal combination.
        - Achieved a classification accuracy of 83.99% using Adam optimizer with random normal and L1 regularization.
        """)
    
elif selected_tab == "Internships":
    st.markdown("## Internships")
    
    # Internship One
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("LandT.png", caption="Internship One")
    with col2:
        st.markdown("""
        ### Data Analyst Intern
        **Larsen And Toubro**
        
        - Demonstrated exceptional contributions to diverse projects within the Quality Assurance team, ensuring the delivery of highquality results and adherence to strict standards.
        - Spearheaded the development of cutting-edge Power BI dashboards, streamlining data cleaning processes that led to a remarkable 30% reduction in dashboard refresh time.
        - Scripted a Python automation program, enabling efficient iteration through folders and transforming Excel files to meet precise format requirements.
        - Leveraged advanced Machine Learning techniques to develop a predictive model for Man-days estimation, optimizing resource allocation and enhancing project planning efficiency. 
        """)
    
    # Internship Two
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("DRDO.png", caption="Internship Two")
    with col2:
        st.markdown("""
        ### Data Analyst Intern
        **Research & Development Establishment (Engrs.), DRDO**
        
        - Analyzed the data manually in Microsoft Excel.
        - Scripted a Python automation program, enabling the analysis of attendance data of employees to meet precise format requirements.
        - Developed a Streamlit webapp to deploy the python script
        """)

elif selected_tab == "Achievements":
    st.markdown("## Achievements")
    
    # Achievements Images
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("Nirmaan.png", width=300, caption="Nirmaan Ideathon")
    with col2:
        st.image("Certificate.png", width=250,caption="Nirmaan Ideathon")  # Replace with actual image file
    with col3:
        st.image("Certificate2.jpg", width=250,caption="Chess Tournament")  # Replace with actual image file
    with col4:
        st.image("Certificate1.jpg", width=250,caption="Chess Tournament")  # Replace with actual image file

    st.markdown("""
    - **Nirmaan Ideathon**: 1st runner-up in “Nirmaan Ideathon” to ideate and develop solution organized by GDSC.
    - **Best Player**: MITAOE Best player award in institutional-level Chess competition.
    """, unsafe_allow_html=True)

elif selected_tab == "Contact":
    st.markdown("""
    ## Contact

    - **Email**: aryarpatil2503@gmail.com
    - **LinkedIn**: [arya-patil2503](https://www.linkedin.com/in/arya-patil2503/)
    - **GitHub**: [AryaPatil2503](https://github.com/AryaPatil2503)
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Arya Patil. All rights reserved.</div>', unsafe_allow_html=True)
