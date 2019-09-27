label school_events(event=False):
    if event:
        if event == 'finished':
            if detention_served:
                $ current_time = "17:00"
            else:
                $ current_time = "15:05"
                call school_hacker_talk(True) from _call_school_hacker_talk
            "After school, you decide to just trek back home. No plans for today, and not that much interesting happening in town anyway"
            call change_loc('fp_outside',sec_call='evening_home',prev_loc=current_location) from _call_change_loc_54

        if event == 'sn_punishment_late':
            $ addtime(False,25)
            sn "You're late! This will not be tolerated, [fp]. You will be on time, or I will be forced to reduce your grades for this semester! For now, you have detention, come meet me here after you're done with classes for today."
            $ conditions.addcondition("Mouth off to [sn]","int(current_time[:2]) < 9")
            label respond_detention():
                menu:
                    "Mouth off to [sn]" (cs="evil"):
                        fp "Oh, shut it! I'm a few minutes late. It's not like I do this often, and it wasn't like I tried to arrive late. Damn, \"reduce my grades\" - you know you'll have to give me a warning first, and even a letter that I might receive a reduced grade... and I have definitely not deserved that, yet"
                        sn "How dare you talk to me like that? Go see [sp] right now! I will not have a student talk to me like this!"
                        fp "Oh, stop pretending! You're not a bad-ass, [sn]. You never will be."
                        sn "{b}NOW!{/b}"
                        fp "Fine, fine..."
                        "You head to [sp]s office"
                        $ statschangenotify("sn_dom",1.5,True)
                        $ statschangenotify("sn_rel",-1,True)
                        $ statschangenotify("sn_aro",1)
                        call school_events('punishment') from _call_school_events_8
                    "Yes, [sn]!" (cs="good"):
                        $ statschangenotify("sn_dom",-1,True)
                        $ statschangenotify("sn_rel",1)
                        call school_events('detention') from _call_school_events_7

        if event == 'punishment':
            $ addtime(1, False)
            call school_po_scene from _call_school_po_scene
            sp "[fp]! What have you done, to be sent to me?"
            fp "I mouthed off to Miss Novak."
            fp "She was yelling at me for being late, and I just lost it."
            fp "I'm sorry."
            sp "You need to control your temper, son."
            sp "You have a tendency to end up in these situations, and I don't think we can ignore it much longer."
            $ statschangenotify("fp_att",.5,True)
            $ statschangenotify("punishment_late",1)
            if punishment_late >= 5:
                sp "I will need to call your parents, and tell them about this."
                $ statschangenotify("fm_rel",-2.5)
            sp "You will report to [sn] after your regular hours today."
            sp "I'm sure she already informed you that you would serve detention today..."
            fp "Well..."
            sp "{i}Your principal shoots you a stern look{/i}\n"
            extend "You can go, [fp]"
            call schoolbuilding_scene from _call_schoolbuilding_scene_1
            $ after_principal_talk = True
            call school_events('detention') from _call_school_events_9

        if event == 'detention':
            if after_principal_talk:
                "You go about your daily tasks as normal, but come end of day, you know you have to go meet [sn] for your detention. You head off towards your classroom..."
            else:
                "After having dealth with [sn]s blow-out, you go about your day as normal - attending classes, avoiding freshmen, trying to catch a glance of the cheerleaders rehearsing..."
                "But, come end of day, you need to get your ass to [sn]s classroom, and serve detention."
            $ settime(15,5)
            $ detention_served = True
            if sn_rel > 15 or sn_aro > 10:
                if renpy.random.random() > .5:
                    "Arriving at room 603, you see [sn] standing by her desk, looking sternly at you. Her top two buttons are unbuttoned, showing a hint of cleavage. You have to do a double take, forcing yourself not to stare"
                    menu:
                        "Stare":
                            if sn_aro > 15:
                                "You notice [sn] catching you staring, but she just lets you know, giving you a long look, but doesn't do anything about it"
                                $ statschangenotify("sn_aro",1)
                                "You are pondering if you should try to catch a better view..."
                                menu:
                                    "Sit down, and try looking up her skirt":
                                        $ snd_r = renpy.random.random()
                                        if sn_aro > 15 and sn_rel > 10 and snd_r > .5:
                                            "You notice [sn] again catching your glance, but this time she just slides her legs a little further apart, making you shift a little uncomfortably in your chair"
                                            $ statschangenotify("sn_aro",1)
                                        else:
                                            "[sn] abruptly stands up, and marches over to where you're sitting."
                                            sn "Have you had your fill for today, [fp]? Do you think you might wanna keep your eyes to yourself? If not, I'm sure we can find some kind of punishment you'll appreciate! Or, rather, that {i}I{/i} will appreciate!"
                                            fp "That... won't be necessary, [sn]"
                                            $ statschangenotify("sn_aro",.5,True)
                                            $ statschangenotify("sn_rel",-.5)
                                        call school_events('finished') from _call_school_events_10
                                    "Sit down, but refrain from peeping up her skirt":
                                        jump sn_lookaway_detention
                            else:
                                "You notice [sn] catching your glance, and feel her ice-cold stare as she haughtily asks you if you're done undressing her with your eyes"
                                sn "You're gonna get another punishment for that, [fp]. Meet here after school tomorrow, for another round of detention!"
                                $ statschangenotify("sn_aro",.5,True)
                                $ statschangenotify("sn_rel",-1)
                        "Manage to look away":
                            jump sn_lookaway_detention
                    label sn_lookaway_detention():
                        "You decide to play it cool, and just get the detention done with, so you can go home"
                        call school_events('finished') from _call_school_events_11
                else:
                    "Arriving at room 603, you see [sn] standing by her desk, clearly waiting for the last arrival for today."
                    sn "Glad you could make it, [fp]. Sit down and get out your books. I'm assuming you have homework or studying to do?"
                    fp "I do, [sn]."
                    if not backpack.has_item(schoolbooks_item):
                        sn "What are you waiting for, [fp]? I told you to get your books out!"
                        fp "I... I seem to have forgotten them at home..."
                        sn "What?!"
                        sn "Can't you even remember something basic, like your books?"
                        sn "Fine! Go to the library, and do your studying there! And don't forget your books again!"
                        fp "Okay..."
                        $ statschangenotify('sn_rel',-1,True)
                        $ statschangenotify('fp_att',-1)
                        "You head over to the library, to see if you can find a copy of your books there, and actually get some stuff done today"
                        call school_events('finished') from _call_school_events_12
                    else:
                        "You get out your books, and start studying for next weeks algebra-test"
                        call school_events('finished') from _call_school_events_13
            else:
                "Arriving at room 603, you see [sn] standing by her desk, clearly waiting for the last arrival for today."
                sn "Glad you could make it, [fp]. Sit down and get out your books. I'm assuming you have homework or studying to do?"
                fp "I do, [sn]."
                if not backpack.has_item(schoolbooks_item):
                    sn "What are you waiting for, [fp]? I told you to get your books out!"
                    fp "I... I seem to have forgotten them at home..."
                    sn "What?!"
                    sn "Can't you even remember something basic, like your books?"
                    sn "Fine! Go to the library, and do your studying there! And don't forget your books again!"
                    fp "Okay..."
                    $ statschangenotify('sn_rel',-1,True)
                    $ statschangenotify('fp_att',-1)
                    "You head over to the library, to see if you can find a copy of your books there, and actually get some stuff done today"
                    call school_events('finished') from _call_school_events_14
                else:
                    "You get out your books, and start studying for next weeks algebra-test"
                    call school_events('finished') from _call_school_events_15