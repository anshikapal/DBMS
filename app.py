# Importing pakages
import streamlit as st
import mysql.connector
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from function import loan_1
from join import join
from aggregate import agg
from queries import execute_query
#from procedure import info_1

mydb = mysql.connector.connect(
host="localhost",
user="root"
)
c = mydb.cursor()

# c.execute("CREATE DATABASE pes1ug20cs062_final_project")
c.execute("use pes1ug20cs062_final_project")

def main():
    st.title("VIRTUAL MONEY TRANSFER")
    menu = ["Add", "View", "Edit", "Remove","Function","Join","Aggregate","Query"]
    table_names=["user_account","wallet","promo_offers_transactions","transactions","promo_offers","dependents","transaction_status"]
    choice = st.sidebar.selectbox("action", menu)
    table=st.sidebar.selectbox("table", table_names)
    create_table(table)
    if choice == "Add":
        if table=='user_account':
            st.subheader("Enter user_account Details:")
            create(table)
        elif table=='wallet':
            st.subheader("Enter wallet Details:")
            create(table)
        elif table=='promo_offers_transactions':
            st.subheader("Enter promo_offers Details:")
            create(table)
        elif table=='transactions':
            st.subheader("Enter transactions Details:")
            create(table)
        elif table=='promo_offers':
            st.subheader("Enter promo_offers Details:")
            create(table)
        elif table=='dependents':
            st.subheader("Enter dependents Details:")
            create(table)
        elif table=='transaction_status':
            st.subheader("Enter transaction_status Details:")
            create(table)


    if choice == "View":
        if table=='user_account':
            st.subheader("View entered user_account Details:")
            read(table)
        elif table=='wallet':
            st.subheader("View entered wallet Details:")
            read(table)
        elif table=='promo_offers_transactions':
            st.subheader("View promo_offers Details:")
            read(table)
        elif table=='transactions':
            st.subheader("View entered transactions Details:")
            read(table)
        elif table=='promo_offers':
            st.subheader("View entered promo_offers Details:")
            read(table)
        elif table=='dependents':
            st.subheader("View entered dependents Details:")
            read(table)
        elif table=='transaction_status':
            st.subheader("View entered transaction_status Details:")
            read(table)
    
    if choice == "Remove":
        if table=='user_account':
            st.subheader("Delete enetered user_account Details:")
            delete(table)
        elif table=='wallet':
            st.subheader("Delete entered wallet Details:")
            delete(table)
        elif table=='promo_offers_transactions':
            st.subheader("Delete promo_offers_transactions:")
            delete(table)
        elif table=='transactions':
            st.subheader("Delete entered transactions Details:")
            delete(table)
        elif table=='promo_offers':
            st.subheader("Delete entered promo_offers Details:")
            delete(table)
        elif table=='dependents':
            st.subheader("Delete entered dependents Details:")
            delete(table)
        elif table=='transaction_status':
            st.subheader("Delete entered transaction_status Details:")
            delete(table)

    if choice == "Edit":
        if table=='user_account':
            st.subheader("Update entered user_account Details:")
            update(table)
        elif table=='wallet':
            st.subheader("Update entered wallet Details:")
            update(table)
        elif table=='promo_offers_transactions':
            st.subheader("Update entered promo_offers_transactions Details:")
            update(table)
        elif table=='transactions':
            st.subheader("Update entered transactions Details:")
            update(table)
        elif table=='promo_offers':
            st.subheader("Update entered promo_offers Details:")
            update(table)
        elif table=='dependents':
            st.subheader("Update entered dependents Details:")
            update(table)
        elif table=='transaction_status':
            st.subheader("Update entered transaction_status Details:")
            update(table)

    

    if choice=='Function':
        st.subheader("CAN YOU APPLY FOR LOAN?")
        loan_1()
    
    if choice=='Join':
        st.subheader("join:")
        join()

    if choice=='Aggregate':
        st.subheader("Aggregate:")
        agg()

    if choice=='Query':
        st.subheader("Enter QUERY:")
        execute_query()

    #if choice=='Procedure':
    #    st.subheader("Information about customer:")
    #    info_1()
    

    




if __name__ == '__main__':
    main()