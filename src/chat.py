from db import connect
import random


def get_chats(id_user):
    conn = connect()
    cur = conn.cursor()
    cur.execute('select "id_chat", "name_chat" from "Chat" where "id_user" = '+id_user.__str__()+' ')
    rows = cur.fetchall()
    result = []
    for row in rows:
        data = {
            "id_chat": row[0],
            "name_chat": row[1]
        }
        result.append(data)
    conn.close()
    return result

def create_chat(id_user):
    conn = connect()
    cur = conn.cursor()
    number = random.randint(1, 100000).__str__()
    cur.execute('insert into "Chat" ("id_chat", "name_chat", "id_user", "id_permission") '
                'values('+number+','+name_chat.__str__()+', '+id_user.__str__
                +', 2 , \'Chat'+number+'\')'
                'returning "id_chat"')
    id_dialog = cur.fetchone()
    conn.commit()
    conn.close()
    result = {
        "id_chat": id_chat[0]
    }
    return result

def del_mes(id_chat, id_message, id_user):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        'update from "Messages" set "del_mes"= 1 where "id_chat" = ' + id_chat.__str__() +
        ' and "id_message" = ' + id_message.__str__() + ' and "id_user" = ' + id_user.__str__()
    )
    conn.commit()
    conn.close()
    return

def get_all_mes(id_chat):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        'select * from "Message" where "id_chat" = '+id_chat.__str__()+' order by "time"'
    )
    rows = cur.fetchall()
    result = []
    for row in rows:
        data = {
            "id_message": row[0],
            "id_chat": row[1],
            "id_user": row[2],
            "Time": row[3],
            "id_status": row[4],
        }
        result.append(data)
    conn.commit()
    conn.close()
    return result

def add_in_dialog(id_user, id_dialog):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Dialogs" WHERE "IdDialog" = '+id_dialog.__str__())
    row = cursor.fetchone()
    cursor.execute('INSERT INTO "Dialogs" ("IdDialog", "IdUser", "Status", "NameDialog", "Photo") VALUES '
                   + ' (' + id_dialog.__str__()+', ' + id_user.__str__() + ', ' + row[2].__str__()
                   + ', \'' + row[3].__str__() + '\', \'' + row[5].__str__() + '\')')
    conn.commit()
    conn.close()
    return
