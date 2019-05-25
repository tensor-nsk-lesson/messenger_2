import psycopg2


connect = psycopg2.connect("dbname=messenger_2 user=messneger_2 host=90.189.168.29 password=messenger_2")
cursor = connect.cursor()
# создать табоицу
cursor.execute(open("../SQL/messenger_2.sql", "r").read())
# заполнить таблицу авторизации
cursor.execute(open("../SQL/Auth_insert.sql", "r").read())
# заполнить таблицу чатов
cursor.execute(open("../SQL/Chat_insert.sql", "r").read())
# заполнить таблицу содержимых сообщений
cursor.execute(open("../SQL/Content_insert.sql", "r").read())
# заполнить таблицу сообщений
cursor.execute(open("../SQL/Message_insert.sql", "r").read())
# заполнить таблицу разрешений
cursor.execute(open("../SQL/Permission_insert.sql", "r").read())
# заполнить таблицу пользователей
cursor.execute(open("../SQL/User_insert.sql", "r").read())