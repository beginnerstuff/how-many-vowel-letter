sesli_harfler="aeıioöuü"

kelime =input("bir kelime girin:")

sayı=0
for i in kelime:
    if i in sesli_harfler:
        sayı +=1
mesaj="\n{}kelimesinde {} tane sesli harf vardır."

print(mesaj.format(kelime,sayı))

input("\nçıkmak için bir tuşa basınız.")
