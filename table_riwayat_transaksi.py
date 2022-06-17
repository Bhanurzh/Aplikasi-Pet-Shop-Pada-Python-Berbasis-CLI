import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="petshop"
)

cursor = db.cursor()
sql = """CREATE TABLE riwayat_transaksi (
    id_riwayat_transaksi INT AUTO_INCREMENT PRIMARY KEY,
    nama_pelanggan varchar(40),
    jenis_transaksi varchar(30),
    total_tagihan int(18),
    status_tagihan varchar(30),
    tanggal timestamp
)
"""
cursor.execute(sql)
print("Tabel riwayat_transaksi berhasil dibuat!")