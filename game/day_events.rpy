label day_events():
    #day events goes here
    label weekend_sat():
        if sat_event:
            call livingroom_scene
            label sat_what_to_do():
                if not mc_f:
                    call garage_scene
                    call change_loc('garage')
                    call w_mc(True)
                else:
                    fp "Ah, it's a beautiful day. Maybe I should go to the beach...?"
                    menu:
                        "Go to the beach":
                            call sat_beach()
                        "Nah, slack of in the garden instead":
                            call sat_end()
            label sat_beach():
                "this is a beach scene on saturday"
                call beach_scene from _call_beach_scene
                call change_loc('beach')
                $ renpy.pause()    
            label sat_end():
                $ sat_event = False
                call change_loc('livingroom')
            $ sat_event = False
            return
        else:
            return
    label weekend_sun():
        if sun_event:
            if renpy.random.random() <= .5:
                fM "Could you help me open this, [fp]? I can't seem to get it open, and I need this for dinner today"
                menu:
                    "Yes, [fmName.informal], no problem. *you open the jar*":
                        if fM_dom <= 5:
                            $ statschangeNotify("fM_dom",.5,True)
                            $ statschangeNotify("fM_rel",1)
                        else:
                            $ statschangeNotify("fM_rel",.5)
                    "No, [shortfM], I don't have time to help you right now":
                        $ statschangeNotify("fM_dom",.5,True)
                        $ statschangeNotify("fM_rel",-.5)
            $ sun_event = False
            call livingroom_scene
            call change_loc('livingroom')
            return
        else:
            return

    label school_on_time():
        call schoolbuilding_scene
        if late_oh_shit:
            $ current_hour = "08:00"
            "{i}Barely, but on time. Close call indeed!{/i}"
        else:
            call addtime(False,25)
            if int(current_hour[:2]) >= 8 and int(current_hour[4:]) > 0:
                $ school_walk_late_arrival = True
                call school_walk_late_arrival_event()
            else:
                "You arrive with plenty of time to spare before the bell rings"
                call school_finished()

    label school_finished():
        if detention_served:
            $ current_hour = "17:00"
        else:
            $ current_hour = "15:05"
            if school_hacker:
                if school_hacker_first_thought:
                    "{i}You've been thinking about what happened with your sister, and you were almost sure that it wouldn't be possible to manage that many mistakes by accident. Also, they hadn't found out who had updated the records... that's usually registered...{/i}"
                    $ school_hacker_first_thought = False
                fp "I should go talk to Natalie. She loves me, I'm sure I'll be able to get some answers from her!"
                menu:
                    "Go talk to Natalie, try to find out more about what happened to [shortfs]":
                        call talk_to_sCN()
                    "Nah, not today, I'll do it tomorrow instead":
                        pass
        "After school, you decide to just trek back home. No plans for today, and not that much interesting happening in town anyway"
        call evening_home()

    if school_walk_late_arrival:
        label school_walk_late_arrival_event(called=False):
            if called:
                "{i}Arriving at school, you can see that you're late{/i}\nYou hurry up the stairs, trying to get to your classroom as fast as humanly possible"
                sn "Greetings, [fp]!"
                "[sn]s voice sneaks up on you as you hurry through the hallways"
                "You turn around, and see [sn] standing in one of the doorways leading to the teacher's lounge"
                fp "[sn]! Hi! I was just..."
                sn "You're {b}late!{/b}"
                "[sn] cuts you off, snapping at you"
                fp "Yes, [sn], I am. I'm sorry, but..."
                sn "I don't care, [fp]. You're not hurt, it seems, and doesn't seem to be in any distress, so I'm just gonna assume that you're late because of tardiness. Detention!"
            call miss_novak_respond_detention()

    label miss_novak_punishment_late():
        call schoolbuilding_scene
        call addtime(False,25)
        sn "You're late! This will not be tolerated, [fP]. You will be on time, or I will be forced to reduce your grades for this semester! For now, you have detention, come meet me here after you're done with classes for today."
        
        label miss_novak_respond_detention():
            menu:
                "Yes, [sn]!":
                    $ statschangeNotify("sn_dom",-1,True)
                    $ statschangeNotify("sn_rel",1)
                    call miss_novak_detention()
                "Mouth off to [sn]":
                    fP "Oh, shut it! I'm a few minutes late. It's not like I do this often, and it wasn't like I tried to arrive late. Damn, \"reduce my grades\" - you know you'll have to give me a warning first, and even a letter that I might receive a reduced grade... and I have definitely not deserved that, yet"
                    sn "How dare you talk to me like that? Go see [sp] right now! I will not have a student talk to me like this!"
                    fP "Oh, stop pretending! You're not a bad-ass, [sn]. You never will be."
                    sn "{b}NOW!{/b}"
                    fP "Fine, fine..."
                    "You head to [sp]s office"
                    $ statschangeNotify("sn_dom",1.5,True)
                    $ statschangeNotify("sn_rel",-1,True)
                    $ statschangeNotify("sn_aro",1)
                    call principal_after_punishment_late()
    
    label talk_to_sCN():
        "Conversation with Natalie goes here"
        call evening_home()

    label evening_home():
        if day_week <= 4:
            call livingroom_scene
            if detention_served:
                $ current_hour = "17:45"
            else:
                $ current_hour = "15:30"
                $ n = renpy.random.randint(0,3)
                $ home_events = [
                    ["You arrive home. Nobody is there at the moment, it seems, as "+fmName.informal+"'s car is gone, and "+fsName.yourinformal+" is nowhere to be seen.",False],
                    ["When you arrive home, the door is locked, and you realise you've forgotten your key. Noone is answering the door when you try the doorbell, so both "+fmName.yourinformal+" and "+fmName.yourinformal+" must be out. You weren't really that keen on sitting outside all day, waiting for them, so you're pondering what else you can do instead",False],
                    ["Arriving home, you see "+fmName.yourinformal+"'s car in the driveway.",False],
                    ["When you arrive home, you catch a glimpse of "+fsName.yourformal+" by the pool, but "+fmName.yourformal+" is nowhere to be seen. Her car is still here, though.",True]
                ] # create more events here
                $ text = home_events[n][0]
                "[text]"
                if home_events[n][1] and fs_mad:
                    call firstday_talk_fs(True)
            
            if renpy.random.random() > .5:
                if  current_month >= 5 and current_month <= 8 and not detention_served:
                    "You decide to just lounge by the pool for a while, trying to stand the heat"
            else:
                if not detention_served:
                    if not mc_f:
                        "You decide that you can spend a few more hours on your bike today"
                        call garage_scene
                        call change_loc('garage')
                        call w_mc(True)
                        if current_hour[:2] > 19:
                            "You're feeling a bit tired, after school, and working on your bike, so you decide taking a shower will be a nice relief right now"
                            call taking_shower_evening()
                        else:
                            call garage_scene
                            call change_loc('garage')
                            call w_mc(True)
                            "After putting in a few more hours on the bike, you decide that the rest of the evening should be spent doing less arduous tasks, and head inside to watch some TV, maybe play some games"
                            call tv_vgames_evening()
                    else:
                        if renpy.random.random() > .65 and current_hour[:2] < 17:
                            "You decide to take a ride"
                            if (renpy.random.random() > .65 and nk_rel > 15) or (renpy.random.random() > .5 and nk_rel > 20):
                                "You decide to call up [nk] to see if she wants to come with"
                                nk ahead "Hi, [fp]"
                                fp "Hi, [nk]. I was wondering if you wanted to come for a ride with me today? Was thinking we could"
                                $ conditions.addcondition("Go to the cabin","current_month >= 9 and current_month <= 3 and has_cabin")
                                $ conditions.addcondition("Go to the marina","boat_at_marina")
                                menu:
                                    "Go to the beach":
                                        jump beach_ride
                                    "Ride to the next town over":
                                        jump next_town_ride
                                    "Go to the cabin":
                                        jump cabin_ride
                                    "Go to the marina":
                                        jump marina_ride
                            else:
                                "No answer. Oh well, you'll call her again some other time"
                        else:
                            "It's just not the day for outdoors activities, you decide to stay inside and just watch some TV instead"
                            if fp_sts > 0:
                                $ statschangeNotify("fp_sts",-1)
            if not evening_event:
                call end_of_day()
            else:
                call evening_event_label()

