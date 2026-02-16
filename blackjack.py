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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
jatekos_kez = []
haz_kez = []

#megvan az inic menjünk át a logikán, tehát az y esetén húzunk a játékosnak 2 kártyát a háznak pedig 1 et és megkérdezzük, hogy akar e húzni méggegyet.
#egy comparator fogja a játék 3 állapotát vizsgálni 

house_vs_player = False

def comparator(value1,value2,house_vs_player):
    if house_vs_player == False:
        if value1 <= 21:
            return True
        else:
            return False
    else:
        if value1 > value2:
            print("A játékos nyert!")
        if value2 > value1:
            print("A ház nyert!")
        else:
            print("Döntetlen!")

#kártyahúzás és shuffle

def kartyat_huz(cards):
    random.shuffle(cards)
    random_kartya = cards[random.randint(0,len(cards))]
    return random_kartya

#játékos ciklus beleágyazva ház ciklus

while(kartyat_ker):
    kartyak_ker = True
