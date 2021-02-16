e = 97
z = 26

def enc_vignere(word, key):
    key_list = list(key)
    n = len(key_list)
    n_word = len(word)
    count = n_word // n
    re = n_word % n
    word_new = ''

    for i in range(count+1):
        if i != count:
            sample = word[i*n:(i+1)*n]
            for j in range(n):
                x1_letter,x2_letter = key_list[j], sample[j]
                x1,x2 = ord(x1_letter)-e,ord(x2_letter)-e
                y = (x1+x2)%z
                l = chr(y+e)
                word_new = word_new + l
        else:
            sample = word[i*n:n_word+1]
            for j in range(re):
                x1_letter,x2_letter = key_list[j], sample[j]
                x1,x2 = ord(x1_letter)-e,ord(x2_letter)-e
                y = (x1+x2)%z
                l = chr(y+e)
                word_new = word_new + l

    return word_new

def dec_vignere(word,key):
    key_list = list(key)
    n = len(key_list)
    n_word = len(word)
    count = n_word // n
    re = n_word % n
    word_res = ''

    for i in range(count+1):
        if i != count:
            sample = word[i*n:(i+1)*n]
            for j in range(n):
                x1_letter,x2_letter = key_list[j], sample[j]
                x1,x2 = z-(ord(x1_letter)-e),ord(x2_letter)-e
                y = (x1+x2)%z
                l = chr(y+e)
                word_res = word_res + l
        else:
            sample = word[i*n:n_word+1]
            for j in range(re):
                x1_letter,x2_letter = key_list[j], sample[j]
                x1,x2 = z-(ord(x1_letter)-e),ord(x2_letter)-e
                y = (x1+x2)%z
                l = chr(y+e)
                word_res = word_res + l

    return word_res

print(enc_vignere("hariinibelajarkripto","hai"))
print(dec_vignere("oazpivpbmsarhrsyixao","hai"))