import pygal
from flask import Flask,request,render_template
import psycopg2
import json
import jsonpickle
app = Flask(__name__)


@app.route('/api/<month>',methods=["GET"]) #restricting the method to only POST method
def create_chart(month="all"):
	conn=psycopg2.connect(database="dvdrental",user="postgres",password="admin",host="127.0.0.1",port=5432)
	cur=conn.cursor()
	cur.execute("select * from sales2 order by product asc")
	rows=cur.fetchall()
	dict_a={}
	list_rows=[]
	for row in rows:
		list_rows.append({"product":row[0],"sales":row[2]})
	data=json.dumps(list_rows)
	conn.close()
	return render_template('index.html',chart=create_barchart(data))

def create_barchart(data):
	bar_chart=pygal.Bar()
	data2=json.loads(data)
	for x in data2:
		# print (x)
		bar_chart.add(x["product"],x["sales"])
	return bar_chart.render_data_uri()

if __name__ == '__main__':
	app.run("localhost",3333)

