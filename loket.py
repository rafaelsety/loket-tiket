import pandas as pd
import datetime

#list penumpang
nama = []
no_telp = []
tgl_pesan = []
tgl_berangkat =[]
#list tiket
tujuan = []
kelas = []
no_gerbong = []
no_kursi = []
#list pembayar
jml_tiket = []
x = datetime.datetime.now()
harga = []
total_bayar = []
uang_bayar = []
kembalian = []

i = 0

#data tiket
def tiket_jakarta():
    tujuan.append('Jakarta')
    print("Pilih kelas".center(50))
    print("A) Ekonomi    B) Eksekutif      C) Bisnis".center(50))
    print("Rp 100.000      Rp 200.000     Rp 300.000".center(50))
    print('-'*50)
    kode_kelas = input("Masukan Kelas [A/B/C] : ")
    print('-'*50)
    if kode_kelas == "A" or kode_kelas == "a":
        kelas.append('Ekonomi')
        harga.append(100000)
    elif kode_kelas == "B" or kode_kelas == "b":
        kelas.append('Eksekutif')
        harga.append(200000)
    elif kode_kelas == "C" or kode_kelas == "c":
        kelas.append('Bisnis')
        harga.append(300000)
    else:
        quit()

def tiket_bandung():
    tujuan.append('Bandung')
    print("Pilih kelas".center(50))
    print("A) Ekonomi    B) Eksekutif      C) Bisnis".center(50))
    print("Rp 200.000      Rp 300.000     Rp 400.000".center(50))
    print('-'*50)
    kode_kelas = input("Masukan Kelas [A/B/C] : ")
    print('-'*50)
    if kode_kelas == "A" or kode_kelas == "a":
        kelas.append('Ekonomi')
        harga.append(200000)
    elif kode_kelas == "B" or kode_kelas == "b":
        kelas.append('Eksekutif')
        harga.append(300000)
    elif kode_kelas == "C" or kode_kelas == "c":
        kelas.append('Bisnis')
        harga.append(400000)
    else:
        quit()

def tiket_yogyakarta():
    tujuan.append('Yogyakarta')
    print("Pilih kelas".center(50))
    print("A) Ekonomi    B) Eksekutif      C) Bisnis".center(50))
    print("Rp 300.000      Rp 400.000     Rp 500.000".center(50))
    print('-'*50)
    kode_kelas = input("Masukan Kelas [A/B/C] : ")
    print('-'*50)
    if kode_kelas == "A" or kode_kelas == "a":
        kelas.append('Ekonomi')
        harga.append(300000)
    elif kode_kelas == "B" or kode_kelas == "b":
        kelas.append('Eksekutif')
        harga.append(400000)
    elif kode_kelas == "C" or kode_kelas == "c":
        kelas.append('Bisnis')
        harga.append(500000)
    else:
        quit()

#input
print('-'*50)
print("KA LAJU JAYA".center(50))
print("Silahkan Input Data".center(50))
print('-'*50)
nama.append(input("Masukan Nama : "))
no_telp.append(input("Masukan No Telepon : "))
tgl_berangkat.append(input("Masukan Tanggal/Bulan/Tahun Keberangkatan : "))
jml_tiket.append(int(input("Jumlah Tiket : ")))

#proses
print('-'*50)
print('TUJUAN'.center(50))
print(" No Stasiun Asal  -  Stasiun Tiba")
print("(1)        Bogor  -       Jakarta")
print("(2)        Bogor  -       Bandung")
print("(3)        Bogor  -    Yogyakarta")
print('-'*50)
kode_tujuan = input("Masukkan Tujuan [1/2/3] : ")
print('-'*50)
if kode_tujuan == "1":
    tiket_jakarta()
elif kode_tujuan == "2":
    tiket_bandung()
elif kode_tujuan == "3":
    tiket_yogyakarta()
else:
    quit()

pilih = input("Lanjut Pilih Gerbong & Kursi [Y/T] ? ")
if pilih == 'Y' or pilih == 'y':
    a = 0
    while a < jml_tiket[i]:
        print("Penumpang ke-", a+1)
        no_gerbong.append(input("Masukan Nomor Gerbong : "))
        no_kursi.append(input("Masukan Nomor Kursi   : "))
        a=a+1
elif pilih == 'T' or pilih == 't':
    quit()
print('-'*50)

#output
print("\n\n")
print('-'*50)
print("KA LAJU JAYA".center(50))
print("STRUK PEMBELIAN TIKET KERETA API".center(50))
print('-'*50)
#data penumpang
print("Nama                  :", nama[i])
print("Nomor Telepon         :", no_telp[i])
print("Tanggal Pemesanan     :", x.strftime("%x"))
#data tiket
penumpang = {
    "Tujuan" : tujuan *jml_tiket[i],
    "Kelas" : kelas *jml_tiket[i],
    "  No Gerbong" : no_gerbong,
    "  No kursi" : no_kursi
}
data = pd.DataFrame(penumpang)
data.index += 1
print('-'*50)
print("Data Tiket".center(50))
print(data)
print('-'*50)
print("Tanggal Keberangkatan :", tgl_berangkat[i])
print("Jumlah Tiket          :",jml_tiket[i])
print("Harga / Tiket         : Rp",harga[i])
admin = 5000
print("Biaya Admin           : Rp",admin)
print('-'*50)
#data bayar
total_bayar.append(harga[i] * jml_tiket[i] + admin)
print("Total Harga           : Rp",total_bayar[i])
print('-'*50)
uang_bayar.append(int(input("Uang Bayar            : Rp ")))
kembalian.append(uang_bayar[i] - total_bayar[i])
print("Uang Kembali          : Rp",kembalian[i])