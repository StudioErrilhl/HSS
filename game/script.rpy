label splashscreen:
    scene black
    $ renpy.pause(1)
    show image "gui/studioerrilhl_logo.webp" with dissolve
    $ renpy.pause(2)
    hide image "gui/studioerrilhl_logo.webp" with dissolve
    if not persistent.splash_screen:
        show image "gui/hss-logo.webp" with dissolve:
            xalign .5 yalign .5
        $ renpy.pause(2)
        hide image "gui/hss-logo.webp" with dissolve
        $ renpy.pause(.75)
        if not persistent.accepted_splashscreen:
            call screen confirm_age()
        $ persistent.accepted_splashscreen = True
        call screen splash_info()
        show screen disclaimer()
        $ renpy.pause(4)
        hide screen disclaimer
        show text "{size=30}{color=#ffffff}Code / story / art by Studio Errilhl{/color}{/size}"
        $ renpy.pause(4)
        $ persistent.splash_screen = True
        $ renpy.block_rollback()
    return

label after_load:
    $ updateInventory()
    return

init 1:
    defineDynamicName gameName:
        name "HSS"
        shortname "HSS"
    defineDynamicName fmName:
        name "Anne"
        shortname "Anne"
        informal "Anne"
        formal "Anne"
        role "landlady"
        myformal "my landlady"
        yourformal "your landlady"
        myinformal "my landlady"
        yourinformal "your landlady"
        relation "extended \"family\""
    defineDynamicName fsName:
        name "Juliette"
        shortname "Jules"
        informal "Jules"
        formal "Juliette"
        role "housemate"
        myformal "my housemate"
        yourformal "your housemate"
        myinformal "my housemate"
        yourinformal "your housemate"
        relation "extended \"family\""

init python:
    import os
    def define_images(imageFolder, excludeFolders=0):
        for path in renpy.list_files():
            if path.startswith(imageFolder):
                path_list = ("/".join(path.split())).split("/")
                path_list[-1] = os.path.splitext(path_list[-1])[0]
                path_list = tuple(path_list[excludeFolders:])
                renpy.image(path_list, path)
                # print(path_list)


    define_images('test')

