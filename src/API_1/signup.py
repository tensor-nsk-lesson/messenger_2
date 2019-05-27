from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Регистрация
@app.route("/signup", methonds=['POST'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    cursor.execute("SELECT count(*) FROM \"User\"")
    for table in cursor.fetchall():
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
    cursor.close()
    connect.commit()
    connect.close()
    return 'Succesfully'

if __name__ == "__main__":
    app.run()
