define config.screenshot_pattern = "D:\Dropbox\RenPy-games\Screenshots\HSS-screenshot%04d.png"
label splashscreen:
    scene black 
    $ renpy.pause(1)
    show text "{size=60}{color=#ffffff}Studio Errilhl Presents ... {/color}{/size}" with dissolve
    $ renpy.pause(2)
    hide text with dissolve
    if not persistent.splash_screen:
        show image "images/hss-logo.png" with dissolve:
            xalign .5 yalign .5
        $ renpy.pause(2)
        hide image "images/hss-logo.png" with dissolve
        $ renpy.pause(.75)
        if persistent.patch_enabled:
            show text "{size=30}{color=#ffffff}HSS - High School Shenanigans is a story about a very hot summer, where you'll play as <your name here>\n(You can name your own character, but the default is \"Marten\", so let's just go with that for now). So, you play as Marten, on his last stretch of high school, aiming to finish school, have some fun, fix his bike, and take his dream cross-country trip on it - but first, there's the exams. And the hot chicks... (among them, his mother and sister, who is both hot, and definitely part of his nighttime jerk-off sessions), the pool, the neighbor girl, and so much more - pretty much like there is in every teenager's life. You control what happens, who you eventually hook up with, what you end up doing with them, and so on and so forth.\n\n{b}Note that this is a very early Alpha-relese, and that quite a lot of the events haven't been added yet,\nor for those that have, might abruptly end. The game is playable,\nbut you won't reach a fulfilling conclusion as of yet!{/b}{/color}{/size}" as line1 with dissolve
        else:
            show text "{size=30}{color=#ffffff}HSS - High School Shenanigans is a story about a very hot summer, where you'll play as <your name here>\n(You can name your own character, but the default is \"Marten\", so let's just go with that for now). So, you play as Marten, on his last stretch of high school, aiming to finish school, have some fun, fix his bike, and take his dream cross-country trip on it - but first, there's the exams. And the hot chicks... and the pool, the neighbor girl, and so much more - pretty much like there is in every teenager's life. You control what happens, who you eventually hook up with, what you end up doing with them, and so on and so forth.\n\n{b}Note that this is a very early Alpha-relese, and that quite a lot of the events haven't been added yet,\nor for those that have, might abruptly end. The game is playable,\nbut you won't\nreach a fulfilling conclusion as of yet!{/b}{/color}{/size}" as line1 with dissolve
        show text "{size=20}{color=#ffffff}Click to continue{/click}{/size}" as line2 with dissolve:
            xalign .5 yalign 1.0
        $ renpy.pause()
        hide line1
        hide line2
        with dissolve
        show text "{size=30}{color=#ffffff}The story is purely fictional, and does not reflect the creator's worldview.\nWe do not condone, nor support the actions and opinions of the characters{/color}{/size}" with dissolve
        $ renpy.pause(3)
        hide text with dissolve
        $ renpy.pause(1)
        show text "{size=60}{color=#ff0000}This game has the rollback / history enabled. Unfortunately, using it might mess up the inventory-system, so use at your own risk - it won't break the game, but some items may show up repeatedly, and other might not check correctly (for stat-mods and such). Come Beta (or earlier if possible), the rollback function will be disabled. Unfortunately, at the current stages, there are no real workarounds for this issue{/color}{/size}" as line1 with dissolve
        show text "{size=20}{color=#ffffff}Click to continue{/click}{/size}" as line2 with dissolve:
            xalign .5 yalign 1.0
        $ renpy.pause()
        hide line1
        hide line2
        show text "{size=30}{color=#ffffff}Code / story by Studio Errilhl\nCharacter art by DivineChihaya{/color}{/size}"
        $ renpy.pause(4)
        $ persistent.splash_screen = True
    return

label after_load:
    $ updateInventory()
    return

init 1:
    defineDynamicName fmName:
        name "Anne"
        informal "Anne"
        formal "Anne"
        role "landlady"
        myformal "my landlady"
        yourformal "your landlady"
        myinformal "my landlady"
        yourinformal "your landlady"
    defineDynamicName fsName:
        name "Juliette"
        informal "Jules"
        formal "Juliette"
        role "housemate"
        myformal "my housemate"
        yourformal "your housemate"
        myinformal "my housemate"
        yourinformal "your housemate"

