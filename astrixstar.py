def game():
    choice = input("Which one would you like: up, down, wave ")
    if choice == "up":
        def astrixtstar():
            amount = input("How many rows? ")
            last = float(amount)
            a = 0
            c = ""
            while a <= last:
                b = "*"
                n = b
                c = c + n
                print(c)
                a = a + 1
        astrixtstar()

    elif choice == "down":
        def downstar():
            amount = int(input("How many rows? "))
            a = amount
            c = "*"
            for number in range(amount):
                print(a * c)
                a = a - 2
        downstar()

    elif choice == "wave":
        def arrows():
            width = int(input("How many arrows? "))
            count = int(input("What is the width? "))
            a = 0
            for number in range(width):
                while a < width:
                    print(a * "*")
                    a += 1
                while a > 1:
                    print(a * "*")
                    a -= 1
        arrows()
    else:
        print("Choice not found")
game()
