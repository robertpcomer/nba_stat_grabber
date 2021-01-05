import bs4
import urllib.request
from bs4 import BeautifulSoup
import csv, sqlite3,unicodedata, os.path
import calendar
import pandas as pd
import unidecode
import mysql.connector
away_team = "Washington Wizards"
##home_team = "San Antonio Spurs"

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


def clean_insert_boxscore(soup,testhomeid,testawayid,testgameid):
##print(soup)
    print(soup)
  
    stats = urllib.request.urlopen(soup)
    this_soup = BeautifulSoup(stats, "html")
    count = 0
    team = "N/A"
    lazy_add =0
    for table in this_soup.find_all('table', {'class': 'sortable stats_table'}):
    
        mydb = mysql.connector.connect(
        host="localhost",
        user="robert",
        password=""password_here""
        )
        msqlcursor = mydb.cursor()
        #print(table)
        with open('boxscore.csv', 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

            print(team)
            #print(type(table))
            #print("Yes")  
            id = table.contents[0]
            #print("Table Name")
            #print(id.text)
            tr =table.find_all('tr')
            #print(str(count))
            if 1 <= count <= 6:
                team = away_team
            print("This is the count")
            print(count)
            advanced_check =table['id']
            firstq_check = table['id']
            print(id.text)
            print(advanced_check)
            print(testhomeid)
            print(testawayid)
            #quarter_half_insert = []
            quarter = 0
            half = 0
            overtime = 0

            if((advanced_check).find("advanced") != -1):
                print("This is advanced")
                if(count==7):
                    print("This is advanced for away")                   
                    box_type= 'Advanced'
                    box_typeid = 'abox_id'
                    #print(table)
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = ''
                    home_away = 'away'
                if(count==15):
                    print("This is advacned for home")
                
                    box_type= 'Advanced'
                    box_typeid = 'abox_id'
                    
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = ''
                    home_away = 'home'
            print("values are here")
            print(testawayid)
            
            print(id.text)
            if(count ==1):
                print("This is the id text we're looking for")
                print(firstq_check)
            if ((firstq_check).find("q1") != -1):
                
                if(count==1):
                    print("This is the away team Q1")
                    ##Away Team
                    box_type= 'Quarter'
                    box_typeid = 'qbox_id'
                    quarter = '1'
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'quarter,'
                    home_away = 'away'
                    print("we made it into the loop")
         
                if(count==9):
                    print("This is the home team Q1")
                    box_type= 'Quarter'
                    box_typeid = 'qbox_id'
                    quarter = '1'
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'quarter,'
                    home_away = 'home'

            if ((firstq_check).find("q2") != -1):
                print("This is the second quarter")
                if(count==2):
                    print("THIS IS AWAY q2")
           
                    box_type= 'Quarter'
                    box_typeid = 'qbox_id'
                    quarter = '2'
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'quarter,'
                    home_away = 'away'
                if(count==10):
                ##Away Team
                    box_type= 'Quarter'
                    box_typeid = 'qbox_id'
                    quarter = '2'
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'quarter,'
                    home_away = 'home'
            if ((firstq_check).find("h1") != -1):
                print("This is the first half ") 
                if(count==3):
                ##Away Team
                    box_type= 'Half'
                    box_typeid = 'hbox_id'
                    half = '1'
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'half,'
                    home_away = 'away'

                if(count==11):
                ##Away Team
                    box_type= 'Half'
                    box_typeid = 'hbox_id'
                    half = '1'
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'half,'  
                    home_away = 'home' 

            if ((firstq_check).find("q3") != -1):
                print("This is the third quarter") 
                if(count==4):
                ##Away Team
                    box_type= 'Quarter'
                    box_typeid = 'qbox_id'
                    quarter = '3'
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'quarter,' 
                    home_away = 'away'         
                if(count==12):
                ##Away Team
                    box_type= 'Quarter'
                    box_typeid = 'qbox_id'
                    quarter = '3'
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'quarter,' 
                    home_away = 'home'

            if ((firstq_check).find("q4") != -1):
                print("This is the fourth quarter")  
                if(count==5):
                    print("this should be the away 4th q")       
                ##Away Team
                    box_type= 'Quarter'
                    box_typeid = 'qbox_id'
                    quarter = '4'
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'quarter,'
                    home_away = 'away'
                if(count==13):
                    ##Away Team
                    box_type= 'Quarter'
                    box_typeid = 'qbox_id'
                    quarter = '4'
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'quarter,'
                    home_away = 'home'
      
            if ((firstq_check).find("h2") != -1):
                print("This is the second half ")    
                if(count==6):
                ##Away Team
                    box_type= 'Half'
                    box_typeid = 'hbox_id'
                    half = '2'
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'half,'
                    home_away = 'away'        
                if(count==14):
                ##Away Team
                    box_type= 'Half'
                    box_typeid = 'hbox_id'
                    half = '2'
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'half,'
                    home_away = 'home'

            if ((firstq_check).find("ot1") != -1):
                print("This is overtime")
                if(count==7):
                    print("this should be the away overtime")
                    box_type= 'Overtime'
                    box_typeid = 'obox_id'             
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'overtime, '
                    home_away = 'away'
                    overtime = '1'
                if(count==15):
                    print("this should be the home overtime")
                    box_type= 'Overtime'
                    box_typeid = 'obox_id'             
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'overtime, '
                    home_away = 'home'
                    overtime = '1'
                count= count - 1
            if ((firstq_check).find("ot2") != -1):
                print("This is second overtime")
                
                if(count==7):
                    #print("this should be the away overtime")
                    box_type= 'Overtime'
                    box_typeid = 'obox_id'             
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'overtime, '
                    home_away = 'away'
                    overtime = '2'
                    print(overtime)
                if(count==15):
                    #print("this should be the home overtime")
                    box_type= 'Overtime'
                    box_typeid = 'obox_id'             
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'overtime, '
                    home_away = 'home'
                    overtime = '2'  
                count= count -1
         
            if ((firstq_check).find("ot3") != -1):
                #print("This is third overtime")
               
                
                if(count==7):
                    #print("this should be the away overtime")
                    #count= count -1
                    box_type= 'Overtime'
                    box_typeid = 'obox_id'             
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'overtime, '
                    home_away = 'away'
                    overtime = '3'
                if(count==15):
                    #print("this should be the home overtime")
                    box_type= 'Overtime'
                    box_typeid = 'obox_id'             
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'overtime, '
                    home_away = 'home'
                    overtime = '3'
                print(overtime)
                count= count -1
            print(id.text)
            if ((firstq_check).find("ot4") != -1):
                #print("This is third overtime")
                
                print(count)
                if(count==7):
                    #print("this should be the away overtime")
                    box_type= 'Overtime'
                    box_typeid = 'obox_id'             
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = 'overtime, '
                    home_away = 'away'
                    overtime = '4'
                if(count==15):
                    #print("this should be the home overtime")
                    box_type= 'Overtime'
                    box_typeid = 'obox_id'             
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = 'overtime, '
                    home_away = 'home'
                    overtime = '4'
                count= count -1


            if ((id.text).find("-") != -1):
                #print("This is basic entire") 
                if(count==0):
                    box_type= 'Entire'
                    box_typeid = 'ebox_id'             
                    team = testawayid
                    game = testgameid
                    quarter_half_insert = ''
                    home_away = 'away'
                if(count==8):
                
                    box_type= 'Entire'
                    box_typeid = 'ebox_id'
                    #print(table)

                    
                    team = testhomeid
                    game = testgameid
                    quarter_half_insert = ''
                    home_away = 'home'

            rowstart = 0
            bs_type = tr[0].text
          
            columnheaders = tr[1].text

            columnheaders = columnheaders.replace("\n","`,`")
            columnheaders = columnheaders[2:]
            columnheaders = columnheaders[:-2]

            num_col = len(columnheaders.split(","))
            #print(num_col)
            database_name = id.text
            database_name = database_name.find("(") 
            ###print(columnheaders)

            #print(id)
            #print(columnheaders)

            


 

            
            
                #print(table)
            
            






            


            if(count==16):
                
                box_type= 'Entire'
                box_typeid = 'ebox_id'
                
                team = testhomeid
                game = testgameid
                quarter_half_insert = ''
                home_away = 'home'
            

            #print(type(quarter_half_insert))
            insert_statement = "Insert INTO nba_stats." +box_type +"_BoxScore(" +box_typeid +",game_id, team_id," + quarter_half_insert + "`Home/Away`," +columnheaders + ") VALUES ("
            #print(insert_statement)
            

            #print(testhomeid)
            #print(testawayid)
            #print(testgameid)
            
            print(overtime)
            #print(team + "," + id.text + "," + bs_type  + "," + columnheaders )
            #print(id.text)
            
            for row in tr:
                game_for_id = game *2
                team_for_id = team * 3
                #print(lazy_add)
                #print(game_for_id)
                #print(team_for_id)
                insert_df = pd.Series()    
                lazyid =  str(lazy_add) +str(game_for_id) +str(team_for_id) +str(rowstart) + str(len(columnheaders)) + str(count) +str(team) 
                if(rowstart >= 2): 
                    insert_count = 0
                    insert_item=[]
                    insert_item.append(lazyid)
                    insert_count +=1
                    insert_item.append(game)
                    insert_count +=1
                    print(team)
                    insert_item.append(team)
                    insert_count +=1
                    
                    if (quarter == 0):
                        if(half !=0):
                            insert_item.append(half)
                            insert_count +=1
                    if(half==0):
                        if(quarter != 0):
                            insert_item.append(quarter)
                            insert_count +=1
                    if(overtime =='1'):
                        insert_item.append(overtime)
                        insert_count +=1
                    if (overtime =='2'):
                        insert_item.append(overtime)
                        insert_count +=1
                    if (overtime =='3'):
                        insert_item.append(overtime)
                        insert_count +=1
                    if (overtime =='4'):
                        insert_item.append(overtime)
                        insert_count +=1 


                    insert_item.append(home_away)
                    insert_count +=1
                    
                    ths = tr[rowstart].find('th')
                    
                    name= strip_accents(ths.text)
                    insert_item.append(name)
                    insert_count +=1
                    tds = tr[rowstart].find_all('td')
                    lazy_add += 1
                    for cell in tds:
                        new_cell = cell.prettify
                        lazy_add += 1
                        #if (cell.text) == (''):
                            #print("we entered this loop")
                            #insert_item.append(0.00)
                        if (cell.text == '\xa0'):
                            insert_item.append("Did Not Play")
                        else:
                            insert_item.append(cell.text)
                        #if(rowstart==2):
                            #insert_count +=1
                        
                    
                    
                    
                    total_col = insert_count + num_col - 1


                    while (len(insert_item) != total_col):
                        insert_item.append('null')

                    insert_questions =[]
                    insert_questions.append("%s")
                    z =1
                    while len(insert_item) > z:
                        
                        insert_questions.append("%s")
                        z +=1
                    lazy_add +=1    
                    lazyid = lazyid + str(lazy_add)
                    if(insert_item[4] != "Reserves"):
                        if (insert_item[4] != 'Team Totals'):
                            
                            #csv_insert_string= insert_statement, str(insert_item)[1:-1]  +")"
                            
                            #print(insert_item)
                            #print(insert_statement, str(insert_item)[1:-1]  +")")
                            insert_all= insert_statement + str(insert_item)[1:-1]  +")"
                            print(insert_all)
                            msqlcursor.execute(insert_all)
                            mydb.commit()
                            
                    
                            wr.writerow(insert_item)
                

                #print(len(insert_item))
                #print(len(insert_questions))


                    
                


                rowstart +=1
        
            #insert_df.append(insert_item)
        #conn = sqlite3.connect("NbaStats.db")
        #curs = conn.cursor()    
        #reader = csv.reader(open('boxscore.csv','r'), delimiter='"')
         #  for row in reader:
          #      curs.execute("INSERT INTO teams(count, team_id, full_name, abbreviation, nickname, city, state, year_founded) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
#conn.commit()
            
        ##table = BeautifulSoup(table)
        ##print(table)
        ##for row ineach 
        
##print(soup)
        #conn.commit()
        count += 1







testhomeid = 1610612740
testawayid = 1610612763
testgameid = 21901253



#clean_insert_boxscore(this_soup,testhomeid,testawayid,testgameid)

def url_builder():
    base = "https://www.basketball-reference.com/boxscores/"


    mydb = mysql.connector.connect(
    host="localhost",
    user="robert",
    password="Da@sani1"
    )

    curs = mydb.cursor()
    curs.execute("SELECT team_id, game_id, Game_date, Matchup FROM nba_stats.games where game_id not in (select game_id from nba_stats.entire_boxscore);")
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
        #print(date)
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
        #print(hometeams)
        all_urls.append(final_url)


    return(all_urls, gameids,hometeams,awayteams)





def gather_data_from_url(urs,gameids,hometeams,awayteams):
    y=0
    for url in urls:
        conn = sqlite3.connect("NbaStats.db")
        curs = conn.cursor()
        curs.execute("SELECT team_id from teams where abbreviation like '"+awayteams[y] +"';")
        for row in curs:
            awayteamid = row[0]
        curs.execute("SELECT team_id from teams where abbreviation like '"+hometeams[y] +"';")
        for row in curs:
            hometeamid = row[0]
        clean_insert_boxscore(url, hometeamid, awayteamid, gameids[y])
        y+=1
#print(teamids)


#testhomeid = 1610612740
#testawayid = 1610612763
#testgameid = 21901253
url = "https://www.basketball-reference.com/boxscores/201911010DAL.html"
urls, gameids, hometeams, awayteams = url_builder()
gather_data_from_url(urls,gameids,hometeams,awayteams)


