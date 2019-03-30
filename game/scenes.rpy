label beach_scene(trans=True):
    if not beach_ach:
        $ beach_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if weather in [1,2]:
            scene beach_night_bw
            if weather == 2:
                show beach_night_bw behind rain
                if trans:
                    with Dissolve(.25)
        else:
            scene beach_night
            if trans:
                with Dissolve(.25)
    else:
        if weather in [1,2]:
            scene beach_morning_bw
            if weather == 2:
                show beach_morning_bw behind rain
                if trans:
                    with Dissolve(.25)
        else:
            scene beach_morning
            if trans:
                with Dissolve(.25)
    return

label fp_entrance_scene(trans=True):
    if not fp_entrance_ach:
        $ fp_entrance_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene fp_en
        if trans:
            with Dissolve(.25)
    else:
        if weather == 1 or weather == 2:
            scene fp_em_bw
        else:
            scene fp_em
        if trans:
            with Dissolve(.25)
    return

label fp_bedroom_fp_scene(trans=True): #this is the starting scene, and the one that repeats every morning (unless there are circumstances altering the morning events)
    if not fp_bedroom_fp_ach:
        $ fp_bedroom_fp_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene fp_bn_fp
        if trans:
            with Dissolve(.25)
    elif int(current_time[:2]) in [7,8,9,10,11] and day_week <= 4 and not morning_out_of_bed and fpmc_r < .75 and not morning_event_done:
        if weather == 1:
            scene fp_bm_fp_bw_wakeup_anne
            if trans:
                with Dissolve(.25)
        elif weather == 2:
            scene fp_bm_fp_bw_wakeup_anne
            if trans:
                with Dissolve(.25)
        else:
            scene fp_bm_fp_wakeup_anne
            if trans:
                with Dissolve(.25)
    elif not morning_out_of_bed and not morning_event_done:
        if weather == 1:
            scene fp_bm_fp_bw_wakeup
            if trans:
                with Dissolve(.25)
        elif weather == 2:
            scene fp_bm_fp_bw_wakeup
            if trans:
                with Dissolve(.25)
        else:
            scene fp_bm_fp_wakeup
            if trans:
                with Dissolve(.25)
    else:
        if weather == 1:
            scene fp_bm_fp_bw
            if trans:
                with Dissolve(.25)
        elif weather == 1:
            scene fp_bm_fp_bw
            if trans:
                with Dissolve(.25)
        else:
            scene fp_bm_fp
            if trans:
                with Dissolve(.25)
    return

label fp_bedroom_fm_scene(trans=True):
    if not fp_bedroom_fm_ach:
        $ fp_bedroom_fm_ach = True
        $ update_been_everywhere_achievement()
    if firstday_talk:
        scene fp_bm_fm_fs_intro with Dissolve(.25)
    else:
        if int(current_time[:2]) in night:
            scene fp_bn_fm_transparent
            if weather == 1:
                show fp_bn_fm_outside behind fp_bn_fm_transparent
            elif weather == 2:
                show rain behind fp_bn_fm_transparent:
                    alpha .25
                show fp_bn_fm_outside behind rain
            else:
                show fp_bn_fm_outside behind fp_bn_fm_transparent
            if trans:
                with Dissolve(.25)
        else:
            if weather == 1:
                scene fp_bm_fm_bw_transparent
                show fp_bm_fm_bw_outside behind fp_bm_fm_bw_transparent
            elif weather == 2:
                scene fp_bm_fm_bw_transparent
                show rain behind fp_bm_fm_bw_transparent
                show fp_bm_fm_bw_outside behind rain
            else:
                scene fp_bm_fm_transparent
                show fp_bm_fm_outside behind fp_bm_fm_transparent
            if trans:
                with Dissolve(.25)
    return

