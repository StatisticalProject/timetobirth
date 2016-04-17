import csv, json, sys,os

def load_json(myjson):
  try:
    return json.loads(myjson)
  except ValueError :
    return {}
  return {}

def load_file_json(myjson):
  if ( os.path.exists(myjson)) :
      f = open(myjson, 'r')
      return load_json(f.read())
  return {}

def flattenjson( b, delim ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]

    return val
f = open("biogarphies.csv", 'w')
f.write("id,height_cm,surname,full_name,other_names,str(weight_kg),date_of_birth,short_name,default_position\n")
         
for dirname, dirnames, filenames in os.walk('biography'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname,"biography.json"))
        try:
            input = open(os.path.join(dirname, subdirname,"biography.json"))
            data = json.load(input)
            input.close()
            height_cm=data["height_cm"]
            surname=data["surname"]
            full_name=data["full_name"]
            other_names=data["other_names"]
            weight_kg=data["weight_kg"]
            date_of_birth=data["date_of_birth"]
            idd=data["id"]
            short_name=data["short_name"]
            default_position=data["default_position"]
            f.write(str(idd)+","+str(height_cm)+","+surname+","+full_name+","+other_names+","+str(weight_kg)+","+date_of_birth+","+short_name+","+default_position+"\n")
        except:
            print ("no "+subdirname)
f.close() 

f = open("breakdown.csv", 'w')
f.write("subdirname,code,team_id,team_name,team_code,team_short_name,player_id,player_full_name,player_short_name,period,time,name,display_time,team_A_score,team_B_score,video_id,sequence_no\n")
         
for dirname, dirnames, filenames in os.walk('breakdown'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname,"breakdown.json"))
        try:
            input = open(os.path.join(dirname, subdirname,"breakdown.json"))
            data = json.load(input)
            input.close()
        except:
            print ("no "+subdirname)
            data={"events":[]}
        events=data["events"]
        for event in events :
                
                code=event["code"]
                team_id=str(event["team"]["id"])
                team_name=event["team"]["name"]
                team_code=event["team"]["code"]
                team_short_name=event["team"]["short_name"]
                player_id=str(event["player"]["id"])
                player_full_name=event["player"]["full_name"]
                player_short_name=event["player"]["short_name"]
                period=str(event["period"])
                time=str(event["time"])
                name=event["name"]
                display_time=event["display_time"]
                
                team_A_score=str(event["team_A_score"])
                team_B_score=str(event["team_B_score"])
                
                video_id=event["video_id"]
                if video_id is None:
                    video_id=""
                try:
                    sequence_no=str(event["sequence_no"])
                except:
                    sequence_no=""

                f.write(subdirname+","+code+","+team_id+","+team_name+","+team_code+","+team_short_name+","+player_id+","+player_full_name+","+player_short_name+","+period+","+time+","+name+","+display_time+","+team_A_score+","+team_B_score+","+video_id+","+sequence_no+"\n")
        
f.close()

f = open("commentary.csv", 'w')
f.write("subdirname,code,team_id,team_name,team_code,team_short_name,period,time,name,display_time,team_A_score,team_B_score,video_id,commentary\n")
         
for dirname, dirnames, filenames in os.walk('commentary'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname,"commentary.json"))
        try:
            input = open(os.path.join(dirname, subdirname,"commentary.json"))
            data = json.load(input)
            input.close()
        except:
            print ("no "+subdirname)
            data=[]
        for event in data :
                
                code=event["code"]
                team_id=str(event["team"]["id"])
                team_name=event["team"]["name"]
                team_code=event["team"]["code"]
                team_short_name=event["team"]["short_name"]
                period=str(event["period"])
                time=str(event["time"])
                name=event["name"]
                display_time=event["display_time"]
                
                team_A_score=str(event["team_A_score"])
                team_B_score=str(event["team_B_score"])
                
                video_id=event["video_id"]
                commentary=event["commentary"]
                
                if video_id is None:
                    video_id=""
                if code is None:
                    code=""

                f.write(subdirname+","+code+","+team_id+","+team_name+","+team_code+","+team_short_name+","+period+","+time+","+name+","+display_time+","+team_A_score+","+team_B_score+","+video_id+",\""+commentary+"\"\n")
        
f.close()

