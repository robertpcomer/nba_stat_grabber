
from nba_api.stats.endpoints import TeamGameLog
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import CommonTeamRoster
import sqlite3
import csv
import time



##opening connection to SQL 
conn = sqlite3.connect("NbaStats.db")
curs = conn.cursor()
##getting all team ids
curs.execute("SELECT team_id FROM teams;")
all_teamids = curs.fetchall()

##Loop through each teamid
for id in all_teamids:
    ##Call the get_all_players function passing the teamid
    get_all_players(id)
    time.sleep(10)
    reader = csv.reader(open('roster_csv.csv','r'), delimiter=',')
    for row in reader:
        to_db =[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]]
        curs.execute("INSERT INTO players(count, team_ID,SEASON,LeagueID,PLAYER,PLAYER_SLUG,NUM,POSITION,HEIGHT,WEIGHT,BIRTH_DATE,AGE,EXP,SCHOOL,PLAYER_ID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
        
    time.sleep(10)



def get_team_season_history():

    teamstats = TeamGameLog(
        team_id=' 1610612745',
        season='2019-20',
        ##league_id_nullable =='00',
        ##per_mode_simple='PerGame',
        season_type_all_star='Regular Season'
    )



    teams_dict = teamstats.get_data_frames()

    print(teams_dict)

def get_all_players(teamID):


    teamRoster = CommonTeamRoster(
        team_id= teamID,
        season='2019-20',
    )
    roster = teamRoster.get_data_frames()
    ##print(roster[0])
    roster[0].to_csv('roster_csv.csv',header=False)
    
    
    
    


##get_all_players(team)


   
def create_table():
    curs.execute("CREATE TABLE players (count INTEGER, team_ID INTEGER,SEASON INTEGER,LeagueID INTEGER ,PLAYER TEXT,PLAYER_SLUG TEXT,NUM INTEGER,POSITION TEXT,HEIGHT TEXT,WEIGHT TEXT,BIRTH_DATE TEXT,AGE INTEGER,EXP INTEGER,SCHOOL TEXT,PLAYER_ID INTEGER PRIMARY KEY);")
    conn.commit()

conn.commit()
#get_all_players(team)





#reader = csv.reader(open('teamid_csv.csv','r'), delimiter=',')
#for row in reader:
 #   to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
 #   curs.execute("INSERT INTO teams(count, team_id, full_name, abbreviation, nickname, city, state, year_founded) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
#conn.commit()


##upload_data_frame_to_csv(roster)