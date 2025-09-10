print("Welcome to the Manga/Manhwa/Manhua Reader Recommendator!")
genre = input("What genre would you like to read? (action/ horror/ romance): ")

if genre == "action":
    print("You've selected action.")
    length = input("How long do you want to read the manga/manhwa/manhua? (short, medium, long): ")
    if length == "short":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of action manga/manhwa/manhua before the 2000s")
            print("Domu\nGrey\nHotel Harbour View\nAppleseed: The Promethean Challenge\nCyber Blue")
        else:
            print("Here's the list of action manga/manhwa/manhua after the 2000s")
            print("All You Need Is Kill\nAttack On Titan\nJormungand\nDogs: Bullets and Carnage\nBullet Armors")
                
    elif length == "medium":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of action manga/manhwa/manhua before the 2000s")
            print("Battle Angel Alita\nSpriggan\nBlack Lion\nBlasterKnuckle\nMadBull")
        else:
            print("Here's the list of action manga/manhwa/manhua after the 2000s")
            print("Sun-ken Rock\nDoubt\nAfter School\nCharisma\nArea D\nBlack Lagoon")
                
    elif length == "long":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of action manga/manhwa/manhua before the 2000s")
            print("Rurouni Kenshin\nFist of the Northern Star\nJojo's Bizarre Adventure\nBastard!!\nGuyver: The Bioboosted Armor")
        else:
            print("Here's the list of action manga/manhwa/manhua after the 2000s")
            print("Jojo's Bizarre Adventure: Unbreakable Diamond, Attack on Titan, Strike The Blood")              
    else:
        print("That is not a valid length.")     
elif genre == "romance":
    print("You've selected romance.")
    length = input("How long do you want to read the manga/manhwa/manhua? (short, medium, long): ")
    if length == "short":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of romance manga/manhwa/manhua before the 2000s")
            print("Please Save My Earth\nBoys Over Flowers\nKimi wa Petto\nZettai Kareshi\nItazura na Kiss")
        else:
            print("Here's the list of romance manga/manhwa/manhua after the 2000s")
            print("Kimi ni Todoke\nAo Haru Ride\nMy Little Monster\nSay I Love You\nFruits Basket")

    elif length == "medium":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of romance manga/manhwa/manhua before the 2000s")
            print("Mars\nParadise Kiss\nBoys Over Flowers\nKimi wa Petto\nZettai Kareshi")
        else:
            print("Here's the list of romance manga/manhwa/manhua after the 2000s")
            print("Kimi ni Todoke\nAo Haru Ride\nMy Little Monster\nSay I Love You\nFruits Basket")

    elif length == "long":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of romance manga/manhwa/manhua before the 2000s")
            print("Boys Over Flowers\nKimi wa Petto\nZettai Kareshi\nItazura na Kiss")
        else:
            print("Here's the list of romance manga/manhwa/manhua after the 2000s")
            print("Kaichou wa Maid-sama!\nKimi ni Todoke\nAo Haru Ride\nMy Little Monster\nSay I Love You")
    else:
        print("That is not a valid length.")     
elif genre == "horror":
    print("You've selected horror.")
    length = input("How long do you want to read the manga/manhwa/manhua? (short, medium, long): ")
    if length == "short":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of horror manga/manhwa/manhua before the 2000s")
            print("Uzumaki\nTomie\nGyo\nThe Drifting Classroom\nParasyte")
        else:
            print("Here's the list of horror manga/manhwa/manhua after the 2000s")
            print("Tokyo Ghoul\nI Am a Hero\nThe Promised Neverland\nAnother\nParanoia Agent")
                
    elif length == "medium":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of horror manga/manhwa/manhua before the 2000s")
            print("Uzumaki\nTomie\nGyo\nThe Drifting Classroom\nParasyte")
        else:
            print("Here's the list of horror manga/manhwa/manhua after the 2000s")
            print("Another\nThe Promised Neverland\nI Am a Hero\nTokyo Ghoul\nParanoia Agent")

    elif length == "long":
        decade = eval(input("Which decade?: "))
        if decade < 2000:
            print("Here's the list of horror manga/manhwa/manhua before the 2000s")
            print("Uzumaki\nTomie\nGyo\nThe Drifting Classroom\nParasyte")
        else:
            print("Here's the list of horror manga/manhwa/manhua after the 2000s")
            print("Junji Ito's Cat Diary\nThe Promised Neverland\nI Am a Hero\nTokyo Ghoul\nParanoia Agent")
    else:
        print("That is not a valid length.")   
else: 
    print("Invalid genre.")