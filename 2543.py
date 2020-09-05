while True:
    try:
        gameplays, universityId = input().split()
        gameplays = int(gameplays)
        universityId = int(universityId)

        quantityOfGameplays = 0
        for i in range(gameplays):
            universityAuthorId, game = input().split()
            universityAuthorId = int(universityAuthorId)
            game = int(game)
            if universityAuthorId == universityId and game == 0:
                quantityOfGameplays += 1

        print(quantityOfGameplays)

    except EOFError:
        break
