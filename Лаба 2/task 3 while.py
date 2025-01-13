number = int(input("Введите число: "))
def is_prime(number):
        simple = True
        i = 2
        if number <= 1:
                simple = False
        while i < number:
                if number%i == 0:
                        simple = False
                        break
                i+=1
        return(simple)
print(is_prime(number))
