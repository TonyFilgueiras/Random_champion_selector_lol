from random import randint
from xmlrpc.client import boolean

class Champion:
    def __init__(self, name, damage_type:list, top:boolean, jg:boolean, mid:boolean, bot:boolean, sup:boolean):
        self.name = name
        self.damage_type = damage_type
        self.top = top
        self.jg = jg
        self.mid = mid
        self.bot = bot
        self.sup = sup

def error():
    print("Insert a valid input!!")

list_of_champions = [
    Champion("Zeri", ["ad", "ap"], False, False, True, True,False),
    Champion("Vex", ["ap"], False, False, True, True, True),
    Champion("Akshan", ["ad"], False,False,True,True,False),
    Champion("Samira", ["ad"], False, False, True, True, False),
    Champion("Seraphine", ["ap"], False, False, True, True, True),
    Champion("Rell", ["ap"], False, False, False, False, True),
    Champion("Viego", ["ad"], False, True, False, False, False),
    Champion("Gwen", ["ap"], True, False, False, False, False),
    Champion("Pyke", ["ad"], False, False, True, False, True),
    Champion("Neeko", ["ap"], False, False, True, True, True),
    Champion("Sylas", ["ap"], True, True, True, False, False),
    Champion("Yuumi", ["ap"], False, False, False, False, True),
    Champion("Qiyana", ["ad"], False, False, True, False, False),
    Champion("Senna", ["ad"], False, False, False, True, True),
    Champion("Aphelios", ["ad"], False, False, False, True, False),
    Champion("Sett", ["ad"], True, False, False, False, True),
    Champion("Lillia", ["ap"], True, True, True, False, False),
    Champion("Yone", ["ad"], True, True, True, False, False),
    Champion("Taliyah", ["ap"], False, True, True, True, True),
    Champion("Kled", ["ad"], True, False, True, False, False),
    Champion("Ivern", ["ap"], False, True, False, False, True),
    Champion("Camille", ["ad"], True, True, False, False, False),
    Champion("Rakan", ["ap"], False, False, False, False, True),
    Champion("Xayah", ["ad"], False, False, False, True, False),
    Champion("Kayn", ["ad"], False, True, False, False, False),
    Champion("Ornn", ["ad"], True, False, False, False, False),
    Champion("Zoe", ["ap"], False, False, True, True, True),
    Champion("Kai'sa", ["ad", "ap"], False, False, True, True, False),
    Champion("Yasuo", ["ad"], False, False, True, True, False),
    Champion("Yorick", ["ad"], True, False, False, False, False),
    Champion("Zac", ["ap"], False, True, False, False, False),
    Champion("Zed", ["ad"], False, False, True, False, False),
    Champion("Ziggs", ["ap"], False, False, True, True, False),
    Champion("Zilean", ["ap"], False, False, True, False, True),
    Champion("Zyra", ["ap"], False, False, True, False, True),
    Champion("Bard", ["ap"], False, False, False, False, True),
    Champion("Ekko", ["ap"], False, True, True, False, False),
    Champion("Tahm kench", ["ap"], True, False, False, False, True),
    Champion("Kindred", ["ad"], False, True, True, True, False),
    Champion("Illaoi", ["ad"], True, False, False, False, False),
    Champion("Jhin", ["ad"], False, False, False, True, False),
    Champion("Aurelion Sol", ["ap"], False, False, True, True, True),
    Champion("Twitch", ["ad", "ap"], False, False, False, True, False),
    Champion("Udyr", ["ad", "ap"], False, True, False, False, False),
    Champion("Urgot", ["ad"], True, False, False, False, False),
    Champion("Varus", ["ad", "ap"], False, False, True, True, False),
    Champion("Vayne", ["ad"], True, False, False, True, False),
    Champion("Veigar", ["ap"], True, False, True, True, False),
    Champion("Vel'Koz", ["ap"], False, False, True, False, True),
    Champion("Vi", ["ad"], True, True, False, False, False),
    Champion("Viktor", ["ap"], False, False, True, False, False),
    Champion("Vladimir", ["ap"], True, False, True, False, False),
    Champion("Volibear", ["ad", "ap"], True, True, False, False, False),
    Champion("Warwick", ["ad"], True, True, False, False, False),
    Champion("Wukong", ["ad"], True, True, True, False, False),
    Champion("Xerath", ["ap"], False, False, True, False, True),
    Champion("Xin Zhao", ["ad"], True, True, True, False, False),
    Champion("Swain", ["ap"], True, False, True, True, True),
    Champion("Syndra", ["ap"], False, False, True, True, False),
    Champion("Talon", ["ad"], False, False, True, False, False),
    Champion("Taric", ["ap"], True, False, False, False, True),
    Champion("Teemo", ["ap"], True, False, False, True, True),
    Champion("Thresh", ["ap"], False, False, False, False, True),
    Champion("Tristana", ["ad"], False, False, False, True, False),
    Champion("Trundle", ["ad"], True, True, False, False, False),
    Champion("Tryndamere", ["ad"], True, False, False, False, False),
    Champion("Twisted Fate", ["ad", "ap"], False, False, True, True, False),
    Champion("Renekton", ["ad"], True, False, True, False, False),
    Champion("Rengar", ["ad"], False, True, False, False, False),
    Champion("Riven", ["ad"], True, False, False, False, False),
    Champion("Rumble", ["ap"], True, False, True, False, False),
    Champion("Ryze", ["ap"], False, False, True, True, False),
    Champion("Sejuani", ["ap"], True, True, False, False, False),
    Champion("Shaco", ["ad", "ap"], False, True, False, False, False),
    Champion("Shen", ["ad"], True, False, False, False, True),
    Champion("Shyvana", ["ad", "ap"], False, True, False, False, False),
    Champion("Singed", ["ap"], True, False, False, False, False),
    Champion("Sion", ["ad"], True, False, False, False, False),
    Champion("Sivir", ["ad"], False, False, True, True, False),
    Champion("Skarner", ["ad", "ap"], False, True, False, False, False),
    Champion("Sona", ["ap"], False, False, True, True, True),
    Champion("Soraka", ["ap"], False, False, False, False, True),
    Champion("Mordekaiser", ["ap"], True, False, False, False, False),
    Champion("Morgana", ["ap"], False, False, True, False, True),
    Champion("Nami", ["ap"], False, False, False, False, True),
    Champion("Nasus", ["ad", "ap"], True, False, False, False, False),
    Champion("Nautilus", ["ap"], False, False, False, False, True),
    Champion("Nidalee", ["ap"], False, True, True, True, True),
    Champion("Nocturne", ["ad"], True, True, True, False, False),
    Champion("Nunu", ["ap"], True, True, True, False, False),
    Champion("Olaf", ["ad"], True, True, False, False, False),
    Champion("Orianna", ["ap"], False, False, True, True, True),
    Champion("Pantheon", ["ad"], True, True, True, False, True),
    Champion("Poppy",["ad"], True, True, False, False, True),
    Champion("Quinn", ["ad"], True, False, False, True, False),
    Champion("Rammus", ["ap"], False, True, False, False, False),
    Champion("Rek'Sai", ["ad"], False, True, False, False, False),
    Champion("Leona", ["ad", "ap"], False, False, False, False, True),
    Champion("Lissandra", ["ap"], False, False, True, True, False),
    Champion("Lucian", ["ad"], False, False, True, True, False),
    Champion("Lulu", ["ad", "ap"], False, False, True, True, True),
    Champion("Lux", ["ap"], False, False, True, True, True),
    Champion("Malphite", ["ap"], True, False, False, False, False),
    Champion("Malzahar", ["ap"], False, False, True, False, False),
    Champion("Maokai", ["ap"], True, False, False, False, True),
    Champion("Master Yi", ["ad"], False, True, False, False, False),
    Champion("Miss Fortune", ["ad"], False, False, False, True, False),
    Champion("Karma", ["ap"], False, False, True, False, True),
    Champion("Karthus", ["ap"], False, True, True, True, False),
    Champion("Kassadin", ["ap"], False, False, True, False, False),
    Champion("Katarina", ["ad", "ap"], False, False, True, False, False),
    Champion("Kayle", ["ad", "ap"], True, False, True, False, True),
    Champion("Kennen", ["ap"], True, False, True, True, False),
    Champion("Kha'Zix", ["ad"], False, True, False, False, False),
    Champion("Kog'Maw", ["ad", "ap"], False, False, True, True, False),
    Champion("LeBlanc", ["ap"], False, False, True, False, False),
    Champion("Lee Sin", ["ad"], False, True, False, False, True),
    Champion("Evelynn", ["ap"], False, True, False, False, False),
    Champion("Ezreal", ["ad", "ap"], False, False, True, True, False),
    Champion("Fiddlesticks", ["ap"], False, True, False, False, False),
    Champion("Fiora", ["ad"], True, False, False, False, False),
    Champion("Fizz", ["ap"], False, False, True, False, False),
    Champion("Galio", ["ap"], True, False, True, False, True),
    Champion("Gangplank", ["ad"], True, False, False, False, False),
    Champion("Garen", ["ad"], True, False, False, False, False),
    Champion("Gnar", ["ad"], True, False, False, True, False),
    Champion("Gragas", ["ap"], False, True, False, False, False),
    Champion("Graves", ["ad"], False, True, False, False, False),
    Champion("Hecarim", ["ad"], False, True, False, False, False),
    Champion("Heimerdinger", ["ap"], False, False, True, True, False),
    Champion("Irelia", ["ad"], True, False, True, False, False),
    Champion("Janna", ["ap"], False, False, False, False, True),
    Champion("Jarvan IV", ["ad"], False, True, False, False, False),
    Champion("Jax", ["ad"], True, False, False, False, False),
    Champion("Jayce", ["ad"], True, False, True, True, False),
    Champion("Jinx", ["ad"], False, False, False, True, False),
    Champion("Kalista", ["ad"], False, False, False, True, False),
    Champion("Aatrox", ["ad"], True, False, False, False, False),
    Champion("Ahri", ["ap"], False, False, True, False, True),
    Champion("Akali", ["ap"], True, False, True, False, False),
    Champion("Alistar", ["ap"], False, False, False, False, True),
    Champion("Amumu", ["ap"], True, True, False, False, True),
    Champion("Anivia", ["ap"], False, False, True, True, True),
    Champion("Annie", ["ap"], False, False, True, False, True),
    Champion("Ashe", ["ad"], False, False, False, True, True),
    Champion("Azir", ["ap"], False, False, True, False, False),
    Champion("Blitzcrank", ["ap"], False, False, False, False, True),
    Champion("Brand", ["ap"], False, False, True, False, True),
    Champion("Braum", ["ap"], False, False, False, False, True),
    Champion("Caitlyn", ["ad"], False, False, False, True, False),
    Champion("Cassiopeia", ["ap"], False, False, True, True, False),
    Champion("Cho'Gath", ["ap"], True, False, False, False, False),
    Champion("Corki", ["ad", "ap"], False, False, True, True, False),
    Champion("Darius", ["ad"], True, False, False, False, False),
    Champion("Diana", ["ap"], False, True, True, False, False),
    Champion("Dr. Mundo", ["ap"], True, False, False, False, False),
    Champion("Draven", ["ad"], False, False, False, True, False),
    Champion("Elise", ["ap"], False, True, False, False, False),
    Champion("Renata Glasc",["ap"],False,False,False,False,True),
    Champion("Bel Veth",["ad"],False,True,False,False,False),
    Champion("Nillah",["ad"],False,True,False,True,False),
    
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

    damage_type_choice=''

    while damage_type_choice not in selection2:
        damage_type_choice = input('''Ap or Ad??
[1] Ap
[2] Ad
[3] Any

Your choice: ''')
        if damage_type_choice not in selection2:
            error()



    possible_choices = []

    if role == "1" and damage_type_choice == "3":
        for i in list_of_champions:
            if i.top == True:
                possible_choices.append(i.name)
    elif role == "1" and damage_type_choice == "1":
        for i in list_of_champions:
            if i.top == True and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "1" and damage_type_choice == "2":
        for i in list_of_champions:
            if i.top == True and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "2" and damage_type_choice == "3":
        for i in list_of_champions:
            if i.jg == True:
                possible_choices.append(i.name)
    elif role == "2" and damage_type_choice == "1":
        for i in list_of_champions:
            if i.jg == True and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "2" and damage_type_choice == "2":
        for i in list_of_champions:
            if i.jg == True and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "3" and damage_type_choice == "3":
        for i in list_of_champions:
            if i.mid == True:
                possible_choices.append(i.name)
    elif role == "3" and damage_type_choice == "1":
        for i in list_of_champions:
            if i.mid == True and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "3" and damage_type_choice == "2":
        for i in list_of_champions:
            if i.mid == True and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "4" and damage_type_choice == "3":
        for i in list_of_champions:
            if i.bot == True:
                possible_choices.append(i.name)
    elif role == "4" and damage_type_choice == "1":
        for i in list_of_champions:
            if i.bot == True and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "4" and damage_type_choice == "2":
        for i in list_of_champions:
            if i.bot == True and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "5" and damage_type_choice == "3":
        for i in list_of_champions:
            if i.sup == True:
                possible_choices.append(i.name)
    elif role == "5" and damage_type_choice == "1":
        for i in list_of_champions:
            if i.sup == True and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "5" and damage_type_choice == "2":
        for i in list_of_champions:
            if i.sup == True and "ad" in i.damage_type:
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