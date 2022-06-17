import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="petshop"
)

cursor = db.cursor()
sql = """CREATE TABLE transaksi (
    id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
    nama_pelanggan varchar(40),
    kode_transaksi int,
    jenis_transaksi varchar(30),
    tanggal timestamp,
    total_tagihan int(18),
    status_tagihan varchar(30)
)
"""
cursor.execute(sql)
print("Tabel transaksi berhasil dibuat!")