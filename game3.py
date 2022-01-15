# Game 3
# Mit Zahlen rechnen:
# Was können wir mit Zahlen machen in Python?

#1 Zahlen ausdrucken mit dem print Befehl:
print(1)
print(52)

#2 Direcktes ausrechnen:
print(2+5)
print(8-3)
print(2*2)
#3 Rechnen mit Klammern:
print(1 + (2*2))

#4 Zahlen wählen und speichern:
meine_Zahl = 22
zahl2 = 3
zahl3 = "5"   # Der Computer denkt jetzt, dass 5 eigentlich ein Wort ist und keine Zahl, das ist aber nicht schlimm

#5 Gespeicherte Zahlen benutzen:
print(meine_Zahl + zahl2)
print(zahl2 + int(zahl3)) # Wir müssen zahl3 in eine richtige Zahl verwandeln sonst kann der Computer nicht damit rechnen.
# Also vor zahl3 int, das bedeutet für den Computer Zahl (Englisch: integer)




#6 Wir programmieren jetzt einen Taschenrechner, für +

# Der Taschenrechner soll uns am Anfang nach den Zahlen fragen:
# Wie wir früher schon gelernt haben benutzen wir input
Zahl1 = input("Die erste Zahl: ")
Zahl2 = input("Die zweite Zahl: ")

# Wir sagen dem Computer, er soll das Resultat ausrechnen:
# Resultat = zahl1 + zahl2
Resultat = int(Zahl1) + int(Zahl2)  # Jetzt brauchen wir wieder int, damit der Computer versteht, dass es Zahlen sind

# Am Schluss wollen wir das Resultat ausdrucken, mit print:
print("Das Resultat ist: ")
print(Resultat)

# Der Taschenrechner ist fertig!
