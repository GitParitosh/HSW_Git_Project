pi=3.14159
#NASA uses 15 digits of Pi for their calculations. Since we're not going to Space I think we can do with 5 :p
def PrincipalBranch(x):
    #This converts our value into a value between -pi and pi
    r=x%pi
    try:
        branch=(x%(2*pi)-pi)/abs(x%(2*pi)-pi)
    except ZeroDivisionError:
        branch=-1
        
        
    return r,branch

def sin(x):
    #The Taylor Series for Sin(x) around 0 is being used here. It has a very low error rate
    #Infact the error is less than x^15/15!, which in our Principal Branch is less than 0.00002 at maximum
    #This could be lower, but the next term in the Taylour series is 17! that hass 15 digits. I just stopped at the one with 10 terms.
    #A more reasonable optimaization would be in the PrincipalBranch() function, such that it reduces x to between 0 and pi/2 then it returns a quadrant to reconstruct the function with. But that's considerably more work
    n=PrincipalBranch(x)
    x=n[0]
    branch=n[1]
    r=x-(x**3)/6+(x**5)/120-(x**7)/5040+(x**9)/362880-(x**11)/39916800+(x**13)/6227020800
    return round(r*branch*(-1),5)

def cos(x):
    #Using Identity cos(x)=sin(pi/2-x)
    r=sin((pi/2)-x)
    return r
def tan(x):
    #Definition of tan(x)
    try:
        r=sin(x)/cos(x)
    except ZeroDivisionError:
        return "ERROR"
    return r
def cosec(x):
    #Definition of cosec(x)
    try:
        r=1/sin(x)
    except ZeroDivisionError:
        return "ERROR"
    return r
def sec(x):
    #Definition of sec(x)
    try:
        r=1/cos(x)
    except ZeroDivisionError:
        return "ERROR"
    return r
def cot(x):
    #Definition of sec(x)
    try:
        r=cot(x)/sin(x)
    except ZeroDivisionError:
        return "ERROR"
    return r
