# location changer
label change_loc(locname=False,timeadd=False,char=False,imgname=False):
    if timeadd:
        $ addtime(False, 30)
    if locname:
        $ current_location = locname.replace(' ','_')+"_loc"
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
        
label entrance_loc():
    if not entrance_ach:
        $ entrance_ach = True
        $ update_been_everywhere_achievement()
    call entrance_scene
    call change_loc('entrance')
    # # return

label fp_bedroom_loc(fpl_called=False):
    $ update_been_everywhere_achievement()    
    if fpl_called or uhl_fpb_cfs:
        $ fpl_called = uhl_fpb_cfs = False
        call fp_bedroom_scene
        if schoolbooks_added:
            $ backpack.add_item(schoolbooks_item)
            $ schoolbooks_added = False
        if phone_added:
            $ backpack.add_item(phone_item)
            $ phone_added = False
            $ carry_phone = True
        if current_hour[:2] in morning and not morning_event_done:
            call fp_morning_content(True)
        else:
            call change_loc('fp bedroom')                
    # else:
    #     # return

label fs_bedroom_loc(fsl_called=False):
    if not fs_bedroom_ach:
        $ fs_bedroom_ach = True
        $ update_been_everywhere_achievement()        
    if fsl_called or uhl_fsb_cfs:
        $ fsl_called = uhl_fsb_cfs = False
        if ipad_added:
            "Oh, she left her iPad..."
            if not ipad_always_look:
                menu:
                    "Look at iPad":
                        show ipad_background:
                            zoom .5
                            yalign .5
                            xalign .5
                        $ renpy.pause()
                        $ ipad_added = False
                        $ find_ipad = True
                        $ ipad_always_look = True
                    "Leave iPad":
                        $ ipad_added = False
                        $ find_ipad = True
            else:
                show ipad_background:
                    zoom .5
                    yalign .5
                    xalign .5
                $ renpy.pause()
                $ ipad_added = False
                $ find_ipad = True
        if panties_added:
            # "Hm... [fsName.formal]s panties...\n{b}sniffs them{/b}\nShould I take them with me?"
            $ current_p = getattr(store,gp_bed+"_panties_item")
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
                        $ backpack.add_item(fs_bright_pink_panties_item)
                    elif gp_bed == 'fs_pale_pink':
                        $ backpack.add_item(fs_pale_pink_panties_item)
                    elif gp_bed == 'fs_light_blue':
                        $ backpack.add_item(fs_light_blue_panties_item)
                    elif gp_bed == 'fs_yellow':
                        $ backpack.add_item(fs_yellow_panties_item)
                    $ panties_added = False
                    $ fp_creep += 1
                    $ update_panties_achievements()
                "Leave panties":
                    $ panties_added = False
                    $ find_panties = True
        if pb_added:
            "Holy... is that a {b}buttplug{/b}!?"
            menu:
                "Take the buttplug":
                    $ pb_added = False
                    $ statschangenotify('fs_cor',1,True)
                    $ statschangenotify('fs_anal',3)                    
                    $ backpack.add_item(pink_buttplug_item)
                "Leave the buttplug":
                    $ pb_added = False
                    $ statschangenotify('fs_cor',1,True)
                    $ find_pb = True

        call fs_bedroom_scene
        call change_loc('fs bedroom')
    # else:
    #     # return

label garage_loc(gar_called=False):
    if not garage_ach:
        $ garage_ach = True
        $ update_been_everywhere_achievement()
    if gar_called or gar_cfs:
        $ gar_called = g_called_from_screen = False
        if not backpack.has_item(toolbox_item):
            if toolbox_added:
                $ backpack.add_item(toolbox_item)
                $ toolbox_added = False
        call garage_scene
        call change_loc('garage')
    #     # return
    # else:
    #     # return

label kitchen_loc(kit_called=False):
    if not kitchen_ach:
        $ kitchen_ach = True
        $ update_been_everywhere_achievement()
    if kit_called or kit_cfs:
        $ kit_called = kit_cfs = False
        if wine_added:
            menu:
                "Take the bottle" if bottles == 1:
                    $ backpack.add_item(wine_item)
                    $ bottles = 0
                    $ br = 0
                    $ wcount = 0
                    $ wine_added = False
                    $ achievement_wine_collector.update()
                    $ achievement_all_the_wine.update()
                    $ achievement_even_more_wine.update()
                "Leave the bottle" if bottles == 1:
                    $ wine_added = False
                "Take one bottle" if bottles == 2:
                    $ backpack.add_item(wine_item)
                    $ bottles = 1
                    $ br = 1
                    $ wine_added = False
                    $ achievement_wine_collector.update()                    
                    $ achievement_all_the_wine.update()
                    $ achievement_even_more_wine.update()                    
                "Take both bottles" if bottles == 2:
                    $ backpack.add_item(wine_item)
                    $ renpy.pause(.25)
                    $ backpack.add_item(wine_item)
                    $ bottles = 0
                    $ br = 0
                    $ wcount = 0
                    $ wine_added = False
                    $ achievement_wine_collector.update(2)                                        
                    $ achievement_all_the_wine.update(2)
                    $ achievement_even_more_wine.update(2)                    
                "Leave the bottles" if bottles == 2:
                    $ wine_added = False
                "Take one bottle" if bottles == 3:
                    $ backpack.add_item(wine_item)
                    $ bottles = 2
                    $ br = 2
                    $ wine_added = False
                    $ achievement_wine_collector.update()
                    $ achievement_all_the_wine.update()
                    $ achievement_even_more_wine.update()                                        
                "Take two bottles" if bottles == 3:
                    $ backpack.add_item(wine_item)
                    $ renpy.pause(.25)
                    $ backpack.add_item(wine_item)
                    $ bottles = 1
                    $ br = 1
                    $ wine_added = False
                    $ achievement_wine_collector.update(2)                    
                    $ achievement_all_the_wine.update(2)
                    $ achievement_even_more_wine.update(2)                    
                "Take all three bottles" if bottles == 3:
                    $ backpack.add_item(wine_item)
                    $ renpy.pause(.25)
                    $ backpack.add_item(wine_item)
                    $ renpy.pause(.25)
                    $ backpack.add_item(wine_item)
                    $ bottles = 0
                    $ br = 0
                    $ wcount = 0
                    $ wine_added = False
                    $ achievement_wine_collector.update(3)                    
                    $ achievement_all_the_wine.update(3)
                    $ achievement_even_more_wine.update(3)                    
                "Leave the bottles" if bottles == 3:
                    $ wine_added = False
        if int(current_hour[:2]) in morning and not morning_event_done:
            call kitchen_scene
            # call change_loc('kitchen')
            call breakfast_interaction(True)
        elif int(current_hour[:2]) >= 16 and int(current_hour[:2]) <= 18:
            call kitchen_scene
            if dinner_event:
                call dinner_events(True)
            else:
                call change_loc('kitchen')
        else:
            call kitchen_scene
            call change_loc('kitchen')
        # return
    # else:
    #     # return

