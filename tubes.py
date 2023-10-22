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
current_login = False
harga = 0
pesanan = []

# Fungsi
def cls():
    for i in range(100):
        print()


def beli_tiket(r, c, matrix):
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
    
    while studio_1[pilih_r][pilih_c]:
        print(f"Kursi Telah dipesan\n")
        pilih_r = int(input("Pilih baris\t: "))
        pilih_c = int(input("Pilih kolom\t: "))

    matrix[pilih_r][pilih_c] = True

    return 30



def beli_makanan():
    print(f"Silahkan pilih makanan di bawah:\n\n")

    print("1. Popcorn 20k")
    print("2. Minum 25k")
    print("3. Popcorn + Minum 40k")

    print(f"\n\nMasukkan sembarang untuk keluar")
    pilihan = input("Pilih nomor: ")
    if pilihan == "1":
        return 20
    elif pilihan == "2":
        return 25
    elif pilihan == "3":
        return 40
    else:
        return 0


def login(): # kurang cek benar / tidak
    global current_login
    if current_login:
        print("Anda sudah login")
    else:
        print(f"Login\n")
        uname = input(f"Masukkan Username\t: ")
        pw = input(f"Masukkan Password\t: ")
        current_login = True
        cls()
        print(f"\nSelamat Anda berhasil login\n")


def bayar(): # kurang metode bayar
    global current_login
    if current_login:
        print(f"Total harga adalah {harga}k.")
    else:
        login()
        bayar()


# main
cls()
while True:

    print(f"## SELAMAT DATANG DI XVI ##\n")
    print(f"Silahkan pilih menu di bawah:\n\n")

    print("1. Beli Tiket")
    print("2. Beli Makanan")
    print("3. Bayar")
    if not current_login:
        print("9. Login")

    print(f"\n\nTotal harga {harga}k\n\nMasukkan sembarang untuk keluar")
    pilihan = input("Pilih nomor: ")
    if pilihan == "9":
        cls()
        login()

    elif pilihan == "1":
        cls()
        print(f"Silahkan pilih film (harga 30k)\n")

        print(f"1. Spiderman \t12:00")
        print(f"2. Superman \t15:00")
        print(f"3. Batman \t19:00")

        pilihan_film = int(input(f"\n\nMasukkan nomor: "))
        n = int(input("Jumlah tiket: "))
        if pilihan_film == 1:
            for i in range(n):
                harga += beli_tiket(r_1, c_1, studio_1)
        if pilihan_film == 2:
            for i in range(n):
                harga += beli_tiket(r_2, c_2, studio_2)
        if pilihan_film == 3:
            for i in range(n):
                harga += beli_tiket(r_3, c_3, studio_3)
        cls()

    elif pilihan == "2":
        cls()
        n = int(input("Jumlah makanan: "))
        for i in range(n):
            harga += beli_makanan()
        cls()

    elif pilihan == "3": 
        cls()
        bayar()

        print(f"\nTerima kasih telah menggunakan aplikasi ini")
        break

    else:
        if harga == 0:
            print(f"\nTerima kasih telah menggunakan aplikasi ini")
            break
        else:
            bayar()
            break
        