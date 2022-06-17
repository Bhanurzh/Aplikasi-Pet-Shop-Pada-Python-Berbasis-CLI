import mysql.connector
import os
import random

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "petshop"
)

def clear_screen():
    os.system("cls")

#========================================================================================================================================
def back_to_menu_transaksi():
    print("\n")
    input("Tekan Enter Untuk Kembali Ke Menu Transaksi")
    transaksi(db)

def transaksi(db):
    clear_screen()
    while True:
        print("\t\t\t=========== Menu Transaksi ===========")
        print("\t\t\t[1] Makanan Aksesoris Obat dan Vitamin")
        print("\t\t\t[2] Grooming")
        print("\t\t\t[3] Penitipan Hewan")
        print("\t\t\t[4] Kembali")
        print("\t\t\t--------------------------------------")
        pilih = int(input("\t\t\tPilihan anda : "))
        if pilih == 1:
            shoping(db)
        elif pilih == 2:
            grooming(db)
        elif pilih == 3:
            penitipan(db)
        elif pilih == 4:
            main_menu(db)
        else:
            print("Pilihan Anda Salah!")
            continue

def grooming(db):
    clear_screen()
    jenis_transaksi = "Grooming"
    print("------------------------------------------------")
    print("Masukan data diri dan data hewan terlebih dahulu")
    print("------------------------------------------------")
    print()
    print("======= Data Diri =======")
    nama =   input("Nama   : ")
    alamat = input("Alamat : ")
    tlp =    input("No TLP : ")
    print("=========================")
    print()

    print("======= Data Hewan ======")
    nama_hewan=input("Nama Hewan        : ")
    jenis_hwn =input("Jenis Hewan       : ")
    jk =       input("Jenis Kelamin[B/J]: ")
    usia =     input("Usia Hewan        : ")
    berat =    input("Berat Hewan       : ")
    print("=========================")
    print()

    print("======== Pilihan Paket Grooming ========")
    print("[1] Paket Biasa              Rp.120.000")
    print("[2] Paket Premium            Rp.170.000")
    print("[3] Paket Spesial            Rp.230.000")
    print("----------------------------------------")
    biasa = 0; premium = 0; spesial = 0
    pilih = int(input("Pilihan anda: "))
    if pilih == 1:
        biasa = 120000
    elif pilih == 2:
        premium = 170000
    elif pilih == 3:
        spesial = 230000
    else:
        print("Pilihan anda salah!")

    admin = 5000
    total = 0
    total = biasa + premium + spesial
    kode_transaksi = random.randint(123456789,987654321)
    print()
    print("         Asteri Pet Shop")
    print("-----------------------------------")
    print("         Detail Transaksi")
    print("-----------------------------------")
    print("Nama Pelanggan:",nama)
    print("Nama Hewan    :",nama_hewan)
    print("Jenis Hewan   :",jenis_hwn)
    print("Jenis Kelamin :",jk)
    print("Usia          :",usia)
    print("Berat         :",berat)
    print("-----------------------------------")
    print("         Rincian Pembayaran")
    print("-----------------------------------")
    print("Biaya Admin   :Rp.",admin)
    print("Paket Grooming:Rp.",total)
    print("-----------------------------------")
    print("Kode Transaksi:",kode_transaksi)
    print("-----------------------------------")
    print("    SEGERA LAKUKAN PEMBAYARAN")
    print("\n")
    print("             Pembayaran")
    print("------------------------------------")
    status = ""
    grandtotal = total + admin
    while True:
        byr_kode = int(input("Masukan Kode Transaksi: "))
        if byr_kode == kode_transaksi:
            print("------------------------------------")
            print("Total Tagihan             : Rp.",grandtotal)
            bayar = int(input("Masukan Nominal Pembayaran: Rp. "))
            if bayar < total:
                print("    Mohon Maaf Uang anda kurang   ")
                print("Silahkan Melakukan Transaksi Ulang")
                print("------------------------------------")
                status = "Invalid"
                break
            else:
                print("Kembalian Anda            : Rp.", bayar - grandtotal)
                print("------------------------------------")
                status = "Approve"
                break
        else:
            print("   Mohon Maaf Kode Transaksi Anda Salah!!   ")
            print("Silahkan Masukan Kembali Kode Transaksi Anda")
            continue
    print("Status Pembayaran :",status)

    val1 = (nama, alamat, tlp)
    cursor = db.cursor()
    sql1 = "INSERT INTO pelanggan (nama, alamat, no_tlp) VALUES (%s, %s, %s)"
    cursor.execute(sql1, val1)
    db.commit()

    val2 = (nama_hewan, jenis_hwn, jk, usia, berat)
    cursor = db.cursor()
    sql2 = "INSERT INTO hewan (nama_hewan, jenis_hewan, jenis_kelamin, usia_hewan, berat_hewan) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql2, val2)
    db.commit()

    val3 = (nama, kode_transaksi, jenis_transaksi, grandtotal, status)
    cursor = db.cursor()
    sql3 = "INSERT INTO transaksi (nama_pelanggan, kode_transaksi, jenis_transaksi, total_tagihan, status_tagihan) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql3, val3)
    db.commit()

    val4 = (nama, jenis_transaksi, grandtotal, status)
    cursor = db.cursor()
    sql4 = "INSERT INTO riwayat_transaksi (nama_pelanggan, jenis_transaksi, total_tagihan, status_tagihan) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql4, val4)
    db.commit()
    back_to_menu_transaksi()
    
