# location changer
label change_loc(locname=False,loctrans=False,timeadd=False,char=False,imgname=False,sec_call=False,prev_loc=False,event=False,showerstat=False):
    if timeadd:
        $ addtime(False, 30)
    if locname:
        $ locname = locname.replace('_loc','').replace('scene','').replace('bw','').replace('light','').replace('windows','').replace('after_shower','').replace('wallet','').replace('empty','').replace('wallart','').replace('sincity','').replace('parkinglot','').replace('peekaboo','').replace('roadtrip','').replace('ferrari','').replace('_',' ').replace('__',' ')
        $ current_location = locname.replace(' ','_')
        if current_location.endswith('_'):
            $ current_location = current_location[:-1]
        if prev_loc:
            $ previous_location = prev_loc
        $ tmpname = locname.replace(' ','_').replace('bw','').replace('_build','').replace('_finished','').replace('_windows','').replace('_after_shower','').replace('_light','').replace('_loc','').replace('__','_')
        if 'scene' not in tmpname:
            if tmpname.endswith('_'):
                $ tmpname = tmpname[:-1]
            $ tmpname = tmpname+'_scene'
        if loctrans:
            $ loctrans = False
            if showerstat:
                call expression tmpname pass (trans=False,wetshower=showerstat) from _call_expression
            else:
                call expression tmpname pass (trans=False) from _call_expression_1
        else:
            if showerstat:
                call expression tmpname pass (wetshower=showerstat) from _call_expression_3
            else:
                call expression tmpname from _call_expression_4
        $ renpy.hide(current_location)
        show screen location(current_location) #with Dissolve(.25)
        if nk_school_assignment_evening:
            if 18 <= int(current_time[:2]) < 20:
                call evening_event_label(True) from _call_evening_event_label_1

        if char and imgname:
            show expression "images/characters/[char]/body/standing/[imgname].webp" as character: # at fs_standing_ahead_ani with dissolve:
                zoom .65
                xpos .7
                ypos 1.0
                xanchor .5
                xanchor .5
                yanchor .75
        if sec_call:
            if sec_call == "go_to_school":
                call expression sec_call from _call_expression_6
            else:
                if event:
                    call expression sec_call pass (event=event) from _call_expression_5
                else:
                    call expression sec_call pass (True) from _call_expression_2
        call screen empty()
        hide screen empty
        hide screen locname
        hide character

label fp_entrance(trans=False):
    $ current_location = 'fp_entrance'
    if not fp_entrance_ach:
        $ fp_entrance_ach = True
        $ update_been_everywhere_achievement()
    call change_loc('fp_entrance') from _call_change_loc_2

label fp_bedroom_fp(fpl_called=False,trans=False):
    $ current_location = 'fp_bedroom_fp'
    $ loct = False
    if not fp_bedroom_fp_ach:
        $ fp_bedroom_fp_ach = True
        $ update_been_everywhere_achievement()
    if fpl_called or uhl_fpb_cfs:
        $ fpl_called = uhl_fpb_cfs = False
        if schoolbooks_added:
            if carry_backpack:
                if not backpack.has_item(schoolbooks_item):
                    $ schoolbooks_pickup = True
                    $ update_all_the_stuff()
                $ backpack.add_item(schoolbooks_item)
                $ schoolbooks_added = False
                $ loct = True
            else:
                $ renpy.notify("You don't have anywhere to carry the books")
                if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                    $ renpy.notify("You should try to find something to carry items in")
                    $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
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
        # if current_time[:2] in morning and not morning_event_done:
        #     # call fp_morning_content(True)
        #     call morning_events() from _call_morning_events
        # else:
        call change_loc('fp_bedroom_fp',loctrans=loct) from _call_change_loc_3

label fp_bedroom_fm(fml_called=False,trans=False):
    $ current_location = 'fp_bedroom_fm'
    $ loct = False
    if not fp_bedroom_fm_ach:
        $ fp_bedroom_fm_ach = True
        $ update_been_everywhere_achievement()
    if fml_called or fmb_cfs:
        $ fml_called = fmb_cfs = False
    call change_loc('fp_bedroom_fm',loctrans=loct) from _call_change_loc_12

