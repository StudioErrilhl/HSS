label morning_events():
    #this is a wrapping label for morning events
    if int(current_time[:2]) in morning and not morning_event_done:
        call fp_bedroom_scene from _call_fp_bedroom_scene_3
        call fp_morning_content(True) from _call_fp_morning_content_1

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
                                            # call firstday_talk_fs(True)
                                            call garage_loc(True) from _call_garage_loc
                                    # if firstday_talk:
                                    label firstday_talk_fs(fdtfs_called=False):
                                        if fdtfs_called and (firstday_talk or talk_later):
                                            $ fdtfs_called = False
                                            # call livingroom_scene
                                            show fs_standing annoyed with dissolve
                                            if talk_later:
                                                $ addtime(10)
                                            else:
                                                $ addtime(False,30)
                                            fp "Hi, [fsName.informal]. Can we talk?"
                                            show fs_standing mad with dissolve
                                            fs mad "{b}Fuck you!{/b}"
                                            show fs_standing ahead with dissolve
                                            $ text = "Look, I'm really sorry about {0}! I didn't mean to perv on you, {1}.".format("this morning" if first_day else "the other day", fsName.informal )                                    
                                            fp "[text]"
                                            show fs_standing mad with dissolve
                                            fs "So, you just happened to be leaning against my door because...?"
                                            fp "Well, that bit is true, but I was just trying to figure out what the sounds coming from your bedroom was. Honestly!"
                                            show fs_standing annoyed with dissolve
                                            fs annoyed "So... you heard noises coming from my bedroom, and your first instinct is \"Let's check out the sounds from [fsName.myformal]s bedroom\"?"
                                            fp "Yeah...\n{b}you muster a foolish grin{/b}\nWhen you put it like that, it sounds sort of stupid..."
                                            show fs_standing ahead with dissolve
                                            $ addtime(False, 30)
                                            fs ahead "Can we just agree that unless I'm screaming bloody murder... and even if I am, {i}check first!{/i}, that you do not go creeping about my door?"                                    
                                            fp "Sure, [fsName.informal]. I am really sorry!"
                                            fs ahead_eyes_closed "Yeah, yeah... not as sorry as me..."
                                            fp "Huh?"
                                            show fs_standing ahead with dissolve
                                            fs ahead "Your timing was beyond belief bad!"
                                            fp "Uhh... yeah, I get that... I stumbled in on you almost bare naked..."
                                            show fs_standing blushing with dissolve
                                            fs blushing "No, you idiot. I was about 5 seconds away from an awesome orgasm. Let's just say you ruined the mood."
                                            show fs_standing blushing with dissolve
                                            fp "{i}Oh, shit...\nDid she actually just say that?{/i}\nI'm really sorry? Look, I owe you one, okay. If you need anything, a ride, drinks, anything, just ask, okay?"
                                            show fs_standing smile_open with dissolve
                                            fs smile "{b}Smiling now...{/b}\nOh, don't you worry. I will ask. You bet on it!"
                                            "With that, she picks herself off the couch, and wanders off"
                                            $ addtime(1,False)
                                            hide fs_standing with dissolve
                                            $ statschangenotify("fs_rel",3,True)
                                            $ firstday_talk = False
                                            $ firstday_view = 0
                                            $ firstday_after_talk = True
                                            if fs_mad:
                                                if debug:
                                                    "fsmad happened after talk"
                                                $ fs_mad = False
                                                $ morning_event_done = True
                                                # if int(current_time[:2]) in morning or int(current_time[:2]) in day:
                                                # if int(current_time[:2]) in morning+day:
                                                #     call change_loc('livingroom')
                                                if int(current_time[:2]) in night: #else:
                                                    call end_of_day(True) from _call_end_of_day_5
                                                return
                                            else:
                                                if debug:
                                                    "else fsmad happened"
                                                # jump firstday_mc_work
                                                $ morning_event_done = True
                                                # if int(current_time[:2]) in morning or int(current_time[:2]) in day:
                                                if int(current_time[:2]) in night: #else:
                                                    call end_of_day(True) from _call_end_of_day_6
                                                return

                                        elif fdtfs_called:
                                            $ fdtfs_called = False
                                            call settime(22,False) from _call_settime_4
                                            "{i}Hmm... where did my damn [fsName.role] go?{/i}"
                                            "{i}Oh, well. I'll find her tomorrow. Time for bed{/i}"
                                            # call fp_bedroom_scene
                                            call change_loc('fp bedroom') from _call_change_loc_11
                                else:
                                    fp "It's late, and probably time to call it a day"
                                    $ count = 0
                                    call entrance_loc() from _call_entrance_loc_2
                                    # return
                            "Or, I could just slack off today, and work on the bike another day...":
                                if not firstday_after_talk:
                                    $ fs_mad = True
                                $ count = 0
                                call entrance_loc() from _call_entrance_loc_3
                else:
                    fp "Ah, it's a beautiful day. Maybe I should go to the beach...?"
                    menu:
                        "Go to the beach":
                            call beach_ride(True) from _call_beach_ride
                        "Nah, slack of in the garden instead":
                            call entrance_loc() from _call_entrance_loc_4
    # return
    label breakfast_interaction(bin_called=False):
        if bin_called and not had_breakfast:
            $ bin_called = False
            if breakfast_food:
                show fm_standing ahead with dissolve
                if breakfast_food == 'cereal':
                    fm "I poured you some [breakfast_food]. We're sort of out of everything. Need to go shopping"
                else:
                    fm "I made [breakfast_food]"
                fp "[breakfast_reply], [fmName.informal]"
                $ setattr( store, breakfast_att, getattr( store, breakfast_att ) + breakfast_mod )
                $ had_breakfast = True
                hide fm_standing with dissolve
            $ addtime(False,30)
            if breakfast_mod != 0:
                $ statschangenotify(breakfast_att,breakfast_mod)
            
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
                        elif day_week <= 4 and (sis_school_issue or sis_school_issue_2 or school_hacker_2 or school_clues_search_2):
                            if sis_school_issue:
                                fp "How you doing today?"                        
                                fs sad "Bah. It's a crappy day, and I have to go to school today, and talk to my teacher. Something about maybe not being allowed to take one of my finals"
                                fp "Seriously? That sounds bad"
                                fs annoyed "It's an error on their part, not on mine. I've been good all year, done all my work, behaved. But for some reason their system says I've gotten a written warning, and that I've gotten 3 or 4 calls home. I've gotten [fmName.informal] to come with, so she can tell them in person that it's wrong"
                                fs crying "It's bloody annoying! I've been good. Done everything, behaved, been nice. Nothing to deserve this, not one single thing! And nobody wants to listen to me, claiming that their system is fail-proof. I hope bringing [fmName.informal] will at least make them look over it again."
                                fp "I'm sorry that you have so much trouble. It's probably just a computer-glitch, or something like that. Somebody hit the wrong button for an ID, or something."
                                fs sad "Thanks, [fp]"
                                fp "Good luck, [fsName.informal]"
                                $ statschangenotify("fs_rel",1)
                                $ sis_school_issue = False
                                $ sis_school_issue_2 = True
                            elif sis_school_issue_2:
                                fp "How did it go with the issue you had with the school?"
                                if renpy.random.random() > .5:
                                    fs ahead "Oh, it was nothing, really. We talked, and ended up going through all the entries made about me the last year. Mom confirmed she hadn't received any of the notes or calls that were registerd in the system, which sort of made my teacher a little upset."
                                    fs ahead "Ended up going to the principal's office, and talked to one of the clerks there, and she was able to look a bit, and figure out that someone had made a boo-boo, and registered complaints on another student on me. She couldn't say for sure who'd done it, though, so they were gonna look into it."
                                    fp "But you're off the hook?"
                                    fs smile "Yeah, all is good with me, I'm gonna be allowed to take my exams, and everything."
                                    fp "{i}Hmm... sounds weird that they would make so many mistakes, all pertaining to [fsName.myformal]. Either they're completely incompetent, or there is something else going on...{/i}"
                                    $ school_hacker = True
                                    $ sis_school_issue_2 = False
                                    $ statschangenotify("fs_rel",1)
                                else:
                                    fs mad "Oh, the damn idiots didn't even wanna listen to me. Or [fmName.informal], for that matter. Just went on about how their system didn't make mistakes."
                                    fp "Okay...? So, they're still threathening with disallowing you for your finals?"
                                    fs mad "Yeah. Bloody Miss Enger had the audacity to say, to my face, that if I wasn't causing so much trouble, she wouldn't need to make such a harsh judgement. I think she's getting senile - I haven't even raised my voice in her classroom {b}once{/b}!"
                                    fp "Did you have a talk to [scn] or [scm] at the principal's office?"
                                    fs annoyed "No. Don't even know who they are, [fp]!"
                                    fp "Okay, sorry... they're the office clerks. Usually they're the ones doing the book-keeping, so to speak."
                                    "{i}Hm... maybe I can score some points with [fsName.myformal], if I figure this out?{/i}"
                                    $ school_clues_search = True
                                    $ sis_school_issue_2 = False
                                    $ statschangenotify("fs_rel",.5)
                            elif school_hacker_2:
                                fp "How you doing today?"
                                fs sad "Okay, I guess. A bit worried about finals."
                                fp "Well, at least you get to take them!"
                                fs ahead "Oh, shush. You know I didn't do anything wrong!"
                                fp "I know, I know! But unless you had gotten in their face about it, it would probably not ended well, and you might have had to take summer-school or something to make it up"
                                fs ahead "Yeah. That would have totally sucked!"
                                fp "Well, I'm glad you're only gonna have to worry about your exams"
                                fs smile "You can't help it, can you. Just have to rub it in!"
                                fp "You know me, [fsName.informal]! I love rubbing it in!"
                                $ statschangenotify("fs_aro",.5,True)
                                $ statschangenotify("fs_rel",1)
                                $ school_hacker_2 = False
                                $ school_hacker_3 = True
                            elif school_clues_search_2:
                                fp "How you doing today?"
                                fs ahead "Oh, I'm good. Got a call from school the other day that they've figured out that I was right. No excuses or anything, just... \"You were right, you can take your exams\". Fuck 'em. But I'm happy I don't have to do summer-school or something like that!"
                                fp "Yeah... I went to talk to the clerks. They know me. Got [clerk_talked_to] to look it over. Guess she found something"
                        else:
                            fp "How you doing today?"
                            fs ahead "Oh, I'm okay. Nothing much going on"
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
                                call livingroom_scene from _call_livingroom_scene_1
                                call firstday_talk_fs(True) from _call_firstday_talk_fs_1
                                call change_loc('livingroom') from _call_change_loc_12
                            "Continue the day, and try to talk to [fsName.yourformal] later":
                                $ shitty_morning = True
                                $ morning_event_done = True                                
                                call after_fs_mad_morning(True) from _call_after_fs_mad_morning
                                call change_loc('livingroom') from _call_change_loc_13
                    if not breakfast_jump:
                        if late_oh_shit:
                            # label late_oh_shit:
                            label late_morning():
                                if day_week <= 4:
                                    fp "Oh, shit! {b} *throws on some clothes, rushes out the door*{/b} Fuck breakfast, no time!"
                                    call outside_scene from _call_outside_scene_1
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
                                    call travel_school(True) from _call_travel_school_1                                    
                        else:
                            $ late_oh_shit = False
                            $ morning_event_done = True                            
                            $ shitty_morning = False
                    if day_week <= 4:
                        if debug:
                            "event outside - day-week 4 (event 1)"
                        $ morning_event_done = True
                        # call change_loc('outside neighborhood')
                        # call outside_loc(True) from _call_outside_loc_2
                        call change_loc('outside',sec_call="outside_loc") from _call_change_loc_29
                else:
                    if debug:
                        "renpy random below 5"
                    $ morning_event_done = True                    
                    # call outside_loc(True) from _call_outside_loc_3
                    call change_loc('outside',sec_call="outside_loc") from _call_change_loc_30
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
                                call firstday_talk_fs(True) from _call_firstday_talk_fs_2
                            "Continue the day, and try to talk to [fsName.yourformal] later":
                                $ shitty_morning = True
                                $ morning_event_done = True                                
                                call after_fs_mad_morning(True) from _call_after_fs_mad_morning_1
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
    

    # return
    label fp_morning_content(fpc_called=False):
        if fpc_called:
            $ fpc_called = False
            $ fpmc_r = renpy.random.random()
            # $ renpy.watch(str(fpmc_r))
            if (fpmc_r < .35 and day_week <= 4 and overslept) or (int(current_time[:2]) > 7 and day_week <= 4):
                $ overslept = False
                # $ current_time = "07:35"
                show fm_standing ahead with dissolve                
                fmName.Formal "[fp]! Wake UP!"
                fp "uuuhh..."
                fmName.Formal "[fp]! Get out of bed THIS INSTANT!"
                $ conditions.addcondition("[fmName.informal]! Shut up! I'm awake, and getting up!","fm_rel >= 15 and fm_dom >= 20")            
                $ conditions.addcondition("Yeez, [fmName.informal]! Stop nagging me, will you? I'm gonna get up in a second","fm_rel >= 5")
                menu:
                    "[fmName.informal]! Shut up! I'm awake, and getting up!":
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
                        fmName.Formal "Don't talk to me like that! I'm your [fmName.role]! You respect me, you hear?"
                        if fm_dom >= 45:
                            fp "[fmName.formal]! *You bark at her*"
                            fp "Get your fat ass over here right this instant!"
                            "[fmName.yourrole] hurries over to you, eyes downcast, not wanting to anger you further"
                            fp "What did you just say to me?"
                            fmName.Formal "I'm... I'm sorry. I didn't mean to raise my voice. I'm just a bit stressed..."
                            fp "Stop it! I don't wanna hear it! Get down!"
                            "[fmName.name] stares at you, bewildered. Down...?"
                            "You grab her shoulder, and push her down, hard, so that she lands on her knees"
                            fmName.Formal "*OUCH!*"
                            fp "Shut it!"
                            "She shuts her mouth immediately, recognizing the mood you're in"
                            $ addtime(False,15)
                            fp "Are you just gonna sit there? I'm already late for school. Shouldn't you be getting on with your apology by now?"
                            fmName.Formal "You want me to...?"
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
                                        fmName.Formal "Do you really wanna fuck my ass?"
                                        menu:
                                            "Yes":
                                                call morning_assfuck() from _call_morning_assfuck_1
                                            "No":
                                                call morning_pussyfuck() from _call_morning_pussyfuck
                                    else:
                                        fmName.Formal "What are you going to do?\n{i}Her voice shakes a little bit{/i}"
                                        fp "Oh, I dunno... *you slap her ass, hard*"
                                        $ statschangenotify("fm_dom",1)
                                        fmName.Formal "{b}OUCH!{/b}"
                                        fp "Shut up!\n{b}you slap her again{/b}"
                                        "Getting turned on by her sounds, and the spanking in general, you continue, till she begs for mercy"
                                        fmName.Formal "{b}PLEASE!{/b}\nStop it.\n{i}Tears are streaming down her face{/i}"
                                        $ statschangenotify("fm_rel",-1,True)
                                        $ statschangenotify("fm_dom",1.5)
                                        "You stop, looking over her ass, which is reddening nicely"
                                        fp "Get up, get dressed, and get out of my room"
                                        fmName.Formal "Okay... {i}she meekly replies, staring into the ground{/i}"
                                "Tell her to sit back and spread her pussy for you":
                                    $ statschangenotify("fm_dom",1.5,True)
                                    $ statschangenotify("fm_pussy",1)
                                    if fm_pussy >= 10 and fm_pussy >= fm_bj:
                                        $ statschangenotify("fm_pussy",1)
                                        call morning_pussyfuck() from _call_morning_pussyfuck_1
                                    elif fm_pussy >= 10 and fm_pussy <= fm_bj:
                                        fmName.Formal "Do you want my pussy, or do you want a blowjob?"
                                        menu:
                                            "Pussy":
                                                call morning_pussyfuck() from _call_morning_pussyfuck_2
                                            "Blowjob":
                                                call morning_bj() from _call_morning_bj
                                            "How about both?":
                                                call morning_pussy_bj() from _call_morning_pussy_bj
                                    else:                            
                                        "You watch as [fmName.yourshort] hitches her thumbs under her panties and swiftly pulls them down over her thighs. She's got shapely legs, not at all bad for a woman in her forties. She pulls up her skirt, and sits back on the bed, spreading her legs as she does so."
                                        fmName.Formal "Happy now? {i}There's still a bit of defiance in her voice, some residual want to fight you, to stand up for herself{/i}"
                                        fp "Not quite. I would love to introduce my cock to your pussy, but I don't have time. Start masturbating!"
                                        fmName.Formal "{b}Gasp{/b} You... you want me to... rub... rub my pussy... here? In... in front of you?"
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
                                        fmName.Formal "Do you want a blowjob, or do you want my pussy?"
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
                            fmName.Formal "... Yes, [fp] ... "
                            "{i}[yourCapsfM] looks down at the floor, a slight blush on her cheeks, clearly uncomfortable with the situation. Maybe also a little afraid. Not really of you, but that she's excited, just a slight stirring in her loins, by all this...{/i}"
                            $ statschangenotify("fm_aro",1)                    
                            fmName.Formal "... You're in charge. What will you have me do?"
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
                            fmName.Formal "{b}her lip quivering...{/b} don't... just... you're gonna be late..."
                            fp "Where are you going? Come right back here and apologize!"
                            "[fmName.name] slowly turns, shuffles back towards you and, in a barely audible whisper..."
                            fmName.Formal "I'm sorry, [fp]. I apologize for my behavior"
                            fp "Fine. Don't let it happen again!"
                            $ fm_apologize = True
                            $ addtime(False,10)
                            "[yourCapsfM] walks out of the room"
                            $ morning_event_done = True                            
                            hide fm_standing                            
                            call late_morning() from _call_late_morning_2
                        # return
                
                label fm_morningchoice_reldom(called=False):
                    if called:
                        $ called = False
                        if fm_dom < 25:
                            $ statschangenotify("fm_dom",.5,True)                
                            $ statschangenotify("fm_rel",.5)    
                        $ fm_choice1_choice = "reldom"
                        fmName.formal "You're gonna be late for school, [fp]"
                        fp "Yes, yes, I know. Just... let me get dressed, and take a shower, okay?"
                        fmName.formal "Fine! I'm going to work. Make sure you lock the door when you leave!"
                        $ morning_event_done = True
                        call change_loc('fp bedroom') from _call_change_loc_14
                    
                label fm_morningchoice_rel(called=False):
                    if called:
                        $ called = False
                        if fm_rel < 25:
                            $ statschangenotify("fm_rel",1.5)
                        elif fm_rel < 40:
                            $ statschangenotify("fm_rel",1)
                        else:
                            $ statschangenotify("fm_rel",.25)
                        fmName.Formal "You need to stop staying up all night, [fp]. If you can't get out of bed in the morning, you'll fail both school and work, when that time comes."
                        fp "You know that there are jobs where you work both evenings and nights, right [fmName.informal]?"
                        fmName.Formal "Of course I do! But that doesn't mean that you should aim for those jobs. Now get your ass in gear!"
                        $ addtime(False,10)
                        if int(current_time[3:]) == 0:
                            $ already_late = True
                            fmName.Formal "You're late. School just started!"
                        else:
                            if int(current_time[:2]) <= 8:
                                if int(current_time[:2]) == 8:
                                    $ tt = abs(int(current_time[3:]))
                                    fmName.formal "You're late. School started [tt] minutes ago"
                                else:
                                    $ tl = abs(int(current_time[3:])-60)
                                    fmName.Formal "You're gonna be late. School starts in [tl] minutes."
                            else:
                                $ already_late = True
                                $ th = abs(int(current_time[:2])-8)
                                $ text = "You're late. School started over {0} {1} ago".format(th,'hours' if th > 1 else 'hour')
                                fmName.formal "[text]"
                        $ morning_event_done = True
                        call late_morning() from _call_late_morning_3
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
                fmName.Formal "[fp], time to get out of bed and have some breakfast"
                fp "Sure, [fmName.informal] - I'll be right down"
                hide fm_standing
                $ breakfast_jump = True
                # $ morning_event_done = True
                call fp_bedroom_loc(True) from _call_fp_bedroom_loc_3
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
                        call garage_scene from _call_garage_scene_2
                        call change_loc('garage') from _call_change_loc_15
                        call w_mc(True) from _call_w_mc
                        fp "{i}Oh, I better get going, if I'm gonna be on time{/i}"
                        call entrance_loc() from _call_entrance_loc_5
                    else:
                        # $ current_time = "07:45"
                        fp "{i}I should take the bike. It's a nice day for a ride anyways{/i}"
                        ## depending on the relationship with nk, there should be a possibility of her joining the ride to school
                    # return
                elif int(current_time[:2]) == 6 and day_week >= 5:
                    if not mc_f:
                        fp "Oh, it's really early... oh well, maybe I can get an early start and work on the bike today"
                        call garage_scene from _call_garage_scene_3
                        call change_loc('garage') from _call_change_loc_16
                        call w_mc(True) from _call_w_mc_1
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
                call school_on_time(True) from _call_school_on_time
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

        label after_fs_mad_morning(afs_mad=False):
            if afs_mad:
                $ afs_mad = False
                $ afsmm_r = renpy.random.random()
                if debug:
                    $ renpy.watch(str(afsm_r))
                if afsmm_r < .5 and shitty_morning and day_week <= 4:
                    nk ahead "Hi [fp]! You wanna ride to school?"
                    if not nk_driving:
                        fp "Hi [nk]... Didn't know you drove?"
                        nk ahead "My mom got me this for my birthday. Haven't really driven it much, but it's awesome."
                        $ nk_driving = True
                    else:
                        fp "Hi [nk]"
                    if bad_weather and rainstorm:
                        $ text1 = "Sure! That way I won't be late, not to mention drowning by the time I get there!\n{i}Damn, she saved my scrawny ass. Don't understand why she gets so much flak at school, she's nice...{/i}"
                        $ text2 = "No thanks, [nk]. I've got a buddy picking me up, he'll be here soon.\n{i}Even in this weather I'm not gonna get in a car with her... I'd never hear the end of it at school{/i}"
                    else:
                        $ text1 = "Sure! Then I won't be late!\n{i}Who cares if [nk] is not one of the popular kids - her offer is nice{/i}"
                        $ text2 = "No thanks! I'll just walk. Don't really wanna trust my life to your driving!\n{i}Don't wanna be caught dead in the same car as [nk]...{/i}"
                    menu:
                        "[text1]":
                            $ statschangenotify("nk_rel",1.5)                                    
                            $ renpy.pause(.25)
                            call school_on_time(True) from _call_school_on_time_1
                        "[text2]":
                            if bad_weather and rainstorm:
                                $ statschangenotify('nk_rel',-1)
                            else:
                                $ statschangenotify("nk_rel",-3)
                            $ renpy.pause(.25)
                            if renpy.random.random() < .4:
                                call school_walk_late(True) from _call_school_walk_late
                            else:
                                call sn_punishment_late(True) from _call_sn_punishment_late
                elif afsmm_r < .5 and not shitty_morning and day_week <= 4:
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
                        "Nah... I just wanna go by myself today, if you don't mind":
                            show nk_standing annoyed with dissolve
                            $ renpy.pause(.5)
                            call school_on_time(True) from _call_school_on_time_2
                        "No thanks, [nk]":
                            show nk_standing mad with dissolve
                            if nk_rel < 15:
                                $ nkrel = -.5
                            else:
                                $ nkrel = -.25
                            $ statschangenotify("nk_rel",nkrel)
                            $ renpy.pause(.5)
                            call school_on_time(True) from _call_school_on_time_3
                elif afsmm_r > .5 and day_week <= 4:
                    "[fp] walks to school, arriving on time"
                    call school_on_time(True) from _call_school_on_time_4
                # elif skip_breakfast:
                #     call skip_breakfast(True)
                elif day_week == 5 and not early_morning_we:
                    fp "Ah! This is gonna be a nice day! Weekends are my favorite time of the week!"
                    $ sat_event = True
                    call weekend_sat() from _call_weekend_sat
                elif day_week == 5 and early_morning_we:
                    $ sat_event = True
                    call weekend_sat() from _call_weekend_sat_1
                elif day_week == 6:
                    if not bad_weather and not rainstorm:
                        fp "Ah, this day is gonna be awesome!"
                    else:
                        fp "Ah, crap, it's raining cats and dogs. That sucks. No trip to the beach today, then."
                    $ sun_event = True
                    call weekend_sun(True) from _call_weekend_sun_3
                else:
                    "[fp] starts walking to school, knowing he'll be late to class. Wondering what Miss Novak's reaction will be..."
                    call sn_punishment_late(True) from _call_sn_punishment_late_1

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
                        call school_on_time(True) from _call_school_on_time_5
                    else:
                        show nk_standing annoyed with dissolve
                        nk annoyed "I don't think so, [fp]. Wouldn't feel right you looking at my work..."
                        "Seems your relationship with [nk] isn't strong enough to ask her for help yet"
                        call school_on_time(True) from _call_school_on_time_6
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
                    call school_on_time(True) from _call_school_on_time_7
            else:
                call school_on_time(True) from _call_school_on_time_8

    label travel_school(trs_called=False):
        if trs_called:
            $ trs_called = False
            call schoolbuilding_scene from _call_schoolbuilding_scene
            if late_oh_shit:
                $ current_time = "08:00"
                "Barely, but on time. Close call indeed!"
            else:
                $ addtime(False,25)
                if int(current_time[:2]) >= 8 and int(current_time[4:]) >= 0:
                    call school_walk_late_arrival_event(True) from _call_school_walk_late_arrival_event
                else:
                    "You arrive with plenty of time to spare before the bell rings"
                    call school_finished(True) from _call_school_finished

    label school_on_time(sot_called=False):
        if sot_called:
            $ sot_called = False
            call schoolbuilding_scene from _call_schoolbuilding_scene_1
            if late_oh_shit:
                $ current_time = "08:00"
                "{i}Barely, but on time. Close call indeed!{/i}"
            else:
                $ addtime(False,25)
                if int(current_time[:2]) >= 8 and int(current_time[4:]) > 0:
                    $ school_walk_late_arrival = True
                    call school_walk_late_arrival_event(True) from _call_school_walk_late_arrival_event_1
                else:
                    "You arrive with plenty of time to spare before the bell rings"
                    call school_finished(True) from _call_school_finished_1

    label school_walk_late(swl_called=False):
        if swl_called:
            $ swl_called = False
            $ swl_weights = [(0,6),(1,6),(2,1),(3,3)]
            $ swl_events = [
                ["see something","get a better look",False,'30'],
                ["hear a loud noise","figure out where the sound came from",False,'30'],
                ["feel suddenly cold","shake off the feeling of dread suddenly coming over you. There is no reason for you to feel like that, and you're not superstitous at the least",False,False],
                ["remember that you forgot your books","get home as fast as you can, so you don't waste more time",'1',False]
            ]
            $ which_event = weighted_choice(swl_weights)
            $ sense = swl_events[which_event][0]
            $ function = swl_events[which_event][1]
            $ addhour = swl_events[which_event][2]
            $ addminute = swl_events[which_event][3]
            if addhour:
                $ addtime(addhour,False)
            if addminute:
                $ addtime(False,addminute)
            $ text = "You're walking to school, when you suddenly {0}. You turn, trying to {1}".format(sense,function)
            "[text]"
            $ addtime(False,45)
    
    label school_walk_late_arrival_event(swl_ae_called=False):
        if swl_ae_called:
            $ swl_ae_called = False
            "{i}Arriving at school, you can see that you're late{/i}\nYou hurry up the stairs, trying to get to your classroom as fast as humanly possible"
            sn "Greetings, [fp]!"
            "[sn]s voice sneaks up on you as you hurry through the hallways"
            "You turn around, and see [sn] standing in one of the doorways leading to the teacher's lounge"
            fp "[sn]! Hi! I was just..."
            sn "You're {b}late!{/b}"
            "[sn] cuts you off, snapping at you"
            fp "Yes, [sn], I am. I'm sorry, but..."
            sn "I don't care, [fp]. You're not hurt, it seems, and doesn't seem to be in any distress, so I'm just gonna assume that you're late because of tardiness. Detention!"
            call sn_respond_detention(True) from _call_sn_respond_detention