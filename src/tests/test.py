import unittest
import requests


class TestApi(unittest.TestCase):

# Тест регистрации
    def test_signup(self):
        data = {
            'user_number': '+79990009900',
            'user_name': 'topka',
            'password': 'qazwsx123'
        }
        resp = requests.post('http://127.0.0.1:5000/signup', json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Тест авторизации
    def test_login(self):
        data = {
            'user_number': '+79990009900',
            'password': 'qazwsx123'
        }
        resp = requests.post('http://127.0.0.1:5000/login', json=data)
        global id_session
        id_session = resp.json().get('session')
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Получение чатов
    def test_get_chats(self):
        data = {
            "id_user": 1
        }
        #global id_session
        resp = requests.get('http://127.0.0.1:5000/chat')
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Добавление чата
    def test_create_chat(self):
        data = {
            "name_chat": "Печеньки",
            "id_user": 1
        }
        resp = requests.post('http://127.0.0.1:5000/chat', json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Изменение настроек чата (добавление пользователя_2 в чат_1 или изменение его прав, переименование чата)
    def test_chat_edit(self):
        data = {
            "id_user": 2, 
            "id_chat":1,
            "id_permission":1,
            "name_chat":"Печеньки v2"
        }
        resp = requests.put('http://127.0.0.1:5000/chat/'+id_chat)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Получение сообщений из чата
    def test_get_message(self):
        data = {
            "id_chat": 1
        }
        #global id_session
        resp = requests.get('http://127.0.0.1:5000/chat/'+id_chat)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Отправка сообщения
    def test_post_message(self):
        data = {
            "id_chat": 1,
            "text_message": "Как дела?"
        }
        #global id_session
        resp = requests.post('http://127.0.0.1:5000/chat'+id_chat, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Редактирование сообщения
    def test_edit_message(self):
        data = {
            "id_chat": 1,
            "id_message": 1,
            "text_message": "Как погода?"
        }
        #global id_session
        resp = requests.post('http://127.0.0.1:5000/chat'+id_chat, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Удаление сообщения
    def test_del_message(self):
        data = {
            "id_chat": 1,
            "id_message": 1,
            "del_mes": True
        }
        #global id_session
        resp = requests.put('http://127.0.0.1:5000/chat/'+id_chat, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Добавление контакта
    def test_add_contact(self):
        data = {
            'id_user': 1,
            'id_user_cont': 2
        }
        #global id_session
        resp = requests.post('http://127.0.0.1:5000/contacts', json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Получение контактов
    def test_get_contacts(self):
        data = {
            'id_user':1
        }
        #global id_session
        resp = requests.get('http://127.0.0.1:5000/contacts')
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Обновление статуса контакта
def test_change_status_contact(self):
        data = {
            "id_cont": 1,
            "cont_status": False
        }
        resp = requests.put('http://127.0.0.1:5000/contacts', json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

# Получение информации профиля
def test_get_profile(self):
        data = {
            "id_user": 1,
        }
        resp = requests.get('http://127.0.0.1:5000/profile'+id_user, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text) 

# Изменение информации профиля
def test_edit_profile(self):
        data = {
            "id_user": 1,
            "user_number": "+79999999999",
            "user_name": "jjjjake2244",
            "password": "qazwsx123456",
            "age": 20,
            "avatar": 'https://aim400kg.com/uploads/photos/large/171673_1588_YbZioTgMtn.jpg',
            "status": "Чудес не бывает...",
        }
        resp = requests.post('http://127.0.0.1:5000/profile', json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)      

# Удаление профиля
def test_del_profile(self):
        data = {
            "id_user": 1,
            "status_user": False,
        }
        #global id_session
        resp = requests.put('http://127.0.0.1:5000/profile', json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text) 

