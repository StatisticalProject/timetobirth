import urllib, json
import urllib.request,os
import socket
import random
import re

socket.setdefaulttimeout(50)
#https://www.hide-my-ip.com/fr/proxylist.shtml
# .*(\[\{.*\]).*
KEY="A00239D3-45F6-4A0A-810C-54A347F144C2"
KEY="720129CF233B4CA2DF97DAE48C8717E1"
KEY="35d28185-0ca1-47f0-8caf-edc457802c9d"
KEY="B36714DE794D0080A183B5A12BEAF8B4"
KEYS=["B36714DE794D0080A183B5A12BEAF8B4","35d28185-0ca1-47f0-8caf-edc457802c9d","A00239D3-45F6-4A0A-810C-54A347F144C2","720129CF233B4CA2DF97DAE48C8717E1","A00239D3-45F6-4A0A-810C-54A347F144C2"]#,"9b0610b4-cc4e-455a-b64d-e2fd01b5b086"]
SERIES="1"
IDSEASON="118"
urlProxys=["http://104.28.26.15:80","http://195.89.201.48:80"]

with urllib.request.urlopen('https://www.hide-my-ip.com/fr/proxylist.shtml') as response:

  print("load list")
  html = str(response.read())
  #p = re.compile('.*(\[\{"i".*\}\])\;.*')
  #line=p.match(html).group(0)
  print ("parse1")
  p = re.compile('.*\[\{"i"')
  print ("parse2")
  
  liner=p.sub( '[{"i"', html, count=1)
  print ("parse3")
  
  p = re.compile('\}\];.*')
  print ("parse4")
  
  line2=p.sub( '}]', liner, count=1)
  print ("parse5")
  line3=line2.replace("\\n","")
  line4=line3.replace("\\","")
  line=line4.replace("}, n {","},{").replace(" n ","")
  
  #line = re.sub(p, "%s", html)
  f = open("jjj.json", 'w')
  f.write(line)
  f.close()
  json_object = json.loads(line)
  print ("mount node")
  for jsone in json_object:
    urlProxys.append("http://"+jsone["i"]+":"+jsone["p"])
  
proxy = urllib.request.FancyURLopener({"http":"http://201.208.63.214:3128"})
#proxy = urllib.request.URLopener()

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError :
    return False
  return True

def is_file_json(myjson):
  if ( os.path.exists(myjson)) :
      f = open(myjson, 'r')
      return is_json(f.read())
  return False

def loadAndWrite(myjson,filie):
    proxyMi=True
    counter=0
    while proxyMi:
        proxyurl = random.choice (urlProxys)
        try:
         
         proxy = urllib.request.FancyURLopener({"http":random.choice (urlProxys)})
         with proxy.open(myjson, data=None ) as url:
                response = url.read().decode('utf-8')
                
         data = json.loads(response)
         f = open(filie, 'w')
         f.write(response)
         f.close()
         print ("nice:"+filie)
         proxyMi=False
        except ValueError :
         print ('error '+str(counter)+':'+myjson+":"+filie+":"+proxyurl)
         if counter>15 :
           proxyMi=False
         counter=counter+1
        except OSError :
         print ('retry:'+myjson+":"+filie+":"+proxyurl)    

if( not os.path.exists("currenseason")):
    os.mkdir("currenseason")
if( not os.path.exists("currenseason/"+SERIES)):
    os.mkdir("currenseason/"+SERIES)    
if( not is_file_json("currenseason/"+SERIES+"/currentseason.json")):
    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/currentseason.json"
    loadAndWrite(url,"currenseason/"+SERIES+"/currentseason.json")
    
f = open('currenseason/'+SERIES+'/currentseason.json', 'r')
data=json.loads(f.read())
f.close()
IDSEASON=str(data["current_season"]["id"])
IDSEASON="116"

if( not os.path.exists("conferences")):
    os.mkdir("conferences")

if( not os.path.exists("conferences/conferences.json")):
    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/conferences.json?userkey="+random.choice (KEYS)
    loadAndWrite(url,"conferences/conferences.json")


if( not os.path.exists("ladder")):
    os.mkdir("ladder")
if( not os.path.exists("ladder/"+SERIES)):
    os.mkdir("ladder/"+SERIES)
if( not os.path.exists("ladder/"+SERIES+"/"+IDSEASON)):
    os.mkdir("ladder/"+SERIES+"/"+IDSEASON)
