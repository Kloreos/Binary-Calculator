while True:
    def binary2int(binary): 
        int_val, i, n = 0, 0, 0
        
        while(binary != 0): 
            a = binary % 10
            int_val = int_val + a * pow(2, i) 
            binary = binary//10
            i += 1
        try: print(int_val) 
        except ValueError:
            print("Wrong value enter again noob")
    inpbin = int(input("Binary: "))

    binary2int(inpbin)