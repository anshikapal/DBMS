import streamlit as st
import pandas as pd
from database import aggregate_2
from database import aggregate
from database import aggregate_3
from database import aggregate_4

def agg():

    if st.button('Display Bank Count'):
        df=pd.DataFrame(aggregate(),columns=['Bank_Name','Count'])
        st.dataframe(df)
    if st.button('Display Total Amount recieved to a user'):
        df=pd.DataFrame(aggregate_2(),columns=['To_user_id','Total Amount'])
        st.dataframe(df)
    if st.button('Display Average of amount bank has'):
        df=pd.DataFrame(aggregate_2(),columns=['Bank_name','Average'])
        st.dataframe(df)
    if st.button('Display Max amount'):
        df=pd.DataFrame(aggregate_2(),columns=['First Name','Amount'])
        st.dataframe(df)