from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Авторизация
@app.route("/chat", methonds=['POST'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    chat_id = request.form['chat_id']
    user_id = request.form['user_id']
    cursor.execute("SELECT count(*) FROM \"Message\"")
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    cursor.execute("INSERT INTO \"Message\" (id_message, id_chat, id_user, time, id_status, del_mes)" 
                   "VALUES(" + num + ", " + chat_id + ", " + user_id + ", now(), '0', '0');")
    cursor.close()
    connect.commit()
    connect.close()

if __name__ == "__main__":
    app.run()