label fp_bedroom_fs_scene(trans=True):
    if not fp_bedroom_fs_ach:
        $ fp_bedroom_fs_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if weather == 1:
            scene fp_bn_fs_transparent
            show fp_bn_fs_outside behind fp_bn_fs_transparent
        elif weather == 2:
            scene fp_bn_fs_bw_transparent
            show rain behind fp_bn_fs_bw_transparent
            show fp_bn_fs_bw_outside behind rain
        else:
            scene fp_bn_fs_transparent
            show fp_bn_fs_outside behind fp_bn_fs_transparent
        if trans:
            with Dissolve(.25)
    else:
        if weather == 1:
            scene fp_bm_fs_bw_transparent
            show fp_bm_fs_bw_outside behind fp_bm_fs_bw_transparent
        elif weather == 2:
            scene fp_bm_fs_bw_transparent
            show rain behind fp_bm_fs_bw_transparent
            show fp_bm_fs_bw_outside behind rain
        else:
            scene fp_bm_fs_transparent
            show fp_bm_fs_outside behind fp_bm_fs_transparent
        if trans:
            with Dissolve(.25)
    return

label fs_intro_scene(trans=True):
    if daycount == int(0):
        scene fs_bedroom_morning_intro
        show juliette_on_bed_intro:
            zoom .6
            xalign .5
            yalign 1.0
            xoffset -100
            yoffset -65
        if trans:
            with Dissolve(.25)
    return

label fp_garage_scene(trans=True): #updated
    if not fp_garage_ach:
        $ fp_garage_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if weather == 1:
            scene fp_gn_transparent
            show fp_gn_outside behind fp_gn_transparent
        elif weather == 2:
            scene fp_gn_transparent
            show rain behind fp_gn_transparent
            show fp_gn_outside behind rain
        else:
            scene fp_gn_transparent
            show fp_gn_outside behind fp_gn_transparent
        if trans:
            with Dissolve(.25)
    else:
        if weather == 1:
            scene fp_gm_bw_transparent
            show fp_gm_bw_outside behind fp_gm_bw_transparent
        elif weather == 2:
            scene fp_gm_bw_transparent
            show rain behind fp_gm_bw_transparent
            show fp_gm_bw_outside behind rain
        else:
            scene fp_gm_transparent
            show fp_gm_outside behind fp_gm_transparent
        if trans:
            with Dissolve(.25)
    return

label fp_garage_fb_scene(trans=True):
    if int(current_time[:2]) in night:
        if trans:
            scene fp_garage_fb_night with Dissolve(.25)
        else:
            scene fp_garage_fb_night
    else:
        if trans:
            scene fp_garage_fb_morning with Dissolve(.25)
        else:
            scene fp_garage_fb_morning
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

label fp_kitchen_scene(trans=True): #updated
    if not fp_kitchen_ach:
        $ fp_kitchen_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene fp_kn_transparent
        if weather == 1 or weather == 3:
            show fp_kn_outside behind fp_kn_transparent
        elif weather == 2:
            show rain behind fp_kn_transparent:
                alpha .25
            show fp_kn_outside behind rain
        else:
            show fp_kn_outside behind fp_kn_transparent
        if trans:
            with Dissolve(.25)
    else:
        if weather == 1:
            scene fp_km_bw_transparent
            show fp_km_bw_outside behind fp_km_bw_transparent
        elif weather == 2:
            scene fp_km_bw_transparent
            show rain behind fp_km_bw_transparent
            show fp_km_bw_outside behind rain
        else:
            scene fp_km_transparent
            show fp_km_outside behind fp_km_transparent
        if trans:
            with Dissolve(.25)
    return

label fp_livingroom_scene(trans=True): #updated
    if not fp_livingroom_ach:
        $ fp_livingroom_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if weather == 1:
            scene fp_ln_transparent
            show fp_ln_outside behind fp_ln_transparent
        elif weather == 2:
            scene fp_ln_transparent
            show rain behind fp_ln_transparent:
                alpha .25
            show fp_ln_outside behind rain
        else:
            scene fp_ln_transparent
            show fp_ln_outside behind fp_ln_transparent
        if trans:
            with Dissolve(.25)
    else:
        if weather == 1:
            scene fp_lm_bw_transparent
            show fp_lm_bw_outside behind fp_lm_bw_transparent
        elif weather == 2:
            scene fp_lm_bw_transparent
            show rain behind fp_lm_bw_transparent:
                alpha .25
            show fp_lm_bw_outside behind rain
        else:
            scene fp_lm_transparent
            show fp_lm_outside behind fp_lm_transparent
        if trans:
            with Dissolve(.25)
    return

