from flask import Flask, request
import json
import math
import datetime
import calendar
import MySQLdb # pip install MySQL-python

USERNAME = "communalert"
PASSWORD = "communalert"

app = Flask(__name__)
#app.debug = True

def dist(x1,y1,x2,y2):
	R = 3958.76
	return R*math.acos(math.sin(y1)*math.sin(y2) + math.cos(y1)*math.cos(y2)*math.cos(x2-x1))

def dpa(x,latitude,longitude):
	k1 = 1
	k2 = 1
	time = datetime.datetime.now() - (x[4]) #timedelta
	time = time.total_seconds()
	severity = 1
	distance = dist(x[2],x[3],latitude,longitude)
	return (-1)*(k1*math.exp((-1)*k2*time)*(severity/(distance**2)))

@app.route("/")
def root():
	return "CommunAlert API"

@app.route("/GET", methods=['GET'])
def get():
	latitude = float(request.args['latitude'])
	longitude = float(request.args['longitude'])
	# make sql request
	db = MySQLdb.connect("localhost", USERNAME , PASSWORD , "communalert");
	cursor = db.cursor()
	cursor.execute("SELECT * FROM reports WHERE report_time > NOW() - INTERVAL 60 MINUTE;")
	data = cursor.fetchall()
	data = list(data)
	# sort with lambda = DPA
	data = sorted(data,key=lambda x:dpa(x,latitude,longitude))
	# send back json of most relevant
	# return json.dumps("stuff")
	db.close()
	newdata = []
	for i in data:
		timestamp = calendar.timegm(i[4].utctimetuple())
		j = (i[0],i[1],i[2],i[3],timestamp,i[5])
		newdata.append(j)
	return json.dumps(newdata)

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

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=3500)
