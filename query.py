import sqlite3

conn = sqlite3.connect("factbook.db")

c = conn.cursor()

c.execute("select name from facts order by population_growth asc limit 10")

print(c.fetchall())
