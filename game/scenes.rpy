label beach_scene:
    if int(current_hour[:2]) in night:
        scene beach_night
    else:
        scene beach_morning
    return

label entrance_scene:
    if int(current_hour[:2]) in night:
        scene entrance_night
    else:
        scene entrance_morning
    return

label fp_bedroom_scene: #this is the starting scene, and the one that repeats every morning (unless there are circumstances altering the morning events)
    $ hours = [0,1,22,23]
    if int(current_hour[:2]) in hours:
        scene fp_bedroom_night_glow
    elif int(current_hour[:2]) in night:
        scene fp_bedroom_night
    else:
        scene fp_bedroom_morning
    return

label fs_bedroom_scene:
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
    if mc_f:
        scene honda_cx_500_finished
    else:
        if int(current_hour[:2]) in night:
            scene honda_cx_500_build_night
        else:
            scene honda_cx_500_build_morning
    return

label kitchen_scene:
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

label lower_hallway_scene:
    if int(current_hour[:2]) in night:
        scene lower_hallway_night
    else:
        scene lower_hallway_morning
    return

label outside_neighborhood_scene:
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
    if int(current_hour[:2]) in night:
        scene upper_hallway_night
    else:
        scene upper_hallway_morning
    return

label upper_hallway_bathroom_scene:
    if int(current_hour[:2]) in night and bathroom_light:
        scene upper_hallway_bathroom_night_light
    elif int(current_hour[:2]) in night:
        scene upper_hallway_bathroom_night
    else:
        scene upper_hallway_bathroom_morning
    return