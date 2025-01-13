name = str(input("Введите имя: "))
def greet(name):
    print("Привет,",name)
greet(name)

number = int(input("Введите число: "))
def square(number):
    print(number**2)
square(number)

x,y=map(int,input("Введите 2 числа через пробел: ").split())
def max_of_two(x,y):
    if x>y:
        return ('Большее:', x)
    elif y>x:
        return ('Большее число:',y)
    else:
        return ("Они одинаковы")
print(max_of_two(x,y))

