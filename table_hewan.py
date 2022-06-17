import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="petshop"
)

cursor = db.cursor()
sql = """CREATE TABLE hewan (
    id_hewan INT AUTO_INCREMENT PRIMARY KEY,
    nama_hewan varchar(255),
    jenis_hewan varchar(255),
    jenis_kelamin varchar(1),
    usia_hewan varchar(255),
    berat_hewan varchar(30)
)
"""
cursor.execute(sql)
print("Tabel hewan berhasil dibuat!")