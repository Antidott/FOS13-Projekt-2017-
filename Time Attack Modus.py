#Time Attack Modus

import time

def Countdown():
    sec = 0
    while sec != 15: #mehr Zeit bei schwereren Aufgaben?
        time.sleep(1)
        sec += 1
        x = 15 - int(sec)
        y = str('Seconds left: ') + str(x)
        print(y) #erwünscht?
        if sec == 15: #mehr Zeit bei schwereren Aufgaben?
            return 'Die Zeit ist abgelaufen.' #erwünscht?
            # Hier ergänzen: Skip zur nächsten Aufgabe

print(Countdown())
