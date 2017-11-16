from flask import Flask,request
app = Flask(__name__)

@app.route('/user/<username>',methods=["POST"]) #restricting the method to only POST method
def hello_user(username):
	print (request.form)
	if (request.form["username"]=="harini"):
		return 'Hello, %s! You are an authorized user' % username
	else:
		return 'Unauthorized user!'

if __name__ == '__main__':
	app.run("localhost",3333)

#ImmutableMultiDict is aka dictionary