import streamlit as st
import pandas as pd
import numpy as np
st.title("My First Streamlit app")
st.divider()
st.header('Header')
st.divider()
st.subheader('Subheader')
st.divider()
st.text("This is text\n It is in another line")
st.divider()
st.text("\nThis is another text",help='This is streamlit text')
st.divider()
st.caption('This is caption')
st.divider()
st.markdown('*Hello* **This is another line** ***This is another***')
st.divider()
code = '''def hello():
    print("Hello, Streamlit!")
    print('I am Arvind')'''
st.code(code,language="Python",line_numbers=True,wrap_lines=True,height=None)
st.divider()
# Line Chart
chart_data = pd.DataFrame(np.random.randn(30,3),columns=["A","B","C"])
st.line_chart(chart_data)
st.divider()
st.help(pd)