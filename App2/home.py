import streamlit as st
about_page = st.Page(
    page = 'pages/about.py',
    title = 'About Me',
    icon = ':material/home:',
    default = True
)

contact_page = st.Page(
    page='pages/contact.py',
    title='Contact',
    icon = ':material/home:'
)

our_services = st.Page(
    page='pages/services.py',
    title='Our Services',
    icon = ':material/download:'
)
# pg = st.navigation(pages=[about_page,contact_page])
pg = st.navigation(
    {
        'Info':[about_page],
        'Contact':[contact_page],
        'Services':[our_services]
    }
)
st.logo("assets/heart.png")
st.sidebar.text("Made with 💕 by Arvind")
pg.run()