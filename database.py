# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pes1ug20cs062_final_project"
)
c = mydb.cursor()


def create_table(table):
    if table=='uder_account':
        c.execute('CREATE TABLE IF NOT EXISTS user_account(user_id TEXT,fname TEXT,lname TEXT,dob TEXT,phone TEXT,email TEXT,country TEXT,city TEXT,pincode TEXT,bank_name TEXT)')
    elif table=='wallet':
        c.execute('CREATE TABLE IF NOT EXISTS wallet(t_id TEXT ,user_id TEXT,account_no TEXT, bank_name TEXT,balance TEXT,promocode TEXT,loan TEXT)')
    elif table=='transactions':
        c.execute('CREATE TABLE IF NOT EXISTS transactions(transaction_id TEXT, transaction_date TEXT,transaction_detail TEXT, amount TEXT,to_id TEXT,from_id TEXT,type_trans TEXT)')
    elif table=='promo_offers':
        c.execute('CREATE TABLE IF NOT EXISTS promo_offers(promo_id TEXT,user_id TEXT,start_date TEXT,end_date TEXT,duration TEXT,status TEXT, amount_value TEXT)')
    elif table=='dependents':
        c.execute('CREATE TABLE IF NOT EXISTS dependents(dependent_id TEXT,trans_id TEXT,user_ref_id TEXT,fname TEXT,lname TEXT,phone TEXT,email TEXT,dob TEXT,relation TEXT)')
    elif table=='transaction_status':
        c.execute('CREATE TABLE IF NOT EXISTS transaction_status(trans_id TEXT,u_id TEXT,status TEXT)')


