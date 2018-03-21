label morning_events():
    #this is a wrapping label for morning events
    if int(current_time[:2]) in morning and not morning_event_done:
        call fp_bedroom_scene from _call_fp_bedroom_scene_2
        $ fpmc_r = renpy.random.random()
        if (fpmc_r < .35 and day_week <= 4 and overslept and int(current_time[:2]) > 7) or (int(current_time[:2]) > 7 and day_week <= 4):
            $ overslept = False
            show fm_standing mad with dissolve
            fm mad "[fp]! Wake UP!"
            fp "uuuhh..."
            fm mad "[fp]! Get out of bed THIS INSTANT!"
            $ conditions.addcondition("[fmName.Informal]! Shut up! I'm awake, and getting up!","fm_rel >= 15 and fm_dom >= 20")
            $ conditions.addcondition("Yeez, [fmName.informal]! Stop nagging me, will you? I'm gonna get up in a second","fm_rel >= 5")
            menu:
                "[fmName.Informal]! Shut up! I'm awake, and getting up!":
                    call fm_morningchoice_dom(True) from _call_fm_morningchoice_dom
                "Yeez, [fmName.informal]! Stop nagging me, will you? I'm gonna get up in a second":
                    call fm_morningchoice_reldom(True) from _call_fm_morningchoice_reldom
                "Okay, [fmName.informal]... I'm up, I'm up. Please don't yell":
                    call fm_morningchoice_rel(True) from _call_fm_morningchoice_rel
            $ conditions.clear()

            label fm_morningchoice_dom(called=False):
                if called:
                    if fm_dom < 25:
                        $ statschangenotify("fm_dom",2)
                        pass
                    if fm_dom >= 25:
                        $ statschangenotify("fm_dom",.5)
                        pass
                    else:
                        $ statschangenotify("fm_dom",-.5)
                        pass
                    $ fm_choice1_choice = "dom"
                    $ addtime(False, 10)
                    fm mad "Don't talk to me like that! I'm your [fmName.role]! You respect me, you hear?"
                    if fm_dom >= 45:
                        fp "[fmName.Formal]! *You bark at her*"
                        fp "Get your fat ass over here right this instant!"
                        "[fmName.yourrole] hurries over to you, eyes downcast, not wanting to anger you further"
                        fp "What did you just say to me?"
                        fm sad "I'm... I'm sorry. I didn't mean to raise my voice. I'm just a bit stressed..."
                        fp "Stop it! I don't wanna hear it! Get down!"
                        "[fmName.name] stares at you, bewildered. Down...?"
                        "You grab her shoulder, and push her down, hard, so that she lands on her knees"
                        fm crying "*OUCH!*"
                        fp "Shut it!"
                        "She shuts her mouth immediately, recognizing the mood you're in"
                        $ addtime(False,15)
                        fp "Are you just gonna sit there? I'm already late for school. Shouldn't you be getting on with your apology by now?"
                        fm blushing "You want me to...?"
                        $ conditions.addcondition("Tell her to pull down her pants and present her ass to you","fm_dom >= 40")
                        $ conditions.addcondition("Tell her to sit back and spread her pussy for you","fm_dom >= 30")
                        menu:
                            "Tell her to pull down her pants and present her ass to you":
                                $ statschangenotify("fm_dom",2,True)
                                $ statschangenotify("fm_anal",1)
                                if fm_anal >= 10 and fm_anal >= fm_pussy:
                                    $ statschangenotify("fm_anal",1)
                                    call morning_assfuck() from _call_morning_assfuck
                                elif fm_anal >= 10 and fm_anal <= fm_pussy:
                                    fm blushing "Do you really wanna fuck my ass?"
                                    menu:
                                        "Yes":
                                            call morning_assfuck() from _call_morning_assfuck_1
                                        "No":
                                            call morning_pussyfuck() from _call_morning_pussyfuck
                                else:
                                    fm ahead "What are you going to do?\n{i}Her voice shakes a little bit{/i}"
                                    fp "Oh, I dunno... *you slap her ass, hard*"
                                    $ statschangenotify("fm_dom",1)
                                    fm crying "{b}OUCH!{/b}"
                                    fp "Shut up!\n{b}you slap her again{/b}"
                                    "Getting turned on by her sounds, and the spanking in general, you continue, till she begs for mercy"
                                    fm crying "{b}PLEASE!{/b}\nStop it.\n{i}Tears are streaming down her face{/i}"
                                    $ statschangenotify("fm_rel",-1,True)
                                    $ statschangenotify("fm_dom",1.5)
                                    "You stop, looking over her ass, which is reddening nicely"
                                    fp "Get up, get dressed, and get out of my room"
                                    fm ahead_eyes_closed "Okay... {i}she meekly replies, staring into the ground{/i}"
                            "Tell her to sit back and spread her pussy for you":
                                $ statschangenotify("fm_dom",1.5,True)
                                $ statschangenotify("fm_pussy",1)
                                if fm_pussy >= 10 and fm_pussy >= fm_bj:
                                    $ statschangenotify("fm_pussy",1)
                                    call morning_pussyfuck() from _call_morning_pussyfuck_1
                                elif fm_pussy >= 10 and fm_pussy <= fm_bj:
                                    fm ahead "Do you want my pussy, or do you want a blowjob?"
                                    menu:
                                        "Pussy":
                                            call morning_pussyfuck() from _call_morning_pussyfuck_2
                                        "Blowjob":
                                            call morning_bj() from _call_morning_bj
                                        "How about both?":
                                            call morning_pussy_bj() from _call_morning_pussy_bj
                                else:
                                    "You watch as [fmName.yourshort] hitches her thumbs under her panties and swiftly pulls them down over her thighs. She's got shapely legs, not at all bad for a woman in her forties. She pulls up her skirt, and sits back on the bed, spreading her legs as she does so."
                                    fm ahead "Happy now? {i}There's still a bit of defiance in her voice, some residual want to fight you, to stand up for herself{/i}"
                                    fp "Not quite. I would love to introduce my cock to your pussy, but I don't have time. Start masturbating!"
                                    fm blushing "{b}Gasp{/b} You... you want me to... rub... rub my pussy... here? In... in front of you?"
                                    fp "Yes, I though I made myself pretty clear? If it was possible to misunderstand, I apologize. Let's see... \"{b}rub your pussy! Until you cum{/b}"
                                    "You can see her hesitating. The emotions play over her face, making it clear that she's weighing the options, carefully."
                                    "You look at your watch, realising you're gonna be late."
                                    $ addtime(False,40)
                                    fp "Fuck!"
                                    "Your outburst startles [fmName.yourshort] - she looks at, you, a bit worried"
                                    fp "I would love to continue this, but I'm gonna be late for school. That shouldn't prevent {b}you{/b} from enjoying yourself, though. Finish up. Then send me a picture when you're done!"
                                    "With that, you leave [fmName.yourshort], half naked, on your bed, and head for the door"
                                    hide fm_standing
                                    call late_morning() from _call_late_morning
                            "Tell her to get your cock out and start sucking":
                                $ statschangenotify("fm_dom",1,True)
                                $ statschangenotify("fm_bj",1)
                                if fm_bj >= 10:
                                    $ statschangenotify("fm_bj",1)
                                    call morning_bj() from _call_morning_bj_1
                                elif fm_bj >= 10 and fm_bj <= fm_pussy:
                                    fm ahead "Do you want a blowjob, or do you want my pussy?"
                                    menu:
                                        "Blowjob":
                                            call morning_bj() from _call_morning_bj_2
                                        "Pussy":
                                            call morning_pussyfuck() from _call_morning_pussyfuck_3
                                        "How about both?":
                                            call morning_pussy_bj() from _call_morning_pussy_bj_1
                                else:
                                    "This is a placeholder for the morning event for fm_dom above 45"
                    elif fm_dom >= 30:
                        fp "Hell no, [fmName.informal]! You've lost that. I'm the one in charge here now."
                        fm ahead_eyes_closed "... Yes, [fp] ... "
                        "{i}[yourCapsfM] looks down at the floor, a slight blush on her cheeks, clearly uncomfortable with the situation. Maybe also a little afraid. Not really of you, but that she's excited, just a slight stirring in her loins, by all this...{/i}"
                        $ statschangenotify("fm_aro",1)
                        fm ahead_eyes_closed "... You're in charge. What will you have me do?"
                        menu:
                            "Screw school, I can be late for once. Strip!":
                                $ statschangenotify("fm_dom",1,True)
                                $ statschangenotify("fm_cor",1,True)
                                $ statschangenotify("fm_rel",-5)
                                hide fm_standing
                                call morning_strip() from _call_morning_strip
                            "{b}I'll be late for school{/b}":
                                hide fm_standing
                                call late_morning() from _call_late_morning_1
                            "Have your mom drive you to school, and make sure you're not late":
                                $ statschangenotify("fm_dom",.5)
                                hide fm_standing
                                call drive_to_school() from _call_drive_to_school
                    elif fm_dom >= 20:
                        fp "Oh, shut it, [fmName.name]. \"Respect\". Don't make me laugh!"
                        fm ahead_eyes_closed "{b}her lip quivering...{/b} don't... just... you're gonna be late..."
                        fp "Where are you going? Come right back here and apologize!"
                        "[fmName.name] slowly turns, shuffles back towards you and, in a barely audible whisper..."
                        fm ahead_eyes_closed "I'm sorry, [fp]. I apologize for my behavior"
                        fp "Fine. Don't let it happen again!"
                        $ fm_apologize = True
                        $ addtime(False,10)
                        "[yourCapsfM] walks out of the room"
                        $ morning_event_done = True
                        hide fm_standing
                        call late_morning() from _call_late_morning_2

            label fm_morningchoice_reldom(called=False):
                if called:
                    $ called = False
                    if fm_dom < 25:
                        $ statschangenotify("fm_dom",.5,True)
                        $ statschangenotify("fm_rel",.5)
                    $ fm_choice1_choice = "reldom"
                    if int(current_time[3:]) == 0:
                        $ already_late = True
                        fm ahead "You're late. School just started!"
                    else:
                        if int(current_time[:2]) <= 8:
                            if int(current_time[:2]) == 8:
                                $ tt = abs(int(current_time[3:]))
                                fm ahead "You're late. School started [tt] minutes ago"
                            else:
                                $ tl = abs(int(current_time[3:])-60)
                                fm ahead "You're gonna be late. School starts in [tl] minutes."
                        else:
                            $ already_late = True
                            $ th = abs(int(current_time[:2])-8)
                            $ text = "You're late. School started over {0} {1} ago".format(th,'hours' if th > 1 else 'hour')
                            fm ahead "[text]"
                    fp "Yes, yes, I know. Just... let me get dressed, and take a shower, okay?"
                    fm ahead "Fine! I'm going to work. Make sure you lock the door when you leave!"
                    $ morning_event_done = True
                    call change_loc('fp bedroom') from _call_change_loc_33

            label fm_morningchoice_rel(called=False):
                if called:
                    $ called = False
                    if fm_rel < 25:
                        $ statschangenotify("fm_rel",1.5)
                    elif fm_rel < 40:
                        $ statschangenotify("fm_rel",1)
                    else:
                        $ statschangenotify("fm_rel",.25)
                    fm ahead "You need to stop staying up all night, [fp]. If you can't get out of bed in the morning, you'll fail both school and work, when that time comes."
                    fp "You know that there are jobs where you work both evenings and nights, right [fmName.informal]?"
                    fm ahead "Of course I do! But that doesn't mean that you should aim for those jobs. Now get your ass in gear!"
                    $ addtime(False,10)
                    if int(current_time[3:]) == 0:
                        $ already_late = True
                        fm ahead "You're late. School just started!"
                    else:
                        if int(current_time[:2]) <= 8:
                            if int(current_time[:2]) == 8:
                                $ tt = abs(int(current_time[3:]))
                                fm ahead "You're late. School started [tt] minutes ago"
                            else:
                                $ tl = abs(int(current_time[3:])-60)
                                fm ahead "You're gonna be late. School starts in [tl] minutes."
                        else:
                            $ already_late = True
                            $ th = abs(int(current_time[:2])-8)
                            $ text = "You're late. School started over {0} {1} ago".format(th,'hours' if th > 1 else 'hour')
                            fm ahead "[text]"
                    $ morning_event_done = True
                    call late_morning() from _call_late_morning_3
        elif fpmc_r < .75:
            $ overslept = False
            if not backpack.has_item(schoolbooks_item):
                if day_week <= 4:
                    if debug:
                        "test books on dresser"
                    show books_on_dresser
            show fm_standing ahead with dissolve
            fm ahead "[fp], time to get out of bed and have some breakfast"
            fp "Sure, [fmName.informal] - I'll be right down"
            hide fm_standing
            $ breakfast_jump = True
            call fp_bedroom_loc(True) from _call_fp_bedroom_loc_3
        else:
            $ overslept = False
            $ current_time = "06:00"
            if not backpack.has_item(schoolbooks_item):
                if day_week <= 4:
                    show books_on_dresser
            fp "{b}Yawn{/b}"
            fp "{i}What time is it...?{/i}"
            if int(current_time[:2]) == 6 and day_week <= 4:
                if not mc_f:
                    fp "{i}Oh, it's really early... oh well, lets get up, maybe I can do some work on the bike before school{/i}"
                    call change_loc('garage') from _call_change_loc_34
                    fp "{i}Oh, I better get going, if I'm gonna be on time{/i}"
                    call entrance_loc() from _call_entrance_loc_2
                else:
                    fp "{i}I should take the bike. It's a nice day for a ride anyways{/i}"
                    ## depending on the relationship with nk, there should be a possibility of her joining the ride to school
            elif int(current_time[:2]) == 6 and day_week >= 5:
                if not mc_f:
                    fp "Oh, it's really early... oh well, maybe I can get an early start and work on the bike today"
                    call garage_scene from _call_garage_scene
                    call change_loc('garage') from _call_change_loc_35
                    call w_mc(True) from _call_w_mc
                    $ early_morning_we = True
                    $ addtime(False,15)
                else:
                    fp "Hm... really nice weather today, maybe I should take a ride"
            $ breakfast_jump = True
            $ shitty_morning = False
            $ morning_event_done = True
    label morning_strip(fm_ms_called=False):
        if fm_ms_called:
            $ fm_ms_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning strip"
    label drive_to_school(fm_ds_called=False):
        if fm_ds_called:
            $ fm_ds_called = False
            $ late_oh_shit = True
            call travel_events('arrive_school') from _call_travel_events_18
    label morning_assfuck(fm_ma_called=False):
        if fm_ma_called:
            $ fm_ma_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning AF"
    label morning_pussyfuck(fm_mp_called=False):
        if fm_mp_called:
            $ fm_mp_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning PF"
    label morning_pussy_bj(fm_mpbj_called=False):
        if fm_mpbj_called:
            $ fm_mpbj_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning PFBJ"
    label morning_bj(fm_mbj_called=False):
        if fm_mbj_called:
            $ fm_mbj_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning BJ"

    if skip_breakfast:
        label skip_breakfast(called=False):
            $ skip_breakfast = False
            if called:
                $ called = False
                $ addtime(False,30)
                fp "{i}Deciding to skip breakfast, to avoid uncomfortable incidents with [fsName.myformal], I go straight to the garage.{/i}"
                call garage_scene from _call_garage_scene_1
                if not mc_f:
                    fp "Ah, at least working on my bike tends to get my mind off things."
                    label firstday_mc_work:
                        menu:
                            "Hm. Working on the bike usually calms me a bit, I might be able to get some work done today":
                                label firstday_mc_work_internal():
                                if count < 3:
                                    fp "{i}Damn... I just can't get that image out of my head...{/i}\nI've got to get this sorted, or else I won't be able to do anything all day."
                                    $ addtime(1,False)
                                    $ count += 1
                                    menu:
                                        "Continue to work, trying to get your emotions under control":
                                            call firstday_mc_work_internal() from _call_firstday_mc_work_internal
                                        "Try to find [fsName.yourformal], and see if she's willing to talk with you":
                                            $ firstday_talk = True
                                            $ count = 3
                                            call change_loc('livingroom',sec_call='fs_talk') from _call_change_loc_36
                                else:
                                    fp "It's late, and probably time to call it a day"
                                    $ count = 0
                                    $ talk_later = True
                                    call entrance_loc() from _call_entrance_loc_3
                            "Or, I could just slack off today, and work on the bike another day...":
                                if not firstday_after_talk:
                                    $ fs_mad = True
                                $ count = 0
                                $ talk_later = True
                                call entrance_loc() from _call_entrance_loc_4
                else:
                    fp "Ah, it's a beautiful day. Maybe I should go to the beach...?"
                    menu:
                        "Go to the beach":
                            call change_loc('beach') from _call_change_loc_74
                        "Nah, slack of in the garden instead":
                            call entrance_loc() from _call_entrance_loc_5

    label breakfast_interaction(bin_called=False):
        if bin_called and not had_breakfast:
            $ bin_called = False
            if breakfast_food:
                show fm_standing ahead with dissolve
                if breakfast_food == 'cereal':
                    fm ahead "I poured you some [breakfast_food]. We're sort of out of everything. Need to go shopping"
                    fp "Cereal is fine, [fmName.informal]"
                    $ resolved = breakfast_nice_att = breakfast_nice_mod = breakfast_mean_att1 = breakfast_mean_att2 = breakfast_mean_mod1 = breakfaste_mean_mod2 = False
                else:
                    fm ahead "I made [breakfast_food]"
                    menu:
                        "Be nice":
                            $ resolved = 'nice'
                            $ breakfast_reply = breakfast_nice.format(breakfast_food).capitalize()
                        "Be mean":
                            $ resolved = 'mean'
                            $ breakfast_reply = breakfast_mean.format(breakfast_food).capitalize()
                    fp "[breakfast_reply], [fmName.informal]"
                if resolved == 'nice':
                    $ resolved = False
                    show fm_standing smile with dissolve
                    $ statschangenotify(breakfast_nice_att,breakfast_nice_mod)
                elif resolved == 'mean':
                    $ resolved = False
                    show fm_standing mad with dissolve
                    $ statschangenotify(breakfast_mean_att1,breakfast_mean_mod1,True)
                    $ statschangenotify(breakfast_mean_att2,breakfast_mean_mod2)
                $ resolved = breakfast_nice_att = breakfast_nice_mod = breakfast_mean_att1 = breakfast_mean_att2 = breakfast_mean_mod1 = breakfaste_mean_mod2 = False
                $ had_breakfast = True
                hide fm_standing with dissolve
            $ addtime(False,30)
            if day_week <= 4:
                if debug:
                    "weekday triggered"
                if renpy.random.random() > .5:
                    if debug:
                        "renpy random more than 5"
                    if not fs_mad:
                        if renpy.random.random() > .5:
                            show fs_standing ahead flip with dissolve
                        else:
                            show fs_standing ahead with dissolve
                        fs ahead "Good morning, [fp]"
                        fp "Hi, [fsName.informal]"
                        if renpy.random.random() > .90:
                            fp "How you doing today?"
                            fs smile "I'm doing great! I have the day off, so I'm gonna go with [fmName.name] and check out some summer clothes, maybe a new bikini"
                            if fs_rel > 15 and fs_aro > 10:
                                fp "Cool. {i}In a whisper: Buy something sexy to wear at home ;){/i}"
                                if renpy.random.random() > .65:
                                    $ statschangenotify("fs_aro",1)
                                if renpy.random.random() > .5:
                                    $ statschangenotify("fs_rel",1)
                                fs blushing "I'll see what I can manage, [fp]"
                            else:
                                fp "Cool"
                        else:
                            call fs_talk(True) from _call_fs_talk_1
                        $ shitty_morning = False
                        $ morning_event_done = True
                    else:
                        if renpy.random.random() > .5:
                            show fs_standing annoyed flip with dissolve
                        else:
                            show fs_standing annoyed with dissolve
                        fp "Hi [fsName.informal]"
                        show fs_standing mad with dissolve
                        fs mad "Fuck off, [fp]"
                        fp "... okay..."
                        $ statschangenotify("fs_rel",-1)
                        fp "{i}I should probably try to talk to her later, and apologize for earlier... Seems she's still pissed at me{/i}"
                        menu:
                            "Skip the day, and talk to [fsName.yourformal]":
                                $ talk_later = True
                                $ morning_event_done = True
                                call livingroom_scene from _call_livingroom_scene
                                call fs_talk(True) from _call_fs_talk_2
                                call change_loc('livingroom') from _call_change_loc_37
                            "Continue the day, and try to talk to [fsName.yourformal] later":
                                $ shitty_morning = True
                                $ morning_event_done = True
                                call change_loc(current_location) from _call_change_loc_38
                    if not breakfast_jump:
                        if late_oh_shit:
                            label late_morning():
                                if day_week <= 4:
                                    fp "Oh, shit! {b} *throws on some clothes, rushes out the door*{/b} Fuck breakfast, no time!"
                                    call outside_scene from _call_outside_scene_2
                                    if not mc_f and not already_late:
                                        fp "{i}Damn, I wish I had my bike ready. If I had, I wouldn't be late...{/i}"
                                    elif not mc_f and already_late:
                                        fp "{i}Damn... even if I had my bike, no way I would reach school in time{/i}"
                                    elif mc_f and not already_late:
                                        fp "{i}Hmmm... maybe I should take my bike. That way I'll be on time even though I'm running late{/i}"
                                    else:
                                        fp "{i}I'll take my bike. I'm running late already, but I can at least have a bit of fun on the way{/i}"
                                    $ shitty_morning = True
                                    $ morning_event_done = True
                                    call travel_events('travel_school') from _call_travel_events_19
                        else:
                            $ late_oh_shit = False
                            $ morning_event_done = True
                            $ shitty_morning = False
                    if day_week <= 4:
                        if debug:
                            "event outside - day-week 4 (event 1)"
                        $ morning_event_done = True
                        call change_loc('outside',sec_call="outside_loc") from _call_change_loc_39
                else:
                    if debug:
                        "renpy random below 5"
                    $ morning_event_done = True
                    call change_loc('outside',sec_call="outside_loc") from _call_change_loc_40
            else:
                if debug:
                    "weekend"
                if renpy.random.random() > .95: #changed from 6
                    if not fs_mad:
                        if renpy.random.random() > .5:
                            show fs_standing ahead flip
                        else:
                            show fs_standing ahead:
                                yalign 0.0
                        fs ahead "Good morning, [fp]"
                        fp "Hi, [fsName.informal]"
                        if renpy.random.random() > .5:
                            fp "How you doing today?"
                            fs smile "I'm doing great! I have the day off, so I'm gonna go with [fmName.name] and check out some summer clothes, maybe a new bikini"
                            if fs_rel > 15 and fs_aro > 10:
                                fp "Cool. {i}In a whisper: Buy something sexy to wear at home ;){/i}"
                                if renpy.random.random() > .65:
                                    $ statschangenotify("fs_aro",1)
                                if renpy.random.random() > .5:
                                    $ statschangenotify("fs_rel",1)
                                fs blushing "I'll see what I can manage, [fp]"
                            else:
                                fp "Cool"
                                $ morning_event_done = True
                                call kitchen_loc(True) from _call_kitchen_loc
                        else:
                            $ morning_event_done = True
                            if renpy.random.random() > .5:
                                $ sun_event = True
                                call weekend_sun(True) from _call_weekend_sun
                            else:
                                call kitchen_loc(True) from _call_kitchen_loc_1
                    else:
                        if renpy.random.random() > .5:
                            show fs_standing annoyed flip with dissolve
                        else:
                            show fs_standing annoyed with dissolve
                        fp "Hi [fsName.informal]"
                        show fs_standing mad with dissolve
                        fs mad "Fuck off, [fp]"
                        fp "... okay..."
                        $ statschangenotify("fs_rel",-1)
                        fp "{i}I should probably try to talk to her later, and apologize for earlier... Seems she's still pissed at me{/i}"
                        menu:
                            "Skip the day, and talk to [fsName.yourformal]":
                                $ talk_later = True
                                $ morning_event_done = True
                                call fs_talk(True) from _call_fs_talk_3
                            "Continue the day, and try to talk to [fsName.yourformal] later":
                                $ shitty_morning = True
                                $ morning_event_done = True
                                call change_loc(current_location) from _call_change_loc_41
                else:
                    $ morning_event_done = True
                    if debug:
                        if renpy.random.random() > .1:
                            $ sun_event = True
                            call weekend_sun(True) from _call_weekend_sun_1
                        else:
                            call kitchen_loc(True) from _call_kitchen_loc_2
                    else:
                        if renpy.random.random() > .5:
                            $ sun_event = True
                            call weekend_sun(True) from _call_weekend_sun_2
                        else:
                            call kitchen_loc(True) from _call_kitchen_loc_3