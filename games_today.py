from nba_api.stats.endpoints import teamgamelog
# Basic Request
##player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)



custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Only available after v1.1.0
# Proxy Support, Custom Headers Support, Timeout Support (in seconds)
##print(player_info.available_seasons.get_data_frame())

from nba_api.stats.endpoints import Scoreboard
from nba_api.stats.library.parameters import LeagueID
from nba_api.stats.library.data import teams
import datetime

#List the games of the day
date = datetime.datetime.now()

teams = dict((team[0],team[5]) for team in teams)

gamefinder = Scoreboard(league_id=LeagueID.nba,
                            day_offset=0,
                            game_date=date)

games_dict = gamefinder.get_normalized_dict()

for game in games_dict['GameHeader']:
    print(f"\t{teams[game['VISITOR_TEAM_ID']]} @ {teams[game['HOME_TEAM_ID']]} - ({game['GAME_STATUS_TEXT']})")