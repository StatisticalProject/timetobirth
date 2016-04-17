import urllib, json
import urllib.request,os
KEY="A00239D3-45F6-4A0A-810C-54A347F144C2"
KEY="720129CF233B4CA2DF97DAE48C8717E1"
SERIES="1"
IDSEASON="118"
if( not os.path.exists("currenseason")):
    os.mkdir("currenseason")
if( not os.path.exists("currenseason/"+SERIES)):
    os.mkdir("currenseason/"+SERIES)    
if( not os.path.exists("currenseason/"+SERIES+"/currentseason.json")):
    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/currentseason.json"
    with urllib.request.urlopen(url) as url:
        response = url.read().decode('utf-8')
    data = json.loads(response)
    f = open('currenseason/'+SERIES+'/currentseason.json', 'w')
    f.write(response)
    f.close()
    print (data)
    print (data['name'])

f = open('currenseason/'+SERIES+'/currentseason.json', 'r')
data=json.loads(f.read())
f.close()
IDSEASON=str(data["current_season"]["id"])

if( not os.path.exists("conferences")):
    os.mkdir("conferences")

if( not os.path.exists("conferences/conferences.json")):
    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/conferences.json?userkey="+KEY
    with urllib.request.urlopen(url) as url:
        response = url.read().decode('utf-8')
    data = json.loads(response)
    f = open('conferences/conferences.json', 'w')
    f.write(response)
    f.close()
    print (data)

if( not os.path.exists("ladder")):
    os.mkdir("ladder")
if( not os.path.exists("ladder/"+SERIES)):
    os.mkdir("ladder/"+SERIES)
if( not os.path.exists("ladder/"+SERIES+"/"+IDSEASON)):
    os.mkdir("ladder/"+SERIES+"/"+IDSEASON)
if( not os.path.exists("ladder/"+SERIES+"/"+IDSEASON+"/lader.json")):
    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/ladder.json?userkey="+KEY
    with urllib.request.urlopen(url) as url:
        response = url.read().decode('utf-8')
    data = json.loads(response)
    f = open("ladder/"+SERIES+"/"+IDSEASON+"/lader.json", 'w')
    f.write(response)
    f.close()
    print (data)

f = open("ladder/"+SERIES+"/"+IDSEASON+"/lader.json", 'r')
dataTeam=json.loads(f.read())
f.close()