def penitipan(db):
    clear_screen()
    jenis_transaksi = "Penitipan Hewan"
    print("------------------------------------------------")
    print("Masukan data diri dan data hewan terlebih dahulu")
    print("------------------------------------------------")
    print()
    print("======= Data Diri =======")
    nama =   input("Nama   : ")
    alamat = input("Alamat : ")
    tlp =    input("No TLP : ")
    print("=========================")
    print()

    print("======= Data Hewan ======")
    nama_hewan=input("Nama Hewan        : ")
    jenis_hwn =input("Jenis Hewan       : ")
    jk =       input("Jenis Kelamin[B/J]: ")
    usia =     input("Usia Hewan        : ")
    berat =    input("Berat Hewan       : ")
    print("=========================")
    print()

    print("======== Pilihan Paket Penitipan ========")
    print("[1] Paket Bronze  (1 Hari)    Rp.30.000")
    print("[2] Paket Silver  (2 Hari)    Rp.50.000")
    print("[3] Paket Gold    (3 Hari)    Rp.80.000")
    print("[4] Paket Diamond (4 Hari)    Rp.130.000")
    print("-----------------------------------------")
    bronze = 0; silver = 0; gold = 0; diamond = 0
    durasi1 = ""; durasi2 = ""; durasi3 = ""; durasi4 = ""
    pilih = int(input("Pilihan anda: "))
    if pilih == 1:
        bronze = 30000
        durasi1 = "1 Hari"
    elif pilih == 2:
        silver = 50000
        durasi2 = "2 Hari"
    elif pilih == 3:
        gold = 80000
        durasi3 = "3 Hari"
    elif pilih == 4:
        diamond = 130000
        durasi4 = "4 Hari"
    else:
        print("Pilihan anda salah!")

    durasi_penitipan = durasi1 + durasi2 + durasi3 + durasi4
    admin = 5000
    total = 0
    total = bronze + silver + gold + diamond
    kode_transaksi = random.randint(123456789,987654321)
    print()
    print("         Asteri Pet Shop")
    print("----------------------------------")
    print("         Detail Transaksi")
    print("----------------------------------")
    print("Nama Pelanggan:",nama)
    print("Alamat        :",alamat)
    print("No Telepon    :",tlp)
    print("Nama Hewan    :",nama_hewan)
    print("Jenis Hewan   :",jenis_hwn)
    print("Jenis Kelamin :",jk)
    print("Usia          :",usia)
    print("Berat         :",berat)
    print("-----------------------------------")
    print("         Rincian Pembayaran")
    print("-----------------------------------")
    print("Biaya Admin    :Rp.",admin)
    print("Paket Penitipan:Rp.",total)
    print("-----------------------------------")
    print("Kode Transaksi:",kode_transaksi)
    print("-----------------------------------")
    print("    SEGERA LAKUKAN PEMBAYARAN")
    print("\n")
    print("             Pembayaran")
    print("-----------------------------------")
    status = ""
    grandtotal = total + admin
    while True:
        byr_kode = int(input("Masukan Kode Transaksi: "))
        if byr_kode == kode_transaksi:
            print("------------------------------------")
            print("Total Tagihan             : Rp.",grandtotal)
            bayar = int(input("Masukan Nominal Pembayaran: Rp. "))
            if bayar < total:
                print("    Mohon Maaf Uang anda kurang   ")
                print("Silahkan Melakukan Transaksi Ulang")
                print("------------------------------------")
                status = "Invalid"
                break
            else:
                print("Kembalian Anda            : Rp.", bayar - grandtotal)
                print("------------------------------------")
                status = "Approve"
                break
        else:
            print("   Mohon Maaf Kode Transaksi Anda Salah!!   ")
            print("Silahkan Masukan Kembali Kode Transaksi Anda")
            continue
    print("Status Pembayaran :",status)

    val1 = (nama, alamat, tlp)
    cursor = db.cursor()
    sql1 = "INSERT INTO pelanggan (nama, alamat, no_tlp) VALUES (%s, %s, %s)"
    cursor.execute(sql1, val1)
    db.commit()

    val2 = (nama_hewan, jenis_hwn, jk, usia, berat)
    cursor = db.cursor()
    sql2 = "INSERT INTO hewan (nama_hewan, jenis_hewan, jenis_kelamin, usia_hewan, berat_hewan) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql2, val2)
    db.commit()

    val3 = (nama, kode_transaksi, jenis_transaksi, grandtotal, status)
    cursor = db.cursor()
    sql3 = "INSERT INTO transaksi (nama_pelanggan, kode_transaksi, jenis_transaksi, total_tagihan, status_tagihan) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql3, val3)
    db.commit()

    val4 = (nama, jenis_transaksi, grandtotal, status)
    cursor = db.cursor()
    sql4 = "INSERT INTO riwayat_transaksi (nama_pelanggan, jenis_transaksi, total_tagihan, status_tagihan) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql4, val4)
    db.commit()

    val5 = (nama_hewan, jenis_hwn, jenis_transaksi, durasi_penitipan)
    cursor = db.cursor()
    sql5 = "INSERT INTO kandang (nama_hewan, jenis_hewan, jenis_penggunaan, lama_penggunaan) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql5, val5)
    db.commit()
    back_to_menu_transaksi()

