#calculator.py

def sum(m, n):
    inc = 1

    if n < 0:
        inc = -1

    for i in range(abs(n)):
        m += inc

    return m

def divide(m, n):
    
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

if __name__ == "__main__":
    print(sum(-40,-2))
    print(divide(-6,-3))
