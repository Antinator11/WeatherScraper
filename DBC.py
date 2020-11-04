import sqlite3

con = sqlite3.connect()
c = con.cursor()

con.close()