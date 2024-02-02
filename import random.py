import random


harfler = "abcdefghijklnopqrstuvwxyz"
buyukharfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayilar = "1234567890"
semboller = "+-/*!&$#?=@"

def olusturma():
    karakterler = [harfler, buyukharfler, sayilar, semboller]

    uzunluk = int(input("şifreniz kaç haneli olsun?"))

    sifre=""

    oran = uzunluk = uzunluk / 2


    for i in range(oran):  
        sifre += random.choice(harfler)
    for i in range(oran):  
        sifre += random.choice(buyukharfler)     
    print(sifre)

olusturma()

while True:

    yenileme = input("şifreyi yenilemek istermisiniz?")
    if yenileme == ("evet"):
        olusturma()
    elif yenileme == ("Evet"):
        olusturma()
    elif yenileme == ("EVET"):
        olusturma()
    else:
        print("yazım hatası yaptıysanız tekrar deneyin")


