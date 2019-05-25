from flask import Flask, request
import psycopg2

app = Flask(__name__)

# подключение к таблице
connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
cursor = connect.cursor()


def get_id_to_add_in(table):
    return len(cursor.execute('SELECT * FROM \"' + table + '\"').fetchall())


def get_hash(s):
    return s

# Вход в систему
@app.route("/login", methonds=['POST'])
def login():
    cursor.execute("SET search_path TO public")
    num = "89518074028"
    pas = "qwerty2"
    cursor.execute("SELECT * FROM \"Authorization\"")
    mes = ""
    for table in cursor.fetchall():
        if table[2] == pas and table[3] == num:
            return "Successfully"
    cursor.close()
    connect.close()
    return "Login or Password not found"


# регистрация
@app.route('/signup', methonds=['POST'])
def signup():
    cursor.execute('SET search_path TO public')
    num = request.form['num']
    cursor.execute('SELECT user_number \
                    FROM \"Authorization\" \
                    WHERE user_number \
                    LIKE ' + num)
    usr = cursor.fetchone()
    res = ''
    if usr is not None:
        res = 'denied'
    else:
        cursor.execute('INSERT INTO \"Authorization\" (id_user, user_number, password_user) \
                        VALUES (' + get_id_to_add_in('User') + ' ' + \
                                    num + ' \'' + \
                                    get_hash(request.form['password']) + '\'')
        res = 'ok'
    return res


if __name__ == "__main__":
    app.run()
