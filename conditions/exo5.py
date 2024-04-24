""" 
Faites une condition ternaire qui teste si une variable existe ou non. Si elle n’existe pas
écrivez “cette variable n’existe pas” autrement écrivez “42”.

"""
variable = 32

test = "42" if locals().get("variable") else "cette variable n'existe pas"

print(test)