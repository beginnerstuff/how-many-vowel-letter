




class findingVowels():
    print("sesli harf bulma uygulaması ")
    
    vowel_letters="aeıioöuü"
    number=0
    control = True
    while control:
        word =input("bir kelime girin:")

        for i in word:
            if i in vowel_letters:
                number +=1
        message="\n{} kelimesinde {} tane sesli harf vardır."

        print(message.format(word,number))


