import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="petshop"
)

cursor = db.cursor()
sql = """CREATE TABLE kandang (
    no_kandang INT AUTO_INCREMENT PRIMARY KEY,
    nama_hewan varchar(255),
    jenis_hewan varchar(255),
    jenis_penggunaan varchar(30),
    lama_penggunaan varchar(30),
    tanggal_masuk timestamp
)
"""
cursor.execute(sql)
print("Tabel kandang berhasil dibuat!")