#Import all Libraries required for the Operators
import Trigonometry as trig
import Factorial as fact
SupportedOperators=["+","-","/","*","^","!"]
SupportedFunctions=["sin"]
SupportedConstants={"c":3000000,"pi":3.14159,"e":2.718}
#This is a list of all Operations/Functions Supported by the calculator.

def Unique(l):
    #This just removes any duplicates from a list
    out=[]
    for i in l:
        if i not in out: out.append(i)
    return out

def MathObjects(inp):
    #This function converts a string into a list of Mathematical objects which can then be Parsed by StringParser()
    #For eg. if the input is "7*8+21" this function should return [7,"*",8,"+",21]
    #For a more complex example, "sin(3pi)+8!" should return ["sin",3,3.14159,8,"!"]
    #It should also have bracket support, so entering "(3+4+7)*9" should return [[3,"+",4,"+",7],"*",9] then the list will be parsed again through MathObjects
    inp=inp+"⫸"
    out=[]
    MObj=""
    BracketObj=[]
    BracketReader=0
    NestingLvl=0
    if inp[0]==".":
        inp="0"+inp
    for i in inp:
        if i == "⫸":
            if MObj in SupportedFunctions or MObj in SupportedOperators:
                out.append(MObj)
                MObj=i
                continue
            if MObj in SupportedConstants:
                out.append(SupportedConstants[MObj])
                MObj=i
                continue
            if MObj!="" and MObj!="⫸":
                out.append(float(MObj))
            continue
        if BracketReader>0:
            if i not in "()":
                MObj+=i
            elif i==")":
                BracketReader=BracketReader-1
                if BracketReader==0:
                    BracketObj=MathObjects(MObj)
                    out.append(BracketObj[0])
                    MObj=""
                else:
                    MObj+=i
            elif i=="(":
                BracketReader=BracketReader+1
                
        else:
            if MObj=="" or MObj==" ":
                MObj=i
                continue
            if MObj=="(":
                if i!=")":
                    MObj=i
                    BracketReader=BracketReader+1
                    continue
                else:
                    MObj=""
                    out.append("ERROR")
                    continue
            if MObj in SupportedFunctions or MObj in SupportedOperators:
                out.append(MObj)
                MObj=i
                continue
            if MObj in SupportedConstants:
                out.append(SupportedConstants[MObj])
                MObj=i
                continue
            if MObj.isdecimal() and i.isdecimal() or i==".":
                MObj=MObj+i
                continue
            elif MObj.isdecimal() and i=="(":
                out.append(float(MObj))
                MObj=i
                out.append("*")
                BracketReader=1
                continue
            elif MObj.isdecimal() and i.isalpha():
                out.append(float(MObj))
                out.append("*")
                MObj=i
                continue
            elif MObj.isdecimal() and not i.isdecimal():
                out.append(float(MObj))
                MObj=i
                continue
            if "." in MObj:
                tempsplit = MObj.split(".")
                temp=tempsplit[-1]
                if (temp.isdecimal() or temp=="") and i.isdecimal():
                    MObj=MObj+i
                    continue
                elif temp.isdecimal and i=="(":
                    out.append(float(MObj))
                    out.append("*")
                    MObj=i
                    continue
                elif (temp.isdecimal or temp=="") and i==".":
                    MObj=MObj+"0"
                    out.append("ERROR")
                elif (temp.isdecimal() or temp=="") and not i.isdecimal():
                    out.append(float(MObj))
                    MObj=i
                    continue
            if MObj.isalpha() and i.isalpha():
                MObj=MObj+i
                continue
            elif MObj.isalpha() and i=="(":
                out.append(MObj)
                MObj=i
                BracketReader=1
                continue
    return out
            
def MathParser(inp):
    #This function reads a list of Math Objects as returned by MathObjects and outputs the results
    #This function respects PEMDAS, but all other functions are resolved left to right(While respecting Brackets)
    #Resolving Errors
    for i in range(len(inp)):
        if i=="ERROR":
            return "ERROR"
    #Resolve Brackets
    for i in range(len(inp)):
        if type(inp[i])==list:
            BracketResult=MathParser(i)
            inp[i]=BracketResult
    #Resolve Functions
    #This includes Trigonometry but also Hyperbolic Trigonometry and Ln(x)/Log(x). Basically any mathematical function that only depends on the bracket after it.
    for i in range(len(inp)):
        if inp[i] in SupportedFunctions:
            func="Result="+"trig."+inp[i]+"("+inp[i+1]+")"
            exec(func)
            inp[i+1]=Result
            inp[i]="temp"
            #WARNING: exec() is a large security issue, very vulnerable to code injection. Luckilly this code will never be on a server.
            #This code could be replaced to be safer but then I'd have to hardcode the call for every function in the list
    while "temp" in inp:
        inp.remove("temp")
    #Resolve Factorials
    #Because of the nature of Factorial symbol being put after a number it needs to be parsed seperately to both functions and opperators
    for i in range(len(inp)):
        if inp[i]=="!":
            inp[i+1]=fact.factorial(i)
            inp[i]="temp"
    while "temp" in inp:
        inp.remove("temp")
    #Resolve Exponents
    #PEMDAS
    for i in range(len(inp)):
        if inp[i]=="^":
            inp[i-1]=inp[i-1]^inp[i+1]
            inp[i]="temp"
            inp[i+1]="temp"
    while "temp" in inp:
        inp.remove("temp")
    #Resolve Multiplication
    #PEMDAS
    for i in range(len(inp)):
        if inp[i]=="*":
            inp[i-1]=inp[i-1]*inp[i+1]
            inp[i]="temp"
            inp[i+1]="temp"
    while "temp" in inp:
        inp.remove("temp")
    #Resolve Division
    #PEMDAS
    for i in range(len(inp)):
        if inp[i]=="/":
            inp[i-1]=inp[i-1]/inp[i+1]
            inp[i]="temp"
            inp[i+1]="temp"
    while "temp" in inp:
        inp.remove("temp")
    #Resolve Addition
    #PEMDAS
    for i in range(len(inp)):
        if inp[i]=="+":
            inp[i-1]=inp[i-1]+inp[i+1]
            inp[i]="temp"
            inp[i+1]="temp"
    while "temp" in inp:
        inp.remove("temp")
    #Resolve Subtraction
    #PEMDAS
    for i in range(len(inp)):
        if inp[i]=="-":
            inp[i-1]=inp[i-1]-inp[i+1]
            inp[i]="temp"
            inp[i+1]="temp"
    while "temp" in inp:
        inp.remove("temp")
    #Finalizing answer and verifying format
    if len(inp)!=1:
        return "ERROR"
    else:
        return inp[0]
