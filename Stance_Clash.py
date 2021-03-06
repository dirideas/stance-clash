import EvenementIDLE
import EvenementKaart
import random
from btn import *

def setup():
    global scherm, evenement
    EvenementKaart.setup()
    size(1920,1080)
    scherm = 8
    evenement = 0
    
######## Mijn Titleschreen met de button naar Evenement ###########

def draw():
    # Functie welk scherm moet gedrawed worden
    global scherm, evenementlist, randomlist
    if scherm == 8:
        background(150,200,225)
        # Titel
        textSize(200)
        fill(225)
        text("Stance Clash", width/4 - 100, height/2 - 200)
        fill(225)
        # Event Button
        textSize(85)
        x = buttons[11]
        rectFromDict(x)
    elif scherm == 9:
        EvenementIDLE.draw()
        if scherm == 10:
            EvenementKaart.draw()
    # lijst met alle evenementen
    
    

# Werking achter de Event button & terug button
def mousePressed():
    global scherm, evenement, randomlist
    # Functie voor EVENT button
    if scherm == 0:
        if width/2 - 200 <= mouseX and mouseX <= width/2 + 200 and height/2 + 50 <= mouseY and mouseY <= height/2 + 250:
            scherm = 1
    # Functie voor BACK button
    elif scherm == 1 and evenement != 1:
        if width/2 - 200 <= mouseX and mouseX <= width/2 + 200 and height/2 + 50 <= mouseY and mouseY <= height/2 + 250:
            scherm = 0
        
    # Functie voor start Evenement button
        if width/2 - 200 <= mouseX and mouseX <= width/2 + 200 and 340 <= mouseY and mouseY <= 540:
            evenement = 1
            EvenementKaart.evenementkaart()
    # Functie back button (in evenement kaart)
    elif scherm == 1:
        if 820 <= mouseX and mouseX <= 1020 and 850 >= mouseY and mouseY >= 750:
            evenement = 0 
