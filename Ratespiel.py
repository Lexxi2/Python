#Zahl raten
from random import randint

# Wir generieren eine zufällige Zahl; wir könnten die Zahl auch vorgeben, wenn wir möchten.
zahl= randint(1,10)

# Die Frage nach dem ersten Versuch und wir zählen die Versuche.
guess= int( input("Rate die Zahl? ") )
versuche= 1

# Solange die Geratene Zahl nicht gleich der Gesuchten Zahl ist wird while ausheführt
while guess != zahl:
    guess = int( input("Die Zahl war leider falsch, rate nochmals: ") )

    if guess > zahl: # Wir geben Hinweise damit das Spiel etwas einfacher wird.
        print("Die Zahl ist kleiner als dein Tipp.")

    elif guess < zahl:
        print("Die Zahl ist grösser als dein Tipp.")
    versuche = versuche + 1

# Dieser Code ist ausserhalb des while, also wenn guess=zahl, dann wird dieser Code ausgeführt
print("Richtig du hast die Zahl erraten! Die Zahl war: " + str(zahl))
print("Du hast " + str(versuche) + " Versuche gebraucht.")
