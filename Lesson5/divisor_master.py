def if_simple(x):
    if x % 2 == 0:
        return x == 2
    a = 3
    while a * a <= x and x % a != 0:
        a += 2
    return a * a > x

def divisors(x):
    div = []
    for i in range(1,x+1):
        if x % i == 0:
            div.append((i))
    return div

def biggest(x):
    for i in reversed(range(1,x+1)):
        if x % i == 0:
            if if_simple(i) == True:
                return i

def simple_m(x):
    ms = []
    a = 2
    while a * a <= x:
        if x % a == 0:
            ms.append(a)
            x //= a
        else:
            a += 1
    if a > 1:
        ms.append(x)
    return ms

def biggest_d(x):
    for i in range(2, x+1):
        if x % i == 0:
            return x // i

