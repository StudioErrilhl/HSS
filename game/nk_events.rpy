label nk_talk(event=False):
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
                            call travel_events('arrive_school')
                        "[text2]" if text2:
                            if bad_weather and rainstorm:
                                $ statschangenotify('nk_rel',-3)
                                $ renpy.pause(.25)
                                call school_events('sn_punishment_late')
                            else:
                                $ statschangenotify("nk_rel",-1)
                                $ renpy.pause(.25)
                                if renpy.random.random() < .35:
                                    call travel_events('arrive_school')
                                else:
                                    call school_events('sn_punishment_late')
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
                    call nk_walk_with(True)
                "Nah... I just wanna go by myself today, I got a lot on my mind, need to think a little bit":
                    show nk_standing annoyed with dissolve
                    $ renpy.pause(.5)
                    call travel_events('arrive_school')
                "No thanks, [nk]":
                    show nk_standing mad with dissolve
                    if nk_rel < 15:
                        $ nkrel = -.5
                    else:
                        $ nkrel = -.25
                    $ statschangenotify("nk_rel",nkrel)
                    $ renpy.pause(.5)
                    call travel_events('arrive_school')