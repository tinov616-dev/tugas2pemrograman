from produk import Produk

banyak_produk = 2
total_semua_pembelian = 0

for i in range(banyak_produk):
    print(f"\nProduk ke-{i+1}")
    nama_produk = input("Masukan nama Produk: ")
    harga_produk = int(input("Masukan Harga Produk: "))
    jumlah_beli = int(input("Masukan Jumlah Produk: "))

    item = Produk(nama_produk, harga_produk)
    total_pembelian = item.hitung_total(jumlah_beli)
    diskon = item.hitung_diskon(total_pembelian)
    total_akhir = total_pembelian - diskon

    print(f"Total Pembelian {item.nama}: Rp {total_pembelian}")
    print(f"Diskon: Rp {diskon}")
    print(f"Total Pembelian {item.nama} setelah diskon: Rp {total_akhir}")

    total_semua_pembelian += total_akhir

print(f"\nTotal Seluruh Pembelian: Rp {total_semua_pembelian}")