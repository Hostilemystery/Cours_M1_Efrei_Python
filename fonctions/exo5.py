"""  
 Vous devez réaliser une horloge numérique en affichant l’heure actuelle en temps réel.
 Cette horloge devra être actualisée toutes les secondes.
 Resultat attendu :
 23:00 1 seconde après-> 23:01 etc …

"""

from datetime import datetime
import time

def horloge () :
    while True:
        current_time = datetime.now()
        print("Il est :", current_time.strftime("%H:%M:%S"))
        time.sleep(1) 

horloge()