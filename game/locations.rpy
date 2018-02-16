# location changer
label change_loc(locname=False,loctrans=False,timeadd=False,char=False,imgname=False,sec_call=False):
    if timeadd:
        $ addtime(False, 30)
    if locname:
        if 'loc' not in locname:
            $ current_location = locname.replace(' ','_')+"_loc"
        else:
            $ current_location = locname.replace(' ','_')
            $ locname = locname.replace('_loc','')
        $ tmpname = locname.replace(' ','_').replace('_loc','')+"_scene"
        if loctrans:
            $ loctrans = False
            call expression tmpname pass (False)
        else:
            call expression tmpname
        show screen location(locname)
        if locname in firstday_talk_list:
            if firstday_talk:
                if renpy.random.random() > .75:
                    call fs_talk(True)
        if char and imgname:
            show expression "images/characters/[char]/body/standing/[imgname].png" as character: # at fs_standing_ahead_ani with dissolve:
                zoom .65
                xpos .7
                ypos 1.0
                xanchor .5
                yanchor .75
        if sec_call:
            call expression sec_call pass (True)
        call screen empty()
        hide screen empty
        hide screen location
        hide character

label entrance_loc(trans=False):
    $ current_location = 'entrance_loc'
    if not entrance_ach:
        $ entrance_ach = True
        $ update_been_everywhere_achievement()
    call change_loc('entrance')

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
                $ renpy.notify("You don't have anything to carry the books in")
                $ schoolbooks_added = False
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
            call fp_morning_content(True)
        else:
            call change_loc('fp bedroom',loctrans=loct)

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
            "You do not have anywhere to carry these at the moment"
            if 'carry all these things' not in hints:
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
        call change_loc('fs bedroom',loctrans=loct)

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
            $ renpy.notify("You don't have anywhere to carry this item")
        call change_loc('garage')

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
                        $ renpy.notify("You have no way of carrying this")
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
                        $ renpy.notify("You have no way of carrying this")
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
                        $ renpy.notify("You have no way of carrying this")
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
                        $ renpy.notify("You have no way of carrying this")
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
                        $ renpy.notify("You have no way of carrying this")
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
                        $ renpy.notify("You have no way of carrying this")
                        $ wine_added = False                        
                        $ loct = True
                "Leave the bottles" if bottles == 3:
                    $ wine_added = False
                    $ loct = True

        if int(current_time[:2]) in morning and not morning_event_done:
            call change_loc('kitchen',sec_call="breakfast_interaction",loctrans=loct)
        elif 16 <= int(current_time[:2]) <= 18:
            if dinner_event:
                call change_loc('kitchen',sec_call="dinner_events",loctrans=loct)
            else:
                call change_loc('kitchen',loctrans=loct)
        if day_week <= 4 and int(current_time[:2]) in fs_present and renpy.random.random() < .5:
            call change_loc('kitchen',sec_call='fs_talk',loctrans=loct)
        elif day_week > 4 and int(current_time[:2]) in fs_present_we and renpy.random.random() < .5:
            call change_loc('kitchen',sec_call='fs_talk',loctrans=loct)
        else:
            call change_loc('kitchen',loctrans=loct)

label livingroom_loc(lvr_called=False,trans=False):
    $ current_location = 'livingroom_loc'
    if lvr_called or lvr_cfs:
        $ lvr_called = lvr_cfs = False
        if not livingroom_ach:
            $ livingroom_ach = True
            $ update_been_everywhere_achievement()
        if day_week <= 4 and int(current_time[:2]) in fs_present and renpy.random.random() < .5:
            call change_loc('livingroom',sec_call='fs_talk')
        elif day_week > 4 and int(current_time[:2]) in fs_present_we and renpy.random.random() < .5:
            call change_loc('livingroom',sec_call='fs_talk')
        else:
            call change_loc('livingroom')

label outside_loc(out_called=False,trans=False):
    $ current_location = 'outside_loc'
    if out_called or out_cfs:
        $ out_called = out_cfs = False
        if not outside_ach:
            $ outside_ach = True
            $ update_been_everywhere_achievement()
        if trans:    
            call outside_scene
        if day_week <= 4 and int(current_time[:2]) in morning:
            call outside_scene
            menu:
                "Go to school":
                    # call travel_school(True)
                    call travel_events('travel_school')
                    # call nk_talk(True)
                "Stay home":
                    pass
        call change_loc('outside')

label upper_hallway_loc(uhl_called=False,trans=False):
    $ current_location = 'upper_hallway_loc'
    if not uhl_ach:
        $ uhl_ach = True
        $ update_been_everywhere_achievement()        
    if uhl_called or uhl_cfs:
        $ uhl_called = uhl_cfs = False
        if backpack.has_item(princessplug_item):
            call talk_fs(True)   
        call change_loc('upper hallway')

label upper_hallway_bathroom_loc(uhl_bl_called=False,trans=False):
    $ current_location = 'upper_hallway_bathroom_loc'
    $ loct = False
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
                        $ fp_creep += 1
                        $ update_panties_achievements()
                    "Leave panties":
                        $ bathroom_panties_added = False
                        $ bathroom_find_panties = True
                        $ loct = True               
        else:
            "You have nowhere to keep those panties at the moment"
            if 'carry all these things' not in hints:
                $ hints.append("You should perhaps try to get something to carry all these things you seem to be able to pick up...")
            $ bathroom_panties_added = False
            $ bathroom_find_panties = True
            $ loct = True
        if fpshower:
            if filth_val == 0:
                fp "I don't need to take a shower right now"
            else:
                if day_week <= 4 and int(current_time[:2]) < 8:
                    $ addtime(False,30)
                else:
                    $ addtime(1, False)
                if filth_val != 0:
                    $ filth_val -= 20
                    if filth_val < 0:
                        $ filth_val = 0
                fp "{i}Ah, that was refreshing{/i}"
            $ fpshower = False
            $ loct = True
        if fpsink:
            $ addtime(False,15)
            if filth_val != 0:
                $ filth_val -= 5
                if filth_val <0:
                    $ filth_val = 0
            fp "{i}Good to get the filth off my hands{/i}"
            $ fpsink = False
            $ loct = True
        call change_loc('upper hallway bathroom',loctrans=loct)

label tv_games_evening(tvg_called=False,trans=False):
    if tvg_called:
        $ tvg_called = False
        "This is just a placeholder for this event"
    call end_of_day()

label beach_ride(br_called=False):
    if br_called:
        $ br_called = False
        $ addtime(1,30)
        call change_loc('beach')
    call end_of_day()

label next_town_ride(ntr_called=False,trans=False):
    if ntr_called:
        $ ntr_called = False
        "This is just a placeholder for this event"
    call end_of_day()
label cabin_ride(cr_called=False,trans=False):
    if cr_called:
        $ cr_called = False
        "This is just a placeholder for this event"
    call end_of_day()
label marina_ride(mr_called=False,trans=False):
    if mr_called:
        $ mr_called = False
        "This is just a placeholder for this event"    
    call end_of_day()