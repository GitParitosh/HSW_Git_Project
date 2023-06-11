e=2.71828
#Euler's number till 5 places
def sinh(x):
    #Definition of Sinh(x). Way simpler than Trig
    r=(e**x-e**(-x))/2
    return r
def cosh(x):
    #Definition of Cosh(x)
    r=(e**x+e**(-x))/2
    return r
def tanh(x):
    #Definition of tanh(x)
    try:
        r=sinh(x)/cosh(x)
    except ZeroDivisionError:
        return "ERROR"
    return r
def cosech(x):
    #Definition of cosech(x)
    try:
        r=1/sinh(x)
    except ZeroDivisionError:
        return "ERROR"
    return r
def sech(x):
    #Definition of sech(x)
    try:
        r=1/cosh(x)
    except ZeroDivisionError:
        return "ERROR"
    return r
def coth(x):
    #Definition of sech(x)
    try:
        r=coth(x)/sinh(x)
    except ZeroDivisionError:
        return "ERROR"
    return r