label start:
    $ conditions = Conditions() ## enables the conditions-parameter used for assigning conditions to disable / enable choice-items
    $ backpack = Container()
    $ updateInventory()

    $ current_hour = "09:00"
    call fp_bedroom_scene
    ## intro - this is shown only once, when starting the game from the beginning

    python:
        fpinput = renpy.input("First, we'll need to know your name (default, Marten):")
        fpinput = fpinput.strip()
        if not fpinput:
            fpinput = "Marten" 

    if persistent.skipintro:
        menu:
            "View intro":
                jump viewintro
            "Skip intro":
                jump skippedintro
    label viewintro:
        fp "{i}Hi! I'm [fp], and this is the story of what happens this summer. Did that come out a little stilted? I felt that it did. Oh, well, I'm not that well versed in being a narrator. Hence, I will mostly conduct this in a first-person perspective - you know, \"Hi, I'm [fp] and you're about to be taken for a wild ride!\" That sound good? {b}GREAT!{/b}{/i}"
        fp "{i}Now, where were we? Oh, right. Yeah. This summer. You know, the one you're gonna be playing through? So much have happened, I don't even really know where to start. Hmm... Maybe May? Or... no, I think we'll have to go all the way back to April, actually. You see, I was attending my last high-school semester. Grinding away, trying to get my grades up that last bit, all the while trying not to become a total geek.{/i}"
        fp "{i}Sorta failing, but I wasn't too worried. I had plans, both for the summer after end of high school, and for the year after. Oh, I was gonna go to college, of course, but I was planning on taking some time off before that, and take a cross-country trip. I'd been working on my bike for over a year, and now it was just a little bit left to do, before I could put on the very last, finishing touches. And, when it got done, I'd be taking it, and myself across the country.{/i}"
        fp "{i}I was planning on starting more or less were I've grown up, on the East coast, and just drive - visiting as many states, online friends and aquaintances, landmarks and interesting spots I could possibly manage over the 3-4 months I was planning to spend. That was basically what was on my mind those last couple months of high school. \"What to do AFTER high school\". I completely failed to take into account what would happen BEFORE I finished...{/i}"
        fp "{i}So, there we are. April 1st, a Saturday, if I'm not mistaken. I'd just woken up, and was on my way downstairs to the kitchen when I heard noises coming from [fsName.formal]'s room. Usually I wouldn't care, but those sounds sounded... muffled. Like she was trying to keep it down, but failing. And I was curious what the hell she was doing. So, I walked up to her door, thinking I would just try to listen in, see if I could figure out what was going on.{/i}"
        fp "{i}Unfortunately, spying has never been my strong suit, and the door wasn't closed all the way... so when I leaned against it, I suddenly found myself tumbling into her room. Not very elegantly, mind. Quite ungracefully, in fact. But... that wasn't what was on my mind AT ALL.{/i}"
        call fs_intro_scene
        fp "{i}[fsName.Myformalrole]'s room has the bed opposed the door. So right in front of my prone body, on her bed... well, half off her bed, was [fsName.informal], naked from the waist down, with most of her right hand buried between her legs, which, mind you, was spread quite wide over the edge of the bed. I couldn't really have had a better viewpoint even if I was sitting right in front of a porn-shoot.{/i}"
        call upper_hallway_scene
        show fs_standing mad with dissolve
        fp "{i}Didn't last long, though. About 5 seconds after me landing on her bedroom floor, I got hit with something hard! Then the shouting began, and 10 seconds after that, I was out in the hallway again, with a furious, but still very half-naked sister yelling at me. I'm still amazed that [fmName.informal] didn't show up... THAT would've been embarassing, for both of us... mostly for me.{/i}"
        fp "{i}Thankfully, [fsName.informal] realised what she was doing (partly because I had a raging boner in my boxer's, I guess) - turned on her heel, and went into her room again - this time locking the door.{/i}"
        hide fs_standing with dissolve        
        call upper_hallway_bathroom_scene
        fp "{i}Me... I went to the bathroom and jerked off. Yes, I know she's [fsName.myformal], and all that, but DAMN.{/i}"
        fp "{i}Okay... that might have been a bit TMI. I'm sorry. I just wanted you to understand what happened. And how that sort of led to... other things that happened as well. During that summer. You know... spring. Summer. End of high-school. The time I had all planned out. The plans that really didn't happen. Like... at all.{/i}"
        "So... the coming days, weeks and months, you'll be trying to pass your exams, finish your bike, getting some action, and generally being a high school senior going on freedom!"
        $ persistent.skipintro = True
        $ fs_mad = True        
        return
    label skippedintro:
        $ fs_mad = True
        show screen ingame_menu_display()
        fp "So. Quick recap: I woke up on April 1st, tried to somewhat remotely function and seem awake, and figure out what to with the day. Then, a little later, shellshocked, and trying to figure out how to get the image of my naked [fsName.role] off my mind, I decided spending the day working on my bike would be as good a way as any..."
        # if current_month == 3 and current_month_day == 1:
        $ skip_breakfast = True
        call skip_breakfast(True)
        return

    label day_start():
        $ detention_served = False
        $ late_oh_shit = False
        $ breakfast_jump = False
        $ shitty_morning = False
        $ count = 0
        $ end_bike_repair = False
        $ find_panties = True if renpy.random.random() > .75 else False
        $ morning_event_done = False
        $ gp = random.choice(fs_p)
        $ br = random.choice([0,1,2,3])
        if wcount < 5:
            $ wcount += 1

        if renpy.random.random() > .75:
            $ bad_weather = True
            $ rainstorm = True
        else:
            $ bad_weather = False
            $ rainstorm = False

        if fs_mad:
            $ statschangeNotify("fs_rel",-1)
            pass
        if mc_b >= mc_b_max:
            $ mc_f = True
        else:
            $ mc_f = False
        
        # breakfast choices - the bf_weights is updated when you pick something, and will change the weight depending on whether or not you benefit or not
        $ bf_weights = [(0,5),(1,4),(2,2),(3,1),(4,5),(5,2),(6,2),(7,4),(8,1),(9,4),(10,2)]
        $ breakfast = [
            ["pancakes","I love your pancakes",2,"fm_rel",.5], #food, reply, modifier, stat, weight-modifier
            ["bacon and eggs","I'm gonna get fat if I continue eating this",1,"fm_rel",.25],
            ["scones","I don't really like scones",-1,"fm_rel",.25],
            ["scones","Ah, scones again... okay, I guess they'll do",0,"fm_rel",.25],
            ["sandwiches","Ah, I just love those sandwiches",2,"fm_rel",.5],
            ["beans and bacon","What am I? A cowboy? Seriously",-1,"fm_rel",.25],
            ["cereal","Well, if there's nothing else...",-1,"fm_rel",.25],
            ["cereal","Cereal is fine",1,"fm_rel",.25],
            ["muffins","I'm not in the mood for anything sweet. I'll just have coffee",0,"fm_rel",.25],
            ["muffins","Sure, lemme have them",1,"fm_rel",.25],
            ["muffins","These muffins taste... I'll just have coffe, thanks",-1,"fm_rel",.25]
        ] 

        $ breakfast_select = weighted_choice(bf_weights)
        $ breakfast_food = breakfast[breakfast_select][0]
        $ breakfast_reply = breakfast[breakfast_select][1]
        $ breakfast_mod = breakfast[breakfast_select][2]
        $ breakfast_att = breakfast[breakfast_select][3]
        $ breakfast_weight = breakfast[breakfast_select][4]
        if breakfast_mod >= 0:
            $ new_weight = bf_weights[breakfast_select][1] + breakfast_weight
        else:
            $ new_weight = bf_weights[breakfast_select][1] - breakfast_weight
        $ bf_weights[breakfast_select] = (bf_weights[breakfast_select][0],new_weight)

        # call day_wrapper()
        if int(current_hour[:2]) in night:
            if day_week <= 4:
                $ mh = format(int(morning[renpy.random.randint(0,(len(morning)-3))]),"02d")
                $ mm = format(renpy.random.randint(00,30),"02d")
                call settime(mh,mm)
            elif day_week >= 5:
                $ mh = format(int(random.choice(morning)),"02d")
                $ mm = format(renpy.random.randint(00,59),"02d")
                call settime(mh,mm)
                # if int(current_hour[:2]) == 6:
                #     call addtime(1, False) 

        call day_wrapper()

        label day_wrapper():
            if int(current_hour[:2]) in morning:
                call morning_events()
                # "this is the morning time"
            elif int(current_hour[:2]) in day:
                # call day_events()
                "this is the day time"
            elif int(current_hour[:2]) in night:
                # call night_events()
                "this is the night time"
            # if day_week <= 4: #monday through friday
            #     if 6 <= int(current_hour[:2]) <= 8 and morning:
            #         call fp_bedroom_loc(True)
            #     if 8 < int(current_hour[:2]) <= 15 and schoolday:
            #         "schoolday weekday"
            #         # what happens at school
            #     if 15 <= int(current_hour[:2]) <= 17 and detention and schoolday:
            #         "detention happened schoolday"
            #     elif 15 <= int(current_hour[:2]) <= 17 and day:
            #         "nothing happened, home after school"
            #         # what happens at home in the evening
            #     if 17 < int(current_hour[:2]) < 22 and evening:
            #         "evening schoolday"
            #         # night events / sleep
            #     if 22 < int(current_hour[:2]) and night:
            #         "night, first pass schoolday" #first part of night
            #     if int(current_hour[:2]) < 5 and night:
            #         "night, second pass schoolday" #second part of night
            # else: #weekend
            #     if 6 < int(current_hour[:2]) <= 12 and morning:
            #         call fp_bedroom_loc(True)
            #     if 12 < int(current_hour[:2]) < 19 and day:
            #         "weekend daytime"
            #         # daytime events
            #     if 19 < int(current_hour[:2]) < 22 and evening:
            #         "weekend evening"
            #         # evening events
            #     if 22 < int(current_hour[:2]) and night:
            #         "weekend first pass night" #first part of night
            #     if int(current_hour[:2]) < 5 and night:
            #         "weekend second pass night" #second part of night
            # # jump day_start
            # return
            # return

