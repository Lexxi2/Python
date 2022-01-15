zahl1 = input("Die erste Zahl: ")
zahl2 = input("Die zweite Zahl: ")

was = input("Willst du +, -, * oder / rechnen? ")

if was == "+":
    resultat = int(zahl1) + int(zahl2)

elif was == "-":
    resultat = int(zahl1) - int(zahl2)

elif was == "*":
    resultat = int(zahl1) * int(zahl2)

elif was == "/":
    resultat = int(zahl1) / int(zahl2)

else:
    print("keine gültige Eingabe")

print(resultat)
