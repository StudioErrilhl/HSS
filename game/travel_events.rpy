label travel_events(event=False):
    if event:
        if event == 'travel_school':
            if 6 <= int(current_time[:2]) <= 8 and day_week <= 4:
                if shitty_morning and int(current_time[:2]) <= 7:
                    nk ahead "Hi [fp]! You wanna ride to school?"
                    if not nk_driving:
                        fp "Hi [nk]... Didn't know you drove?"
                        nk ahead "My mom got me this for my birthday. Haven't really driven it much, but it's awesome."
                        $ nk_driving = True
                    else:
                        fp "Hi [nk]"
                    if bad_weather and rainstorm:
                        $ text1 = "Sure! That way I won't be late, not to mention drowning by the time I get there!\n{i}Damn, she saved my scrawny ass. Don't understand why she gets so much flak at school, she's nice...{/i}"
                        $ text2 = False
                    else:
                        $ text1 = "Sure! Then I won't be late!\n{i}Who cares if "+nk.name+" is not one of the popular kids - her offer is nice{/i}"
                        $ text2 = "No thanks! I'll just walk. Don't really wanna trust my life to your driving!\n{i}Don't wanna be caught dead in the same car as "+nk.name+"...{/i}"
                    if text1 or text2:
                        menu:
                            "[text1]" if text1:
                                $ statschangenotify("nk_rel",1.5)
                                $ renpy.pause(.25)
                                $ nk_sa_status = ['happy','drive']
                                call travel_events('arrive_school') from _call_travel_events_5
                            "[text2]" if text2:
                                if bad_weather and rainstorm:
                                    $ statschangenotify('nk_rel',-3)
                                    $ renpy.pause(.25)
                                    $ nk_sa_status = ['mad','drive']
                                    call travel_events('arrive_school') from _call_travel_events_6
                                else:
                                    $ statschangenotify("nk_rel",-1)
                                    $ renpy.pause(.25)
                                    $ nk_sa_status = ['annoyed','drive']
                                    if renpy.random.random() < .35:
                                        call travel_events('arrive_school') from _call_travel_events_7
                                    else:
                                        call school_events('sn_punishment_late') from _call_school_events_2
                elif not shitty_morning and int(current_time[:2]) <= 7 and renpy.random.random() < .5:
                    show nk_standing ahead with dissolve
                    nk ahead "Hi [fp]! Wanna walk to school with me?"
                    menu:
                        "Sure, [nk]":
                            show nk_standing smile with dissolve
                            if nk_rel < 15:
                                $ nkrel = 1
                            else:
                                $ nkrel = .5
                            $ statschangenotify("nk_rel",nkrel)
                            call nk_walk_with(True) from _call_nk_walk_with_1
                        "Nah... I just wanna go by myself today, I got a lot on my mind, need to think a little bit":
                            show nk_standing annoyed with dissolve
                            $ renpy.pause(.5)
                            call travel_events('arrive_school') from _call_travel_events_8
                        "No thanks, [nk]":
                            show nk_standing mad with dissolve
                            if nk_rel < 15:
                                $ nkrel = -.5
                            else:
                                $ nkrel = -.25
                            $ statschangenotify("nk_rel",nkrel)
                            $ renpy.pause(.5)
                            call travel_events('arrive_school') from _call_travel_events_9
                elif not shitty_morning and renpy.random.random() > .75:
                    $ t_w = [(0,6),(1,6),(2,1),(3,3)] # travel events weights
                    $ t_e = [ # travel events
                        ["see something",False,"You cross the street, trying to get a better look","Forget about it",False,30],
                        ["hear a loud noise coming from an alleyway to your right",False,"You enter the alleyway, trying to figure out where the sound came from","Forget about it",False,30],
                        ["feel cold","Shake off the feeling of dread suddenly coming over you","There is no reason for you to feel like that, and you're not superstitous in the least - you still want to figure out what that was","You ignore it, and keep going",False,False],
                        ["remember that you forgot your books",False,"Turn back, and go fetch your books","Decide to go anyway, you don't have time to go back to get them",1,False]
                    ]
                    $ w_e = weighted_choice(t_w)
                    $ s_e = t_e[w_e]
                    $ text = "You're walking to school, when you suddenly {0}".format(s_e[0])
                    "[text]"
                    menu:
                        "[s_e[1]]" if s_e[1]:
                            pass
                        "[s_e[2]]":
                            if s_e[4]:
                                $ addtime(s_e[4])
                            if s_e[5]:
                                $ addtime(False,s_e[5])
                            $ event = "arrive_school"
                            call travel_events(event) from _call_travel_events_10
                        "[s_e[3]]":
                            $ event = "arrive_school"
                            call travel_events(event) from _call_travel_events_11
                else:
                    $ event = "arrive_school"
                    call travel_events(event) from _call_travel_events_12
            else:
                $ event = "arrive_school"
                call travel_events(event) from _call_travel_events_13
        elif event == "arrive_school":
            $ current_location = 'schoolbuilding_loc'
            call schoolbuilding_scene from _call_schoolbuilding_scene
            if late_oh_shit:
                $ current_time = "08:00"
                "Barely, but on time. Close call indeed!"
            else:
                $ addtime(False,25)
                if int(current_time[:2]) >= 8 and int(current_time[3:]) >= 0:
                    # call school_walk_late_arrival_event(True)
                    if (int(current_time[3:]) <= 10 and renpy.random.random() < .25) or int(current_time[3:]) > 10:
                        "{i}Arriving at school, you can see that you're late{/i}\nYou hurry up the stairs, trying to get to your classroom as fast as humanly possible"
                        sn "Greetings, [fp]!"
                        "[sn]s voice sneaks up on you as you hurry through the hallways"
                        "You turn around, and see [sn] standing in one of the doorways leading to the teacher's lounge"
                        fp "[sn]! Hi! I was just..."
                        sn "You're {b}late!{/b}"
                        "[sn] cuts you off, snapping at you"
                        fp "Yes, [sn], I am. I'm sorry, but..."
                        sn "I don't care, [fp]. You're not hurt, it seems, and doesn't seem to be in any distress, so I'm just gonna assume that you're late because of tardiness. Detention!"
                        call respond_detention() from _call_respond_detention
                    else:
                        "You arrive a little too late, but fortunately, you manage to sneak into class without anyone spotting you"
                        call school_events('finished') from _call_school_events_3
                else:
                    if int(current_time[:2]) == 7 and int(current_time[3:]) < 55:
                        if int(current_time[3:]) < 45:
                            "You arrive with plenty of time to spare before the bell rings"
                            if nk_sa_status and nk_sa_status[0] == 'happy' and nk_sa_status[1] == 'drive':
                                if nk_rel > 20:
                                    nk "So... {i}She's sitting there, a bit nervous, it seems...\n\nSuddenly, she leans over the gearshift, and, catching you entirely by surprise, french-kisses you for about 2 minutes{/i}"
                                    menu:
                                        "Kiss her back":
                                            $ statschangenotify('nk_rel',2)
                                        "Tell her to get off":
                                            $ statschangenotify('nk_rel',-4)
                                        "Push her away, gently":
                                            $ statschangenotify('nk_rel',0)
                                    call school_events('finished') from _call_school_events_4
                                else:
                                    if rainstorm:
                                        fp "Thanks, [nk]! I would've drowned out there on my own"
                                        nk smile "Oh, no, you wouldn't, you doofus. You're just lazy, and happy someone drove you!"
                                        menu:
                                            "Compliment her":
                                                pass
                                            "Tease her":
                                                pass
                                            "Dismiss her":
                                                pass
                                    else:
                                        fp "Thanks for the ride, [nk]!"
                                        nk "You're welcome, [fp]!"
                                    call school_events('finished') from _call_school_events_5
                        else:
                            "You arrive, with just a few minutes left before the bell rings"
                    elif int(current_time[:2]) < 7:
                        "You arrive way too early, but decide to just hang around and wait for school to start"
                    else:
                        "You barely arrive on time, but you're still in the door before the bell rings"
                    call school_events('finished') from _call_school_events_6



