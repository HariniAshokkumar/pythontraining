import psycopg2
import jsonpickle
from datetime import datetime

conn=psycopg2.connect(database="dvdrental",user="postgres",password="admin",host="127.0.0.1",port=5432)

cur=conn.cursor()
cur.execute("select * from actor")
rows=cur.fetchall() #result is a list of tuples
dt=datetime.now()
#inserting one row and using the above date value instead of postgre now() function
cur.execute('insert into public.actor (first_name,last_name,last_update) values (%s,%s,%s)',("Tom","Noideawhat",dt,))
for x in range(1000): #inserting 1000 rows
	cur.execute('insert into public.actor (first_name,last_name,last_update) values (%s,%s,%s)',("Tom","Noideawhat","now()",))
conn.commit() #obligatory
conn.close() #obligatory
