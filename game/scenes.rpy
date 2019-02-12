label beach_scene(trans=True):
    if not beach_ach:
        $ beach_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene beach_night with Dissolve(.25)
    else:
        scene beach_morning with Dissolve(.25)
    return

label fp_entrance_scene(trans=True):
    if not fp_entrance_ach:
        $ fp_entrance_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene fp_en with Dissolve(.25)
    else:
        scene fp_em with Dissolve(.25)
    return

label fp_bedroom_fp_scene(trans=True): #this is the starting scene, and the one that repeats every morning (unless there are circumstances altering the morning events)
    if not fp_bedroom_fp_ach:
        $ fp_bedroom_fp_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene fpbn
    elif int(current_time[:2]) in [7,8,9,10,11] and day_week <= 4 and not morning_out_of_bed and fpmc_r < .75 and not morning_event_done:
        scene fpbm_wakeup_anne
    elif not morning_out_of_bed and not morning_event_done:
        scene fpbm_wakeup
    else:
        scene fpbm_empty
    return

label fp_bedroom_fm_scene(trans=True):
    if not fp_bedroom_fm_ach:
        $ fp_bedroom_fm_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if trans:
            scene fpbn_fm with Dissolve(.25)
        else:
            scene fpbn_fm
    else:
        if trans:
            scene fpbm_fm with Dissolve(.25)
        else:
            scene fpbm_fm
    return

label fp_bedroom_fs_scene(trans=True):
    if not fp_bedroom_fs_ach:
        $ fp_bedroom_fs_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if trans:
            scene fsbn with Dissolve(.25)
        else:
            scene fsbn
    else:
        if trans:
            scene fsbm with Dissolve(.25)
        else:
            scene fsbm
    return

label fs_intro_scene():
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

label fp_garage_scene(trans=True):
    if not fp_garage_ach:
        $ fp_garage_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if trans:
            scene fp_gn with Dissolve(.25)
        else:
            scene fp_gn
    else:
        if trans:
            scene fp_gm with Dissolve(.25)
        else:
            scene fp_gm
    return

label fp_garage_fb_scene(trans=True):
    if int(current_time[:2]) in night:
        if trans:
            scene bike_repair_night with Dissolve(.25)
        else:
            scene bike_repair_night
    else:
        if trans:
            scene bike_repair_morning with Dissolve(.25)
        else:
            scene bike_repair_morning
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

label fp_kitchen_spill_scene(trans=True):
    if not fp_kitchen_ach:
        $ fp_kitchen_ach = True
        $ update_been_everywhere_achievement()
    if not fm_seen:
        if trans:
            scene fp_kitchen_spill with Dissolve(.25)
        else:
            scene fp_kitchen_spill
    return

label fp_kitchen_scene(trans=True):
    if not fp_kitchen_ach:
        $ fp_kitchen_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if trans:
            scene fpkn with Dissolve(.25)
        else:
            scene fpkn
    else:
        if trans:
            scene fpkm with Dissolve(.25)
        else:
            scene fpkm
    return

label fp_livingroom_scene(trans=True):
    if not fp_livingroom_ach:
        $ fp_livingroom_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if weather == 1 or weather == 2:
            scene fp_ln_bad_weather with Dissolve(.25)
        else:
            scene fp_ln with Dissolve(.25)
        # if weather == 1:
        #     show fp_ln_bad_weather_windows
        # elif weather == 2:
        #     show rain behind livingroom_night_bad_weather
        #     show livingroom_night_bad_weather_windows behind rain
    else:
        if weather == 1 or weather == 2:
            scene fp_lm_bad_weather with Dissolve(.25)
        else:
            scene fp_lm with Dissolve(.25)
        # if weather == 1:
        #     show livingroom_morning_bad_weather_windows
        # elif weather == 2:
        #     show rain behind livingroom_morning_bad_weather
        #     show livingroom_morning_bad_weather_windows behind rain
    return

label fp_outside_scene(trans=True):
    if not fp_outside_ach:
        $ fp_outside_ach = True
        $ update_been_everywhere_achievement()
    # if int(current_time[:2]) in day+night:
    if int(current_time[:2]) in day and (int(current_time[:2]) > 15 and int(current_time[:2]) < 22):
        if trans:
            if weather == 1:
                scene outside_morning_bad_weather_with_car with Dissolve(.25)
            else:
                scene outside_morning_with_car with Dissolve(.25)
        else:
            if weather == 1:
                scene outside_morning_bad_weather_with_car
            else:
                scene outside_morning_with_car
    elif int(current_time[:2]) in night:
        if int(current_time[:2]) < 4 or int(current_time[:2]) >= 22:
            if trans:
                if weather == 1:
                    scene outside_night_bad_weather_with_car with Dissolve(.25)
                else:
                    scene outside_night_with_car with Dissolve(.25)
            else:
                if weather == 1:
                    scene outside_night_bad_weather_with_car
                else:
                    scene outside_night_with_car
        else:
            if trans:
                if weather == 1:
                    scene outside_night_bad_weather with Dissolve(.25)
                else:
                    scene outside_night with Dissolve(.25)
            else:
                if weather == 1:
                    scene outside_night_bad_weather
                else:
                    scene outside_night
    else:
        if trans:
            if weather == 1:
                scene outside_morning_bad_weather with Dissolve(.25)
            else:
                scene fp_outside with Dissolve(.25)
        else:
            if weather == 1:
                scene outside_morning_bad_weather
            else:
                scene fp_outside
    return

