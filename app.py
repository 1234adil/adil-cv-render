from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Adil Ahmadzada"
PAGE_ICON = ":wave:"
NAME = "Adil Ahmadzada"
DESCRIPTION = """
Business Development Manager / Consultant, Lean Six Sigma Professional.
"""
EMAIL = "adilahmadzada5@gmail.com"
SOCIAL_MEDIA = {
    "YouTube":  "https://www.youtube.com/channel/UCWmMj6MDEvHmiad8FgGBVNQ",
    "LinkedIn": "https://www.linkedin.com/in/adil-ahmadzada-9375251b8/",
    "Personal": "https://adilahmadzada.dorik.io/"
}
PROJECTS = {
    "🏆 Azerbaijan: Plastic injection and moulding machine manufacturing project.": "https://adilahmadzada.dorik.io/",
    "🏆 Azerbaijan: Building projects.": "https://adilahmadzada.dorik.io/",
    "🏆 Azerbaijan: Residential area projects.": "https://adilahmadzada.dorik.io/",
    "🏆 Kazakhstan: Business mall construction projects.": "https://adilahmadzada.dorik.io/",
    "🏆 Kazakhstan: Residential area construction projects.": "https://adilahmadzada.dorik.io/",
    "🏆 Kazakhstan: Road construction projects.": "https://adilahmadzada.dorik.io/",
    "🏆 Macedonia:  Solar panel energy projects.": "https://adilahmadzada.dorik.io/",
    "🏆 Maritious:  Oil refinery projects.": "https://adilahmadzada.dorik.io/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Master of Engineering: Azerbaijan State Oil and Industrial University | 2021-2023
- ✔️ Bachelor of Engineering: Azerbaijan State Oil and Industrial University | 2014-2018 
- ✔️ Master of Project Management: Rochester Institute of Technology | 2022-current
- ✔️ Diploma in Business Administration: Alison University (UK/CPD) | 2020-2021 
- ✔️ Master of Engineering Project Management: Rice University | 2019-2020
- ✔️ Lean Six Sigma Black Belt: Project Management Institute (USA) | 2019-2020
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 🖥️ Microsoft Office: Word, Excel, Power point, Outlook, Teams, Project
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Business Development Manager | Galatine**")
st.write("07/2022 - Present")
st.write(
    """
- ► Achieving business goals and revenue targets.
- ► Overseeing daily operations, managing budgets, and setting performance objectives.
- ► Developing and implementing business, marketing, and advertising plans.
- ► Managing internal and external stakeholder relations and negotiating contracts.
- ► Planning, evaluating, and optimizing operations to be efficient and cost-effective.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Business Development Manager | Caspian Express**")
st.write("07/2022 - 03/20223")
st.write(
    """
- ► Preparing and presenting monthly, quarterly, and annual statements, analyses, and reports of operations and finances.
- ► Achieving business goals and revenue targets.
- ► Overseeing daily operations, managing budgets, and setting performance objectives.
- ► Developing and implementing business, marketing, and advertising plans.
- ► Managing internal and external stakeholder relations and negotiating contracts.
- ► Planning, evaluating, and optimizing operations to be efficient and cost-effective.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Project Developer | ASOS Company**")
st.write("12/2021 - 07/2022")
st.write(
    """
- ► Achieving business goals and revenue targets.
- ► Overseeing daily operations, managing budgets, and setting performance objectives.
- ► Developing and implementing business, marketing, and advertising plans.
- ► Managing internal and external stakeholder relations and negotiating contracts.
- ► Planning, evaluating, and optimizing operations to be efficient and cost-effective.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Production Engineer | AFF COMPANY ( LUMUN & PASHA HOLDING )**")
st.write("12/2020 - 12/2021")
st.write(
    """
- ► Achieving business goals and revenue targets.
- ► Overseeing daily operations, managing budgets, and setting performance objectives.
- ► Developing and implementing business, marketing, and advertising plans.
- ► Managing internal and external stakeholder relations and negotiating contracts.
- ► Planning, evaluating, and optimizing operations to be efficient and cost-effective.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Manufacturing Sales Engineer | Sumgait Technologies Parks**")
st.write("12/2019 - 12/2020")
st.write(
    """
- ► Achieving business goals and revenue targets.
- ► Overseeing daily operations, managing budgets, and setting performance objectives.
- ► Developing and implementing business, marketing, and advertising plans.
- ► Managing internal and external stakeholder relations and negotiating contracts.
- ► Planning, evaluating, and optimizing operations to be efficient and cost-effective.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

