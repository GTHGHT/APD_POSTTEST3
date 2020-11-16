import sys

bilangan = int(input("Masukkan Bilangan : "))
for i in range(sys.maxsize):
    if 10 ** i > bilangan:
        print(
            f"Bilangan Pangkat 10 yang terdekat adalah {10**i}"
        )
        break