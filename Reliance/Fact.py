def factorial(n):
    product = 1
    if n ==1:
        return 1
    else:
        while n!=0 :
            product*=n
            n=n-1
        return product

print(factorial(1))

def fact_recur(n):
    if n < 1:
        return 1
    else:
        return n*fact_recur(n-1)

print(fact_recur(5))