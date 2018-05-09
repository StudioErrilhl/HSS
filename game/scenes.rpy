label beach_scene(trans=True):
    if not beach_ach:
        $ beach_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene beach_night with Dissolve(.25)
    else:
        scene beach morning with Dissolve(.25)
    return

label entrance_scene(trans=True):
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
    if not backpack_carry:
        if int(current_time[:2]) in hours:
            if not carry_phone and not carry_wallet:
                scene fp_bedroom_night_glow_phone_backpack_wallet
            elif not carry_phone:
                scene fp_bedroom_night_glow_phone_backpack
            elif not carry_wallet:
                scene fp_bedroom_night_glow_backpack_wallet
            else:
                scene fp_bedroom_night_glow_backpack
        elif int(current_time[:2]) in night:
            if not carry_phone and not carry_wallet:
                scene fp_bedroom_night_phone_backpack_wallet
            elif not carry_phone:
                scene fp_bedroom_night_phone_backpack
            elif not carry_wallet:
                scene fp_bedroom_night_backpack_wallet
            else:
                scene fp_bedroom_night_backpack
        else:
            if not carry_phone and not carry_wallet:
                scene fp_bedroom_morning_phone_backpack_wallet
            elif not carry_phone:
                scene fp_bedroom_morning_phone_backpack
            elif not carry_wallet:
                scene fp_bedroom_morning_backpack_wallet
            else:
                scene fp_bedroom_morning_backpack
    else:
        if int(current_time[:2]) in hours:
            if not carry_phone and not carry_wallet:
                scene fp_bedroom_night_glow_phone_wallet
            elif not carry_phone:
                scene fp_bedroom_night_glow_phone
            elif not carry_wallet:
                scene fp_bedroom_night_glow_wallet
            else:
                scene fp_bedroom_night
        elif int(current_time[:2]) in night:
            if not carry_phone and not carry_wallet:
                scene fp_bedroom_night_phone_wallet
            elif not carry_phone:
                scene fp_bedroom_night_phone
            elif not carry_wallet:
                scene fp_bedroom_night_wallet
            else:
                scene fp_bedroom_night
        else:
            if not carry_phone and not carry_wallet:
                scene fp_bedroom_morning_phone_wallet
            elif not carry_phone:
                scene fp_bedroom_morning_phone
            elif not carry_wallet:
                scene fp_bedroom_morning_wallet
            else:
                scene fp_bedroom_morning
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
    if day_week == 5 and current_month == 3:
        scene fs_bedroom_morning_intro with Dissolve(.25)
        show juliette_on_bed_intro with Dissolve(.25):
            zoom .6
            xalign .5
            yalign 1.0
            xoffset -100
            yoffset -65
    # else:
    #     scene fs_intro_scene with Dissolve(.25)
    return

label garage_scene(trans=True):
    if not garage_ach:
        $ garage_ach = True
        $ update_been_everywhere_achievement()
    if mc_f:
        if int(current_time[:2]) in night:
            if trans:
                scene garage_finished_night with Dissolve(.25)
            else:
                scene garage_finished_night
        else:
            if trans:
                scene garage_finished_morning with Dissolve(.25)
            else:
                scene garage_finished_morning
    else:
        if int(current_time[:2]) in night:
            if trans:
                scene garage_build_night with Dissolve(.25)
            else:
                scene garage_build_night
        else:
            if trans:
                scene garage_build_morning with Dissolve(.25)
            else:
                scene garage_build_morning
    return

label icafe_scene(trans=True):
    if not icafe_ach:
        $ icafe_ach = True
        $ update_been_everywhere_achievement()
    if trans:
        scene icafe with Dissolve(.25)
    else:
        scene icafe
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

label livingroom_scene(trans=True):
    if not livingroom_ach:
        $ livingroom_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if bad_weather:
            scene livingroom_night_bad_weather with Dissolve(.25)
        else:
            scene livingroom_night with Dissolve(.25)
        if bad_weather:
            if rainstorm:
                show rain behind livingroom_night_bad_weather
                show livingroom_night_bad_weather_windows behind rain
            else:
                show livingroom_night_bad_weather_windows
    else:
        if bad_weather:
            scene livingroom_morning_bad_weather with Dissolve(.25)
        else:
            scene livingroom_morning with Dissolve(.25)
        if bad_weather:
            if rainstorm:
                show rain behind livingroom_morning_bad_weather
                show livingroom_morning_bad_weather_windows behind rain
            else:
                show livingroom_morning_bad_weather_windows
    return