label start:
    $ conditions = Conditions() ## enables the conditions-parameter used for assigning conditions to disable / enable choice-items
    $ backpack = Container()
    $ updateInventory()
    $ gp_bed = random.choice(fs_p)
    $ gp_bath = random.choice(fs_p)
    $ current_time = "09:00"
    $ weather = renpy.random.randint(1,3)
    call fp_bedroom_scene from _call_fp_bedroom_scene_1

    if config.developer:
        show screen debug_tools()

    ## intro - this is shown only once, when starting the game from the beginning
    $ fpinput = (renpy.input("First, you'll need to provide your name (default, Marten):") or "Marten").strip()

    $ dinner = [ # food, reply, comeback, modifier, stat, weight-mod
                ["I just made mac n' cheese today","Okay, "+fmName.informal+", I like mac n' cheese","Well, that's good",1,"fm_rel",.5],
                ["I made pizza - ham, cheese and tomato","Aw, no pepperoni?","No pepperoni today, "+fpinput+"",1,"fm_rel",.35],
                ["I made steak","Oh, neat, I love steak","I know, "+fpinput+"",2,"fm_rel",.5],
                ["I went vegetarian today","Oh...","You will try it before you go all mopey!",-1,"fm_rel",.25]
            ]

    if persistent.skipintro:
        $ this_is_a_test = False
        menu:
            "View intro" if not this_is_a_test:
                $ this_is_a_test = True
                jump viewintro
            "View intro again" if this_is_a_test:
                jump viewintro
            "Skip intro":
                jump skippedintro
    label viewintro:
        "So! Your name's [fp], and this is the (fucked up) story of your life. Did that come out a little stilted? I felt that it did. Oh, well, I'm not that well versed in being a narrator. Hence, the story will mostly proceed in a first-person perspective - you know, \"Hi, I'm [fp] and you're about to be taken for a wild ride!\" That sound good? {b}GREAT!{/b}"
        "Now, where were we? Oh, right. Yeah. This... well, life. You know, the one you're gonna be playing through? Well, at least from the current point in time. No need to go back to your childhood, or early teens, or antyhing like that. So, where to start."
        "Hmm... Maybe May? Or... no, I think we'll have to go all the way back to April, actually. You see, you were... attending your last semester at highschool. (Yeah, lets go with that, for now). Grinding away, trying to keep your grades up to at least passing standard, all the while trying not to attract too much attention."
        "Sorta failing most of that, but I wouldn't be too worried. You had plans, both for the summer after high school, and for what comes after. You were planning on taking some time off, take a cross-country trip. Been working on your bike for a while now, and it was (slowly) getting done; the last, finishing touches left, so to speak. And, when done, you'd be taking it on th road, no definite goal, just... away!"
        "Planning on starting more or less were we are right now, on the East coast, and just drive - visiting as many places, people, landmarks and interesting spots that could possibly fit into a 3-4 months trip. That was basically what was on your mind these days... Until shit hit the fan. \"What to do AFTER high school\"... completely failing to take into account what would happen BEFORE that..."
        call change_loc('upstairs',sec_call='intro_hallway')
        label intro_hallway(intro_cont=False):
        fp "{i}So, here we are. April 1st, a Saturday, if I'm not mistaken. I'd just woken up, and was on my way downstairs to get some breakfast, when I heard noises coming from [fsName.formal]'s room. Usually I wouldn't care, but those sounds sounded... muffled. Like she was trying to keep it down, but failing. And I was curious what the hell she was doing. So, I walked up to her door, thinking I would just try to listen in, see if I could figure out what was going on.{/i}"
        call change_loc('upstairs closerdoor',sec_call='falling_scene')
        label falling_scene(intro_falling=False):
        pause(.1)
        show fpfalling
        fp "{i}Unfortunately, spying has never been one of my strong suits, and the door wasn't closed all the way... so when I leaned against it, I suddenly found myself tumbling into her room. Not very elegantly, mind. Quite ungracefully, in fact. But... that was quite quickly forgotten!{/i}"
        play sound "sounds/medium_camera_shutter.mp3"
        $ image_unlock('DCIM00001_landscape.webp')
        fp "{i}[fsName.Myformal] was on her bed, going at it with vigor! Her right hand buried between her legs, which, mind you, was spread quite wide. Nimble, that girl is. I couldn't really have had a better viewpoint even if I was sitting right in front of a porn-shoot.{/i}"
        fp "{i}Didn't last long, though. About 5 seconds after me landing on her bedroom floor, I got hit with something hard!{/i}"
        call upstairs_closerdoor_scene
        play sound "sounds/medium_camera_shutter.mp3"
        $ image_unlock('DCIM00002_portrait.webp')
        show juliette_intro
        with dissolve
        fp "{i}Then the shouting began, and 10 seconds after that, I was out in the hallway again, with a furious, but still very half-naked [fsName.role] yelling at me. I'm still amazed that [fmName.informal] didn't show up... THAT would've been embarassing, for both of us... mostly for me.{/i}"
        hide juliette_intro
        show juliette_intro_ani
        pause(1.5)
        play sound "sounds/medium_camera_shutter.mp3"
        $ image_unlock('DCIM00003_portrait.webp')
        hide juliette_intro_ani
        with dissolve
        fp "{i}Thankfully, [fsName.informal] realised what she was doing (partly because I had a raging boner pitching a tent in my pants, I guess) - turned on her heel, and went into her room again - this time locking the door.{/i}"
        call ufbm_scene
        fp "{i}Me... I went to the bathroom and jerked off. Yes, I know she's [fsName.myformal], and all that, but DAMN. She's HOT!{/i}"
        fp "{i}Okay... that might have been a bit TMI. I'm sorry. I just wanted you to understand what happened. And how that sort of led to... other things that happened as well. During that summer. You know... spring. Summer. End of high-school. The time I had all planned out. The plans that really didn't happen. Like... at all.{/i}"
        "So... the coming days, weeks and months, you'll be finishing high school, maybe fix up your bike, and... try not to get into too much trouble. You know... the kind of trouble you sort of gave up on?"
        $ persistent.skipintro = True
        $ fs_mad = 1

    label skippedintro():
        $ fs_mad = 1
        show screen ingame_menu_display()
        if 'DCIM00001_portrait.webp' not in images_unlocked:
            $ set_hint("You chose to skip the intro - which means that a couple of the images in the photo-gallery is not gonna be available to you")
        if persistent.maininfo:
            call screen maininfo()
        fp "So. Quick recap: I woke up on April 1st, tried to somewhat remotely function and seem awake, and figure out what to with my day. Then, a little later, shellshocked, and trying to figure out how to get the image of my naked [fsName.role] off my mind, I decided spending the day working on my bike would be as good a way as any..."
        $ skip_breakfast = True
        $ resolved = breakfast_nice_att = breakfast_nice_mod = breakfast_mean_att1 = breakfast_mean_att2 = breakfast_mean_mod1 = breakfaste_mean_mod2 = False
        $ breakfast_food = False
        $ dinner_food = False
        $ dinner_reply = False
        $ dinner_comeback = False
        $ dinner_mod = False
        $ dinner_att = False
        call skip_breakfast(True) from _call_skip_breakfast

    label day_start():
        $ daycount += 1
        $ fpe = fme = fse = hje = nbe = nre = nke = nce = sne = see = spe = sje = scne = scme = False
        $ find_panties = True if renpy.random.random() > .75 else False
        $ find_pb_mod = .65 if fs_aro > 10 else .90
        $ find_pb = True if renpy.random.random() > find_pb_mod else False
        $ bathroom_find_panties = True if renpy.random.random() > .60 else False
        $ find_tablet = True if renpy.random.random() > .65 else False
        $ gp_bed = random.choice(fs_p)
        $ gp_bath = random.choice(fs_p)
        $ br = random.choice([0,1,2,3])
        $ bathroom_occupied_fs = False
        $ bathroom_occupied_fm = False
        $ home_from_school = False
        $ not_entered = True
        $ tmp_filth_val = False
        if nc_action_started and nc_action_started < 8:
            $ nc_action_started += 1
        if hacker_6:
            if check_nc_event_status == 0:
                $ nc_event = 'nc_meet_hacker'
                $ check_nc_event_status = 1
            elif check_nc_event_status == 1:
                $ hacker_6 = False
                $ hacker_event_not_happen = True
        if hacker_event_not_happen:
            $ hacker_event_not_happen = False
            $ nc_event = False
            $ set_message('unk',unk,"You stay away from "+str(nc)+"! You forget about the issues at the school. You basically make yourself scarce. Else, I'll hurt both you and her")

        $ dream_event = True if renpy.random.random() > .75 else False

        if fs_rel > 12:
            $ dreameventsChars.append('fs')

        $ call_nk = True if nk_rel > 20 else False
        $ call_nk_event = 'nk_date' if call_nk and not nk_mad else False

        $ breakfast_jump = False
        $ had_breakfast = False
        $ morning_event_done = False
        $ dinner_event = True
        $ shitty_morning = False
        $ late_oh_shit = False
        $ detention_served = False
        $ after_principal_talk = False

        $ count = 0
        $ end_bike_repair = False

        if wcount < 5:
            $ wcount += 1

        $ weather = renpy.random.randint(1,3)

        if fs_mad == 1:
            $ statschangenotify("fs_rel",-1)
        $ mc_f = True if mc_b >= mc_b_max else False

        $ breakfast_select = random.randint(0,len(breakfast_food_list)-1)
        $ breakfast_food = breakfast_food_list[breakfast_select]
        $ breakfast_nice_select = random.randint(0,len(breakfast_nice_list)-1)
        $ breakfast_nice = breakfast_nice_list[breakfast_nice_select][0]
        $ breakfast_nice_mod = breakfast_nice_list[breakfast_nice_select][1]
        $ breakfast_nice_att = breakfast_nice_list[breakfast_nice_select][2]
        $ breakfast_mean_select = random.randint(0,len(breakfast_mean_list)-1)
        $ breakfast_mean = breakfast_mean_list[breakfast_mean_select][0]
        $ breakfast_mean_mod1 = breakfast_mean_list[breakfast_mean_select][1]
        $ breakfast_mean_att1 = breakfast_mean_list[breakfast_mean_select][2]
        $ breakfast_mean_mod2 = breakfast_mean_list[breakfast_mean_select][3]
        $ breakfast_mean_att2 = breakfast_mean_list[breakfast_mean_select][4]

        $ dinner_select = weighted_choice(dinner_weights)
        $ dinner_food = dinner[dinner_select][0]
        $ dinner_reply = dinner[dinner_select][1]
        $ dinner_comeback = dinner[dinner_select][2]
        $ dinner_mod = dinner[dinner_select][3]
        $ dinner_att = dinner[dinner_select][4]
        $ dinner_weight = dinner[dinner_select][5]
        if dinner_mod >= 0:
            $ new_weight = dinner_weights[dinner_select][1] + dinner_weight
        else:
            $ new_weight = dinner_weights[dinner_select][1] - dinner_weight
        $ dinner_weights[dinner_select] = (dinner_weights[dinner_select][0],new_weight)

        if int(current_time[:2]) in night:
            if day_week <= 4 and not alarmclock:
                $ mh = format(int(morning[renpy.random.randint(0,(len(morning)-4))]),"02d")
                $ mm = format(renpy.random.randint(00,30),"02d")
                $ settime(mh,mm)
            elif day_week <= 4 and alarmclock:
                if overslept and renpy.random.random() < .2:
                    $ mh = format(int(morning[renpy.random.randint(1,(len(morning)-4))]),"02d")
                    $ mm = format(renpy.random.randint(00,59),"02d")
                    if mh >= int(alarmclock_time[:2]):
                        if mm > int(alarmclock_time[3:]):
                            $ settime(mh,mm)
                else:
                    $ settime(format(int(alarmclock_time[:2]),"02d"),format(int(alarmclock_time[3:]),"02d"))
            elif day_week >= 5:
                $ mh = format(int(random.choice(morning)),"02d")
                $ mm = format(renpy.random.randint(00,59),"02d")
                $ settime(mh,mm)
                if int(current_time[:2]) == 6:
                    $ addtime(1, False)

        call day_wrapper() from _call_day_wrapper

        label day_wrapper():
            if int(current_time[:2]) in morning:
                call morning_events() from _call_morning_events_1
            elif int(current_time[:2]) in day:
                # call day_events()
                "this is the day time"
            elif int(current_time[:2]) in night:
                # call night_events()
                "this is the night time"

    label w_mc(wmc_called=False): # this is the controlling label for working on the bike
        if wmc_called or wmc_cfs:
            $ wmc_called = wmc_cfs = False
            $ c = 0
            $ mc_t = 0
            $ event = False
            $ maxc = 1 if int(current_time[:2]) == 6 else 2 if int(current_time[:2]) > 14 and int(current_time[:2]) < 22 and day_week <= 4 else 3
            $ events = [0,1,2,3,4,5,6,7,8,9,10]
            $ outside_events = [66,77,88,99]
            $ modifier = .5 if mc_b < 50 else .4 if mc_b < 100 else .35

            label repeat_event(event=0):
                $ choice1 = False
                $ choice2 = False
                if (not mc_b % 25 == 0) or (mc_b == 0):
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
                    elif sc <= 3 and day_week <= 4 and event not in outside_events and home_from_school:
                        $ choice1 = "Since I stayed home today, I can get some work done on the bike"
                        $ choice2 = "Or, I could just slack off in front of the TV, or something..."
                        if not event or event == 0:
                            $ event = 5
                else:
                    $ choice1 = "Crap. I won't be able to continue working on the bike unless I get ahold of the part I need"
                    $ choice2 = "Or, I can just wait on working on the bike for now"
                    if not event or event == 0:
                        $ event = 6

                if event in events:
                    if choice1 or choice2:
                        menu:
                            "[choice1]" if choice1:
                                if event == 6:
                                    $ addtime(False,30)
                                    $ event = 66
                                    call repeat_event(66)
                                if event == 7:
                                    $ addtime(1,False)
                                    $ filth_val += 10
                                    if renpy.random.random() > modifier:
                                        if backpack.has_item(toolbox_item):
                                            $ mc_t = 2
                                        else:
                                            $ mc_t = 1
                                    $ event = 77
                                    # $ mc_b += mc_t
                                    $ mc_b = min(mc_b + mc_t,mc_b_max)
                                    $ mc_p = min((float(mc_b)/float(mc_b_max))*100,100)
                                    $ mc_p = "{0:.2f}".format(mc_p)
                                    if mc_b == 150:
                                        $ renpy.notify("You have increased the bike status by "+str(mc_t)+". You're currently "+str(mc_p)+"% done with the bike")
                                        $ mc_f = True
                                        $ update_mc_achievement(mc_b,mc_f)
                                        call change_loc('garage') from _call_change_loc_72
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
                                    $ mc_b = min(mc_b + mc_t,mc_b_max)
                                    $ mc_p = min((float(mc_b)/float(mc_b_max))*100,100)
                                    $ mc_p = "{0:.2f}".format(mc_p)
                                    if mc_b == 150:
                                        $ renpy.notify("You have increased the bike status by "+str(mc_t)+". You're currently "+str(mc_p)+"% done with the bike")
                                        $ mc_f = True
                                        $ update_mc_achievement(mc_b,mc_f)
                                        call change_loc('garage') from _call_change_loc_73
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
                    else:
                        $ event = 77
                        call repeat_event(77) from _call_repeat_event_5
                elif event == 66:
                    "You need to get a piece to complete the bike. You can get this from the bike-shop, or from the scrapyard, or perhaps you can find something on Profit"
                    if 25 >= mc_b < 50:
                        "I need to get a front wheel for the bike"
                    elif 50 >= mc_b < 75:
                        "The gastank is completely busted. I'll have to get a new one"
                    if 75 >= mc_b < 100:
                        "Hm, better find new lights for this bike, I don't think I can save these ones"
                    if 100 >= mc_b < 125:
                        "Got to get those handlebars and that seat fixed"
                    if 125 >= mc_b < 150:
                        "Just need to get the exhaust now"
                    call entrance_loc()
                elif event == 77:
                    if not home_from_school:
                        $ text = "I should go in, {0} and {1}".format("take a shower","have breakfast and get ready for school" if day_week <= 4 else "have breakfast")
                        "[text]"
                        if 'shower' in text:
                            $ required_shower = True
                            call change_loc('ufbm') from _call_change_loc_30
                        else:
                            call change_loc('kitchen') from _call_change_loc_67
                    else:
                        call repeat_event(6) from _call_repeat_event_6
                elif event == 88:
                    "You're done working on the bike today"
                    $ end_bike_repair = True
                    if weather == 1:
                        call entrance_loc() from _call_entrance_loc
                    else:
                        call change_loc('garage') from _call_change_loc_31
                elif event == 99:
                    "You don't really wanna work on the bike right now"
                    if weather == 1:
                        call entrance_loc() from _call_entrance_loc_1
                    else:
                        call change_loc('garage') from _call_change_loc_32

if end_game:
    return