import hashlib
import getpass

def get_tok(filename):
    with open(filename, 'r') as file:
        first_line = file.readline()
    return first_line

def authenticate():
    with open('credentials.txt', 'r') as file:
        credentials = [line.strip().split(':') for line in file.readlines()]

    for i in range(5):
        username = input("ВВедите вашь логин: ")
        password =  getpass.getpass("ВВедите вашь пароль: ")
        #Расчёт хеш функции MD5 логина и пароля 
        username = hashlib.sha512(username.encode())
        password = hashlib.sha512(password.encode())
        
        for correct_username, correct_password, correct_sha512 in credentials:
            if username.hexdigest() == correct_username and password.hexdigest() == correct_password:
                tok = input("Вставте токен (1): ")
                if int(tok) == 1 : 
                    get = get_tok("tok.txt")
                    if correct_sha512 == get: 
                        print ("успешный вход в систему!")
                        return True
                    else: 
                        print ("неверный токен")
                else: 
                    print ("неверный токен")

            else:
                print('не верный логин или пароль. Попробуйте еще раз.')

    print('Превышено количество попыток ввода. Пожалуйста, попробуйте позже.')
    return False

authenticate()

