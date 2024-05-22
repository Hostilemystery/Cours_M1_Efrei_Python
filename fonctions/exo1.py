""" 
Vous devez créer une fonction “myPutStr” cette fonction doit permettre de retourner un
String. Si c’est un nombre retournez “et pourquoi pas 42 ?”.
"""


def myPutStr(myVar):
    if type(myVar) == int:
        return "et pourquoi pas 42 ?"
    else:
        return str(myVar)
   


print(myPutStr("Test"))
print(myPutStr(4))