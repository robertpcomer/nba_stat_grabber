from nba_api.stats.endpoints import TeamGameLog
import pandas as pd
import sqlite3
import time
import csv

teamid = '1610612745'

def get_team_season_history(teamid,season_type,season_years):

    teamstats = TeamGameLog(
        team_id=teamid,
        season=season_years,
        ##league_id_nullable =='00',
        ##per_mode_simple='PerGame',
        season_type_all_star=season_type
    )



    roster = teamstats.get_data_frames()
    ##print(type(roster[0]))
    roster[0].to_csv('box_score_csv.csv',header=False)

##get_team_season_history(teamid)




conn = sqlite3.connect("NbaStats.db")
curs = conn.cursor()
#getting all team ids
curs.execute("SELECT team_id FROM teams;")
all_teamids = curs.fetchall()


def insert_loop(season_type,season_years):
    conn = sqlite3.connect("NbaStats.db")
    curs = conn.cursor()
    #getting all team ids
    curs.execute("SELECT team_id FROM teams;")
    all_teamids = curs.fetchall()

    
    for id in all_teamids:
        ##Call the get_all_players function passing the teamid
        get_team_season_history(id,season_type,season_years)
        time.sleep(5)
        reader = csv.reader(open('box_score_csv.csv','r'), delimiter=',')
        for row in reader:
            dates= row[3].split(",")
            to_db =[row[0],row[1],row[2],dates[0],dates[1],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27]]
            
            #print(to_db)
            
            curs.execute("INSERT OR IGNORE INTO games(count, team_ID, game_ID, Game_date, Game_Year, Matchup, WL,W_total, L_total, W_pct, Minutes, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
            conn.commit()
        time.sleep(3)
type_season = "Playoffs"
years = "2016-17"
insert_loop(type_season,years)

