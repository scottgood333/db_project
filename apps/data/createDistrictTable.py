
import psycopg2
from tool2 import area_data

# connect to  database
connection = psycopg2.connect(database="health_insurance_hospitals",
                              user="postgres",
                              password="wu8313497",
                              host="localhost",
                              port="5432")
connection.autocommit = True

cursor = connection.cursor()

for city, districts in area_data.items():
    print(city, districts)
    for district in districts:
        cursor.execute(
            f'INSERT INTO district VALUES(\'{city}\',\'{district}\')'
        )
