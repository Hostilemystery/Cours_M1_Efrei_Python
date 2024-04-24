""" 
Créez autant de variables que de types de variable en python avec “my42Type” et
détectez leurs types. Par exemple pour une variable de valeur “true” je dois retourner
“boolean” en string.

"""

entier = 42
decimal = 42.5
chaineDeCharactere = "ceci est un string"
charactere = 'C'
liste = [1,'test',True]
boolean = True
unTuple = (1,'test',True)
dictionnaire = {"key1":"val1", "key2":"val2"}
collection = {1,'test',True}
Null = None


print(f"""
        {entier} = {type(entier).__name__}
        {decimal} = {type(decimal).__name__}
        {chaineDeCharactere} = {type(chaineDeCharactere).__name__}decimal
        {charactere} = {type(charactere).__name__}
        {liste} = {type(liste).__name__}
        {boolean} = {type(boolean).__name__}
        {unTuple} = {type(unTuple).__name__}
        {dictionnaire} = {type(dictionnaire).__name__}
        {collection} = {type(collection).__name__}
        {Null} = {type(Null).__name__}
        
        """)