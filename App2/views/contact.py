import streamlit as st
from forms.contacts import contact_form
st.title("Contact Us")


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# if st.button("📧 Contact Me"):
#         show_contact_form()

show_contact_form()