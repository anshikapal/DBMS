import datetime

import pandas as pd
import streamlit as st
from database import view_all_user_account
from database import view_all_wallet
from database import view_all_data_transactions
from database import view_all_data_promo_offers
from database import view_all_data_dependents
from database import view_all_data_transaction_status
from database import view_all_data_promo_offers_transactions

from database import view_only_user_account
from database import view_only_wallet
from database import view_only_data_transactions
from database import view_only_data_promo_offers
from database import view_only_data_dependents
from database import view_only_data_transaction_status
from database import view_only_data_promo_offers_transactions

from database import get_user_id
from database import get_tid
from database import get_transaction_id
from database import get_promo_id
from database import get_dependent_id
from database import get_trans_id
from database import get_prom_id

from database import edit_user_account_data
from database import edit_wallet_data
from database import edit_transactions_data
from database import edit_promo_offers_data
from database import edit_dependents_data
from database import edit_transaction_status_data
from database import edit_promo_offers_transactions_data





def update(table):
    if table=='user_account':
        result = view_all_user_account()
        # st.write(result)
        df = pd.DataFrame(result, columns=['user_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name'])
        with st.expander("Current user_accounts"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_user_account()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_user_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            user_id = selected_result[0][0]
            fname = selected_result[0][1]
            lname = selected_result[0][2]
            dob = selected_result[0][3]
            phone = selected_result[0][4]
            email = selected_result[0][5]
            country = selected_result[0][6]
            city = selected_result[0][7]
            pincode = selected_result[0][8]
            bank_name = selected_result[0][9]
            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_user_id = st.text_input("user_id:",user_id)
                new_fname = st.text_input("fname:", fname)
                new_lname = st.text_input("lname:", lname)
                new_dob = st.text_input("dob:", dob)
            with col2:
                new_phone = st.text_input("phone:",phone)
                new_email = st.text_input("email:",email)
                new_country = st.text_input("city:",country)
                new_city = st.text_input("city:",city)
                new_pincode = st.text_input("pincode:",pincode)
                new_bank_name = st.text_input("bank_name:",bank_name)
            if st.button("Update user_account"):
                edit_user_account_data(new_user_id,new_fname,new_lname ,new_dob ,new_phone ,new_email ,new_country ,new_city ,new_pincode,new_bank_name,user_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name)
                st.success("Successfully updated:: {} to ::{}".format(user_id, new_user_id))

        result2 = view_all_user_account()
        df2 = pd.DataFrame(result2, columns=['user_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='wallet':
        result = view_all_wallet()
        # st.write(result)
        df = pd.DataFrame(result, columns=['t_id','user_id','account_no', 'bank_name','balance','promocode','loan'])
        with st.expander("Current wallets"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_wallet()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_tid(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            t_id = selected_result[0][0]
            user_id = selected_result[0][1]
            account_no = selected_result[0][2]
            bank_name = selected_result[0][3]
            balance = selected_result[0][4]
            promocode = selected_result[0][5]
            loan = selected_result[0][6]
            

            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_t_id = st.text_input("t_id:",t_id)
                new_user_id = st.text_input("user_id:", user_id)
                new_account_no = st.text_input("account_no:", account_no)
                new_bank_name = st.text_input("bank_name:", bank_name)
            with col2:
                new_balance = st.text_input("balance:",balance)
                new_promocode = st.text_input("promocode:",promocode)
                new_loan = st.text_input("loan:",loan)
                
            if st.button("Update book"):
                edit_wallet_data(new_t_id,new_user_id,new_account_no, new_bank_name,new_balance,new_promocode,new_loan,t_id,user_id,account_no, bank_name,balance,promocode,loan)
                st.success("Successfully updated:: {} to ::{}".format(t_id, new_t_id))

        result2 = view_all_wallet()
        df2 = pd.DataFrame(result2, columns=['tid','user_id','account_no', 'bank_name','balance','promocode','loan'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='promo_offers_transactions':
        result = view_all_data_promo_offers_transactions()
        # st.write(result)
        df = pd.DataFrame(result, columns=['prom_id','usr_id','transactions_no','duration','amount_value'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_promo_offers_transactions()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_prom_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            prom_id = selected_result[0][0]
            usr_id = selected_result[0][1]
            transactions_no = selected_result[0][2]
            duration = selected_result[0][3]
            amount_value = selected_result[0][4]
            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_prom_id = st.text_input("prom_id:",prom_id)
                new_usr_id = st.text_input("usr_id:", usr_id)
                new_transactions_no = st.text_input("transactions_no:", transactions_no)
                
            with col2:
                new_duration = st.text_input("duration:",duration)
                new_amount_value = st.text_input("amount_value:",amount_value)
            if st.button("Update book"):
                edit_promo_offers_transactions_data(new_prom_id,new_usr_id,new_transactions_no,new_duration,new_amount_value,prom_id,usr_id,transactions_no,duration,amount_value)
                st.success("Successfully updated:: {} to ::{}".format(prom_id, new_prom_id))

        result2 = view_all_data_promo_offers_transactions()
        df2 = pd.DataFrame(result2, columns=['prom_id','usr_id','transactions_no','duration', 'amount_value'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='transactions':
        result = view_all_data_transactions()
        # st.write(result)
        df = pd.DataFrame(result, columns=['transaction_id', 'transaction_date','transaction_detail', 'amount','to_id','from_id','type_trans'])
        with st.expander("Current transactions"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_transactions()]
        selected_dealer = st.selectbox("transactions to Edit", list_of_dealers)
        selected_result = get_transaction_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            transaction_id = selected_result[0][0]
            transaction_date = selected_result[0][1]
            transaction_detail = selected_result[0][2]
            amount = selected_result[0][3]
            to_id = selected_result[0][4]
            from_id = selected_result[0][5]
            type_trans = selected_result[0][6]
            
            # Layout of Create

            col1, col2 = st.columns(2)
            with col1:
                new_transaction_id = st.text_input("transaction_id:",transaction_id)
                new_transaction_date = st.text_input("transaction_date:", transaction_date)
                new_transaction_detail = st.text_input("transaction_detail:", transaction_detail)
                new_amount = st.text_input("amount:", amount)
            with col2:
                new_to_id = st.text_input("to_id:",to_id)
                new_from_id = st.text_input("from_id:",from_id)
                new_type_trans = st.text_input("type_trans:",type_trans)
                
            if st.button("Update book"):
                edit_transactions_data(new_transaction_id, new_transaction_date,new_transaction_detail, new_amount,new_to_id,new_from_id,new_type_trans,transaction_id, transaction_date,transaction_detail, amount,to_id,from_id,type_trans)
                st.success("Successfully updated:: {} to ::{}".format(transaction_id, new_transaction_id))

        result2 = view_all_data_transactions()
        df2 = pd.DataFrame(result2, columns=['transaction_id', 'transaction_date','transaction_detail', 'amount','to_id','from_id','type_trans'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='promo_offers':
        result = view_all_data_promo_offers()
        # st.write(result)
        df = pd.DataFrame(result, columns=['promo_id','user_id','start_date','end_date','duration','status', 'amount_value'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_promo_offers()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_promo_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            promo_id = selected_result[0][0]
            user_id = selected_result[0][1]
            start_date = selected_result[0][2]
            end_date = selected_result[0][3]
            duration = selected_result[0][4]
            status = selected_result[0][5]
            amount_value = selected_result[0][6]
            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_promo_id = st.text_input("promo_id:",promo_id)
                new_user_id = st.text_input("user_id:", user_id)
                new_start_date = st.text_input("start_date:", start_date)
                
            with col2:
                new_end_date = st.text_input("end_date:", end_date)
                new_duration = st.text_input("duration:",duration)
                new_status = st.text_input("status:",status)
                new_amount_value = st.text_input("amount_value:",amount_value)
            if st.button("Update book"):
                edit_promo_offers_data(new_promo_id,new_user_id,new_start_date,new_end_date,new_duration,new_status, new_amount_value,promo_id,user_id,start_date,end_date,duration,status, amount_value)
                st.success("Successfully updated:: {} to ::{}".format(promo_id, new_promo_id))

        result2 = view_all_data_promo_offers()
        df2 = pd.DataFrame(result2, columns=['promo_id','user_id','start_date','end_date','duration','status', 'amount_value'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='dependents':
        result = view_all_data_dependents()
        # st.write(result)
        df = pd.DataFrame(result, columns=['dependent_id','trans_id','user_ref_id','fname','lname','phone' ,'email' ,'dob','relation'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_dependents()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_dependent_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            dependent_id = selected_result[0][0]
            trans_id = selected_result[0][1]
            user_ref_id = selected_result[0][2]
            fname = selected_result[0][3]
            lname = selected_result[0][4]
            phone = selected_result[0][5]
            email = selected_result[0][6]
            dob = selected_result[0][7]
            relation = selected_result[0][8]


            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_dependent_id = st.text_input("dependent_id:",dependent_id)
                new_trans_id = st.text_input("trans_id:", trans_id)
                new_user_ref_id = st.text_input("user_ref_id:", user_ref_id)
                new_fname = st.text_input("fname:", fname)
            with col2:
                new_lname = st.text_input("lname:",lname)
                new_phone = st.text_input("phone:",phone)
                new_email = st.text_input("email:",email)
                new_dob = st.text_input("dob:",dob)
                new_relation = st.text_input("relation:",relation)
            if st.button("Update book"):
                edit_dependents_data(new_dependent_id,new_trans_id,new_user_ref_id,new_fname,new_lname,new_phone,new_email,new_dob,new_relation,dependent_id,trans_id,user_ref_id,fname,lname,phone,email,dob,relation)
                st.success("Successfully updated:: {} to ::{}".format(dependent_id, new_dependent_id))

        result2 = view_all_data_dependents()
        df2 = pd.DataFrame(result2, columns=['dependent_id','trans_id','user_ref_id','fname','lname','phone' ,'email' ,'dob','relation'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='transaction_status':
        result = view_all_data_transaction_status()
        # st.write(result)
        df = pd.DataFrame(result, columns=['trans_id','u_id','status'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_transaction_status()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_trans_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            trans_id = selected_result[0][0]
            u_id = selected_result[0][1]
            status = selected_result[0][2]

            # Layout of Create

            col1, col2 = st.columns(2)
            with col1:
                new_trans_id = st.text_input("trans_id:",trans_id)
                new_u_id = st.text_input("u_id:",u_id)
                
            with col2:
                new_status = st.text_input("status:",status)

                
            if st.button("Update book"):
                edit_transaction_status_data(new_trans_id,new_u_id,new_status,trans_id,u_id,status)
                st.success("Successfully updated:: {} to ::{}".format(trans_id, new_trans_id))

        result2 = view_all_data_transaction_status()
        df2 = pd.DataFrame(result2, columns=['trans_id','u_id','status'])
        with st.expander("Updated data"):
            st.dataframe(df2)