label fp_bedroom_fs(fsl_called=False,trans=False):
    $ current_location = 'fp_bedroom_fs'
    $ loct = False
    if not fp_bedroom_fs_ach:
        $ fp_bedroom_fs_ach = True
        $ update_been_everywhere_achievement()
    if fsl_called or uhl_fsb_cfs:
        $ fsl_called = uhl_fsb_cfs = False
        # if tablet_added:
        #     if not tablet_always_look:
        #         "Oh, she left her tablet..."
        #         menu:
        #             "Look at tablet (evil)":
        #                 $ statschangenotify("lil_bad",1,True)
        #                 $ statschangenotify('fp_alignment',-1)
        #                 $ ic_num = []
        #                 $ tablet_always_look = True
        #                 call screen fs_tablet()
        #             "Leave tablet (good)":
        #                 $ statschangenotify("aru_good",1,True)
        #                 $ statschangenotify('fp_alignment',1)
        #                 $ tablet_added = False
        #                 $ find_tablet = True
        #     else:
        #         call screen fs_tablet()
        # if panties_added:
        #     $ current_p = getattr(store,gp_bed+"_panties_item")
        #     if carry_backpack:
        #         if not backpack.has_item(current_p):
        #             $ r = random.randint(0,3)
        #             $ text = p_response[r]
        #             if r == 0 or r == 3:
        #                 $ panties_sniffer = True
        #                 $ update_panties_achievements()
        #         else:
        #             $ aux = list(p_response)
        #             $ del aux[2]
        #             $ r = random.randrange(len(aux))
        #             $ text = p_response[r]
        #             if r == 0 or r == 3:
        #                 $ panties_sniffer = True
        #                 $ update_panties_achievements()
        #         "[text]"
        #         menu:
        #             "Take panties (evil)":
        #                 $ statschangenotify("lil_bad",1,True)
        #                 $ statschangenotify('fp_alignment',-1,True)
        #                 if gp_bed == 'fsp_hot_pink':
        #                     if not backpack.has_item(fsp_hot_pink_item):
        #                         $ fsp_hot_pink_pickup = True
        #                         $ update_all_the_stuff()
        #                     $ backpack.add_item(fsp_hot_pink_item)
        #                 elif gp_bed == 'fsp_black':
        #                     if not backpack.has_item(fsp_black_item):
        #                         $ fsp_black_pickup = True
        #                         $ update_all_the_stuff()
        #                     $ backpack.add_item(fsp_black_item)
        #                 elif gp_bed == 'fsp_light_blue':
        #                     if not backpack.has_item(fsp_light_blue_item):
        #                         $fsp_light_blue_pickup = True
        #                         $ update_all_the_stuff()
        #                     $ backpack.add_item(fsp_light_blue_item)
        #                 elif gp_bed == 'fsp_yellow':
        #                     if not backpack.has_item(fsp_yellow_item):
        #                         $ fsp_yellow_pickup = True
        #                         $ update_all_the_stuff()
        #                     $ backpack.add_item(fsp_yellow_item)
        #                 elif gp_bed == 'fsp_red':
        #                     if not backpack.has_item(fsp_red_item):
        #                         $ fsp_red_pickup = True
        #                         $ update_all_the_stuff()
        #                     $ backpack.add_item(fsp_red_item)
        #                 $ panties_added = False
        #                 $ fp_creep += 1
        #                 $ update_panties_achievements()
        #             "Leave panties (good)":
        #                 $ statschangenotify("aru_good",1,True)
        #                 $ statschangenotify('fp_alignment',1)
        #                 $ panties_added = False
        #                 $ find_panties = True
        #                 $ loct = True
        #     else:
        #         $ renpy.notify("You don't have anywhere to carry the panties")
        #         if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
        #             $ renpy.notify("You should try to find something to carry items in")
        #             $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
        #         $ panties_added = False
        #         $ find_panties = True
        #         $ loct = True
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
        call change_loc('fp_bedroom_fs',loctrans=loct) from _call_change_loc_4

