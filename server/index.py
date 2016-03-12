from flask import Flask, request
import json
import MySQLdb # pip install MySQL-python

USERNAME = "communalert"
PASSWORD = "communalert"

app = Flask(__name__)
app.debug = True

@app.route("/")
def root():
	return "xD"

@app.route("/GET", methods=['GET'])
def get():
	latitude = float(request.args['latitude'])
	longitude = float(request.args['longitude'])
	# make sql request
	db = MySQLdb.connect("localhost", USERNAME , PASSWORD , "communalert");
	cursor = db.cursor()
	cursor.execute("SELECT * FROM reports WHERE report_time > NOW() - INTERVAL 60 MINUTE;")
	data = cursor.fetchone()
	# sort with lambda = DPA
	# send back json of most relevant
	# return json.dumps("stuff")
	db.close()
	return str(data)

@app.route("/POST",methods=['POST'])
def post():
	latitude = float(request.form['latitude'])
	longitude = float(request.form['longitude'])
	userid = float(request.form['user_id'])
	reporttype = request.form['type']
	db = MySQLdb.connect("localhost", USERNAME , PASSWORD , "communalert");
	cursor = db.cursor()
	cursor.execute("INSERT INTO reports (user_id,latitude,longitude,report_type) VALUES (" + str(userid) + "," + str(latitude) + "," + str(longitude) + ",\"" + reporttype + "\");")
	db.commit()
	db.close()
	return "success"
	# sql insert into

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=3500)
