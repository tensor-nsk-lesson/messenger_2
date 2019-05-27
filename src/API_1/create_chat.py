from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Создание чата
@app.route("/chat", methods=['POST'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    name_chat = request.form['name_chat']
    user_id = request.form['user_id']
    permission_id = request.form['permission_id']
    cursor.execute("SELECT count(*) FROM \"Chat\"")
    for table in cursor.fetchone():
        num = table[0] + 1
        num = str(num)
    cursor.execute("INSERT INTO \"Chat\" (id_chat, name_chat, id_user, id_permission)" 
                   "VALUES(" + num + ", " + name_chat + ", " + user_id + ", " + permission_id + " );")
    cursor.close()
    connect.commit()
    connect.close()

if __name__ == "__main__":
    app.run()
