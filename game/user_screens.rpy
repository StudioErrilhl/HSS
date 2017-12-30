style tooltip_hover:
    yalign 0.5
    xmaximum 600

style red_color:
    color "#f00"

screen empty()

screen choice(items):
    style_prefix "choice"

    vbox:
        yalign .8
        spacing 20
        for caption, action, chosen in items:
            if action:
                if conditions.check(caption):
                    button:
                        style "choice_button"
                        text conditions.text(caption) style "choice_button_disabled"
                else:
                    button:
                        action action
                        style "choice_button"
                        text caption style "choice_button"                 
            else:                           
                text caption style "choice_button"
init -2:
    $ config.narrator_menu = True

    style choice_vbox is vbox
    style choice_button is button
    style choice_button_text is button_text
    style choice_button_disabled_text is button_text

    style choice_vbox:
        xalign 0.5
        ypos 405
        yanchor 0.5
        spacing gui.choice_spacing

    style choice_button is default:
        properties gui.button_properties("choice_button")

    style choice_button_text is default:
        properties gui.button_text_properties("choice_button")

    style choice_button_disabled is default:
        properties gui.button_properties("choice_button_disabled")

    style choice_button_disabled is default:
        properties gui.button_text_properties("choice_button_disabled")
        color "#aaaaaa"        
    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)



screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:
                        if conditions.check(caption):                            
                            button:
                                style "nvl_menu_choice_button"
                                text conditions.text(caption) style "nvl_menu_choice"
                        else:
                            button:
                                style "nvl_menu_choice_button"
                                action action

                                text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Main Menu") action MainMenu()
        textbutton _("Save") action ShowMenu("save")
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("History") action ShowMenu("history")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Changelog") action [Show ("changelog")]        

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        if renpy.variant("pc") and not main_menu:
            textbutton _("Help") action ShowMenu("help")
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

screen main_menu():
    tag menu

    if main_menu:
        imagemap:
            ground "gui/menu.png"
            hover "gui/menu_hover.png"

            hotspot (44, 100, 355, 110) action Start()
            hotspot (44, 210, 378, 110) action ShowMenu("load")
            hotspot (44, 320, 392, 110) action ShowMenu("preferences")
            hotspot (44, 430, 400, 110) action ShowMenu("about")
            hotspot (44, 540, 396, 110) action ShowMenu("changelog")
            hotspot (44, 650, 381, 110) 
            hotspot (44, 760, 356, 110) action ShowMenu("help")
            hotspot (44, 870, 324, 110) action Quit(confirm=not main_menu)

    style_prefix "main_menu"

    frame:
        pass

    if gui.show_name:
        vbox:
            text "[config.name!t]":
                style "main_menu_title"

    vbox:
        xalign 1.0
        yalign 1.0
        text "[config.version]":
            style "main_menu_version"
            xpos -830
            ypos 65

        imagebutton:
            idle "images/patreon_idle.png"
            hover "images/patreon_hover.png"
            action OpenURL("https://www.patreon.com/errilhl")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        text_style "white_color"
        action Return()

    label title

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gm_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    color "#ffffff"
    size 40

style gm_label_text:
    color "#ffffff"
    yalign 0.25
    xoffset -40

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0

style white_color:
    color "#ffffff"

screen notify(message,status=False):

    if status:
        $ message = message
    elif isinstance(message, ( set, list, tuple )):
        $ status = message[1]
        $ message = message[0]
    elif not isinstance(message, basestring ):
        $ message = "{0}:{1}".format( type( message ), repr( message ) )
    else:
        $ message = message

    zorder 100
    style_prefix "notify"

    timer 3.25 action Hide('notify')

    if status:
        frame at notify_appear:
            text "[message!tq]" style "red_color"
    else:
        frame at notify_appear:
            text "[message!tq]"

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

