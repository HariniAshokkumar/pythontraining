from flask import Flask,request
import json
app = Flask(__name__)

@app.route('/user/',methods=["POST"]) #restricting the method to only POST method
def hello_user(): #GET variables can be mentioned inside the brackets
	print (request.form)
	user=request.form["username"]
	converted_data=json.loads(request.form["data"])
	command=converted_data["command"]
	if (user=="harini"):
		return 'your command is %s!' % command
	else:
		return 'Unauthorized user!'

if __name__ == '__main__':
	app.run("localhost",3333)

#ImmutableMultiDict is aka dictionary