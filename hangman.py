def hangman():
    import random
    print("Welcome to Hangman!")
    print("Note there are spaces in the word, you must press the space button for a space!")
    level = input("Please select your difficulty: EASY, MEDIUM, HARD ")
    topic = input("Please select a topic: Disney and Pixar Princesses, Young Adult Fiction Books, Disney and Pixar Characters ")
    first = """
        __________
       |          |
       O          |
                  |
                  |
                  |
                  |
                  |
            ______|______
    """
    second = """
        __________
       |          |
       O          |
       |          |
       |          |
                  |
                  |
                  |
            ______|______
    """
    third = """
        __________
       |          |
       O          |
      _|          |
       |          |
                  |
                  |
                  |
            ______|______
    """
    fourth = """
        __________
       |          |
       O          |
      _|_         |
       |          |
                  |
                  |
                  |
            ______|______
    """
    fifth = """
        __________
       |          |
       O          |
      _|_         |
       |          |
        \         |
                  |
                  |
            ______|______
    """
    sixth = """
        __________
       |          |
       O          |
      _|_         |
       |          |
      / \         |
                  |
                  |
            ______|______
    """
    seventh = """
        __________
       |          |
      /O          |
      _|_         |
       |          |
      / \         |
                  |
                  |
            ______|______
    """
    eigth = """
        __________
       |          |
      /O\         |
      _|_         |
       |          |
      / \         |
                  |
                  |
            ______|______
    """

    if level == "EASY":
        if topic == "Disney and Pixar Princesses":
            list = ["cinderella", "Auora", "jasmine", "ariel", "mulan", "belle"]
        elif topic == "Young Adult Fiction Books":
            list = ["divergent", "hunger games", "city of bones", "percy jackson and the olympians", "kane chronicles", "maze runner"]
        elif topic == "Disney and Pixar Characters":
            list = ["mickey", "goofy", "pooh", "olaf", "aliens", "woody"]
        else:
            print("Topic not found")

        choice = random.randint(0,len(list)-1)
        word = list[choice]
        blanks = len(word)
        print("_ " * blanks)
        index = 0
        life = 8
        win = 0
        while index < blanks:
            guess = input(" ")
            if guess in word:
                place = 0
                for number in range(0,len(word)):
                    if guess == word[place]:
                        place = place + 1
                        win = win + 1
                        print("Your letter is number %i in the word" %place)
                    else:
                        place = place + 1
            else:
                life -= 1
                if life == 7:
                    print(first)
                elif life == 6:
                    print(second)
                elif life == 5:
                    print(third)
                elif life == 4:
                    print(fourth)
                elif life == 3:
                    print(fifth)
                elif life == 2:
                    print(sixth)
                elif life == 1:
                    print(seventh)
                else:
                    print(eigth)
            if life == 0:
                print("GAME OVER")
                print("The word was: %s" %word)
                break
            if win == len(word):
                print("Good job! You win! :)")
                print("The word was: %s" %word)
                break

    elif level == "MEDIUM":
        if topic == "Disney and Pixar Princesses":
            list = ["rapunzel", "elsa", "anna", "moana", "pocahontas", "tiana"]
        elif topic == "Young Adult Fiction Books":
            list =["the fault in our stars", "catching fire", "uglies", "matched", "insurgent", "thirteen reasons why"]
        elif topic == "Disney and Pixar Characters":
            list == ["lightning mcqueen", "dumbo", "bambi", "nemo", "eva", "aladdin"]
        else:
            print("Topic not found")
        choice = random.randint(0,len(list)-1)
        word = list[choice]
        blanks = len(word)
        print("_ " * blanks)
        index = 0
        life = 8
        win = 0
        while index < blanks:
            guess = input(" ")
            if guess in word:
                place = 0
                for number in range(0,len(word)):
                    if guess == word[place]:
                        place = place + 1
                        win = win + 1
                        print("Your letter is number %i in the word" %place)
                    else:
                        place = place + 1
            else:
                life -= 1
                if life == 7:
                    print(first)
                elif life == 6:
                    print(second)
                elif life == 5:
                    print(third)
                elif life == 4:
                    print(fourth)
                elif life == 3:
                    print(fifth)
                elif life == 2:
                    print(sixth)
                elif life == 1:
                    print(seventh)
                else:
                    print(eigth)
            if life == 0:
                print("GAME OVER")
                print("The word was: %s" %word)
                break
            if win == len(word):
                print("Good job! You win! :)")
                print("The word was: %s" %word)
                break

    elif level == "HARD":
        if topic == "Disney and Pixar Princesses":
            list = ["megara", "shuri", "gamora", "merida", "giselle", "tinker bell"]
        elif topic == "Young Adult Fiction Books":
            list = ["holes", "lord of the flies", "the outsiders", "bridge to terabithia", "a wrinkle in time", "lord of the rings"]
        elif topic == "Disney and Pixar Characters":
            list = ["sally", "baymax", "pinocchio", "pluto", "nala", "joy"]
        else:
            print("Topic not found")
        choice = random.randint(0,len(list)-1)
        word = list[choice]
        blanks = len(word)
        print("_ " * blanks)
        index = 0
        life = 8
        win = 0
        while index < blanks:
            guess = input(" ")
            if guess in word:
                place = 0
                for number in range(0,len(word)):
                    if guess == word[place]:
                        place = place + 1
                        win = win + 1
                        print("Your letter is number %i in the word" %place)
                    else:
                        place = place + 1
            else:
                life -= 1
                if life == 7:
                    print(first)
                elif life == 6:
                    print(second)
                elif life == 5:
                    print(third)
                elif life == 4:
                    print(fourth)
                elif life == 3:
                    print(fifth)
                elif life == 2:
                    print(sixth)
                elif life == 1:
                    print(seventh)
                else:
                    print(eigth)
            if life == 0:
                print("GAME OVER")
                print("The word was: %s" %word)
                break
            if win == len(word):
                print("Good job! You win! :)")
                print("The word was: %s" %word)
                break
hangman()
