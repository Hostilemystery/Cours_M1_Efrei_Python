"""  
Faite en sorte de créer une fonction “is_palindrome” qui vérifie si une chaîne de
caractère est un palindrome elle devra renvoyer “True” ou “False”
"""

def is_palindrome(mot):
    mot = mot.replace(" ","").lower()
    return mot == mot[::-1]
    
print(is_palindrome("no lemon , no melon"))