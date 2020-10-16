from nba_api.stats.endpoints import LeagueGameFinder
import pandas as pd
import sqlite3
import time
import csv

teamid = '1610612745'
##boxscore = BoxScoreMatchups(
 ##   game_id ="21900558"
#)

#df=boxscore.get_data_frames()


#print(df)


gameid = 21700807
def get_box_score(game):

    boxscore = LeagueGameFinder(
        player_or_team_abbreviation='T'
    )



    box = boxscore.get_data_frames()
    print(box)

get_box_score(gameid)