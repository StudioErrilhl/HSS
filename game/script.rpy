﻿# define config.screenshot_pattern = "D:\Dropbox\RenPy-games\Screenshots\HSS-screenshot%04d.png"

label splashscreen:
    scene black 
    $ renpy.pause(1)
    show text "{size=60}{color=#ffffff}Studio Errilhl Presents ... {/color}{/size}" with dissolve
    $ renpy.pause(2)
    hide text with dissolve
    $ renpy.block_rollback()
    if not persistent.splash_screen:
        show image "images/hss-logo.png" with dissolve:
            xalign .5 yalign .5
        $ renpy.pause(2)
        hide image "images/hss-logo.png" with dissolve
        $ renpy.pause(.75)
        if not persistent.accepted_splashscreen:
            call screen confirm_age()   
            $ renpy.block_rollback()
        $ persistent.accepted_splashscreen = True
        call screen splash_info()
        $ renpy.block_rollback()
        show screen disclaimer()
        $ renpy.block_rollback()        
        $ renpy.pause(4)
        hide screen disclaimer        
        show text "{size=30}{color=#ffffff}Code / story by Studio Errilhl\nCharacter art by DivineChihaya{/color}{/size}"
        $ renpy.block_rollback()
        $ renpy.pause(4)
        $ persistent.splash_screen = True
        $ renpy.block_rollback()        
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
    $ gp_bed = random.choice(fs_p)
    $ gp_bath = random.choice(fs_p)    
    $ current_time = "09:00"
    call fp_bedroom_scene from _call_fp_bedroom_scene_2

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
        call fs_intro_scene from _call_fs_intro_scene
        fp "{i}[fsName.Myformal]'s room has the bed opposed the door. So right in front of my prone body, on her bed... well, half off her bed, was [fsName.informal], naked from the waist down, with most of her right hand buried between her legs, which, mind you, was spread quite wide over the edge of the bed. I couldn't really have had a better viewpoint even if I was sitting right in front of a porn-shoot.{/i}"
        call upper_hallway_scene from _call_upper_hallway_scene_1
        show juliette_reflection
        show juliette_mad_pantless:
            zoom .74
            yalign .72
            xalign .2
        with dissolve
        fp "{i}Didn't last long, though. About 5 seconds after me landing on her bedroom floor, I got hit with something hard! Then the shouting began, and 10 seconds after that, I was out in the hallway again, with a furious, but still very half-naked sister yelling at me. I'm still amazed that [fmName.informal] didn't show up... THAT would've been embarassing, for both of us... mostly for me.{/i}"
        fp "{i}Thankfully, [fsName.informal] realised what she was doing (partly because I had a raging boner in my boxer's, I guess) - turned on her heel, and went into her room again - this time locking the door.{/i}"
        hide juliette_mad_pantless
        hide juliette_reflection
        with dissolve
        call upper_hallway_bathroom_scene from _call_upper_hallway_bathroom_scene_1
        fp "{i}Me... I went to the bathroom and jerked off. Yes, I know she's [fsName.myformal], and all that, but DAMN. She's HOT!{/i}"
        fp "{i}Okay... that might have been a bit TMI. I'm sorry. I just wanted you to understand what happened. And how that sort of led to... other things that happened as well. During that summer. You know... spring. Summer. End of high-school. The time I had all planned out. The plans that really didn't happen. Like... at all.{/i}"
        "So... the coming days, weeks and months, you'll be trying to pass your exams, finish your bike, getting some action, and generally being a high school senior going on freedom!"
        $ persistent.skipintro = True
        $ fs_mad = True        
        # return
    label skippedintro:
        $ fs_mad = True
        show screen ingame_menu_display()
        fp "So. Quick recap: I woke up on April 1st, tried to somewhat remotely function and seem awake, and figure out what to with the day. Then, a little later, shellshocked, and trying to figure out how to get the image of my naked [fsName.role] off my mind, I decided spending the day working on my bike would be as good a way as any..."
        $ skip_breakfast = True
        $ breakfast_food = False
        $ breakfast_reply = False
        $ breakfast_mod = False
        $ breakfast_att = False
        call skip_breakfast(True) from _call_skip_breakfast

    label day_start():
        $ detention_served = False
        $ late_oh_shit = False
        $ breakfast_jump = False
        $ shitty_morning = False
        $ count = 0
        $ end_bike_repair = False
        $ find_panties = True if renpy.random.random() > .75 else False
        $ find_pb = True if renpy.random.random() > .80 else False
        $ bathroom_find_panties = True if renpy.random.random() > .30 else False
        $ find_tablet = True if renpy.random.random() > .65 else False        
        $ had_breakfast = False
        $ morning_event_done = False
        $ gp_bed = random.choice(fs_p)
        $ gp_bath = random.choice(fs_p)
        $ br = random.choice([0,1,2,3])
        $ after_principal_talk = False
        if wcount < 5:
            $ wcount += 1

        if renpy.random.random() > .75:
            $ bad_weather = True
            $ rainstorm = True
        else:
            $ bad_weather = False
            $ rainstorm = False

        if fs_mad:
            $ statschangenotify("fs_rel",-1)
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

        if int(current_time[:2]) in night:
            if day_week <= 4:
                $ mh = format(int(morning[renpy.random.randint(0,(len(morning)-3))]),"02d")
                $ mm = format(renpy.random.randint(00,30),"02d")
                call settime(mh,mm) from _call_settime_2
            elif day_week >= 5:
                $ mh = format(int(random.choice(morning)),"02d")
                $ mm = format(renpy.random.randint(00,59),"02d")
                call settime(mh,mm) from _call_settime_3
                if int(current_time[:2]) == 6:
                    $ addtime(1, False) 

        call day_wrapper() from _call_day_wrapper

        label day_wrapper():
            if int(current_time[:2]) in morning:
                call morning_events() from _call_morning_events
            elif int(current_time[:2]) in day:
                # call day_events()
                "this is the day time"
            elif int(current_time[:2]) in night:
                # call night_events()
                "this is the night time"

    label w_mc(wmc_called=False):
        if wmc_called or wmc_cfs:
            $ wmc_called = wmc_cfs = False
            $ c = 0
            $ mc_t = 0
            $ event = False
            $ maxc = 1 if int(current_time[:2]) == 6 else 2 if int(current_time[:2]) > 14 and int(current_time[:2]) < 22 and day_week <= 4 else 3
            $ events = [0,1,2,3,4,5,6,7,8,9,10]
            $ outside_events = [77,88,99]
            $ modifier = .5 if mc_b < 50 else .4 if mc_b < 100 else .35

            label repeat_event(event=0):
                if int(current_time[:2]) < 7 and day_week <= 4 and event not in outside_events:
                    $ choice1 = "Hm... I have at least an hour before school. Maybe I can get a bit done on the bike"
                    $ choice2 = "Or, I could just go back inside, eat breakfast and leave early"
                    if not event or event == 0:
                        $ event = 7
                elif int(current_time[:2]) < 7 and day_week >= 5 and event not in outside_events:
                    $ choice1 = "Hm... I have at least an hour before anyone else is out of bed. I can probably get a bit done before breakfast"
                    $ choice2 = "Or... I could go back inside, take a shower, get some breakfast, and get back out here later"
                    if not event or event == 0:                    
                        $ event = 7
                elif int(current_time[:2]) in morning and day_week <= 4 and event not in outside_events+events:
                    $ choice1 = False
                    $ choice2 = "I don't really have time to work on the bike right now. I need to get to school"
                    if not event or event == 0:
                        $ event = 3
                elif 3 and 14 < int(current_time[:2]) < 20 and event not in outside_events and event != 5 and day_week <= 4:
                    $ choice1 = "I can probably do at least a couple hours of bike repair today"
                    $ choice2 = "Or I could go back in the house, see if there's anything on TV, or play a game..."
                    if not event or event == 0:                    
                        $ event = 4
                elif sc <= 3 and day_week >= 5 and event not in outside_events:
                    $ choice1 = "I have the entire day off. Maybe I could spend some time on the bike, see if I can get some traction on the rebuild"
                    $ choice2 = "Or, I could just slack off today, and work on the bike another day"
                    if not event or event == 0:                    
                        $ event = 5

                if event in events:
                    menu:
                        "[choice1]" if choice1:
                            if event == 7:
                                $ addtime(1,False)
                                $ filth_val += 10
                                if renpy.random.random() > modifier:
                                    if backpack.has_item(toolbox_item):
                                        $ mc_t = 2
                                    else:
                                        $ mc_t = 1
                                $ event = 77
                                $ mc_b += mc_t
                                $ mc_p = (float(mc_b)/float(mc_b_max))*100
                                $ mc_p = "{0:.2f}".format(mc_p)
                                if mc_t == 0:
                                    $ renpy.notify("You did not improve the status of the bike this time")
                                else:                                    
                                    $ renpy.notify("You have increased the bike status by "+str(mc_t)+". You're currently "+str(mc_p)+"% done with the bike")                               
                                call repeat_event(77) from _call_repeat_event
                            elif c <= maxc:
                                $ addtime(1, False)
                                $ filth_val += 10                                
                                if renpy.random.random() > modifier:
                                    if backpack.has_item(toolbox_item):
                                        $ mc_t = 2
                                    else:
                                        $ mc_t = 1                                        
                                $ c += 1
                                $ mc_b += mc_t
                                $ mc_p = (float(mc_b)/float(mc_b_max))*100
                                $ mc_p = "{0:.2f}".format(mc_p)
                                if mc_t == 0:
                                    $ renpy.notify("You did not improve the status of the bike this time")
                                else:                                    
                                    $ renpy.notify("You have increased the bike status by "+str(mc_t)+". You're currently "+str(mc_p)+"% done with the bike")                               
                                if c == (maxc):
                                    call repeat_event(88) from _call_repeat_event_1
                                else:
                                    call repeat_event() from _call_repeat_event_2
                            else:
                                $ event = 88
                                call repeat_event(88) from _call_repeat_event_3
                        "[choice2]" if choice2:
                            $ event = 99
                            call repeat_event(99) from _call_repeat_event_4
                elif event == 77:
                    $ text = "I should go in, {0} and {1}".format("take a shower","have breakfast and get ready for school" if day_week <= 4 else "have breakfast")
                    "[text]"
                    call kitchen_scene from _call_kitchen_scene_3
                    call breakfast_interaction(True) from _call_breakfast_interaction_1
                elif event == 88:
                    "You're done working on the bike today"
                    $ end_bike_repair = True
                    if bad_weather:
                        call entrance_loc() from _call_entrance_loc
                    else:
                        # call outside_loc(True) from _call_outside_loc
                        call change_loc('outside') from _call_change_loc_27
                elif event == 99:
                    "You don't really wanna work on the bike right now"
                    if bad_weather:
                        call entrance_loc() from _call_entrance_loc_1
                    else:
                        # call outside_loc(True) from _call_outside_loc_1
                        call change_loc('outside') from _call_change_loc_28

if end_game:
    return