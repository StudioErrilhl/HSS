# location changer
label change_loc(locname=False,loctrans=False,timeadd=False,char=False,imgname=False,sec_call=False,showerstat=False):
    if timeadd:
        $ addtime(False, 30)
    if locname:
        if 'loc' not in locname:
            $ current_location = locname.replace(' ','_')+"_loc"
        else:
            $ current_location = locname.replace(' ','_')
            $ locname = locname.replace('_loc','').replace('_',' ')
        $ tmpname = locname.replace(' ','_').replace('_loc','')+"_scene"
        if loctrans:
            $ loctrans = False
            if showerstat:
                call expression tmpname pass (trans=False,wetshower=showerstat)
            else:
                call expression tmpname pass (trans=False)
        else:
            if showerstat:
                call expression tmpname pass (wetshower=showerstat)
            else:
                call expression tmpname
        show screen location(locname)
        if locname in firstday_talk_list:
            if firstday_talk:
                if renpy.random.random() > .75:
                    call fs_talk(True) from _call_fs_talk
        if char and imgname:
            show expression "images/characters/[char]/body/standing/[imgname].png" as character: # at fs_standing_ahead_ani with dissolve:
                zoom .65
                xpos .7
                ypos 1.0
                xanchor .5
                xanchor .5
                yanchor .75
        if sec_call:
            call expression sec_call pass (True) from _call_expression_2
        call screen empty()
        hide screen empty
        hide screen location
        hide character

label entrance_loc(trans=False):
    $ current_location = 'entrance_loc'
    if not entrance_ach:
        $ entrance_ach = True
        $ update_been_everywhere_achievement()
    call change_loc('entrance') from _call_change_loc_2

label fp_bedroom_loc(fpl_called=False,trans=False):
    $ current_location = 'fp_bedroom_loc'
    $ loct = False
    if not fp_bedroom_ach:
        $ fp_bedroom_ach = True
        $ update_been_everywhere_achievement()
    if fpl_called or uhl_fpb_cfs:
        $ fpl_called = uhl_fpb_cfs = False
        if schoolbooks_added:
            if backpack_carry:
                if not backpack.has_item(schoolbooks_item):
                    $ schoolbooks_pickup = True
                    $ update_all_the_stuff()
                $ backpack.add_item(schoolbooks_item)
                $ schoolbooks_added = False
                $ loct = True
            else:
                $ renpy.notify("You don't have anywhere to carry the books")
                if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                    $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                $ schoolbooks_added = False
                $ loct = True
        if wallet_added:
            if not backpack.has_item(wallet_item):
                $ wallet_pickup = True
                $ update_all_the_stuff()
            $ backpack.add_item(wallet_item)
            $ wallet_added = False
            $ carry_wallet = True
            $ loct = True
        if phone_added:
            if charge_phone:
                menu:
                    "The phone is charging. Current charge is [battery_text]\%"
                    "Do you want to grab the phone?":
                        if not backpack.has_item(phone_item):
                            $ phone_pickup = True
                            $ update_all_the_stuff()
                        $ backpack.add_item(phone_item)
                        $ phone_added = False
                        $ carry_phone = True
                        $ charge_phone = False
                        $ loct = True
                    "Leave the phone to charge":
                        $ phone_added = False
                        $ loct = True
            else:
                if not backpack.has_item(phone_item):
                    $ phone_pickup = True
                    $ update_all_the_stuff()
                $ backpack.add_item(phone_item)
                $ phone_added = False
                $ carry_phone = True
                $ loct = True
        elif charge_phone and carry_phone:
            $ backpack.remove_item(phone_item,sec_reply=True)
            $ carry_phone = False
            $ loct = True
        if current_time[:2] in morning and not morning_event_done:
            # call fp_morning_content(True)
            call morning_events() from _call_morning_events
        else:
            call change_loc('fp bedroom',loctrans=loct) from _call_change_loc_3

