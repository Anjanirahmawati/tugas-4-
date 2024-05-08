# Inisialisasi variabel
jumlah_deret = 10
total = 0

# Loop untuk menghasilkan deret bilangan genap dan menjumlahkannya
for i in range(1, jumlah_deret + 1):
    bilangan_genap = 2 * i
    total += bilangan_genap

# Menampilkan hasil
print("Hasil penjumlahan 10 deret bilangan genap:")
print(" + ".join(str(2 * i) for i in range(1, jumlah_deret + 1)), "=", total)