label fp_garage(gar_called=False,trans=False):
    $ current_location = 'fp_garage'
    if not fp_garage_ach:
        $ fp_garage_ach = True
        $ update_been_everywhere_achievement()
    if gar_called or gar_cfs:
        $ gar_called = g_called_from_screen = False
        # call change_loc('fp_garage') from _call_change_loc_5
        if bc_clicked:
            $ bc_clicked = False
            if int(current_time[:2]) in evening+night:
                if filth_val <= 15:
                    $ second_menu_choice = "Stay home {0}".format("today" if int(current_time[:2]) in day else "tonight")
                    menu:
                        "Do a [drivingcmp] run":
                            $ randmoney = random.randrange(50,250)
                            $ randmoney = int(round((float(randmoney) / 100.0) * float(70)))
                            $ reply = "You made $"+str(randmoney)+" {0}".format("today" if int(current_time[:2]) in day else "tonight")
                            $ renpy.notify(""+reply+"")
                            $ fp_money += randmoney
                            $ addtime(3,False)
                            call change_loc('fp_garage',loctrans=True) from _call_change_loc_13
                        "Go to [icafe]" if int(current_time[:2]) > 21 and int(current_time[:2]) <= 23 and icafe_discovered:
                            if visit_icafe_1:
                                $ addtime(False,25)
                                $ call = 'nc_talk'
                                $ event = 'icafe_visit'
                            elif visit_icafe_2:
                                $ addtime(False,25)
                                $ call = 'nc_talk'
                                $ event = 'icafe_talk'
                            elif visit_icafe_3:
                                $ addtime(False,25)
                                $ call = 'nc_talk'
                                $ event = 'icafe_talk_after_payment'
                            elif visit_icafe_4:
                                $ addtime(False,25)
                                $ call = 'nc_talk'
                                $ event = nc_event
                            else:
                                $ addtime(False,25)
                                $ call = False
                                $ event = False
                            call change_loc('icafe',sec_call=call,event=event) from _call_change_loc_15
                        "[second_menu_choice]":
                            call change_loc('fp_garage',loctrans=True) from _call_change_loc_30
                else:
                    $ renpy.notify("You should go take a shower. No way is the people using "+drivingcmp+" gonna want to ride with you")
                    $ renpy.pause(.4)
                call change_loc('fp_garage',loctrans=True) from _call_change_loc_36
        call change_loc('fp_garage',loctrans=True) from _call_change_loc_59


label fp_garage_fb(gar_fb_called=False,trans=False):
    $ current_location = 'fp_garage_fb'
    if not fp_garage_ach:
        $ fp_garage_ach = True
        $ update_been_everywhere_achievement()
    # if gar_fb_called or gar_fb_cfs:
    #     if carry_backpack:
    #         if not backpack.has_item(toolbox_item):
    #             $ toolbox_pickup = True
    #             $ update_all_the_stuff()
    #             if toolbox_added:
    #                 $ backpack.add_item(toolbox_item)
    #                 $ toolbox_added = False
    #     else:
    #         $ renpy.notify("You don't have anywhere to carry the toolbox")
    #         if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
    #             $ renpy.notify("You should try to find something to carry items in")
    #             $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
    call change_loc('fp_garage_fb') from _call_change_loc_60


label fp_garage_exit(gar_exit_called=False,trans=False):
    $ current_location = 'fp_garage_exit'
    if not fp_garage_ach:
        $ fp_garage_ach = True
        $ update_been_everywhere_achievement()
    call change_loc('fp_garage_exit') from _call_change_loc_61

label icafe_loc(ic_called=False,trans=False):
    $ current_location = 'icafe_loc'
    if not icafe_ach:
        $ icafe_ach = True
        $ update_been_everywhere_achievement()
    if ic_called or ic_cfs:
        $ ic_called = ic_cfs = False
        call change_loc('icafe') from _call_change_loc_58

label fp_kitchen_spill_loc(ks_called=False,trans=False):
    $ current_location = 'fp_kitchen'
    $ loct = False
    if not fp_kitchen_ach:
        $ fp_kitchen_ach = True
        $ update_been_everywhere_achievement()
    if ks_called or ks_cfs:
        $ ks_called = ks_cfs = False
        if not fm_seen:
            $ fm_seen = True
        else:
            call change_loc('fp_kitchen',loctrans=loct) from _call_change_loc_81
    call change_loc('fp_kitchen_spill_loc',loctrans=loct) from _call_change_loc_82