label fp_outside_scene(trans=True):
    if not fp_outside_ach:
        $ fp_outside_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if weather == 1:
            scene fp_on
            if trans:
                with Dissolve(.25)
        if weather == 2:
            scene fp_on
            # if trans:
            #     show rain with Dissolve(.25):
            #         alpha .25
            # else:
            #     show rain
    else:
        if weather == 1:
            scene fp_om_bw
        elif weather == 2:
            scene fp_om_bw
            show rain
        else:
            scene fp_om
        if trans:
            with Dissolve(.25)
    return

label fp_patio_scene(trans=True):
    if not fp_patio_ach:
        $ fp_patio_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if weather == 1 or weather == 3:
            scene fp_pn_transparent
            show fp_pn_outside behind fp_pn_transparent
        elif weather == 2:
            scene fp_pn_transparent
            show rain behind fp_pn_transparent:
                alpha .25
            show fp_pn_outside behind rain
    else:
        if weather == 1:
            scene fp_pm_bw_transparent
            show fp_pm_bw_outside behind fp_pm_bw_transparent
        elif weather == 2:
            scene fp_pm_bw_transparent
            show rain behind fp_pm_bw_transparent
            show fp_pm_bw_outside behind rain
        else:
            scene fp_pm_transparent
            show fp_pm_outside behind fp_pm_transparent
    if trans:
        with Dissolve(.25)
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
        scene fp_tsn with Dissolve(.25)
    else:
        scene fp_tsm with Dissolve(.25)
    return

label fp_upstairs_scene(trans=True):
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        scene fp_un with Dissolve(.25)
    else:
        scene fp_um with Dissolve(.25)
    return

label upstairs_closerdoor_scene(trans=True):
    if not fp_topofstairs_ach:
        $ fp_topofstairs_ach = True
        $ update_been_everywhere_achievement()
    scene fp_intro_cd with Dissolve(.25)
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
                scene fp_ufbn_toilet #scene ufbn_after_shower_light with Dissolve(.25)
            else:
                scene fp_ufbn_toilet #scene ufbn_light with Dissolve(.25)
            with Dissolve(.25)
        else:
            if wetshower:
                scene fp_ufbn_toilet #ufbn_after_shower_light
            else:
                scene fp_ufbn#scene ufbn_light
    elif int(current_time[:2]) in night:
        if trans:
            if wetshower:
                scene fp_ufbn_toilet #ufbn_after_shower with Dissolve(.25)
            else:
                scene fp_ufbn_toilet #ufbn with Dissolve(.25)
            with Dissolve(.25)
        else:
            if wetshower:
                scene fp_ufbn_toilet #ufbn_after_shower
            else:
                scene fp_ufbn_toilet #ufbn
    else:
        if trans:
            if wetshower:
                scene fp_ufbm_toilet #upper_hallway_bathroom_morning_after_shower with Dissolve(.25)
            else:
                scene fp_ufbm_toilet #with Dissolve(.25)
            with Dissolve(.25)
        else:
            if wetshower:
                scene fp_ufbm_toilet #upper_hallway_bathroom_morning_after_shower
            else:
                scene fp_ufbm_toilet
    return

label fp_pool_scene(trans=True):
    if not fp_pool_ach:
        $ fp_pool_ach = True
        $ update_been_everywhere_achievement()
    if firstday_talk:
        scene fp_pm_fs_after_intro_talk with Dissolve(.25)
    else:
        if int(current_time[:2]) in night:
            if trans:
                scene fp_pn with Dissolve(.25)
            else:
                scene fp_pn
        else:
            if trans:
                scene fp_pm with Dissolve(.25)
            else:
                scene fp_pm
    return

