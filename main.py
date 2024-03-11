import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid

from excel_rw import read_excel_file

st.set_page_config(layout="wide")
st.title('Medical information labeling')

#file selection
uploaded_file = st.file_uploader("Choose a file",type=['xlsx','xls'])

if uploaded_file is None:
        st.stop()
df = read_excel_file(uploaded_file)
columns = df.columns.tolist()

selected_columns = st.multiselect('Select columns', columns)
if(selected_columns):
    AgGrid(df[selected_columns],editable=True)
else:
        st.write("Please select one or more column to display")
        st.stop()


if st.button('Save'):
        df.to_excel('output.xlsx',index=False)
        st.write("File saved as output.xlsx")