def menu_toko():
    menu = """
                                    ------------------------------------
    ==================================  Makanan Kering Kucing dan Anjing  ===================================
                                    ------------------------------------
    [1] Makanan Anak Kucing Me-O 500g   Rp.23.000           [7] Makanan Anjing Pedigree 1.5Kg      Rp.65.000       
    [2] Makanan Anak Kucing Me-O 1Kg    Rp.45.000           [8] Makanan Anjing Ganador 400g        Rp.20.000
    [3] Makanan Kucing Me-O 1Kg         Rp.50.000           [9] Makanan Anjing Dog Choize 800g     Rp.14.000
    [4] Makanan Kucing Whiskas 500g     Rp.26.000           [10] Makanan Anjing Alpo Dog 500g      Rp.15.000
    [5] Makanan Kucing Whiskas 750g     Rp.35.000           [11] Makanan Anjing Alpo Dog 1.5Kg     Rp.44.000
    [6] Makanan Kucing Royal Canin 250g Rp.29.000
    =========================================================================================================
                                        -------------------------------
                                        Aksesoris Kucing dan Anjing
                                        -------------------------------
    [12] Kalung Kucing Biasa            Rp.8.000            [17] Kalung Anjing Biasa               Rp.9.000    
    [13] Kalung Kucing Lonceng          Rp.10.000           [18] Kalung Anjing Custom Nama         Rp.35.000
    [14] Kalung Kucing Scarf Bandana    Rp.13.000           [19] Kaca Mata Anjing                  Rp.21.000
    [15] Kalung Kucing Custom Nama      Rp.30.000
    [16] Kaca Mata Kucing               Rp.19.000
    =========================================================================================================
                                    ----------------------------------
                                    Obat dan Vitamin Kucing dan Anjing
                                    ----------------------------------
    [20] Obat Kutu Kucing dan Anjing    Rp.79.000           [25] Vitamin Nafsu Makan Anjing        Rp.55.000
    [21] Obat Flu Batuk Kucing          Rp.43.000           [26] Vitamin Imunitas Kucing           Rp.40.000
    [22] Obat Tetes Mata Kucing         Rp.25.000           [27] Vitamin Imunitas Anjing           Rp.43.000
    [23] Obat Flu Batuk Anjing          Rp.50.000           [28] Vitamin Bulu Kucing dan Anjing    Rp.80.000
    [24] Vitamin Nafsu Makan Kucing     Rp.60.000           [29] Vitamin Diare Kucing              Rp.74.000
    =========================================================================================================
    """
    print(menu)

