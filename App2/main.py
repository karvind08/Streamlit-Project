import streamlit as st

about_page = st.Page(
    page = "views/about_me.py",
    title = "About Us",
    icon = ":material/account_circle:",
    default = True,
)

project_1_page = st.Page(
    page = "views/sales_dashboard.py",
    title = "Sales Dashboard",
    icon = ":material/bar_chart:",
)

project_2_page = st.Page(
    page = "views/chatbot.py",
    title = "Chat Bot",
    icon = ":material/smart_toy:",
)

project_3_page = st.Page(
    page = "views/contact.py",
    title = "Contact",
    icon = ":material/contact_page:",
)
#pg = st.navigation(pages=[about_page,project_1_page,project_2_page,project_3_page])

pg = st.navigation(
    {
        "Info": [about_page,project_3_page],
        "Projects": [project_1_page,project_2_page],
    }
)

st.logo("assets/logo.png")
st.sidebar.text("Made with 💕 by Arvind")
pg.run()