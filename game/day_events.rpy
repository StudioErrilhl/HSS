label day_events():
    #day events goes here
    label weekend_sat():
        if sat_event:
            call livingroom_scene from _call_livingroom_scene_1
            label sat_what_to_do():
                if not mc_f:
                    call garage_scene from _call_garage_scene_2
                    call change_loc('garage') from _call_change_loc_42
                    call w_mc(True) from _call_w_mc_1
                else:
                    fp "Ah, it's a beautiful day. Maybe I should go to the beach...?"
                    menu:
                        "Go to the beach":
                            call sat_beach() from _call_sat_beach
                        "Nah, slack of in the garden instead":
                            call sat_end() from _call_sat_end
            label sat_beach():
                "this is a beach scene on saturday"
                call beach_scene from _call_beach_scene
                call change_loc('beach') from _call_change_loc_43
                $ renpy.pause()
            label sat_end():
                $ sat_event = False
                call change_loc('livingroom') from _call_change_loc_44
            $ sat_event = False

    label weekend_sun(wsun_called=False):
        if wsun_called:
            $ wsun_called = False
            if sun_event:
                if renpy.random.random() <= .5:
                    show fm_standing ahead
                    fm ahead "Could you help me open this, [fp]? I can't seem to get it open, and I need this for dinner today"
                    menu:
                        "Yes, [fmName.informal], no problem. *you open the jar*":
                            if fm_dom <= 5:
                                $ statschangenotify("fm_dom",.5,True)
                                $ statschangenotify("fm_rel",1)
                            else:
                                $ statschangenotify("fm_rel",.5)
                        "No, [fmName.informal], I don't have time to help you right now":
                            show fm_standing mad
                            $ statschangenotify("fm_dom",.5,True)
                            $ statschangenotify("fm_rel",-.5)
                $ sun_event = False
                hide fm_standing
                call change_loc(current_location) from _call_change_loc_70

    label dinner_events(de_called=False):
        if de_called:
            $ de_called = False
            if dinner_event:
                if fs_mad:
                    show fm_standing smile with dissolve
                    fm smile "Hey [fp]. It's dinnertime soon, do you wanna go see if you can find [fsName.name], and tell her to get ready?"
                    fp "Well... [fsName.name] isn't really speaking to me at the moment..."
                    show fm_standing ahead
                    fm ahead "Oh? What did you do now?"
                    fp "Why do you just assume I did anything? I'll talk to her, but now might not be the best time... I'll tell her dinner is ready if I see her, okay?"
                    fm ahead "Fine. But you fix this with [fsName.yourformal], okay?"
                    fp "I will, [fmName.informal], I will"
                    $ dinner_event = False
                    $ talk_later = True
                    hide fm_standing
                elif dinner_food:
                    show fm_standing smile with dissolve
                    fm smile "Hey [fp]. Dinner is ready soon"
                    fp "Nice. What are we having?"
                    fm smile "[dinner_food]"
                    fp "[dinner_reply]"
                    if dinner_mod > 0:
                        fm smile "[dinner_comeback]"
                    else:
                        fm ahead "[dinner_comeback]"
                    if dinner_mod > 0:
                        show fm_standing smile with dissolve
                    else:
                        show fm_standing ahead with dissolve
                    $ statschangenotify(dinner_att,dinner_mod)
                    $ dinner_event = False
                    $ renpy.pause(.25)
                    hide fm_standing with dissolve
                    $ addtime(1)
                call change_loc('kitchen',loctrans=True) from _call_change_loc_45

    label evening_home(evh_called=False):
        if evh_called:
            $ evh_called = False
            $ n = renpy.random.randint(0,3)
            if day_week <= 4:
                if detention_served:
                    $ current_time = "17:45"
                else:
                    $ current_time = "15:30"

                if n == 1:
                    call change_loc('outside',sec_call="harsh_homecoming") from _call_change_loc_46
                    label harsh_homecoming(True):
                        $ text = home_events[n][0]
                        "[text]"
                        $ addtime(2)
                        "After waiting for ages, [fmName.yourformal] finally comes home and let you into the house"
                        call change_loc('entrance') from _call_change_loc_71
                else:
                    call livingroom_scene from _call_livingroom_scene_2
                    if renpy.random.random() > .5 and not hacker_3:
                        if  current_month >= 5 and current_month <= 8 and not detention_served:
                            call change_loc('outside',sec_call='lounge_pool') from _call_change_loc_48
                            label lounge_pool(True):
                                "You decide to just lounge by the pool for a while, trying to stand the heat"
                        elif int(current_time[:2]) <= 19:
                            "You decide that you can spend a few more hours on your bike today"
                            call change_loc('garage',sec_call='after_evening_bike_repair') from _call_change_loc_49
                            label after_evening_bike_repair(True):
                                "After putting in a few more hours on the bike, you decide that the rest of the evening should be spent doing less arduous tasks, and head inside to watch some TV, maybe play some games"
                                call change_loc('livingroom',sec_call='tv_games_evening') from _call_change_loc_50
                        elif int(current_time[:2]) > 19:
                            "You're feeling a bit tired, after school, and working on your bike, so you decide taking a shower will be a nice relief right now"
                            call change_loc('upper hallway bathroom',sec_call='taking_shower_evening') from _call_change_loc_51
                        else:
                            call change_loc('livingroom',sec_call='lounge_livingroom') from _call_change_loc_52
                            label lounge_livingroom(True):
                                "You decide to just slouch on the couch for a bit, chilling in front of the TV"
                    elif not detention_served and hacker_3 and call_nr:
                        $ hacker_3 = False
                        $ call_nr = False
                        $ hacker_4 = True
                        call nr_talk('nr_intro') from _call_nr_talk

                if home_events[n][1] and fs_mad:
                    call fs_talk(True) from _call_fs_talk_4

                call change_loc('livingroom') from _call_change_loc_47

            if mc_f and renpy.random.random() > .65 and current_time[:2] < 17:
                "You decide to take a ride"
                "You decide to call up [nk] to see if she wants to come with"
                if (renpy.random.random() > .65 and nk_rel > 15) or (renpy.random.random() > .5 and nk_rel > 20) or (renpy.random.random() > .35 and nk_rel > 30):
                    nk ahead "Hi, [fp]"
                    fp "Hi, [nk]. I was wondering if you wanted to come for a ride with me today? Was thinking we could"
                    $ conditions.addcondition("Go to the cabin","current_month >= 9 and current_month <= 3 and has_cabin")
                    $ conditions.addcondition("Go to the marina","boat_at_marina")
                    menu:
                        "Go to the beach":
                            call change_loc('beach')
                        "Ride to the next town over":
                            jump next_town_ride
                        "Go to the cabin":
                            jump cabin_ride
                        "Go to the marina":
                            jump marina_ride
                else:
                    "No answer. Oh well, you'll call her again some other time"
            else:
                "It's just not the day for outdoor activities, you decide to stay inside and just watch some TV instead"
                if fp_sts > 0:
                    $ statschangenotify("fp_sts",-1)
                else:
                    $ evening_event = True
                if not evening_event:
                    call end_of_day(True) from _call_end_of_day_7
                else:
                    call evening_event_label(True) from _call_evening_event_label

    label taking_shower_evening(tse_called=False):
        if tse_called:
            $ tse_called = False
            "You decide to take a shower after a long day"
            $ fpshower = True
            call change_loc('bathroom_loc') from _call_change_loc_53

    # label talk_fs(tfs_called=False):
    #     if tfs_called or tfs_cfs:
    #         $ tfs_called = tfs_cfs = False
    #         show fs_standing ahead with dissolve
    #         if not pb_return:
    #             fs ahead "Hey [fp]!"
    #             fp "Hey, [fsName.informal] - what's up?"
    #             if fs_aro > 10 and backpack.has_item(princessplug_item):
    #                 fs "Have you taken my buttplug?"
    #             else:
    #                 fs "Have you been in my room?"
    #             if fs_bedroom_ach:
    #                 menu:
    #                     "Yes (offer no explanation)":
    #                         $ result = "true_1"
    #                     "Yes, I went in there looking for you the other day, when I wanted to talk to you":
    #                         $ result = "lie_(white)_1"
    #                     "You mean except when I stumbled in on you earlier?":
    #                         $ result = "question"
    #                     "No (lie)":
    #                         $ result = "lie_1"
    #             else:
    #                 menu:
    #                     "Yes (lie)":
    #                         $ result = "lie_2"
    #                     "Yes - I went in there looking for you the other day, when I wanted to talk to you":
    #                         $ result = "lie_(white)_2"
    #                     "You mean except when I stumbled in on you earlier?":
    #                         $ resule = "question"
    #                     "No (tell the truth)":
    #                         $ result = "true_2"
    #             if result == "lie_1":
    #                 fs "You're lying"
    #                 if backpack.has_item(princessplug_item) and fs_aro > 10:
    #                     fs "I know you went in my room. There is no need to deny it, I know you did, and I know you took something!"
    #                     fp "Took what?"
    #                     fs "What I asked you about, dummy!"
    #                     fp "Oh..."
    #                     $ item = backpack.has_item(princessplug_item,returnname=True)
    #                     menu:
    #                         "Return the [item] to [fsName.yourformal]":
    #                             $ pb_return = True
    #                             $ backpack.remove_item(princessplug_item,sec_reply=True)
    #                         "Keep the [item]":
    #                             $ pb_return = False
    #             elif result == "question":
    #                 fs "Answering with a question of your own, huh? I guess you're hiding {i}something{/i}!"
    #                 fp "I'm not hiding anything, I promise!"
    #                 fs "I don't believe you. I really don't!"
    #                 fp "Well, I can't do anything about that, now can I?"
    #                 fs "Jerk!"
    #                 $ statschangenotify('fs_aro',-1,True)
    #                 $ statschangenotify('fs_rel',-1)
    #             else:
    #                 fs "That's actually refreshing. Truth!"
    #         hide fs_standing with dissolve
    #         $ renpy.pause()
    #         return

    label no_answer():
        $ calling = duringcall = False
        fp "No answer - I guess I'll try again later"
        call change_loc(current_location) from _call_change_loc_57

    label evening_event_label(ee_called=False):
        if ee_called:
            $ ee_called = False
            if nk_school_assignment_evening and day_week <= 4:
                $ nk_school_assignment_evening = False
                "{b}*ding dong*{/b}"
                fm ahead "{b}[fp], can you get that?{/b}"
                call entrance_scene from _call_entrance_scene
                "You go to get the door, expecting it to be [nk]"
                nk smile "Hi [fp]."
                "[nk] is outside, all smiles and with a stack of books in her arms."
                fp "Hi... you do know we have Internet on the premises, right? And on our phones, and pretty much in every Starshots in town...?"
                nk smile "I know, silly. But I've always felt that books provide some... well, they make it easier to focus on the task at hand!\n{i}she lets out a cute little laugh{/i}"
                fp "Well, I was thinking we could set up in my room. I have set up a double set of chairs, I have my computer there, and we should have room enough to go through the books you brought. {i}You grab the books from her, and motion for her to come along{/i}"
                call fp_bedroom_scene from _call_fp_bedroom_scene_3
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
                call end_of_day(True) from _call_end_of_day_8
            else:
                call end_of_day(True) from _call_end_of_day_9