label beach_scene:
    if not beach_ach:
        $ beach_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_hour[:2]) in night:
        scene beach_night
        return
    else:
        scene beach_morning
        return
    return

label entrance_scene:
    if not entrance_ach:
        $ entrance_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_hour[:2]) in night:
        scene entrance_night
    else:
        scene entrance_morning
    return

label fp_bedroom_scene: #this is the starting scene, and the one that repeats every morning (unless there are circumstances altering the morning events)
    $ update_been_everywhere_achievement()
    $ hours = [0,1,22,23]
    if int(current_hour[:2]) in hours:
        if backpack.has_item(phone_item):
            scene fp_bedroom_night_glow
        else:
            scene fp_bedroom_night_glow_phone
    elif int(current_hour[:2]) in night:
        if backpack.has_item(phone_item):
            scene fp_bedroom_night
        else:
            scene fp_bedroom_night_phone
    else:
        if backpack.has_item(phone_item):
            scene fp_bedroom_morning
        else:
            scene fp_bedroom_morning_phone
    return

label fs_bedroom_scene:
    if not fs_bedroom_ach:
        $ fs_bedroom_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_hour[:2]) in night:
        scene fs_bedroom_night
    else:
        scene fs_bedroom_morning
    return

label fs_intro_scene:
    if day_week == 0 and current_month == 4:
        scene fs_intro_scene
    else:
        scene fs_intro_scene
    return

label garage_scene:
    if not garage_ach:
        $ garage_ach = True
        $ update_been_everywhere_achievement()        
    if mc_f:
        if int(current_hour[:2]) in night:
            scene honda_cx_500_finished_night
        else:
            scene honda_cx_500_finished_morning
    else:
        if int(current_hour[:2]) in night:
            scene honda_cx_500_build_night
        else:
            scene honda_cx_500_build_morning
    return

label kitchen_scene:
    if not kitchen_ach:
        $ kitchen_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_hour[:2]) in night:
        scene kitchen_night
    else:
        scene kitchen_morning
    return   

label livingroom_scene:
    if int(current_hour[:2]) in night:
        scene livingroom_night
    else:
        scene livingroom_morning
    return

# label lower_hallway_scene:
#     if int(current_hour[:2]) in night:
#         scene lower_hallway_night
#     else:
#         scene lower_hallway_morning
#     return

label outside_neighborhood_scene:
    if not outside_ach:
        $ outside_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_hour[:2]) in night:
        if bad_weather and rainstorm:
            scene neighborhood_night
            show rain
        else:
            scene neighborhood_night
    else:
        if bad_weather and rainstorm:
            scene neighborhood_morning
            show rain
        else:
            scene neighborhood_morning
    return

label schoolbuilding_scene:
    if not school_ach:
        $ school_ach = True
        $ update_been_everywhere_achievement()
    if int(current_hour[:2]) in night:
        if bad_weather and rainstorm:
            scene schoolbuilding_night
            show rain
        else:
            scene schoolbuilding_night
    else:
        if bad_weather and rainstorm:
            scene schoolbuilding_morning
            show rain
        else:
            scene schoolbuilding_morning
    return

label upper_hallway_scene:
    if not uhl_ach:
        $ uhl_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_hour[:2]) in night:
        scene upper_hallway_night
    else:
        scene upper_hallway_morning
    return

label upper_hallway_bathroom_scene:
    if not uhl_bathroom_ach:
        $ uhl_bathroom_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_hour[:2]) in night and bathroom_light:
        scene upper_hallway_bathroom_night_light
    elif int(current_hour[:2]) in night:
        scene upper_hallway_bathroom_night
    else:
        scene upper_hallway_bathroom_morning
    return