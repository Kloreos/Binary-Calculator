inprange = int(input("Enter range:"))
finalr = ""
switch = False
for i in range(inprange):
    inpask = input('\nEnter dec: ')
    if int(inpask)<10 and int(inpask)>=4:
        def DecimalToBinary(num):
            global finalr
            if num >= 1:
                DecimalToBinary(num // 2)
            # print(num % 2)
            a = num%2
            finalr += str(a)
            # print(finalr)
        finalr+= " "
    elif int(inpask)<10 and int(inpask)>=2:
        def DecimalToBinary(num):
            global finalr
            if num >= 1:
                DecimalToBinary(num // 2)
            # print(num % 2)
            a = num%2
            
            finalr += str(a)
            # print(finalr)
        finalr+= " "
        finalr+="0"

    elif int(inpask) == 1:
        def DecimalToBinary(num):
            global finalr
            if num >= 1:
                DecimalToBinary(num // 2)
            # print(num % 2)
            a = num%2
            
            finalr += str(a)
            # print(finalr)
        finalr+= " "
        finalr+="00"
    DecimalToBinary(int(inpask))
print(finalr)