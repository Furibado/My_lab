name = str(input("Введите имя человека: "))
age = str(input("Введите возраст человека: "))
def describe_person(name, age=30):
    word = str('лет')
    if int(age)%10 == 1:
        word = 'год'
    elif int(age)%10 in (2,3,4) and int(age)//10 != 1:
        word = 'года'
    else:
        word = word
    print(f'Его зовут {name} и ему {age} {word}')
describe_person(name, age)