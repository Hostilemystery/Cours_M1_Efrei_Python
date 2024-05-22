""" 
 Faite en sorte de créer une fonction “validMyInternationalPhone” qui contrôle un
 numéro de téléphone passé en argument et l’indicatif du pays concerné dans un second
 argument. Vous devrez vérifier et faire en sorte que les numéros Français et des
 Etats-Unis renvoient “True” si le numéro est compatible avec le pays du second
 argument et “False” dans le cas contraire.
"""
import re
def validMyInternationalPhone(numero,indicatif):
    pattern = {
        'FR': r'^(?:\+33|0)([1-9]\d{8})$',
        'US': r'^(?:\+1|1)?([2-9]\d{9})$'
    }
    espaceNumero = re.sub(r'\D', '', numero)
    if indicatif in pattern:
        if re.match(pattern[indicatif], numero):
            return True
    return False
    
    

print(validMyInternationalPhone('+33123456789', 'FR'))  
print(validMyInternationalPhone('+12345678900', 'US'))  






