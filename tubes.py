# Deklarasi studio
r_1 = 7
c_1 = 10
studio_1 = [[False for i in range(c_1 + 1)] for j in range(r_1 + 1)]
r_2 = 6
c_2 = 9
studio_2 = [[False for i in range(c_2 + 1)] for j in range(r_2 + 1)]
r_3 = 4
c_3 = 6
studio_3 = [[False for i in range(c_1 + 1)] for j in range(r_3 + 1)]

# Deklarasi kondisi
akun = {
    "user": "user",
    "username": "password",
    "admin": "admin",
    "uname": "pw"
}
tanggal = ""
current_login = False
harga = 0
saldo_qris = 10000
saldo_spay = 9000
saldo_ovo = 8000
saldo_vm = 7000
pesanan_tiket = []
pesanan_makanan = []

for i in range(4, 6):
    for j in range(4, 8):
        studio_1[i][j] = True
studio_1[3][4] = True
studio_1[3][2] = True
studio_1[3][5] = True
studio_1[3][8] = True
studio_1[6][1] = True
studio_1[6][2] = True
studio_1[6][3] = True

# Fungsi
def cls():
    for i in range(100):
        print()


def beli_tiket(r, c, matrix, nama, jam):
    r += 1; c += 1
    for i in range(c):
        print("---", end='')
    print()
    for i in range(c-4):
        print("--", end='')
    print("LAYAR", end='')
    for i in range(c-4):
        print("--", end='')
    print()
    for i in range(c):
        print("---", end='')
    print(f"\n")
    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                print("   ", end='')
            elif i == 0:
                print(f"{j}  ", end='')
            elif j == 0:
                print(f"{i}  ", end='')
            else:
                if matrix[i][j]:
                    print("#  ", end='')
                else:
                    print("_  ", end='')
        print()

    pilih_r = int(input("Pilih baris\t: "))
    pilih_c = int(input("Pilih kolom\t: "))
    
    while matrix[pilih_r][pilih_c]:
        print(f"Kursi Telah dipesan\n")
        pilih_r = int(input("Pilih baris\t: "))
        pilih_c = int(input("Pilih kolom\t: "))
    while pilih_c < 1 or pilih_c > c or pilih_r < 1 or pilih_r > r:
        print("Nomor tidak valid")
        pilih_r = int(input("Pilih baris\t: "))
        pilih_c = int(input("Pilih kolom\t: "))


    matrix[pilih_r][pilih_c] = True
    pesanan_tiket.append([nama, jam, pilih_r, pilih_c, 30])

    return 30


def beli_makanan():
    print(f"Silahkan pilih makanan di bawah:\n\n")

    print("1. Popcorn 20k")
    print("2. Minum 25k")
    print("3. Popcorn + Minum 40k")

    print(f"\n\nMasukkan sembarang untuk keluar")
    pilihan = input("Pilih nomor: ")
    jumlah_item = int(input("Jumlah item: "))
    if pilihan == "1":
        pesanan_makanan.append([f"Popcorn\t", jumlah_item, jumlah_item * 20])
        return jumlah_item * 20
    elif pilihan == "2":
        pesanan_makanan.append([f"Minum\t", jumlah_item, jumlah_item * 25])
        return jumlah_item * 25
    elif pilihan == "3":
        pesanan_makanan.append(["Popcorn + Minum", jumlah_item, jumlah_item * 40])
        return jumlah_item * 40
    else:
        return 0


def login(): 
    global current_login
    if current_login:
        print("Anda sudah login")
    else:
        print(f"Login\n")
        uname = input(f"Masukkan Username\t: ")
        pw = input(f"Masukkan Password\t: ")
        if uname in akun:
            if akun[uname] == pw:
                current_login = True
            else:
                login()
        else:
            print(f"Username tidak ditemukan\n")
            login()
        cls()
        print(f"\nSelamat Anda berhasil login\n")


