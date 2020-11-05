import sqlite3

if __name__ == '__main__':
    con = sqlite3.connect('Weather.db')
    c = con.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS "Weather" (
        "Id" INTEGER PRIMARY KEY,
        "Loc" TEXT,
        "Rain" INTEGER,
        "RainChance" INTEGER,
        "Clounds" INTEGER,
        "Date" DATE,
        "SunRise" TIME,
        "SunSet" TIME,
        "Temp"	INTEGER,
        "Wind" INTEGER
        )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS "Clouds" (
        "Id" INTEGER PRIMARY KEY,
        "Message" TEXT
        )""")

    con.commit()
    con.close()