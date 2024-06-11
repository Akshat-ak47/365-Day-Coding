# Pow(x, n)

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1/x
        n = -n
    if n % 2 == 0:
        return power(x*x, n//2)
    else:
        return power(x*x, (n-1)//2)

x = 2.0
n = 5
print("Result:", power(x, n)) 