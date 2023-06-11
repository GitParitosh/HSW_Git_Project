import MathParser as m
ErrorMessage='''There was an error in the program.
Input expression maybe invalid, if you believe that this is not the case please contact the developers


'''
while True:
    Result=''
    print('''Welcome to the Calculator, here you can calculate mathematical expressions using common symbols
Type H or Help to go to learn about supported functions
Type any Mathematical expression and press enter to get answer
Type c or Close to Close calculator''')
    inp=input("")
    inp=inp.lower()
    if inp=="h" or inp=="help":
        print('''
Enter Help Message here, WIP''')
    else:
        try:
            Result=m.MathParser(m.MathObjects(inp))
        except Exception as e:
            Result="ERROR"
        if Result=="ERROR":
            print(ErrorMessage)
        else:
            print(Result)
