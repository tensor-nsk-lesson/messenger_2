from db import connect


def get_profile(id_user):
    conn = connect()
    cur = conn.cursor()
    cur.execute('select "age", '
                '"user_name", '
                '"avatar", '
                '"visit_time", '
                '"status" from public.\"User\" where "id_user"='+id_user.__str__())
    info = cur.fetchone()
    col_names = [column[0] for column in cur.description]
    result = {}
    length = len(col_names)
    for i in range(length):
        result[col_names[i]] = info[i]
    cur.close()
    conn.close()
    return result