label fp_kitchen(kit_called=False,trans=False):
    $ current_location = 'fp_kitchen'
    $ loct = False
    if not fp_kitchen_ach:
        $ fp_kitchen_ach = True
        $ update_been_everywhere_achievement()
    if kit_called or kit_cfs:
        $ kit_called = kit_cfs = False
        if wine_added:
            menu:
                "Take the bottle" (cs="evil") if bottles == 1:
                    $ statschangenotify("lil_bad",1,True)
                    $ statschangenotify('fp_alignment',-1)
                    if carry_backpack:
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
                            $ renpy.notify("You should try to find something to carry items in")
                            $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Leave the bottle" (cs="good") if bottles == 1:
                    $ statschangenotify("aru_good",1,True)
                    $ statschangenotify('fp_alignment',1)
                    $ wine_added = False
                    $ loct = True
                "Take one bottle" (cs="evil") if bottles == 2:
                    $ statschangenotify("lil_bad",1,True)
                    $ statschangenotify('fp_alignment',-1)
                    if carry_backpack:
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
                            $ renpy.notify("You should try to find something to carry items in")
                            $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Take both bottles" (cs="evil") if bottles == 2:
                    $ statschangenotify("lil_bad",2,True)
                    $ statschangenotify('fp_alignment',-2)
                    if carry_backpack:
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
                            $ renpy.notify("You should try to find something to carry items in")
                            $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Leave the bottles" (cs="good") if bottles == 2:
                    $ statschangenotify("aru_good",2,True)
                    $ statschangenotify('fp_alignment',2)
                    $ wine_added = False
                    $ loct = True
                "Take one bottle" (cs="evil") if bottles == 3:
                    $ statschangenotify("lil_bad",1,True)
                    $ statschangenotify('fp_alignment',-1)
                    if carry_backpack:
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
                            $ renpy.notify("You should try to find something to carry items in")
                            $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Take two bottles" (cs="evil") if bottles == 3:
                    $ statschangenotify("lil_bad",2,True)
                    $ statschangenotify('fp_alignment',-2)
                    if carry_backpack:
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
                            $ renpy.notify("You should try to find something to carry items in")
                            $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Take all three bottles" (cs="evil") if bottles == 3:
                    $ statschangenotify("lil_bad",3,True)
                    $ statschangenotify('fp_alignment',-3)
                    if carry_backpack:
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
                            $ renpy.notify("You should try to find something to carry items in")
                            $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                        $ wine_added = False
                        $ loct = True
                "Leave the bottles" (cs="good") if bottles == 3:
                    $ statschangenotify("aru_good",3,True)
                    $ statschangenotify('fp_alignment',3)
                    $ wine_added = False
                    $ loct = True

        if int(current_time[:2]) in morning and not morning_event_done:
            call change_loc('fp_kitchen',sec_call="breakfast_interaction",loctrans=loct) from _call_change_loc_6
        elif 16 <= int(current_time[:2]) <= 18:
            if not fm_seen:
                call change_loc('fp_kitchen_spill',sec_call="fp_kitchen_spill_event",loctrans=loct) from _call_change_loc_83
            elif dinner_event:
                call change_loc('fp_kitchen',sec_call="dinner_events",loctrans=loct) from _call_change_loc_7
            else:
                call change_loc('fp_kitchen',loctrans=loct) from _call_change_loc_8
        if day_week <= 4 and int(current_time[:2]) in fs_present and renpy.random.random() < .5:
            call change_loc('fp_kitchen',loctrans=loct) from _call_change_loc_9
        elif day_week > 4 and int(current_time[:2]) in fs_present_we and renpy.random.random() < .5:
            call change_loc('fp_kitchen',loctrans=loct) from _call_change_loc_10
        else:
            call change_loc('fp_kitchen',loctrans=loct) from _call_change_loc_11

label fp_livingroom(lvr_called=False,trans=False):
    $ current_location = 'fp_livingroom'
    if lvr_called or lvr_cfs:
        $ lvr_called = lvr_cfs = False
        if not fp_livingroom_ach:
            $ fp_livingroom_ach = True
            $ update_been_everywhere_achievement()
        if carkeys_added:
            $ carkeys_added = False
            $ carkeys_pickup = True
            $ carry_carkeys = True
            $ update_all_the_stuff()
            $ backpack.add_item(carkeys_item)
            call change_loc(current_location) from _call_change_loc_64
        if day_week <= 4 and int(current_time[:2]) in fs_present and renpy.random.random() < .5:
            call change_loc('fp_livingroom') from _call_change_loc_65
        elif day_week > 4 and int(current_time[:2]) in fs_present_we and renpy.random.random() < .5:
            call change_loc('fp_livingroom') from _call_change_loc_74
        else:
            call change_loc('fp_livingroom') from _call_change_loc_14

label fp_outside(out_called=False,trans=False):
    if not carry_phone:
        menu:
            "Ah, shit, I forgot my phone! I should go get it":
                call change_loc(prev_loc) from _call_change_loc_88

    $ current_location = 'fp_outside'
    # if not bc_clicked:
    #     call fp_outside_scene from _call_outside_scene
    if out_called or out_cfs:
        $ out_called = out_cfs = False
        if not fp_outside_ach:
            $ fp_outside_ach = True
            $ update_been_everywhere_achievement()
        # if trans:
        #     call fp_outside_scene from _call_outside_scene_1
        if day_week <= 4 and int(current_time[:2]) in morning:
            call change_loc('fp outside',sec_call="go_to_school") from _call_change_loc_89
            menu go_to_school:
                "Stay home" (cs="evil"):
                    $ statschangenotify("lil_bad",1,True)
                    $ statschangenotify('fp_alignment',-1)
                    $ home_from_school = True
                    pass
                "Go to school" (cs="good"):
                    $ statschangenotify("aru_good",1,True)
                    $ statschangenotify('fp_alignment',1)
                    call travel_events('travel_school') from _call_travel_events
        call change_loc('fp outside') from _call_change_loc_90