def bayar(): 
    global current_login
    if current_login:
        global saldo_qris
        global saldo_spay
        global saldo_ovo
        global saldo_vm
        bill()
        print(f"\nPilih metode pembayaran di bawah:\n")
        print(f"1. QRIS                 {saldo_qris}k")
        print(f"2. Shopeepay            {saldo_spay}k")
        print(f"3. Ovo                  {saldo_ovo}k")
        print(f"4. Visa / Mastercard    {saldo_vm}k")
        metode = input("Pilih Nomor: ").strip()
        if metode == "1":
            saldo_qris -= harga
            print(f"Sisa saldo {saldo_qris}k")
            print(f"Booking id: {tanggal}0001")
        elif metode == "2":
            saldo_spay -= harga
            print(f"Sisa saldo {saldo_spay}k")
            print(f"Booking id: {tanggal}0001")
        elif metode == "3":
            saldo_ovo -= harga
            print(f"Sisa saldo {saldo_ovo}k")
            print(f"Booking id: {tanggal}0001")
        elif metode == "4":
            saldo_vm -= harga
            print(f"Sisa saldo {saldo_vm}k")
            print(f"Booking id: {tanggal}0001")
        else:
            print("Pilihan tidak valid")
            bayar()
    else:
        login()
        bayar()


def bill():
    idx = 1

    print(f"\nNo.\tNama Item\tWaktu\tBaris\tKolom\tJumlah\tHarga")
    for x in pesanan_tiket:
        print(f"{idx}.\t{x[0]}\t{x[1]}\t{x[2]}\t{x[3]}\t1\t{x[4]}k")
        idx += 1
    for x in pesanan_makanan:
        print(f"{idx}.\t{x[0]}\t\t\t\t{x[1]}\t{x[2]}k")
        idx += 1
    print(f"Total\t\t\t\t\t\t\t{harga}k\n")


# main
cls()
while True:
    if pesanan_makanan or pesanan_tiket:
        bill()

    print(f"## SELAMAT DATANG DI XVI ##\n")
    print(f"Silahkan pilih menu di bawah:\n\n")

    print("1. Beli Tiket")
    print("2. Beli Makanan")
    print("3. Bayar")
    # print("4. Keranjang Belanja")
    if not current_login:
        print("9. Login")

    print(f"\n\nMasukkan sembarang untuk keluar")
    pilihan = input("Pilih nomor: ")
    if pilihan == "9":
        cls()
        login()

    elif pilihan == "1":
        cls()
        tanggal = input("Masukkan tanggal dengan format yyyy/mm/dd: ")
        print(f"Silahkan pilih film (harga 30k)\n")

        print(f"1. Revenger \t12:00")
        print(f"2. Life of Po \t15:00")
        print(f"3. Covid-19 \t19:00")

        print(f"\nMasukkan sembarang untuk keluar")
        pilihan_film = int(input(f"Masukkan nomor: "))
        if pilihan_film == 1:
            n = int(input("Jumlah tiket: "))
            for i in range(n):
                harga += beli_tiket(r_1, c_1, studio_1, "Revenger", "12:00")
        elif pilihan_film == 2:
            n = int(input("Jumlah tiket: "))
            for i in range(n):
                harga += beli_tiket(r_2, c_2, studio_2, "Life of Po", "15:00")
        elif pilihan_film == 3:
            n = int(input("Jumlah tiket: "))
            for i in range(n):
                harga += beli_tiket(r_3, c_3, studio_3, "Covid-19", "19:00")
        cls()

    elif pilihan == "2":
        cls()
        harga += beli_makanan()
        cls()

    elif pilihan == "3": 
        cls()
        bayar()

        print(f"\nTerima kasih telah menggunakan aplikasi ini")
        break

    # elif pilihan == "4":
    #     cls()
    #     bill()

    else:
        if harga == 0:
            print(f"\nTerima kasih telah menggunakan aplikasi ini")
            break
        else:
            bayar()
            break
        