#location changer
    label change_loc(locname=False,timeadd=False,char=False,imgname=False):
        if timeadd:
            call addtime(False, 30)
        if locname:
            $ tmpname = locname.replace(' ','_')+"_scene"
            call expression tmpname
            show screen location(locname)
            if char and imgname:
                show expression "images/characters/[char]/body/standing/[imgname].png" as character at fs_standing_ahead_ani with dissolve:
                    zoom .65
                    xpos .7
                    ypos 1.0
                    xanchor .5
                    yanchor .75
            call screen empty()
            hide screen empty
            hide screen location
            hide character
        # return

#event-labels


    label travel_school(trs_called=False):
        if trs_called:
            $ trs_called = False
            call schoolbuilding_scene
            if late_oh_shit:
                $ current_hour = "08:00"
                "Barely, but on time. Close call indeed!"
            else:
                call addtime(False,25)
                if int(current_hour[:2]) >= 8 and current_hour[4:] >= '00':
                    $ school_walk_late_arrival = True
                    call school_walk_late_arrival_event(True)
                else:
                    "You arrive with plenty of time to spare before the bell rings"
                    call school_finished()
            # return
        # else:
        #     return

    # if school_walk_late_arrival:
    #     label school_walk_late_arrival_event(called=False):
    #         if called:
    #             "{i}Arriving at school, you can see that you're late{/i}\nYou hurry up the stairs, trying to get to your classroom as fast as humanly possible"
    #             sn "Greetings, [fp]!"
    #             "[sn]s voice sneaks up on you as you hurry through the hallways"
    #             "You turn around, and see [sn] standing in one of the doorways leading to the teacher's lounge"
    #             fp "[sn]! Hi! I was just..."
    #             sn "You're {b}late!{/b}"
    #             "[sn] cuts you off, snapping at you"
    #             fp "Yes, [sn], I am. I'm sorry, but..."
    #             sn "I don't care, [fp]. You're not hurt, it seems, and doesn't seem to be in any distress, so I'm just gonna assume that you're late because of tardiness. Detention!"
    #         # jump miss_novak_respond_detention


    label w_mc(wmc_called=False):
        if wmc_called or wmc_cfs:
            # $ wmc_called = wmc_cfs = False
            $ c = 0
            $ maxc = 1 if int(current_hour[:2]) == 6 else 2 if int(current_hour[:2]) > 14 and int(current_hour[:2]) < 22 and day_week <= 4 else 3
            $ events = [0,1,2,3,4,5,6,7,8,9,10]
            $ outside_events = [77,88,99]

            label repeat_event(event=0):
                if int(current_hour[:2]) < 7 and day_week <= 4 and event not in outside_events:
                    $ choice1 = "Hm... I have at least an hour before school. Maybe I can get a bit done on the bike"
                    $ choice2 = "Or, I could just go back inside, eat breakfast and leave early"
                    if not event or event == 0:
                        $ event = 7
                elif int(current_hour[:2]) < 7 and day_week >= 5 and event not in outside_events:
                    $ choice1 = "Hm... I have at least an hour before anyone else is out of bed. I can probably get a bit done before breakfast"
                    $ choice2 = "Or... I could go back inside, take a shower, get some breakfast, and get back out here later"
                    if not event or event == 0:                    
                        $ event = 7
                elif int(current_hour[:2]) >= 7 and day_week <= 4 and event not in outside_events:
                    $ choice1 = False
                    $ choice2 = "I don't really have time to work on the bike right now. I need to get to school"
                    if not event or event == 0:
                        $ event = 3
                elif 14 < int(current_hour[:2]) < 20 and event not in outside_events:
                    $ choice1 = "I can probably do at least a couple hours of bike repair today"
                    $ choice2 = "Or I could go back in the house, see if there's anything on TV, or play a game..."
                    if not event or event == 0:                    
                        $ event = 4
                elif sc <= 3 and event not in outside_events:
                    $ choice1 = "I have the entire day off. Maybe I could spend some time on the bike, see if I can get some traction on the rebuild"
                    $ choice2 = "Or, I could just slack off today, and work on the bike another day"
                    if not event or event == 0:                    
                        $ event = 5

                if event in events:
                    menu:
                        "[choice1]" if choice1:
                            if event == 7:
                                call addtime(1,False)
                                if renpy.random.random() > .5:
                                    if backpack.has_item(toolbox_item):
                                        $ mc_b += 2
                                    else:
                                        $ mc_b += 1
                                $ event = 77
                                call repeat_event(77)
                            elif c < maxc:
                                call addtime(1, False)
                                if renpy.random.random() > .5:
                                    if backpack.has_item(toolbox_item):
                                        $ mc_b += 2
                                    else:
                                        $ mc_b += 1                                        
                                $ c += 1
                                $ mc_p = (float(mc_b)/float(mc_b_max))*100
                                $ mc_p = "{0:.2f}".format(mc_p)
                                $ renpy.notify("You're currently "+str(mc_p)+"% done with the bike")
                                call repeat_event()
                            else:
                                $ event = 88
                                call repeat_event(88)
                        "[choice2]" if choice2:
                            $ event = 99
                            call repeat_event(99)
                elif event == 77:
                    $ text = "I should go in, {0} and {1}".format("take a shower","have breakfast and get ready for school" if day_week <= 4 else "have breakfast")
                    "[text]"
                    call kitchen_scene
                    call breakfast_interaction(True)
                elif event == 88:
                    "You're done working on the bike today"
                    call outside_loc()
                elif event == 99:
                    "You don't really wanna work on the bike right now"
                    call outside_loc()
                # return
        # else:
        #     return

