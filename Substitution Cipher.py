def subs():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key      = "qwertyuioplkjhgfdsazxcvbnm"
    
    text = str(input("Input message : "))
    
    encrypted = ""
    
    for i in text:
        if i.lower() in alphabet:
            encrypted += key[alphabet.find(i.lower())]
        else:
            encrypted += i
        
    print("\nEncrypted message : ",encrypted)
    
    decrypted = ""
    
    for k in encrypted :
        if k.lower() in key:
            decrypted += alphabet[key.find(k.lower())]
        else:
            decrypted += k
    
    print("Decrypted message : ",decrypted)

print("\n === Substitution Cipher ===")    
subs()