def shoping(db):
    clear_screen()
    jenis_transaksi = "Umum"
    print("---------------------------------")
    print("Masukan data diri terlebih dahulu")
    print("---------------------------------")
    print()
    print("======= Data Diri =======")
    nama =   input("Nama   : ")
    alamat = input("Alamat : ")
    tlp =    input("No TLP : ")
    print("=========================")
    print()

    menu_toko()
    mk1=0; mk2=0; mk3=0; mk4=0; mk5=0; mk6=0; mk7=0; mk8=0; mk9=0; mk10=0; mk11=0
    ak1=0; ak2=0; ak3=0; ak4=0; ak5=0; ak6=0; ak7=0; ak8=0
    ob1=0; ob2=0; ob3=0; ob4=0; vt1=0; vt2=0; vt3=0; vt4=0; vt5=0; vt6=0
    list_beli = []
    while True:
        print("Silahkan Pilih Nomor yang ingin Anda Pesan")
        pilih = int(input("Ingin Pesan Apa? : "))
        if pilih == 1:
            list_beli.append("Makanan Anak Kucing Me-O 500g")
            mk1+=23000
        elif pilih == 2:
            list_beli.append("Makanan Anak Kucing Me-O 1Kg")
            mk2+=45000
        elif pilih == 3:
            list_beli.append("Makanan Kucing Me-O 1Kg")
            mk3+=50000
        elif pilih == 4:
            list_beli.append("Makanan Kucing Whiskas 500g")
            mk4+=26000
        elif pilih == 5:
            list_beli.append("Makanan Kucing Whiskas 750g")
            mk5+=35000
        elif pilih == 6:
            list_beli.append("Makanan Kucing Royal Canin 250g")
            mk6+=29000
        elif pilih == 7:
            list_beli.append("Makanan Anjing Pedigree 1.5Kg")
            mk7+=65000
        elif pilih == 8:
            list_beli.append("Makanan Anjing Ganador 400g")
            mk8+=20000
        elif pilih == 9:
            list_beli.append("Makanan Anjing Dog Choize 800g")
            mk9+=14000
        elif pilih == 10:
            list_beli.append("Makanan Anjing Alpo Dog 500g")
            mk10+=15000
        elif pilih == 11:
            list_beli.append("Makanan Anjing Alpo Dog 1.5Kg")
            mk11+=44000
        elif pilih == 12:
            list_beli.append("Kalung Kucing Biasa")
            ak1+=8000
        elif pilih == 13:
            list_beli.append("Kalung Kucing Lonceng")
            ak2+=10000
        elif pilih == 14:
            list_beli.append("Kalung Kucing Scarf Bandana")
            ak3+=13000
        elif pilih == 15:
            list_beli.append("Kalung Kucing Custom Nama")
            ak4+=30000
        elif pilih == 16:
            list_beli.append("Kaca Mata Kucing")
            ak5+=19000
        elif pilih == 17:
            list_beli.append("Kalung Anjing Biasa")
            ak6+=9000
        elif pilih == 18:
            list_beli.append("Kalung Anjing Custom Nama")
            ak7+=35000
        elif pilih == 19:
            list_beli.append("Kaca Mata Anjing")
            ak8+=21000
        elif pilih == 20:
            list_beli.append("Obat Kutu Kucing dan Anjing")
            ob1+=79000
        elif pilih == 21:
            list_beli.append("Obat Flu Batuk Kucing")
            ob2+=43000
        elif pilih == 22:
            list_beli.append("Obat Tetes Mata Kucing")
            ob3+=25000
        elif pilih == 23:
            list_beli.append("Obat Flu Batuk Anjing")
            ob4+=50000
        elif pilih == 24:
            list_beli.append("Vitamin Nafsu Makan Kucing")
            vt1+=60000
        elif pilih == 25:
            list_beli.append("Vitamin Nafsu Makan Anjing")
            vt2+=55000
        elif pilih == 26:
            list_beli.append("Vitamin Imunitas Kucing")
            vt3+=40000
        elif pilih == 27:
            list_beli.append("Vitamin Imunitas Anjing")
            vt4+=43000
        elif pilih == 28:
            list_beli.append("Vitamin Bulu Kucing dan Anjing")
            vt5+=80000
        elif pilih == 29:
            list_beli.append("Vitamin Diare Kucing")
            vt6+=74000
        else:
            print("Pilihan Anda Tidak Terdapat didalam Menu!")
        tanya = input("Apakah masih ingin memesan? (Y/T): ")
        if tanya == 'y' or tanya == 'Y':
            continue
        else:
            break
    admin = 2000
    total = 0
    total = mk1+mk2+mk3+mk4+mk5+mk6+mk7+mk8+mk9+mk10+mk11+ak1+ak2+ak3+ak4+ak5+ak6+ak7+ak8+ob1+ob2+ob3+ob4+vt1+vt2+vt3+vt4+vt5+vt6
    kode_transaksi = random.randint(123456789,987654321)
    print()
    print("               Asteri Pet Shop")
    print("---------------------------------------------")
    print("        Daftar Belanja Yang Anda Pesan       ")
    print("---------------------------------------------")
    for daftar in list_beli:
        print("-> {}".format(daftar))
    print("---------------------------------------------")
    print("Total Belanja              : Rp.",total)
    print("Biaya Admin                : Rp.",admin)
    print("---------------------------------------------")
    print("Kode Transaksi             :",kode_transaksi)
    print("---------------------------------------------")
    print("          SEGERA LAKUKAN PEMBAYARAN          ")
    print("\n")
    print("                 Pembayaran                  ")
    print("---------------------------------------------")
    status = ""
    grandtotal = total + admin
    while True:
        byr_kode = int(input("Masukan Kode Transaksi: "))
        if byr_kode == kode_transaksi:
            print("---------------------------------------------")
            print("Total Tagihan             :Rp.",grandtotal)
            bayar = int(input("Masukan Nominal Pembayaran:Rp. "))
            if bayar < total:
                print("    Mohon Maaf Uang anda kurang   ")
                print("Silahkan Melakukan Transaksi Ulang")
                print("---------------------------------------------")
                status = "Invalid"
                break
            else:
                print("Kembalian Anda            : Rp.", bayar - grandtotal)
                print("---------------------------------------------")
                status = "Approve"
                break
        else:
            print("   Mohon Maaf Kode Transaksi Anda Salah!!   ")
            print("Silahkan Masukan Kembali Kode Transaksi Anda")
            continue
    print("Status Pembayaran :",status)

    val1 = (nama, alamat, tlp)
    cursor = db.cursor()
    sql1 = "INSERT INTO pelanggan (nama, alamat, no_tlp) VALUES (%s, %s, %s)"
    cursor.execute(sql1, val1)
    db.commit()

    val3 = (nama, kode_transaksi, jenis_transaksi, grandtotal, status)
    cursor = db.cursor()
    sql3 = "INSERT INTO transaksi (nama_pelanggan, kode_transaksi, jenis_transaksi, total_tagihan, status_tagihan) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql3, val3)
    db.commit()

    val4 = (nama, jenis_transaksi, grandtotal, status)
    cursor = db.cursor()
    sql4 = "INSERT INTO riwayat_transaksi (nama_pelanggan, jenis_transaksi, total_tagihan, status_tagihan) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql4, val4)
    db.commit()
    back_to_menu_transaksi()

