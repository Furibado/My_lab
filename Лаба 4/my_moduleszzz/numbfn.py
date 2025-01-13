def sum(a,b):
    return (a+b)

def raznica(a,b):
    if a > b:
        return(a-b)
    elif a < b:
        return(b-a)
    else:
        return 0

def doublefact (a):
    fact = 1
    if a % 2 != 0:
        for i in range(1, a + 1, 2):
            fact *= i
        return(fact)
    elif a == 0:
        return (0)
    else:
        for i in range(2, a + 1, 2):
            fact *= i
        return(fact)
