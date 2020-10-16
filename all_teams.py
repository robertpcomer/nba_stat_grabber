from nba_api.stats.static import teams
import csv
import pandas as pd

all_teams =teams.get_teams()
##print(all_teams[0])

df = pd.DataFrame(all_teams)
print(df)

df.to_csv('teamid_csv.csv',index =True)