def ln(x):
    r = 9999999*(x**(1/9999999))-9999999
    return round(r,5)
def log(b,x):
    r=ln(x)/ln(b)
    return round(r,5)
