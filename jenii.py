def penjumlahan_deret_genap(n):
    total = 0
    for i in range(1, n + 1):
        bilangan_genap = 2 * i
        total += bilangan_genap
        print(" + ".join(str(j) for j in range(2, bilangan_genap + 1, 2)), "=", total)

# Panggil fungsi dengan parameter n sesuai dengan tinggi segitiga yang diinginkan
tinggi_segitiga = 5
penjumlahan_deret_genap(tinggi_segitiga)
