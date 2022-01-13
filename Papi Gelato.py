
meerbestellen = 'j'
abakje = 0
ahoorn = 0
atopping = 0
eurotopping = 0
particulier = 'j'
zakelijk = 'j'

print('“Welkom bij Papi Gelato”')

def parofzakelijk():
    vrzakelijk = input("Bent u (1) particulier of (2) zakelijk?")
    if vrzakelijk == '1':
        global bolliter
        global particulier
        global zakelijk
        particulier = 'j'
        zakelijk = 'n'
        bolliter = 'bolletjes'
        return vrzakelijk
    if vrzakelijk == '2':
        particulier = 'n'
        zakelijk = 'j'
        bolliter = 'liter'
        return vrzakelijk
    else:
        print("Sorry, dat snap ik niet...")
        

def ijs():
    input("Druk op enter om te bestellen.")
    print(" -------")
    bolletjes = int(input(f"Hoeveel {bolliter} wilt u? :"))
    if vrzakelijk == '1':
        if bolletjes == 1 or bolletjes == 2 or bolletjes == 3:
            return bolletjes
        elif bolletjes == 4 or bolletjes == 5 or bolletjes == 6 or bolletjes == 7 or bolletjes == 8:
            print(f"Dan krijgt u van mij een bakje met {bolletjes} bolletjes.")
            return bolletjes
        elif bolletjes > 8:
            print("Sorry, zulke grote bakken hebben niet.")
        else:
            print("Sorry, dat snap ik niet...")
    if vrzakelijk == '2':
        bolletjes >= 1
        print(f"Dan krijgt u van mij {bolletjes} liter.")
        return bolletjes


def smaken():
    Sbolletjes = 1
    while Sbolletjes <= bolletjes:
        smaak = input(f"Welke smaak wilt u voor {bolliter} nummer {Sbolletjes}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
        if smaak == 'a' or 'c' or 'm' and 'v':
            Sbolletjes += 1
        else:
            print("Sorry dat snap ik niet...")
        
    
def bakjehoorntje():
    while bolletjes < 4:
        bakhoorn = input(f"Wilt u deze {bolletjes} bolletje(s) in een bakje (a) of hoorntje (b) :").lower()
        if bakhoorn == 'a':
            global abakje
            bakhoorn = 'bakje'
            abakje =+ 1
            return bakhoorn
        elif bakhoorn == 'b':
            global ahoorn
            bakhoorn = 'hoorntje'
            ahoorn =+ 1
            return bakhoorn   
        else:
            print("Sorry, dat snap ik niet...")

def toppings():
    topping = input(f"Wat voor topping wilt u: (a) Geen, (b) Slagroom, (c) Sprinkels of (d) Caramel Saus?")
    global atopping
    if topping == 'a':
        topping = 0
        return topping
    if topping == 'b':
        topping = 0.50
        atopping =+ 1
        return topping
    if topping == 'c':
        topping = 0.30
        atopping =+ 1
        return topping
    if topping == 'd':
        atopping =+ 1
        if bakhoorn == 'a':
            topping = 0.90
            return topping
        elif bakhoorn == 'b':
            topping = 0.60
            return topping
    else:
        print("Sorry dat snap ik niet...")


def verderbestellen():
    while bolletjes < 4:
        meerbestellen = input(f"Hier is uw {bakhoorn} met {bolletjes} bolletje(s). Wilt u nog meer bestellen? j/n :").lower()
        if meerbestellen == 'j':
            return meerbestellen
        elif meerbestellen == 'n':
            return meerbestellen
        else:
            print("Sorry, dat snap ik niet...")
    while bolletjes >= 4:
        meerbestellen = input(f"Hier is uw bakje met {bolletjes} bolletje(s). Wilt u nog meer bestellen? j/n :").lower()
        if meerbestellen == 'j':
            return meerbestellen
        elif meerbestellen == 'n':
            print("Bedankt en tot ziens!")
            return meerbestellen
        else:
            print("Sorry, dat snap ik niet...")

def bonnetje():
        if particulier == 'j' and zakelijk == 'n':
            input("Druk op enter om uw bonnetje te zien.")

            eurobolletje = bolletjes * 0.95
            eurohoorn = ahoorn * 1.25
            eurobakje = abakje * 0.75
            if eurotopping >= 0.10:
                atopping * topping
                
            eurototaal = eurobolletje + eurobakje + eurohoorn + topping
                    
            print("---------[ Papi Gelato ]---------")
            print("""
            """)
            print(f"Bolletjes    {bolletjes} x €0.95    = € {round(eurobolletje, 2)}")
            print(f"Horrentje    {ahoorn} x €1,25    = € {round(eurohoorn, 2)}")
            print(f"Bakje        {abakje} x €0,75    = € {round(eurobakje, 2)}")
            print(f"Toppings     {atopping} x €{topping}     = € {round(topping, 2)}")
            print("""
                                -------- +""")
            print(f"Totaal                    = € {round(eurototaal, 2)}")
            
        elif particulier == 'n' and zakelijk == 'j':
            input("Druk op enter op uw bonnetje te zien.")


            euroliter = bolletjes * 9.80
            btw = euroliter / 100 * 6
            print("---------[ Papi Gelato ]---------")
            print("""
            """)
            
            print(f"Liter       {bolletjes} x 9.80  = {round(euroliter, 2)}")  
            print("""
                                -------- +""")  
            print(f"Totaal                    = € {round(euroliter, 2)}")
            print(f"BTW (6%)                  = € {round(btw, 2)}")
            

# einde
vrzakelijk = parofzakelijk()
if particulier == 'j' and zakelijk == 'n':
    while particulier == 'j' and zakelijk == 'n':
        if particulier == 'j':
            bolletjes = ijs()
            smaak = smaken()
            bakhoorn = bakjehoorntje()
            topping = toppings()
            particulier = verderbestellen()
    particulier = 'j'
    bonnetje()
    particulier = 'n'
elif particulier == 'n' and zakelijk == 'j':
    if zakelijk == 'j':
        bolletjes = ijs()
        smaak = smaken()
        bonnetje()

input("Druk op enter om het aftesluiten")



