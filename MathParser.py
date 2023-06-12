#Import all Libraries required for the Operators
import MainFunctions as mfunc
SupportedOperators=["+","-","/","*","^","!","%","mod","x","log"]
SupportedFunctions=["deg","sin","cos","tan","cosec","sec","cot","sinh","cosh","tanh","cosech","coth","ln"]
SupportedConstants={"c":3000000,"pi":3.14159,"e":2.71828,"g":9.81,}
#This is a list of all Operations/Functions Supported by the calculator.
def NoNesting(x):
    #GOD. JUST TO REMOVE NESTING FROM THE MathObjects OUTPUT TO MathOrder.
    Nested=True
    while Nested:
        y=[]
        for i in x:
            if type(i)==list:
                y.extend(i)
            else:
                y.append(i)
        x=list(y)
        Nested=False
        for i in x:
            if type(i)==list:
                Nested=True
    return x
def MathOrder(inp):
    #This takes all functions in the list, removes any duplicates and then orders them by the order Func->Factorial->Log->EMMDAS
    #(Second M is Modulo)
    inp=NoNesting(inp)
    l2=[]
    out=[]
    for i in inp:
        if i not in l2 and (i in SupportedFunctions or i in SupportedOperators):
            l2.append(i)
    for i in l2:
        if i in SupportedFunctions:
            out.append(i)
    if "!" in l2: out.append("!")
    if "log" in l2: out.append("log")
    if "^" in l2: out.append("^")
    if "*" in l2: out.append("*")
    if "x" in l2: out.append("x")
    if "%" in l2: out.append("%")
    if "mod" in l2: out.append("mod")
    if "/" in l2: out.append("/")
    if "+" in l2: out.append("+")
    if "-" in l2: out.append("-")
    return out

def MathObjects(inp,depth=0):
    #This function converts a string into a list of Mathematical objects which can then be Parsed by StringParser()
    #For eg. if the input is "7*8+21" this function should return [7,"*",8,"+",21]
    #For a more complex example, "sin(3pi)+8!" should return ["sin",3,3.14159,8,"!"]
    #It should also have bracket support, so entering "(3+4+7)*9" should return [[3,"+",4,"+",7],"*",9] then the list will be parsed again through MathObjects
    inp=inp+"⫸"
    out=[]
    MObj=""
    UsedFunctions=[]
    BracketObj=[]
    BracketReader=0
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
                if MObj.isdecimal():
                    out.append(float(MObj))
                    continue
                else:
                    BracketObj=MathObjects(MObj,depth+1)
                    out.append(BracketObj[0])
                    MObj=""
                    continue
        if BracketReader>0:
            if i not in "()":
                MObj=MObj+i
            elif i==")":
                BracketReader=BracketReader-1
                if BracketReader==0:
                    BracketObj=MathObjects(MObj,depth+1)
                    out.append(BracketObj[0])
                    MObj=""
                    continue
                else:
                    MObj=MObj+i
            elif i=="(":
                MObj=MObj+i
                BracketReader=BracketReader+1
                
        else:
            if MObj=="" or MObj==" ":
                if i=="-":
                    out.append(-1)
                    MObj="*"
                    continue
                else:
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
                if i == "-":
                    out.append(MObj)
                    out.append(-1)
                    MObj="*"
                    continue
                elif MObj.isalpha() and i.isalpha():
                    pass
                else:
                    out.append(MObj)
                    MObj=i
                    continue
                    
            if MObj in SupportedConstants:
                if not i.isalpha():
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
            elif MObj.isdecimal() and i.isalpha() and i not in "xlm":
                #Even jankier implementation? Possibly, but due to nature of program this should work without issue.
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
    if depth==0:
        UsedFunctions=MathOrder(out)
    return out,UsedFunctions
    
            
def MathParser(inp,UsedFunctions):
    #This function reads a list of Math Objects as returned by MathObjects and outputs the results
    #This function respects PEMDAS, but all other functions are resolved left to right(While respecting Brackets)
    #Resolve Brackets
    for i in range(len(inp)):
        if type(inp[i])==list:
            BracketResult=MathParser(inp[i],UsedFunctions)
            inp[i]=BracketResult
    #Resolving Errors
    for i in range(len(inp)):
        if i=="ERROR":
            return "ERROR"

    for f in UsedFunctions:
        while f in inp:
                    #Resolve Functions
            #This includes Trigonometry but also Hyperbolic Trigonometry and Ln(x). Basically any mathematical function that only depends on the bracket after it.
            for i in range(len(inp)):
                if inp[i] in SupportedFunctions and inp[i]==f:
                    func="Result="+"mfunc."+str(inp[i])+"("+str(inp[i+1])+")"
                    exec(func)
                    inp[i+1]=locals()["Result"]
                    inp[i]="temp"
                    break
            #Resolve Factorials
            #Because of the nature of Factorial symbol being put after a number it needs to be parsed seperately to both functions and opperators
            for i in range(len(inp)):
                if inp[i]=="!":
                    inp[i+1]=mfunc.factorial(i)
                    inp[i]="temp"
                    break
            #Resolve Log
            #Unlike Ln, Log has a base so it must be computed seperately. Currently It's in the format Base Log Value
            for i in range(len(inp)):
                if inp[i]=="log" and inp[i]==f:
                    inp[i-1]=mfunc.log(inp[i-1],inp[i+1])
                    inp[i]="temp"
                    inp[i+1]="temp"
                    break
            #Resolve Exponents
            #PEMDAS
            for i in range(len(inp)):
                if inp[i]=="^" and inp[i]==f:
                    inp[i-1]=inp[i-1]**inp[i+1]
                    inp[i]="temp"
                    inp[i+1]="temp"
                    break
            #Resolve Multiplication
            #PEMDAS
            for i in range(len(inp)):
                if (inp[i]=="*" or inp[i]=="x") and inp[i]==f:
                    inp[i-1]=inp[i-1]*inp[i+1]
                    inp[i]="temp"
                    inp[i+1]="temp"
                    break
            #Resolve Modulo
            #This returns the remainder after division, so I thought that it would be apropriate to put this here.
            for i in range(len(inp)):
                if (inp[i]=="%" or inp[i]=="mod") and inp[i]==f:
                    try:
                        inp[i-1]=inp[i-1]%inp[i+1]
                    except:
                        return "ERROR"
                    inp[i]="temp"
                    inp[i+1]="temp"
            #Resolve Division
            #PEMDAS
            for i in range(len(inp)):
                if inp[i]=="/" and inp[i]==f:
                    try:
                        inp[i-1]=inp[i-1]/inp[i+1]
                    except:
                        return "ERROR"
                    inp[i]="temp"
                    inp[i+1]="temp"
            #Resolve Addition
            #PEMDAS
            for i in range(len(inp)):
                if inp[i]=="+" and inp[i]==f:
                    inp[i-1]=inp[i-1]+inp[i+1]
                    inp[i]="temp"
                    inp[i+1]="temp"
                    break
            #Resolve Subtraction
            #PEMDAS
            for i in range(len(inp)):
                if inp[i]=="-" and inp[i]==f:
                    inp[i-1]=inp[i-1]-inp[i+1]
                    inp[i]="temp"
                    inp[i+1]="temp"
                    break
            #Removing all temp objects
            while "temp" in inp:
                inp.remove("temp")
    #Finalizing answer and verifying format
    if len(inp)!=1:
        return "ERROR"
    else:
        return round(inp[0],5)
