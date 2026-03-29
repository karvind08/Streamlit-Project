import streamlit as st
from forms.contacts import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

st.title("About Me")

col1,col2 = st.columns(2,gap="small",vertical_alignment="center")

with col1:
#   st.image("./assets/arvind.png", width=150)
 st.subheader("Arvind Kumar", anchor=False) 
 #st.write("Arvind Kumar", anchor=False)

with col2:
    #st.write("Founder/Director", anchor=False)
    st.write("Founder/Director, Actolaze Technology LLP, Kharwal Academy - The School of Programming")
    if st.button("📧 Contact Me"):
        show_contact_form()

st.write("\n")
st.subheader("Programmings",anchor=False)
st.write("""
    - **C Programming** - C programming is a powerful, high-level language known for its efficiency and control over system resources. 
    - **Python Programming** - Python is a high-level, versatile programming language known for its readability, simplicity, and extensive libraries, widely used in data science and web development.
    - **Java Programming** - Java is a popular, object-oriented programming language known for its portability, security, and extensive libraries, widely used in enterprise applications.
    - **C++** - C++ is an extension of C, supporting object-oriented programming, templates, and low-level memory manipulation, widely used in software development and gaming.
""")

st.write("\n")
st.subheader("Technologies",anchor=False)
st.write("""
    - **WordPress** - WordPress is a popular content management system (CMS) that enables users to create and manage websites easily, featuring customizable themes and plugins.
    - **Joomla** - Joomla is a flexible content management system (CMS) that allows users to build websites and online applications, offering extensive features and extensions.
    - **Drupal** - Drupal is a powerful, open-source content management system (CMS) known for its flexibility, scalability, and robust community support for complex websites.
    - **Moodle** - Moodle is an open-source learning management system (LMS) designed for online education, offering tools for course creation, management, and student engagement.
    - **Django** - Django is a high-level Python web framework that promotes rapid development, clean design, and scalability, simplifying the creation of secure web applications.
    - **Laravel** - Laravel is a popular PHP framework that simplifies web application development with elegant syntax, built-in tools, and a robust ecosystem for developers.
    - **Streamlit** - Streamlit is an open-source framework for building interactive web applications in Python, enabling data scientists to create visualizations and dashboards effortlessly.
""")