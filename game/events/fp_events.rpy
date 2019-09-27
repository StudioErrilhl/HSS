label fp_find_keys(trans=True):
    if not carry_carkeys:
        fp "Crap! I don't have the keys. I'll need to find them..."
        $ find_keys = True
        $ set_hint("You need to find the carkeys to drive the car")
        call change_loc(current_location,prev_loc=current_location) from _call_change_loc_104

label fp_aquire_couch(trans=True):
    $ conditions.addcondition("Yes (cost: 250,-)","fp_money > 250")
    if fp_money > 250:
        $ tempText = "Do you want to buy a couch?"
    else:
        $ tempText = "Do you want to buy a couch? (You need 250 cash or more to purchase)"
    menu:
        "[tempText]"
        "No":
            $ fp_couch_aquired = False
            call change_loc(current_location,prev_loc=current_location) from _call_change_loc_92
        "Yes (cost: 250,-)":
            $ fp_couch_aquired = True
            $ statschangenotify('fp_money',-250)
            call change_loc(current_location,prev_loc=current_location) from _call_change_loc_91

label fp_aquire_art(trans=True):
    $ tempcount = sum(1 for i in wallart.values() if i)
    if tempcount >= 2:
        $ conditions.addcondition("Buy","not all(wallart.values())")
        menu:
            "Do you want to swap out the art you own, or buy more art?"
            "Neither":
                call change_loc(current_location,prev_loc=current_location) from _call_change_loc_105
            "Buy":
                jump buyart
            "Swap":
                jump swapmenu

    menu swapmenu:
        "Swap out the wallart"
        "Swap with Parking lot wallart" if not active_wallart == 'parkinglot' and wallart['parkinglot']:
            $ active_wallart = 'parkinglot'
            call change_loc(current_location,prev_loc=current_location) from _call_change_loc_106
        "Swap with Ferrari wallart" if not active_wallart == 'ferrari' and wallart['ferrari']:
            $ active_wallart = 'ferrari'
            call change_loc(current_location,prev_loc=current_location) from _call_change_loc_107
        "Swap with Roadtrip wallart" if not active_wallart == 'roadtrip' and wallart['roadtrip']:
            $ active_wallart = 'roadtrip'
            call change_loc(current_location,prev_loc=current_location) from _call_change_loc_108
        "Swap with Sin City wallart" if not active_wallart == 'sincity' and wallart['sincity']:
            $ active_wallart = 'sincity'
            call change_loc(current_location,prev_loc=current_location) from _call_change_loc_109
        "Swap with Peekaboo wallart" if not active_wallart == 'peekaboo' and wallart['peekaboo']:
            $ active_wallart = 'peekaboo'
            call change_loc(current_location,prev_loc=current_location) from _call_change_loc_110

    $ conditions.addcondition("Yes","fp_money > 75")
    $ conditions.addcondition("Buy Parking lot wallart","not wallart['parkinglot']")
    $ conditions.addcondition("Buy Ferrari wallart","not wallart['ferrari']")
    $ conditions.addcondition("Buy Roadtrip wallart","not wallart['roadtrip']")
    $ conditions.addcondition("Buy Sin City wallart","not wallart['sincity']")
    $ conditions.addcondition("Buy Peekaboo wallart","not wallart['peekaboo']")
    menu buyart:
        "Do you want to buy some art?"
        "No":
            call change_loc(current_location,prev_loc=current_location) from _call_change_loc_111
        "Yes":
            menu:
                "Buy Parking lot wallart" (badge='wallart_parkinglot_badge'):
                    $ wallart['parkinglot'] = True
                    $ active_wallart = 'parkinglot'
                    $ statschangenotify('fp_money',-75)
                    $ update_all_wallart_achievement()
                    call change_loc(current_location,prev_loc=current_location) from _call_change_loc_112
                "Buy Ferrari wallart" (badge='wallart_ferrari_badge'):
                    $ wallart['ferrari'] = True
                    $ active_wallart = 'ferrari'
                    $ statschangenotify('fp_money',-75)
                    $ update_all_wallart_achievement()
                    call change_loc(current_location,prev_loc=current_location) from _call_change_loc_113
                "Buy Roadtrip wallart" (badge='wallart_roadtrip_badge'):
                    $ wallart['roadtrip'] = True
                    $ active_wallart = 'roadtrip'
                    $ statschangenotify('fp_money',-75)
                    $ update_all_wallart_achievement()
                    call change_loc(current_location,prev_loc=current_location) from _call_change_loc_114
                "Buy Sin City wallart" (badge='wallart_sincity_badge'):
                    $ wallart['sincity'] = True
                    $ active_wallart = 'sincity'
                    $ statschangenotify('fp_money',-75)
                    $ update_all_wallart_achievement()
                    call change_loc(current_location,prev_loc=current_location) from _call_change_loc_115
                "Buy Peekaboo wallart" (badge='wallart_peekaboo_badge'):
                    $ wallart['peekaboo'] = True
                    $ active_wallart = 'peekaboo'
                    $ statschangenotify('fp_money',-75)
                    $ update_all_wallart_achievement()
                    call change_loc(current_location,prev_loc=current_location) from _call_change_loc_116
                "No thanks, not right now":
                    call change_loc(current_location,prev_loc=current_location) from _call_change_loc_117