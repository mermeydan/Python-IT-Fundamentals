harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {harf: harfler.index(harf) for harf in harfler}


isimler = ["ışık", "ahmet",  "ismail", "çiğdem", "can", "şule"]

isimler.sort(key=lambda x: çevrim.get(x[0]))

print(isimler)
