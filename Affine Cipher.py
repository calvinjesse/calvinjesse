import math

def affine():    
    a=int(input("Input a = "))
    b=int(input("Input b = "))
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    text = str(input("Input message : "))
    
    n = len(text)
    encrypted = ""
    
    if math.gcd(a,26)==1 :
        
        for i in range (n) :
            char = text[i]
            loc = alphabets.find(char)
            new_loc = (a*loc + b)%26
            encrypted += alphabets[new_loc]
        p = encrypted.upper()    
        print("\nEncrypted message : ",p,"\n")
        
        
        for x in range (0,26):
            if (((a%26) * (x%26)) % 26 == 1):
                print("Invers dari ",a," adalah ",x,"\n")
                inv=x
        
        m = len(encrypted)
        decrypted = ""        
    
        for k in range (m) :
            char2 = encrypted[k]
            loc2 = alphabets.find(char2)
            new_loc2 = (inv*(loc2-b))%26
            decrypted += alphabets[new_loc2]
        
        print("Decrypted message : ", decrypted)
    
    else :
        print (a,"mod26 != 1, your message can't be encrypted")
    
affine()
    
    
