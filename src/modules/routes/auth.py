from flask import Flask, request
from database import sql_execute

@auth.route("/signup", methods=['POST'])
def signup():
    cursor.execute("SELECT count(*) FROM \"User\"")
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    age = request.form['age']
    username = request.form['username']
    cursor.execute("INSERT INTO \"User\" ( id_user, age, user_name, avatar, visit_time, status_user)"
                   "VALUES(" + num + "," + age + "," + username + " , 'default', now(),'1');")
    user_number = request.form['user_number']
    password = request.form['password']
    cursor.execute("INSERT INTO \"Authorization\" (id_auth, id_user, user_number, password)" 
                   "VALUES(" + num + "," + user_number + "," + password + ") "
                                                                          "SELECT 'id_user' FROM \"User\" "
                                                                          "WHERE id_user = " + num + ";")
    return {'status':1}

@auth.route("/", methods=['POST'])
def login():
    number = request.form['number']
    password = request.form['password']
    cursor.execute("SELECT * FOR \"Authorization\" WHERE 'user_number' = " + number + ";")
    mes = ''
    for table in cursor.fetchone():
        if table[2] == number and table[3] == password:
            return {'status':1}
    return 'login or password is not found'

