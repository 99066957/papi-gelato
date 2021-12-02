opnieuw = 'j'

print('“Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.”')

def ijs():
    input("Druk op enter om te bestellen.")
    print(" -------")
    bolletjes = int(input("Hoeveel bolletjes wilt u? :"))
    if bolletjes == 1 or bolletjes == 2 or bolletjes == 3:
        return bolletjes
    elif bolletjes == 4 or bolletjes == 5 or bolletjes == 6 or bolletjes == 7 or bolletjes == 8:
        print(f"Dan krijgt u van mij een bakje met {bolletjes} bolletjes.")
        return bolletjes
    elif bolletjes > 8:
        print("Sorry, zulke grote bakken hebben niet.")
    else:
        print("Sorry, dat snap ik niet...")

def bakjehoorntje():
    while bolletjes < 4:
        bakhoorn = input(f"Wilt u deze {bolletjes} bolletje(s) in een bakje (a) of hoorntje (b) :").lower()
        if bakhoorn == 'a':
            bakhoorn = 'bakje'
            return bakhoorn
        elif bakhoorn == 'b':
            bakhoorn = 'hoorntje'
            return bakhoorn   
        else:
            print("Sorry, dat snap ik niet...")

def verderbestellen():
    while bolletjes < 4:
        meerbestellen = input(f"Hier is uw {bakhoorn} met {bolletjes} bolletje(s). Wilt u nog meer bestellen? j/n :").lower()
        if meerbestellen == 'j':
            opnieuw ==  True
            return meerbestellen
        elif meerbestellen == 'n':
            print("Bedankt en tot ziens!")
            input("Druk op enter om het aftesluiten.")
            exit()
        else:
            print("Sorry, dat snap ik niet...")
    while bolletjes >= 4:
        meerbestellen = input(f"Hier is uw bakje met {bolletjes} bolletje(s). Wilt u nog meer bestellen? j/n :").lower()
        if meerbestellen == 'j':
            opnieuw ==  True
            return meerbestellen
        elif meerbestellen == 'n':
            print("Bedankt en tot ziens!")
            input("Druk op enter om het aftesluiten.")
            exit()
        else:
            print("Sorry, dat snap ik niet...")


while opnieuw == 'j':
    bolletjes = ijs()
    bakhoorn = bakjehoorntje()
    meerbestellen = verderbestellen()
input("Druk op enter om het aftesluiten.")


