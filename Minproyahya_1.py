#NAMA: YAHYA JAILANI
#KELAS: SISTEM INFORMASI C
#NIM: 2409116085
#TEMA: Sistem Manajemen Produk Di Aplikasi LUNApos

produk = []

print("=== Data Aplikasi ===")
print("1. Masukan Produk")
print("2. Lihat Produk")
print("3. promo special")

masukan = (input(f"pilih produk (1-3): "))

if masukan == "1":
    nama = input("masukan jenis produk yang ingin dijual atau dibeli: ")
    jumlah = float(input("masukan harga produk: "))
    jual = int(input("masukan harga jual: "))
    promo = int(input("masukan promo penjualan jika ada: "))
    produk = [nama, jumlah, jual, promo]
    total = str(jumlah - promo)
    print("total harga jika berpromo adalah : " + ", Rp. " + total)
    print("produk berhasil di tambahkan")

if masukan == "2": 
    produk_saya = ["americano", "cappucino", "greentea", "stickymilk"]
    print(produk_saya)

if masukan == "3":
    promo_special = ("greentea", "cappucino")
    print(promo_special)

else:
    print("promo special telah habis")
   

