import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="robert",
  password=""password_here""
)

msqlcursor = mydb.cursor()
#msqlcursor.
msqlcursor.execute("SELECT * FROM nba_stats.games;")
query = msqlcursor.fetchall()
print(query)
