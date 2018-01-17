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
            # return
        # else:
            # return
    label weekend_sun():
        if sun_event:
            if renpy.random.random() <= .5:
                fm "Could you help me open this, [fp]? I can't seem to get it open, and I need this for dinner today"
                menu:
                    "Yes, [fmName.informal], no problem. *you open the jar*":
                        if fm_dom <= 5:
                            $ statschangenotify("fm_dom",.5,True)
                            $ statschangenotify("fm_rel",1)
                        else:
                            $ statschangenotify("fm_rel",.5)
                    "No, [fmName.informal], I don't have time to help you right now":
                        $ statschangenotify("fm_dom",.5,True)
                        $ statschangenotify("fm_rel",-.5)
            $ sun_event = False
            # call livingroom_scene
            # call change_loc('livingroom')
            # return
        # else:
            # return

    label school_finished(sf_called = False):
        if sf_called:
            $ sf_called = False
            if detention_served:
                $ current_hour = "17:00"
            else:
                $ current_hour = "15:05"
                if school_hacker:
                    if school_hacker_first_thought:
                        "{i}You've been thinking about what happened with your sister, and you were almost sure that it wouldn't be possible to manage that many mistakes by accident. Also, they hadn't found out who had updated the records... that's usually registered...{/i}"
                        $ school_hacker_first_thought = False
                    fp "I should go talk to [scn]. She loves me, I'm sure I'll be able to get some answers from her!"
                    menu:
                        "Go talk to [scn], try to find out more about what happened to [fsName.yourformal]":
                            fp "Hi, [scn]!"
                            scn "Hi, [fp] - did you have an appointment today? I don't have anything on screen, it seems?"
                            fp "Nah, [scn] - I just swung by to say hi! {i}You give [scn] a quick wink{/i}"
                            "{i}[scn] is blushing a bit{/i}"
                            #"Oh, you silly boy, you'll make a cradle snatcher out of me! I'm more than twice your age, you know!" 
                            scn "Oh, you silly boy! You shouldn't flirt with women more than twice your age, [fp]! {i}She's trying to sound scolding, but she's not very successful. Her slight smile gives away that she's mostly pleased with the situation{/i}"
                            fp "{i}Trying to look sad and apologetic{/i}\nOkay, [scn]. I promise I won't do it again!"
                            scn "..."
                            fp "Ah, who am I kidding! I will definitely be doing it again!"
                            "[scn] looks pleased, although she's still blushing slightly"
                            fp "Oh, and I wanted to ask you about something. I know you're not supposed to talk about other students, but it's about [fmName.myformal]. She was in here the other day, and I thought what she told me after sounded... a bit weird."
                            scn "Yeah, I remember. The whole thing is a bit embarrassing, to be honest"
                            fp "Oh?"
                            scn "Yeah... {i}She lowers her voice, obviously not wanting to be overheard{/i}\nYou see, there is evidence that none of the teachers did this, whether by accident or by malice"
                            fp "Oh... kay? So, none of the teachers, huh?"
                            scn "Yeah... interprete that as you will"
                            fp "{i}So, there {b}is{/b} a chance someone did this on purpose - or, maybe even just by accident, messing with the internal systems. Damn, I wish I was a little bit more knowledgeable about computers... I have no idea what kind of knowledge this would take, nor if anyone here at school would be capable. Maybe I could ask [nr]. He's pretty geeky, and probably knows who is able to do something like this...{/i}"
                            $ school_hacker = False
                            $ school_hacker_2 = True                         
                            $ call_nr = True
                            call evening_home(True)
                        "Nah, not today, I'll do it tomorrow instead":
                            call evening_home(True)
            "After school, you decide to just trek back home. No plans for today, and not that much interesting happening in town anyway"
            call evening_home(True)

        label sn_punishment_late(snp_called=False):
            if snp_called:
                $ snp_called = False
                call schoolbuilding_scene
                $ addtime(False,25)
                sn "You're late! This will not be tolerated, [fp]. You will be on time, or I will be forced to reduce your grades for this semester! For now, you have detention, come meet me here after you're done with classes for today."
            
        label sn_respond_detention(snr_called = False):
            if snr_called:
                $ snr_called = False
                menu:
                    "Yes, [sn]!":
                        $ statschangenotify("sn_dom",-1,True)
                        $ statschangenotify("sn_rel",1)
                        call sn_detention(True)
                    "Mouth off to [sn]":
                        fp "Oh, shut it! I'm a few minutes late. It's not like I do this often, and it wasn't like I tried to arrive late. Damn, \"reduce my grades\" - you know you'll have to give me a warning first, and even a letter that I might receive a reduced grade... and I have definitely not deserved that, yet"
                        sn "How dare you talk to me like that? Go see [sp] right now! I will not have a student talk to me like this!"
                        fp "Oh, stop pretending! You're not a bad-ass, [sn]. You never will be."
                        sn "{b}NOW!{/b}"
                        fp "Fine, fine..."
                        "You head to [sp]s office"
                        $ statschangenotify("sn_dom",1.5,True)
                        $ statschangenotify("sn_rel",-1,True)
                        $ statschangenotify("sn_aro",1)
                        call principal_after_punishment_late(True)
    
    label dinner_events(de_called=False):
        if de_called:
            $ de_called = False
            if dinner_event:
                if day_week <= 4:
                    if fs_mad:
                        fm "Hey [fp]. It's dinnertime soon, do you wanna go see if you can find [fsName], and tell her to get ready?"
                        fp "Well... [fsName] isn't really speaking to me at the moment..."
                        fm "Oh? What did you do now?"
                        fp "Why do you just assume I did anything? I'll talk to her, but now might not be the best time... I'll tell her dinner is ready if I see her, okay?"
                        fm "Fine. But you fix this with your sister, okay?"
                        fp "I will, [fsName.shortrole], I will"
                        $ dinner_event = False
                        call kitchen_loc(True)
                    else:
                        $ dinner_event = False
                        call kitchen_loc(True)
                if day_week >= 5:
                    $ dinner_event = False
                    call kitchen_loc(True)


    label evening_home(evh_called=False):
        if evh_called:
            $ evh_called = False
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
                
                if renpy.random.random() > .5 and not school_hacker_3:
                    if  current_month >= 5 and current_month <= 8 and not detention_served:
                        "You decide to just lounge by the pool for a while, trying to stand the heat"
                else:
                    if not detention_served:
                        if not mc_f:
                            if school_hacker_3:
                                menu:
                                    "So... you can either work a bit on your bike, or call up [nr] and see if he can give you some info about [fsName.yourformal]s problems"
                                    "Go work on bike":
                                        call garage_scene
                                        call change_loc('garage')
                                        call w_mc(True)
                                    "Call [nr]":
                                        pass
                            else:
                                "You decide that you can spend a few more hours on your bike today"
                                call garage_scene
                                call change_loc('garage')
                                call w_mc(True)
                            if current_hour[:2] > 19:
                                "You're feeling a bit tired, after school, and working on your bike, so you decide taking a shower will be a nice relief right now"
                                call taking_shower_evening(True)
                            else:
                                call garage_scene
                                call change_loc('garage')
                                call w_mc(True)
                                "After putting in a few more hours on the bike, you decide that the rest of the evening should be spent doing less arduous tasks, and head inside to watch some TV, maybe play some games"
                                call tv_games_evening(True)
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
                                    $ statschangenotify("fp_sts",-1)
                if not evening_event:
                    call end_of_day()
                else:
                    call evening_event_label()

    label principal_after_punishment_late(pap_called=False):
        if pap_called:
            $ pap_called = False
            $ addtime(1, False)
            sp "[fp]! What have you done, to be sent to me?"
            fp "I mouthed off to Miss Novak."
            fp "She was yelling at me for being late, and I just lost it."
            fp "I'm sorry."
            sp "You need to control your temper, son."
            sp "You have a tendency to end up in these situations, and I don't think we can ignore it much longer."
            $ statschangenotify("fp_att",.5,True)
            $ statschangenotify("punishment_late",1)
            if punishment_late >= 5:
                sp "I will need to call your parents, and tell them about this. You can go"
                $ statschangenotify("fm_rel",-2.5)
            call school_finished(True)

    label sn_detention(snd_called = False):
        if snd_called:
            $ snd_called = False
            "After arriving at school, and dealth with [sn]s blow-out, you go about your day as normal - attending classes, avoiding freshmen, trying to catch a glance of the cheerleaders rehearsing..."
            "But, come end of day, you need to get your ass to [sn]s classroom, and attend detention."
            $ current_hour = "15:05"
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
                                        call school_finished()
                                    "Sit down, but refrain from peeping up her skirt":
                                        call sn_lookaway_detention()
                            else:
                                "You notice [sn] catching your glance, and feel her ice-cold stare as she haughtily asks you if you're done undressing her with your eyes"
                                sn "You're gonna get another punishment for that, [fp]. Meet here after school tomorrow, for another round of detention!"
                                $ statschangenotify("sn_aro",.5,True)
                                $ statschangenotify("sn_rel",-1)
                        "Manage to look away":
                            call sn_lookaway_detention()
                    label sn_lookaway_detention():
                        "You decide to play it cool, and just get the detention done with, so you can go home"
                        call school_finished()
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
                        call school_finished()
                    else:
                        "You get out your books, and start studying for next weeks algebra-test"
                        call school_finished()
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
                    call school_finished()
                else:
                    "You get out your books, and start studying for next weeks algebra-test"
                    call school_finished()

    label taking_shower_evening(tse_called=False):
        if tse_called:
            $ tse_called = False
            "You decide to take a shower after a long day"
            $ fpshower = True
            call change_loc('bathroom_loc')

    label talk_fs(tfs_called=False):
        if tfs_called or tfs_cfs:
            $ tfs_called = tfs_cfs = False
            show fs_standing ahead with dissolve
            if not pb_return:
                fs ahead "Hey [fp]!"
                fp "Hey, [fsName.role] - what's up?"
                if pb_return:
                    fs "Have you taken my buttplug?"
                fs "Have you been in my room?"
                if fs_bedroom_ach:
                    menu:
                        "Yes (offer no explanation)":
                            $ result = "true"
                        "Yes, I went in there looking for you the other day, when I wanted to talk to you":
                            $ result = "lie (white)"
                        "You mean except when I stumbled in on you earlier?":
                            $ result = "question"
                        "No (lie)":
                            $ result = "lie"
                else:
                    menu:
                        "Yes (lie)":
                            $ result = "lie"
                        "Yes - I went in there looking for you the other day, when I wanted to talk to you":
                            $ result = "lie (white)"
                        "You mean except when I stumbled in on you earlier?":
                            $ resule = "question"
                        "No (tell the truth)":
                            $ result = "true"
                if result == "lie":
                    fs "You're lying"
                elif result == "question":
                    fs "Answering with a question of your own, huh? I guess you're hiding {i}something{/i}!"
                else:
                    fs "That's actually refreshing. Truth!"
            show fs_standing ahead with dissolve
            # $ renpy.watch(result)
            $ renpy.pause()

    label evening_event_label(ee_called=False):
        if ee_called:
            $ ee_called = False
            if nk_school_assignment_evening and day_week <= 4:
                $ nk_school_assignment_evening = False            
                "{b}*ding dong*{/b}"
                fm "{b}[fp], can you get that?{/b}"
                call entrance_scene
                "You go to get the door, expecting it to be [nk]"
                nk smile "Hi [fp]."
                "[nk] is outside, all smiles and with a stack of books in her arms."
                fp "Hi... you do know we have Internet on the premises, right? And on our phones, and pretty much in every Starshots in town...?"
                nk smile "I know, silly. But I've always felt that books provide some... well, they make it easier to focus on the task at hand!\n{i}she lets out a cute little laugh{/i}"
                fp "Well, I was thinking we could set up in my room. I have set up a double set of chairs, I have my computer there, and we should have room enough to go through the books you brought. {i}You grab the books from her, and motion for her to come along{/i}"
                call fp_bedroom_scene
                fp "Long time since you've been here, I've changed a few things"
                nk ahead "{i}She looks around your room{/i}\nI can see that. No more supercar wallpaper :D"
                fp "Yeah, yeah. Stop mocking me. I was eight!"
                nk smile_open "Okay, okay... let's get this show on the road, shall we?"
                if nk_rel > 15:
                    "[nk] steps up to you, grabs you, and presses against you. Soon after she's kissing you agressively"
                    $ statschangenotify("nk_aro",.5)
                    "You're stunned, and for a little while you just stand there, letting her kiss you. {i}This was not what you thought she meant when she said \"let's get this show on the road\"{/i}"
                    "After a short, confused moment, you decide that this is definitely better than doing homework, and start kissing her back"
                    $ statschangenotify("nk_rel",3,True)
                    $ statschangenotify("nk_aro",1.5)
                    if nk_rel > 25:
                        "This is just a placeholder for this event"
                    elif nk_rel > 30:
                        "This is just a placeholder for this event"
                else:
                    "You spend a few hours studying, chatting and generally just catching up"
                    $ statschangenotify("nk_rel",2)
                    $ addtime(5,False)
                call end_of_day(True)