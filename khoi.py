def binary2int(binary): 
    int_val, i, n = 0, 0, 0
    
    while(binary != 0): 
        a = binary % 10
        int_val = int_val + a * pow(2, i) 
        binary = binary//10
        i += 1
    try: return(int_val) 
    except ValueError:
        print("Value error")

inpbin = int(input("Binary: "))
finalr = ""
def reverse(a):
    return a[::-1]
for i in range(int(len(str(inpbin))/2)):
    finalr += str(binary2int(inpbin%10000))
    inpbin = inpbin//10000
print(int(reverse(finalr)))
# print(finalr)
# binary2int(inpbin)