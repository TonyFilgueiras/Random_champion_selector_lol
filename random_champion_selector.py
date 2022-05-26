from random import randint
from xmlrpc.client import boolean

class Champion:
    def __init__(self, name, ad:boolean, ap:boolean, top:boolean, jg:boolean, mid:boolean, bot:boolean, sup:boolean):
        self.name = name
        self.ad = ad
        self.ap = ap
        self.top = top
        self.jg = jg
        self.mid = mid
        self.bot = bot
        self.sup = sup

def error():
    print("Insert a valid input!!")

list_of_champions = [
    Champion("Zeri", True, True, False, False, True, True,False),
    Champion("Vex", False, True, False, False, True, True, True),
    Champion("Akshan", True,False,False,False,True,True,False),
    Champion("Samira", True, False, False, False, True, True, False),
    Champion("Seraphine", False, True, False, False, True, True, True),
    Champion("Rell", False, True, False, False, False, False, True),
    Champion("Viego", True, False, False, True, False, False, False),
    Champion("Gwen", False, True, True, False, False, False, False),
    Champion("Pyke", True, False, False, False, True, False, True),
    Champion("Neeko", False, True, False, False, True, True, True),
    Champion("Sylas", False, True, True, True, True, False, False),
    Champion("Yuumi", False, True, False, False, False, False, True),
    Champion("Qiyana", True, False, False, False, True, False, False),
    Champion("Senna", True, False, False, False, False, True, True),
    Champion("Aphelios", True, False, False, False, False, True, False),
    Champion("Sett", True, False, True, False, False, False, True),
    Champion("Lillia", False, True, True, True, True, False, False),
    Champion("Yone", True, False, True, True, True, False, False),
    Champion("Taliyah", False, True, False, True, True, True, True),
    Champion("Kled", True, False, True, False, True, False, False),
    Champion("Ivern", False, True, False, True, False, False, True),
    Champion("Camille", True, False, True, True, False, False, False),
    Champion("Rakan", False, True, False, False, False, False, True),
    Champion("Xayah", True, False, False, False, False, True, False),
    Champion("Kayn", True, False, False, True, False, False, False),
    Champion("Ornn", True, False, True, False, False, False, False),
    Champion("Zoe", False, True, False, False, True, True, True),
    Champion("Kai'sa", True, True, False, False, True, True, False),
    Champion("Yasuo", True, False, False, False, True, True, False),
    Champion("Yorick", True, False, True, False, False, False, False),
    Champion("Zac", False, True, False, True, False, False, False),
    Champion("Zed", True, False, False, False, True, False, False),
    Champion("Ziggs", False, True, False, False, True, True, False),
    Champion("Zilean", False, True, False, False, True, False, True),
    Champion("Zyra", False, True, False, False, True, False, True),
    Champion("Bard", False, True, False, False, False, False, True),
    Champion("Ekko", False, True, False, True, True, False, False),
    Champion("Tahm kench", False, True, True, False, False, False, True),
    Champion("Kindred", True, False, False, True, True, True, False),
    Champion("Illaoi", True, False, True, False, False, False, False),
    Champion("Jhin", True, False, False, False, False, True, False),
    Champion("Aurelion Sol", False, True, False, False, True, True, True),
    Champion("Twitch", True, True, False, False, False, True, False),
    Champion("Udyr", True, True, False, True, False, False, False),
    Champion("Urgot", True, False, True, False, False, False, False),
    Champion("Varus", True, True, False, False, True, True, False),
    Champion("Vayne", True, False, True, False, False, True, False),
    Champion("Veigar", False, True, True, False, True, True, False),
    Champion("Vel'Koz", False, True, False, False, True, False, True),
    Champion("Vi", True, False, False, True, False, False, False),
    Champion("Viktor", False, True, False, False, True, False, False),
    Champion("Vladimir", False, True, True, False, True, False, False),
    Champion("Volibear", True, True, True, True, False, False, False),
    Champion("Warwick", True, False, True, True, False, False, False),
    Champion("Wukong", True, False, True, True, True, False, False),
    Champion("Xerath", False, True, False, False, True, False, True),
    Champion("Xin Zhao", True, False, True, True, True, False, False),
    Champion("Swain", False, True, True, False, True, True, True),
    Champion("Syndra", False, True, False, False, True, True, False),
    Champion("Talon", True, False, False, False, True, False, False),
    Champion("Taric", False, True, True, False, False, False, True),
    Champion("Teemo", False, True, True, False, False, True, True),
    Champion("Thresh", False, True, False, False, False, False, True),
    Champion("Tristana", True, False, False, False, False, True, False),
    Champion("Trundle", True, False, True, True, False, False, False),
    Champion("Tryndamere", True, False, True, False, False, False, False),
    Champion("Twisted Fate", True, True, False, False, True, True, False),
    Champion("Renekton", True, False, True, False, True, False, False),
    Champion("Rengar", True, False, False, True, False, False, False),
    Champion("Riven", True, False, True, False, False, False, False),
    Champion("Rumble", False, True, True, False, True, False, False),
    Champion("Ryze", False, True, False, False, True, True, False),
    Champion("Sejuani", False, True, True, True, False, False, False),
    Champion("Shaco", True, True, False, True, False, False, False),
    Champion("Shen", True, False, True, False, False, False, True),
    Champion("Shyvana", True, True, False, True, False, False, False),
    Champion("Singed", False, True, True, False, False, False, False),
    Champion("Sion", True, False, True, False, False, False, False),
    Champion("Sivir", True, False, False, False, True, True, False),
    Champion("Skarner", True, True, False, True, False, False, False),
    Champion("Sona", False, True, False, False, True, True, True),
    Champion("Soraka", False, True, False, False, False, False, True),
    Champion("Mordekaiser", False, True, True, False, False, False, False),
    Champion("Morgana", False, True, False, False, True, False, True),
    Champion("Nami", False, True, False, False, False, False, True),
    Champion("Nasus", True, True, True, False, False, False, False),
    Champion("Nautilus", False, True, False, False, False, False, True),
    Champion("Nidalee", False, True, False, True, True, True, True),
    Champion("Nocturne", True, False, True, True, True, False, False),
    Champion("Nunu", False, True, True, True, True, False, False),
    Champion("Olaf", True, False, True, True, False, False, False),
    Champion("Orianna", False, True, False, False, True, True, True),
    Champion("Pantheon", True, False, True, True, True, False, True),
    Champion("Poppy", True, False, True, True, False, False, True),
    Champion("Quinn", True, False, True, False, False, True, False),
    Champion("Rammus", False, True, False, True, False, False, False),
    Champion("Rek'Sai", True, False, False, True, False, False, False),
    Champion("Leona", True, True, False, False, False, False, True),
    Champion("Lissandra", False, True, False, False, True, True, False),
    Champion("Lucian", True, False, False, False, True, True, False),
    Champion("Lulu", True, True, False, False, True, True, True),
    Champion("Lux", False, True, False, False, True, True, True),
    Champion("Malphite", False, True, True, False, False, False, False),
    Champion("Malzahar", False, True, False, False, True, False, False),
    Champion("Maokai", False, True, True, False, False, False, True),
    Champion("Master Yi", True, False, False, True, False, False, False),
    Champion("Miss Fortune", True, False, False, False, False, True, False),
    Champion("Karma", False, True, False, False, True, False, True),
    Champion("Karthus", False, True, False, True, True, True, False),
    Champion("Kassadin", False, True, False, False, True, False, False),
    Champion("Katarina", True, True, False, False, True, False, False),
    Champion("Kayle", True, True, True, False, True, False, True),
    Champion("Kennen", False, True, True, False, True, True, False),
    Champion("Kha'Zix", True, False, False, True, False, False, False),
    Champion("Kog'Maw", True, True, False, False, True, True, False),
    Champion("LeBlanc", False, True, False, False, True, False, False),
    Champion("Lee Sin", True, False, False, True, False, False, True),
    Champion("Evelynn", False, True, False, True, False, False, False),
    Champion("Ezreal", True, True, False, False, True, True, False),
    Champion("Fiddlesticks", False, True, False, True, False, False, False),
    Champion("Fiora", True, False, True, False, False, False, False),
    Champion("Fizz", False, True, False, False, True, False, False),
    Champion("Galio", False, True, True, False, True, False, True),
    Champion("Gangplank", True, False, True, False, False, False, False),
    Champion("Garen", True, False, True, False, False, False, False),
    Champion("Gnar", True, False, True, False, False, True, False),
    Champion("Gragas", False, True, False, True, False, False, False),
    Champion("Graves", True, False, False, True, False, False, False),
    Champion("Hecarim", True, False, False, True, False, False, False),
    Champion("Heimerdinger", False, True, False, False, True, True, False),
    Champion("Irelia", True, False, True, False, True, False, False),
    Champion("Janna", False, True, False, False, False, False, True),
    Champion("Jarvan IV", True, False, False, True, False, False, False),
    Champion("Jax", True, False, True, False, False, False, False),
    Champion("Jayce", True, False, True, False, True, True, False),
    Champion("Jinx", True, False, False, False, False, True, False),
    Champion("Kalista", True, False, False, False, False, True, False),
    Champion("Aatrox", True, False, True, False, False, False, False),
    Champion("Ahri", False, True, False, False, True, False, True),
    Champion("Akali", False, True, True, False, True, False, False),
    Champion("Alistar", False, True, False, False, False, False, True),
    Champion("Amumu", False, True, True, True, False, False, True),
    Champion("Anivia", False, True, False, False, True, True, True),
    Champion("Annie", False, True, False, False, True, False, True),
    Champion("Ashe", True, False, False, False, False, True, True),
    Champion("Azir", False, True, False, False, True, False, False),
    Champion("Blitzcrank", False, True, False, False, False, False, True),
    Champion("Brand", False, True, False, False, True, False, True),
    Champion("Braum", False, True, False, False, False, False, True),
    Champion("Caitlyn", True, False, False, False, False, True, False),
    Champion("Cassiopeia", False, True, False, False, True, True, False),
    Champion("Cho'Gath", False, True, True, False, False, False, False),
    Champion("Corki", True, True, False, False, True, True, False),
    Champion("Darius", True, False, True, False, False, False, False),
    Champion("Diana", False, True, False, True, True, False, False),
    Champion("Dr. Mundo", False, True, True, False, False, False, False),
    Champion("Draven", True, False, False, False, False, True, False),
    Champion("Elise", False, True, False, True, False, False, False),
    Champion("Renata Glasc",False,True,False,False,False,False,True)
    
]

