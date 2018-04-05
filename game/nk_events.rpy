label nk_talk(event=False,callrand=False):
    if event:
        $ text1 = text2 = False
        $ nktr = renpy.random.random()
        if event == 'ride':
            if int(current_time[:2]) <= 7:
                nk ahead "Hi [fp]! You wanna ride to school?"
                if not nk_driving:
                    fp "Hi [nk]... Didn't know you drove?"
                    nk ahead "My mom got me this for my birthday. Haven't really driven it much, but it's awesome."
                    $ nk_driving = True
                else:
                    fp "Hi [nk]"
                if bad_weather and rainstorm:
                    $ text1 = "Sure! That way I won't be late, not to mention drowning by the time I get there!\n{i}Damn, she saved my scrawny ass. Don't understand why she gets so much flak at school, she's nice...{/i}"
                else:
                    $ text1 = "Sure! Then I won't be late!\n{i}Who cares if [nk] is not one of the popular kids - her offer is nice{/i}"
                    $ text2 = "No thanks! I'll just walk. Don't really wanna trust my life to your driving!\n{i}Don't wanna be caught dead in the same car as [nk]...{/i}"
                if text1 or text2:
                    menu:
                        "[text1]" if text1:
                            $ statschangenotify("nk_rel",1.5)                                    
                            $ renpy.pause(.25)
                            call travel_events('arrive_school') from _call_travel_events_1
                        "[text2]" if text2:
                            if bad_weather and rainstorm:
                                $ statschangenotify('nk_rel',-3)
                                $ renpy.pause(.25)
                                call school_events('sn_punishment_late') from _call_school_events
                            else:
                                $ statschangenotify("nk_rel",-1)
                                $ renpy.pause(.25)
                                if renpy.random.random() < .35:
                                    call travel_events('arrive_school') from _call_travel_events_2
                                else:
                                    call school_events('sn_punishment_late') from _call_school_events_1
        elif event == 'nk_date' and not nk_mad and not nke:
            if not nk_first_date:
                nk "Hey, [fp]"
                "You can hear the smile in her voice"
                fp "Hey, [nk]"
                "..."
                nk "[fp]... are you there?"
                fp "Yeah, I'm here..."
                nk "So...?"
                fp "Sorry, I suck at this!"
                nk "What? Talking?"
                "You can hear her teasing you"
                nk "So, lemme make this easier on you, [fp]"
                fp "... okay?"
                nk "You wanna go get a burger or something? Maybe see if you're better at talking in person than over the phone?"
                fp "Sure! {i}Damn... too eager!{/i}"
                "[nk]s cute laugh sounds through the phone"
                $ text = "Fine! We'll go {0}!".format('this Saturday' if (day_week <= 4 or day_week == 6) else 'tomorrow')
                nk "[text]"
                fp "Great! I will see if I can borrow the car, and pick you up around 18?"
                nk "Sounds great!"
                $ calling = duringcall = False
                $ nk_first_date = True
                $ nk_day_date = current_month_day + (6 - day_week)
                if nk_day_date == current_month_day:
                    $ nk_day_date += 6
                $ renpy.hide_screen('phone')
                $ call_nk_event = False
                call change_loc(current_location) from _call_change_loc_78
        elif nktr < .5 and day_week <= 4 and not shitty_morning:
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
                    call nk_walk_with(True) from _call_nk_walk_with
                "Nah... I just wanna go by myself today, I got a lot on my mind, need to think a little bit":
                    show nk_standing annoyed with dissolve
                    $ renpy.pause(.5)
                    call travel_events('arrive_school') from _call_travel_events_3
                "No thanks, [nk]":
                    show nk_standing mad with dissolve
                    if nk_rel < 15:
                        $ nkrel = -.5
                    else:
                        $ nkrel = -.25
                    $ statschangenotify("nk_rel",nkrel)
                    $ renpy.pause(.5)
                    call travel_events('arrive_school') from _call_travel_events_4