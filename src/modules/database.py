import psycopg2
from psycopg2.extras import RealDictCursor

def sql_execute(query, fetch_all):
    conn = psycopg2.connect(dbname='messenger_2', user='messenger_2', password='messenger_2', host='90.189.168.29')
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    answer = None
    cursor.execute(query)
    conn.commit()
    try:
        if fetch_all:
            answer = cursor.fetchall()
        else:
            answer = cursor.fetchone()
    except psycopg2.Error as err:
        print(err)
        return {'status': 0, 'message': 'Error in database'}
    finally:
        cursor.close()
        conn.close()
        return answer