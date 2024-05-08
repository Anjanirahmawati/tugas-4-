def hitung_perkalian_dan_cetak(n):
    hasil = 1
    for i in range(1, n+1):
        print("1", end=" ")
        for j in range(3, 2*i, 2):
            print("*", j, end=" ")
            hasil *= j
        print("= ", hasil)
        hasil = 1

tinggi_segitiga = 5
hitung_perkalian_dan_cetak(tinggi_segitiga)
