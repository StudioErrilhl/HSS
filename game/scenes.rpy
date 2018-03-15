label beach_scene(trans=True):
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
    if int(current_time[:2]) in hours:
        if not backpack_carry and not carry_phone:
            if trans:
                scene fp_bedroom_night_glow_phone_backpack with Dissolve(.25)
            else:
                scene fp_bedroom_night_glow_phone_backpack
        elif not backpack_carry and carry_phone:
            if trans:
                scene fp_bedroom_night_glow_backpack with Dissolve(.25)
            else:
                scene fp_bedroom_night_glow_backpack
        elif backpack_carry and not carry_phone:
            if trans:
                scene fp_bedroom_night_glow_phone with Dissolve(.25)
            else:
                scene fp_bedroom_night_glow_phone
        else:
            if trans:
                scene fp_bedroom_night_glow with Dissolve(.25)
            else:
                scene fp_bedroom_night_glow
    elif int(current_time[:2]) in night:
        if not backpack_carry and not carry_phone:
            if trans:
                scene fp_bedroom_night_phone_backpack with Dissolve(.25)
            else:
                scene fp_bedroom_night_phone_backpack
        elif not backpack_carry and carry_phone:
            if trans:
                scene fp_bedroom_night_backpack with Dissolve(.25)
            else:
                scene fp_bedroom_night_backpack
        elif backpack_carry and not carry_phone:
            if trans:
                scene fp_bedroom_night_phone with Dissolve(.25)
            else:
                scene fp_bedroom_night_phone
        else:
            if trans:
                scene fp_bedroom_night with Dissolve(.25)
            else:
                scene fp_bedroom_night
    else:
        if not backpack_carry and not carry_phone:
            if trans:
                scene fp_bedroom_morning_phone_backpack with Dissolve(.25)
            else:
                scene fp_bedroom_morning_phone_backpack
        elif not backpack_carry and carry_phone:
            if trans:
                scene fp_bedroom_morning_backpack with Dissolve(.25)
            else:
                scene fp_bedroom_morning_backpack
        elif backpack_carry and not carry_phone:
            if trans:
                scene fp_bedroom_morning_phone with Dissolve(.25)
            else:
                scene fp_bedroom_morning_phone
        else:
            if trans:
                scene fp_bedroom_morning with Dissolve(.25)
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
    if day_week == 0 and current_month == 4:
        scene fs_intro_scene with Dissolve(.25)
    else:
        scene fs_intro_scene with Dissolve(.25)
    return

label garage_scene(trans=True):
    if not garage_ach:
        $ garage_ach = True
        $ update_been_everywhere_achievement()
    if mc_f:
        if int(current_time[:2]) in night:
            if trans:
                scene honda_cx_500_finished_night with Dissolve(.25)
            else:
                scene honda_cx_500_finished_night
        else:
            if trans:
                scene honda_cx_500_finished_morning with Dissolve(.25)
            else:
                scene honda_cx_500_finished_morning
    else:
        if int(current_time[:2]) in night:
            if trans:
                scene honda_cx_500_build_night with Dissolve(.25)
            else:
                scene honda_cx_500_build_night
        else:
            if trans:
                scene honda_cx_500_build_morning with Dissolve(.25)
            else:
                scene honda_cx_500_build_morning
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
        scene livingroom_night with Dissolve(.25)
    else:
        scene livingroom_morning with Dissolve(.25)
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

label upper_hallway_bathroom_peek_scene(trans=True):
    if not uhl_bathroom_ach:
        $ uhl_bathroom_ach = True
        $ update_been_everywhere_achievement()
    if trans:
        scene upper_hallway_bathroom_morning
        show upper_hallway_bathroom_juliette_shower_bubbles
        with Dissolve(.25)
    else:
        scene upper_hallway_bathroom_morning
        show upper_hallway_bathroom_juliette_shower_bubbles
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