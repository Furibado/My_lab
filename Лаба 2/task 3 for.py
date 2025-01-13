number = int(input("Введите число: "))
def is_prime(number):
        simple = True
        if number <= 1:
            simple = False
        for i in range(2, number):
            if number % i == 0:
                simple = False
                break
        return(simple)
print(is_prime(number))

