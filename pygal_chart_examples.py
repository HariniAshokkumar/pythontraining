import pygal

def create_barchart(data):
	bar_chart=pygal.Bar()
	for x in data["data"]:
		bar_chart.add(x["name"],x["values"])
	bar_chart.render_to_file('charts\pygal_chart_function_bar.svg')

def create_piechart(data):
	pie_chart=pygal.Pie()
	for x in data["data"]:
		print (x)
		pie_chart.add(x["browser"],x["usage"])
	pie_chart.render_to_file('charts\pygal_chart_function_pie.svg')

#data should be of the below format for this example program
# data1={"chart_type":"barchart",
# 	   "data":[{
# 	   		"name":"Fibonacci",
# 	   		"values":[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 	   },{
# 	   		"name":"Natural numbers",
# 	   		"values":[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# 	   }
# 	   ]}

data1={"chart_type":"barchart","data":[{"name":"Fibonacci","values":[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]},{"name":"Natural numbers","values":[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}]}
data2={"chart_type":"Pie","data":[{"name":"Browser","values":["IE","FF","Chrome","Safari","Opera"]},{"name":"usage","values":[19.5,36.6,36.3,4.5,2.3]}]}
data2={"chart_type":"Pie","data":[{"browser":"IE","usage":[19.5]},{"browser":"FF","usage":[36.6]},{"browser":"Chrome","usage":[36.3]}]}
create_barchart(data1)
create_piechart(data2)