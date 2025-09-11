## Exercises 1-4:
import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE Roster (Name TEXT, Species TEXT, Age INT)''')
values = [('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)]
c.executemany('INSERT INTO Roster VALUES (?,?,?)', values)
c.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
c.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
print(c.fetchall())
conn.commit()
conn.close()
