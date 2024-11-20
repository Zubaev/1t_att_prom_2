from psycopg2 import connect
conn = connect(host='zubaev', port=5432, user='zms', password='123456', dbname='test_db')
conn.autocommit = True

with conn: 
    with conn.cursor() as curs:
     curs.execute('''select age 
                      from test_table
                      where (age = (select MAX(age) from test_table 
                      where LENGTH(name) < 6) OR
                      age = (select MIN(age) from test_table 
                      where LENGTH(name) < 6)) and LENGTH(name) < 6 group by age order by age asc;
                  ''')
     row = curs.fetchall()

print(f'Минимальный возраст: {row[0][0]}')
print(f'Максимальный возраст: {row[1][0]}')

curs.close()
conn.close()