label nk_walk_with(nkww_called=False):
    if nkww_called:
        $ nkww_called = False
        show nk_standing smile with dissolve
        "[fp] starts walking with [nk] towards their school, talking about everything and nothing. It's a nice day, and [nk] is, as always, nice to be around"
        if nk_rel > 5:
            fp "So, did you finish the assignment yet?"
            if renpy.random.random() > .5:
                nk ahead "Yeah, I did. Wasn't that much work, so I finished it last night. Why?"
                fp "Well... I was hoping you'd lemme look at your assignment, maybe gimme a few pointers. I'm a bit lost"
                if nk_rel > 15:
                    show nk_standing smile_open with dissolve
                    nk smile_open "Sure. How about I come over after school, and we can look at it together?"
                    fp "That would be awesome, [nk]! Thanks a million"
                    nk devious "Oh, you'll make it up to me... ;)"
                    $ nk_sa_status = ['happy','walk']
                    call travel_events('arrive_school') from _call_travel_events_14
                else:
                    show nk_standing annoyed with dissolve
                    nk annoyed "I don't think so, [fp]. Wouldn't feel right you looking at my work..."
                    "Seems your relationship with [nk] isn't strong enough to ask her for help yet"
                    $ nk_sa_status = ['annoyed','walk']
                    call travel_events('arrive_school') from _call_travel_events_15
            else:
                show nk_standing sad with dissolve
                nk sad "No, I haven't even started yet. There is so much schoolwork, and I'm behind on studying for finals... {i}she trails off, looking a bit troubled{/i}"
                fp "How about you come over to my house this evening, and we can work on it together?"
                show nk_standing smile with dissolve
                nk smile "Oh, that would be nice. Sure, I can do that. Let's say around seven?"
                fp "Sure, that works for me. I'll be working on my bike till then"
                $ statschangenotify("nk_rel",.5)
                $ nk_sa_status = ['happy','walk']
                $ evening_event = True
                $ nk_school_assignment_evening = True
                call travel_events('arrive_school') from _call_travel_events_16
        else:
            call travel_events('arrive_school') from _call_travel_events_17
