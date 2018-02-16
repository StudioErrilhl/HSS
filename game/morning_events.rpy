label morning_events():
    #this is a wrapping label for morning events
    if int(current_time[:2]) in morning and not morning_event_done:
        call fp_bedroom_scene
        # call fp_morning_content(True)
# label fp_morning_content(fpc_called=False):
#         if fpc_called:
#             $ fpc_called = False
        $ fpmc_r = renpy.random.random()
        # $ renpy.watch(str(fpmc_r))
        if (fpmc_r < .35 and day_week <= 4 and overslept) or (int(current_time[:2]) > 7 and day_week <= 4):
            $ overslept = False
            # $ current_time = "07:35"
            show fm_standing mad with dissolve                
            fm mad "[fp]! Wake UP!"
            fp "uuuhh..."
            fm mad "[fp]! Get out of bed THIS INSTANT!"
            $ conditions.addcondition("[fmName.Informal]! Shut up! I'm awake, and getting up!","fm_rel >= 15 and fm_dom >= 20")            
            $ conditions.addcondition("Yeez, [fmName.informal]! Stop nagging me, will you? I'm gonna get up in a second","fm_rel >= 5")
            menu:
                "[fmName.Informal]! Shut up! I'm awake, and getting up!":
                    call fm_morningchoice_dom(True)
                "Yeez, [fmName.informal]! Stop nagging me, will you? I'm gonna get up in a second":
                    call fm_morningchoice_reldom(True)
                "Okay, [fmName.informal]... I'm up, I'm up. Please don't yell":
                    call fm_morningchoice_rel(True)
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
                                    call morning_assfuck()
                                elif fm_anal >= 10 and fm_anal <= fm_pussy:
                                    fm blushing "Do you really wanna fuck my ass?"
                                    menu:
                                        "Yes":
                                            call morning_assfuck()
                                        "No":
                                            call morning_pussyfuck()
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
                                    call morning_pussyfuck()
                                elif fm_pussy >= 10 and fm_pussy <= fm_bj:
                                    fm ahead "Do you want my pussy, or do you want a blowjob?"
                                    menu:
                                        "Pussy":
                                            call morning_pussyfuck()
                                        "Blowjob":
                                            call morning_bj()
                                        "How about both?":
                                            call morning_pussy_bj()
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
                                    call late_morning()
                            "Tell her to get your cock out and start sucking":
                                $ statschangenotify("fm_dom",1,True)
                                $ statschangenotify("fm_bj",1)
                                if fm_bj >= 10:
                                    $ statschangenotify("fm_bj",1)
                                    call morning_bj()
                                elif fm_bj >= 10 and fm_bj <= fm_pussy:
                                    fm ahead "Do you want a blowjob, or do you want my pussy?"
                                    menu:
                                        "Blowjob":
                                            call morning_bj()
                                        "Pussy":
                                            call morning_pussyfuck()
                                        "How about both?":
                                            call morning_pussy_bj()
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
                                call morning_strip()
                            "{b}I'll be late for school{/b}":
                                hide fm_standing                                
                                call late_morning()
                            "Have your mom drive you to school, and make sure you're not late":
                                $ statschangenotify("fm_dom",.5)
                                hide fm_standing                                    
                                call drive_to_school()
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
                        call late_morning()
                    # return
            
            label fm_morningchoice_reldom(called=False):
                if called:
                    $ called = False
                    if fm_dom < 25:
                        $ statschangenotify("fm_dom",.5,True)                
                        $ statschangenotify("fm_rel",.5)    
                    $ fm_choice1_choice = "reldom"
                    # fm "You're gonna be late for school, [fp]"
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
                    call change_loc('fp bedroom')
                
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
                    call late_morning()
                    # return
        elif fpmc_r < .75:
            # if day_week <= 4:
            #     $ current_time = "07:00"
            # else:
            #     $ current_time = "09:00"
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
            # $ morning_event_done = True
            call fp_bedroom_loc(True)
            # return
        else:
            $ current_time = "06:00"
            if not backpack.has_item(schoolbooks_item):
                if day_week <= 4:
                    show books_on_dresser
            fp "{b}Yawn{/b}"
            fp "{i}What time is it...?{/i}"
            if int(current_time[:2]) == 6 and day_week <= 4:
                if not mc_f:
                    fp "{i}Oh, it's really early... oh well, lets get up, maybe I can do some work on the bike before school{/i}"
                    # call garage_scene
                    call change_loc('garage')
                    # call w_mc(True)
                    fp "{i}Oh, I better get going, if I'm gonna be on time{/i}"
                    call entrance_loc()
                else:
                    # $ current_time = "07:45"
                    fp "{i}I should take the bike. It's a nice day for a ride anyways{/i}"
                    ## depending on the relationship with nk, there should be a possibility of her joining the ride to school
                # return
            elif int(current_time[:2]) == 6 and day_week >= 5:
                if not mc_f:
                    fp "Oh, it's really early... oh well, maybe I can get an early start and work on the bike today"
                    call garage_scene
                    call change_loc('garage')
                    call w_mc(True)
                    $ early_morning_we = True
                    $ addtime(False,15)
                else:
                    # $ current_time = "07:45"
                    fp "Hm... really nice weather today, maybe I should take a ride"
                # return
            $ breakfast_jump = True
            # jump leave_bedroom_morning
            $ shitty_morning = False
            $ morning_event_done = True
            # return
    # else:
    #     return
    label morning_strip(fm_ms_called=False):
        if fm_ms_called:
            $ fm_ms_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning strip"
            # return
    label drive_to_school(fm_ds_called=False):
        if fm_ds_called:
            $ fm_ds_called = False
            $ late_oh_shit = True
            call school_on_time(True)
            # return
    label morning_assfuck(fm_ma_called=False):
        if fm_ma_called:
            $ fm_ma_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning AF"
            # return
    label morning_pussyfuck(fm_mp_called=False):
        if fm_mp_called:
            $ fm_mp_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning PF"
            # return
    label morning_pussy_bj(fm_mpbj_called=False):
        if fm_mpbj_called:
            $ fm_mpbj_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning PFBJ"
            # return
    label morning_bj(fm_mbj_called=False):
        if fm_mbj_called:
            $ fm_mbj_called = False
            $ addtime(False,30)
            "This is a placeholder for the morning BJ"
            # return

    if skip_breakfast:
        label skip_breakfast(called=False):
            $ skip_breakfast = False
            if called:
                $ called = False
                $ addtime(False,30)
                fp "{i}Deciding to skip breakfast, to avoid uncomfortable incidents with [fsName.myformal], I go straight to the garage.{/i}"
                call garage_scene
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
                                            call firstday_mc_work_internal()
                                        "Try to find [fsName.yourformal], and see if she's willing to talk with you":
                                            $ firstday_talk = True
                                            $ count = 3
                                            call change_loc('livingroom',sec_call='fs_talk')
                                else:
                                    fp "It's late, and probably time to call it a day"
                                    $ count = 0
                                    call entrance_loc()
                            "Or, I could just slack off today, and work on the bike another day...":
                                if not firstday_after_talk:
                                    $ fs_mad = True
                                $ count = 0
                                call entrance_loc()
                else:
                    fp "Ah, it's a beautiful day. Maybe I should go to the beach...?"
                    menu:
                        "Go to the beach":
                            call beach_ride(True)
                        "Nah, slack of in the garden instead":
                            call entrance_loc()
    # return
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
                        else: #if day_week <= 4:# and (sis_school_issue or sis_school_issue_2 or hacker_2 or school_clues_search_2):
                            call fs_talk(True)
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
                                call livingroom_scene
                                call fs_talk(True)
                                call change_loc('livingroom')
                            "Continue the day, and try to talk to [fsName.yourformal] later":
                                $ shitty_morning = True
                                $ morning_event_done = True                                
                                # call after_fs_mad_morning(True)
                                call change_loc(current_location)
                    if not breakfast_jump:
                        if late_oh_shit:
                            # label late_oh_shit:
                            label late_morning():
                                if day_week <= 4:
                                    fp "Oh, shit! {b} *throws on some clothes, rushes out the door*{/b} Fuck breakfast, no time!"
                                    call outside_scene
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
                                    # call travel_school(True)
                                    call travel_events('travel_school')
                        else:
                            $ late_oh_shit = False
                            $ morning_event_done = True                            
                            $ shitty_morning = False
                    if day_week <= 4:
                        if debug:
                            "event outside - day-week 4 (event 1)"
                        $ morning_event_done = True
                        # call change_loc('outside neighborhood')
                        # call outside_loc(True)
                        call change_loc('outside',sec_call="outside_loc")
                else:
                    if debug:
                        "renpy random below 5"
                    $ morning_event_done = True                    
                    # call outside_loc(True)
                    call change_loc('outside',sec_call="outside_loc")
            else:
                if debug:
                    "weekend"
                if renpy.random.random() > .95: #changed from 6
                    if not fs_mad:
                        if renpy.random.random() > .5:
                            show fs_standing ahead flip
                        else:
                            show fs_standing ahead
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
                                call kitchen_loc(True)
                        else:
                            $ morning_event_done = True
                            if renpy.random.random() > .5:
                                $ sun_event = True
                                call weekend_sun(True)
                            else:
                                call kitchen_loc(True)
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
                                call fs_talk(True)
                            "Continue the day, and try to talk to [fsName.yourformal] later":
                                $ shitty_morning = True
                                $ morning_event_done = True                                
                                # call after_fs_mad_morning(True)
                                call change_loc(current_location)
                else:
                    $ morning_event_done = True
                    if debug:                    
                        if renpy.random.random() > .1:
                            $ sun_event = True
                            call weekend_sun(True)
                        else:
                            call kitchen_loc(True)
                    else:
                        if renpy.random.random() > .5:
                            $ sun_event = True
                            call weekend_sun(True)
                        else:
                            call kitchen_loc(True)
    

    # return
    # label fp_morning_content(fpc_called=False):
    #     if fpc_called:
    #         $ fpc_called = False
    #         $ fpmc_r = renpy.random.random()
    #         # $ renpy.watch(str(fpmc_r))
    #         if (fpmc_r < .35 and day_week <= 4 and overslept) or (int(current_time[:2]) > 7 and day_week <= 4):
    #             $ overslept = False
    #             # $ current_time = "07:35"
    #             show fm_standing mad with dissolve                
    #             fm mad "[fp]! Wake UP!"
    #             fp "uuuhh..."
    #             fm mad "[fp]! Get out of bed THIS INSTANT!"
    #             $ conditions.addcondition("[fmName.Informal]! Shut up! I'm awake, and getting up!","fm_rel >= 15 and fm_dom >= 20")            
    #             $ conditions.addcondition("Yeez, [fmName.informal]! Stop nagging me, will you? I'm gonna get up in a second","fm_rel >= 5")
    #             menu:
    #                 "[fmName.Informal]! Shut up! I'm awake, and getting up!":
    #                     call fm_morningchoice_dom(True)
    #                 "Yeez, [fmName.informal]! Stop nagging me, will you? I'm gonna get up in a second":
    #                     call fm_morningchoice_reldom(True)
    #                 "Okay, [fmName.informal]... I'm up, I'm up. Please don't yell":
    #                     call fm_morningchoice_rel(True)
    #             $ conditions.clear()
                
    #             label fm_morningchoice_dom(called=False):
    #                 if called:
    #                     if fm_dom < 25: 
    #                         $ statschangenotify("fm_dom",2)
    #                         pass 
    #                     if fm_dom >= 25:
    #                         $ statschangenotify("fm_dom",.5)                
    #                         pass
    #                     else:
    #                         $ statschangenotify("fm_dom",-.5)                                
    #                         pass
    #                     $ fm_choice1_choice = "dom"
    #                     $ addtime(False, 10)
    #                     fm mad "Don't talk to me like that! I'm your [fmName.role]! You respect me, you hear?"
    #                     if fm_dom >= 45:
    #                         fp "[fmName.Formal]! *You bark at her*"
    #                         fp "Get your fat ass over here right this instant!"
    #                         "[fmName.yourrole] hurries over to you, eyes downcast, not wanting to anger you further"
    #                         fp "What did you just say to me?"
    #                         fm sad "I'm... I'm sorry. I didn't mean to raise my voice. I'm just a bit stressed..."
    #                         fp "Stop it! I don't wanna hear it! Get down!"
    #                         "[fmName.name] stares at you, bewildered. Down...?"
    #                         "You grab her shoulder, and push her down, hard, so that she lands on her knees"
    #                         fm crying "*OUCH!*"
    #                         fp "Shut it!"
    #                         "She shuts her mouth immediately, recognizing the mood you're in"
    #                         $ addtime(False,15)
    #                         fp "Are you just gonna sit there? I'm already late for school. Shouldn't you be getting on with your apology by now?"
    #                         fm blushing "You want me to...?"
    #                         $ conditions.addcondition("Tell her to pull down her pants and present her ass to you","fm_dom >= 40")
    #                         $ conditions.addcondition("Tell her to sit back and spread her pussy for you","fm_dom >= 30")
    #                         menu:
    #                             "Tell her to pull down her pants and present her ass to you":
    #                                 $ statschangenotify("fm_dom",2,True)
    #                                 $ statschangenotify("fm_anal",1)
    #                                 if fm_anal >= 10 and fm_anal >= fm_pussy:
    #                                     $ statschangenotify("fm_anal",1)
    #                                     call morning_assfuck()
    #                                 elif fm_anal >= 10 and fm_anal <= fm_pussy:
    #                                     fm blushing "Do you really wanna fuck my ass?"
    #                                     menu:
    #                                         "Yes":
    #                                             call morning_assfuck()
    #                                         "No":
    #                                             call morning_pussyfuck()
    #                                 else:
    #                                     fm ahead "What are you going to do?\n{i}Her voice shakes a little bit{/i}"
    #                                     fp "Oh, I dunno... *you slap her ass, hard*"
    #                                     $ statschangenotify("fm_dom",1)
    #                                     fm crying "{b}OUCH!{/b}"
    #                                     fp "Shut up!\n{b}you slap her again{/b}"
    #                                     "Getting turned on by her sounds, and the spanking in general, you continue, till she begs for mercy"
    #                                     fm crying "{b}PLEASE!{/b}\nStop it.\n{i}Tears are streaming down her face{/i}"
    #                                     $ statschangenotify("fm_rel",-1,True)
    #                                     $ statschangenotify("fm_dom",1.5)
    #                                     "You stop, looking over her ass, which is reddening nicely"
    #                                     fp "Get up, get dressed, and get out of my room"
    #                                     fm ahead_eyes_closed "Okay... {i}she meekly replies, staring into the ground{/i}"
    #                             "Tell her to sit back and spread her pussy for you":
    #                                 $ statschangenotify("fm_dom",1.5,True)
    #                                 $ statschangenotify("fm_pussy",1)
    #                                 if fm_pussy >= 10 and fm_pussy >= fm_bj:
    #                                     $ statschangenotify("fm_pussy",1)
    #                                     call morning_pussyfuck()
    #                                 elif fm_pussy >= 10 and fm_pussy <= fm_bj:
    #                                     fm ahead "Do you want my pussy, or do you want a blowjob?"
    #                                     menu:
    #                                         "Pussy":
    #                                             call morning_pussyfuck()
    #                                         "Blowjob":
    #                                             call morning_bj()
    #                                         "How about both?":
    #                                             call morning_pussy_bj()
    #                                 else:                            
    #                                     "You watch as [fmName.yourshort] hitches her thumbs under her panties and swiftly pulls them down over her thighs. She's got shapely legs, not at all bad for a woman in her forties. She pulls up her skirt, and sits back on the bed, spreading her legs as she does so."
    #                                     fm ahead "Happy now? {i}There's still a bit of defiance in her voice, some residual want to fight you, to stand up for herself{/i}"
    #                                     fp "Not quite. I would love to introduce my cock to your pussy, but I don't have time. Start masturbating!"
    #                                     fm blushing "{b}Gasp{/b} You... you want me to... rub... rub my pussy... here? In... in front of you?"
    #                                     fp "Yes, I though I made myself pretty clear? If it was possible to misunderstand, I apologize. Let's see... \"{b}rub your pussy! Until you cum{/b}"
    #                                     "You can see her hesitating. The emotions play over her face, making it clear that she's weighing the options, carefully."
    #                                     "You look at your watch, realising you're gonna be late."
    #                                     $ addtime(False,40)
    #                                     fp "Fuck!"
    #                                     "Your outburst startles [fmName.yourshort] - she looks at, you, a bit worried"
    #                                     fp "I would love to continue this, but I'm gonna be late for school. That shouldn't prevent {b}you{/b} from enjoying yourself, though. Finish up. Then send me a picture when you're done!"
    #                                     "With that, you leave [fmName.yourshort], half naked, on your bed, and head for the door"
    #                                     hide fm_standing
    #                                     call late_morning()
    #                             "Tell her to get your cock out and start sucking":
    #                                 $ statschangenotify("fm_dom",1,True)
    #                                 $ statschangenotify("fm_bj",1)
    #                                 if fm_bj >= 10:
    #                                     $ statschangenotify("fm_bj",1)
    #                                     call morning_bj()
    #                                 elif fm_bj >= 10 and fm_bj <= fm_pussy:
    #                                     fm ahead "Do you want a blowjob, or do you want my pussy?"
    #                                     menu:
    #                                         "Blowjob":
    #                                             call morning_bj()
    #                                         "Pussy":
    #                                             call morning_pussyfuck()
    #                                         "How about both?":
    #                                             call morning_pussy_bj()
    #                                 else:                            
    #                                     "This is a placeholder for the morning event for fm_dom above 45"
    #                     elif fm_dom >= 30:
    #                         fp "Hell no, [fmName.informal]! You've lost that. I'm the one in charge here now."
    #                         fm ahead_eyes_closed "... Yes, [fp] ... "
    #                         "{i}[yourCapsfM] looks down at the floor, a slight blush on her cheeks, clearly uncomfortable with the situation. Maybe also a little afraid. Not really of you, but that she's excited, just a slight stirring in her loins, by all this...{/i}"
    #                         $ statschangenotify("fm_aro",1)                    
    #                         fm ahead_eyes_closed "... You're in charge. What will you have me do?"
    #                         menu:
    #                             "Screw school, I can be late for once. Strip!":
    #                                 $ statschangenotify("fm_dom",1,True)
    #                                 $ statschangenotify("fm_cor",1,True)
    #                                 $ statschangenotify("fm_rel",-5)
    #                                 hide fm_standing                                    
    #                                 call morning_strip()
    #                             "{b}I'll be late for school{/b}":
    #                                 hide fm_standing                                
    #                                 call late_morning()
    #                             "Have your mom drive you to school, and make sure you're not late":
    #                                 $ statschangenotify("fm_dom",.5)
    #                                 hide fm_standing                                    
    #                                 call drive_to_school()
    #                     elif fm_dom >= 20:
    #                         fp "Oh, shut it, [fmName.name]. \"Respect\". Don't make me laugh!"
    #                         fm ahead_eyes_closed "{b}her lip quivering...{/b} don't... just... you're gonna be late..."
    #                         fp "Where are you going? Come right back here and apologize!"
    #                         "[fmName.name] slowly turns, shuffles back towards you and, in a barely audible whisper..."
    #                         fm ahead_eyes_closed "I'm sorry, [fp]. I apologize for my behavior"
    #                         fp "Fine. Don't let it happen again!"
    #                         $ fm_apologize = True
    #                         $ addtime(False,10)
    #                         "[yourCapsfM] walks out of the room"
    #                         $ morning_event_done = True                            
    #                         hide fm_standing                            
    #                         call late_morning()
    #                     # return
                
    #             label fm_morningchoice_reldom(called=False):
    #                 if called:
    #                     $ called = False
    #                     if fm_dom < 25:
    #                         $ statschangenotify("fm_dom",.5,True)                
    #                         $ statschangenotify("fm_rel",.5)    
    #                     $ fm_choice1_choice = "reldom"
    #                     # fm "You're gonna be late for school, [fp]"
    #                     if int(current_time[3:]) == 0:
    #                         $ already_late = True
    #                         fm ahead "You're late. School just started!"
    #                     else:
    #                         if int(current_time[:2]) <= 8:
    #                             if int(current_time[:2]) == 8:
    #                                 $ tt = abs(int(current_time[3:]))
    #                                 fm ahead "You're late. School started [tt] minutes ago"
    #                             else:
    #                                 $ tl = abs(int(current_time[3:])-60)
    #                                 fm ahead "You're gonna be late. School starts in [tl] minutes."
    #                         else:
    #                             $ already_late = True
    #                             $ th = abs(int(current_time[:2])-8)
    #                             $ text = "You're late. School started over {0} {1} ago".format(th,'hours' if th > 1 else 'hour')
    #                             fm ahead "[text]"
    #                     fp "Yes, yes, I know. Just... let me get dressed, and take a shower, okay?"
    #                     fm ahead "Fine! I'm going to work. Make sure you lock the door when you leave!"
    #                     $ morning_event_done = True
    #                     call change_loc('fp bedroom')
                    
    #             label fm_morningchoice_rel(called=False):
    #                 if called:
    #                     $ called = False
    #                     if fm_rel < 25:
    #                         $ statschangenotify("fm_rel",1.5)
    #                     elif fm_rel < 40:
    #                         $ statschangenotify("fm_rel",1)
    #                     else:
    #                         $ statschangenotify("fm_rel",.25)
    #                     fm ahead "You need to stop staying up all night, [fp]. If you can't get out of bed in the morning, you'll fail both school and work, when that time comes."
    #                     fp "You know that there are jobs where you work both evenings and nights, right [fmName.informal]?"
    #                     fm ahead "Of course I do! But that doesn't mean that you should aim for those jobs. Now get your ass in gear!"
    #                     $ addtime(False,10)
    #                     if int(current_time[3:]) == 0:
    #                         $ already_late = True
    #                         fm ahead "You're late. School just started!"
    #                     else:
    #                         if int(current_time[:2]) <= 8:
    #                             if int(current_time[:2]) == 8:
    #                                 $ tt = abs(int(current_time[3:]))
    #                                 fm ahead "You're late. School started [tt] minutes ago"
    #                             else:
    #                                 $ tl = abs(int(current_time[3:])-60)
    #                                 fm ahead "You're gonna be late. School starts in [tl] minutes."
    #                         else:
    #                             $ already_late = True
    #                             $ th = abs(int(current_time[:2])-8)
    #                             $ text = "You're late. School started over {0} {1} ago".format(th,'hours' if th > 1 else 'hour')
    #                             fm ahead "[text]"
    #                     $ morning_event_done = True
    #                     call late_morning()
    #                     # return
    #         elif fpmc_r < .75:
    #             # if day_week <= 4:
    #             #     $ current_time = "07:00"
    #             # else:
    #             #     $ current_time = "09:00"
    #             if not backpack.has_item(schoolbooks_item):
    #                 if day_week <= 4:
    #                     if debug:
    #                         "test books on dresser"
    #                     show books_on_dresser
    #             show fm_standing ahead with dissolve
    #             fm ahead "[fp], time to get out of bed and have some breakfast"
    #             fp "Sure, [fmName.informal] - I'll be right down"
    #             hide fm_standing
    #             $ breakfast_jump = True
    #             # $ morning_event_done = True
    #             call fp_bedroom_loc(True)
    #             # return
    #         else:
    #             $ current_time = "06:00"
    #             if not backpack.has_item(schoolbooks_item):
    #                 if day_week <= 4:
    #                     show books_on_dresser
    #             fp "{b}Yawn{/b}"
    #             fp "{i}What time is it...?{/i}"
    #             if int(current_time[:2]) == 6 and day_week <= 4:
    #                 if not mc_f:
    #                     fp "{i}Oh, it's really early... oh well, lets get up, maybe I can do some work on the bike before school{/i}"
    #                     # call garage_scene
    #                     call change_loc('garage')
    #                     # call w_mc(True)
    #                     fp "{i}Oh, I better get going, if I'm gonna be on time{/i}"
    #                     call entrance_loc()
    #                 else:
    #                     # $ current_time = "07:45"
    #                     fp "{i}I should take the bike. It's a nice day for a ride anyways{/i}"
    #                     ## depending on the relationship with nk, there should be a possibility of her joining the ride to school
    #                 # return
    #             elif int(current_time[:2]) == 6 and day_week >= 5:
    #                 if not mc_f:
    #                     fp "Oh, it's really early... oh well, maybe I can get an early start and work on the bike today"
    #                     call garage_scene
    #                     call change_loc('garage')
    #                     call w_mc(True)
    #                     $ early_morning_we = True
    #                     $ addtime(False,15)
    #                 else:
    #                     # $ current_time = "07:45"
    #                     fp "Hm... really nice weather today, maybe I should take a ride"
    #                 # return
    #             $ breakfast_jump = True
    #             # jump leave_bedroom_morning
    #             $ shitty_morning = False
    #             $ morning_event_done = True
    #             # return
    #     # else:
    #     #     return
    #     label morning_strip(fm_ms_called=False):
    #         if fm_ms_called:
    #             $ fm_ms_called = False
    #             $ addtime(False,30)
    #             "This is a placeholder for the morning strip"
    #             # return
    #     label drive_to_school(fm_ds_called=False):
    #         if fm_ds_called:
    #             $ fm_ds_called = False
    #             $ late_oh_shit = True
    #             call school_on_time(True)
    #             # return
    #     label morning_assfuck(fm_ma_called=False):
    #         if fm_ma_called:
    #             $ fm_ma_called = False
    #             $ addtime(False,30)
    #             "This is a placeholder for the morning AF"
    #             # return
    #     label morning_pussyfuck(fm_mp_called=False):
    #         if fm_mp_called:
    #             $ fm_mp_called = False
    #             $ addtime(False,30)
    #             "This is a placeholder for the morning PF"
    #             # return
    #     label morning_pussy_bj(fm_mpbj_called=False):
    #         if fm_mpbj_called:
    #             $ fm_mpbj_called = False
    #             $ addtime(False,30)
    #             "This is a placeholder for the morning PFBJ"
    #             # return
    #     label morning_bj(fm_mbj_called=False):
    #         if fm_mbj_called:
    #             $ fm_mbj_called = False
    #             $ addtime(False,30)
    #             "This is a placeholder for the morning BJ"
    #             # return

        # label after_fs_mad_morning(afs_mad=False):
        #     if afs_mad:
        #         $ afs_mad = False
        #         $ afsmm_r = renpy.random.random()
        #         if debug:
        #             $ renpy.watch(str(afsm_r))
        #         if afsmm_r < .5 and shitty_morning and day_week <= 4:
        #             nk ahead "Hi [fp]! You wanna ride to school?"
        #             if not nk_driving:
        #                 fp "Hi [nk]... Didn't know you drove?"
        #                 nk ahead "My mom got me this for my birthday. Haven't really driven it much, but it's awesome."
        #                 $ nk_driving = True
        #             else:
        #                 fp "Hi [nk]"
        #             if bad_weather and rainstorm:
        #                 $ text1 = "Sure! That way I won't be late, not to mention drowning by the time I get there!\n{i}Damn, she saved my scrawny ass. Don't understand why she gets so much flak at school, she's nice...{/i}"
        #                 $ text2 = "No thanks, [nk]. I've got a buddy picking me up, he'll be here soon.\n{i}Even in this weather I'm not gonna get in a car with her... I'd never hear the end of it at school{/i}"
        #             else:
        #                 $ text1 = "Sure! Then I won't be late!\n{i}Who cares if [nk] is not one of the popular kids - her offer is nice{/i}"
        #                 $ text2 = "No thanks! I'll just walk. Don't really wanna trust my life to your driving!\n{i}Don't wanna be caught dead in the same car as [nk]...{/i}"
        #             menu:
        #                 "[text1]":
        #                     $ statschangenotify("nk_rel",1.5)                                    
        #                     $ renpy.pause(.25)
        #                     call school_on_time(True)
        #                 "[text2]":
        #                     if bad_weather and rainstorm:
        #                         $ statschangenotify('nk_rel',-1)
        #                     else:
        #                         $ statschangenotify("nk_rel",-3)
        #                     $ renpy.pause(.25)
        #                     if renpy.random.random() < .4:
        #                         call school_walk_late(True)
        #                     else:
        #                         call sn_punishment_late(True)
        #         elif afsmm_r < .5 and not shitty_morning and day_week <= 4:
        #             show nk_standing ahead with dissolve
        #             nk ahead "Hi [fp]! Wanna walk to school with me?"
        #             menu:
        #                 "Sure, [nk]":
        #                     show nk_standing smile with dissolve
        #                     if nk_rel < 15:
        #                         $ nkrel = 1
        #                     else:
        #                         $ nkrel = .5
        #                     $ statschangenotify("nk_rel",nkrel)
        #                     call nk_walk_with(True)
        #                 "Nah... I just wanna go by myself today, if you don't mind":
        #                     show nk_standing annoyed with dissolve
        #                     $ renpy.pause(.5)
        #                     call school_on_time(True)
        #                 "No thanks, [nk]":
        #                     show nk_standing mad with dissolve
        #                     if nk_rel < 15:
        #                         $ nkrel = -.5
        #                     else:
        #                         $ nkrel = -.25
        #                     $ statschangenotify("nk_rel",nkrel)
        #                     $ renpy.pause(.5)
        #                     call school_on_time(True)
        #         elif afsmm_r > .5 and day_week <= 4:
        #             "[fp] walks to school, arriving on time"
        #             call school_on_time(True)
        #         # elif skip_breakfast:
        #         #     call skip_breakfast(True)
        #         elif day_week == 5 and not early_morning_we:
        #             fp "Ah! This is gonna be a nice day! Weekends are my favorite time of the week!"
        #             $ sat_event = True
        #             call weekend_sat()
        #         elif day_week == 5 and early_morning_we:
        #             $ sat_event = True
        #             call weekend_sat()
        #         elif day_week == 6:
        #             if not bad_weather and not rainstorm:
        #                 fp "Ah, this day is gonna be awesome!"
        #             else:
        #                 fp "Ah, crap, it's raining cats and dogs. That sucks. No trip to the beach today, then."
        #             $ sun_event = True
        #             call weekend_sun(True)
        #         else:
        #             "[fp] starts walking to school, knowing he'll be late to class. Wondering what Miss Novak's reaction will be..."
        #             call sn_punishment_late(True)

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
                        call school_on_time(True)
                    else:
                        show nk_standing annoyed with dissolve
                        nk annoyed "I don't think so, [fp]. Wouldn't feel right you looking at my work..."
                        "Seems your relationship with [nk] isn't strong enough to ask her for help yet"
                        call school_on_time(True)
                else:
                    show nk_standing sad with dissolve
                    nk sad "No, I haven't even started yet. There is so much schoolwork, and I'm behind on studying for finals... {i}she trails off, looking a bit troubled{/i}"
                    fp "How about you come over to my house this evening, and we can work on it together?"
                    show nk_standing smile with dissolve
                    nk smile "Oh, that would be nice. Sure, I can do that. Let's say around seven?"
                    fp "Sure, that works for me. I'll be working on my bike till then"
                    $ statschangenotify("nk_rel",.5)  
                    $ evening_event = True
                    $ nk_school_assignment_evening = True
                    call school_on_time(True)
            else:
                call school_on_time(True)

    