if( not is_file_json("ladder/"+SERIES+"/"+IDSEASON+"/lader.json") ):
    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/ladder.json?userkey="+random.choice (KEYS)
    loadAndWrite(url,"ladder/"+SERIES+"/"+IDSEASON+"/lader.json")



f = open("ladder/"+SERIES+"/"+IDSEASON+"/lader.json", 'r')
dataTeam=json.loads(f.read())
f.close()
countyx=0
for teamm in dataTeam['teams']:
    countyx=countyx+1
    print("TT "+str(countyx)+"/"+str(len(dataTeam['teams'])))
    TEAM=str(teamm['id'])
    if( not os.path.exists("fixturesandresultswithbyes")):
        os.mkdir("fixturesandresultswithbyes")
    if( not os.path.exists("fixturesandresultswithbyes/"+SERIES)):
        os.mkdir("fixturesandresultswithbyes/"+SERIES)
    if( not os.path.exists("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON)):
        os.mkdir("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON)

    if( not os.path.exists("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM)):
        os.mkdir("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM)
    if( not is_file_json("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/fixturesandresultswithbyes.json")):
        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/teams/"+TEAM+"/fixturesandresultswithbyes.json?userkey="+random.choice (KEYS)
        loadAndWrite(url,"fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/fixturesandresultswithbyes.json")
    
    if( not os.path.exists("summary")):
        os.mkdir("summary")
    if( not os.path.exists("summary/"+SERIES)):
        os.mkdir("summary/"+SERIES)
    if( not os.path.exists("summary/"+SERIES+"/"+IDSEASON)):
        os.mkdir("summary/"+SERIES+"/"+IDSEASON)

    if( not os.path.exists("summary/"+SERIES+"/"+IDSEASON+"/"+TEAM)):
        os.mkdir("summary/"+SERIES+"/"+IDSEASON+"/"+TEAM)
    if( not is_file_json("summary/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/summary.json")):
        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/teams/"+TEAM+"/summary.json?userkey="+random.choice (KEYS)
        loadAndWrite(url,"summary/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/summary.json")
    try:
     f = open("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/fixturesandresultswithbyes.json", 'r')
     dataMatchId=json.loads(f.read())
     f.close()
    except:
     print ("err:fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/fixturesandresultswithbyes.json")
     dataMatchId=[]
    county = 0
    for macth in dataMatchId:
        county=county+1
        print ("NB "+str(county)+"/"+str(len(dataMatchId)))
        MATCHID=macth['match_id']
        if MATCHID is not None:
            if( not os.path.exists("scoreboard")):
                os.mkdir("scoreboard")
            if( not os.path.exists("scoreboard/"+MATCHID)):
                os.mkdir("scoreboard/"+MATCHID)
            if( not is_file_json("scoreboard/"+MATCHID+"/scoreboard.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/scoreboard.json?userkey="+random.choice (KEYS)
                loadAndWrite(url,"scoreboard/"+MATCHID+"/scoreboard.json")

            if( not os.path.exists("breakdown")):
                os.mkdir("breakdown")
            if( not os.path.exists("breakdown/"+MATCHID)):
                os.mkdir("breakdown/"+MATCHID)
            if( not is_file_json("breakdown/"+MATCHID+"/breakdown.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/breakdown.json?userkey="+random.choice (KEYS)
                loadAndWrite(url,"breakdown/"+MATCHID+"/breakdown.json")

            if( not os.path.exists("teamstats")):
                os.mkdir("teamstats")
            if( not os.path.exists("teamstats/"+MATCHID)):
                os.mkdir("teamstats/"+MATCHID)
            if( not is_file_json("teamstats/"+MATCHID+"/teamstats.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/teamstats.json?userkey="+random.choice (KEYS)
                loadAndWrite(url,"teamstats/"+MATCHID+"/teamstats.json")
                

            if( not os.path.exists("commentary")):
                os.mkdir("commentary")
            if( not os.path.exists("commentary/"+MATCHID)):
                os.mkdir("commentary/"+MATCHID)
            if( not is_file_json("commentary/"+MATCHID+"/commentary.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/commentary.json?userkey="+random.choice (KEYS)
                loadAndWrite(url,"commentary/"+MATCHID+"/commentary.json")
          
            if( not os.path.exists("players")):
                os.mkdir("players")
            if( not os.path.exists("players/"+MATCHID)):
                os.mkdir("players/"+MATCHID)
            if( not is_file_json("players/"+MATCHID+"/players.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/players.json?userkey="+random.choice (KEYS)
                loadAndWrite(url,"players/"+MATCHID+"/players.json")
            if (is_file_json("players/"+MATCHID+"/players.json")):
                f = open("players/"+MATCHID+"/players.json", 'r')
                dataPlayers=json.loads(f.read())
                f.close()
                playerss=dataPlayers['team_A']['players']
                for player in playerss:
                    PLAYERID=str(player['id'])
                    if( not os.path.exists("players")):
                        os.mkdir("players")
                    if( not os.path.exists("players/"+MATCHID)):
                        os.mkdir("players/"+MATCHID)
                    if( not os.path.exists("players/"+MATCHID+"/"+PLAYERID)):
                        os.mkdir("players/"+MATCHID+"/"+PLAYERID)
                    if( not is_file_json("players/"+MATCHID+"/"+PLAYERID+"/stats.json")):
                        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/players/"+PLAYERID+"/stats.json?userkey="+random.choice (KEYS)
                        loadAndWrite(url,"players/"+MATCHID+"/"+PLAYERID+"/stats.json")
                       
                    if( not os.path.exists("playersAll")):
                        os.mkdir("playersAll")
                    if( not os.path.exists("playersAll/"+IDSEASON)):
                        os.mkdir("playersAll/"+IDSEASON)
                    if( not os.path.exists("playersAll/"+IDSEASON+"/"+PLAYERID)):
                        os.mkdir("playersAll/"+IDSEASON+"/"+PLAYERID)
                    if( not is_file_json("playersAll/"+IDSEASON+"/"+PLAYERID+"/stats.json")):
                        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/players/"+PLAYERID+"/stats.json?userkey="+random.choice (KEYS)
                        loadAndWrite(url,"playersAll/"+IDSEASON+"/"+PLAYERID+"/stats.json")
                        
                    if( not os.path.exists("biography")):
                        os.mkdir("biography")
                    if( not os.path.exists("biography/"+PLAYERID)):
                        os.mkdir("biography/"+PLAYERID)
                    if( not is_file_json("biography/"+PLAYERID+"/biography.json")):
                        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/players/"+PLAYERID+"/biography.json?userkey="+random.choice (KEYS)
                        loadAndWrite(url,"biography/"+PLAYERID+"/biography.json")
                        
                        
                playerss=dataPlayers['team_B']['players']
                for player in playerss:
                    PLAYERID=str(player['id'])
                    if( not os.path.exists("players")):
                        os.mkdir("players")
                    if( not os.path.exists("players/"+MATCHID)):
                        os.mkdir("players/"+MATCHID)
                    if( not os.path.exists("players/"+MATCHID+"/"+PLAYERID)):
                        os.mkdir("players/"+MATCHID+"/"+PLAYERID)
                    if( not is_file_json("players/"+MATCHID+"/"+PLAYERID+"/stats.json")):
     
                        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/players/"+PLAYERID+"/stats.json?userkey="+random.choice (KEYS)
                        loadAndWrite(url,"players/"+MATCHID+"/"+PLAYERID+"/stats.json")
                        
                        
                    if( not os.path.exists("playersAll")):
                        os.mkdir("playersAll")
                    if( not os.path.exists("playersAll/"+IDSEASON)):
                        os.mkdir("playersAll/"+IDSEASON)
                    if( not os.path.exists("playersAll/"+IDSEASON+"/"+PLAYERID)):
                        os.mkdir("playersAll/"+IDSEASON+"/"+PLAYERID)
                    if( not is_file_json("playersAll/"+IDSEASON+"/"+PLAYERID+"/stats.json")):
                        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/players/"+PLAYERID+"/stats.json?userkey="+random.choice (KEYS)
                        loadAndWrite(url,"playersAll/"+IDSEASON+"/"+PLAYERID+"/stats.json")
                       

                    if( not os.path.exists("biography")):
                        os.mkdir("biography")
                    if( not os.path.exists("biography/"+PLAYERID)):
                        os.mkdir("biography/"+PLAYERID)
                    if( not is_file_json("biography/"+PLAYERID+"/biography.json")):
                        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/players/"+PLAYERID+"/biography.json?userkey="+random.choice (KEYS)
                        loadAndWrite(url,"biography/"+PLAYERID+"/biography.json")
                   

