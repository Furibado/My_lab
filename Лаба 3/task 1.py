with open('Example.txt','r', encoding="utf-8") as file:
    content = file.read()
    print(content)

with open('Example.txt', 'r', encoding="utf-8") as file:
    for line in file:
        print(line.strip())

with open('Example.txt', 'r', encoding="utf-8") as file:
    type = input('Введите метод чтения файла (Сразу весь файл или построчный) ')
    if type.lower() == 'сразу весь файл':
        content = file.read()
        print(content)
    elif type.lower() == 'построчный':
        for line in file:
            print(line.strip())