loop = ' '
while loop != "N":
    role = " "
    selection1= ["1","2","3","4","5","6"]
    selection2=["1","2","3"]
    while role not in selection1:
        role = input('''Which role you would like to play? 
[1] Top
[2] Jg
[3] Mid
[4] Bot
[5] Sup
[6] Any

Your choice: ''')
        if role not in selection1:
            error()

    damage_type=''

    while damage_type not in selection2:
        damage_type = input('''Ap or Ad??
[1] Ap
[2] Ad
[3] Any

Your choice: ''')
        if damage_type not in selection2:
            error()



    possible_choices = []

    if role == "1" and damage_type == "3":
        for i in list_of_champions:
            if i.top == True:
                possible_choices.append(i.name)
    elif role == "1" and damage_type == "1":
        for i in list_of_champions:
            if i.top == True and i.ap==True:
                possible_choices.append(i.name)
    elif role == "1" and damage_type == "2":
        for i in list_of_champions:
            if i.top == True and i.ad==True:
                possible_choices.append(i.name)
    elif role == "2" and damage_type == "3":
        for i in list_of_champions:
            if i.jg == True:
                possible_choices.append(i.name)
    elif role == "2" and damage_type == "1":
        for i in list_of_champions:
            if i.jg == True and i.ap==True:
                possible_choices.append(i.name)
    elif role == "2" and damage_type == "2":
        for i in list_of_champions:
            if i.jg == True and i.ad==True:
                possible_choices.append(i.name)
    elif role == "3" and damage_type == "3":
        for i in list_of_champions:
            if i.mid == True:
                possible_choices.append(i.name)
    elif role == "3" and damage_type == "1":
        for i in list_of_champions:
            if i.mid == True and i.ap==True:
                possible_choices.append(i.name)
    elif role == "3" and damage_type == "2":
        for i in list_of_champions:
            if i.mid == True and i.ad==True:
                possible_choices.append(i.name)
    elif role == "4" and damage_type == "3":
        for i in list_of_champions:
            if i.bot == True:
                possible_choices.append(i.name)
    elif role == "4" and damage_type == "1":
        for i in list_of_champions:
            if i.bot == True and i.ap==True:
                possible_choices.append(i.name)
    elif role == "4" and damage_type == "2":
        for i in list_of_champions:
            if i.bot == True and i.ad==True:
                possible_choices.append(i.name)
    elif role == "5" and damage_type == "3":
        for i in list_of_champions:
            if i.sup == True:
                possible_choices.append(i.name)
    elif role == "5" and damage_type == "1":
        for i in list_of_champions:
            if i.sup == True and i.ap==True:
                possible_choices.append(i.name)
    elif role == "5" and damage_type == "2":
        for i in list_of_champions:
            if i.sup == True and i.ad==True:
                possible_choices.append(i.name)
    else:
        for i in list_of_champions:
            possible_choices.append(i.name)

    print(f'''possible choices --- 
------------------------------------------------------------------------------------------------------
{possible_choices}
-------------------------------------------------------------------------------------------------------''')

    print(f"Your champion --> {possible_choices[randint(0, len(possible_choices))]}")

    loop = input("Go again??: [Y/N] ").upper()