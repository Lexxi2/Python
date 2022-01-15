# Game 2
# Wir wollen versuchen einen einfachen zufalls-Würfel zu programmieren:
# Dafür brauchen wir die Funktion "Zufall". wir importieren diese so:

from random import randint
# random heisst zufällig auf englisch

# Jetzt brauchen wir eine Zahl, wir nennen sie x
x = randint(1,6)  # (1,6) ist die grösste und kleinste Zahl die unser Würfel machen kann und natürlich alle dazwischen
print("Würfeln:")  # Wir werfen den Würfel und drucken nachher gleich die Zahl aus.
print(x)

# Wir können natürlich auch eine viel grössere auswahl von Zahlen machen, dafür müssen wir einfach (1,6) ändern. zb (1,20)
