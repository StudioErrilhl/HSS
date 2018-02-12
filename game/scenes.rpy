label beach_scene:
    if not beach_ach:
        $ beach_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_time[:2]) in night:
        scene beach_night with Dissolve(.25)
        return
    else:
        scene beach_morning with Dissolve(.25)
        return
    return

label entrance_scene:
    if not entrance_ach:
        $ entrance_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_time[:2]) in night:
        scene entrance_night with Dissolve(.25)
    else:
        scene entrance_morning with Dissolve(.25)
    return

label fp_bedroom_scene(trans=True): #this is the starting scene, and the one that repeats every morning (unless there are circumstances altering the morning events)
    if not fp_bedroom_ach:
        $ fp_bedroom_ach = True
        $ update_been_everywhere_achievement()
    $ hours = [0,1,22,23]
    if int(current_time[:2]) in hours:
        if backpack.has_item(phone_item):
            if trans:
                scene fp_bedroom_night_glow with Dissolve(.25)
            else:
                scene fp_bedroom_night_glow
        else:
            if trans:
                scene fp_bedroom_night_glow_phone with Dissolve(.25)
            else:
                scene fp_bedroom_night_glow_phone
    elif int(current_time[:2]) in night:
        if backpack.has_item(phone_item):
            if trans:
                scene fp_bedroom_night with Dissolve(.25)
            else:
                scene fp_bedroom_night
        else:
            if trans:
                scene fp_bedroom_night_phone with Dissolve(.25)
            else:
                scene fp_bedroom_night_phone
    else:
        if backpack.has_item(phone_item):
            if trans:
                scene fp_bedroom_morning with Dissolve(.25)
            else:
                scene fp_bedroom_morning
        else:
            if trans:
                scene fp_bedroom_morning_phone with Dissolve(.25)
            else:
                scene fp_bedroom_morning_phone
    return

label fs_bedroom_scene(trans=True):
    if not fs_bedroom_ach:
        $ fs_bedroom_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_time[:2]) in night:
        if trans:
            scene fs_bedroom_night with Dissolve(.25)
        else:
            scene fs_bedroom_night
    else:
        if trans:
            scene fs_bedroom_morning with Dissolve(.25)
        else:
            scene fs_bedroom_morning
    return

label fs_intro_scene:
    if day_week == 0 and current_month == 4:
        scene fs_intro_scene with Dissolve(.25)
    else:
        scene fs_intro_scene with Dissolve(.25)
    return

label garage_scene:
    if not garage_ach:
        $ garage_ach = True
        $ update_been_everywhere_achievement()        
    if mc_f:
        if int(current_time[:2]) in night:
            scene honda_cx_500_finished_night with Dissolve(.25)
        else:
            scene honda_cx_500_finished_morning with Dissolve(.25)
    else:
        if int(current_time[:2]) in night:
            scene honda_cx_500_build_night with Dissolve(.25)
        else:
            scene honda_cx_500_build_morning with Dissolve(.25)
    return

label kitchen_scene(trans=True):
    if not kitchen_ach:
        $ kitchen_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_time[:2]) in night:
        if trans:
            scene kitchen_night with Dissolve(.25)
        else:
            scene kitchen_night
    else:
        if trans:
            scene kitchen_morning with Dissolve(.25)
        else:
            scene kitchen_morning
    return   

label livingroom_scene:
    if not livingroom_ach:
        $ livingroom_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene livingroom_night with Dissolve(.25)
    else:
        scene livingroom_morning with Dissolve(.25)
    return

label outside_scene:
    if not outside_ach:
        $ outside_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_time[:2]) in night:
        if bad_weather and rainstorm:
            scene neighborhood_night
            show rain
            with Dissolve(.25)
        else:
            scene neighborhood_night with Dissolve(.25)
    else:
        if bad_weather and rainstorm:
            scene neighborhood_morning
            show rain
            with Dissolve(.25)
        else:
            scene neighborhood_morning with Dissolve(.25)
    return

label schoolbuilding_scene:
    if not school_outside_ach:
        $ school_outside_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if bad_weather and rainstorm:
            scene school_outside_night
            show rain
            with Dissolve(.25)
        else:
            scene school_outside_night with Dissolve(.25)
    else:
        if bad_weather and rainstorm:
            scene school_outside_morning
            show rain
            with Dissolve(.25)
        else:
            scene school_outside_morning with Dissolve(.25)
    return

label school_po_scene:
    if not school_principal_office_ach:
        $ school_prinicpal_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene school_principal_office_night with Dissolve(.25)
    else:
        scene school_principal_office_morning with Dissolve(.25)
    return

label upper_hallway_scene:
    if not uhl_ach:
        $ uhl_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_time[:2]) in night:
        scene upper_hallway_night with Dissolve(.25)
    else:
        scene upper_hallway_morning with Dissolve(.25)
    return

label upper_hallway_bathroom_scene(trans=True):
    if not uhl_bathroom_ach:
        $ uhl_bathroom_ach = True
        $ update_been_everywhere_achievement()        
    if int(current_time[:2]) in night and bathroom_light:
        if trans:
            scene upper_hallway_bathroom_night_light with Dissolve(.25)
        else:
            scene upper_hallway_bathroom_night_light
    elif int(current_time[:2]) in night:
        if trans:
            scene upper_hallway_bathroom_night with Dissolve(.25)
        else:
            scene upper_hallway_bathroom_night
    else:
        if trans:
            scene upper_hallway_bathroom_morning with Dissolve(.25)
        else:
            scene upper_hallway_bathroom_morning
    return