import my_module


a,b = map(int,input("Введите два числа, разделённых пробелом ").split())
answer = my_module.sum(a,b)
print(answer)