#         # locations
#         label upper_hallway_bathroom_loc():
#             if smallkeys_added:
#                 "{i}Hmm... a pair of keys. Haven't seen them before. Wonder what they open?\nShould I take them?{/i}"
#                 menu:
#                     "Take keys":
#                         $ backpack.add_item(small_keys_item)
#                         $ smallkeys_added = False
#                     "Leave keys":
#                         $ smallkeys_added = False
#             if fPshower:
#                 call addtime(1, False)           
#                 fp "{i}Ah, that was refreshing{/i}"
#                 $ fPshower = False
#             if fPsink:
#                 call addtime(False,15)
#                 fp "{i}Good to get the filth off my hands{/i}"
#                 $ fPsink = False
#             call upper_hallway_bathroom_scene
#             call change_loc('upper hallway bathroom')
#             return

#         label schoolbuilding_loc():
#             call schoolbuilding_scene
#             call change_loc('schoolbuilding')
#             return

#         label beach_loc():
#             call beach_scene
#             call change_loc('beach')
#             return

#         label skip_breakfast(called=False):
#             # $ skip_breakfast = False
#             if called:
#                 $ called = False
#                 call addtime(False,30)
#                 fp "{i}Deciding to skip breakfast, to avoid uncomfortable incidents with [fsName.myformal], I go straight to the garage.{/i}"
#                 call garage_scene
#                 if not mc_f:
#                     fp "Ah, at least working on my bike will get my mind off things."
#                     label firstday_mc_work:
#                         menu:
#                             "Hm. Working on the bike usually calms me a bit, I might be able to get some work done today":
#                                 label firstday_mc_work_internal():
#                                 if count < 3:
#                                     fp "{i}Damn... I just can't get that image out of my head...{/i}\nI've got to get this sorted, or else I won't be able to do anything all day."
#                                     call addtime(1,False)
#                                     $ count += 1
#                                     menu:
#                                         "Continue to work, trying to get your emotions under control":
#                                             call firstday_mc_work_internal()
#                                         "Try to find [fsName.yourformal], and see if she'll willing to talk with you":
#                                             $ firstday_talk = True
#                                             $ count = 3
#                                             call firstday_talk_fs(True)
#                                     # if firstday_talk:
#                                     label firstday_talk_fs(called=False):
#                                         if called:
#                                             $ called = False
#                                             call livingroom_scene
#                                             show fs_standing annoyed with dissolve
#                                             if talk_later:
#                                                 call addtime(10)
#                                             else:
#                                                 call addtime(False,30)
#                                             fp "Hi, [fsName.informal]. Can we talk?"
#                                             show fs_standing mad with dissolve
#                                             fs mad "Fuck you"
#                                             show fs_standing ahead with dissolve
#                                             $ text = "Look, I'm really sorry about {0}! I didn't mean to perv on you, {1}.".format("this morning" if first_day else "the other day",  )                                    
#                                             fp "[text]"
#                                             show fs_standing mad with dissolve
#                                             fs "So, you just happened to be leaning against my door because...?"
#                                             fp "Well, that bit is true, but I was just trying to figure out what the sounds coming from your bedroom was. Honestly!"
#                                             show fs_standing annoyed with dissolve
#                                             fs annoyed "So... you heard noises coming from my bedroom, and your first instinct is \"Let's check out the sounds from [fsName.myformal]s bedroom\"?"
#                                             fp "Yeah...\n{b}you muster a foolish grin{/b}\nWhen you put it like that, it sounds sort of stupid..."
#                                             show fs_standing ahead with dissolve
#                                             call addtime(False, 30)
#                                             fs ahead "Can we just agree that unless I'm screaming bloody murder... and even if I am, check first!, that you do not go creeping about my door?"                                    
#                                             fp "Sure, [fsName.informal]. I am really sorry!"
#                                             fs ahead_eyes_closed "Yeah, yeah... not as sorry as me..."
#                                             fp "Huh?"
#                                             show fs_standing ahead with dissolve
#                                             fs ahead "Your timing was beyond belief bad!"
#                                             fp "Uhh... yeah, I get that... I stumbled in on you almost bare naked..."
#                                             show fs_standing flustered with dissolve
#                                             fs flustered "No, you idiot. I was about 5 seconds away from an awesome orgasm. Let's just say you ruined the mood."
#                                             show fs_standing blushing with dissolve
#                                             fp "{i}Oh, shit...\nDid she actually just say that?{/i}\nI'm really sorry? Look, I owe you one, okay. If you need anything, a ride, drinks, anything, just ask, okay?"
#                                             show fs_standing smile_open with dissolve
#                                             fs smile "{b}Smiling now...{/b}\nOh, don't you worry. I will ask. You bet on it!"
#                                             "With that, she picks herself off the couch, and wanders off"
#                                             call addtime(1,False)
#                                             $ statschangeNotify("fs_rel",3,True)
#                                             $ firstday_talk = False
#                                             $ firstday_view = 0
#                                             $ firstday_after_talk = True
#                                             if fs_mad:
#                                                 $ fs_mad = False
#                                                 call end_of_day(True)
#                                             else:
#                                                 # jump firstday_mc_work
#                                                 call end_of_day(True)
#                                 else:
#                                     fp "It's late, and probably time to call it a day"
#                                     $ count = 0
#                                     call entrance_loc()
#                                     # return
#                             "Or, I could just slack off today, and work on the bike another day...":
#                                 if not firstday_after_talk:
#                                     $ fs_mad = True
#                                 $ count = 0
#                                 call entrance_loc()
#                 else:
#                     fp "Ah, it's a beautiful day. Maybe I should go to the beach...?"
#                     menu:
#                         "Go to the beach":
#                             call beach_loc()
#                         "Nah, slack of in the garden instead":
#                             call entrance_loc()
#                 return

