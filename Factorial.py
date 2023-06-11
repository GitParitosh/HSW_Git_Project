def factorial(x):
    if x-round(x)!=0:
        return "ERROR"
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
