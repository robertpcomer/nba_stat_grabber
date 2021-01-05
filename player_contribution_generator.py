##We're going to create a new table based off of the following program
##We're going to go through every players boxscores and calculate their 36min expected outcome
##We're going to look at their last 10-15 games and determine if the individual is exceeding their expected outcome
##We're going to calculate a players PER and maybe even alter it a bit :)

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="robert",
  password=""password_here""
)


##Ask user for the date range to create

#start_date = input("Enter the start date: ") 
#end_date = input("Enter the end date: ") 
start_date = '2019-10-25'
end_date = '2020-10-11'

print(start_date)
print(end_date)

cursor = mydb.cursor()
cursor.execute("Select game_id, game_date, winning_teamABR, winning_teamID, losing_teamABR, losing_teamID from nba_stats.games where Game_date between '"+start_date + "' and '" +end_date + "';")
table_rows = cursor.fetchall()
df = pd.DataFrame(table_rows)

df.rename(columns={0: "Game_id", 1: "game_date", 2: "winning_teamABR", 3: "winning_teamID", 4: "losing_teamABR", 5 : "losing_teamID"},  inplace=True)

print(df) 

cursor.execute("Select * from nba_stats.players;")
player_table = cursor.fetchall()
#print(player_table)
cursor.execute("Select * from nba_stats.entire_boxscore;" )
table_rows = cursor.fetchall()
player_stats_df = pd.DataFrame(table_rows)
#df.rename(columns={0: "Game_id", 1: "game_date", 2: "winning_teamABR", 3: "winning_teamID", 4: "losing_teamABR", 5 : "losing_teamID"},  inplace=True)
#print(player_stats_df)


for player in player_table:
    print(player[0])
    playerName= player[0]
    box_scores =  (player_stats_df[player_stats_df[4]==playerName])
    print(box_scores)






##For each player in player.fetchall():
	##playerName is = player[0]
    ##
    