""" 
Utilisez le “match” pour déterminer le jour de la semaine avec “datetime”. Si nous
sommes lundi vous devrez reconnaître que nous sommes lundi et afficher “nous
sommes {jour}”. Faites cela pour tous les autres jours de la semaine.

"""
import datetime
# jours = datetime.datetime.now().strftime("%A")

jours = datetime.datetime.now().weekday()
jours_fr = {
    0: "Lundi",
    1: "Mardi",
    2: "Mercredi",
    3: "Jeudi",
    4: "vendredi",
    5: "Samedi",
    6: "Dimanche",}



match jours : 
    case 0 :
        print(f"Nous sommes {jours_fr[jours]}")
    case 1 :
        print(f"Nous sommes {jours_fr[jours]}")
    case 2 :
        print(f"Nous sommes {jours_fr[jours]}")
    case 3 :
        print(f"Nous sommes {jours_fr[jours]}")
    case 4 :
        print(f"Nous sommes {jours_fr[jours]}")
    case 5 :
        print(f"Nous sommes {jours_fr[jours]}")
    case 6 :
        print(f"Nous sommes {jours_fr[jours]}")