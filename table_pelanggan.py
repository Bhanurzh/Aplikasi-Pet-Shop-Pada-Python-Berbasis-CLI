import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="petshop"
)

cursor = db.cursor()
sql = """CREATE TABLE pelanggan (
    id_pelanggan INT AUTO_INCREMENT PRIMARY KEY,
    nama varchar(255),
    alamat varchar(255),
    no_tlp varchar(12)
)
"""
cursor.execute(sql)
print("Tabel pelanggan berhasil dibuat!")