label schoolbuilding_scene(trans=True):
    if not fp_school_outside_ach:
        $ fp_school_outside_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if weather == 2:
            scene school_outside_night
            show rain
            with Dissolve(.25)
        else:
            scene school_outside_night with Dissolve(.25)
    else:
        if weather == 2:
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

label fp_topofstairs_scene(trans=True):
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene fptsn with Dissolve(.25)
    else:
        scene fptsm with Dissolve(.25)
    return

label fp_upstairs_scene(trans=True):
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene upstairs_night with Dissolve(.25)
    else:
        scene upstairs_morning with Dissolve(.25)
    return

label upstairs_closerdoor_scene(trans=True):
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    scene upstairs_closerdoor with Dissolve(.25)
    return

label upper_hallway_bathroom_peek_scene(trans=True,wetshower=False):
    if not fp_ufb_ach:
        $ fp_ufb_ach = True
        $ update_been_everywhere_achievement()
    if trans:
        if int(current_time[:2]) in night:
            scene ufbn_after_shower_light with Dissolve(.25)
            show juliette_shower_night
        else:
            # $ print('showerscene during morning with trans')
            scene upper_hallway_bathroom_morning with Dissolve(.25)
            show juliette_shower
            # with Dissolve(.25)
    else:
        if int(current_time[:2]) in night:
            # $ print('showerscene during night')
            scene ufbn_after_shower_light
            show juliette_shower_night
        else:
            # $ print('showerscene during morning')
            scene upper_hallway_bathroom_morning
            show juliette_shower
    return

label ufbm_toilet_scene(trans=True):
    if int(current_time[:2]) in night and bathroom_light:
        if trans:
            if wetshower:
                scene ufbn_toilet #scene ufbn_after_shower_light with Dissolve(.25)
            else:
                scene ufbn_toilet #scene ufbn_light with Dissolve(.25)
            with Dissolve(.25)
        else:
            if wetshower:
                scene ufbn_toilet #ufbn_after_shower_light
            else:
                scene ufbn#scene ufbn_light
    elif int(current_time[:2]) in night:
        if trans:
            if wetshower:
                scene ufbn_toilet #ufbn_after_shower with Dissolve(.25)
            else:
                scene ufbn_toilet #ufbn with Dissolve(.25)
            with Dissolve(.25)
        else:
            if wetshower:
                scene ufbn_toilet #ufbn_after_shower
            else:
                scene ufbn_toilet #ufbn
    else:
        if trans:
            if wetshower:
                scene ufbm_toilet #upper_hallway_bathroom_morning_after_shower with Dissolve(.25)
            else:
                scene ufbm_toilet #with Dissolve(.25)
            with Dissolve(.25)
        else:
            if wetshower:
                scene ufbm_toilet #upper_hallway_bathroom_morning_after_shower
            else:
                scene ufbm_toilet
    return


label fp_ufb_scene(trans=True,wetshower=False):
    if not fp_ufb_ach:
        $ fp_ufb_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night and bathroom_light:
        if trans:
            if wetshower:
                scene ufbn_after_shower_light with Dissolve(.25)
            else:
                scene ufbn_light with Dissolve(.25)
        else:
            if wetshower:
                scene ufbn_after_shower_light
            else:
                scene ufbn_light
    elif int(current_time[:2]) in night:
        if trans:
            if wetshower:
                scene ufbn_after_shower with Dissolve(.25)
            else:
                scene ufbn with Dissolve(.25)
        else:
            if wetshower:
                scene ufbn_after_shower
            else:
                scene ufbn
    else:
        if trans:
            if wetshower:
                scene ufbm_transparent_background
                show ufbm_outside behind ufbm_transparent_background #upper_hallway_bathroom_morning_after_shower with Dissolve(.25)
                with Dissolve(.25)
            else:
                if weather == 1 or weather == 2:
                    scene ufbm_transparent_background_rain
                    if weather == 1:
                        show ufbm_outside_rain behind ufbm_transparent_background_rain
                    elif weather == 2:
                        show rain behind ufbm_transparent_background_rain
                        show ufbm_outside_rain behind rain
                    with Dissolve(.25)
                else:
                    if not fp_bath_lock and not leave_lock:
                        # scene ufbm_marten_doorway_door_closed
                        scene ufbm_transparent_background
                        show ufbm_outside behind ufbm_transparent_background
                        with Dissolve(.25)
                    else:
                        scene ufbm_transparent_background
                        show ufbm_outside behind ufbm_transparent_background
                        with Dissolve(.25)

        else:
            if wetshower:
                scene ufbm_transparent_background
                show ufbm_outside behind ufbm_transparent_background #upper_hallway_bathroom_morning_after_shower
            else:
                if weather == 1 or weather == 2:
                    scene ufbm_transparent_background_rain
                    if weather == 1:
                        show ufbm_outside_rain behind ufbm_transparent_background_rain
                    elif weather == 2:
                        show rain behind ufbm_transparent_background_rain
                        show ufbm_outside_rain behind rain
                else:
                    if not fp_bath_lock and not leave_lock:
                        # scene ufbm_marten_doorway_door_closed
                        scene ufbm_transparent_background
                        show ufbm_outside behind ufbm_transparent_background
                    else:
                        scene ufbm_transparent_background
                        show ufbm_outside behind ufbm_transparent_background
    return
