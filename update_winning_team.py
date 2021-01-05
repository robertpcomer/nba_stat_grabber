import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="robert",
  password=""password_here""
)

teamcursor = mydb.cursor()
teamcursor.execute("Select * from nba_stats.teams")
table_rows = teamcursor.fetchall()
df = pd.DataFrame(table_rows)
print(df) 
#print(df[df[0]=='POR'])


msqlcursor = mydb.cursor()

msqlcursor.execute("SELECT * FROM nba_stats.games;")


#print(query)

for row in msqlcursor.fetchall():
    updatecursor = mydb.cursor()
    #print("Regular teams id")
    #print(row[1])
    #print("Matchup")
    #print(row[5])
    #print("W/L after this")
    #print(row[6])
    
    #print("Should be the other team id")
  
 


    Determiner = row[5].split(" ")
    if row[6] == 'L':
      other_team = (df[df[2]==Determiner[2]])
      other_teamid = other_team[0].values
      other_teamid=(str(other_teamid).lstrip('[').rstrip(']'))
      LosingTeamId = row[1]
      LosingTeamAbbr = Determiner[0]
      WinningTeamAbbr = Determiner[2]
      WinningTeamId = other_teamid
      print( LosingTeamAbbr + ", " + str(LosingTeamId) + ", " + WinningTeamAbbr + ", " + str(WinningTeamId))
    if row[6] == 'W':
      other_team = (df[df[2]==Determiner[2]])
      #print("This is the df id other team we're looking for")
      print(other_team)
      other_teamid = other_team[0].values
    
      other_teamid=(str(other_teamid).lstrip('[').rstrip(']'))
      LosingTeamId = other_teamid
      LosingTeamAbbr = Determiner[2]
      WinningTeamAbbr = Determiner[0]
      WinningTeamId = row[1]
    
      print( LosingTeamAbbr + ", " + str(LosingTeamId) + ", " + WinningTeamAbbr + ", " + str(WinningTeamId))
    update_statement = "Update nba_stats.games SET winning_teamID =" + str(WinningTeamId) + ", winning_teamABR = '" + WinningTeamAbbr + "', losing_teamID =" + str(LosingTeamId) + ", losing_teamABR = '" +LosingTeamAbbr + "' WHERE game_ID =" + str(row[2]) + ";"
    print(update_statement)
    updatecursor.execute(update_statement)
    mydb.commit()
	


##Determiner = Matchup.Split(" ")    
## If W/L == W

    ##LosingTeamId = yadda Yadda
    ##LosingTeamAbbr = Determiner[2]
    ##WinningTeamAbbr = Determiner[0]
    ##WinningTeamId = team_id


    gameid = str(row[2])
  # msqlcursor2.execute("Select * FROM nba_stats.games where game_id = " + gameid + ";")
    #query = msqlcursor2.fetchall()
    #print(query)
