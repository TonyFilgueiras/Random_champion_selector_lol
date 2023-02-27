from random import randint

class Champion:
    def __init__(self, name, damage_type:list, lane:list):
        self.name = name
        self.damage_type = damage_type
        self.lane = lane

def error():
    print("Insert a valid input!!")

list_of_champions = [
    Champion("Zeri", ["ad", "ap"], ["mid", "bot"]),
    Champion("Vex", ["ap"], ["mid", "bot", "sup"]),
    Champion("Akshan", ["ad"], ["mid", "bot"]),
    Champion("Samira", ["ad"], ["mid", "bot"]),
    Champion("Seraphine", ["ap"], ["mid", "bot", "sup"]),
    Champion("Rell", ["ap"], ["sup"]),
    Champion("Viego", ["ad"], ["jg"]),
    Champion("Gwen", ["ap"], ["top"]),
    Champion("Pyke", ["ad"], ["mid", "sup"]),
    Champion("Neeko", ["ap"], ["mid", "bot", "sup"]),
    Champion("Sylas", ["ap"], ["top", "jg", "mid"]),
    Champion("Yuumi", ["ap"], ["sup"]),
    Champion("Qiyana", ["ad"], ["mid"]),
    Champion("Senna", ["ad"], ["bot", "sup"]),
    Champion("Aphelios", ["ad"], ["bot"]),
    Champion("Sett", ["ad"], ["top", "sup"]),
    Champion("Lillia", ["ap"], ["top", "jg", "mid"]),
    Champion("Yone", ["ad"], ["top", "jg", "mid"]),
    Champion("Taliyah", ["ap"], ["jg", "mid", "bot", "sup"]),
    Champion("Kled", ["ad"], ["top"]),
    Champion("Ivern", ["ap"], ["jg", "sup"]),
    Champion("Camille", ["ad"], ["top", "jg"]),
    Champion("Rakan", ["ap"], ["sup"]),
    Champion("Xayah", ["ad"], ["bot"]),
    Champion("Kayn", ["ad"], ["jg"]),
    Champion("Ornn", ["ad"], ["top"]),
    Champion("Zoe", ["ap"], ["mid", "bot", "sup"]),
    Champion("Kai'sa", ["ad", "ap"], ["bot", "mid"]),
    Champion("Yasuo", ["ad"], ["bot", "mid"]),
    Champion("Yorick", ["ad"], ["top"]),
    Champion("Zac", ["ap"], ["jg"]),
    Champion("Zed", ["ad"], ["mid"]),
    Champion("Ziggs", ["ap"], ["bot", "mid"]),
    Champion("Zilean", ["ap"], ["mid", "sup"]),
    Champion("Zyra", ["ap"], ["mid", "sup"]),
    Champion("Bard", ["ap"], ["sup"]),
    Champion("Ekko", ["ap"], ["jg", "mid"]),
    Champion("Tahm kench", ["ap"], ["top", "sup"]),
    Champion("Kindred", ["ad"], ["jg", "mid", "bot"]),
    Champion("Illaoi", ["ad"], ["top"]),
    Champion("Jhin", ["ad"], ["bot"]),
    Champion("Aurelion Sol", ["ap"], ["mid", "bot", "sup"]),
    Champion("Twitch", ["ad", "ap"], ["bot"]),
    Champion("Udyr", ["ad", "ap"], ["jg"]),
    Champion("Urgot", ["ad"], ["top"]),
    Champion("Varus", ["ad", "ap"], ["bot", "mid"]),
    Champion("Vayne", ["ad"], ["top", "bot"]),
    Champion("Veigar", ["ap"], ["top", "mid", "bot"]),
    Champion("Vel'Koz", ["ap"], ["mid", "sup"]),
    Champion("Vi", ["ad"], ["top", "jg"]),
    Champion("Viktor", ["ap"], ["mid"]),
    Champion("Vladimir", ["ap"], ["top", "mid"]),
    Champion("Volibear", ["ad", "ap"], ["top", "jg"]),
    Champion("Warwick", ["ad"], ["top", "jg"]),
    Champion("Wukong", ["ad"], ["top", "jg", "mid"]),
    Champion("Xerath", ["ap"], ["mid", "sup"]),
    Champion("Xin Zhao", ["ad"], ["top", "jg", "mid"]),
    Champion("Swain", ["ap"], ["top", "mid", "bot", "sup"]),
    Champion("Syndra", ["ap"], ["bot", "mid"]),
    Champion("Talon", ["ad"], ["mid"]),
    Champion("Taric", ["ap"], ["top", "sup", "sup"]),
    Champion("Teemo", ["ap"], ["top", "bot", "sup"]),
    Champion("Thresh", ["ap"], ["sup"]),
    Champion("Tristana", ["ad"], ["bot"]),
    Champion("Trundle", ["ad"], ["top", "jg"]),
    Champion("Tryndamere", ["ad"], ["top"]),
    Champion("Twisted Fate", ["ad", "ap"], ["bot", "mid"]),
    Champion("Renekton", ["ad"], ["top", "mid"]),
    Champion("Rengar", ["ad"], ["jg"]),
    Champion("Riven", ["ad"], ["top"]),
    Champion("Rumble", ["ap"], ["top", "mid"]),
    Champion("Ryze", ["ap"], ["bot", "mid"]),
    Champion("Sejuani", ["ap"], ["top", "jg"]),
    Champion("Shaco", ["ad", "ap"], ["jg"]),
    Champion("Shen", ["ad"], ["top", "sup"]),
    Champion("Shyvana", ["ad", "ap"], ["jg"]),
    Champion("Singed", ["ap"], ["top"]),
    Champion("Sion", ["ad"], ["top"]),
    Champion("Sivir", ["ad"], ["bot", "mid"]),
    Champion("Skarner", ["ad", "ap"], ["jg"]),
    Champion("Sona", ["ap"], ["mid", "bot", "sup"]),
    Champion("Soraka", ["ap"], ["sup"]),
    Champion("Mordekaiser", ["ap"], ["top"]),
    Champion("Morgana", ["ap"], ["mid", "sup"]),
    Champion("Nami", ["ap"], ["sup"]),
    Champion("Nasus", ["ad", "ap"], ["top"]),
    Champion("Nautilus", ["ap"], ["sup"]),
    Champion("Nidalee", ["ap"], ["jg", "mid", "bot", "sup"]),
    Champion("Nocturne", ["ad"], ["top", "jg", "mid"]),
    Champion("Nunu", ["ap"], ["top", "jg", "mid"]),
    Champion("Olaf", ["ad"], ["top", "jg"]),
    Champion("Orianna", ["ap"], ["mid", "bot", "sup"]),
    Champion("Pantheon", ["ad"], ["top", "jg", "mid", "sup"]),
    Champion("Poppy",["ad"], ["top", "jg", "sup"]),
    Champion("Quinn", ["ad"], ["top", "bot"]),
    Champion("Rammus", ["ap"], ["jg"]),
    Champion("Rek'Sai", ["ad"], ["jg"]),
    Champion("Leona", ["ad", "ap"], ["sup"]),
    Champion("Lissandra", ["ap"], ["bot", "mid"]),
    Champion("Lucian", ["ad"], ["bot", "mid"]),
    Champion("Lulu", ["ad", "ap"], ["mid", "bot", "sup"]),
    Champion("Lux", ["ap"], ["mid", "bot", "sup"]),
    Champion("Malphite", ["ap"], ["top"]),
    Champion("Malzahar", ["ap"], ["mid"]),
    Champion("Maokai", ["ap"], ["top", "sup"]),
    Champion("Master Yi", ["ad"], ["jg"]),
    Champion("Miss Fortune", ["ad"], ["bot"]),
    Champion("Karma", ["ap"], ["mid", "sup"]),
    Champion("Karthus", ["ap"], ["jg", "mid", "bot"]),
    Champion("Kassadin", ["ap"], ["mid"]),
    Champion("Katarina", ["ad", "ap"], ["mid"]),
    Champion("Kayle", ["ad", "ap"], ["top", "mid", "sup"]),
    Champion("Kennen", ["ap"], ["top", "mid", "bot"]),
    Champion("Kha'Zix", ["ad"], ["jg"]),
    Champion("Kog'Maw", ["ad", "ap"], ["bot", "mid"]),
    Champion("LeBlanc", ["ap"], ["mid"]),
    Champion("Lee Sin", ["ad"], ["jg", "sup"]),
    Champion("Evelynn", ["ap"], ["jg"]),
    Champion("Ezreal", ["ad", "ap"], ["bot", "mid"]),
    Champion("Fiddlesticks", ["ap"], ["jg"]),
    Champion("Fiora", ["ad"], ["top"]),
    Champion("Fizz", ["ap"], ["mid"]),
    Champion("Galio", ["ap"], ["top", "mid", "sup"]),
    Champion("Gangplank", ["ad"], ["top"]),
    Champion("Garen", ["ad"], ["top"]),
    Champion("Gnar", ["ad"], ["top", "bot"]),
    Champion("Gragas", ["ap"], ["jg"]),
    Champion("Graves", ["ad"], ["jg"]),
    Champion("Hecarim", ["ad"], ["jg"]),
    Champion("Heimerdinger", ["ap"], ["bot", "mid"]),
    Champion("Irelia", ["ad"], ["top", "mid"]),
    Champion("Janna", ["ap"], ["sup"]),
    Champion("Jarvan IV", ["ad"], ["jg"]),
    Champion("Jax", ["ad"], ["top"]),
    Champion("Jayce", ["ad"], ["top", "mid", "bot"]),
    Champion("Jinx", ["ad"], ["bot"]),
    Champion("Kalista", ["ad"], ["bot"]),
    Champion("Aatrox", ["ad"], ["top"]),
    Champion("Ahri", ["ap"], ["mid", "sup"]),
    Champion("Akali", ["ap"], ["top", "mid"]),
    Champion("Alistar", ["ap"], ["sup"]),
    Champion("Amumu", ["ap"], ["top", "jg", "sup"]),
    Champion("Anivia", ["ap"], ["mid", "bot", "sup"]),
    Champion("Annie", ["ap"], ["mid", "sup"]),
    Champion("Ashe", ["ad"], ["bot", "sup"]),
    Champion("Azir", ["ap"], ["mid"]),
    Champion("Blitzcrank", ["ap"], ["sup"]),
    Champion("Brand", ["ap"], ["mid", "sup"]),
    Champion("Braum", ["ap"], ["sup"]),
    Champion("Caitlyn", ["ad"], ["bot"]),
    Champion("Cassiopeia", ["ap"], ["mid", "bot"]),
    Champion("Cho'Gath", ["ap"], ["top"]),
    Champion("Corki", ["ad", "ap"], ["mid", "bot"]),
    Champion("Darius", ["ad"], ["top"]),
    Champion("Diana", ["ap"], ["jg", "mid"]),
    Champion("Dr. Mundo", ["ap"], ["top"]),
    Champion("Draven", ["ad"], ["bot"]),
    Champion("Elise", ["ap"], ["jg"]),
    Champion("Renata Glasc",["ap"], ["sup"]),
    Champion("Bel Veth",["ad"], ["jg"]),
    Champion("Nillah",["ad"], ["jg", "bot"]),
    Champion("K'Sante",["ad"], ["top"]),
    
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
            if "top" in i.lane:
                possible_choices.append(i.name)
    elif role == "1" and damage_type_choice == "1":
        for i in list_of_champions:
            if "top" in i.lane and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "1" and damage_type_choice == "2":
        for i in list_of_champions:
            if "top" in i.lane and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "2" and damage_type_choice == "3":
        for i in list_of_champions:
            if "jg" in i.lane:
                possible_choices.append(i.name)
    elif role == "2" and damage_type_choice == "1":
        for i in list_of_champions:
            if "jg" in i.lane and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "2" and damage_type_choice == "2":
        for i in list_of_champions:
            if "jg" in i.lane and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "3" and damage_type_choice == "3":
        for i in list_of_champions:
            if "mid" in i.lane:
                possible_choices.append(i.name)
    elif role == "3" and damage_type_choice == "1":
        for i in list_of_champions:
            if "mid" in i.lane and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "3" and damage_type_choice == "2":
        for i in list_of_champions:
            if "mid" in i.lane and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "4" and damage_type_choice == "3":
        for i in list_of_champions:
            if "bot" in i.lane:
                possible_choices.append(i.name)
    elif role == "4" and damage_type_choice == "1":
        for i in list_of_champions:
            if "bot" in i.lane and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "4" and damage_type_choice == "2":
        for i in list_of_champions:
            if "bot" in i.lane and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "5" and damage_type_choice == "3":
        for i in list_of_champions:
            if "sup" in i.lane:
                possible_choices.append(i.name)
    elif role == "5" and damage_type_choice == "1":
        for i in list_of_champions:
            if "sup" in i.lane and "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "5" and damage_type_choice == "2":
        for i in list_of_champions:
            if "sup" in i.lane and "ad" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "6" and damage_type_choice == "1":
        for i in list_of_champions:
            if "ap" in i.damage_type:
                possible_choices.append(i.name)
    elif role == "6" and damage_type_choice == "2":
        for i in list_of_champions:
            if "ad" in i.damage_type:
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