class UserAccount:

    def __init__ (self, username, email, password):
        self.username = username
        self. email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return (password == self.__password )

Loloshka = UserAccount("Loloshka", "Loloshkashop.ru", "123456")
new_password = str(input("Введите новый пароль "))
Loloshka.set_password(new_password)
password = str(input("Введите ваш пароль "))
if Loloshka.check_password(password) == True:
    print("Пароль верный")
else:
    print("Пароль неверный")