screen ingame_menu_display(day_week=day_week,month=current_month_text,month_day=current_month_day,current_hour=current_hour):
    zorder 300
    default tt = Tooltip("")
    default x = 500
    default y = 400
    # Get mouse coords:
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    vbox xalign 0 yalign 0:
        imagebutton auto "images/stats_%s.png" focus_mask True action Show('stat_screen'):
            hovered tt.Action("Here you'll find all the stats for all the characters in the game. Some characters doesn't have a lot of stats currently, this may change with the coming updates")
        add "images/stats_overlay.png":
            ypos -128
            if int(current_hour[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5

    vbox xalign .99 yalign .99: #inventory / backpack
        imagebutton auto "images/backpack_%s.png":
            xalign 0.8
            ypos 100
            focus_mask True 
            action [Show("inventory_screen")]
            hovered tt.Action("Here you'll be able to see what you have in your backpack")
        add "images/backpack_overlay.png":
            ypos -16
            if int(current_hour[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5

    frame: #calendar-display
        xpos 1810
        xpadding 0
        ypadding 0
        background Image("images/calendar.png")
        vbox: #month and date and dayname
            xsize 100
            xalign .5
            $ current_day = week_days[day_week]
            $ current_month = month
            $ current_month_day = month_day
            text "[current_month]":
                xalign .5
                color "#ffffff"
                size 20
            text "[current_month_day]":
                xalign .5
                ypos -5
                size 60
            if bad_weather and rainstorm and int(current_hour[:2]) in night:
                add "images/night_rain_icon.png":
                    xalign .5
                    ypos -20                
            elif bad_weather and rainstorm:
                add "images/morning_rain_icon.png":
                    xalign .5
                    ypos -20                
            elif int(current_hour[:2]) in night:
                add "images/night_icon.png":
                    xalign .5
                    ypos -20
            else:
                add "images/sun_icon.png":
                    xalign .5
                    ypos -20
            text "[current_day]":
                ypos -25
                xalign .5
                size 16
                if current_day == "Saturday" or current_day == "Sunday":
                    color "#f00"

            add "images/calendar_overlay.png":
                ypos -145
                if int(current_hour[:2]) not in night:
                    alpha 0.0
                else:
                    alpha 0.5

    frame: #clock-display
        xpos 1810
        ypos 120
        xpadding 0
        ypadding 0
        background Image('images/clock.png')
        hbox: #hour-display
            xsize 50
            $ hour = current_hour[:2]
            text "[hour]":
                color "#ffffff"
                xalign .5
                font "gui/fonts/digital_dismay.otf"
                size 25
        hbox: #: - separates hours and minutes
            xsize 2
            xpos 44
            ypos -2
            text ":":
                color "#ffffff"
                xalign .5
                font "gui/fonts/digital_dismay.otf"
                size 34
        hbox: #minute-display
            xsize 50
            xpos 50
            $ minute = current_hour[3:]
            text "[minute]":
                color "#ffffff"
                xalign .5
                font "gui/fonts/digital_dismay.otf"                
                size 25                

        add "images/clock_overlay.png":
            if int(current_hour[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5


    if tt.value: #show tooltips
        frame:
            pos(x, y)
            anchor (xval, yval)
            text tt.value style "tooltip_hover"

screen changelog():
    tag menu

    use game_menu(_("Changelog"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if gui.changelog:
                text "[gui.changelog!t]\n"


## This is redefined in options.rpy to add text to the about screen.
define gui.changelog = ""

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

screen splash():
    timer 2.0 action Hide("splash",dissolve) #Hide("splash",dissolve) #Dissolve(1.0)
    add "#000"
    # scene black
    text "Errilhl Studios Presents..." size 60 color "#ffffff" yalign .5 xalign .5

screen stat_screen():
    modal True
    zorder 10000
    default stats = None
    frame:
        xalign .5 ypos .1
        xsize 800
        ysize 700
        vpgrid:
            cols 6
            spacing 20
            for i in chars:
                if i[1] == "fs":
                    imagebutton auto "images/characters/juliette/juliette_%s.png" focus_mask True action [SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                        hovered SetScreenVariable("stats",i)
                        if not setstate == i[1]:
                            unhovered SetScreenVariable("stats",False)
                    text "[i[0]]" ypos 25
                # elif i[1] == "fM":
                #     imagebutton auto "images/characters/anne/anne_face_%s.png" focus_mask True action SetScreenVariable("stats",i)
                #     text "[i[0]]" ypos 25
                elif i[1] == "nk":
                    imagebutton auto "images/characters/karen/karen_%s.png" focus_mask True action [SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                        hovered SetScreenVariable("stats",i)
                        if not setstate == i[1]:
                            unhovered SetScreenVariable("stats",False)
                    text "[i[0]]" ypos 25
                else:
                    imagebutton auto "images/question_mark_%s.png" focus_mask True action [SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                        hovered SetScreenVariable("stats",i)
                        if not setstate == i[1]:
                            unhovered SetScreenVariable("stats",False)
                    if i[1] == "sn" or i[1] == "sp":
                        text "[i[0]]" ypos 25
                    else:
                        text "[i[0]]" ypos 35
        imagebutton auto "gui/closebutton_%s.png" xalign 1.0 yalign 1.0 focus_mask True action [SetScreenVariable('stats',False),Hide("stat_screen")]

        if stats:
            vbox:
                xalign .5
                yalign .8
                text "{b}[stats[0]]'s stats{/b}"
                $ mc_p = (float(mc_b)/float(mc_b_max))*100
                $ mc_p = "{0:.2f}".format(mc_p)
                if stats[1] == "fp":
                    text "Main sexual preference: [fp_sex_pref]"
                    if punishment_late < 3:
                        text "Late: [punishment_late]"
                    else:
                        text "Late: [punishment_late]" style "red_color"
                    text "Motorcyle done: [mc_b]/[mc_b_max] ([mc_p]%)"
                    text "Attitude: [fp_att]"
                elif stats[1] == "nr" or stats[1] == "sp" or stats[1] == "sj":
                    text "Rel: ["+stats[1]+"_rel]"
                else:
                    hbox:
                        hbox:
                            xsize 200
                            text "Dom:"
                            text "["+stats[1]+"_dom]":
                                xpos 10
                        if cheat:
                            imagebutton auto "images/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_dom",getattr(store,stats[1]+"_dom")-1):
                                ypos 5
                                xpos 40
                            imagebutton auto "images/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_dom",getattr(store,stats[1]+"_dom")+1):
                                ypos 5
                                xpos 50
                    hbox:
                        hbox:
                            xsize 200
                            text "Rel:"
                            text "["+stats[1]+"_rel]":
                                xpos 20
                        if cheat:                                
                            imagebutton auto "images/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_rel",getattr(store,stats[1]+"_rel")-1):
                                ypos 5
                                xpos 40
                            imagebutton auto "images/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_rel",getattr(store,stats[1]+"_rel")+1):
                                ypos 5
                                xpos 50
                    hbox:
                        hbox:
                            xsize 200
                            text "Aro:"
                            text "["+stats[1]+"_aro]":
                                xpos 20
                        if cheat:                                
                            imagebutton auto "images/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_aro",getattr(store,stats[1]+"_aro")-1):
                                ypos 5
                                xpos 40
                            imagebutton auto "images/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_aro",getattr(store,stats[1]+"_aro")+1):
                                ypos 5
                                xpos 50
                    if getattr(store, ""+stats[1]+"_cor") > 10:
                        text "BJ: ["+stats[1]+"_bj] / 20"
                        text "Sex: ["+stats[1]+"_pussy] / 30"
                        text "Anal: ["+stats[1]+"_anal] / 40"

screen inventory_screen():
    zorder 250
    modal True
    frame:
        xalign .5 ypos .1
        xsize 740
        ysize 700
        $ current_items = set()
        $ xa = 0
        $ ya = 0
        $ i = 0
        for file in renpy.list_files():
            if file.startswith('images/inventory/') and file.endswith('.png'):
                if 'hover' in file:
                    $ name = file.replace('images/inventory/','').replace('_idle','').replace('_hover','').replace('.png','')
                    for item in backpack:
                        if item.name == name:
                            vbox:
                                xpos xa
                                ypos ya
                                xsize 148
                                ysize 148
                                $ current_items = item.name
                                imagebutton auto "images/inventory/"+name+"_%s.png":
                                    xalign 0
                                    yalign 0
                                    focus_mask True 
                                    action [Hide("inventory_screen")]
                                text "[item.amount]":
                                    xalign .5
                            $ xa += 148
                            $ i += 1
                            if (i % 5 == 0):
                                $ xa = 0
                                $ ya += 173
                    if not name in current_items:
                        vbox:
                            xpos xa
                            ypos ya
                            xsize 148
                            ysize 148
                            add "images/inventory/"+name+"_insensitive.png"
                            text "0":
                                xalign .5
                        $ xa += 148
                        $ i += 1
                        if (i % 5 == 0):
                            $ xa = 0
                            $ ya += 173

        imagebutton auto "gui/closebutton_%s.png" xalign 1.0 yalign 1.0 focus_mask True action Hide("inventory_screen")                        

screen say(who, what):
    style_prefix "say"
    # zorder -1

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
                if who.upper() == fpinput.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_fp.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == fmName.formal.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_fm.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == fsName.formal.upper():
                    style "namebox_char"                    
                    background Frame("gui/namebox_fs.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == nb.name.upper():
                    style "namebox_char"                    
                    background Frame("gui/namebox_nb.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == nk.name.upper():
                    style "namebox_char"                    
                    background Frame("gui/namebox_nk.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == nr.name.upper():
                    style "namebox_char"                    
                    background Frame("gui/namebox_nr.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == sn.name.upper():
                    style "namebox_char"                    
                    background Frame("gui/namebox_sn.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == sp.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_sp.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == sj.name.upper():
                    style "namebox_char"                    
                    background Frame("gui/namebox_sj.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
        if who is not None and what:
            background Image("gui/textbox_cutout.png", xalign=0.5, yalign=1.0)
        elif not what:
            background Image("gui/textbox_transparent.png", xalign=0.5,yalign=1.0)
        else:
            background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

        text what id "what":
            properties gui.text_properties("dialogue")
            xpos gui.dialogue_xpos
            xsize 990
            ypos gui.dialogue_ypos

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign .5 xpos 250 yalign 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

# if who is not None:
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style namebox_char:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=False)
    xalign gui.name_xalign
    yalign 0.5
    color "#ffffff"

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

screen location(room=False):
    layer "master"
    $ exitdown = exitleft = exitup = exitright = False
    default tt = Tooltip("")
    default x = 500
    default y = 400
    # Get mouse coords:
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    if room == 'entrance':
        if int(current_hour[:2]) in night:
            imagebutton auto "images/backgrounds/interactions_move/front_door_night_%s.png" focus_mask True action Jump('outside_loc'):
                hovered tt.Action("Go outside")
            imagebutton auto "images/backgrounds/interactions_move/kitchen_door_night_%s.png" focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]:
                hovered tt.Action('Kitchen')
            imagebutton auto "images/backgrounds/interactions_move/livingroom_door_night_%s.png" focus_mask True action Jump('livingroom_loc'):
                hovered tt.Action("Livingroom")
            imagebutton auto "images/backgrounds/interactions_move/stairs_up_night_%s.png" focus_mask True action [SetVariable('uhl_cfs',True),Jump('upper_hallway_loc')]
            # imagebutton auto "images/backgrounds/entrance_hallway_night_%s.png" focus_mask True action Jump('lower_hallway_loc'):
            #     hovered tt.Action("Hallway")
        else:
            imagebutton auto "images/backgrounds/interactions_move/front_door_morning_%s.png" focus_mask True action Jump('outside_loc'):
                hovered tt.Action("Go outside")
            imagebutton auto "images/backgrounds/interactions_move/kitchen_door_morning_%s.png" focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]:
                hovered tt.Action('Kitchen')                            
            imagebutton auto "images/backgrounds/interactions_move/livingroom_door_morning_%s.png" focus_mask True action Jump('livingroom_loc'):
                hovered tt.Action("Livingroom")            
            imagebutton auto "images/backgrounds/interactions_move/stairs_up_morning_%s.png" focus_mask True action [SetVariable('uhl_cfs',True),Jump('upper_hallway_loc')]                
        #     imagebutton auto "images/backgrounds/entrance_hallway_morning_%s.png" focus_mask True action Jump('lower_hallway_loc'):
        #         hovered tt.Action("Hallway")

        # $ exitdown_event = "lower_hallway_loc"
        # $ exitdown = "Hallway"

    if room == "fp bedroom":
        if day_week <= 4:
            if not backpack.has_item(schoolbooks_item):
                if int(current_hour[:2]) in night:
                    add "images/backgrounds/interactions_item/fp_bedroom_night_dresser_idle.png"
                else:
                    imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_morning_dresser_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('schoolbooks_added',True),Jump('fp_bedroom_loc')]

        if int(current_hour[:2]) == 22 or int(current_hour[:2]) == 23 or current_hour[:2] == 0 or int(current_hour[:2]) == 1:
            imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_night_bed_glow_%s.png" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]
        elif int(current_hour[:2]) in night:
            imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_night_bed_%s.png" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]
        else:
            imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_morning_bed_%s.png" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]

        $ exitdown_event_var = "uhl_cfs"
        $ exitdown_event = "upper_hallway_loc"
        $ exitdown = "Upper hallway"

    if room == "fs bedroom":
        if find_panties:
            if int(current_hour[:2]) in night:
                imagebutton auto "images/backgrounds/interactions_item/"+gp+"_night_%s.png" focus_mask True action [SetVariable('find_panties',False),SetVariable('panties_added',True),SetVariable('gp',gp),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
            else:
                imagebutton auto "images/backgrounds/interactions_item/"+gp+"_morning_%s.png" focus_mask True action [SetVariable('find_panties',False),SetVariable('panties_added',True),SetVariable('gp',gp),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]

        $ exitdown_event_var = "uhl_cfs"
        $ exitdown_event = "upper_hallway_loc"
        $ exitdown = "Upper hallway"       

    if room == "garage":
        if not backpack.has_item(toolbox_item):
            if int(current_hour[:2]) in night:
                add "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_night_idle.png"
            elif not end_bike_repair:
                imagebutton auto "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('toolbox_added',True),Jump('garage_loc')]
            else:
                imagebutton auto "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]

        if int(current_hour[:2]) not in night and not end_bike_repair:
            imagebutton auto "images/tools_1_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('wmc_cfs',True),Jump('w_mc')]:
                xalign .5
                yalign .5

        $ exitdown_event = "outside_loc"
        $ exitdown = "Go outside"        

    if room == "livingroom":
        $ exitdown_event = "entrance_loc"
        $ exitdown = "Entrance"

    # if room == "lower hallway":
    #     if int(current_hour[:2]) in night:
    #         imagebutton auto "images/backgrounds/interactions_move/lower_hallway_night_kitchen_%s.png" focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]
    #     else:
    #         imagebutton auto "images/backgrounds/interactions_move/lower_hallway_morning_kitchen_%s.png" focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]
    #     if hallway_pot_enable:
    #         imagebutton auto "images/backgrounds/interactions_item/lower_hallway_morning_pot_%s.png" focus_mask True action Jump('lower_hallway_loc')

    #     $ exitleft_event_var = "uhl_cfs"
    #     $ exitleft_event = "upper_hallway_loc"
    #     $ exitleft = "Upper hallway"
    #     $ exitdown_event = "entrance_loc"
    #     $ exitdown = "Entrance"

    if room == "kitchen":
        if wcount == 5:
            if bottles == 1 or br == 1:
                imagebutton auto "images/backgrounds/interactions_item/wine_bottle_%s.png" focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',1),SetVariable('wine_added',True),Jump('kitchen_loc')]
            elif bottles == 2 or br == 2:
                imagebutton auto "images/backgrounds/interactions_item/wine_two_bottles_%s.png" focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]
            elif bottles == 3 or br == 3:
                imagebutton auto "images/backgrounds/interactions_item/wine_three_bottles_%s.png" focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]

        $ exitdown_event = "entrance_loc"
        $ exitdown = "Entrance"

    if room == "outside neighborhood":
        $ exitdown_event = "entrance_loc"
        $ exitdown = "Back into the house"
        $ exitleft_event_var = "gar_cfs"
        $ exitleft_event = "garage_loc"
        $ exitleft = "Garage"
        if mc_f:
            $ exitright_event = "beach_ride"
            $ exitright = "Go to the beach"

    if room == "upper hallway":
        if int(current_hour[:2]) in night:
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_fp_door_night_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]:
                hovered tt.Action("Enter your room")
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_fs_door_night_%s.png" focus_mask True action [SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]:
                hovered tt.Action("Enter [fsName.yourformal]'s room")
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_bathroom_night_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),Jump('upper_hallway_bathroom_loc')]:
                hovered tt.Action("Enter bathroom")
            imagebutton auto "images/backgrounds/interactions_move/stairs_down_night_%s.png" focus_mask True action Jump('entrance_loc'):
                hovered tt.Action("Downstairs")       
        else:
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_fp_door_morning_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]:
                hovered tt.Action("Enter your room")
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_fs_door_morning_%s.png" focus_mask True action [SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]:
                hovered tt.Action("Enter [fsName.yourformal]'s room")
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_bathroom_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),Jump('upper_hallway_bathroom_loc')]:
                hovered tt.Action("Enter bathroom")       
            imagebutton auto "images/backgrounds/interactions_move/stairs_down_morning_%s.png" focus_mask True action Jump('entrance_loc'):
                hovered tt.Action("Downstairs")       



    if room == "upper hallway bathroom":
        if int(current_hour[:2]) >= 6 and int(current_hour[:2]) <= 14 and not backpack.has_item(small_keys_item) and keys_mentioned:
            imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_keys_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("smallkeys_added",True),Jump('upper_hallway_bathroom_loc')]

        if int(current_hour[:2]) in night:
            # imagebutton auto "images/backgrounds/upper_hallway_bathroom_shower_night_%s.png" focus_mask True action [SetVariable("fpshower",True),Jump('upper_hallway_bathroom_loc')]
            imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_sink_night_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("fpsink",True),Jump('upper_hallway_bathroom_loc')]
        else:
            imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_shower_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("fpshower",True),Jump('upper_hallway_bathroom_loc')]            
            imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_sink_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("fpsink",True),Jump('upper_hallway_bathroom_loc')]                        

        $ exitdown_event_var = "uhl_cfs"
        $ exitdown_event = "upper_hallway_loc"
        $ exitdown = "Upper hallway"


    if exitdown:
        if exitdown_event_var:
            imagebutton auto "images/exit_down_%s.png" focus_mask True action [SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                xalign .5
                yalign 1.0
                hovered tt.Action(exitdown)
        else:
            imagebutton auto "images/exit_down_%s.png" focus_mask True action Jump(exitdown_event):
                xalign .5
                yalign 1.0
                hovered tt.Action(exitdown)
    if exitleft:
        if exitleft_event_var:
            imagebutton auto "images/exit_left_%s.png" focus_mask True action [SetVariable(exitleft_event_var,True),Jump(exitleft_event)]:
                xalign 0.0
                yalign .5
                hovered tt.Action(exitleft)
        else:
            imagebutton auto "images/exit_left_%s.png" focus_mask True action Jump(exitleft_event):
                xalign 0.0
                yalign .5
                hovered tt.Action(exitleft)
    if exitup:
        if exitup_event_var:
            imagebutton auto "images/exit_up_%s.png" focus_mask True action [SetVariable(exitup_event_var,True),Jump(exitup_event)]:
                xalign .5
                yalign 0.0
                hovered tt.Action(exitup)
        else:
            imagebutton auto "images/exit_up_%s.png" focus_mask True action Jump(exitup_event):
                xalign .5
                yalign 0.0
                hovered tt.Action(exitup)
    if exitright:
        if exitright_event_var:
            imagebutton auto "images/exit_right_%s.png" focus_mask True action [SetVariable(exitright_event_var,True),Jump(exitright_event)]:
                xalign 1.0
                yalign .5
                hovered tt.Action(exitright)
        else:
            imagebutton auto "images/exit_right_%s.png" focus_mask True action Jump(exitright_event):
                xalign 1.0
                yalign .5
                hovered tt.Action(exitright)

    if tt.value:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text tt.value style "tooltip_hover"        