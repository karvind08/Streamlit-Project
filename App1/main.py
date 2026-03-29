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
# st.help(pd)
# st.help(st)
st.divider()
st.html('<body><h1> Hello</></body>')
st.divider()
st.button('Click Me')
st.divider()
st.button("Reset", type="primary")
st.divider()
btn = st.button("Say hello")
if btn:
    st.write("Why hello there")
else:
    st.write("Goodbye")
st.divider()
left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")
st.divider()