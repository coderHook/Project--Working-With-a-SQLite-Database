import pandas as pd
import sqlite3, math

conn = sqlite3.connect("factbook.db")

df = pd.read_sql_query("select * from facts;", conn)
# This drops any row that has a Nan value.
df = df.dropna(axis=0, how='any')

def predict_2015(row):
    
    final_population = row['population']*(math.e**((row['population_growth']/100)*35))
    return round(final_population, 0)

df['2050_population'] = df.apply(predict_2015, axis=1)

print(df.columns)