label fp_ufb_scene(trans=True,wetshower=False):
    if not fp_ufb_ach:
        $ fp_ufb_ach = True
        $ update_been_everywhere_achievement()
    if int(current_time[:2]) in night:
        if not bathroom_light:
            if weather == 1 or weather == 3:
                scene fp_ufbn_transparent
                show fp_ufbn_outside behind fp_ufbn_transparent
            elif weather == 2:
                scene fp_ufbn_transparent
                show rain behind fp_ufbn_transparent
                show fp_ufbn_outside behind rain
            if trans:
                with Dissolve(.25)
    else:
        if weather == 1:
            scene fp_ufbm_bw_transparent
            show fp_ufbm_bw_outside behind fp_ufbm_bw_transparent
        elif weather == 2:
            scene fp_ufbm_bw_transparent
            show rain behind fp_ufbm_bw_transparent
            show fp_ufbm_bw_outside behind rain
        else:
            scene fp_ufbm_transparent
            show fp_ufbm_outside behind fp_ufbm_transparent
        if trans:
            with Dissolve(.25)

    # if int(current_time[:2]) in night and bathroom_light:
    #     if trans:
    #         if wetshower:
    #             scene fp_ufbn_after_shower_light with Dissolve(.25)
    #         else:
    #             scene fp_ufbn_light with Dissolve(.25)
    #     else:
    #         if wetshower:
    #             scene fp_ufbn_after_shower_light
    #         else:
    #             scene fp_ufbn_light
    # elif int(current_time[:2]) in night:
    #     if trans:
    #         if wetshower:
    #             scene fp_ufbn_after_shower with Dissolve(.25)
    #         else:
    #             scene fp_ufbn with Dissolve(.25)
    #     else:
    #         if wetshower:
    #             scene fp_ufbn_after_shower
    #         else:
    #             scene fp_ufbn
    # else:
    #     if trans:
    #         if wetshower:
    #             scene fp_ufbm_transparent
    #             show fp_ufbm_outside behind fp_ufbm_transparent #upper_hallway_bathroom_morning_after_shower with Dissolve(.25)
    #             with Dissolve(.25)
    #         else:
    #             if weather == 1 or weather == 2:
    #                 scene fp_ufbm_bw_transparent
    #                 if weather == 1:
    #                     show fp_ufbm_outside_rain behind fp_ufbm_bw_transparent
    #                 elif weather == 2:
    #                     show rain behind fp_ufbm_bw_transparent
    #                     show fp_ufbm_outside_rain behind rain
    #                 with Dissolve(.25)
    #             else:
    #                 if not fp_bath_lock and not leave_lock:
    #                     # scene ufbm_marten_doorway_door_closed
    #                     scene fp_ufbm_transparent
    #                     show fp_ufbm_outside behind fp_ufbm_transparent
    #                     with Dissolve(.25)
    #                 else:
    #                     scene fp_ufbm_transparent
    #                     show fp_ufbm_outside behind fp_ufbm_transparent
    #                     with Dissolve(.25)

    #     else:
    #         if wetshower:
    #             scene fp_ufbm_transparent
    #             show fp_ufbm_outside behind fp_ufbm_transparent #upper_hallway_bathroom_morning_after_shower
    #         else:
    #             if weather == 1 or weather == 2:
    #                 scene fp_ufbm_bw_transparent
    #                 if weather == 1:
    #                     show fp_ufbm_outside_rain behind fp_ufbm_bw_transparent
    #                 elif weather == 2:
    #                     show rain behind fp_ufbm_bw_transparent
    #                     show fp_ufbm_outside_rain behind rain
    #             else:
    #                 if not fp_bath_lock and not leave_lock:
    #                     # scene ufbm_marten_doorway_door_closed
    #                     scene fp_ufbm_transparent
    #                     show fp_ufbm_outside behind fp_ufbm_transparent
    #                 else:
    #                     scene fp_ufbm_transparent
    #                     show fp_ufbm_outside behind fp_ufbm_transparent
    return
