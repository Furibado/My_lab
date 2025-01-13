text = input('Введите текст, который будет в файле')
with open('input.txt','w', encoding = 'utf-8') as file:
    file.write(text)

text = input('Введите текст, который будет в файле')
with open('input.txt','a', encoding = 'utf-8') as file:
    file.write(text)
