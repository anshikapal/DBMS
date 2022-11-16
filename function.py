import streamlit as st
import pandas as pd
from database import loan


def loan_1():
    x = st.text_input("Enter Balance in your account:")
    if st.button('Validate'):
        df=pd.DataFrame(loan(int(x)),columns=['Validate'])
        st.dataframe(df)
