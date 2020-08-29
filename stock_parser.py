
import util.database as db

if __name__ == "__main__":
	print "stock parser"
	json_data = db.update_database()
	print json_data
	with open("20200828.json", "w") as f:
		json.dump(json_data, f)
