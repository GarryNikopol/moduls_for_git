while True:
    print("Создайте логин (от 4 до 20 символов):")
    login = input()
    
    if 4 <= len(login) <= 20:
    	print("Логин принят")
    	break
    else:
    	print("Логин не соответсвует требованиям")

while True:
	print("Создайте пароль от 8 до 20 символов, включая заглавные буквы и цифры")
	password = input()
	
	if 8 <= len(password) <= 20 and any('A' <= c <= 'Z' for c in password) and any('0' <= c <= '9' for c in password) and any('a' <= c <= 'z' for c in password):
		print("Пароль принят")
		break
	else:
		print("Пароль не соответствует требованиям.")

while True:
    login_input = input("Введите ваш логин: ")
    password_confirm = input("Введите ваш пароль: ")

    if login_input == login and password_confirm == password:
        print("Доступ разрешён")
        break
    else:
        print("Доступ запрещён.") 