def add_data_user_account(user_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name):
        c.execute('INSERT INTO user_account(user_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                  (user_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name))
        mydb.commit()

def add_data_wallet(t_id,user_id,account_no, bank_name,balance,promocode,loan):
        c.execute('INSERT INTO wallet(t_id,user_id,account_no, bank_name,balance,promocode,loan) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                  (t_id,user_id,account_no, bank_name,balance,promocode,loan))
        mydb.commit()

def add_data_promo_offers_transactions(prom_id,usr_id,transactions_no,duration,amount_value):
        c.execute('INSERT INTO promo_offers_transactions(prom_id,usr_id,transactions_no,duration,amount_value) VALUES (%s,%s,%s,%s,%s)',
                  (prom_id,usr_id,transactions_no,duration,amount_value))
        mydb.commit()


def add_data_transactions(transaction_id, transaction_date,transaction_detail, amount,to_id,from_id,type_trans):
        c.execute('INSERT INTO transactions(transaction_id, transaction_date,transaction_detail, amount,to_id,from_id,type_trans) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                  (transaction_id, transaction_date,transaction_detail, amount,to_id,from_id,type_trans))
        mydb.commit()


def add_data_promo_offers(promo_id,user_id,start_date,end_date,duration,status, amount_value):
        c.execute('INSERT INTO promo_offers(promo_id,user_id,start_date,end_date,duration,status, amount_value) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                  (promo_id,user_id,start_date,end_date,duration,status, amount_value))
        mydb.commit()


def add_data_dependents(dependent_id,trans_id,user_ref_id,fname,lname,phone ,email ,dob,relation):
        c.execute('INSERT INTO dependents(dependent_id,trans_id,user_ref_id,fname,lname,phone ,email ,dob,relation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                  (dependent_id,trans_id,user_ref_id,fname,lname,phone ,email ,dob,relation))
        mydb.commit()


def add_data_transaction_status(trans_id,u_id,status):
        c.execute('INSERT INTO transaction_status(trans_id,u_id,status) VALUES (%s,%s,%s)',
                  (trans_id,u_id,status))
        mydb.commit()

#view tables
def view_all_user_account():
    c.execute('SELECT * FROM user_account')
    data = c.fetchall()
    return data
def view_all_wallet():
    c.execute('SELECT * FROM wallet')
    data = c.fetchall()
    return data
def view_all_data_promo_offers_transactions():
    c.execute('SELECT * FROM promo_offers_transactions')
    data = c.fetchall()
    return data
def view_all_data_transactions():
    c.execute('SELECT * FROM transactions')
    data = c.fetchall()
    return data
def view_all_data_promo_offers():
    c.execute('SELECT * FROM promo_offers')
    data = c.fetchall()
    return data
def view_all_data_dependents():
    c.execute('SELECT * FROM dependents')
    data = c.fetchall()
    return data
def view_all_data_transaction_status():
    c.execute('SELECT * FROM transaction_status')
    data = c.fetchall()
    return data




#viewonly tables
def view_only_user_account():
    c.execute('SELECT user_id FROM user_account')
    data = c.fetchall()
    return data
def view_only_wallet():
    c.execute('SELECT t_id FROM wallet')
    data = c.fetchall()
    return data
def view_only_data_promo_offers_transactions():
    c.execute('SELECT prom_id FROM promo_offers_transactions')
    data = c.fetchall()
    return data
def view_only_data_transactions():
    c.execute('SELECT transaction_id FROM transactions')
    data = c.fetchall()
    return data
def view_only_data_promo_offers():
    c.execute('SELECT promo_id FROM promo_offers')
    data = c.fetchall()
    return data
def view_only_data_dependents():
    c.execute('SELECT dependent_id FROM dependents')
    data = c.fetchall()
    return data
def view_only_data_transaction_status():
    c.execute('SELECT trans_id FROM transaction_status')
    data = c.fetchall()
    return data


#getting
def get_user_id(user_id):
    c.execute('SELECT * FROM user_account WHERE user_id="{}"'.format(user_id))
    data = c.fetchall()
    return data
def get_tid(t_id):
    c.execute('SELECT * FROM wallet WHERE t_id="{}"'.format(t_id))
    data = c.fetchall()
    return data

def get_prom_id(prom_id):
    c.execute('SELECT * FROM promo_offers_transactions WHERE prom_id="{}"'.format(prom_id))
    data = c.fetchall()
    return data

def get_transaction_id(transaction_id):
    c.execute('SELECT * FROM transactions WHERE transaction_id="{}"'.format(transaction_id))
    data = c.fetchall()
    return data

def get_promo_id(promo_id):
    c.execute('SELECT * FROM promo_offers WHERE promo_id="{}"'.format(promo_id))
    data = c.fetchall()
    return data

def get_dependent_id(dependent_id):
    c.execute('SELECT * FROM dependents WHERE dependent_id="{}"'.format(dependent_id))
    data = c.fetchall()
    return data

def get_trans_id(trans_id):
    c.execute('SELECT * FROM transaction_status WHERE trans_id="{}"'.format(trans_id))
    data = c.fetchall()
    return data


#editig
def edit_user_account_data(new_user_id,new_fname,new_lname ,new_dob ,new_phone ,new_email ,new_country ,new_city ,new_pincode,new_bank_name,user_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name):
    c.execute("UPDATE user_account SET user_id=%s,fname=%s, lname=%s, dob=%s, phone=%s,email=%s,country=%s,city=%s,pincode=%s,bank_name=%s WHERE "
              "user_id=%s and fname=%s and lname=%s and dob=%s and phone=%s and email=%s and country=%s and city=%s and pincode=%s and bank_name=%s",(new_user_id,new_fname,new_lname ,new_dob ,new_phone ,new_email ,new_country ,new_city ,new_pincode,new_bank_name,user_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_wallet_data(new_t_id,new_user_id,new_account_no, new_bank_name,new_balance,new_promocode,new_loan,t_id,user_id,account_no, bank_name,balance,promocode,loan):
    c.execute("UPDATE wallet SET t_id=%s, user_id=%s, account_no=%s, bank_name=%s,balance=%s,promocode=%s,loan=%s WHERE "
              "t_id=%s and user_id=%s and account_no=%s and bank_name=%s and balance=%s and promocode=%s and loan=%s", (new_t_id,new_user_id,new_account_no, new_bank_name,new_balance,new_promocode,new_loan,t_id,user_id,account_no, bank_name,balance,promocode,loan))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_promo_offers_transactions_data(new_prom_id,new_usr_id,new_transactions_no,new_duration,new_amount_value,prom_id,usr_id,transactions_no,duration,amount_value):
    c.execute("UPDATE promo_offers_transactions SET prom_id=%s, usr_id=%s, transactions_no=%s,duration=%s,amount_value=%s WHERE "
              "prom_id=%s and usr_id=%s and transactions_no=%s and duration=%s and amount_value=%s  ", (new_prom_id,new_usr_id,new_transactions_no,new_duration,new_amount_value,prom_id,usr_id,transactions_no,duration,amount_value))
    mydb.commit()
    data = c.fetchall()
    return data


def edit_transactions_data(new_transaction_id, new_transaction_date,new_transaction_detail, new_amount,new_to_id,new_from_id,new_type_trans,transaction_id, transaction_date,transaction_detail, amount,to_id,from_id,type_trans):
    c.execute("UPDATE transactions SET transaction_id=%s, transaction_date=%s, transaction_detail=%s, amount=%s, to_id=%s, from_id=%s, type_trans=%s WHERE "
              "transaction_id=%s and transaction_date=%s and transaction_detail=%s and amount=%s and to_id=%s and from_id=%s and type_trans=%s ", (new_transaction_id, new_transaction_date,new_transaction_detail, new_amount,new_to_id,new_from_id,new_type_trans,transaction_id, transaction_date,transaction_detail, amount,to_id,from_id,type_trans))
    mydb.commit()
    data = c.fetchall()
    return data



def edit_promo_offers_data(new_promo_id,new_user_id,new_start_date,new_end_date,new_duration,new_status, new_amount_value,promo_id,user_id,start_date,end_date,duration,status, amount_value):
    c.execute("UPDATE promo_offers SET promo_id=%s, user_id=%s, start_date=%s,end_date=%s, duration=%s, status=%s, amount_value=%s WHERE "
              "promo_id=%s and user_id=%s and start_date=%s and end_date=%s and duration=%s and status=%s and amount_value=%s  ", (new_promo_id,new_user_id,new_start_date,new_end_date,new_duration,new_status, new_amount_value,promo_id,user_id,start_date,end_date,duration,status, amount_value))
    mydb.commit()
    data = c.fetchall()
    return data



def edit_dependents_data(new_dependent_id,new_trans_id,new_user_ref_id,new_fname,new_lname,new_phone,new_email,new_dob,new_relation,dependent_id,trans_id,user_ref_id,fname,lname,phone,email,dob,relation):
    c.execute("UPDATE dependents SET dependent_id=%s, trans_id=%s, user_ref_id=%s, fname=%s,lname=%s, phone=%s, email=%s, dob=%s, relation=%s WHERE "
              "dependent_id=%s and trans_id=%s and user_ref_id=%s and fname=%s and lname=%s and phone=%s and email=%s and dob=%s and relation=%s ", (new_dependent_id,new_trans_id,new_user_ref_id,new_fname,new_lname,new_phone,new_email,new_dob,new_relation,dependent_id,trans_id,user_ref_id,fname,lname,phone,email,dob,relation))
    mydb.commit()
    data = c.fetchall()
    return data



def edit_transaction_status_data(new_trans_id,new_u_id,new_status,trans_id,u_id,status):
    c.execute("UPDATE transaction_status SET trans_id=%s, u_id=%s, status=%s WHERE "
              "trans_id=%s and u_id=%s and status=%s ", (new_trans_id,new_u_id,new_status,trans_id,u_id,status))
    mydb.commit()
    data = c.fetchall()
    return data



#delete
def delete_user_account(user_id):
    c.execute('DELETE FROM user_account WHERE user_id="{}"'.format(user_id))
    mydb.commit()

def delete_wallet(t_id):
    c.execute('DELETE FROM wallet WHERE t_id="{}"'.format(t_id))
    mydb.commit()

def delete_promo_offers_trsansactions(prom_id):
    c.execute('DELETE FROM promo_offers_transactions WHERE prom_id="{}"'.format(prom_id))
    mydb.commit()

def delete_transactions(transaction_id):
    c.execute('DELETE FROM transactions WHERE transaction_id="{}"'.format(transaction_id))
    mydb.commit()
def delete_promo_offers(promo_id):
    c.execute('DELETE FROM promo_offers WHERE promo_id="{}"'.format(promo_id))
    mydb.commit()

def delete_dependents(dependent_id):
    c.execute('DELETE FROM dependents WHERE dependent_id="{}"'.format(dependent_id))
    mydb.commit()
def delete_transaction_status(trans_id):
    c.execute('DELETE FROM transaction_status WHERE trans_id="{}"'.format(trans_id))
    mydb.commit()


def loan(x):
    c.execute('SELECT loan({})'.format(x))
    data = c.fetchall()
    return data


def joining():
    c.execute('SELECT wallet.user_id, wallet.account_no, wallet.bank_name, transactions.transaction_detail FROM wallet JOIN transactions ON wallet.t_id = transactions.transaction_id;')
    data = c.fetchall()
    return data

def joining_2():
    c.execute('SELECT transactions.transaction_id, transaction_status.u_id,transactions.to_id, transactions.from_id, transaction_status.status FROM transactions JOIN transaction_status ON transaction_status.trans_id= transactions.transaction_id;')
    data = c.fetchall()
    return data

def joining_3():
    c.execute('SELECT transactions.transaction_id, transactions.type_trans,transactions.transaction_detail, dependents.dependent_id, dependents.relation FROM transactions JOIN dependents ON dependents.user_ref_id= transactions.transaction_id')
    data = c.fetchall()
    return data

def joining_4():
    c.execute('SELECT user_account.user_id, user_account.fname, user_account.lname, user_account.bank_name, wallet.balance, wallet.loan FROM user_account JOIN wallet ON user_account.user_id= wallet.user_id')
    data = c.fetchall()
    return data

def aggregate():
    c.execute('SELECT bank_name, COUNT(bank_name) FROM user_account GROUP BY bank_name;')
    data = c.fetchall()
    return data

def aggregate_2():
    c.execute('SELECT to_id, SUM(amount) FROM transactions GROUP BY to_id;')
    data = c.fetchall()
    return data

def aggregate_3():
    c.execute('SELECT bank_name, ROUND(AVG (BALANCE), 0) avg_balance FROM wallet GROUP BY bank name ORDER BY bank_name;')
    data = c.fetchall()
    return data

def aggregate_4():
    c.execute('SELECT user_account.fame, MAX(balance) highest_balance FROM user_account INNER JOIN wallet USING (user_id);')
    data = c.fetchall()
    return data

def query_1(x):
    c.execute(x)
    data = c.fetchall()
    return data






