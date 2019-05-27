from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Получение одного контакта
@app.route("/contacts", methonds=['GET'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    user_id = request.form['user_id']
    cont_id = request.form['cont_id']
    cursor.execute("SELECT * FOR \"Contact\" WHERE 'id_user' = " + user_id + " AND 'id_user_cont' = " + cont_id + ";")
    mes = ''
    for table in cursor.fetchone():
        mes += table.__str__() + "<br>"
    cursor.close()
    connect.commit()
    connect.close()
    return mes

if __name__ == "__main__":
    app.run()
