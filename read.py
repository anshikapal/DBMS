import pandas as pd
import streamlit as st
import plotly.express as px

from database import view_all_user_account
from database import view_all_wallet
from database import view_all_data_transactions
from database import view_all_data_promo_offers
from database import view_all_data_dependents
from database import view_all_data_transaction_status
from database import view_all_data_promo_offers_transactions




def read(table):
    if table=='user_account':
        result = view_all_user_account()
        # st.write(result)
        df = pd.DataFrame(result, columns=['user_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name'])
        with st.expander("View all user_accounts"):
            st.dataframe(df)
        with st.expander("user city"):
            task_df = df['city'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='city')
            st.plotly_chart(p1)


    elif table=='wallet':
        result = view_all_wallet()
        # st.write(result)
        df = pd.DataFrame(result, columns=['t_id','user_id','account_no', 'bank_name','balance','promocode','loan'])
        with st.expander("View all wallets"):
            st.dataframe(df)
        with st.expander("user Bank_name"):
            task_df = df['bank_name'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='bank_name')
            st.plotly_chart(p1)

    elif table=='promo_offers_transactions':
        result = view_all_data_promo_offers_transactions()
        # st.write(result)
        df = pd.DataFrame(result, columns=['prom_id','usr_id','transactions_no','duration', 'amount_value'])
        with st.expander("View all promo_offers"):
            st.dataframe(df)
        with st.expander("user promos"):
            task_df = df['usr_id'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='usr_id')
            st.plotly_chart(p1)


    elif table=='transactions':
        result = view_all_data_transactions()
        # st.write(result)
        df = pd.DataFrame(result, columns=['transaction_id', 'transaction_date','transaction_detail', 'amount','to_id','from_id','type_trans'])
        with st.expander("View all transactions"):
            st.dataframe(df)


    elif table=='promo_offers':
        result = view_all_data_promo_offers()
        # st.write(result)
        df = pd.DataFrame(result, columns=['promo_id','user_id','start_date','end_date','duration','status', 'amount_value'])
        with st.expander("View all promo_offers"):
            st.dataframe(df)
        with st.expander("user promos"):
            task_df = df['user_id'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='user_id')
            st.plotly_chart(p1)


    elif table=='dependents':
        result = view_all_data_dependents()
        # st.write(result)
        df = pd.DataFrame(result, columns=['dependent_id','trans_id','user_ref_id','fname','lname','phone' ,'email' ,'dob','relation'])
        with st.expander("View all dependents"):
            st.dataframe(df)
        


    elif table=='transaction_status':
        result = view_all_data_transaction_status()
        # st.write(result)
        df = pd.DataFrame(result, columns=['trans_id','u_id','status'])
        with st.expander("View all status"):
            st.dataframe(df)
        

