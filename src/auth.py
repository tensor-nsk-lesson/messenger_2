from db import connect
import secrets


def authorization(user_number, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute('select "id_auth" from "Authorization" where "user_number" = \''+user_number.__str__()+'\' and "password" = '+password.__str__())
    user = cur.fetchone()
    if not user:
        data = {
            "Error":"Неверный логин или пароль"
        }
    else:
        data = {
            "id_user":user[0]
        }
    conn.close()
    return data


def signup(user_number, user_name, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute('insert into "Authorization" ("user_number","password")'
                ' values(\''+user_number.__str__()+'\', '+password.__str__()+') returning "id_user"');
    id = cur.fetchone();
    conn.commit()
    cur.execute('insert into "User" ("id_user", "user_name", "status_user")'
                ' values('+id[0].__str__()+',\''+user_name.__str__()+'\', 1)')
    conn.commit()
    conn.close()
    return
