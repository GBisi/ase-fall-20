#calculator.py

def sum(m, n):
    inc = 1

    if n < 0:
        inc = -1

    for i in range(abs(n)):
        m += inc

    return m

def divide(m, n):

    if n == 0:
        raise ZeroDivisionError()
    
    i = 0
    negative = m>0 and n<0 or m<0 and n>0    
    m = abs(m)
    n = abs(n)


    while (m-n) >= 0:
        m -= n
        i += 1
    
    if negative:
        return -i
    else:
        return i

def subtract(m,n):
    dec = 1

    if n < 0:
        dec = -1

    for i in range(abs(n)):
        m -= dec

    return m

def multiply(m, n):
    negative = m>0 and n<0 or m<0 and n>0    
    m = abs(m)
    n = abs(n)
    mul = 0

    for i in range(n):
        mul+=m
    
    if negative:
        return -mul
    else:
        return mul

def gcd(m, n):
    while n != 0:
        tmp = n
        n = m%n
        m = tmp 
    return m

if __name__ == "__main__":
    print(sum(-40,-2))
    print(subtract(40,-2))
    print(divide(-294,-7))
    print(multiply(-6,7))
    print(gcd(2,4))