label livingroom_loc(lvr_called=False):
    if lvr_called or lvr_cfs:
        $ lvr_called = lvr_cfs = False
        if not livingroom_ach:
            $ livingroom_ach = True
            $ update_been_everywhere_achievement()
        call livingroom_scene
        call change_loc('livingroom')
    # return

# label lower_hallway_loc():
#     call lower_hallway_scene
#     call change_loc('lower hallway')
#     # return

label outside_loc(out_called=False):
    if out_called or out_cfs:
        $ out_called = out_cfs = False
        if not outside_ach:
            $ outside_ach = True
            $ update_been_everywhere_achievement()        
        call outside_neighborhood_scene
        if day_week <= 4 and int(current_hour[:2]) in morning:
            menu:
                "Go to school":
                    call travel_school(True)
                "Stay home":
                    pass
        call change_loc('outside neighborhood')
    # return

label upper_hallway_loc(uhl_called=False):
    if not uhl_ach:
        $ uhl_ach = True
        $ update_been_everywhere_achievement()        
    if uhl_called or uhl_cfs:
        $ uhl_called = uhl_cfs = False
        call upper_hallway_scene
        if backpack.has_item(pink_buttplug_item):
            call talk_fs(True)   
        call change_loc('upper hallway')
        # return
    # else:
    #     # return

label upper_hallway_bathroom_loc(uhl_bl_called=False):
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
            # "Hm... [fsName.formal]s panties...\n{b}sniffs them{/b}\nShould I take them with me?"
            $ current_p = getattr(store,gp_bath+"_panties_item")
            if not backpack.has_item(current_p):
                $ r = random.randint(0,3)
                # $ renpy.watch(str(r))
                $ text = p_response[r]
                if r == 0 or r == 3:
                    $ panties_sniffer = True
                    $ update_panties_achievements()
            else:
                $ aux = list(p_response)
                $ del aux[2]
                $ r = random.randrange(len(aux))
                # $ renpy.watch(str(r)+"aux")                
                $ text = p_response[r]
                if r == 0 or r == 3:
                    $ panties_sniffer = True
                    $ update_panties_achievements()
            "[text]"            
            menu:
                "Take panties":
                    if gp_bath == 'fs_bright_pink':
                        $ backpack.add_item(fs_bright_pink_panties_item)
                    elif gp_bath == 'fs_pale_pink':
                        $ backpack.add_item(fs_pale_pink_panties_item)
                    elif gp_bath == 'fs_light_blue':
                        $ backpack.add_item(fs_light_blue_panties_item)
                    elif gp_bath == 'fs_yellow':
                        $ backpack.add_item(fs_yellow_panties_item)
                    $ bathroom_panties_added = False
                    $ fp_creep += 1
                    $ update_panties_achievements()
                "Leave panties":
                    $ bathroom_panties_added = False
                    $ bathroom_find_panties = True                    
        if fpshower:
            $ addtime(1, False)
            fp "{i}Ah, that was refreshing{/i}"
            $ fpshower = False
        if fpsink:
            $ addtime(False,15)
            fp "{i}Good to get the filth off my hands{/i}"
            $ fpsink = False
        call upper_hallway_bathroom_scene
        call change_loc('upper hallway bathroom')
        # hide screen room
    # $ renpy.pause()
    # # return

label tv_games_evening(tvg_called=False):
    if tvg_called:
        $ tvg_called = False
        "This is just a placeholder for this event"
    call end_of_day()

label beach_ride(br_called=False):
    if br_called:
        $ br_called = False
        $ addtime(1,30)
        call beach_scene
        call change_loc('beach')
    call end_of_day()

label next_town_ride(ntr_called=False):
    if ntr_called:
        $ ntr_called = False
        "This is just a placeholder for this event"
    call end_of_day()
label cabin_ride(cr_called=False):
    if cr_called:
        $ cr_called = False
        "This is just a placeholder for this event"
    call end_of_day()
label marina_ride(mr_called=False):
    if mr_called:
        $ mr_called = False
        "This is just a placeholder for this event"    
    call end_of_day()