import streamlit as st
from database import add_data_user_account
from database import add_data_wallet
from database import add_data_transactions
from database import add_data_promo_offers
from database import add_data_dependents
from database import add_data_transaction_status
from database import add_data_promo_offers_transactions




def create(table):
    if table=='user_account':
        col1, col2 = st.columns(2)
        with col1:
            user_id = st.text_input("user_id:")
            fname = st.text_input("fname:")
            lname =  st.text_input("lname:")
            dob =  st.text_input("dob:")
            phone =  st.text_input("phone:")

        with col2:
            email = st.text_input("email:")
            country = st.text_input("country:")
            city = st.text_input("city:")
            pincode= st.text_input("pincode:")
            bank_name = st.text_input("bank_name:")


        if st.button("Add data"):
            add_data_user_account(user_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name)
            st.success("Successfully booked : {}".format(user_id))

    elif table=='wallet':
        col1, col2 = st.columns(2)
        with col1:
            t_id = st.text_input("t_id:")
            user_id = st.text_input("user_id:")
            account_no =  st.text_input("account_no:")
            bank_name = st.text_input("bank_name:")

        with col2:
            balance = st.text_input("balance:")
            promocode = st.text_input("promocode:")
            loan = st.text_input("loan:")
        if st.button("Add data"):
            add_data_wallet(t_id,user_id,account_no, bank_name,balance,promocode,loan)
            st.success("Successfully added : {}".format(t_id))

    elif table == 'promo_offers_transactions':
        col1, col2 = st.columns(2)
        with col1:
            prom_id = st.text_input("prom_id:")
            usr_id = st.text_input("usr_id:")
            transactions_no = st.text_input("transactions_no:")
        with col2:
            duration = st.text_input("duration:")
            amount_value = st.text_input("amount_value:")

        if st.button("Add data"):
            add_data_promo_offers_transactions(prom_id,usr_id,transactions_no,duration,amount_value)
            st.success("Successfully added : {}".format(prom_id))


    elif table == 'transactions':
        col1, col2 = st.columns(2)
        with col1:
            transaction_id = st.text_input("transaction_id:")
            transaction_date = st.text_input("transaction_date:")
            transaction_detail = st.text_input("transaction_detail:")
            amount = st.text_input("amount:")
            
        with col2:
            to_id = st.text_input("to_id:")
            from_id = st.text_input("from_id:")
            type_trans = st.text_input("type_trans:")

        if st.button("Add data"):
            add_data_transactions(transaction_id, transaction_date,transaction_detail, amount,to_id,from_id,type_trans)
            st.success("Successfully added : {}".format(transaction_id))


    elif table == 'promo_offers':
        col1, col2 = st.columns(2)
        with col1:
            promo_id = st.text_input("promo_id:")
            user_id = st.text_input("user_id:")
            start_date = st.text_input("start_date:")
            end_date = st.text_input("end_date:")
        with col2:
            duration = st.text_input("duration:")
            status = st.text_input("status:")
            amount_value = st.text_input("amount_value:")

        if st.button("Add data"):
            add_data_promo_offers(promo_id,user_id,start_date,end_date,duration,status, amount_value)
            st.success("Successfully added : {}".format(promo_id))


    elif table == 'dependents':
        col1, col2 = st.columns(2)
        with col1:
            dependent_id = st.text_input("dependent_id:")
            trans_id = st.text_input("trans_id:")
            user_ref_id = st.text_input("user_ref_id:")
            fname = st.text_input("fname:")
            lname = st.text_input("lname:")
        with col2:
            phone = st.text_input("phone:")
            email = st.text_input("email:")
            dob = st.text_input("dob:")
            relation = st.text_input("relation:")

        if st.button("Add data"):
            add_data_dependents(dependent_id,trans_id,user_ref_id,fname,lname,phone,email,dob,relation)
            st.success("Successfully added : {}".format(dependent_id))

    elif table == 'transaction_status':
        col1, col2 = st.columns(2)
        with col1:
            trans_id = st.text_input("trans_id:")
            u_id = st.text_input("uid:")
            status = st.text_input("status:")

        if st.button("Add data"):
            add_data_transaction_status(trans_id,u_id,status)
            st.success("Successfully added : {}".format(trans_id))


    
