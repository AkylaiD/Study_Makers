# Task 1
 
# list_ = [i for i in range(1, 101)]
# new_list = [i if i % 3 == 0 and i % 5 == 0 else 'неизвестно' for i in list_]
# print(new_list)

# lst = [i if i % 3 == 0 and i % 5 == 0 else 'неизвестно' for i in range(1, 101)]
# print(lst)


# Task 2

# dct = {'hello': None, 'world': None, 'programmer':None}
# # dct1 = {key: len(key) for key, value in dct.items()}
# dct1 = {key: len(key) for key in dct.keys()}
# print(dct1)


# # Task 3
# name = input('Enter your name: ')
# password = input('Enter password: ')
# database = {name: password}
# def sign_up():
#     x = name
#     y = password
#     database.update{(x: y)}
# print ('You have signed up successfully!')

# def log_in:
#     x = name
#     y = password
    

# def manage():
#     for name, password in database():
#         if name and password in database():
#             print('Welcome back!')
#         else:
#             sign_up()


# users = {'Alex': 'hello'}
# def login(name):
#     print(f'User, {name}! You have logged in succussfully!')
# def registration(name, password):
#     global users
#     users[name] = password
#     print(f'List of users: {users}')
# def manager():
#     name = input('Enter your name: ')
#     password = input('Enter password: ')
#     if name in users:
#         login(name)
#     else:
#         print('You are not registered!')
#         registration(name, password)
#         print('You have been registered!')

# manager()

# Task 4

# Дана БД, реализовать CRUD при помощи функций C-create, R-read/retrieve, U-update, D-delete.

# db = {'John': 23, 'Jack': 52, 'Alex': 23, 'Tom': 34}
# def create():
#     global db
#     name = input('Введите имя: ')
#     age = int(input('Введите возраст: '))
#     if name in db:
#         print('Пользователь уже существует!')
#     else:
#         db.update({name: age})
#         # db[name] = age
#         print('Пользователь успешно добавлен!')
#     print(f'На данный момент список пользователей такой: {db}')


# def read():
#     print(f'На данный момент содержание БД такое: {db}')


# def update():
#     global db
#     name = input('Какого пользователя хотите изменить? ')
#     age = int(input('Новый возраст: '))
#     if name in db:
#         db.update({name: age})
#         print('Пользователь успешно изменен!')
#         print(f'Список на данный момент такой {db}')

# def delete():
#     global db
#     name = input('Какого пользователя удалить? ')
#     if name in db:
#         db.pop(name)
#     print('Пользователь удален', db)

# create()
# read()
# update()
# delete()