label fp_patio(pat_called=False,trans=False):
    $ current_location = 'fp_patio'
    if not fp_patio_ach:
        $ fp_patio_ach = True
        $ update_been_everywhere_achievement()
    if pat_called or pat_cfs:
        $ pat_called = pat_cfs = False
        call change_loc('fp_patio') from _call_change_loc_93

label fp_topofstairs(uts_called=False,trans=False):
    $ current_location = 'fp_topofstairs'
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    if uts_called or uts_cfs:
        $ uts_called = uts_cfs = False
        # if backpack.has_item(princessplug_item):
        #     call change_loc('fp_topofstairs',sec_call='talk_fs')
        call change_loc('fp_topofstairs') from _call_change_loc_84

label upstairs_loc(ups_called=False,trans=False):
    $ current_location = 'fp_upstairs_loc'
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    if ups_called or ups_cfs:
        $ ups_called = ups_cfs = False
        # if backpack.has_item(princessplug_item):
        #     call change_loc('fp_topofstairs',sec_call='talk_fs')
        call change_loc('fp_upstairs') from _call_change_loc_85

label upstairs_closerdoor_loc(upscd_called=False,trans=False):
    $ current_location = 'fp_upstairs_loc'
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    if upscd_called or upscd_cfs:
        $ upscd_called = upscd_cfs = False
        call change_loc('upstairs closerdoor') from _call_change_loc_86

label upstairs_uhaf_loc(uhaf_called=False,trans=False):
    $ current_location = 'fp_upstairs_loc'
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    if uhaf_called or uhaf_cfs:
        $ uhaf_called = uhaf_cfs = False
        call change_loc('upstairs uhaf') from _call_change_loc_94

label ufbm_toilet_loc(ufbmt=False,trans=False):
    $ current_location = 'ufbm_toilet_loc'
    if ufbmt or ufbmtcfs:
        $ ufbmt = ufbmtcfs = False
        $ loct = False
        if fpsink:
            $ addtime(False,15)
            if filth_val != 0:
                $ filth_val -= 5
                if filth_val <0:
                    $ filth_val = 0
            fp "{i}Good to get the filth off my hands{/i}"
            $ fpsink = False
            $ loct = True
            $ wetshower = True
        call change_loc('ufbm toilet',loctrans=loct) from _call_change_loc_87

