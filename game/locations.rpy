label entrance_loc():
    call entrance_scene
    call change_loc('entrance')
    # return

label fp_bedroom_loc(fpl_called=False):
    if fpl_called or uhl_fpb_cfs:
        $ fpl_called = uhl_fpb_cfs = False
        call fp_bedroom_scene
        if schoolbooks_added:
            $ backpack.add_item(schoolbooks_item)
            $ schoolbooks_added = False
        if current_hour[:2] in morning and not morning_event_done:
            call fp_morning_content(True)
        else:
            call change_loc('fp bedroom')                
    # else:
    #     return

label fs_bedroom_loc(fsl_called=False):
    if fsl_called or uhl_fsb_cfs:
        $ fsl_called = uhl_fsb_cfs = False
        if panties_added:
            "Hm... [fsName.formal]s panties...\n{b}sniffs them{/b}\nShould I take them with me?"
            menu:
                "Take panties":
                    if gp == 'fs_bright_pink_panties':
                        $ backpack.add_item(fs_bright_pink_panties_item)
                    elif gp == 'fs_pale_pink_panties':
                        $ backpack.add_item(fs_pale_pink_panties_item)
                    elif gp == 'fs_light_blue_panties':
                        $ backpack.add_item(fs_light_blue_panties_item)
                    elif gp == 'fs_yellow_panties':
                        $ backpack.add_item(fs_yellow_panties_item)
                    $ panties_added = False
                "Leave panties":
                    $ panties_added = False
        call fs_bedroom_scene
        call change_loc('fs bedroom')
    # else:
    #     return

label garage_loc(gar_called=False):
    if gar_called or gar_cfs:
        $ gar_called = g_called_from_screen = False
        if not backpack.has_item(toolbox_item):
            if toolbox_added:
                $ backpack.add_item(toolbox_item)
                $ toolbox_added = False
        call garage_scene
        call change_loc('garage')
    #     return
    # else:
    #     return

label kitchen_loc(kit_called=False):
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
                "Leave the bottle" if bottles == 1:
                    $ wine_added = False
                "Take one bottle" if bottles == 2:
                    $ backpack.add_item(wine_item)
                    $ bottles = 1
                    $ br = 1
                    $ wcount = 0
                    $ wine_added = False
                "Take both bottles" if bottles == 2:
                    $ backpack.add_item(wine_item)
                    $ renpy.pause(.25)
                    $ backpack.add_item(wine_item)
                    $ bottles = 0
                    $ br = 0
                    $ wcount = 0
                    $ wine_added = False
                "Leave the bottles" if bottles == 2:
                    $ wine_added = False
                "Take one bottle" if bottles == 3:
                    $ backpack.add_item(wine_item)
                    $ bottles = 2
                    $ br = 2
                    $ wcount = 0
                    $ wine_added = False
                "Take two bottles" if bottles == 3:
                    $ backpack.add_item(wine_item)
                    $ renpy.pause(.25)
                    $ backpack.add_item(wine_item)
                    $ bottles = 1
                    $ br = 1
                    $ wcount = 0
                    $ wine_added = False
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
                "Leave the bottles" if bottles == 3:
                    $ wine_added = False
        if current_hour[:2] in morning and not morning_event_done:
            # if int(current_hour[:2]) <= 9:
            call kitchen_scene
            call change_loc('kitchen')
            call breakfast_interaction(True)
        else:
            call kitchen_scene
            call change_loc('kitchen')
        return
    # else:
    #     return

label livingroom_loc():
    call livingroom_scene
    call change_loc('livingroom')
    return

label lower_hallway_loc():
    call lower_hallway_scene
    call change_loc('lower hallway')
    return

label outside_loc():
    call outside_neighborhood_scene
    call change_loc('outside neighborhood')
    return

label upper_hallway_loc(uhl_called=False):
    if uhl_called or uhl_cfs:
        $ uhl_called = uhl_cfs = False
        call upper_hallway_scene
        call change_loc('upper hallway')
        return
    # else:
    #     return

label upper_hallway_bathroom_loc(uhl_bl_called=False):
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
        if fpshower:
            call addtime(1, False)
            fp "{i}Ah, that was refreshing{/i}"
            $ fpshower = False
        if fpsink:
            call addtime(False,15)
            fp "{i}Good to get the filth off my hands{/i}"
            $ fpsink = False
        call upper_hallway_bathroom_scene
        call change_loc('upper hallway bathroom')
        # hide screen room
    # $ renpy.pause()
    # return
