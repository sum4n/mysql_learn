import mysql.connector


def connect_to_database(hostname, username, password, dbname):
    global host1, user1, pass1, dbname1
    host1 = hostname
    user1 = username
    pass1 = password
    dbname1 = dbname
    con1 = mysql.connector.connect(
	host = host1,
	user = user1,
	passwd = pass1,
	database = dbname1
	)
    con1.close()

def back_conn(host1, user1, pass1, dbname1):
    global con
    con = mysql.connector.connect(
        host = host1,
        user = user1,
        passwd = pass1,
        database = dbname1
        )

#=====================================================================
def close_win(window):  # to close pet and transaction windows
    window.destroy()

#=================================================================
def viewDataAll():
    back_conn(host1, user1, pass1, dbname1)
    cur=con.cursor()
    cur.execute("SELECT ti.tran_id, ti.tran_date, ti.customer_name, \
                ti.quantity, ti.total_price, pi.pet_id, pi.pet_type, pi.pet_subtype,\
                pi.num_in_stock, pi.num_sold, pi.price\
                FROM pet_info pi\
                LEFT JOIN transaction_info ti\
                ON pi.pet_id = ti.pet_id")
    rows = cur.fetchall()
    con.close()
    return rows

#==============Functions for Both Table Queries================
def viewData(table):
    back_conn(host1, user1, pass1, dbname1)
    cur=con.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(table, col_id, id):
    back_conn(host1, user1, pass1, dbname1)
    cur=con.cursor()
    cur.execute(f"DELETE FROM {table} WHERE {col_id}={id}")
    con.commit()
    con.close()
#==========Pet Table=================================
def addPetRec(pet_type, pet_subtype, num_in_stock, num_sold, price):
    back_conn(host1, user1, pass1, dbname1)
    cur=con.cursor()
    cur.execute("INSERT INTO pet_info (pet_type, pet_subtype, num_in_stock, num_sold, price) VALUES (%s, %s, %s, %s, %s)", \
                (pet_type, pet_subtype, num_in_stock, num_sold, price))
    con.commit()
    con.close()


def searchData(pet_type='', pet_subtype='', num_in_stock='', num_sold='', price=''):
    back_conn(host1, user1, pass1, dbname1)
    cur = con.cursor()

    if num_sold != '':
        cur.execute("SELECT * FROM pet_info WHERE num_sold=%s AND pet_type=%s OR pet_subtype=%s OR price=%s ", \
                (num_sold, pet_type, pet_subtype, price))
    elif num_in_stock != '':
        cur.execute("SELECT * FROM pet_info WHERE  num_in_stock=%s AND pet_type=%s OR pet_subtype=%s OR price=%s", \
                (num_in_stock, pet_type, pet_subtype, price))
    elif num_sold and num_in_stock != '':
        cur.execute("SELECT * FROM pet_info WHERE num_in_stock=%s OR num_sold=%s AND pet_type=%s OR pet_subtype=%s OR price=%s ", \
                (num_in_stock, num_sold, pet_type, pet_subtype, price))
    else:
        cur.execute("SELECT * FROM pet_info WHERE pet_type=%s OR pet_subtype=%s OR price=%s", \
                (pet_type, pet_subtype, price))
        
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(p_id, pet_type='', pet_subtype='', num_in_stock='', num_sold='', price=''):
    back_conn(host1, user1, pass1, dbname1)
    cur = con.cursor()
    cur.execute("UPDATE pet_info SET pet_type=%s, pet_subtype=%s, num_in_stock=%s, num_sold=%s, price=%s WHERE pet_id=%s", \
                (pet_type, pet_subtype, num_in_stock, num_sold, price, p_id))
    con.commit()
    con.close()
    
#==========Transactions Table=================================
def addTranRec(tran_date, customer_name, pet_id, quantity, total_price):
    back_conn(host1, user1, pass1, dbname1)
    cur=con.cursor()
    cur.execute("INSERT INTO transaction_info (tran_date, customer_name, pet_id, quantity, total_price) VALUES (%s, %s, %s, %s, %s)", \
                (tran_date, customer_name, pet_id, quantity, total_price))
    con.commit()
    con.close()

def searchTranData(tran_date='', customer_name='', pet_id='', quantity='', total_price=''):
    back_conn(host1, user1, pass1, dbname1)
    cur = con.cursor()
    cur.execute("SELECT * FROM transaction_info WHERE tran_date=%s OR customer_name=%s OR pet_id=%s OR quantity=%s OR total_price=%s", \
                (tran_date, customer_name, pet_id, quantity, total_price))     
    rows = cur.fetchall()
    con.close()
    return rows

def tran_dataUpdate(t_id, tran_date='', customer_name='', pet_id='', quantity='', total_price=''):
    back_conn(host1, user1, pass1, dbname1)
    cur = con.cursor()
    cur.execute("UPDATE transaction_info SET tran_date=%s, customer_name=%s, pet_id=%s, quantity=%s, total_price=%s WHERE tran_id=%s", \
                (tran_date, customer_name, pet_id, quantity, total_price, t_id))
    con.commit()
    con.close()

    




