# label after_fs_mad_morning(afs_mad=False):
label nk_talk(nkt_called=False):
    # if afs_mad:
    if nkt_called:
        $ nkt_called = False
        # $ afs_mad = False
        $ text1 = text2 = False
        $ nktr = renpy.random.random()
        # $ afsmm_r = renpy.random.random()
        # if debug:
        #     $ renpy.watch(str(afsm_r))
        if nktr < .5 and day_week <= 4 and shitty_morning:
        # if afsmm_r < .5 and shitty_morning and day_week <= 4:
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
                    # $ text2 = "No thanks, [nk]. I've got a buddy picking me up, he'll be here soon.\n{i}Even in this weather I'm not gonna get in a car with her... I'd never hear the end of it at school{/i}"
                else:
                    $ text1 = "Sure! Then I won't be late!\n{i}Who cares if [nk] is not one of the popular kids - her offer is nice{/i}"
                    $ text2 = "No thanks! I'll just walk. Don't really wanna trust my life to your driving!\n{i}Don't wanna be caught dead in the same car as [nk]...{/i}"
                if text1 or text2:
                    menu:
                        "[text1]" if text1:
                            $ statschangenotify("nk_rel",1.5)                                    
                            $ renpy.pause(.25)
                            call school_on_time(True)
                        "[text2]" if text2:
                            if bad_weather and rainstorm:
                                $ statschangenotify('nk_rel',-3)
                                $ renpy.pause(.25)
                                call sn_punishment_late(True)
                            else:
                                $ statschangenotify("nk_rel",-1)
                                $ renpy.pause(.25)
                                if renpy.random.random() < .35:
                                    call school_walk_late(True)
                                else:
                                    call sn_punishment_late(True)
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
                    call school_on_time(True)
                "No thanks, [nk]":
                    show nk_standing mad with dissolve
                    if nk_rel < 15:
                        $ nkrel = -.5
                    else:
                        $ nkrel = -.25
                    $ statschangenotify("nk_rel",nkrel)
                    $ renpy.pause(.5)
                    call school_on_time(True)