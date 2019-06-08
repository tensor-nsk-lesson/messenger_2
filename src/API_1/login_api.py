from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Авторизация
@app.route("/login", methods=['POST','GET'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    number = request.form['number']
    password = request.form['password']
    cursor.execute("SELECT * FOR \"Authorization\" WHERE 'user_number' = " + number + ";")
    mes = ''
    for table in cursor.fetchone():
        if table[2] == number and table[3] == password:
            return 'Succesfully'
    cursor.close()
    connect.commit()
    connect.close()
    return 'login or password is not found'

if __name__ == "__main__":
    app.run()
