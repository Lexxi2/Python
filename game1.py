#Game 1

# Einfaches Spiel mit Print-Statements und user input

# Aufgabe 1 Print-Statement
print( " " )   #Die Form, Text zwischen die Grünen Striche
print( " Hallo " )
print("Hallo Name")





# Aufgabe 2 Informationen speichern
name = " Alexa "   # Alexa wird in name gespeichert
alter = " 21 "    # hier wird das Alter 21 in alter gespeichert
# Wie?
name_der_information = "Information"
# es können auch andere Dinge gespeichert werden wie zum Beispiel:
ich_bin_gross = True    # Ein Wahr oder Falsch Wert: True/False
# Mehrere Wörter werden mit _ getrennt aber ohne Abstand

# Jetzt wissen wir wie wir Informationen speichern können, wir wollen jetzt nach Informationen Fragen!
# Wie fragt man nach Informationen?
input("Wie heisst du? ")   # wir schreiben  input()
# den Text nennt man "promt", die Aufforderung
# jetzt müssen wir die Antwort jedoch noch speichern, also:
name = input("Wie heisst du? ")   # Jetzt wird die Information in name gespeichert.

# jetzt könne wir mit der Information arbeiten:
print(name)     #hier müssen wir keine grünen Striche mehr machen " " , probier es aus


""""

# Aufgabe 3 Ein Gespräch:
print("Hallo ich bin PC, ")
name = input("wer bist du? ")
print("Schön dich kennen zu lernen " + name)

alter = input("Wie alt bist du? ")
print("Aha, du bist also " + alter + " Jahre alt.")

lieblingstier = input("Und was ist dein Lieblingstier, wenn ich fragen darf? ")
LieblingstierPC = "der Hase"
print(lieblingstier + ", das ist ein cooles Tier, mein Lieblingstier ist " + LieblingstierPC + ".")


"""