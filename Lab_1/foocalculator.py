import calculator as c

class FooCalculator:

    #empty constructor 
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m, n)

    def divide(self, m, n):
        return c.divide(m, n)

    def subtract(self, m, n):
        return c.subtract(m, n)

    def multiply(self, m, n):
        return c.multiply(m, n)

    def gcd(self, m ,n):
        return c.gcd(m,n)

if __name__ == "__main__":
    print(FooCalculator().sum(40,2))
    print(FooCalculator().divide(40,2))
    print(FooCalculator().subtract(40,2))
    print(FooCalculator().multiply(40,2))
    print(FooCalculator().gcd(40,2))