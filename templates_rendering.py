import pygal
from flask import Flask,request,render_template
app = Flask(__name__)

data1={"chart_type":"Bar","data":[{"name":"Fibonacci","values":[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]},{"name":"Natural numbers","values":[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}]}
data2={"chart_type":"Pie","data":[{"browser":"IE","usage":[19.5]},{"browser":"FF","usage":[36.6]},{"browser":"Chrome","usage":[36.3]},{"browser":"Safari","usage":[4.5]},{"browser":"Opera","usage":[2.3]}]}

@app.route('/api/<charttype>',methods=["GET"])
def create_chart(charttype):
	return render_template('index.html',chart=create_barchart(data1))

def create_barchart(data):
	bar_chart=pygal.Bar()
	for x in data["data"]:
		bar_chart.add(x["name"],x["values"])
	return bar_chart.render_data_uri()

# def create_piechart(data):
# 	pie_chart=pygal.Pie()
# 	for x in data["data"]:
# 		pie_chart.add(x["browser"],x["usage"])
# 	pie_chart.render_to_file('charts\pygal_chart_function_pie.svg')
# 	return "Pie chart generated"

# create_piechart(data2)

if __name__ == '__main__':
	app.run("localhost",3333)