label outside_scene(trans=True):
    if not outside_ach:
        $ outside_ach = True
        $ update_been_everywhere_achievement()
    # if int(current_time[:2]) in day+night:
    if int(current_time[:2]) in day and (int(current_time[:2]) > 15 and int(current_time[:2]) < 22):
        if trans:
            if bad_weather:
                scene outside_morning_bad_weather_with_car with Dissolve(.25)
            else:
                scene outside_morning_with_car with Dissolve(.25)
        else:
            if bad_weather:
                scene outside_morning_bad_weather_with_car
            else:
                scene outside_morning_with_car
    elif int(current_time[:2]) in night:
        if int(current_time[:2]) < 4 or int(current_time[:2]) >= 22:
            if trans:
                if bad_weather:
                    scene outside_night_bad_weather_with_car with Dissolve(.25)
                else:
                    scene outside_night_with_car with Dissolve(.25)
            else:
                if bad_weather:
                    scene outside_night_bad_weather_with_car
                else:
                    scene outside_night_with_car
        else:
            if trans:
                if bad_weather:
                    scene outside_night_bad_weather with Dissolve(.25)
                else:
                    scene outside_night with Dissolve(.25)
            else:
                if bad_weather:
                    scene outside_night_bad_weather
                else:
                    scene outside_night
    else:
        if trans:
            if bad_weather:
                scene outside_morning_bad_weather with Dissolve(.25)
            else:
                scene outside_morning with Dissolve(.25)
        else:
            if bad_weather:
                scene outside_morning_bad_weather
            else:
                scene outside_morning
    return

label schoolbuilding_scene(trans=True):
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

label school_po_scene(trans=True):
    if not school_principal_office_ach:
        $ school_prinicpal_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene school_principal_office_night with Dissolve(.25)
    else:
        scene school_principal_office_morning with Dissolve(.25)
    return

label upper_hallway_scene(trans=True):
    if not uhl_ach:
        $ uhl_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene upper_hallway_night with Dissolve(.25)
    else:
        scene upper_hallway_morning with Dissolve(.25)
    return

label upper_hallway_bathroom_peek_scene(trans=True,wetshower=False):
    if not uhl_bathroom_ach:
        $ uhl_bathroom_ach = True
        $ update_been_everywhere_achievement()
    if trans:
        if int(current_time[:2]) in night:
            scene upper_hallway_bathroom_night_after_shower_light with Dissolve(.25)
            show juliette_shower_night
        else:
            $ print('showerscene during morning with trans')
            scene upper_hallway_bathroom_morning with Dissolve(.25)
            show juliette_shower
            # with Dissolve(.25)
    else:
        if int(current_time[:2]) in night:
            $ print('showerscene during night')
            scene upper_hallway_bathroom_night_after_shower_light
            show juliette_shower_night
        else:
            $ print('showerscene during morning')
            scene upper_hallway_bathroom_morning
            show juliette_shower
    return

label upper_hallway_bathroom_scene(trans=True,wetshower=False):
    if not uhl_bathroom_ach:
        $ uhl_bathroom_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night and bathroom_light:
        if trans:
            if wetshower:
                scene upper_hallway_bathroom_night_after_shower_light with Dissolve(.25)
            else:
                scene upper_hallway_bathroom_night_light with Dissolve(.25)
        else:
            if wetshower:
                scene upper_hallway_bathroom_night_after_shower_light
            else:
                scene upper_hallway_bathroom_night_light
    elif int(current_time[:2]) in night:
        if trans:
            if wetshower:
                scene upper_hallway_bathroom_night_after_shower with Dissolve(.25)
            else:
                scene upper_hallway_bathroom_night with Dissolve(.25)
        else:
            if wetshower:
                scene upper_hallway_bathroom_night_after_shower
            else:
                scene upper_hallway_bathroom_night
    else:
        if trans:
            if wetshower:
                scene upper_hallway_bathroom_morning_after_shower with Dissolve(.25)
            else:
                scene upper_hallway_bathroom_morning with Dissolve(.25)
        else:
            if wetshower:
                scene upper_hallway_bathroom_morning_after_shower
            else:
                scene upper_hallway_bathroom_morning
    return