#         label school_finished(called=False):
#             if detention_served:
#                 $ current_hour = "17:00"
#             else:
#                 $ current_hour = "15:05"
#             if school_hacker:
#                 if school_hacker_first_thought:
#                     "{i}You've been thinking about what happened with [fsName.yourformal], and you were almost sure that it wouldn't be possible to manage that many mistakes by accident. Also, they hadn't found out who had updated the records... that's usually registered...{/i}"
#                     $ school_hacker_first_thought = False
#                 fp "I should go talk to Natalie. She loves me, I'm sure I'll be able to get some answers from her!"
#                 menu:
#                     "Go talk to Natalie, try to find out more about what happened to [fsName.informal]":
#                         call talk_to_natalie(True)
#                     "Nah, not today, I'll do it tomorrow instead":
#                         call evening_home()
#             "After school, you decide to just trek back home. No plans for today, and not that much interesting happening in town anyway"
#             call evening_home()
#             return
        
#         label talk_to_natalie(called=False):
#             if called:
#                 $ called = False
#                 "Conversation with Natalie goes here"
#                 call evening_home()
#                 return
#             else:
#                 return

#         label evening_home():
#             if day_week <= 4:
#                 call livingroom_scene from _call_livingroom_scene_3
#                 if detention_served:
#                     $ current_hour = "17:45"
#                 else:
#                     $ current_hour = "15:30"
#                     $ n = renpy.random.randint(0,2)
#                     $ home_events = [
#                         ["You arrive home. Nobody is there at the moment, it seems, as "+shortfM+"'s car is gone, and "+fsName.yourformalName.informal+" is nowhere to be seen.",False],
#                         ["When you arrive home, the door is locked, and you realise you've forgotten your key. Noone is answering the door when you try the doorbell, so both "+fmName.informal+" and "+fsName.informal+" must be out. You weren't really that keen on sitting outside all day, waiting for them, so you're pondering what else you can do instead",False],
#                         ["Arriving home, you see "+fmName.informal+"'s car in the driveway.",False],
#                         ["When you arrive home, you catch a glimpse of "+fsName.yourformal+" by the pool, but "+yourfM+" is nowhere to be seen. Her car is still here, though.",True]
#                     ] # create more events here
#                     $ text = home_events[n][0]
#                     "[text]"
#                     if home_events[n][1] and fs_mad:
#                         jump firstday_talk_fS
#                 if renpy.random.random() > .5:
#                     if  current_month >= 5 and current_month <= 8 and not detention_served:
#                         "You decide to just lounge by the pool for a while, trying to stand the heat"
#                 else:
#                     if not detention_served:
#                         if not mc_f:
#                             "You decide that you can spend a few more hours on your bike today"
#                             call garage_scene from _call_garage_scene_5
#                             call change_loc('garage') from _call_change_loc_16
#                             call w_mc(True) from _call_w_mc_3
#                             if current_hour[:2] > 19:
#                                 "You're feeling a bit tired, after school, and working on your bike, so you decide taking a shower will be a nice relief right now"
#                                 jump taking_shower_evening
#                             else:
#                                 call garage_scene from _call_garage_scene_6
#                                 call change_loc('garage') from _call_change_loc_17
#                                 call w_mc(True) from _call_w_mc_4
#                                 "After putting in a few more hours on the bike, you decide that the rest of the evening should be spent doing less arduous tasks, and head inside to watch some TV, or play some games"
#                                 jump tv_vgames_evening
#                         else:
#                             if renpy.random.random() > .65 and current_hour[:2] < 17:
#                                 "You decide to take a ride"
#                                 if (renpy.random.random() > .65 and nK_rel > 15) or (renpy.random.random() > .5 and nK_rel > 20):
#                                     "You decide to call up [nK] to see if she wants to come with"
#                                     nK ahead "Hi, [fp]"
#                                     fp "Hi, [nK]. I was wondering if you wanted to come for a ride with me today? Was thinking we could"
#                                     $ conditions.addcondition("Go to the cabin","current_month >= 9 and current_month <= 3")
#                                     $ conditions.addcondition("Go to the marina","boat_at_marina")
#                                     menu:
#                                         "Go to the beach":
#                                             jump beach_ride
#                                         "Ride to the next town over":
#                                             jump next_town_ride
#                                         "Go to the cabin":
#                                             jump cabin_ride
#                                         "Go to the marina":
#                                             jump marina_ride
#                                 else:
#                                     "No answer. Oh well, you'll call her again some other time"
#                             else:
#                                 "It's just not the day for outdoors activities, you decide to stay inside and just watch some TV instead"
#                                 if fp_sts > 0:
#                                     $ statschangeNotify("fp_sts",-1)
#                 if not evening_event:
#                     jump end_of_day
#                 else:
#                     jump evening_event_label
        
# if end_game:
#     return