import sqlite3

database = "database.sqlite"

conn = sqlite3.connect(database)

print("database connected successfully")

import pandas as pd
tables = pd.read_sql('''
select * from sqlite_master where type = "table";
''', conn)
print(tables)

country = pd.read_sql('''
select * from Country;
''', conn)

city = pd.read_sql('''
select * from City;
''', conn)
print(country)
print(city)

Pakistan_cities = pd.read_sql('''
select city_id, country_id from City
where country_id = (select country_id from city where country_id == 6);
''', conn)
print(Pakistan_cities)