label fs_bedroom_loc(fsl_called=False,trans=False):
    $ current_location = 'fs_bedroom_loc'
    $ loct = False
    if not fs_bedroom_ach:
        $ fs_bedroom_ach = True
        $ update_been_everywhere_achievement()
    if fsl_called or uhl_fsb_cfs:
        $ fsl_called = uhl_fsb_cfs = False
        if tablet_added:
            if not tablet_always_look:
                "Oh, she left her tablet..."
                menu:
                    "Look at tablet":
                        $ ic_num = []
                        $ tablet_always_look = True
                        call screen fs_tablet()
                    "Leave tablet":
                        $ tablet_added = False
                        $ find_tablet = True
            else:
                call screen fs_tablet()
        if panties_added:
            $ current_p = getattr(store,gp_bed+"_panties_item")
            if backpack_carry:
                if not backpack.has_item(current_p):
                    $ r = random.randint(0,3)
                    $ text = p_response[r]
                    if r == 0 or r == 3:
                        $ panties_sniffer = True
                        $ update_panties_achievements()
                else:
                    $ aux = list(p_response)
                    $ del aux[2]
                    $ r = random.randrange(len(aux))
                    $ text = p_response[r]
                    if r == 0 or r == 3:
                        $ panties_sniffer = True
                        $ update_panties_achievements()
                "[text]"
                menu:
                    "Take panties":
                        if gp_bed == 'fs_bright_pink':
                            if not backpack.has_item(fs_bright_pink_panties_item):
                                $ bright_pink_panties_pickup = True
                                $ update_all_the_stuff()
                            $ backpack.add_item(fs_bright_pink_panties_item)
                        elif gp_bed == 'fs_pale_pink':
                            if not backpack.has_item(fs_pale_pink_panties_item):
                                $ pale_pink_panties_pickup = True
                                $ update_all_the_stuff()
                            $ backpack.add_item(fs_pale_pink_panties_item)
                        elif gp_bed == 'fs_light_blue':
                            if not backpack.has_item(fs_light_blue_panties_item):
                                $ light_blue_panties_pickup = True
                                $ update_all_the_stuff()
                            $ backpack.add_item(fs_light_blue_panties_item)
                        elif gp_bed == 'fs_yellow':
                            if not backpack.has_item(fs_yellow_panties_item):
                                $ yellow_panties_pickup = True
                                $ update_all_the_stuff()
                            $ backpack.add_item(fs_yellow_panties_item)
                        $ panties_added = False
                        $ fp_creep += 1
                        $ update_panties_achievements()
                    "Leave panties":
                        $ panties_added = False
                        $ find_panties = True
                        $ loct = True
            else:
                $ renpy.notify("You don't have anywhere to carry the panties")
                if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                    $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                $ panties_added = False
                $ find_panties = True
                $ loct = True
        if pb_added:
            "Holy... is that a {b}buttplug{/b}!?"
            menu:
                "Take the buttplug":
                    if not backpack.has_item(princessplug_item):
                        $ princessplug_pickup = True
                        $ update_all_the_stuff()
                    $ pb_added = False
                    $ statschangenotify('fs_cor',1,True)
                    $ statschangenotify('fs_anal',3)
                    $ backpack.add_item(princessplug_item)
                "Leave the buttplug":
                    $ pb_added = False
                    $ statschangenotify('fs_cor',1,True)
                    $ find_pb = True
                    $ loct = True
        call change_loc('fs bedroom',loctrans=loct) from _call_change_loc_4

label garage_loc(gar_called=False,trans=False):
    $ current_location = 'garage_loc'
    if not garage_ach:
        $ garage_ach = True
        $ update_been_everywhere_achievement()
    if gar_called or gar_cfs:
        $ gar_called = g_called_from_screen = False
        if backpack_carry:
            if not backpack.has_item(toolbox_item):
                $ toolbox_pickup = True
                $ update_all_the_stuff()
                if toolbox_added:
                    $ backpack.add_item(toolbox_item)
                    $ toolbox_added = False
        else:
            $ renpy.notify("You don't have anywhere to carry the toolbox")
            if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
        call change_loc('garage') from _call_change_loc_5

label icafe_loc(ic_called=False,trans=False):
    $ current_location = 'icafe_loc'
    if not icafe_ach:
        $ icafe_ach = True
        $ update_been_everywhere_achievement()
    if ic_called or ic_cfs:
        $ ic_called = ic_cfs = False
    call change_loc('icafe')

