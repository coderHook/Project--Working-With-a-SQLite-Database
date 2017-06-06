import sqlite3

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()

q_area_land = "select sum(area_land) from facts where area_land != '';"
res_land = cursor.execute(q_area_land).fetchone()

q_area_water = "select sum(area_water) from facts where area_water != '';"
res_water = cursor.execute(q_area_water).fetchone()

result = res_land[0] / res_water[0]

print(result)

