label night_events():
    label sleep_the_night(stn_called=False):
        if stn_called or stn_cfs:
            $ stn_called = stn_cfs = False
            if int(current_hour[:2]) not in night:
                menu:
                    "Sleep the day away":
                        call sleeping_day_away(True)
                    "Stay up":
                        call fp_bedroom_loc(True)
            else:
                menu:
                    "Go to sleep":
                        call sleeping(True)
                    "Stay up a bit longer":
                        call fp_bedroom_loc(True)
            # return
        # else:
        #     return


    label end_of_day(end_called=False):
        if end_called or end_cfs:
            $ end_called = end_cfs = False
            "This ends the day"
            hide fs_standing
            hide fm_standing
            hide nk_standing
            with dissolve
            $ nh = format(int(night[renpy.random.randint(0,(len(night)-1))]),"02d")
            $ nm = format(renpy.random.randint(00,59),"02d")
            call settime(nh,nm)
            $ first_day = False
            if int(nh) in xrange(2,6,1):
                $ overslept = True
            if int(current_hour[:2]) in xrange(0,6,1):
                $ day_week = 0 if day_week == 6 else day_week+1
                if current_month_day == months_days[current_month][1]:
                    $ current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                    $ current_month_text = months_days[current_month][0]
                    $ current_month_day = 1
                else:
                    $ current_month_day += 1
                    $ day_ahead = True
            call fp_bedroom_scene
            call sleep_the_night(True)
            # return
        # else:
        #     return

    label sleeping(sle_called=False):
        if sle_called:
            $ sle_called = False
            if not day_ahead:
                $ current_day_of_the_week_3 = day_week
                $ day_week = 0 if day_week == 6 else day_week+1
                $ current_day_of_the_week_1 = day_week
                $ thishappened_1 = "if"
                if current_month_day == months_days[current_month][1]:
                    $ current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                    $ current_month_text = months_days[current_month][0]
                    $ current_month_day = 1
                else:
                    $ current_month_day += 1
                    $ current_day_of_the_week_2 = day_week
                    $ thishappened_2 = "else"
            $ after_sleep = True
            $ day_ahead = False
            jump day_start
            # return
        # else:
            # return

    label sleeping_day_away(sld_called=False):
        if sld_called:
            $ sld_called = False
            call settime(22,False)
            # call fp_bedroom_scene
            call fp_bedroom_loc(True)
            # return
        # else:
        #     return