import bs4
import urllib.request
from bs4 import BeautifulSoup
import csv, sqlite3,unicodedata, os.path
import calendar
import pandas as pd
import unidecode
import mysql.connector
import datetime

base = "https://www.basketball-reference.com/boxscores/"

mydb = mysql.connector.connect(
host="localhost",
user="robert",
password=""password_here""
)

curs = mydb.cursor()
curs.execute("SELECT team_id, game_id, Game_date, Matchup FROM nba_stats.games;")
#print(curs.fetchall())
all_urls = []
hometeamids = []
gameids= []
hometeams= []
awayteams=[]

for row in curs.fetchall():
    
    #print(row[2])
    #date_string = dt.strftime('%m/%d/%Y')
    date= row[2]
    date = date.strftime("%Y-%m-%d")
    print(date)
    date= date.split("-")
    #print(date.text)
    year=date[0]
    hometeamids.append(row[0]) 
    gameids.append(row[1])
 
 
    month=date[1]

    if (len(month) == 1):
        month = "0" + month

    #print(month) 
    day= date[2]

    #day=day.replace(",","")

    ##always needs to be the home team 
    ##Oct 31 Atl vs miami - Atlanta was the home team 
    ## So if "vs" use the first one 
    ##Oct 30  NYK @ Orl -  Orlando was the home team 
    ## So if "@" use the second one
    #print(row[3])
    teams = row[3].split(" ")
    #print(teams)
    
    if(teams[1]== "vs."):
        home_team= teams[0]
        away_team =teams[2] 

    if(teams[1]== "@"):
        home_team =teams[2]
        away_team =teams[0] 
    
    
    hometeams.append(home_team)
    awayteams.append(away_team)
    final_url= base + year +month + day + "0" + home_team + ".html"

    all_urls.append(final_url)

print(all_urls, gameids,hometeams,awayteams)