f = open("fixturesandresultswithbyes.csv", 'w')
f.write("subdirname,season,match_day,sport,series_id,series_name,series_code,series_category,season_id,season_year,season_name,round_name,round_number,round_short_name,"
      +"venue_id,venue_name,venue_city,pool,fixture_id,match_id,match_number,match_start_date,match_sorting_date,is_final,is_grand_final,capture_type,match_status,match_time,"
      +"team_A_id,team_A_name,team_A_code,team_A_score,team_A_short_name,team_A_competition_table_position,team_B_id,team_B_name,team_B_code,team_B_score,team_B_short_name,team_B_competition_table_position,"
      +"is_bye,winning_team_id,is_clock_running\n")
         
for dirname, dirnames, filenames in os.walk('fixturesandresultswithbyes'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        for dirname2, dirnames2, filenames2 in os.walk(os.path.join(dirname, subdirname)):
          for subdirname2 in dirnames2:
            for dirname3, dirnames3, filenames3 in os.walk(os.path.join(dirname, subdirname, subdirname2)):
              for subdirname3 in dirnames3:
                print(os.path.join(dirname, subdirname, subdirname2, subdirname3,"fixturesandresultswithbyes.json"))
                try:
                    input = open(os.path.join(dirname, subdirname, subdirname2, subdirname3,"fixturesandresultswithbyes.json"))
                    data = json.load(input)
                    input.close()
                except:
                    print ("no "+subdirname)
                    data=[]
                for event in data :
                        
                        sport=event["sport"]

                        series_id=str(event["series"]["id"])
                        series_name=event["series"]["name"]
                        series_code=event["series"]["code"]
                        series_category=event["series"]["category"]
                        if series_category is None:
                            series_category=""

                        season_id=str(event["season"]["id"])
                        season_year=str(event["season"]["year"])
                        season_name=event["season"]["name"]

                        round_name=event["round"]["name"]
                        round_number=str(event["round"]["number"])
                        round_short_name=event["round"]["short_name"]

                        venue_id=event["venue"]["id"]
                        if venue_id is None :
                          venue_id=""
                        else:
                          venue_id=str(venue_id)
                        venue_name=event["venue"]["name"]
                        if venue_name is None :
                          venue_name=""                        
                        venue_city=event["venue"]["city"]
                        if venue_city is None :
                          venue_city=""

                        pool=event["pool"]
                        if pool is None :
                          pool=""
                        fixture_id=event["fixture_id"]
                        if fixture_id is None :
                          fixture_id=""
                        else:
                          fixture_id=str(fixture_id)
                        match_id=event["match_id"]
                        if match_id is None :
                          match_id=""
                        else:
                          match_id=str(match_id)
                        match_number=event["match_number"]
                        if match_number is None :
                          match_number=""
                        else:
                          match_number=str(match_number)
                        match_start_date=event["match_start_date"]
                        if match_start_date is None :
                          match_start_date=""
                        match_sorting_date=event["match_sorting_date"]
                        if match_sorting_date is None :
                          match_sorting_date=""
                        is_final=str(event["is_final"])
                        is_grand_final=str(event["is_grand_final"])
                        capture_type=event["capture_type"]
                        match_status=event["match_status"]
                        if match_status is None :
                          match_status=""
                        match_time=event["match_time"]
                        if match_time is None :
                          match_time=""

                        team_A_id=str(event["team_A"]["id"])
                        team_A_name=event["team_A"]["name"]
                        team_A_code=event["team_A"]["code"]
                        team_A_score=event["team_A"]["score"]
                        if team_A_score is None :
                          team_A_score=""
                        else:
                          team_A_score=str(team_A_score)
                        team_A_short_name=event["team_A"]["short_name"]
                        team_A_competition_table_position=str(event["team_A"]["competition_table_position"])

                        team_B_id=str(event["team_B"]["id"])
                        if team_B_id is None :
                          team_B_id=""
                        team_B_name=event["team_B"]["name"]
                        if team_B_name is None :
                          team_B_name=""
                        
                        team_B_code=event["team_B"]["code"]
                        if team_B_code is None :
                          team_B_code=""
                        
                        team_B_score=event["team_B"]["score"]
                        if team_B_score is None :
                          team_B_score=""
                        else:
                          team_B_score=str(team_A_score)
                        team_B_short_name=event["team_B"]["short_name"]
                        if team_B_short_name is None :
                          team_B_short_name=""

                        team_B_competition_table_position=str(event["team_B"]["competition_table_position"])
                        if team_B_competition_table_position is None :
                          team_B_competition_table_position=""
                        
                        is_bye=str(event["is_bye"])
                        if is_bye is None :
                          is_bye="false"
                        else:
                          is_bye=str(is_bye)
                        winning_team_id=event["winning_team_id"]
                        if winning_team_id is None :
                          winning_team_id=""
                        else:
                          winning_team_id=str(winning_team_id)
                        is_clock_running=event["is_clock_running"]
                        if is_clock_running is None :
                          is_clock_running=""
                        else:
                          is_clock_running=str(is_clock_running)
                            
                        #print(event)
                        f.write(subdirname+","+subdirname2+","+subdirname3+","+sport+","+series_id+","+series_name+","+series_code+","
                                +series_category+","+season_id+","+season_year+","+season_name+","+round_name+","+round_number+","+round_short_name+","
                                +venue_id+","+venue_name+","+venue_city+","+pool+","+fixture_id+","+match_id+","+match_number+","+match_start_date+","
                                +match_sorting_date+","+is_final+","+is_grand_final+","+capture_type+","+match_status+","+match_time+","
                                +team_A_id+","+team_A_name+","+team_A_code+","+team_A_score+","+team_A_short_name+","+team_A_competition_table_position+","
                                +team_B_id+","+team_B_name+","+team_B_code+","+team_B_score+","+team_B_short_name+","+team_B_competition_table_position+","
                                +is_bye+","+winning_team_id+","+is_clock_running+"\n")
        
f.close()

f = open("players.csv", 'w')
f.write("match,id,uid,position,citations,conversions,kicks,passes,pilfers,points,possessions,runs,tries,turnovers,tackles,minutes_played,conversion_misses,drop_goal_misses,drop_goals,fantasy_points,"
  +"five_eight_kicks,five_eight_passes,five_eight_runs,forces_penalty,handling_errors,half_back_kicks,half_back_passes,half_back_runs,ineffective_tackles,interchanges_off,interchanges_on,kick_metres,line_break_creates,line_breaks,"
  +"line_outs_lost,line_outs_lost_on_jump_against_throw,line_outs_lost_on_jump_on_throw,line_outs_not_straight,line_outs_won,line_outs_won_against_throw,line_outs_won_by_opposition,line_outs_won_on_jump_against,line_outs_won_on_jump_on_throw,"
  +"missed_tackles,off_loads,over_advantage,over_advantage_failed,penalties_conceded,penalty_goal_misses,penalty_goals,pick_drives,rucks_and_mauls,run_metres,scrum_repacks,scrums_fed,scrums_lost_on_feed,scrums_won_on_feed,send_offs,"
  +"sin_bins,tackle_busts,full_name,short_name,date_of_birth,height_cm,weight_kg,jumper_number,position_code,position_order\n")
         
for dirname, dirnames, filenames in os.walk('players'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
      for dirname2, dirnames2, filenames2 in os.walk(os.path.join(dirname, subdirname)):
        for subdirname2 in dirnames2:
         print(os.path.join(dirname, subdirname,subdirname2,"stats.json"))
         try:
            input = open(os.path.join(dirname, subdirname,subdirname2,"stats.json"))
            data = json.load(input)
            input.close()
         except:
            print ("no "+subdirname)
            continue
         
         uid=str(data["id"])
         position=data["position"]
         citations=str(data["stats"]["citations"])
         conversions=str(data["stats"]["conversions"])
         kicks=str(data["stats"]["kicks"])
         passes=str(data["stats"]["passes"])
         pilfers=str(data["stats"]["pilfers"])
         points=str(data["stats"]["points"])
         possessions=str(data["stats"]["possessions"])
         runs=str(data["stats"]["runs"])
         tries=str(data["stats"]["tries"])
         turnovers=str(data["stats"]["turnovers"])
         tackles=str(data["stats"]["tackles"])
         minutes_played=str(data["stats"]["minutes_played"])
         conversion_misses=str(data["stats"]["conversion_misses"])
         drop_goal_misses=str(data["stats"]["drop_goal_misses"])
         drop_goals=str(data["stats"]["drop_goals"])
         fantasy_points=str(data["stats"]["fantasy_points"])
         five_eight_kicks=str(data["stats"]["five_eight_kicks"])
         five_eight_passes=str(data["stats"]["five_eight_passes"])
         five_eight_runs=str(data["stats"]["five_eight_runs"])
         forces_penalty=str(data["stats"]["forces_penalty"])
         handling_errors=str(data["stats"]["handling_errors"])
         half_back_kicks=str(data["stats"]["half_back_kicks"])
         half_back_passes=str(data["stats"]["half_back_passes"])
         half_back_runs=str(data["stats"]["half_back_runs"])
         ineffective_tackles=str(data["stats"]["ineffective_tackles"])
         interchanges_off=str(data["stats"]["interchanges_off"])
         interchanges_on=str(data["stats"]["interchanges_on"])
         kick_metres=str(data["stats"]["kick_metres"])
         line_break_creates=str(data["stats"]["line_break_creates"])
         line_breaks=str(data["stats"]["line_breaks"])
         line_outs_lost=str(data["stats"]["line_outs_lost"])
         line_outs_lost_on_jump_against_throw=str(data["stats"]["line_outs_lost_on_jump_against_throw"])
         line_outs_lost_on_jump_on_throw=str(data["stats"]["line_outs_lost_on_jump_on_throw"])
         line_outs_not_straight=str(data["stats"]["line_outs_not_straight"])
         line_outs_won=str(data["stats"]["line_outs_won"])
         line_outs_won_against_throw=str(data["stats"]["line_outs_won_against_throw"])
         line_outs_won_by_opposition=str(data["stats"]["line_outs_won_by_opposition"])
         line_outs_won_on_jump_against=str(data["stats"]["line_outs_won_on_jump_against"])
         line_outs_won_on_jump_on_throw=str(data["stats"]["line_outs_won_on_jump_on_throw"])
         missed_tackles=str(data["stats"]["missed_tackles"])
         off_loads=str(data["stats"]["off_loads"])
         over_advantage=str(data["stats"]["over_advantage"])
         over_advantage_failed=str(data["stats"]["over_advantage_failed"])
         penalties_conceded=str(data["stats"]["penalties_conceded"])
         penalty_goal_misses=str(data["stats"]["penalty_goal_misses"])
         penalty_goals=str(data["stats"]["penalty_goals"])
         pick_drives=str(data["stats"]["pick_drives"])
         rucks_and_mauls=str(data["stats"]["rucks_and_mauls"])
         run_metres=str(data["stats"]["run_metres"])
         scrum_repacks=str(data["stats"]["scrum_repacks"])
         scrums_fed=str(data["stats"]["scrums_fed"])
         scrums_lost_on_feed=str(data["stats"]["scrums_lost_on_feed"])
         scrums_won_on_feed=str(data["stats"]["scrums_won_on_feed"])
         send_offs=str(data["stats"]["send_offs"])
         sin_bins=str(data["stats"]["sin_bins"])
         tackle_busts=str(data["stats"]["tackle_busts"])
         full_name=str(data["full_name"])
         short_name=str(data["short_name"])
         date_of_birth=str(data["date_of_birth"])
         height_cm=str(data["height_cm"])
         weight_kg=str(data["weight_kg"])
         jumper_number=str(data["jumper_number"])
         position_code=str(data["position_code"])
         position_order=str(data["position_order"])


         
         
         
         f.write(subdirname+","+subdirname2+","+uid+","+position+","+citations+","+conversions+","+kicks+","+passes+","+pilfers+","+points+","+possessions+","
                 +runs+","+tries+","+turnovers+","+tackles+","+minutes_played+","+conversion_misses+","+drop_goal_misses+","+drop_goals+","+fantasy_points+","
                 +five_eight_kicks+","+five_eight_passes+","+five_eight_runs+","+forces_penalty+","+handling_errors+","+half_back_kicks+","+half_back_passes+","
                 +half_back_runs+","+ineffective_tackles+","+interchanges_off+","+interchanges_on+","+kick_metres+","+line_break_creates+","+line_breaks+","
                 +line_outs_lost+","+line_outs_lost_on_jump_against_throw+","+line_outs_lost_on_jump_on_throw+","+line_outs_not_straight+","+line_outs_won+","
                 +line_outs_won_against_throw+","+line_outs_won_by_opposition+","+line_outs_won_on_jump_against+","+line_outs_won_on_jump_on_throw+","
                 +missed_tackles+","+off_loads+","+over_advantage+","+over_advantage_failed+","+penalties_conceded+","+penalty_goal_misses+","+penalty_goals+","
                 +pick_drives+","+rucks_and_mauls+","+run_metres+","+scrum_repacks+","+scrums_fed+","+scrums_lost_on_feed+","+scrums_won_on_feed+","+send_offs+","
                 +sin_bins+","+tackle_busts+","+full_name+","+short_name+","+date_of_birth+","+height_cm+","+weight_kg+","+jumper_number+","+position_code+","+position_order+"\n")
f.close()

