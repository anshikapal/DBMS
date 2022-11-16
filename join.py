import streamlit as st
import pandas as pd
from database import joining_2
from database import joining
from database import joining_3
from database import joining_4

def join():

    if st.button('Display Join On wallet and transactions'):
        df=pd.DataFrame(joining(),columns=['user_id','acc_no','bank_name',"transaction_details"])
        st.dataframe(df)
    if st.button('Display Join On transaction_status and transactions'):
        df=pd.DataFrame(joining_2(),columns=['transaction_id','u_id','to_id',"from_id",'status'])
        st.dataframe(df)

    if st.button('Display Join On dependents and transactions'):
        df=pd.DataFrame(joining_3(),columns=['Transaction Id','Transaction Type','Detail',"Dependent id",'Relation'])
        st.dataframe(df)
    if st.button('Display Join On wallet and user_account'):
        df=pd.DataFrame(joining_4(),columns=['User Id','First name','Last name',"Bank name",'Balance','Loan'])
        st.dataframe(df)