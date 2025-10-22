isExit = False
favorite_anime = []

while not isExit:
    animeList = input("Enter your favorite anime (or type 'exit' to quit or 'list' to see all entries): ")
    if animeList.lower() == 'exit':
        isExit = True
    elif animeList.lower() == 'list':
        print("Your favorite anime list:")
        for anime in favorite_anime:
            print(f"- {anime}")
    else:
        favorite_anime.append(animeList) 
