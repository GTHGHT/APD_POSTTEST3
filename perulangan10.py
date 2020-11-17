import sys

bilangan = int(input("Masukkan Bilangan : "))
for i in range(sys.maxsize):
    if 10 ** i > bilangan:
        print(
            f"Bilangan 10^x yang terdekat adalah {10**i}"
        )
        break