label fp_ufb(ufbm=False,trans=False,no_lock=False):
    $ current_location = 'fp_ufb'
    if ufbm or ufbmcfs:
        $ ufbm = ufbmcfs = False
        $ loct = False
        if occupied_bath and weather == 3:
            if not bathroom_occupied_fs and not bathroom_occupied_fm:
                if int(current_time[:2]) < 9:
                    if .15 < renpy.random.random() > .45:
                        $ bathroom_occupied_fs = True
                        $ bathroom_occupied_fm = False
                    elif renpy.random.random() < .15:
                        $ bathroom_occupied_fs = False
                        $ bathroom_occupied_fm = True
                elif 9 <= int(current_time[:2]) <= 15:
                    if .20 < renpy.random.random() > .85:
                        $ bathroom_occupied_fs = False
                        $ bathroom_occupied_fm = True
                    elif renpy.random.random() < .20:
                        $ bathroom_occupied_fs = True
                        $ bathroom_occupied_fm = False
                elif int(current_time[:2]) >= 17:
                    if .20 < renpy.random.random() > .55:
                        $ bathroom_occupied_fs = True
                        $ bathroom_occupied_fm = False
                    elif renpy.random.random() < .20:
                        $ bathroom_occupied_fs = False
                        $ bathroom_occupied_fm = True
                elif 17 < int(current_time[:2]) >= 22:
                    if .25 < renpy.random.random() > .75:
                        $ bathroom_occupied_fs = False
                        $ bathroom_occupied_fm = True
                    elif renpy.random.random() < .25:
                        $ bathroom_occupied_fs = True
                        $ bathroom_occupied_fm = False
                else:
                    $ bathroom_occupied_fs = bathroom_occupied_fm = False
        else:
            $ bathroom_occupied_fs = bathroom_occupied_fm = False
        if (bathroom_occupied_fs or bathroom_occupied_fm) and not_entered:
            "The bathroom is occupied"
            $ conditions.addcondition("Sneak a peek","(bathroom_occupied_fs or bathroom_occupied_fm) and broken_ufb_lock")
            menu:
                "Sneak a peek" (tt="You need to find a way to disable the bathroom lock" if not broken_ufb_lock else "",cs="evil"):
                    $ statschangenotify("lil_bad",1,True)
                    $ statschangenotify('fp_alignment',-1)
                    if (bathroom_occupied_fs or bathroom_occupied_fm) and not broken_ufb_lock:
                        $ set_hint("I need to find a way to break the bathroom lock...")
                    elif (bathroom_occupied_fs or bathroom_occupied_fm) and unlocked_bathroom:
                        if not fp_ufb_ach:
                            $ fp_ufb_ach = True
                            $ update_been_everywhere_achievement()
                        if int(current_time[:2]) in [6,7,8]:
                            if bathroom_occupied_fm:
                                # scene fp_ufbm_fm_doorcam_toilet
                                scene psa_renders
                                call change_loc('ufbm_toilet_loc') from _call_change_loc_95
                        else:
                            if bathroom_occupied_fs:
                                play sound "sounds/medium_camera_shutter.mp3"
                                $ image_unlock('DCIM00004_portrait.webp')
                            call change_loc('upper hallway bathroom peek',sec_call='peek_scene_happening') from _call_change_loc_17
                            label peek_scene_happening(True):
                                fp "{i}Oh {b}SHIT{/b}! That is definitely something worth getting thwapped for! But... maybe I should get the hell outta here before I get caught!{/i}"
                                $ conditions.addcondition("Stay and watch","fs_rel >= 30 and fs_aro >= 10")
                                menu:
                                    "Stay and watch" (cs="evil"):
                                        $ statschangenotify("lil_bad",1,True)
                                        $ statschangenotify('fp_alignment',-1)
                                        pass
                                    "Get the hell outta here" (cs="good"):
                                        $ statschangenotify("aru_good",1,True)
                                        $ statschangenotify('fp_alignment',1)
                                        call change_loc('fp_topofstairs') from _call_change_loc_62
                "Knock on the door" (cs="evil"):
                    if (bathroom_occupied_fs or bathroom_occupied_fm) and not broken_ufb_lock:
                        $ set_hint("I need to find a way to break the bathroom lock...")
                    if bathroom_occupied_fs:
                        if fs_mad == 1:
                            fs "What?!?"
                            fp "Hey, [fsName.informal] - I really need to pee, you think I could..."
                            fs "Fuck off, [fp]!"
                            fp "{i}Okay,then...{/i}"
                            $ statschangenotify('fs_rel',-1)
                            call change_loc('fp_topofstairs') from _call_change_loc_18
                        else:
                            fs "I'm in here, you'll have to come back later"
                            fp "I really need to pee, [fsName.informal]!"
                            if fs_rel > 30:
                                fs "{i}Teasing now...{/i}\nSorry, [fp], I'm not at all decent!"
                                fp "I don't care! I need to pee!"
                                fs "Fine! Come in, but no oogling!"
                                "{b}Click!{/b}"
                                if not fp_ufb_ach:
                                    $ fp_ufb_ach = True
                                    $ update_been_everywhere_achievement()
                                call change_loc('fp_ufb',loctrans=True,sec_call="first_bathroom_occupied_label") from _call_change_loc_19
                                label first_bathroom_occupied_label(True):
                                    fs "Lemme get back into the tub, okay?"
                                    fs "Okay, you can come in!"
                                    fp "{i}Running to the toilet{/i}\nOh....\nThanks, sis!"
                                    $ not_entered = False
                                    call change_loc('fp_ufb',loctrans=True) from _call_change_loc_20
                            else:
                                fs "I'm not decent! Use the downstairs bathroom!"
                                fp "I'll never make it! Please let me in?"
                                fs "Fine! Damn it, [fp]!"
                                "{b}Click!{/b}"
                                fs "So, get in there and do your thing!"
                                if not fp_ufb_ach:
                                    $ fp_ufb_ach = True
                                    $ update_been_everywhere_achievement()
                                call change_loc('fp_ufb',loctrans=True,sec_call="second_bathroom_occupied_label") from _call_change_loc_21
                                label second_bathroom_occupied_label(True):
                                    fp "{i}Running to the toilet{/i}\nOh...\n{i}Damn... she looks {b}hot{/b} with nothing but that towel on...{/i}"
                                    $ not_entered = False
                                    call change_loc('fp_ufb',loctrans=True) from _call_change_loc_22
                    if bathroom_occupied_fm:
                        fm "I'm in here, [fp]"
                        fp "I'm sorry, [fmName.informal], but I really, really need to pee!"
                        fm "But... I'm not decent!"
                        fp "[fmName.INFORMAL]! I need to go NOW!"
                        $ not_entered = False
                        if not fp_ufb_ach:
                            $ fp_ufb_ach = True
                            $ update_been_everywhere_achievement()
                        call change_loc('fp_ufb',loctrans=True) from _call_change_loc_23
                "Leave and come back later" (cs="good"):
                    if (bathroom_occupied_fs or bathroom_occupied_fm) and not broken_ufb_lock:
                        $ set_hint("I need to find a way to break the bathroom lock...")
                    $ statschangenotify("aru_good",1,True)
                    $ statschangenotify('fp_alignment',1)
                    # if bathroom_occupied_fs and fs_rel < 30:
                    #     $ statschangenotify('fs_rel',1)
                    # elif bathroom_occupied_fm and fm_rel < 30:
                    #     $ statschangenotify('fm_rel',1)
                    $ occupied_bath = False
                    $ hour = renpy.random.randint(0,1)
                    if hour:
                        $ addtime(hour,False)
                    else:
                        $ addtime(False, 30)
                    call change_loc('fp_topofstairs') from _call_change_loc_24
        else:
            # if not fp_bath_lock and not leave_lock and not no_lock:
            #     call change_loc('fp_ufb',sec_call='lockdoorbathroom',loctrans=True) from _call_change_loc_88
            #     label lockdoorbathroom(trans=False):
            #         $ conditions.clear()
            #         menu:
            #             "Leave door open" (cs="evil"):
            #                 $ statschangenotify("lil_bad",1,True)
            #                 $ statschangenotify('fp_alignment',-1)
            #                 $ fp_bath_lock = False
            #                 $ leave_lock = True
            #                 call change_loc('fp_ufb',loctrans=True) from _call_change_loc_89
            #             "Lock door" (cs="good"):
            #                 $ statschangenotify("aru_good",1,True)
            #                 $ statschangenotify('fp_alignment',1)
            #                 $ fp_bath_lock = True
            #                 $ leave_lock = True
            #                 call change_loc('fp_ufb',loctrans=True) from _call_change_loc_90

            if not fp_ufb_ach:
                $ fp_ufb_ach = True
                $ update_been_everywhere_achievement()
            if smallkeys_added:
                "{i}Hmm... a pair of keys. Haven't seen them before. Wonder what they open?\nShould I take them?{/i}"
                menu:
                    "Take keys":
                        $ backpack.add_item(small_keys_item)
                        $ smallkeys_added = False
                    "Leave keys":
                        $ smallkeys_added = False
            if bathroom_panties_added:
                $ current_p = getattr(store,gp_bath+"_item")
                if carry_backpack:
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
                        "Take panties" (cs="evil"):
                            $ statschangenotify("lil_bad",1,True)
                            if gp_bath == 'fsp_hot_pink':
                                if not backpack.has_item(fsp_hot_pink_item):
                                    $ fsp_hot_pink_pickup = True
                                    $ update_all_the_stuff()
                                    # $ print(str(fsp_hot_pink_item))
                                $ backpack.add_item(fsp_hot_pink_item)
                            elif gp_bath == 'fsp_black':
                                if not backpack.has_item(fsp_black_item):
                                    $ fsp_black_pickup = True
                                    $ update_all_the_stuff()
                                    # $ print(str(fsp_black_item))
                                $ backpack.add_item(fsp_black_item)
                            elif gp_bath == 'fsp_light_blue':
                                if not backpack.has_item(fsp_light_blue_item):
                                    $fsp_light_blue_pickup = True
                                    $ update_all_the_stuff()
                                    # $ print(str(fsp_light_blue_item))
                                $ backpack.add_item(fsp_light_blue_item)
                            elif gp_bath == 'fsp_yellow':
                                if not backpack.has_item(fsp_yellow_item):
                                    $ fsp_yellow_pickup = True
                                    $ update_all_the_stuff()
                                    # $ print(str(fsp_yellow_item))
                                $ backpack.add_item(fsp_yellow_item)
                            elif gp_bath == 'fsp_red':
                                if not backpack.has_item(fsp_red_item):
                                    $ fsp_red_pickup = True
                                    $ update_all_the_stuff()
                                    # $ print(str(fsp_red_item))
                                $ backpack.add_item(fsp_red_item)
                            $ bathroom_panties_added = False
                            $ bathroom_find_panties = False
                            $ fp_creep += 1
                            $ update_panties_achievements()
                            # call change_loc(current_location)
                        "Leave panties" (cs="good"):
                            $ statschangenotify("aru_good",1,True)
                            $ statschangenotify('fp_alignment',1)
                            $ bathroom_panties_added = False
                            $ bathroom_find_panties = True
                            $ loct = True
                else:
                    $ renpy.notify("You don't have anywhere to carry the panties")
                    if "You should perhaps try to get something to carry all these things you seem to be able to pick up..." not in hints+read_hints+disabled_hints:
                        $ renpy.notify("You should try to find something to carry items in")
                        $ set_hint("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
                    $ bathroom_panties_added = False
                    $ bathroom_find_panties = True
                    $ loct = True
            if fpshower:
                if not required_shower:
                    if filth_val == 0:
                        $ renpy.notify("I don't need to take a shower right now")
                    else:
                        menu:
                            "Take a quick shower - 15 minutes / 10\% cleaner":
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
                            "Use up all the hot water - 1 hour / 30\% cleaner":
                                $ addtime(1)
                                if filth_val != 0:
                                    $ filth_val -= 30
                                    if filth_val < 0:
                                        $ filth_val = 0
                                $ fpshower = False
                                $ loct = True
                                $ wetshower = True
                        fp "{i}Ah, that was refreshing{/i}"
                else:
                    jump required_shower
            if fpsink:
                $ addtime(False,15)
                if filth_val != 0:
                    $ filth_val -= 5
                    if filth_val <0:
                        $ filth_val = 0
                fp "{i}Good to get the filth off my hands{/i}"
                $ fpsink = False
                $ loct = True
                $ wetshower = True
            label required_shower:
                if required_shower:
                    menu:
                        "Take a quick shower - 15 minutes / 10\% cleaner":
                            $ addtime(False, 15)
                            if filth_val != 0:
                                $ filth_val -= 10
                                if filth_val < 0:
                                    $ filth_val = 0
                            $ required_shower = False
                            $ loct = True
                            $ wetshower = True
                        "Take a long shower - 30 minutes / 20\% cleaner":
                            $ addtime(False, 30)
                            if filth_val != 0:
                                $ filth_val -= 20
                                if filth_val < 0:
                                    $ filth_val = 0
                            $ required_shower = False
                            $ loct = True
                            $ wetshower = True
                        "Skip the shower":
                            $ required_shower = False
                            $ loct = True
                            $ wetshower = False
                            $ bathroom_occupied_fm = bathroom_occupied_fs = False
                            call change_loc('fp_topofstairs',loctrans=loct) from _call_change_loc_66
                    fp "{i}Ah, that was refreshing{/i}"

        call change_loc('fp_ufb',loctrans=loct,showerstat=wetshower) from _call_change_loc_63

label tv_games_evening(tvg_called=False,trans=False):
    if tvg_called:
        $ tvg_called = False
        $ tvr = random.randint(0,2)
        $ rtv = ['some action movie','some sci-fi series','the latest superhero-franchise-over-the-top-blow-up-everything flic']
        if random.random() < .95:
            "You decide to just see if there is anything on TV"
            $ tvtext = "After flipping through the channels, you end up watching {0} for a couple hours".format(rtv[tvr])
            "[tvtext]"
            $ addtime(2)
        else:
            "You decide to just aimlessly click through channels for now, hoping to find something worth watching"
            $ addtime(2)
        menu:
            "You decide to see if there is anything else you can do today":
                call change_loc(current_location) from _call_change_loc_79
            "You're feeling kinda exhausted, and decide to just go to bed":
                call end_of_day(True) from _call_end_of_day_10

label beach_loc(br_called=False,br_cfs=False):
    if br_called or br_cfs:
        $ br_called = br_cfs = False
        $ addtime(1,30)
        call change_loc('beach') from _call_change_loc_26
    # call end_of_day()

label next_town_ride(ntr_called=False,trans=False):
    if ntr_called:
        $ ntr_called = False
        "This is just a placeholder for this event"
        call end_of_day(True) from _call_end_of_day_4
label cabin_ride(cr_called=False,trans=False):
    if cr_called:
        $ cr_called = False
        "This is just a placeholder for this event"
        call end_of_day(True) from _call_end_of_day_5
label marina_ride(mr_called=False,trans=False):
    if mr_called:
        $ mr_called = False
        "This is just a placeholder for this event"
        call end_of_day(True) from _call_end_of_day_6