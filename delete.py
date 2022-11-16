import pandas as pd
import streamlit as st
from database import view_only_user_account
from database import view_only_wallet
from database import view_only_data_transactions
from database import view_only_data_promo_offers
from database import view_only_data_dependents
from database import view_only_data_transaction_status
from database import view_only_data_promo_offers_transactions


from database import view_all_user_account
from database import view_all_wallet
from database import view_all_data_transactions
from database import view_all_data_promo_offers
from database import view_all_data_promo_offers_transactions
from database import view_all_data_dependents
from database import view_all_data_transaction_status

from database import delete_user_account
from database import delete_wallet
from database import delete_transactions
from database import delete_promo_offers
from database import delete_promo_offers_trsansactions
from database import delete_dependents
from database import delete_transaction_status

def delete(table):
    if table=='user_account':
        result = view_all_user_account()
        df = pd.DataFrame(result, columns=['user_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_user_account()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete user"):
            delete_user_account(selected_user)
            st.success("user has been deleted successfully")
        new_result = view_all_user_account()
        df2 = pd.DataFrame(new_result, columns=['user_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='wallet':
        result = view_all_wallet()
        df = pd.DataFrame(result, columns=['t_id','user_id','account_no', 'bank_name','balance','promocode','loan'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_wallet()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete wallet"):
            delete_wallet(selected_user)
            st.success("Wallet has been deleted successfully")
        new_result = view_all_wallet()
        df2 = pd.DataFrame(new_result, columns=['t_id','user_id','account_no', 'bank_name','balance','promocode','loan'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='promo_offers_trsansactions':
        result = view_all_data_promo_offers_transactions()
        df = pd.DataFrame(result, columns=['prom_id','usr_id','transactions_no','duration', 'amount_value'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_data_promo_offers_transactions()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete promo_offers"):
            delete_promo_offers_trsansactions(selected_user)
            st.success("user has been deleted successfully")
        new_result = view_all_data_promo_offers_transactions()
        df2 = pd.DataFrame(new_result, columns=['prom_id','usr_id','transactions_no','duration', 'amount_value'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='transactions':
        result = view_all_data_transactions()
        df = pd.DataFrame(result, columns=['transaction_id', 'transaction_date','transaction_detail', 'amount','to_id','from_id','type_trans'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_data_transactions()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete transactions"):
            delete_transactions(selected_user)
            st.success("Transaction has been deleted successfully")
        new_result = view_all_wallet()
        df2 = pd.DataFrame(new_result, columns=['transaction_id', 'transaction_date','transaction_detail', 'amount','to_id','from_id','type_trans'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='promo_offers':
        result = view_all_data_transactions()
        df = pd.DataFrame(result, columns=['promo_id','user_id','start_date','end_date','duration','status', 'amount_value'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_data_promo_offers()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete promo_offers"):
            delete_promo_offers(selected_user)
            st.success("user has been deleted successfully")
        new_result = view_all_data_promo_offers()
        df2 = pd.DataFrame(new_result, columns=['promo_id','user_id','start_date','end_date','duration','status', 'amount_value'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    elif table=='dependents':
        result = view_all_data_dependents()
        df = pd.DataFrame(result, columns=['dependent_id','trans_id','user_ref_id','fname','lname','phone' ,'email' ,'dob','relation'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_data_dependents()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete dependents"):
            delete_dependents(selected_user)
            st.success("Dependent has been deleted successfully")
        new_result = view_all_data_dependents()
        df2 = pd.DataFrame(new_result, columns=['dependent_id','trans_id','user_ref_id','fname','lname','phone' ,'email' ,'dob','relation'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='transaction_status':
        result = view_all_data_transaction_status()
        df = pd.DataFrame(result, columns=['trans_id','u_id','status'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_data_transaction_status()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete status"):
            delete_transaction_status(selected_user)
            st.success("status has been deleted successfully")
        new_result = view_all_data_transaction_status()
        df2 = pd.DataFrame(new_result, columns=['trans_id','u_id','status'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    




