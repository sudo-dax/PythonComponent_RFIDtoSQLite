import sqlite3, csv, sys

db_filename = "BathTowel-tags.db"
data_filename = "26715-Moya-x5.csv"

SQL = """
insert into tags (Status, ID, TimeStamp, Reader, Link, Antenna, EPC, TID, RSSI, Count)
values (:Status, :ID, :TimeStamp, :Reader, :Link, :Antenna, :EPC, :TID, :RSSI, :Count)
"""

con = sqlite3.connect(db_filename)
c = con.cursor()


def create_table():
    c.execute('DROP TABLE IF EXISTS tags')
    c.execute("""CREATE TABLE IF NOT EXISTS tags(
        'Status' TEXT,
        'ID' TEXT,
        'TimeStamp' TEXT,
        'Reader' TEXT,
        'Link' TEXT,
        'Antenna' TEXT,
        'EPC' TEXT,
        'TID' TEXT,
        'RSSI' TEXT, 
        'Count' TEXT
        )""")

create_table()



with open('/home/x/Documents/Coding/Python/sqlitedb/RFID-CSVtoSQLite/26715-Moya-x5.csv', 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)
