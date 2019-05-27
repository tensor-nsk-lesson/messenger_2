from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Создание контакта
@app.route("/chat", methonds=['POST'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    id_cont = request.form['user_id_cont']
    user_id_cont = request.form['user_id_cont']
    user_id = request.form['user_id']
    cursor.execute("UPDATE \"Contact\" SET 'cont_status' WHERE 'id_cont' = " + id_cont + ";")
    cursor.execute("SELECT count(*) FROM \"Contact\"")
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    cursor.execute("INSERT INTO \"Contact\" (id_cont, id_user, id_user_cont, cont_status)" 
                   "VALUES(" + num + ", " + user_id + ", " + user_id_cont + ",'1');")
    cursor.close()
    connect.commit()
    connect.close()

if __name__ == "__main__":
    app.run()
