from flask import Flask, request, json
from database import sql_execute


@main.route("/contacts", methods=['POST'])
def create_contact():
    cursor.execute("SET search_path TO public")
    id_cont = request.form['user_id_cont']
    user_id_cont = request.form['user_id_cont']
    user_id = request.form['user_id']
    print (sql_execute("UPDATE \"Contact\" SET 'cont_status' = '0' WHERE 'id_cont' = " + id_cont + ";"))
    print (sql_execute("SELECT count(*) FROM \"Contact\""))
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    print (sql_execute("INSERT INTO \"Contact\" (id_cont, id_user, id_user_cont, cont_status)" 
                   "VALUES(" + num + ", " + user_id + ", " + user_id_cont + ",'1');"))

@main.route("/chat", methods=['POST'])
def create_chat():
    print (sql_execute("SET search_path TO public"))
    id_mess = request.form['id_mess']
    chat_id = request.form['chat_id']
    user_id = request.form['user_id']
    print (sql_execute("UPDATE \"Message\" SET 'del_mes' = '1' WHERE 'id_message' = " + id_mess + ";"))
    print (sql_execute("SELECT count(*) FROM \"Message\""))
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    print (sql_execute("INSERT INTO \"Message\" (id_message, id_chat, id_user, time, id_status, del_mes)" 
                   "VALUES(" + num + ", " + chat_id + ", " + user_id + ", now(),'0', '0');"))

@main.route("/chat", methods=['POST'])
def permission_chat():
    name_chat = request.form['name_chat']
    user_id = request.form['user_id']
    permission_id = request.form['permission_id']
    print (sql_execute("SELECT count(*) FROM \"Chat\""))
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    print (sql_execute("INSERT INTO \"Chat\" (id_chat, name_chat, id_user, id_permission)" 
                   "VALUES(" + num + ", " + name_chat + ", " + user_id + ", " + permission_id + " );"))

@main.route("/contacts", methods=['POST'])
def update_contact():
    user_id_cont = request.form['user_id_cont']
    user_id = request.form['user_id']
    print (sql_execute("SELECT count(*) FROM \"Contact\""))
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    print (sql_execute("INSERT INTO \"Contact\" (id_cont, id_user, id_user_cont, cont_status)" 
                   "VALUES(" + num + ", " + user_id + ", " + user_id_cont + ",'1');"))    

@main.route("/chat", methods=['POST'])
def Message():
    chat_id = request.form['chat_id']
    user_id = request.form['user_id']
    print (sql_execute("SELECT count(*) FROM \"Message\""))
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    print (sql_execute("INSERT INTO \"Message\" (id_message, id_chat, id_user, time, id_status, del_mes)" 
                   "VALUES(" + num + ", " + chat_id + ", " + user_id + ", now(),'0', '0');"))

@main.route("/contacts", methods=['PUT'])
def remove_contact():
id_cont = request.form['id_cont']
    print (sql_execute("UPDATE \"Contact\" SET 'cont_status' = '0' WHERE 'id_cont' = " + id_cont + ";"))

@main.route("/chat", methods=['PUT'])
def remove_message():
    id_mess = request.form['id_mess']
    print (sql_execute("UPDATE \"Contact\" SET 'del_mes' = '1' WHERE 'id_message' = " + id_mess + ";"))

@main.route("/contacts", methods=['GET'])
def get_contacts():
user_id = request.form['user_id']
    print (sql_execute("SELECT * FOR \"Contact\" WHERE 'id_user' = " + user_id + ";"))
    mes = ''
    for table in cursor.fetchall():
        mes += table.__str__() + "<br>"
    return mes

@main.route("/chat", methods=['GET'])
def get_messages():
    user_id = request.form['user_id']
    print (sql_execute("SELECT * FOR \"Message\" WHERE 'id_user' = " + user_id + ";"))
    mes = ''
    for table in cursor.fetchall():
        mes += table.__str__() + "<br>"
    return mes

@main.route("/chat", methods=['GET'])
def get_chats():
user_id = request.form['user_id']
    print (sql_execute("SELECT * FOR \"Chat\" WHERE 'id_user' = " + user_id + ";"))
    mes = ''
    for table in cursor.fetchall():
        mes += table.__str__() + "<br>"
    return mes

@main.route("/contacts", methods=['GET'])
def get_one_contact():
    user_id = request.form['user_id']
    cont_id = request.form['cont_id']
    print (sql_execute("SELECT * FOR \"Contact\" WHERE 'id_user' = " + user_id + " AND 'id_user_cont' = " + cont_id + ";"))
    mes = ''
    for table in cursor.fetchone():
        mes += table.__str__() + "<br>"
    return mes

@main.route("/chat", methods=['GET'])
def get_one_message():
    mes_id = request.form['mes_id']
    print (sql_execute("SELECT * FOR \"Message\" WHERE 'id_message' = " + mes_id + ";"))
    mes = ''
    for table in cursor.fetchone():
        mes = table.__str__() + "<br>"
    return mes

@app.route("/profile", methods=['GET'])
def profile():
    user_id = request.form['user_id']
    print (sql_execute("SELECT * FOR \"User\" WHERE 'id_user' = " + user_id + ";"))
    mes = ''
    for table in cursor.fetchone():
        mes = table.__str__() + "<br>"
    return mes
