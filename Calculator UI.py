import MathParser as m
ErrorMessage='''There was an error in the program.
Input expression may be invalid, if you believe that this is not the case please contact the developers

'''
HelpErrorMessage='''
It looks like you tried typing a help command, make sure that you type in the format "help [Function]" or "h [Function
If you want a list of Functions then you can type "help h" or "h help"
'''
#Every key here represents a help command to be called
HelpMessages={"help":'''This is a command that can be used to get information on any other command. Here is every unique supported commands in this calculator(Some commands have aliases). type help [function] to know more about it
trig
deg
sin
cos
tan
cosec
sec
cot
sinh
cosh
tanh
cosech
sech
coth
log
ln
exponent
factorial
add
subtract
multiply
divide
mod
pemdas
e
pi
c
g
''',
"h":'''This is a command that can be used to get information on any other command. Here is every unique supported commands in this calculator(Some commands have aliases). type help [function] to know more about it
trig
deg
sin
cos
tan
cosec
sec
cot
sinh
cosh
tanh
cosech
sech
coth
log
ln
exponent
factorial
add
subtract
multiply
divide
mod
pemdas
''',
"trig":'''Trigonometry is the branch of mathematics concerned with Angles and their Ratios. It's functions are everpresent in any problem involving meassurements and angles.
Here's a list of supported Trigonometric functions:
Note: All of the following functions except deg take values in Radians. deg() converts degrees into radians to be fed into these commands if that is your preference.
deg
sin
cos
tan
cosec
sec
cot
sinh
cosh
tanh
cosech
sech
coth
''',
"trigonometry":'''Trigonometry is the branch of mathematics concerned with Angles and their Ratios. It's functions are everpresent in any problem involving meassurements and angles.
Here's a list of supported Trigonometric functions:
Note: All of the following functions except deg take values in Radians. deg() converts degrees into radians to be fed into these commands if that is your preference.
deg
sin
cos
tan
cosec
sec
cot
sinh
cosh
tanh
cosech
sech
coth
''',
"sine":'''Sine of an angle is usually defined as the ratio between the side perpidencularly opposite to it and the Hypotenuse to that side.
''',
"sin":'''Sine of an angle is usually defined as the ratio between the side perpidencularly opposite to it and the Hypotenuse to that side.
''',
"cos":'''Cosine of an angle is usually defined as the ratio between the side adjacent to it to and the Hypotenuse to the side perpendicularly opposite to it. 
''',
"cosine":'''Cosine of an angle is usually defined as the ratio between the side adjacent to it to and the Hypotenuse to the side perpendicularly opposite to it. 
''',
"tan":'''Tangent of an angle is usually defined as the ratio between it's sine and it's cosine.
''',
"tangent":'''Tangent of an angle is usually defined as the ratio between it's sine and it's cosine.
''',
"cosec":'''Cosecant of an angle is usually defined as the reciprocal of it's sine.
''',
"cosecant":'''Cosecant of an angle is usually defined as the reciprocal of it's sine.
''',
"secant":'''Secant of an angle is usually defined as the reciprocal of it's cosine.
''',
"cot":'''Cotangent of an angle is usually defined as the reciprocal of it's tangent.
''',
"cosecant":'''Cosetangent of an angle is usually defined as the reciprocal of it's tangent.
''',
"sinh":'''Sinh or Hyperbolic Sine is the equivalent for Sine in Hyperbolic Geometry and is useful for various problems in engineering and architechture.
Most Trigonometric relations and identities remain true for Hyperbolic functions.
''',
"cosh":'''Cosh or Hyperbolic Cosine is the equivalent for Cosine in Hyperbolic Geometry and is useful for various problems in engineering and architechture.
Most Trigonometric relations and identities remain true for Hyperbolic functions.
''',
"tanh":'''Tanh or Hyperbolic Tangent is the equivalent for Tangent in Hyperbolic Geometry and is useful for various problems in engineering and architechture.
Most Trigonometric relations and identities remain true for Hyperbolic functions.
''',
"cosech":'''Cosech or Hyperbolic Cosecant is the equivalent for Cosecant in Hyperbolic Geometry and is useful for various problems in engineering and architechture.
Most Trigonometric relations and identities remain true for Hyperbolic functions.
''',
"sech":'''Sech or Hyperbolic Secant is the equivalent for Secant in Hyperbolic Geometry and is useful for various problems in engineering and architechture.
Most Trigonometric relations and identities remain true for Hyperbolic functions.
''',
"coth":'''Coth or Hyperbolic Cotangent is the equivalent for Cotangent in Hyperbolic Geometry and is useful for various problems in engineering and architechture.
Most Trigonometric relations and identities remain true for Hyperbolic functions.
''',
"log":'''Logarithm is the inverse function of Exponentiation. If B^x=y then BLog(y)=x. Here, B is called the "Base" of the Logarithm. Logarithms are incredibly useful not only in cases where powers are involved but also due to their various properties that make calculations easier
Eg. Blog(x*y)=Blog(x)+Blog(y)
''',
"logarithm":'''Logarithm is the inverse function of Exponentiation. If B^x=y then BLog(y)=x. Here, B is called the "Base" of the Logarithm. Logarithms are incredibly useful not only in cases where powers are involved but also due to their various properties that make calculations easier
Eg. Blog(x*y)=Blog(x)+Blog(y)
''',
"ln":'''Logarithm is the inverse function of Exponentiation. If B^x=y then BLog(y)=x. Here, B is called the "Base" of the Logarithm. ln refers to the Natural Logarithm, which is a Logarithm where the Base is Euler's Number "e". This is an essential part of Calculus mainly for the reason that the function e^x has the slope e^x at any point on the function.
e is a supported constant in this calculator, typing e would automatically be interpretted as it's value to 5 digits(put value of e here)
''',
"factorial":'''Factorial of a number(represented by n!) is equal to the product of it and all the natural numbers less than it(ie till 1). For example, 3! is 3*2*1. 0! is specially desfined to be equal to 1.
This function is only defined for natural numbers for this calculator and it will return an error if used on a non-whole number. 
''',
"!":'''Factorial of a number(represented by n!) is equal to the product of it and all the natural numbers less than it(ie till 1). For example, 3! is 3*2*1. 0! is specially desfined to be equal to 1.
This function is only defined for natural numbers for this calculator and it will return an error if used on a non-whole number. 
''',
"^":'''Exponent is a repeated multiplication of a number by itself. For example, 2^3 is equal to 2*2*2 and 3^5 is 3*3*3*3*3. This is a very common operator in mathematics and is represented by ^ in this calculator.
''',
"**":'''Exponent is a repeated multiplication of a number by itself. For example, 2^3 is equal to 2*2*2 and 3^5 is 3*3*3*3*3. This is a very common operator in mathematics and is represented by ^ in this calculator.
''',
"exponent":'''Exponent is a repeated multiplication of a number by itself. For example, 2^3 is equal to 2*2*2 and 3^5 is 3*3*3*3*3. This is a very common operator in mathematics and is represented by ^ in this calculator.
''',
"exponentiation":'''Exponent is a repeated multiplication of a number by itself. For example, 2^3 is equal to 2*2*2 and 3^5 is 3*3*3*3*3. This is a very common operator in mathematics and is represented by ^ in this calculator.
''',
"*":'''Multiplication is repeated addition of a number with itself. For example 9*5 is equal to 9+9+9+9+9 and 4*2 is equal to 4+4. This is a very common operator in mathematics and can be represented by either * or x in this calculator.
''',
"x":'''Multiplication is repeated addition of a number with itself. For example 9*5 is equal to 9+9+9+9+9 and 4*2 is equal to 4+4. This is a very common operator in mathematics and can be represented by either * or x in this calculator.
''',
"multiply":'''Multiplication is repeated addition of a number with itself. For example 9*5 is equal to 9+9+9+9+9 and 4*2 is equal to 4+4. This is a very common operator in mathematics and can be represented by either * or x in this calculator.
''',
"multiplication":'''Multiplication is repeated addition of a number with itself. For example 9*5 is equal to 9+9+9+9+9 and 4*2 is equal to 4+4. This is a very common operator in mathematics and can be represented by either * or x in this calculator.
''',
"+":'''Addition is increasing one number by another. This is usually understood as going right on the number line. This is a very common operator in mathematics and is represented by + in this calculator
''',
"add":'''Addition is increasing one number by another. This is usually understood as going right on the number line. This is a very common operator in mathematics and is represented by + in this calculator
''',
"addition":'''Addition is increasing one number by another. This is usually understood as going right on the number line. This is a very common operator in mathematics and is represented by + in this calculator
''',
"/":'''Division is the inverse operation of multiplication. If a*b=c then b/a=b. Division is essential as it is how we understand rational numbers. This is represented by / in this calculator.
You CANNOT divide by 0, trying to do so will give an error in the calculator.
''',
"divide":'''Division is the inverse operation of multiplication. If a*b=c then b/a=b. Division is essential as it is how we understand rational numbers. This is represented by / in this calculator.
You CANNOT divide by 0, trying to do so will give an error in the calculator.
''',
"division":'''Division is the inverse operation of multiplication. If a*b=c then b/a=b. Division is essential as it is how we understand rational numbers. This is represented by / in this calculator.
You CANNOT divide by 0, trying to do so will give an error in the calculator.
''',
"-":'''Subtraction is decreasing one number by another. This is usually understood as going left on the number line. Going left of 0 gives us the negative numbers, which are represented in mathematics by "-n". This can also be done on the calculator. The "-" symbol also doubles for the symbol for subtraction(since subtraction can be thought of as addition but with the negative of a value)
''',
"subtract":'''Subtraction is decreasing one number by another. This is usually understood as going left on the number line. Going left of 0 gives us the negative numbers, which are represented in mathematics by "-n". This can also be done on the calculator. The "-" symbol also doubles for the symbol for subtraction(since subtraction can be thought of as addition but with the negative of a value)
''',
"subtraction":'''Subtraction is decreasing one number by another. This is usually understood as going left on the number line. Going left of 0 gives us the negative numbers, which are represented in mathematics by "-n". This can also be done on the calculator. The "-" symbol also doubles for the symbol for subtraction(since subtraction can be thought of as addition but with the negative of a value)
''',
"%":'''The modulous operator returns the difference between the first number and the highest integer multiple of the second number less than it. This is incredibly useful in any field that deals with parity or just with the division of natural numbers. This is also often understood as finding the "Remainder" of division between two numbers. Both % and "mod" can be used as symbols of modulous in thsi calculator.
''',
"mod":'''The modulous operator returns the difference between the first number and the highest integer multiple of the second number less than it. This is incredibly useful in any field that deals with parity or just with the division of natural numbers. This is also often understood as finding the "Remainder" of division between two numbers. Both % and "mod" can be used as symbols of modulous in thsi calculator.
''',
"modulo":'''The modulous operator returns the difference between the first number and the highest integer multiple of the second number less than it. This is incredibly useful in any field that deals with parity or just with the division of natural numbers. This is also often understood as finding the "Remainder" of division between two numbers. Both % and "mod" can be used as symbols of modulous in thsi calculator.
''',
"modulous":'''The modulous operator returns the difference between the first number and the highest integer multiple of the second number less than it. This is incredibly useful in any field that deals with parity or just with the division of natural numbers. This is also often understood as finding the "Remainder" of division between two numbers. Both % and "mod" can be used as symbols of modulous in thsi calculator.
''',
"remainder":'''The modulous operator returns the difference between the first number and the highest integer multiple of the second number less than it. This is incredibly useful in any field that deals with parity or just with the division of natural numbers. This is also often understood as finding the "Remainder" of division between two numbers. Both % and "mod" can be used as symbols of modulous in thsi calculator.
''',
"pemdas":'''PEMDAS is the order that standard mathematical expressions are resolved in. It stands for Parentheseis, Exponentiation, Multiplication, Division, Addition and Subtraction. You go from left to right solving each operation at a time. Functions are naturally solved during the Parentheseis step, due to there being an implied parenthesies around their arguments at all times
Brackets are an important tool to differentiante your equations, they vastly improve readability of your expression, though they might be cumbursome to type each time. This calculator already interprets all equations in the order of PEMDAS for your convinience.
''',
"parentheseis":'''PEMDAS is the order that standard mathematical expressions are resolved in. It stands for Parentheseis, Exponentiation, Multiplication, Division, Addition and Subtraction. You go from left to right solving each operation at a time. Functions are naturally solved during the Parentheseis step, due to there being an implied parenthesies around their arguments at all times
Brackets are an important tool to differentiante your equations, they vastly improve readability of your expression, though they might be cumbursome to type each time. This calculator already interprets all equations in the order of PEMDAS for your convinience.
''',
"brackets":'''PEMDAS is the order that standard mathematical expressions are resolved in. It stands for Parentheseis, Exponentiation, Multiplication, Division, Addition and Subtraction. You go from left to right solving each operation at a time. Functions are naturally solved during the Parentheseis step, due to there being an implied parenthesies around their arguments at all times
Brackets are an important tool to differentiante your equations, they vastly improve readability of your expression, though they might be cumbursome to type each time. This calculator already interprets all equations in the order of PEMDAS for your convinience.
'''
"e":"e, also known as the Euler's Constant"
}
while True:
    Result=''
    print('''Welcome to the Calculator, here you can calculate mathematical expressions using common symbols
Type H or Help to go to learn about supported functions
Type any Mathematical expression and press enter to get answer
Type c or Close to Close calculator''')
    inp=input("")
    inp=inp.lower()
    if inp=="c" or inp=="close":
        break
    elif inp[:2]=="h ":
        try:
            print(HelpMessages(inp[2:]))
        except:
            print(HelpErrorMessage)
    elif inp[:5]=="help ":
        try:
            print(HelpMessages(inp[5:]))
        except:
            print(HelpErrorMessage)
    else:
        try:
            l=m.MathObjects(inp)
            Result=m.MathParser(l[0],l[1])
        except Exception as e:
            Result="ERROR"
        if Result=="ERROR":
            print(ErrorMessage)
        else:
            print(Result)
