print("Selamat Datang Ke Toko Takoyaki")
print("-------------------------------")
print("1. Takoyaki Isi Sosis : Rp.2000")
print("2. Takoyaki isi Keju : Rp.2500")
print("-------------------------------")
input_menu = input("Pilih Isi Takoyaki : ")

if input_menu == "1":
    jumlah_beli = int(input("Beli Berapa Takoyaki : "))
    print("-------------------------------")
    if jumlah_beli <= 45:
        subtotal = jumlah_beli * 2000
        diskon = 0
        if jumlah_beli >= 10:
            diskon = subtotal * 10 / 100
        total_harga = subtotal - diskon
        print(f"Subtotal : Rp.{subtotal}")
        print(f"Diskon : Rp.{diskon}")
        print(f"Total : Rp.{total_harga}")
    else:
        print("Takoyakinya Nggak Cukup")
elif input_menu == "2":
    jumlah_beli = int(input("Beli Berapa Takoyaki : "))
    print("-------------------------------")
    if jumlah_beli <= 40:
        subtotal = jumlah_beli * 2500
        diskon = 0
        if jumlah_beli >= 8:
            diskon = subtotal * 8 / 100
        total_harga = subtotal - diskon
        print(f"Subtotal : Rp.{subtotal}")
        print(f"Diskon : Rp.{diskon}")
        print(f"Total : Rp.{total_harga}")
    else:
        print("Takoyakinya Nggak Cukup")
else:
    print("Inputan Invalid")