def infinity():
    i=0
    while True:
        i+=1
        yield i


bilangan = int(input("Masukkan Bilangan"))
for i in infinity():
    if 10 ** i > bilangan:
        print(f"Bilangan Pangkat 10 yang terdekat adalah {10**i}")
        break
