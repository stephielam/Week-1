import math
def calculator():
    print("Welcome to Simple Calculator! It can do the four basic functions: addition, subtraction, multiplication, and division, find the power and remainder of a certain number, find the minimum and maximum of a range of numbers you put in, and convert binary to decimal, octal, and hexadecimal!")
    print("Would you like use addition, subtraction, multiplication, division, exponent, modules, find the minimum or maximum of a range of numbers?")
    type = input("Please type add for addition, subtract for subtraction, multiply for multiplication, divide for division, exponent for exponent, remainder for modules, min to find the minimum, max to find the maximum of a range of numbers, btod for binary to decimal, btoo for binary to octal, btoh for binary to hexadecimal: ")
    if (type == "add"):
        def addition():
            x = input ("Please put your first number: ")
            y = input ("Please put your second number: ")
            x = float(x)
            y = float(y)
            Sum = x + y
            print("The sum is: %.3f" %Sum)
        addition()

    elif (type == "subtract"):
        def subtraction():
            x = input ("Please put your first number: ")
            y = input ("Please put your second number: ")
            x = float(x)
            y = float(y)
            Difference = x - y
            print("The difference is %.3f" %Difference)
        subtraction()

    elif (type == "multiply"):
        def multiplication():
            x = input ("Please put your first number: ")
            y = input ("Please put your second number: ")
            x = float(x)
            y = float(y)
            product = 0
            z = 1
            n = x
            while y >= z:
                product += n
                z = z + 1
            print("The product is %.3f" %product)
        multiplication()

    elif (type == "divide"):
        def division():
            x = input ("Please put your first number: ")
            y = input ("Please put your second number: ")
            x = float(x)
            y = float(y)
            quotient = 0
            z = 0
            n = x
            while n > 0:
                n -= y
                z = z + 1
                quotient = z
            print("The quotient is %.3f" %quotient)
        division()

    elif (type == "exponent"):
        def exponent():
            x = input ("Please put your first number: ")
            y = input ("Please put your second number: ")
            x = float(x)
            y = float(y)
            power = 1
            z = 1
            n = x
            while y >= z:
                power *= x
                z = z + 1
            print("The power is %.3f" %power)
        exponent()

    elif (type == "remainder"):
        def modules():
            x = input ("Please put your first number: ")
            y = input ("Please put your second number: ")
            x = float(x)
            y = float(y)
            a = 0
            b = 0
            remainder = 0
            a = math.floor(x / y)
            b = int(a * y)
            remainder = x - b
            print ("The remainder is %.3f" %remainder)
        modules()

    elif (type == "min"):
        def minimum():
            list = []
            a = input("Enter a number, type z when you're done: ")
            b = " "
            while a != "z":
                a = input("Enter a number, type z when you're done: ")
                list.append(a)
                list.sort()
                b = min(list)
            print(b)

        minimum()

    elif (type == "max"):
        def maximum():
            list = []
            a = input("Enter a number, type z when you're done: ")
            b = " "
            while a != "z":
                a = input("Enter a number, type z when you're done: ")
                list.append(a)
                list.sort()
                b = max(list)
            print(b)

        maximum()

    elif(type == "btod"):
            def conversion1():
                x = input("Please put the binary number you want to convert: ")
                y = len(x)
                n = 0
                d = 0
                e = 0
                f = 0
                if "." not in x:
                    while y > 0:
                        a = y - 1
                        c = x[a]
                        c = float(c)
                        n = 2 ** c * a
                        d += n
                        y = y - 1
                    print("The decimal number of %s" %x + " is %f" %d)
                else:
                    first = x[0:x.index(".")]
                    last = x[x.index("."):y - 1]
                    a = len(first)
                    b = len(last)
                    print(a)
                    print(b)
                    while a > 0:
                        o = a - 1
                        c = x[o]
                        c = float(c)
                        n = 2 ** c * o
                        e += n
                        a = a - 1
                    while b < 0:
                        o = b - (b - 1)
                        c = x[o]
                        c = float(c)
                        n = 2 ** (0 - (c * o))
                        f += n
                        b = b - 1
                    d = e + f
                    print(d)
                    print("The decimal number of %s" %x + " is %f" %d)
            conversion1()

    elif(type == "btoo"):
        def conversion2():
            number = input("Please put the binary number you want to convert: ")
            [num_bef_dec, num_aft_dec] = number.split(".")
            side_a = len(num_bef_dec)
            side_b = len(num_aft_dec)
            output = " "
            output1 = " "
            index = 0
            group = number[index: index + 3]
            if side_a % 3 == 1:
                num_bef_dec = "00" + num_bef_dec
            elif side_a % 3 == 2:
                num_bef_dec = "0" + num_bef_dec
            else:
                num_bef_dec = num_bef_dec
            while index < side_a:
                group = num_bef_dec[index: index + 3]
                if group == "000":
                    current = "0"
                    output += str(current)
                elif group == "001":
                    current = "1"
                    output += str(current)
                elif group == "010":
                    current = "2"
                    output += str(current)
                elif group == "011":
                    current = "3"
                    output += str(current)
                elif group == "100":
                    current = "4"
                    output += str(current)
                elif group == "101":
                    current = "5"
                    output += str(current)
                elif group == "110":
                    current = "6"
                    output += str(current)
                elif group == "111":
                    current = "7"
                    output += str(current)
                index = index + 3
            output1 = output + "."
            index = 0

            output = " "
            if side_b % 3 == 1:
                num_aft_dec = str(num_aft_dec) + "00"
            elif side_b % 3 == 2:
                num_aft_dec = str(num_aft_dec) + "0"
            else:
                num_aft_dec = num_aft_dec
            while index < side_b:
                group = num_aft_dec[index: index + 3]
                if group == "000":
                    current = "0"
                    output += str(current)
                elif group == "001":
                    current = "1"
                    output += str(current)
                elif group == "010":
                    current = "2"
                    output += str(current)
                elif group == "011":
                    current = "3"
                    output += str(current)
                elif group == "100":
                    current = "4"
                    output += str(current)
                elif group == "101":
                    current = "5"
                    output += str(current)
                elif group == "110":
                    current = "6"
                    output += str(current)
                elif group == "111":
                    current = "7"
                    output += str(current)
                    index = index + 3
            output = output1 + output
            print(output)
        conversion2()

    elif(type == "btoh"):
        def conversion3():
            number = input("Please put the binary number you want to convert: ")
            [num_bef_dec, num_aft_dec] = number.split(".")
            side_a = len(num_bef_dec)
            side_b = len(num_aft_dec)
            output = " "
            index = 0
            group = number[index: index + 4]
            if side_a % 4 == 3:
                num_bef_dec = "0" + num_bef_dec
                print(num_bef_dec)
            elif side_a % 4 == 2:
                num_bef_dec = "00" + num_bef_dec
            elif side_a % 4 == 1:
                num_bef_dec = "000" + num_bef_dec
            else:
                num_bef_dec = num_bef_dec
                while index < side_a:
                    group = num_bef_dec[index: index + 4]
                    if group == "0000":
                        current = "0"
                        output += str(current)
                    elif group == "0001":
                        current = "1"
                        output += str(current)
                    elif group == "0010":
                        current = "2"
                        output += str(current)
                    elif group == "0011":
                        current = "3"
                        output += str(current)
                    elif group == "0100":
                        current = "4"
                        output += str(current)
                    elif group == "0101":
                        current = "5"
                        output += str(current)
                    elif group == "0110":
                        current = "6"
                        output += str(current)
                    elif group == "0111":
                        current = "7"
                        output += str(current)
                    elif group == "1000":
                        current = "8"
                        output += str(current)
                    elif group == "1001":
                        current = "9"
                        output += str(current)
                    elif group == "1010":
                        current = "A"
                        output += str(current)
                    elif group == "1011":
                         current = "B"
                         output += str(current)
                    elif group == "1100":
                          current = "C"
                          output += str(current)
                    elif group == "1101":
                        current = "D"
                        output += str(current)
                    elif group == "1110":
                         current = "E"
                         output += str(current)
                    elif group == "1111":
                          current = "F"
                          output += str(current)

                    index = index + 4
            output1 = output + "."
            output = " "
            index = 0
            if side_a % 4 == 3:
                num_aft_dec = num_aft_dec + "0"
            elif side_a % 4 == 2:
                num_aft_dec = num_aft_dec + "00"
            elif side_a % 4 == 1:
                num_aft_dec = num_aft_dec + "000"
            else:
                num_aft_dec = num_aft_dec
                while index < side_a:
                    group = num_aft_dec[index: index + 4]
                    if group == "0000":
                        current = "0"
                        output += str(current)
                    elif group == "0001":
                        current = "1"
                        output += str(current)
                    elif group == "0010":
                        current = "2"
                        output += str(current)
                    elif group == "0011":
                        current = "3"
                        output += str(current)
                    elif group == "0100":
                        current = "4"
                        output += str(current)
                    elif group == "0101":
                        current = "5"
                        output += str(current)
                    elif group == "0110":
                        current = "6"
                        output += str(current)
                    elif group == "0111":
                        current = "7"
                        output += str(current)
                    elif group == "1000":
                        current = "8"
                        output += str(current)
                    elif group == "1001":
                        current = "9"
                        output += str(current)
                    elif group == "1010":
                        current = "A"
                        output += str(current)
                    elif group == "1011":
                         current = "B"
                         output += str(current)
                    elif group == "1100":
                          current = "C"
                          output += str(current)
                    elif group == "1101":
                        current = "D"
                        output += str(current)
                    elif group == "1110":
                         current = "E"
                         output += str(current)
                    elif group == "1111":
                          current = "F"
                          output += str(current)

                    index = index + 4
            output = output1 + output
            print(output)
        conversion3()

calculator()
