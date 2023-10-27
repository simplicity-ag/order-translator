#Mein Programm Marlon Dinter

#Alle Variablen
Name = input("Wie heist du: ")
Wem = input("An Wem: ")
Age = input("Wie Allt wirt er/sie: ")
ManOderFrau = int(input("Wer ist es 1=Mann 0=Frau: "))


if(ManOderFrau == 1):
    print("Alles Gute Zum Geburstag Lieber " + Wem + " Wünscht dir " + Name + " Du hast ein tolles Alter mit " + Age + " Lasse dich schön feiern")
    pause = input("beenden enter")
    print(pause)
else:
    print(
        "Alles Gute Zum Geburstag Liebe " + Wem + " Wünscht dir " + Name + " Du hast ein tolles Alter mit " + Age + " Lasse dich schön feiern")
    pause = input("beenden enter")
    print(pause)