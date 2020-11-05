import sqlite3

if __name__ == '__main__':
    con = sqlite3.connect('Weather.db')
    c = con.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS "Weather" (
        "Id" INTEGER PRIMARY KEY,
        "Loc" TEXT,
        "RainChance" INTEGER,
        "Date" DATE,
        "Humitiy" INTEGER,
        "UV" INTEGER,
        "Temp"	INTEGER,
        "Wind" INTEGER
        )""")
    con.commit()
    con.close()

else:
    #function to return data for outputting to html
    def OutPut(Day=0):
        con = sqlite3.connect("Weather.db")
        c = con.cursor()
        c.execute("""SELECT Loc, RainChance, Date, Temp, Wind 
        FROM Weather 
        ORDER BY Date DESC""")
        Data = c.fetchall()[0:Day]
        return Data