label kitchen_loc(kit_called=False,trans=False):
    $ current_location = 'kitchen_loc'
    $ loct = False
    if not kitchen_ach:
        $ kitchen_ach = True
        $ update_been_everywhere_achievement()
    if kit_called or kit_cfs:
        $ kit_called = kit_cfs = False
        if wine_added:
            menu:
                "Take the bottle" if bottles == 1:
                    if backpack_carry:
                        if not backpack.has_item(wine_item):
                            $ wine_pickup = True
                            $ update_all_the_stuff()
                        $ backpack.add_item(wine_item)
                        $ bottles = 0
                        $ br = 0
                        $ wcount = 0
                        $ wine_added = False
                        $ achievement_wine_collector.update()
                        $ achievement_all_the_wine.update()
                        $ achievement_even_more_wine.update()
                        $ loct = True
                    else:
                        $ renpy.notify("You don't have anywhere to carry a winebottle")
                        if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                            $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Leave the bottle" if bottles == 1:
                    $ wine_added = False
                    $ loct = True
                "Take one bottle" if bottles == 2:
                    if backpack_carry:
                        if not backpack.has_item(wine_item):
                            $ wine_pickup = True
                            $ update_all_the_stuff()
                        $ backpack.add_item(wine_item)
                        $ bottles = 1
                        $ br = 1
                        $ wine_added = False
                        $ achievement_wine_collector.update()
                        $ achievement_all_the_wine.update()
                        $ achievement_even_more_wine.update()
                        $ loct = True
                    else:
                        $ renpy.notify("You don't have anywhere to carry a winebottle")
                        if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                            $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Take both bottles" if bottles == 2:
                    if backpack_carry:
                        if not backpack.has_item(wine_item):
                            $ wine_pickup = True
                            $ update_all_the_stuff()
                        $ backpack.add_item(wine_item,2)
                        $ bottles = 0
                        $ br = 0
                        $ wcount = 0
                        $ wine_added = False
                        $ achievement_wine_collector.update(2)
                        $ achievement_all_the_wine.update(2)
                        $ achievement_even_more_wine.update(2)
                        $ loct = True
                    else:
                        $ renpy.notify("You don't have anywhere to carry winebottles")
                        if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                            $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Leave the bottles" if bottles == 2:
                    $ wine_added = False
                    $ loct = True
                "Take one bottle" if bottles == 3:
                    if backpack_carry:
                        if not backpack.has_item(wine_item):
                            $ wine_pickup = True
                            $ update_all_the_stuff()
                        $ backpack.add_item(wine_item)
                        $ bottles = 2
                        $ br = 2
                        $ wine_added = False
                        $ achievement_wine_collector.update()
                        $ achievement_all_the_wine.update()
                        $ achievement_even_more_wine.update()
                        $ loct = True
                    else:
                        $ renpy.notify("You don't have anywhere to carry a winebottle")
                        if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                            $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Take two bottles" if bottles == 3:
                    if backpack_carry:
                        if not backpack.has_item(wine_item):
                            $ wine_pickup = True
                            $ update_all_the_stuff()
                        $ backpack.add_item(wine_item,2)
                        $ bottles = 1
                        $ br = 1
                        $ wine_added = False
                        $ achievement_wine_collector.update(2)
                        $ achievement_all_the_wine.update(2)
                        $ achievement_even_more_wine.update(2)
                        $ loct = True
                    else:
                        $ renpy.notify("You don't have anywhere to carry winebottles")
                        if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                            $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Take all three bottles" if bottles == 3:
                    if backpack_carry:
                        if not backpack.has_item(wine_item):
                            $ wine_pickup = True
                            $ update_all_the_stuff()
                        $ backpack.add_item(wine_item,3)
                        $ bottles = 0
                        $ br = 0
                        $ wcount = 0
                        $ wine_added = False
                        $ achievement_wine_collector.update(3)
                        $ achievement_all_the_wine.update(3)
                        $ achievement_even_more_wine.update(3)
                        $ loct = True
                    else:
                        $ renpy.notify("You don't have anywhere to carry winebottles")
                        if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                            $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Leave the bottles" if bottles == 3:
                    $ wine_added = False
                    $ loct = True

        if int(current_time[:2]) in morning and not morning_event_done:
            call change_loc('kitchen',sec_call="breakfast_interaction",loctrans=loct) from _call_change_loc_6
        elif 16 <= int(current_time[:2]) <= 18:
            if dinner_event:
                call change_loc('kitchen',sec_call="dinner_events",loctrans=loct) from _call_change_loc_7
            else:
                call change_loc('kitchen',loctrans=loct) from _call_change_loc_8
        if day_week <= 4 and int(current_time[:2]) in fs_present and renpy.random.random() < .5:
            call change_loc('kitchen',sec_call='fs_talk',loctrans=loct) from _call_change_loc_9
        elif day_week > 4 and int(current_time[:2]) in fs_present_we and renpy.random.random() < .5:
            call change_loc('kitchen',sec_call='fs_talk',loctrans=loct) from _call_change_loc_10
        else:
            call change_loc('kitchen',loctrans=loct) from _call_change_loc_11

