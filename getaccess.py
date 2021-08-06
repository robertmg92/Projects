import getpass
import os

user_login = ['username', 'password']

def get_user_login():
    user_name = input('Please enter your username: ')
    password = getpass.getpass('Please enter your password: ')
    return user_name, password

def check_user_login(user_login):
   username, password = get_user_login()
   return user_login[0] == username and user_login[1] == password

if user_login == user_login:
    login_attempts = 1
    correct_login = check_user_login(user_login)
    while not correct_login and login_attempts < 3:
       print('\nWrong username or password, please try again: \n')
       correct_login = check_user_login(user_login)
       login_attempts += 1

    if correct_login:
       print('Welcome! You now have access to my files')
    else:
       print('\nToo many failed attempts' 
             '\nPlease reload the page and try again')



