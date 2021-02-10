def shift():
    alphabets = 'abcdefghijklmnopqrstuvwxyz '
    text = str(input("Input message : "))
    shift_number = int(input("Input how many shift : "))
    
    n = len(text)
    encrypted = ""
    
    for i in range (n) :
        char = text[i]
        loc = alphabets.find(char)
        new_loc = (loc + shift_number)%27
        encrypted += alphabets[new_loc]
        
    print("\nEncrypted message : ",encrypted)
    
    m = len(encrypted)
    decrypted = ""
    
    for k in range (m) :
        char2 = encrypted[k]
        loc2 = alphabets.find(char2)
        new_loc2 = (loc2 - shift_number)%27
        decrypted += alphabets[new_loc2]
    
    print("Decrypted message : ", decrypted)


print("\n === Shift Cipher ===")    
shift()