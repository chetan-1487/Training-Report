def sum(a,b):
    return a+b
def mul(a,b):
    return a*b


print(sum(1,2))
print(mul(2,3))


def prime_No(n):
    if n==1:
        return False
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    return c==2
print(prime_No(78))
print(prime_No(79))