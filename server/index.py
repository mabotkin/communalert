from flask import Flask
import json
import MySQLdb # pip install MySQL-python

app = Flask(__name__)

@app.route("/GET", methods=['GET'])
def get():
	latitude = float(request.args['latitude'])
	longitude = float(request.args['longitude'])
	# make sql request
	# sort with lambda = DPA
	# send back json of most relevant
	# return json.dumps("stuff")

@app.route("/POST",methods=['POST']
def post():
	latitude = float(request.form['latitude'])
	longitude = float(request.form['longitude'])
	userid = float(request.form['user_id'])
	reporttype = request.form(['type'])
	# sql insert into

if __name__ == "__main__":
	app.run()
