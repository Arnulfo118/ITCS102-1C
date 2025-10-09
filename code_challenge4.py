print("===================================")
print("   Welcome to the Manga Recommender")
print("===================================")
print("Let's find something good to read.\n")

genre = input("Select genre:\n\t1. Action\n\t2. Romance\n\t3. Horror\n> ")

if genre == "1":
    print("\nGenre: Action")
    length = input("Select length:\n\t1. Short\n\t2. Medium\n\t3. Long\n> ")

    if length == "1":
        print("\nLength: Short")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. Fullmetal Alchemist – Two brothers seek the Philosopher’s Stone after a failed ritual.")
            print("2. Naruto – A ninja dreams of becoming Hokage.")
        else:
            print("\nRecommended:")
            print("1. Attack on Titan – Humanity fights Titans for survival.")
            print("2. My Hero Academia – A boy without powers trains to become a hero.")

    elif length == "2":
        print("\nLength: Medium")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. Bleach – A teen becomes a Soul Reaper to battle evil spirits.")
            print("2. D.Gray-man – Exorcists fight demons known as Akuma.")
        else:
            print("\nRecommended:")
            print("1. One Punch Man – A hero seeks meaning in effortless victories.")
            print("2. Tokyo Ghoul – A student becomes half-ghoul, half-human.")

    else:
        print("\nLength: Long")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. One Piece – Pirates seek the legendary treasure, One Piece.")
            print("2. Gintama – Odd-job samurai in alien-occupied Edo.")
        else:
            print("\nRecommended:")
            print("1. Fairy Tail – Wizards take on magical adventures.")
            print("2. Hunter x Hunter (2011) – A boy becomes a Hunter to find his father.")

elif genre == "2":
    print("\nGenre: Romance")
    length = input("Select length:\n\t1. Short\n\t2. Medium\n\t3. Long\n> ")

    if length == "1":
        print("\nLength: Short")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. Lovely★Complex – A tall girl and short boy navigate teenage love.")
            print("2. Paradise Kiss – A student finds love through fashion.")
        else:
            print("\nRecommended:")
            print("1. Ao Haru Ride – A girl reconnects with her first love.")
            print("2. Orange – Letters from the future guide a girl to save her friend.")

    elif length == "2":
        print("\nLength: Medium")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. Kimi ni Todoke – A shy girl finds friendship and love.")
            print("2. Boys Be – Short stories about high school romance.")
        else:
            print("\nRecommended:")
            print("1. Maid Sama – A strict president secretly works at a maid café.")
            print("2. Say I Love You – A loner opens up after meeting a popular boy.")

    else:
        print("\nLength: Long")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. Boys Over Flowers – A poor girl clashes with a rich boy.")
            print("2. Nana – Two women named Nana share a life-changing friendship.")
        else:
            print("\nRecommended:")
            print("1. Your Lie in April – A pianist finds inspiration through a violinist.")
            print("2. Clannad – A boy’s life changes through friendship and love.")

elif genre == "3":
    print("\nGenre: Horror")
    length = input("Select length:\n\t1. Short\n\t2. Medium\n\t3. Long\n> ")

    if length == "1":
        print("\nLength: Short")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. Uzumaki – A town cursed by spirals descends into madness.")
            print("2. Tomie – A beautiful immortal girl brings ruin to all who meet her.")
        else:
            print("\nRecommended:")
            print("1. I Am a Hero – A struggling manga artist faces a zombie outbreak.")
            print("2. Ajin – Immortal beings are hunted by humans.")

    elif length == "2":
        print("\nLength: Medium")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. Parasyte – A boy fights alien parasites taking over humans.")
            print("2. Goth – Students drawn to dark mysteries uncover horror.")
        else:
            print("\nRecommended:")
            print("1. Another – A cursed class faces mysterious deaths.")
            print("2. Corpse Party – Students trapped in a haunted school.")

    else:
        print("\nLength: Long")
        period = input("Select release era:\n\t1. 2000s\n\t2. 2010s\n> ")

        if period == "1":
            print("\nRecommended:")
            print("1. Hellsing – A vampire protects England from supernatural threats.")
            print("2. Bastard!! – A dark wizard unleashes chaos in a fantasy world.")
        else:
            print("\nRecommended:")
            print("1. Tokyo Ghoul – A student becomes half-ghoul and fights for identity.")
            print("2. The Promised Neverland – Children uncover their orphanage’s dark secret.")

else:
    print("\nInvalid choice. Restart to try again.")
