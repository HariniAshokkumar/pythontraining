import psycopg2
import jsonpickle

conn=psycopg2.connect(database="dvdrental",user="postgres",password="admin",host="127.0.0.1",port=5432)

cur=conn.cursor()
cur.execute("select * from actor")
rows=cur.fetchall() #result is a list of tuples
# frozen=jsonpickle.encode(rows)
# print (frozen)
# print (rows)
for row in rows:
	print ("ID: ",row[0]," Name: ",row[1],row[2])
print("No. of rows fetched: ",cur.rowcount)
conn.commit()
conn.close()
