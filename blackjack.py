import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

print("Do you want to play a game of blackjack? y/n: ")
wana_play = input()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
jatekos_kez = []
haz_kez = []
#megvan az inic menjünk át a logikán, tehát az y esetén húzunk a játékosnak 2 kártyát a háznak pedig 1 et és megkérdezzük, hogy akar e húzni méggegyet.
#egy comparator fogja a játék 3 állapotát vizsgálni 

house_vs_player = False

def comparator(value1,value2,house_vs_player):
    if house_vs_player == False:
        if value1 > 21:
            return True
        else:
            return False
    else:
        if value1 > value2:
            print(f"A játékos nyert!: {jatekos_kez}\nHáz kéz: {haz_kez}")
        if value2 > value1:
            print(f"A ház nyert!: {haz_kez}\nJátékos kéz: {jatekos_kez}")
        else:
            print("Döntetlen!")

#kártyahúzás és shuffle

random.shuffle(cards)

def kartyat_huz(cards):
    random_kartya = cards[random.randint(0,len(cards)-1)]
    return random_kartya

#inic pakli
#játékos ciklus beleágyazva ház ciklus

def inic():
    for i in range(2):
        jatekos_kez.append(kartyat_huz(cards))
    haz_kez.append(kartyat_huz(cards))

def hand_ertek_szamolo(kez):
    sum = 0
    for i in kez:
        sum += i
    return sum

#szóval comparator fv igaz v hamis értéket ad vissza a játékos kezének függvényében 
#arra gondoltam, hogy a játékos kártyakérő ciklusából a kilépést azt valósítaná meg ha a ház kártyahúzó ciklusa is a kartyat kér false-t vár mert ha truet kap
#vagyis átlépte a 21 et akkor abba a ciklusba ne tudjon belépni már és megaszakítsa a főciklust mivel veszített a játékos 


if wana_play == "y":
    jatek = True
    while(jatek):
        jatekos_kez.clear()
        haz_kez.clear()
        inic()
        print(f"This is your hand: {jatekos_kez}\nThis is the houses hand: {haz_kez}")
        keres = True
        while(keres):
            print(f"Do you want another card? y/n")
            valasz = input()
            jatekos_veszit = False
            if valasz == "y":
                jatekos_kez.append(kartyat_huz(cards))
                print(f"Your actual hand: {jatekos_kez}")
                if (comparator(hand_ertek_szamolo(jatekos_kez),0,house_vs_player)):
                    jatekos_veszit = True
                    keres = False
            else:
                keres = False
        if jatekos_veszit:
            print(f"You lose! {jatekos_kez}")
        else:
            haz_huz = True
            while(haz_huz):
                haz_veszit = False
                haz_kez.append(kartyat_huz(cards))
                print(f"House hand: {haz_kez}")
                print(hand_ertek_szamolo(haz_kez))
                if hand_ertek_szamolo(haz_kez) >= 16 or hand_ertek_szamolo(haz_kez) < 17 or hand_ertek_szamolo(haz_kez) > 21:
                    if (comparator(hand_ertek_szamolo(haz_kez),0,house_vs_player)):
                        haz_veszit = True
                        haz_huz = False
                else:
                    house_vs_player = True
                    haz_huz = False
            if (haz_veszit):
                print(f"You're winner! {jatekos_kez}\nHouse hand: {haz_kez}")
            else:
                comparator(hand_ertek_szamolo(jatekos_kez),hand_ertek_szamolo(haz_kez),house_vs_player)
        print("Do you wanna play again ? y/n")
        akarsz_meg = input()
        if akarsz_meg == "n":
            jatek = False
else:
    print("Then bye!")


