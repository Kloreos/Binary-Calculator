#ajaja

while True:
    inpchoice = input("Addition[Y]-Subtraction [N]-: ")
    if inpchoice == "Y":
        FirstBinary = input("Enter bin1: ")
        SecondBinary = input("Enter bin2: ")
        sum = bin(int(FirstBinary, 2) + int(SecondBinary, 2))
        print('Answer = ',sum[2:])
    elif inpchoice == "N":
        a = input("Enter bin1: ")
        b = input("Enter bin2: ")
        sum = bin(int(a, 2) - int(b, 2))
        print(sum[2:])
    else: 
        print("ded")