label livingroom_loc(lvr_called=False,trans=False):
    $ current_location = 'livingroom_loc'
    if lvr_called or lvr_cfs:
        $ lvr_called = lvr_cfs = False
        if not livingroom_ach:
            $ livingroom_ach = True
            $ update_been_everywhere_achievement()
        if day_week <= 4 and int(current_time[:2]) in fs_present and renpy.random.random() < .5:
            call change_loc('livingroom',sec_call='fs_talk') from _call_change_loc_12
        elif day_week > 4 and int(current_time[:2]) in fs_present_we and renpy.random.random() < .5:
            call change_loc('livingroom',sec_call='fs_talk') from _call_change_loc_13
        else:
            call change_loc('livingroom') from _call_change_loc_14

label outside_loc(out_called=False,trans=False):
    $ current_location = 'outside_loc'
    call outside_scene
    if int(current_time[:2]) in day+night:
        show black_car behind rain
    if out_called or out_cfs:
        $ out_called = out_cfs = False
        if not outside_ach:
            $ outside_ach = True
            $ update_been_everywhere_achievement()
        if trans:
            call outside_scene from _call_outside_scene
        if day_week <= 4 and int(current_time[:2]) in morning:
            call outside_scene from _call_outside_scene_1
            menu:
                "Go to school":
                    call travel_events('travel_school') from _call_travel_events
                "Stay home":
                    $ home_from_school = True
                    pass
        if int(current_time[:2]) in day+night:
            $ second_menu_choice = "Stay home {0}".format("today" if int(current_time[:2]) in day else "tonight")
            menu:
                "Do a [drivingcmp] run":
                    $ addtime(3,False)
                    $ randmoney = random.randrange(50,250)
                    $ randmoney = int(round((float(randmoney) / 100.0) * float(70)))
                    $ reply = "You made $"+str(randmoney)+" {0}".format("today" if int(current_time[:2]) in day else "tonight")
                    $ renpy.notify(""+reply+"")
                    $ fp_money += randmoney
                    call change_loc('outside')
                "[second_menu_choice]":
                    call change_loc('outside')
            call change_loc('outside',sec_call='outside_loc') from _call_change_loc_15
        call change_loc('outside')

label upper_hallway_loc(uhl_called=False,trans=False):
    $ current_location = 'upper_hallway_loc'
    if not uhl_ach:
        $ uhl_ach = True
        $ update_been_everywhere_achievement()
    if uhl_called or uhl_cfs:
        $ uhl_called = uhl_cfs = False
        # if backpack.has_item(princessplug_item):
        #     call change_loc('upper hallway',sec_call='talk_fs')
        call change_loc('upper hallway') from _call_change_loc_16