for teamm in dataTeam['teams']:
    TEAM=str(teamm['id'])
    if( not os.path.exists("fixturesandresultswithbyes")):
        os.mkdir("fixturesandresultswithbyes")
    if( not os.path.exists("fixturesandresultswithbyes/"+SERIES)):
        os.mkdir("fixturesandresultswithbyes/"+SERIES)
    if( not os.path.exists("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON)):
        os.mkdir("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON)

    if( not os.path.exists("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM)):
        os.mkdir("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM)
    if( not os.path.exists("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/fixturesandresultswithbyes.json")):
        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/teams/"+TEAM+"/fixturesandresultswithbyes.json?userkey="+KEY
        with urllib.request.urlopen(url) as url:
            response = url.read().decode('utf-8')
        data = json.loads(response)
        f = open("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/fixturesandresultswithbyes.json", 'w')
        f.write(response)
        f.close()
        print (data)
    
    if( not os.path.exists("summary")):
        os.mkdir("summary")
    if( not os.path.exists("summary/"+SERIES)):
        os.mkdir("summary/"+SERIES)
    if( not os.path.exists("summary/"+SERIES+"/"+IDSEASON)):
        os.mkdir("summary/"+SERIES+"/"+IDSEASON)

    if( not os.path.exists("summary/"+SERIES+"/"+IDSEASON+"/"+TEAM)):
        os.mkdir("summary/"+SERIES+"/"+IDSEASON+"/"+TEAM)
    if( not os.path.exists("summary/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/summary.json")):
        url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/teams/"+TEAM+"/summary.json?userkey="+KEY
        with urllib.request.urlopen(url) as url:
            response = url.read().decode('utf-8')
        data = json.loads(response)
        f = open("summary/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/summary.json", 'w')
        f.write(response)
        f.close()
        print (data)

    f = open("fixturesandresultswithbyes/"+SERIES+"/"+IDSEASON+"/"+TEAM+"/fixturesandresultswithbyes.json", 'r')
    dataMatchId=json.loads(f.read())
    f.close()

    for macth in dataMatchId:
        MATCHID=macth['match_id']
        if MATCHID is not None:
            if( not os.path.exists("scoreboard")):
                os.mkdir("scoreboard")
            if( not os.path.exists("scoreboard/"+MATCHID)):
                os.mkdir("scoreboard/"+MATCHID)
            if( not os.path.exists("scoreboard/"+MATCHID+"/scoreboard.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/scoreboard.json?userkey="+KEY
                with urllib.request.urlopen(url) as url:
                    response = url.read().decode('utf-8')
                data = json.loads(response)
                f = open("scoreboard/"+MATCHID+"/scoreboard.json", 'w')
                f.write(response)
                f.close()
                print (data)

            if( not os.path.exists("breakdown")):
                os.mkdir("breakdown")
            if( not os.path.exists("breakdown/"+MATCHID)):
                os.mkdir("breakdown/"+MATCHID)
            if( not os.path.exists("breakdown/"+MATCHID+"/breakdown.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/breakdown.json?userkey="+KEY
                with urllib.request.urlopen(url) as url:
                    response = url.read().decode('utf-8')
                data = json.loads(response)
                f = open("breakdown/"+MATCHID+"/breakdown.json", 'w')
                f.write(response)
                f.close()
                print (data)

            if( not os.path.exists("teamstats")):
                os.mkdir("teamstats")
            if( not os.path.exists("teamstats/"+MATCHID)):
                os.mkdir("teamstats/"+MATCHID)
            if( not os.path.exists("teamstats/"+MATCHID+"/teamstats.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/teamstats.json?userkey="+KEY
                with urllib.request.urlopen(url) as url:
                    response = url.read().decode('utf-8')
                data = json.loads(response)
                f = open("teamstats/"+MATCHID+"/teamstats.json", 'w')
                f.write(response)
                f.close()
                print (data)

            if( not os.path.exists("commentary")):
                os.mkdir("commentary")
            if( not os.path.exists("commentary/"+MATCHID)):
                os.mkdir("commentary/"+MATCHID)
            if( not os.path.exists("commentary/"+MATCHID+"/commentary.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/commentary.json?userkey="+KEY
                with urllib.request.urlopen(url) as url:
                    response = url.read().decode('utf-8')
                data = json.loads(response)
                f = open("commentary/"+MATCHID+"/commentary.json", 'w')
                f.write(response)
                f.close()
                print (data)

            if( not os.path.exists("players")):
                os.mkdir("players")
            if( not os.path.exists("players/"+MATCHID)):
                os.mkdir("players/"+MATCHID)
            if( not os.path.exists("players/"+MATCHID+"/players.json")):
                url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/players.json?userkey="+KEY
                with urllib.request.urlopen(url) as url:
                        response = url.read().decode('utf-8')
                data = json.loads(response)
                f = open("players/"+MATCHID+"/players.json", 'w')
                f.write(response)
                f.close()
                print (data)

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
                if( not os.path.exists("players/"+MATCHID+"/"+PLAYERID+"/stats.json")):
                    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/players/"+PLAYERID+"/stats.json?userkey="+KEY
                    with urllib.request.urlopen(url) as url:
                        response = url.read().decode('utf-8')
                    data = json.loads(response)
                    f = open("players/"+MATCHID+"/"+PLAYERID+"/stats.json", 'w')
                    f.write(response)
                    f.close()
                    print (data)
                if( not os.path.exists("playersAll")):
                    os.mkdir("playersAll")
                if( not os.path.exists("playersAll/"+PLAYERID)):
                    os.mkdir("playersAll/"+PLAYERID)
                if( not os.path.exists("playersAll/"+PLAYERID+"/stats.json")):
                    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/players/"+PLAYERID+"/stats.json?userkey="+KEY
                    with urllib.request.urlopen(url) as url:
                        response = url.read().decode('utf-8')
                    data = json.loads(response)
                    f = open("playersAll/"+PLAYERID+"/stats.json", 'w')
                    f.write(response)
                    f.close()
                    print (data)
                if( not os.path.exists("biography")):
                    os.mkdir("biography")
                if( not os.path.exists("biography/"+PLAYERID)):
                    os.mkdir("biography/"+PLAYERID)
                if( not os.path.exists("biography/"+PLAYERID+"/biography.json")):
                    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/players/"+PLAYERID+"/biography.json?userkey="+KEY
                    with urllib.request.urlopen(url) as url:
                        response = url.read().decode('utf-8')
                    data = json.loads(response)
                    f = open("biography/"+PLAYERID+"/biography.json", 'w')
                    f.write(response)
                    f.close()
                    print (data)
                    
            playerss=dataPlayers['team_B']['players']
            for player in playerss:
                PLAYERID=str(player['id'])
                if( not os.path.exists("players")):
                    os.mkdir("players")
                if( not os.path.exists("players/"+MATCHID)):
                    os.mkdir("players/"+MATCHID)
                if( not os.path.exists("players/"+MATCHID+"/"+PLAYERID)):
                    os.mkdir("players/"+MATCHID+"/"+PLAYERID)
                if( not os.path.exists("players/"+MATCHID+"/"+PLAYERID+"/stats.json")):
                    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/matches/"+MATCHID+"/players/"+PLAYERID+"stats.json?userkey="+KEY
                    with urllib.request.urlopen(url) as url:
                        response = url.read().decode('utf-8')
                    data = json.loads(response)
                    f = open("players/"+MATCHID+"/"+PLAYERID+"/stats.json", 'w')
                    f.write(response)
                    f.close()
                    print (data)
                    
                if( not os.path.exists("playersAll")):
                    os.mkdir("playersAll")
                if( not os.path.exists("playersAll/"+PLAYERID)):
                    os.mkdir("playersAll/"+PLAYERID)
                if( not os.path.exists("playersAll/"+PLAYERID+"/stats.json")):
                    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/series/"+SERIES+"/seasons/"+IDSEASON+"/players/"+PLAYERID+"/stats.json?userkey="+KEY
                    with urllib.request.urlopen(url) as url:
                        response = url.read().decode('utf-8')
                    data = json.loads(response)
                    f = open("playersAll/"+PLAYERID+"/stats.json", 'w')
                    f.write(response)
                    f.close()
                    print (data)

                if( not os.path.exists("biography")):
                    os.mkdir("biography")
                if( not os.path.exists("biography/"+PLAYERID)):
                    os.mkdir("biography/"+PLAYERID)
                if( not os.path.exists("biography/"+PLAYERID+"/biography.json")):
                    url = "http://api.stats.foxsports.com.au/3.0/api/sports/rugby/players/"+PLAYERID+"/biography.json?userkey="+KEY
                    with urllib.request.urlopen(url) as url:
                        response = url.read().decode('utf-8')
                    data = json.loads(response)
                    f = open("biography/"+PLAYERID+"/biography.json", 'w')
                    f.write(response)
                    f.close()
                    print (data)