#=======================================================================================================================
def all_data_transaksi_petshop(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM transaksi"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print()
        print("               Data Transaksi             ")
        print("------------------------------------------")
        for data in results:
            print("ID Transaksi        : ", data[0])
            print("Nama Pelanggan      : ", data[1])
            print("Kode Transaksi      : ", data[2])
            print("Jenis Transaksi     : ", data[3])
            print("Tanggal Transaksi   : ", data[4])
            print("Total Tagihan       :  Rp.", data[5])
            print("Status Tagihan      : ", data[6])
            print("------------------------------------------")
    print()
    back_to_menu_utama()

#=========================================================================================================================
def back_to_menu_data_pelanggan():
    print("\n")
    input("Tekan Enter Untuk Kembali Ke Menu Data Pelanggan")
    data_pelanggan(db)

def data_pelanggan(db):
    clear_screen()
    while True:
        print("\t\t\t=============== Menu Data Pelanggan ===============")
        print("\t\t\t[1] Tampilkan Data Pelanggan")
        print("\t\t\t[2] Update Data Pelanggan")
        print("\t\t\t[3] Menghapus Data Pelanggan")
        print("\t\t\t[4] Mencari Data Pelanggan")
        print("\t\t\t[5] Tampilkan Semua Riwayat Transaksi Pelanggan")
        print("\t\t\t[6] Tampilkan Beberapa Riwayat Transaksi Pelanggan")
        print("\t\t\t[7] Mencari Data Riwayat Transaksi")
        print("\t\t\t[8] Kembali")
        print("\t\t\t--------------------------------------------------")
        pilih = int(input("\t\t\tPilihan anda: "))
        if pilih == 1:
            all_data_pelanggan(db)
        elif pilih == 2:
            update_data_pelanggan(db)
        elif pilih == 3:
            hapus_data_pelanggan(db)
        elif pilih == 4:
            search_data_pelanggan(db)
        elif pilih == 5:
            all_data_riwayat_transaksi(db)
        elif pilih == 6:
            few_data_riwayat_transaksi(db)
        elif pilih == 7:
            search_data_riwayat_transaksi(db)
        elif pilih == 8:
            main_menu(db)
        else:
            print("Pilihan Anda Salah!!")
            continue

def all_data_pelanggan(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM pelanggan"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("ID Pelanggan        : ", data[0])
            print("Nama Pelanggan      : ", data[1])
            print("Alamat              : ", data[2])
            print("No Telepon          : ", data[3])
            print("==========================================")
    print()
    back_to_menu_data_pelanggan()

def update_data_pelanggan(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM pelanggan"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("ID Pelanggan        : ", data[0])
            print("Nama Pelanggan      : ", data[1])
            print("Alamat              : ", data[2])
            print("No Telepon          : ", data[3])
            print("==========================================")
    print()
    banyak = int(input("Berapa banyak Data yang ingin anda update? : "))
    for data in range(1, banyak+1):
        print("======== Mengupdate Data ke- {} ========".format(data))
        id = int(input("Masukan ID Pelanggan yang ingin di Update: "))
        nama =   input("Masukan Nama Baru       : ")
        alamat = input("Masukan Alamat Baru     : ")
        tlp =    input("Masukan No Telepon Baru : ")
        print("========================================")
        print("       Data ke- {} Sudah Terupdate      ".format(data))

        cursor = db.cursor()
        sql = "UPDATE pelanggan SET nama=%s, alamat=%s, no_tlp=%s WHERE id_pelanggan=%s"
        val = (nama, alamat, tlp, id)
        cursor.execute(sql, val)
        db.commit()

        cursor2 = db.cursor()
        sql2 = "UPDATE transaksi SET nama_pelanggan=%s where id_transaksi=%s"
        val2 = (nama, id)
        cursor2.execute(sql2, val2)
        db.commit()

        cursor3 = db.cursor()
        sql3 = "UPDATE riwayat_transaksi SET nama_pelanggan=%s where id_riwayat_transaksi=%s"
        val3 = (nama, id)
        cursor3.execute(sql3, val3)
        db.commit()
    print("{} data telah diupdate".format(banyak))
    back_to_menu_data_pelanggan()

def hapus_data_pelanggan(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM pelanggan"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("ID Pelanggan        : ", data[0])
            print("Nama Pelanggan      : ", data[1])
            print("Alamat              : ", data[2])
            print("No Telepon          : ", data[3])
            print("==========================================")
    print()
    banyak = int(input("Berapa banyak Data yang ingin anda hapus? : "))
    for data in range(1, banyak+1):
        print("======== Menghapus Data ke- {} ========".format(data))
        id = int(input("Masukan ID Pelanggan yang ingin di Hapus: "))
        print("========================================")
        print("       Data ke- {} Sudah Terhapus      ".format(data))

        cursor = db.cursor()
        sql = "DELETE FROM pelanggan WHERE id_pelanggan=%s"
        val = (id, )
        cursor.execute(sql, val)
        db.commit()
    print("{} data telah dihapus".format(banyak))
    back_to_menu_data_pelanggan()

def search_data_pelanggan(db):
    clear_screen()
    cursor = db.cursor()
    print("\nMasukan Kata Kunci berupa ID Pelanggan/Nama Pelanggan")
    keyword = input("Kata Kunci: ")
    sql = "SELECT * FROM pelanggan WHERE id_pelanggan = %s or nama = %s"
    val = (keyword, keyword)
    cursor.execute(sql, val)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("ID Pelanggan        : ", data[0])
            print("Nama Pelanggan      : ", data[1])
            print("Alamat              : ", data[2])
            print("No Telepon          : ", data[3])
            print("==========================================")
    back_to_menu_data_pelanggan()

def all_data_riwayat_transaksi(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM riwayat_transaksi"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print()
        print("            Riwayat Transaksi             ")
        print("------------------------------------------")
        for data in results:
            print("ID Riwayat Transaksi: ", data[0])
            print("Nama Pelanggan      : ", data[1])
            print("Jenis Transaksi     : ", data[2])
            print("Total Tagihan       :  Rp.", data[3])
            print("Status Tagihan      : ", data[4])
            print("Tanggal Transaksi   : ", data[5])
            print("------------------------------------------")
    print()
    back_to_menu_data_pelanggan()

def few_data_riwayat_transaksi(db):
    clear_screen()
    cursor = db.cursor(buffered=True)
    sql = "SELECT * FROM riwayat_transaksi"
    cursor.execute(sql)
    banyak = int(input("Banyak Data yang ingin ditampilkan> "))
    results = cursor.fetchmany(banyak)
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print()
        print("            Riwayat Transaksi             ")
        print("------------------------------------------")
        for data in results:
            print("ID Riwayat Transaksi: ", data[0])
            print("Nama Pelanggan      : ", data[1])
            print("Jenis Transaksi     : ", data[2])
            print("Total Tagihan       :  Rp.", data[3])
            print("Status Tagihan      : ", data[4])
            print("Tanggal Transaksi   : ", data[5])
            print("------------------------------------------")
    print()
    back_to_menu_data_pelanggan()

def search_data_riwayat_transaksi(db):
    clear_screen()
    cursor = db.cursor()
    print("\nMencari data berdasarkan ketentuan berikut:")
    print("ID Riwayat Transaksi")
    print("Nama Pelanggan")
    print("Jenis Transaksi [Grooming/Penitipan Hewan/Umum]")
    print("Status Tagihan  [Approve/Invalid]")
    print("--------------------------------------------------")
    print()
    keyword = input("Kata Kunci: ")
    sql = "SELECT * FROM riwayat_transaksi WHERE id_riwayat_transaksi = %s or nama_pelanggan = %s or jenis_transaksi = %s or status_tagihan = %s"
    val = (keyword, keyword, keyword, keyword)
    cursor.execute(sql, val)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print()
        print("            Riwayat Transaksi             ")
        print("------------------------------------------")
        for data in results:
            print("ID Riwayat Transaksi: ", data[0])
            print("Nama Pelanggan      : ", data[1])
            print("Jenis Transaksi     : ", data[2])
            print("Total Tagihan       :  Rp.", data[3])
            print("Status Tagihan      : ", data[4])
            print("Tanggal Transaksi   : ", data[5])
            print("------------------------------------------")
    print()
    back_to_menu_data_pelanggan()

#===================================================================================================================================
def back_to_menu_data_hewan():
    print("\n")
    input("Tekan Enter Untuk Kembali Ke Menu Data Hewan")
    data_hewan(db)

def data_hewan(db):
    clear_screen()
    while True:
        print("\t\t\t================= Menu Data Hewan ================")
        print("\t\t\t[1] Tampilkan Data Hewan")
        print("\t\t\t[2] Update Data Hewan")
        print("\t\t\t[3] Menghapus Data Hewan")
        print("\t\t\t[4] Mencari Data Hewan")
        print("\t\t\t[5] Kembali")
        print("\t\t\t--------------------------------------------------")
        pilih = int(input("\t\t\tPilihan anda: "))
        if pilih == 1:
            all_data_hewan(db)
        elif pilih == 2:
            update_data_hewan(db)
        elif pilih == 3:
            hapus_data_hewan(db)
        elif pilih == 4:
            search_data_hewan(db)
        elif pilih == 5:
            main_menu(db)
        else:
            print("Pilihan Anda Salah!!")
            continue

def all_data_hewan(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM hewan"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("ID Hewan            : ", data[0])
            print("Nama Hewan          : ", data[1])
            print("Jenis Hewan         : ", data[2])
            print("Jenis Kelamin       : ", data[3])
            print("Usia Hewan          : ", data[4])
            print("Berat Hewan         : ", data[5])
            print("==========================================")
    print()
    back_to_menu_data_hewan()

def update_data_hewan(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM hewan"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("ID Hewan            : ", data[0])
            print("Nama Hewan          : ", data[1])
            print("Jenis Hewan         : ", data[2])
            print("Jenis Kelamin       : ", data[3])
            print("Usia Hewan          : ", data[4])
            print("Berat Hewan         : ", data[5])
            print("==========================================")
    print()
    banyak = int(input("Berapa banyak Data yang ingin anda update? : "))
    for data in range(1, banyak+1):
        print("======== Mengupdate Data ke- {} ========".format(data))
        id = int(input("Masukan ID Hewan yang ingin di Update: "))
        nama_hewan  = input("Masukan Nama Baru       : ")
        usia        = input("Masukan Usia Yang Baru  : ")
        berat       = input("Masukan Berat Yang Baru : ")
        print("========================================")
        print("       Data ke- {} Sudah Terupdate      ".format(data))

        cursor = db.cursor()
        sql = "UPDATE hewan SET nama_hewan=%s, usia_hewan=%s, berat_hewan=%s WHERE id_hewan=%s"
        val = (nama_hewan, usia, berat, id)
        cursor.execute(sql, val)
        db.commit()
    print("{} data telah diupdate".format(banyak))
    back_to_menu_data_hewan()

def hapus_data_hewan(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM hewan"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("ID Hewan            : ", data[0])
            print("Nama Hewan          : ", data[1])
            print("Jenis Hewan         : ", data[2])
            print("Jenis Kelamin       : ", data[3])
            print("Usia Hewan          : ", data[4])
            print("Berat Hewan         : ", data[5])
            print("==========================================")
    print()
    banyak = int(input("Berapa banyak Data yang ingin anda hapus? : "))
    for data in range(1, banyak+1):
        print("======== Menghapus Data ke- {} ========".format(data))
        id = int(input("Masukan ID Hewan yang ingin di Hapus: "))
        print("========================================")
        print("       Data ke- {} Sudah Terhapus      ".format(data))

        cursor = db.cursor()
        sql = "DELETE FROM hewan WHERE id_hewan=%s"
        val = (id, )
        cursor.execute(sql, val)
        db.commit()
    print("{} data telah dihapus".format(banyak))
    back_to_menu_data_hewan()

def search_data_hewan(db):
    clear_screen()
    cursor = db.cursor()
    print("\nMasukan Kata Kunci berupa ID Hewan/Nama Hewan/Jenis Hewan")
    keyword = input("Kata Kunci: ")
    sql = "SELECT * FROM hewan WHERE id_hewan = %s or nama_hewan = %s or jenis_hewan = %s"
    val = (keyword, keyword, keyword)
    cursor.execute(sql, val)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("ID Hewan            : ", data[0])
            print("Nama Hewan          : ", data[1])
            print("Jenis Hewan         : ", data[2])
            print("Jenis Kelamin       : ", data[3])
            print("Usia Hewan          : ", data[4])
            print("Berat Hewan         : ", data[5])
            print("==========================================")
    back_to_menu_data_hewan()

#===========================================================================================================================
def kandang(db):
    clear_screen()
    cursor = db.cursor()
    sql = "SELECT * FROM kandang"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        print("==========================================")
        for data in results:
            print("No Kandang          : ", data[0])
            print("Nama Hewan          : ", data[1])
            print("Jenis Hewan         : ", data[2])
            print("Jenis Penggunaan    : ", data[3])
            print("Lama Penggunaan     : ", data[4])
            print("Tanggal Masuk       : ", data[5])
            print("==========================================")
    print()
    back_to_menu_utama()

#===========================================================================================================================
def back_to_menu_utama():
    print("\n")
    input("Tekan Enter Untuk Kembali Ke Menu Utama")
    main_menu(db)

def main_menu(db):
    clear_screen()
    print("\t\t\t               ==========================")
    print("\t\t\t=============== Aplikasi Asteri Pet Shop ===============")
    print("\t\t\t               ==========================")
    print("\t\t\t[1] Transaksi")
    print("\t\t\t[2] Data Transaksi Asteri Pet Shop")
    print("\t\t\t[3] Data Pelanggan")
    print("\t\t\t[4] Data Hewan")
    print("\t\t\t[5] Data Kandang")
    print("\t\t\t[6] Keluar")
    print("\t\t\t--------------------------------------------------------")
    pilih = int(input("\t\t\tPilihan anda > "))
    if pilih == 1:
        transaksi(db)
    elif pilih == 2:
        all_data_transaksi_petshop(db)
    elif pilih == 3:
        data_pelanggan(db)
    elif pilih == 4:
        data_hewan(db)
    elif pilih == 5:
        kandang(db)
    elif pilih == 6:
        exit()
    else:
        print("Pilihan Anda Salah!")

if __name__ == "__main__":
    while True:
        main_menu(db)