label upper_hallway_bathroom_loc(uhl_bl_called=False,trans=False):
    $ current_location = 'upper_hallway_bathroom_loc'
    $ loct = False
    if occupied_bath:
        if not bathroom_occupied_fs and not bathroom_occupied_fm:
            if int(current_time[:2]) < 9:
                if renpy.random.random() > .5:
                    $ bathroom_occupied_fs = True
                    $ bathroom_occupied_fm = False
                elif renpy.random.random() < .15:
                    $ bathroom_occupied_fs = False
                    $ bathroom_occupied_fm = True
            elif int(current_time[:2]) >= 9 and int(current_time[:2]) <= 15:
                if renpy.random.random() > .80:
                    $ bathroom_occupied_fs = False
                    $ bathroom_occupied_fm = True
            elif int(current_time[:2]) >= 17:
                if renpy.random.random() > .65:
                    $ bathroom_occupied_fs = True
                    $ bathroom_occupied_fm = False
                elif renpy.random.random() < .20:
                    $ bathroom_occupied_fs = False
                    $ bathroom_occupied_fm = True
    else:
        $ bathroom_occupied_fs = bathroom_occupied_fm = False
    if (bathroom_occupied_fs or bathroom_occupied_fm) and not_entered:
        $ uhl_bl_called = uhl_bl_cfs = False
        "The bathroom is occupied"
        $ conditions.addcondition("Sneak a peek","bathroom_occupied_fs")
        menu:
            "Sneak a peek":
                $ images_unlocked.append('DCIM00002_portrait.png')
                call change_loc('upper hallway bathroom peek',sec_call='peek_scene_happening') from _call_change_loc_17
                label peek_scene_happening(True):
                    fp "{i}Oh {b}SHIT{/b}! That is definitely something worth getting thwapped for! But... maybe I should get the hell outta here before I get caught!{/i}"
                    $ conditions.addcondition("Stay and watch","fs_rel >= 30 and fs_aro >= 10")
                    menu:
                        "Stay and watch":
                            #call change_loc('upper hallway bathroom peek')
                            pass
                        "Get the hell outta here":
                            call change_loc('upper hallway')
            "Knock on the door":
                # pass
                if bathroom_occupied_fs:
                    if fs_mad:
                        fs "What?!?"
                        fp "Hey, [fsName.informal] - I really need to pee, you think I could..."
                        fs "Fuck off, [fp]!"
                        fp "{i}Okay,then...{/i}"
                        call change_loc('upper hallway') from _call_change_loc_18
                    else:
                        fs "I'm in here, you'll have to come back later"
                        fp "I really need to pee, [fsName.informal]!"
                        if fs_rel > 40:
                            fs "{i}Teasing now...{/i}\nSorry, [fp], I'm not at all decent!"
                            fp "I don't care! I need to pee!"
                            fs "Fine! Come in, but no oogling!"
                            "{b}Click!{/b}"
                            call change_loc('upper hallway bathroom',loctrans=True,sec_call="first_bathroom_occupied_label") from _call_change_loc_19
                            label first_bathroom_occupied_label(True):
                                fs "Lemme get back into the tub, okay?"
                                fs "Okay, you can come in!"
                                fp "{i}Running to the toilet{/i}\nOh....\nThanks, sis!"
                                $ not_entered = False
                                call change_loc('upper hallway bathroom',loctrans=True) from _call_change_loc_20
                        else:
                            fs "I'm not decent! Use the downstairs bathroom!"
                            fp "I'll never make it! Please let me in?"
                            fs "Fine! Damn it, [fp]!"
                            fs "So, get in there and do your thing!"
                            call change_loc('upper hallway bathroom',loctrans=True,sec_call="second_bathroom_occupied_label") from _call_change_loc_21
                            label second_bathroom_occupied_label(True):
                                fp "{i}Running to the toilet{/i}\nOh...\n{i}Damn... she looks {b}hot{/b} with nothing but that towel on...{/i}"
                                $ not_entered = False
                                call change_loc('upper hallway bathroom',loctrans=True) from _call_change_loc_22
                if bathroom_occupied_fm:
                    fm "I'm in here, [fp]"
                    fp "I'm sorry, [fmName.informal], but I really, really need to pee!"
                    fm "But... I'm not decent!"
                    fp "[fmName.INFORMAL]! I need to go NOW!"
                    $ not_entered = False
                    call change_loc('upper hallway bathroom',loctrans=True) from _call_change_loc_23
            "Leave and come back later":
                $ occupied_bath = False
                $ hour = renpy.random.randint(0,1)
                if hour:
                    $ addtime(hour,False)
                else:
                    $ addtime(False, 30)
                call change_loc('upper hallway') from _call_change_loc_24
    else:
        if not uhl_bathroom_ach:
            $ uhl_bathroom_ach = True
            $ update_been_everywhere_achievement()
        if uhl_bl_called or uhl_bl_cfs:
            $ uhl_bl_called = uhl_bl_cfs = False
            if smallkeys_added:
                "{i}Hmm... a pair of keys. Haven't seen them before. Wonder what they open?\nShould I take them?{/i}"
                menu:
                    "Take keys":
                        $ backpack.add_item(small_keys_item)
                        $ smallkeys_added = False
                    "Leave keys":
                        $ smallkeys_added = False
            if bathroom_panties_added:
                $ current_p = getattr(store,gp_bath+"_panties_item")
                if backpack_carry:
                    if not backpack.has_item(current_p):
                        $ r = random.randint(0,3)
                        $ text = p_response[r]
                        if r == 0 or r == 3:
                            $ panties_sniffer = True
                            $ update_panties_achievements()
                    else:
                        $ aux = list(p_response)
                        $ del aux[2]
                        $ r = random.randrange(len(aux))
                        $ text = p_response[r]
                        if r == 0 or r == 3:
                            $ panties_sniffer = True
                            $ update_panties_achievements()
                    "[text]"
                    menu:
                        "Take panties":
                            if gp_bath == 'fs_bright_pink':
                                if not backpack.has_item(fs_bright_pink_panties_item):
                                    $ bright_pink_panties_pickup = True
                                    $ update_all_the_stuff()
                                $ backpack.add_item(fs_bright_pink_panties_item)
                            elif gp_bath == 'fs_pale_pink':
                                if not backpack.has_item(fs_pale_pink_panties_item):
                                    $ pale_pink_panties_pickup = True
                                    $ update_all_the_stuff()
                                $ backpack.add_item(fs_pale_pink_panties_item)
                            elif gp_bath == 'fs_light_blue':
                                if not backpack.has_item(fs_light_blue_panties_item):
                                    $ light_blue_panties_pickup = True
                                    $ update_all_the_stuff()
                                $ backpack.add_item(fs_light_blue_panties_item)
                            elif gp_bath == 'fs_yellow':
                                if not backpack.has_item(fs_yellow_panties_item):
                                    $ yellow_panties_pickup = True
                                    $ update_all_the_stuff()
                                $ backpack.add_item(fs_yellow_panties_item)
                            $ bathroom_panties_added = False
                            $ bathroom_find_panties = False
                            $ fp_creep += 1
                            $ update_panties_achievements()
                            # call change_loc(current_location)
                        "Leave panties":
                            $ bathroom_panties_added = False
                            $ bathroom_find_panties = True
                            $ loct = True
                else:
                    $ renpy.notify("You don't have anywhere to carry the panties")
                    if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                        $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                    $ bathroom_panties_added = False
                    $ bathroom_find_panties = True
                    $ loct = True
            if fpshower:
                if filth_val == 0:
                    $ renpy.notify("I don't need to take a shower right now")
                else:
                    menu:
                        "Take a short shower - 15 minutes / 10\% cleaner":
                            $ addtime(False, 15)
                            if filth_val != 0:
                                $ filth_val -= 10
                                if filth_val < 0:
                                    $ filth_val = 0
                            $ fpshower = False
                            $ loct = True
                            $ wetshower = True
                        "Take a long shower - 30 minutes / 20\% cleaner":
                            $ addtime(False, 30)
                            if filth_val != 0:
                                $ filth_val -= 20
                                if filth_val < 0:
                                    $ filth_val = 0
                            $ fpshower = False
                            $ loct = True
                            $ wetshower = True
                    fp "{i}Ah, that was refreshing{/i}"
            if fpsink:
                $ addtime(False,15)
                if filth_val != 0:
                    $ filth_val -= 5
                    if filth_val <0:
                        $ filth_val = 0
                fp "{i}Good to get the filth off my hands{/i}"
                $ fpsink = False
                $ loct = True
            call change_loc('upper hallway bathroom',loctrans=loct,showerstat=wetshower)

label tv_games_evening(tvg_called=False,trans=False):
    if tvg_called:
        $ tvg_called = False
        "This is just a placeholder for this event"
    call end_of_day() from _call_end_of_day_2

label beach_ride(br_called=False):
    if br_called:
        $ br_called = False
        $ addtime(1,30)
        call change_loc('beach') from _call_change_loc_26
    call end_of_day() from _call_end_of_day_3

label next_town_ride(ntr_called=False,trans=False):
    if ntr_called:
        $ ntr_called = False
        "This is just a placeholder for this event"
    call end_of_day() from _call_end_of_day_4
label cabin_ride(cr_called=False,trans=False):
    if cr_called:
        $ cr_called = False
        "This is just a placeholder for this event"
    call end_of_day() from _call_end_of_day_5
label marina_ride(mr_called=False,trans=False):
    if mr_called:
        $ mr_called = False
        "This is just a placeholder for this event"
    call end_of_day() from _call_end_of_day_6