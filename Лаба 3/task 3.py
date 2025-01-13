try:
    with open('Example.txt','r', encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Нет такого файла')