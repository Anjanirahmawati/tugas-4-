def hitung_deret_ganjil(jumlah_deret):
    deret_ganjil = [2 * i + 1 for i in range(jumlah_deret)]
    total = sum(deret_ganjil)
    return deret_ganjil, total

jumlah_deret = 10
deret, hasil = hitung_deret_ganjil(jumlah_deret)

print("Deret bilangan ganjil:", ' + '.join(map(str, deret)), "=", hasil)
