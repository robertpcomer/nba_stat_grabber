import csv, sqlite3,unicodedata, os.path

conn = sqlite3.connect("NbaStats.db")
curs = conn.cursor()
curs.execute("SELECT team_id FROM teams;")
print(curs.fetchall())
#curs.execute("CREATE TABLE teams (count INTEGER, team_id INTEGER PRIMARY KEY, full_name TEXT, abbreviation TEXT, nickname TEXT, city TEXT, State TEXT, year_founded INTEGER);")
#reader = csv.reader(open('teamid_csv.csv','r'), delimiter=',')
#for row in reader:
 #   to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
 #   curs.execute("INSERT INTO teams(count, team_id, full_name, abbreviation, nickname, city, state, year_founded) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
#conn.commit()