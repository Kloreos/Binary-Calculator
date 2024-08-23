while True:
    a = input("Enter bin1: ")
    b = input("Enter bin2: ")
    sum = bin(int(a, 2) - int(b, 2))
    print(sum[2:])