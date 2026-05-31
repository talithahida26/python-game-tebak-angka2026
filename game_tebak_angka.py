import random
print("===Game Tebak Angka===")
print("gua udah milih angka, giliran lu buat nebak")
angka_rahasia= random.randint(1,50)
tebakan=0
while tebakan!= angka_rahasia:
    tebakan =int(input("Masukin tebakan lu :"))
    if tebakan <angka_rahasia:
        print("kekecilan, coba lagi!")
    elif tebakan >angka_rahasia:
        print("Kegedean jir lah, coba lagi!")
else:
            print(f"BENERRRRR JAGO LU GUA AKUIN, angkanya {angka_rahasia}")