from db import connect


def get_cont(id_user):
    conn = connect()
    cur = conn.cursor()
    cur.execute('select * from "Contact" where ("id_user" = '+id_user.__str__()+' or "id_user_cont" = '+id_user.__str__()+') and "cont_status" = 1')
    rows = cur.fetchall()
    result = []
    for row in rows:
        Contact = 0
        if (row[0] == id_user):
            Contact = row[1]
        else:
            Contact = row[0]
        data = {
            "id_user_cont": Contact,
            "cont_status": row[2]
        }
        result.append(data)
    conn.close()
    return result


def create_cont(id_user, id_user_cont, cont_status):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select * from "Contact" where "Id_user" = '+id_user.__str__()+' or "id_user_cont" ='+id_user.__str__())
    Contact = cursor.fetchone()
    if not Contact:
        cursor.execute('INSERT INTO "Contact" ("Id_user", "id_user_cont", "cont_status") VALUES ('+id_user.__str__()
                   + ', '+id_user_cont.__str__()+', 0')
    else:
        cursor.execute('UPDATE "Contact" set "Cont_status" = 2 where "Cont_status" = 1 and ("Id_user" = '+id_user.__str__()+' or "id_user_cont" ='+id_user.__str__()+')')
    conn.commit()
    conn.close()
    return

