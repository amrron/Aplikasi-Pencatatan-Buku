import os
import time
import mysql.connector
from tabel import *

konek = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_buku"
    )

mycursor = konek.cursor()


def cls():
    os.system("cls")

def login():
    cls()
    print("SELAMAT DATANG DI APLIKASI PENDATAAN BUKU\n")

    user = input("Username  :")
    pwd = input("Password  :")

    if user == "admin" and pwd == "123":
        dashboard()

    else:
        print("Username atau password salah")
        time.sleep(1)
        login()

def dashboard():
    cls()
    print("SELAMAT DATANG DI DASHBOARD")
    print("DAFTAR BUKU\n")

    print()

    print("Pilih menu:\n1. Daftar Buku\n2. Tambah buku\n3. Ubah data buku\n4. Hapus buku\n5. Cari buku\n6. Keluar")

    pil = input("Masukan pilihan: ")

    if pil == "1":
        daftarbuku()
    if pil == "2":
        tambahbuku()
    if pil == "3":
        editbuku()
    if pil == "4":
        hapusbuku()
    if pil == "5":
        caribuku()
    if pil == "6":
        quit()

def tampilbuku(key="SELECT * FROM buku"):

    mycursor.execute(key)

    myresult = mycursor.fetchall()
    i = 1
    header("No", "Judul", "Genre", "Penulis", "Penerbit", "Tahun terbit", "ISBN", "Harga", leng=[3, 20, 10, 10, 15, 15, 14, 10])
    for x in myresult:
        row(i, x[1], x[2], x[3], x[4], x[5], x[6], x[7], leng=[3, 20, 10, 10, 15, 15, 14, 10])
        i += 1

def daftarbuku():
    cls()
    print("DAFTAR BUKU")
    tampilbuku()
    
    while True:
        pil  = input("Ketik 'keluar' untuk keluar: ")
        if pil == "keluar":
            dashboard()
            break

def tambahbuku():
    print("TAMBAH BUKU\n")
    while True:
        judul = input("Judul        : ")
        if len(judul) > 0:
            break
        print("Masukan judul!!!")

    while True:
        genre = input("Genre        : ")
        if len(genre) > 0:
            break
        print("Masukan genre!!!")

    while True:
        penulis = input("Penulis      : ")
        if len(penulis) > 0:
            break
        print("Masukan penulis!!!")

    while True:
        penerbit = input("Penerbit     : ")
        if len(penerbit) > 0:
            break
        print("Masukan penerbit!!!")

    while True:
        thn_terbit = input("Tahun terbit : ")
        if len(thn_terbit) > 0:
            break
        print("Masukan tahun terbit!!!")

    while True:
        isbn = input("ISBN         : ")
        if len(isbn) > 0:
            break
        print("Masukan ISBN!!!")

    while True:
        harga = input("Harga        : ")
        if len(harga) > 0:
            break
        print("Masukan harga!!!")
    
    # judul = input("Judul        : ")
    # genre = input("Genre        : ")
    # penulis = input("Penulis      : ")
    # penerbit = input("Penerbit     : ")
    # thn_terbit = input("Tahun terbit : ")
    # isbn = input("ISBN         : ")
    # harga = input("Harga        : ")

    sql = "INSERT INTO buku (id, judul, genre, penulis, penerbit, thn_terbit, isbn, harga) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = ("", judul, genre, penulis, penerbit, thn_terbit, isbn, harga)

    mycursor.execute(sql, val)
    konek.commit()

    print(mycursor.rowcount, "Buku berhasil di tambahkan.")
    time.sleep(1)
    dashboard()

def hapusbuku():
    cls()
    tampilbuku()
    pil = input("Pilih nomer yang akan dihapus: ")

    no = int(pil)

    mycursor.execute("SELECT * FROM buku")
    myresult = mycursor.fetchall()

    id = myresult[no-1][0]

    sql = "DELETE FROM buku WHERE id = " + str(id)

    mycursor.execute(sql)

    konek.commit()

    print(mycursor.rowcount, "Data berhasil dihapus")
    time.sleep(1)
    dashboard()

def editbuku():
    cls()
    tampilbuku()
    print()
    mycursor.execute("SELECT * FROM buku")
    myresult = mycursor.fetchall()
    no = int(input("Pilih no yang akan diubah: "))
    id = myresult[no-1][0]
    edit(id)

def edit(id):
    cls()
    print("Kosongkan bagian yang tidak ingin diubah")
    mycursor.execute("SELECT * FROM buku WHERE id = "+str(id))
    buku = mycursor.fetchall()
    judul = input("Judul        : ") or buku[0][1]
    genre = input("Genre        : ") or buku[0][2]
    penulis = input("Penulis      : ") or buku[0][3]
    penerbit = input("Penerbit     : ") or buku[0][4]
    thn_terbit = input("Tahun terbit : ") or buku[0][5]
    isbn = input("ISBN         : ") or buku[0][6]
    harga = input("Harga        : ") or buku[0][7]

    sql = "UPDATE buku SET judul='{}', genre='{}', penulis='{}', penerbit='{}', thn_terbit='{}', isbn='{}', harga='{}'  WHERE id = '{}'"
    sql = sql.format(judul, genre, penulis, penerbit, thn_terbit, isbn, harga, id)

    mycursor.execute(sql)
    konek.commit()

    print(mycursor.rowcount, "Data berhasil diubah")
    time.sleep(1)
    dashboard()

    
def caribuku():
    cls()
    print("CARI BUKU\n")

    while True:
        keyword = input("Masukan judul buku (ketik '.keluar' untuk keluar): ")
        if keyword == ".keluar":
            dashboard()
            break
        tampilbuku("SELECT * FROM buku WHERE judul LIKE '%"+keyword+"%'")