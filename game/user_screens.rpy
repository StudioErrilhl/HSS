style tooltip_hover:
    yalign 0.5
    xmaximum 600
    color "#fff"

style red_color:
    color "#f00"

style inventory_text:
    color "#fff"

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
                frame:
                    background "gui/textbox_top.png"
                    xalign .5
                    xpos -50
                    ypos -650
                    hbox:
                        xalign .5
                        text caption:
                            # xalign .8
                            xpos 650
                            ypos 20

init -2:
    $ config.narrator_menu = False

    style choice_vbox is vbox
    style choice_button is button
    style choice_button_text is button_text
    style choice_button_disabled_text is button_text

    style choice_vbox:
        xalign 0.5
        ypos 405
        yanchor 0.5
        spacing gui.choice_spacing

    # style choice_caption:
        # xalign .5
        # yalign 0.0
        # yanchor 0.0
        # ypos -600
        # color "#000"

    style choice_button is default:
        properties gui.button_properties("choice_button")
        hover_color "#000"

    # style choice_button_text is default:
    #     # properties gui.button_text_properties("choice_button")
    #     hover_color "#000"

    style choice_button_disabled is default:
        properties gui.button_properties("choice_button_disabled")

    style choice_button_disabled is default:
        properties gui.button_text_properties("choice_button_disabled")
        color "#aaaaaa"        
    style menu_window is default

    # style menu_choice is button_text:
    #     clear

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

    # add gui.main_menu_background

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
            xpos -730
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
    color "#fff"

screen ingame_menu_display(day_week=day_week,month=current_month_text,month_day=current_month_day,current_time=current_time):
    zorder 300
    # default tt = Tooltip("")
    # default tooltip = ''    
    default x = 500
    default y = 400
    # Get mouse coords:
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    hbox xalign 0 yalign 0:
        imagebutton auto "images/stats_%s.png" focus_mask True action Show('stat_screen'):
            tooltip "Here you'll find all the stats for all the characters in the game. Some characters doesn't have a lot of stats currently, this may change with the coming updates"
        add "images/stats_overlay.png":
            xpos -128
            if int(current_time[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5
        # if carry_phone:
        #     imagebutton auto "images/menu_phone_%s.png" focus_mask True action Show('iphone') at ModZoom(.65):
        #         xpos -175
        #         ypos -15
        #         tooltip "Here's your phone. Here you will be able to load, save and view galleries and more"
        #     add "images/menu_phone_overlay.png" at ModZoom(.65):
        #         xpos -340
        #         ypos -15
        #         if int(current_time[:2]) not in night:
        #             alpha 0.0
        #         else:
        #             alpha 0.5
        if filth_val == 0:
            imagebutton idle "gui/tshirt.png":
                xpos -150
                ypos 10
                tooltip "You're clean as a whistle"
                action NullAction()
        else:
            add "gui/tshirt.png":
                xpos -150
                ypos 10
            imagebutton idle "gui/tshirt_overlay.png":
                xpos -250
                ypos 10
                # ypos -100
                if filth_val < 10:
                    at alpha_transform(.1)
                    tooltip "Might be time to wash your hands ("+str(filth_val)+"% dirty)"
                    action NullAction()                        
                elif filth_val < 20:
                    at alpha_transform(.2)
                    tooltip "Cleanliness is a virtue ("+str(filth_val)+"% dirty)"
                    action NullAction()                        
                elif filth_val < 30:
                    at alpha_transform(.3)
                    tooltip "You pick your nose with those hands? Yuck! ("+str(filth_val)+"% dirty)"
                    action NullAction()                        
                elif filth_val < 40:
                    at alpha_transform(.4)
                    tooltip "Okay, a bit of grime under the fingernails isn't that bad... but seriously ("+str(filth_val)+"% dirty)"
                    action NullAction()                        
                elif filth_val < 50:
                    at alpha_transform(.5)
                    tooltip "There is dirty, and then there is you ("+str(filth_val)+"% dirty)"
                    action NullAction()                        
                elif filth_val < 60:
                    at alpha_transform(.6)
                    tooltip "Have you been digging up the entire back yard? ("+str(filth_val)+"% dirty)"
                    action NullAction()                        
                elif filth_val < 70:
                    at alpha_transform(.7)
                    tooltip "Seriously, have you ever heard of soap? ("+str(filth_val)+"% dirty)"
                    action NullAction()                        
                elif filth_val < 80:
                    at alpha_transform(.8)
                    tooltip "Sometimes, one wonders why we even invented showers, or soap ("+str(filth_val)+"% dirty)"
                    action NullAction()
                elif filth_val < 90:
                    at alpha_transform(.9)
                    tooltip "You're really dirty. You should go take a shower ("+str(filth_val)+"% dirty)"
                    action NullAction()
                else:
                    tooltip "You're filthy! Go wash up! ("+str(filth_val)+"% dirty)"
                    action NullAction()

    vbox xalign .99 yalign .99: #inventory / backpack
        imagebutton auto "images/backpack_%s.png":
            xalign 0.8
            ypos 100
            focus_mask True 
            action [Show("inventory_screen")]
            tooltip "Here you'll be able to see what you have in your backpack"
        add "images/backpack_overlay.png":
            ypos -16
            if int(current_time[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5

    frame: #filth-meter
        xpos 1650
        xpadding 0
        ypadding 0
        background None
        vbox:
            if carry_phone:
                imagebutton auto "images/menu_phone_%s.png" focus_mask True action Show('iphone') at ModZoom(.65):
                    # xpos -175
                    ypos -15
                    tooltip "Here's your phone. Here you will be able to load, save and view galleries and more"
                add "images/menu_phone_overlay.png" at ModZoom(.65):
                    xpos -340
                    ypos -15
                    if int(current_time[:2]) not in night:
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
                color "#fff"
                size 20
            text "[current_month_day]":
                xalign .5
                color "#000"
                ypos -5
                size 55
            if bad_weather and rainstorm and int(current_time[:2]) in night:
                add "images/night_rain_icon.png":
                    xalign .5
                    ypos -15               
            elif bad_weather and rainstorm:
                add "images/morning_rain_icon.png":
                    xalign .5
                    ypos -15                
            elif int(current_time[:2]) in night:
                add "images/night_icon.png":
                    xalign .5
                    ypos -15
            else:
                add "images/sun_icon.png":
                    xalign .5
                    ypos -15
            text "[current_day]":
                ypos -20
                xalign .5
                size 16
                if current_day == "Saturday" or current_day == "Sunday":
                    color "#f00"
                else:
                    color "#000"

            add "images/calendar_overlay.png":
                ypos -140
                if int(current_time[:2]) not in night:
                    alpha 0.0
                else:
                    alpha 0.5

    frame: #clock-display
        xpos 1810
        ypos 120
        xpadding 0
        ypadding 0
        background Image('images/clock_idle.png')
        hbox: #hour-display
            xsize 50
            $ hour = current_time[:2]
            textbutton "[hour]":
                text_color "#ffffff"
                xalign .5
                ypos -20
                text_font "gui/fonts/digital_dismay.otf"
                text_size 25
                # action Function(renpy.call,'addtime',1,False)
                action Function(addtime,1,False,True)
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
            $ minute = current_time[3:]
            textbutton "[minute]":
                text_color "#ffffff"
                xalign .5
                ypos -20
                text_font "gui/fonts/digital_dismay.otf"                
                text_size 25                
                # action Function(renpy.call,'addtime',False,30)
                action Function(addtime,False,30,True)                

        add "images/clock_overlay.png":
            if int(current_time[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"        

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
    timer 2.0 action Hide("splash",dissolve)
    add "#000"
    text "Errilhl Studios Presents..." size 60 color "#ffffff" yalign .5 xalign .5

screen stat_screen():
    modal True
    zorder 800
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
                            imagebutton auto "images/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_dom",math.floor(getattr(store,stats[1]+"_dom")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "images/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_dom",math.floor(getattr(store,stats[1]+"_dom")+1)):
                                ypos 5
                                xpos 50
                    hbox:
                        hbox:
                            xsize 200
                            text "Rel:"
                            text "["+stats[1]+"_rel]":
                                xpos 20
                        if cheat:                                
                            imagebutton auto "images/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_rel",math.floor(getattr(store,stats[1]+"_rel")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "images/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_rel",math.floor(getattr(store,stats[1]+"_rel")+1)):
                                ypos 5
                                xpos 50
                    hbox:
                        hbox:
                            xsize 200
                            text "Aro:"
                            text "["+stats[1]+"_aro]":
                                xpos 20
                        if cheat:                                
                            imagebutton auto "images/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_aro",math.floor(getattr(store,stats[1]+"_aro")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "images/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_aro",math.floor(getattr(store,stats[1]+"_aro")+1)):
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
        xsize 672
        ysize 539
        xpadding 20
        ypadding 20
        $ current_items = set()
        $ xa = 0
        $ ya = 0
        $ i = 0
        vpgrid:
            style_prefix "inventory"
            cols 4
            rows 4
            scrollbars "vertical"
            edgescroll 100,500
            mousewheel True 
            spacing 5               
            for file in renpy.list_files():
                if file.startswith('images/inventory/') and file.endswith('.png'):
                    if 'hover' in file:
                        $ name = file.replace('images/inventory/','').replace('_idle','').replace('_hover','').replace('.png','')
                        for item in backpack:
                            if item.name == name:
                                fixed:
                                    xsize 148
                                    ysize 160
                                    $ current_items = item.name
                                    if name == 'pink_buttplug':
                                        imagebutton auto "images/inventory/"+name+"_%s.png":
                                            xalign .5
                                            yalign 0
                                            focus_mask True
                                            action [Hide('inventory_screen')]
                                    elif name == 'phone' and current_location == 'fp_bedroom_loc':
                                        imagebutton auto "images/inventory/"+name+"_%s.png":
                                            xalign .5
                                            yalign 0
                                            focus_mask True
                                            action [Hide('inventory_screen'),SetVariable('charge_phone',True),SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]
                                    else:
                                        imagebutton auto "images/inventory/"+name+"_%s.png":
                                            xalign .5
                                            yalign 0
                                            focus_mask True 
                                            action [Hide("inventory_screen")]
                                    text "[item.amount]":
                                        xalign .45
                                        yalign 1.0
                                    $ xa += 148
                                    $ i += 1
                                    $ ya -= 148
                                    if (i % 4 == 0):
                                        $ xa = 0
                                        $ ya += 173
                        if not name in current_items:
                            fixed:
                                xsize 148
                                ysize 160
                                add "images/inventory/"+name+"_insensitive.png":
                                    xalign .5
                                text "0":
                                    xalign .5
                                    yalign 1.0
                                $ xa += 148
                                $ i += 1
                                $ ya -= 148
                                if (i % 4 == 0):
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
    default x = 500
    default y = 400
    # Get mouse coords:
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    if room == 'entrance':
        if int(current_time[:2]) in night:
            imagebutton auto "images/backgrounds/interactions_move/front_door_night_%s.png" focus_mask True action [SetVariable('trans',True),SetVariable('out_cfs',True),Jump('outside_loc')]:
                tooltip "Go outside"
            imagebutton auto "images/backgrounds/interactions_move/kitchen_door_night_%s.png" focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]:
                tooltip 'Kitchen'
            imagebutton auto "images/backgrounds/interactions_move/livingroom_door_night_%s.png" focus_mask True action [SetVariable('lvr_cfs',True),Jump('livingroom_loc')]:
                tooltip "Livingroom"
            imagebutton auto "images/backgrounds/interactions_move/stairs_up_night_%s.png" focus_mask True action [SetVariable('uhl_cfs',True),Jump('upper_hallway_loc')]:
                tooltip "Upstairs"
            imagebutton auto "images/backgrounds/interactions_move/stairs_basement_night_%s.png" focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]:
                tooltip "Downstairs / Garage"
        else:
            imagebutton auto "images/backgrounds/interactions_move/front_door_morning_%s.png" focus_mask True action [SetVariable('out_cfs',True),Jump('outside_loc')]:
                tooltip "Go outside"
            imagebutton auto "images/backgrounds/interactions_move/kitchen_door_morning_%s.png" focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]:
                tooltip 'Kitchen'
            imagebutton auto "images/backgrounds/interactions_move/livingroom_door_morning_%s.png" focus_mask True action [SetVariable('lvr_cfs',True),Jump('livingroom_loc')]:
                tooltip "Livingroom"
            imagebutton auto "images/backgrounds/interactions_move/stairs_up_morning_%s.png" focus_mask True action [SetVariable('uhl_cfs',True),Jump('upper_hallway_loc')]:
                tooltip "Upstairs"
            imagebutton auto "images/backgrounds/interactions_move/stairs_basement_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]:
                tooltip "Downstairs / Garage"

    if room == "fp bedroom":
        if day_week <= 4:
            if not backpack.has_item(schoolbooks_item):
                if int(current_time[:2]) in night:
                    add "images/backgrounds/interactions_item/fp_bedroom_night_dresser_idle.png"
                else:
                    imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_morning_dresser_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('schoolbooks_added',True),Jump('fp_bedroom_loc')]

        if int(current_time[:2]) == 22 or int(current_time[:2]) == 23 or current_time[:2] == 0 or int(current_time[:2]) == 1:
            imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_night_bed_glow_%s.png" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]
        elif int(current_time[:2]) in night:
            imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_night_bed_%s.png" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]
        else:
            imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_morning_bed_%s.png" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]

        if not carry_phone:    
            if int(current_time[:2]) in night:
                imagebutton auto "images/backgrounds/interactions_item/phone_night_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('phone_added',True),Jump('fp_bedroom_loc')]
            else:
                imagebutton auto "images/backgrounds/interactions_item/phone_morning_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('phone_added',True),Jump('fp_bedroom_loc')]                

        $ exitdown_event_var = "uhl_cfs"
        $ exitdown_event = "upper_hallway_loc"
        $ exitdown = "Upper hallway"

    if room == "fs bedroom":
        if find_panties:
            if int(current_time[:2]) in night:
                imagebutton auto "images/backgrounds/interactions_item/bedroom_panties_"+gp_bed+"_night_%s.png" focus_mask True action [SetVariable('find_panties',False),SetVariable('panties_added',True),SetVariable('gp_bed',gp_bed),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
            else:
                imagebutton auto "images/backgrounds/interactions_item/bedroom_panties_"+gp_bed+"_morning_%s.png" focus_mask True action [SetVariable('find_panties',False),SetVariable('panties_added',True),SetVariable('gp_bed',gp_bed),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]

        if find_tablet:
            if int(current_time[:2]) in night:
                imagebutton auto "images/backgrounds/interactions_item/fs_tablet_bedroom_night_%s.png" focus_mask True action [SetVariable('find_tablet',False),SetVariable('tablet_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
            else:
                imagebutton auto "images/backgrounds/interactions_item/fs_tablet_bedroom_morning_%s.png" focus_mask True action [SetVariable('find_tablet',False),SetVariable('tablet_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]                
        if find_pb:             
            if not backpack.has_item(princessplug_item):   
                if int(current_time[:2]) in night:
                    imagebutton auto "images/backgrounds/interactions_item/pink_buttplug_night_%s.png" focus_mask True action [SetVariable('find_pb',False),SetVariable('pb_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
                else:
                    imagebutton auto "images/backgrounds/interactions_item/pink_buttplug_morning_%s.png" focus_mask True action [SetVariable('find_pb',False),SetVariable('pb_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        $ exitdown_event_var = "uhl_cfs"
        $ exitdown_event = "upper_hallway_loc"
        $ exitdown = "Upper hallway"       

    if room == "garage":
        if not backpack.has_item(toolbox_item):
            if int(current_time[:2]) in night:
                add "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_night_idle.png"
            elif not end_bike_repair:
                imagebutton auto "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('toolbox_added',True),Jump('garage_loc')]
            else:
                imagebutton auto "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]

        if int(current_time[:2]) not in night and not end_bike_repair and not mc_f:
            imagebutton auto "images/tools_1_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('wmc_cfs',True),Jump('w_mc')]:
                xalign .5
                yalign .5

        $ exitleft_event = "entrance_loc"
        $ exitleft = "Upstairs / Entrance"

        $ exitdown_event_var = "out_cfs"            
        $ exitdown_event = "outside_loc"
        $ exitdown = "Go outside"        

    if room == "livingroom":
        $ exitright_event_var = "kit_cfs"
        $ exitright_event = "kitchen_loc"
        $ exitright = "Kitchen"
        $ exitdown_event = "entrance_loc"
        $ exitdown = "Entrance"

    if room == "kitchen":
        if wcount == 5:
            if bottles == 1 or br == 1 and int(current_time[:2]) in (day or night):
                if int(current_time[:2]) in night:
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_night_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',1),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
                else:
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_morning_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',1),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
            elif bottles == 2 or br == 2:
                if int(current_time[:2]) in night:
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_night_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31       
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_night_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .325                    
                else:
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_morning_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31       
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_morning_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .325
            elif bottles == 3 or br == 3:
                if int(current_time[:2]) in night:
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_night_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .480
                        xpos .315                    
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_night_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31                                        
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_night_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .325                    
                else:
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_morning_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .480
                        xpos .315 
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_morning_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31                    
                    imagebutton auto "images/backgrounds/interactions_item/wine_bottle_morning_%s.png" at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .325                    

        $ exitleft_event_var = "lvr_cfs"
        $ exitleft_event = "livingroom_loc"
        $ exitleft = "Livingroom"                   
        $ exitdown_event = "entrance_loc"
        $ exitdown = "Entrance"

    if room == "outside":
        $ exitdown_event = "entrance_loc"
        $ exitdown = "Back into the house"
        $ exitleft_event_var = "gar_cfs"
        $ exitleft_event = "garage_loc"
        $ exitleft = "Garage"
        if mc_f:
            $ exitright_event = "beach_ride"
            $ exitright = "Go to the beach"

    if room == "upper hallway":
        if int(current_time[:2]) in night:
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_fp_door_night_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]:
                tooltip "Enter your room"
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_fs_door_night_%s.png" focus_mask True action [SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]:
                tooltip "Enter [fsName.yourformal]'s room"
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_bathroom_night_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),Jump('upper_hallway_bathroom_loc')]:
                tooltip "Enter bathroom"
            imagebutton auto "images/backgrounds/interactions_move/stairs_down_night_%s.png" focus_mask True action Jump('entrance_loc'):
                tooltip "Downstairs"
        else:
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_fp_door_morning_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]:
                tooltip "Enter your room"
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_fs_door_morning_%s.png" focus_mask True action [SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]:
                tooltip "Enter [fsName.yourformal]'s room"
            imagebutton auto "images/backgrounds/interactions_move/upper_hallway_bathroom_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),Jump('upper_hallway_bathroom_loc')]:
                tooltip "Enter bathroom"
            imagebutton auto "images/backgrounds/interactions_move/stairs_down_morning_%s.png" focus_mask True action Jump('entrance_loc'):
                tooltip "Downstairs"

    if room == "upper hallway bathroom":
        if int(current_time[:2]) >= 6 and int(current_time[:2]) <= 14 and not backpack.has_item(small_keys_item) and keys_mentioned:
            imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_keys_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("smallkeys_added",True),Jump('upper_hallway_bathroom_loc')]

        if int(current_time[:2]) in night:
            # imagebutton auto "images/backgrounds/upper_hallway_bathroom_shower_night_%s.png" focus_mask True action [SetVariable("fpshower",True),Jump('upper_hallway_bathroom_loc')]
            imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_sink_night_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("fpsink",True),Jump('upper_hallway_bathroom_loc')]
            if bathroom_light:
                imagebutton auto "images/backgrounds/interactions_item/bathroom_lightswitch_night_light_on_%s.png" focus_mask True action [ToggleVariable('bathroom_light'),SetVariable('uhl_bl_cfs',True),Jump('upper_hallway_bathroom_loc')]    
            else:
                imagebutton auto "images/backgrounds/interactions_item/bathroom_lightswitch_night_%s.png" focus_mask True action [ToggleVariable('bathroom_light'),SetVariable('uhl_bl_cfs',True),Jump('upper_hallway_bathroom_loc')]
        else:
            if bathroom_find_panties:
                imagebutton auto "images/backgrounds/interactions_item/bathroom_panties_"+gp_bath+"_%s.png" focus_mask True action [SetVariable('bathroom_find_panties',False),SetVariable('bathroom_panties_added',True),SetVariable('gp_bath',gp_bath),SetVariable('uhl_bl_cfs',True),Jump('upper_hallway_bathroom_loc')]
            imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_shower_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("fpshower",True),Jump('upper_hallway_bathroom_loc')]            
            imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_sink_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("fpsink",True),Jump('upper_hallway_bathroom_loc')]                        
            add "images/backgrounds/interactions_item/bathroom_lightswitch_morning_off_idle.png"

        $ exitdown_event_var = "uhl_cfs"
        $ exitdown_event = "upper_hallway_loc"
        $ exitdown = "Upper hallway"

    if exitdown:
        if exitdown_event_var:
            if current_location == 'upper_hallway_bathroom_loc' and (bathroom_panties_added or fpshower):
                imagebutton auto "images/exit_down_%s.png" focus_mask True action [SetVariable('fpshower',False),SetVariable('bathroom_panties_added',False),SetVariable('bathroom_find_panties',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
            elif current_location == 'fs_bedroom_loc' and (panties_added or pb_added):
                if panties_added and not pb_added:
                    imagebutton auto "images/exit_down_%s.png" focus_mask True action [SetVariable('panties_added',False),SetVariable('find_panties',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
                elif not panties_added and pb_added:
                    imagebutton auto "images/exit_down_%s.png" focus_mask True action [SetVariable('pb_added',False),SetVariable('find_pb',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
                else:
                    imagebutton auto "images/exit_down_%s.png" focus_mask True action [SetVariable('pb_added',False),SetVariable('find_pb',True),SetVariable('panties_added',False),SetVariable('find_panties',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
            else:
                imagebutton auto "images/exit_down_%s.png" focus_mask True action [SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
        else:
            imagebutton auto "images/exit_down_%s.png" focus_mask True action Jump(exitdown_event):
                xalign .5
                yalign 1.0
                tooltip exitdown
    if exitleft:
        if exitleft_event_var:
            imagebutton auto "images/exit_left_%s.png" focus_mask True action [SetVariable(exitleft_event_var,True),Jump(exitleft_event)]:
                xalign 0.0
                yalign .5
                tooltip exitleft
        else:
            imagebutton auto "images/exit_left_%s.png" focus_mask True action Jump(exitleft_event):
                xalign 0.0
                yalign .5
                tooltip exitleft
    if exitup:
        if exitup_event_var:
            imagebutton auto "images/exit_up_%s.png" focus_mask True action [SetVariable(exitup_event_var,True),Jump(exitup_event)]:
                xalign .5
                yalign 0.0
                tooltip exitup
        else:
            imagebutton auto "images/exit_up_%s.png" focus_mask True action Jump(exitup_event):
                xalign .5
                yalign 0.0
                tooltip exitup
    if exitright:
        if exitright_event_var:
            imagebutton auto "images/exit_right_%s.png" focus_mask True action [SetVariable(exitright_event_var,True),Jump(exitright_event)]:
                xalign 1.0
                yalign .5
                tooltip exitright
        else:
            imagebutton auto "images/exit_right_%s.png" focus_mask True action Jump(exitright_event):
                xalign 1.0
                yalign .5
                tooltip exitright

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"        

screen iphone():
    modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    if persistent.iphone_info:
        on 'show' action Show('iphone_info_screen')

    fixed:
        fit_first True
        xmaximum 500
        ymaximum 800  
        xalign .5
        yalign .5   
        add "images/iphone_background_black.png" at ModZoom(.85)
         
        hbox: #notification-bar
            if battery_text != 0:
                add "images/iphone_notification_bar.png" at ModZoom(.85)
                xalign .5
                yalign 0.0
        hbox: #battery-indicator
            if battery_text != 0:
                if battery_text == 100:
                    add "images/iphone_battery_100.png"
                elif battery_text < 100 and battery_text >= 90:
                    add "images/iphone_battery_90.png"
                elif battery_text < 90 and battery_text >= 80:
                    add "images/iphone_battery_80.png"
                elif battery_text < 80 and battery_text >= 70:
                    add "images/iphone_battery_70.png"
                elif battery_text < 70 and battery_text >= 60:
                    add "images/iphone_battery_60.png"
                elif battery_text < 60 and battery_text >= 50:
                    add "images/iphone_battery_50.png"
                elif battery_text < 50 and battery_text >= 40:
                    add "images/iphone_battery_40.png"
                elif battery_text < 40 and battery_text >= 30:
                    add "images/iphone_battery_30.png"
                elif battery_text < 30 and battery_text >= 20:
                    add "images/iphone_battery_20.png"
                elif battery_text < 20 and battery_text >= 10:
                    add "images/iphone_battery_10.png"
                else:
                    add "images/iphone_battery_0.png"                
                at ModZoom(.85)
                xalign .5
                yalign 0.0
        hbox: #battery-text
            if battery_text != 0:
                xalign .825
                yalign 0.123
                text "[battery_text]":
                    font "gui/fonts/texgyreheroes_regular.otf"
                    size 13
        hbox: #clock
            if battery_text != 0:
                xalign .5
                yalign 0.118 
                text "[current_time]":
                    font "gui/fonts/texgyreheroes_regular.otf"
                    size 18
        hbox:
            if battery_text != 0:
                xalign 0.120
                yalign 0.17 
                spacing 10          
                if show_icons:
                    imagebutton auto "images/iphone_achievement_button_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('display_achievements')] at ModZoom(.9):
                        tooltip "Open the achievement-screen"
        hbox:
            add "images/iphone_white.png" at ModZoom(.85)
            xalign .5
            yalign .5
        hbox:
            if battery_text != 0:
                xalign 0.5
                yalign .83
                # yalign 0.22
                spacing 10
                if show_icons:
                    imagebutton auto "images/iphone_main_menu_button_%s.png" focus_mask True action [SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'mainmenu')] at ModZoom(.9):
                        tooltip "Go to the main menu"
                    imagebutton auto "images/iphone_save_button_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('custom_save')] at ModZoom(.9):
                        tooltip "Save your game"
                    imagebutton auto "images/iphone_load_button_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('custom_load')] at ModZoom(.9):
                        tooltip "Load your game"
                    imagebutton auto "images/iphone_settings_button_%s.png" focus_mask True action [SetVariable('pref_screen',True),SetVariable('show_icons',False),Show('custom_preferences')] at ModZoom(.9):
                        tooltip "Show preferences screen"
                    imagebutton auto "images/iphone_quit_button_%s.png" focus_mask True action [SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'quit')] at ModZoom(.9):
                        tooltip "Quit the game"
        hbox:
            imagebutton auto "images/iphone_white_power_%s.png" focus_mask True action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements'),Hide('iphone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            xalign .5
            yalign .5
        hbox:
            if battery_text != 0:
                imagebutton auto "images/iphone_white_home_%s.png" focus_mask True action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements')] at ModZoom(.85):
                    tooltip "Go back to the home-screen"
                xalign .5
                yalign .5

    # if tooltip: #show tooltips
    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"        

screen iphone_info_screen():
    zorder 950
    hbox:
        imagebutton:
            idle "images/iphone_white_power_hover.png"
            hover "images/iphone_white_power_hover.png"
            focus_mask True
            action [SetField(persistent,'iphone_info',False),SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('iphone_info_screen'),Hide('display_achievements'),Hide('iphone')] at ModZoom(.85)
            tooltip "Shut off the phone"
        xalign .5
        yalign .5
    hbox:
        if battery_text != 0:
            imagebutton:
                idle "images/iphone_white_home_hover.png"
                hover "images/iphone_white_home_hover.png"
                focus_mask True
                action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements')] at ModZoom(.85)
                tooltip "Go back to the home-screen"
            xalign .5
            yalign .5

screen custom_confirm(cc_chosen=False):
    zorder 900

    frame:
        background None
        xpadding 0
        top_padding 40
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686
        vbox:
            if cc_chosen == 'quit':
                text "{color=#fff}Do you want to quit?{/color}":
                    xalign .5
            elif cc_chosen == 'mainmenu':
                text "{color=#fff}Do you want to go to the main menu? All unsaved progress will be lost{/color}":
                    xalign .5
            textbutton "{color=#0f0}Yes{/color}\n":
                xalign 0.5
                ypos 100
                if cc_chosen == 'quit':
                    action Function(renpy.quit)                
                elif cc_chosen == 'mainmenu':
                    action MainMenu(confirm=False)
            textbutton "{color=#f00}No{/color}\n":
                xalign 0.5
                ypos 100
                action [SetVariable('show_icons',True),Hide('custom_confirm')]

screen display_achievements():
    modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    on 'show' action Function(achievement_trophy_case.update)

    use display_achievements_category_panel

    hbox:
        xalign .5
        yalign .5
        add "images/iphone_background_light.png" at ModZoom(.85)
    hbox: #notification-bar
        if battery_text != 0:
            add "images/iphone_notification_bar.png" at ModZoom(.85)
            xalign .5
            yalign .5
    hbox: #battery-indicator
        if battery_text != 0:
            if battery_text == 100:
                add "images/iphone_battery_100.png"
            elif battery_text < 100 and battery_text >= 90:
                add "images/iphone_battery_90.png"
            elif battery_text < 90 and battery_text >= 80:
                add "images/iphone_battery_80.png"
            elif battery_text < 80 and battery_text >= 70:
                add "images/iphone_battery_70.png"
            elif battery_text < 70 and battery_text >= 60:
                add "images/iphone_battery_60.png"
            elif battery_text < 60 and battery_text >= 50:
                add "images/iphone_battery_50.png"
            elif battery_text < 50 and battery_text >= 40:
                add "images/iphone_battery_40.png"
            elif battery_text < 40 and battery_text >= 30:
                add "images/iphone_battery_30.png"
            elif battery_text < 30 and battery_text >= 20:
                add "images/iphone_battery_20.png"
            elif battery_text < 20 and battery_text >= 10:
                add "images/iphone_battery_10.png"
            else:
                add "images/iphone_battery_0.png"                
            at ModZoom(.85)
            xalign .5
            yalign .5
    hbox: #battery-text
        if battery_text != 0:
            xalign .575
            yalign .18
            text "[battery_text]":
                font "gui/fonts/texgyreheroes_regular.otf"
                size 13
    hbox: #clock
        if battery_text != 0:
            xalign .5
            yalign .177
            text "[current_time]":
                font "gui/fonts/texgyreheroes_regular.otf"
                size 18
    frame:
        background None
        # add "images/iphone_background_light.png" at ModZoom(.85)
        xpadding 0
        top_padding 40
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686
        # background "images/iphone_background_light.png" at ModZoom(.85)

        viewport:
            mousewheel True
            vbox:
                $ i = 0
                for achievement in achievements:
                    if achievement.category in selected_category:
                        if achievement.hidden:
                            if not hide_hidden_achievements:
                                fixed:
                                    xsize 370
                                    ysize 100
                                    imagebutton auto "images/achievement_%s.png" focus_mask True:
                                        if selected_achievement != achievement_hidden:
                                            action [SetVariable('selected_number',i),SetVariable('selected_achievement', achievement_hidden)]
                                        elif selected_achievement == achievement_hidden and selected_number != i:
                                            action [SetVariable('selected_number',i),SetVariable('selected_achievement', achievement_hidden)]                                            
                                        else:                                
                                            action SetVariable('selected_achievement',False)
                                        selected selected_achievement == achievement_hidden
                                    add achievement.hidden_image at ModZoom(.5):
                                        ypos 14
                                        xalign .1
                                    text "{b}{color=#fff}"+achievement.name+"{/color}{/b}" size 14:
                                        xpos 100  
                                        ypos 38  
                                    add "images/phone_hidden.png":
                                        xpos 300
                                        ypos 35
                                    if selected_achievement == achievement_hidden and i == selected_number:
                                        ysize 160
                                        vbox:
                                            xsize 370
                                            xalign .5
                                            yalign .9
                                            if selected_achievement.unlocked:
                                                text "Achievement Unlocked!" xalign 0.5 yalign 0.5 size 14
                                            text "{b}"+selected_achievement.name+"{/b}" size 16 xalign 0.5 text_align 0.5
                                            text selected_achievement.description size 14 xalign 0.5 text_align 0.5
                                            if selected_achievement is not achievement_hidden and selected_achievement.unlocked is False:
                                                text "[selected_achievement.progress]/[selected_achievement.progress_max]" size 16 xalign 0.5 text_align 0.5                                  
                        else:
                            if hide_unlocked_achievements and hide_locked_achievements:
                                pass
                            elif hide_unlocked_achievements:
                                if not achievement.unlocked:
                                    fixed:
                                        xsize 370
                                        ysize 100                           
                                        imagebutton auto "images/achievement_%s.png" focus_mask True:                                   
                                            if selected_achievement != achievement:
                                                action SetVariable('selected_achievement', achievement)
                                            else:                                
                                                action SetVariable('selected_achievement',False)
                                            selected selected_achievement == achievement
                                        add achievement.image at ModZoom(.5):
                                            ypos 14
                                            xalign .1
                                        text "{b}{color=#fff}"+achievement.name+"{/color}{/b}" size 14:
                                            xpos 100 
                                            ypos 38                                        
                                        add "images/phone_lock.png":
                                            xpos 300
                                            ypos 35
                                        if selected_achievement == achievement:
                                            ysize 160
                                            vbox:
                                                xsize 370
                                                xalign .5
                                                yalign .9
                                                if selected_achievement.unlocked:
                                                    text "Achievement Unlocked!" xalign 0.5 yalign 0.5 size 14
                                                text "{b}"+selected_achievement.name+"{/b}" size 16 xalign 0.5 text_align 0.5
                                                text selected_achievement.description size 14 xalign 0.5 text_align 0.5
                                                if selected_achievement is not achievement_hidden and selected_achievement.unlocked is False:
                                                    text "[selected_achievement.progress]/[selected_achievement.progress_max]" size 16 xalign 0.5 text_align 0.5                                  

                            elif hide_locked_achievements:
                                if achievement.unlocked:
                                    fixed:
                                        xsize 370
                                        ysize 100
                                        imagebutton auto "images/achievement_%s.png" focus_mask True:                                 
                                            if selected_achievement != achievement:
                                                action SetVariable('selected_achievement', achievement)
                                            else:                                
                                                action SetVariable('selected_achievement',False)
                                            selected selected_achievement == achievement                                                
                                        add achievement.image at ModZoom(.5):
                                            ypos 14
                                            xalign .1
                                        text "{b}{color=#fff}"+achievement.name+"{/color}{/b}" size 14:
                                            xpos 100  
                                            ypos 38     
                                        add "images/phone_unlock.png":                               
                                            xpos 300
                                            ypos 35
                                        if selected_achievement == achievement:
                                            ysize 160                                            
                                            vbox:
                                                xsize 370
                                                xalign .5
                                                yalign .9
                                                if selected_achievement.unlocked:
                                                    text "Achievement Unlocked!" xalign 0.5 yalign 0.5 size 14
                                                text "{b}{color=#fff}"+selected_achievement.name+"{/color}{/b}" size 16 xalign 0.5 text_align 0.5
                                                text selected_achievement.description size 14 xalign 0.5 text_align 0.5
                                                if selected_achievement is not achievement_hidden and selected_achievement.unlocked is False:
                                                    text "[selected_achievement.progress]/[selected_achievement.progress_max]" size 16 xalign 0.5 text_align 0.5                                  
                            else:
                                fixed:
                                    xsize 370
                                    ysize 100         
                                    imagebutton auto "images/achievement_%s.png" focus_mask True:                                
                                        if selected_achievement != achievement:
                                            action SetVariable('selected_achievement', achievement)
                                        else:                                
                                            action SetVariable('selected_achievement',False)
                                        selected selected_achievement == achievement                                            
                                    add achievement.image at ModZoom(.5):
                                        ypos 14
                                        xalign .1
                                    text "{b}{color=#fff}"+achievement.name+"{/color}{/b}" size 14:
                                        xpos 100
                                        ypos 38
                                    if achievement.unlocked:
                                        add "images/phone_unlock.png":
                                            xpos 300
                                            ypos 35
                                    elif not achievement.unlocked:
                                        add "images/phone_lock.png":
                                            xpos 300
                                            ypos 35
                                    elif achievement.hidden:
                                        add "images/phone_hidden.png":
                                            xpos 300
                                            ypos 35
                                    if selected_achievement == achievement:
                                        ysize 160
                                        vbox:
                                            xsize 370
                                            xalign .5
                                            yalign .9
                                            if selected_achievement.unlocked:
                                                text "Achievement Unlocked!" xalign 0.5 yalign 0.5 size 14
                                            text "{b}"+selected_achievement.name+"{/b}" size 16 xalign 0.5 text_align 0.5
                                            text selected_achievement.description size 14 xalign 0.5 text_align 0.5
                                            if selected_achievement is not achievement_hidden and selected_achievement.unlocked is False:
                                                text "[selected_achievement.progress]/[selected_achievement.progress_max]" size 12 xalign 0.5 text_align 0.5   
                    $ i += 1                               

    frame:
        background None
        xalign .5
        yalign .5
        hbox:
            imagebutton auto "images/iphone_white_power_%s.png" focus_mask True action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements'),Hide('iphone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            xalign .5
            yalign .5
        hbox:
            imagebutton auto "images/iphone_white_home_%s.png" focus_mask True action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements')] at ModZoom(.85):
                tooltip "Go back to the home-screen"
            xalign .5
            yalign .5           
        hbox:
            xalign .5
            yalign .5
            add "images/iphone_bottom_overlay.png" at ModZoom(.85)
        hbox:
            xalign .5
            yalign .818
            imagebutton idle "phone_unlock.png":
                action ToggleVariable('hide_unlocked_achievements')
                xpos -100
            imagebutton idle "phone_lock.png":
                action ToggleVariable('hide_locked_achievements')
                xalign .5
            imagebutton idle "phone_hidden.png":
                action ToggleVariable('hide_hidden_achievements')        
                xpos 100

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"    


# This allows the user to view achievements based on their category
screen display_achievements_category_panel():
    frame:
        padding 15, 15
        align 0.03, 0.13
        vbox:                 
            spacing 5
            text "Category" xalign 0.5 underline True size 26 color "#fff"
            textbutton "All":
                action SetVariable('selected_category', [category.lower() for category in achievement_categories])
                selected selected_category == [category.lower() for category in achievement_categories]
            for category in achievement_categories:
                textbutton category:
                    action SetVariable('selected_category', category.lower())
                    selected selected_category == category.lower()
                    
# This is the achievement notification
screen display_achievement_unlocked():

    # I SPENT HOURS TRYING TO GET IT TO WORK WITHOUT THIS!!!! I AM SO ANGRY RIGHT NOW AND I FUCKING GIVE UP!!!!!!! <--- LOOK HOW MANY EXCLAMATION MARKS THAT IS!!!!!! (╯°□°)╯︵ ┻━┻
    #if len(achievement_notification_queue) > 0: <---- FUCK YOU!!!!!!!!!! I DON'T NEED YOU ANYMORE
    python:
        show_length = len(achievement_notification_queue[0].name + achievement_notification_queue[0].description) * 0.1            
        if show_length < 3.0: 
            show_length = 3.0 
        elif show_length > 7.0: 
            show_length = 7.0
                                                    
    frame:
        at achievement_transform
        padding 15,15
        #background "#333333"
        xmaximum 450
        hbox:
            spacing 10
            if achievement_notification_queue[0].image:
                add achievement_notification_queue[0].image xalign 0.5 yalign 0.5
            vbox:
                yalign .5
                spacing 5
                text "Achievement Unlocked!" xalign 0.5 size 14 color "#fff"
                text achievement_notification_queue[0].name size 20 xalign 0.5 text_align 0.5 color "#fff"
                text achievement_notification_queue[0].description size 16 xalign 0.5 text_align 0.5 color "#fff"
                
        # timer show_length action [Hide('display_achievement_unlocked'), RemoveFromSet(achievement_notification_queue, achievement_notification_queue[0]), 
                                # If(len(achievement_notification_queue) > 0, true=Show('display_achievement_unlocked'), false=NullAction())]           
        
    timer show_length action If(len(achievement_notification_queue) > 1, 
                                true=[Hide('display_achievement_unlocked'), RemoveFromSet(achievement_notification_queue, achievement_notification_queue[0]), Show('display_achievement_unlocked')], 
                                false=[Hide('display_achievement_unlocked'), RemoveFromSet(achievement_notification_queue, achievement_notification_queue[0])]
                                )      

screen confirm_age():
    frame:
        background "#000"
        margin 15,15
        padding 15,15
        at truecenter
        xsize 1200
        vbox:            
            text "\n{i}{color=#fff}AGE-RESTRICTED CONTENT WARNING{/color}{/i}\n" xalign 0.5
            text "{b}{color=#fff}You must be 18 years of age or older to play this game{/color}{/b}\n" xalign 0.5
            text "{color=#fff}I confirm that I am over 18 years of age, and understand that this game contains material featuring nudity and/or sexually-explicit material and/or adult themes that are age-restricted, and I confirm that by clicking 'ENTER' I agree that I am not offended by viewing such material.{/color}\n" xalign 0.5 
            textbutton "{color=#0f0}ENTER{/color}\n":
                xalign 0.5
                action Return()
            text "{color=#fff}I am under 18 years of age and/or do not want to access this game{/color}\n" xalign 0.5
            textbutton "{color=#f00}EXIT{/color}\n":
                xalign 0.5
                action Function(renpy.quit)

screen splash_info():
    frame:
        background "#000"
        margin 15,15
        padding 15,15
        at truecenter
        xsize 1200
        vbox:
            # if persistent.patch_enabled:
            text "{size=30}{color=#ffffff}HSS - High School Shenanigans is a story about a very hot summer, where you'll play as <your name here> (You can name your own character, but the default is \"Marten\", so let's just go with that for now). So, you play as Marten, on his last stretch of high school, aiming to finish school, have some fun, fix his bike, and take his dream cross-country trip on it - but first, there's the exams. And the hot chicks... (among them, his [fmName.role] and [fsName.role], who is both hot, and definitely part of his nighttime jerk-off sessions), the pool, the neighbor girl, and so much more - pretty much like there is in every teenager's life. You control what happens, who you eventually hook up with, what you end up doing with them, and so on and so forth. \n\n{b}Note that this is a very early Alpha-relese, and that quite a lot of the events haven't been added yet, and those that have been, might abruptly end. The game is playable, but you won't reach a fulfilling conclusion as of yet!{/b}{/color}{/size}"
            # else:
            #     text "{size=30}{color=#ffffff}HSS - High School Shenanigans is a story about a very hot summer, where you'll play as <your name here> (You can name your own character, but the default is \"Marten\", so let's just go with that for now). So, you play as Marten, on his last stretch of high school, aiming to finish school, have some fun, fix his bike, and take his dream cross-country trip on it - but first, there's the exams. And the hot chicks... and the pool, the neighbor girl, and so much more - pretty much like there is in every teenager's life. You control what happens, who you eventually hook up with, what you end up doing with them, and so on and so forth.\n\n{b}Note that this is a very early Alpha-relese, and that quite a lot of the events haven't been added yet, and those that have been, might abruptly end. The game is playable, but you won't reach a fulfilling conclusion as of yet!{/b}{/color}{/size}" #with dissolve
    textbutton "{size=25}{color=#ffffff}Click to continue{/click}{/size}":
        xalign .5 
        yalign 0.9
        action Return()

screen disclaimer():
    frame:
        background "#000"
        margin 15,15
        padding 15,15
        at truecenter
        xsize 1300
        vbox:
            text "{size=30}{color=#ffffff}The story is purely fictional, and does not reflect the creator's worldview.\nWe do not condone, nor support the actions and opinions of the characters{/color}{/size}"


screen custom_save():
    zorder 900
    use custom_file_slots(_("Save"))


screen custom_load():
    zorder 900
    use custom_file_slots(_("Load"))

screen custom_preferences():
    modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    frame:
        background None
        xpadding 0
        top_padding 40
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686

        viewport:
            mousewheel True
            vbox:
                if renpy.variant("pc"):
                    fixed:
                        style_prefix "custom_radio"
                        xsize 370
                        ysize 150
                        hbox:
                            yalign 0.0
                            xalign .5
                            label _("Display"):
                                text_color "#fff"
                        hbox:
                            ypos 40
                            textbutton _("Window") action Preference("display", "window"):
                                foreground "gui/button/check_[prefix_]foreground_white.png"                            
                        hbox:
                            ypos 80
                            textbutton _("Fullscreen") action Preference("display", "fullscreen"):
                                foreground "gui/button/check_[prefix_]foreground_white.png"                            

                fixed:
                    xsize 370
                    ysize 200
                    # style_prefix "custom_radio"
                    style_prefix "custom_radio"
                    hbox:
                        yalign 0.0
                        xalign .5
                        label _("Rollback Side"):
                            text_color "#fff"
                    hbox:
                        ypos 40
                        textbutton _("Disable") action Preference("rollback side", "disable"):
                            foreground "gui/button/check_[prefix_]foreground_white.png"
                    hbox:
                        ypos 80
                        textbutton _("Left") action Preference("rollback side", "left"):
                            foreground "gui/button/check_[prefix_]foreground_white.png"
                    hbox:
                        ypos 120
                        textbutton _("Right") action Preference("rollback side", "right"):
                            foreground "gui/button/check_[prefix_]foreground_white.png"

                fixed:
                    xsize 370
                    ysize 200
                    # style_prefix "custom_check"
                    style_prefix "custom_radio"
                    hbox:
                        yalign 0.0
                        xalign .5
                        label _("Skip"):
                            text_color "#fff"
                    hbox:
                        ypos 40
                        textbutton _("Unseen Text") action Preference("skip", "toggle"):
                            foreground "gui/button/check_[prefix_]foreground_white.png"                        
                    hbox:
                        ypos 80
                        textbutton _("After Choices") action Preference("after choices", "toggle"):
                            foreground "gui/button/check_[prefix_]foreground_white.png"                        
                    hbox:
                        ypos 120
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")):
                            foreground "gui/button/check_[prefix_]foreground_white.png"                        

                fixed:
                    xsize 370
                    ysize 200
                    # style_prefix "custom_slider"
                    hbox:
                        yalign 0.0
                        xalign .5
                        label _("Text Speed"):
                            text_color "#fff"
                    hbox:
                        ypos 80
                        bar value Preference("text speed")
                fixed:
                    xsize 370
                    ysize 200
                    # style_prefix "custom_slider"                   
                    hbox:
                        yalign 0.0
                        xalign .5
                        label _("Auto-Forward Time"):
                            text_color "#fff"
                    hbox:
                        ypos 80
                        bar value Preference("auto-forward time")
                if config.has_music:
                    fixed:
                        xsize 370
                        ysize 200
                        # style_prefix "custom_slider"                    
                        hbox:
                            yalign 0.0
                            xalign .5
                            label _("Music Volume"):
                                text_color "#fff"
                        hbox:
                            ypos 80
                            bar value Preference("music volume"):
                                xsize 375
                if config.has_sound:
                    fixed:
                        xsize 370
                        ysize 200
                        # style_prefix "custom_slider"                                    
                        hbox:
                            yalign 0.0
                            xalign .5
                            label _("Sound Volume"):
                                text_color "#fff"
                        hbox:
                            ypos 80
                            bar value Preference("sound volume"):
                                xsize 375
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                if config.has_voice:
                    fixed:
                        xsize 370
                        ysize 200
                        # style_prefix "custom_slider"                                    
                        hbox:
                            yalign 0.0
                            xalign .5
                            label _("Voice Volume"):
                                text_color "#fff"
                        hbox:
                            ypos 80
                            bar value Preference("voice volume"):
                                xsize 375
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice):
                                    text_color "#fff"
                if config.has_music or config.has_sound or config.has_voice:
                    fixed:
                        xsize 370
                        ysize 200
                        # style_prefix "custom_slider"                                 
                        hbox:
                            yalign 0.0
                            xalign .5
                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"
                                text_color "#fff"
                                foreground "gui/button/check_[prefix_]foreground_white.png"

    frame:
        background None
        xalign .5
        yalign .5
        hbox:
            imagebutton auto "images/iphone_white_power_%s.png" focus_mask True action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements'),Hide('custom_preferences'),Hide('iphone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            xalign .5
            yalign .5
        hbox:
            imagebutton auto "images/iphone_white_home_%s.png" focus_mask True action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements'),Hide('custom_preferences')] at ModZoom(.85):
                tooltip "Go back to the home-screen"
            xalign .5
            yalign .5           

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover" 


# style pref_label is pref_heading
# style pref_label_text is gui_label_text
# style pref_vbox is vbox

# style radio_label is custom_pref_label
# style radio_label_text is custom_pref_label_text
# style radio_button is gui_button
# style radio_button_text is gui_button_text
# style radio_vbox is pref_vbox

# style check_label is custom_pref_label
# style check_label_text is custom_pref_label_text
# style check_button is gui_button
# style check_button_text is gui_button_text
# style check_vbox is pref_vbox

# style slider_label is pref_label
# style slider_label_text is pref_label_text
# style slider_slider is gui_slider
# style slider_button is gui_button
# style slider_button_text is gui_button_text
# style slider_pref_vbox is pref_vbox

# style mute_all_button is check_button
# style mute_all_button_text is check_button_text

# style pref_heading:
#     # xalign .5
#     # xpos 75
#     xalign .5
#     color "#fff"

# style custom_pref_label:
#     top_margin gui.pref_spacing
#     bottom_margin 3
#     color "#fff"

# style custom_pref_label_text:
#     yalign 1.0
#     color "#fff"

# style pref_vbox:
#     xsize 338

# style radio_vbox:
#     spacing gui.pref_button_spacing

# style custom_radio_button:
    # properties gui.button_properties("radio_button")
    # foreground "gui/button/check_[prefix_]foreground_white.png"

# style custom_radio:
#     foreground "gui/button/radio_[prefix_]foreground_white.png"

# style radio_button_text:
#     properties gui.button_text_properties("radio_button")

# style check_vbox:
#     spacing gui.pref_button_spacing

# style custom_check_button:
#     # properties gui.button_properties("check_button")
#     foreground "gui/button/check_[prefix_]foreground_white.png"

# # style check_button_text:
# #     properties gui.button_text_properties("check_button")

# style custom_slider_slider:
#     xsize 375

# # style slider_button:
# #     properties gui.button_properties("slider_button")
# #     yalign 0.5
# #     left_margin 15

# style custom_slider_button_text:
#     color "#fff"

# style slider_vbox:
#     xsize 675

screen custom_file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    frame:
        background None
        xpadding 0
        top_padding 40
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686

        viewport:
            mousewheel True
            ysize 600
            vbox:
                hbox:
                    xalign .5
                    yalign 0
                    maximum 370, 20
                    input:
                        style "custom_page_label_text"
                        value page_name_value

                for i in range(gui.custom_file_slot_cols * gui.custom_file_slot_rows):
                    fixed:
                        style_prefix "custom_slot"
                        xsize 370
                        ysize 220
                        xalign .5
                        $ slot = i + 1

                        button:
                            style "custom_slot_button"
                            if title == "Load":
                                action FileLoad(slot)
                            else:
                                action FileAction(slot)
                            xsize 350
                            ysize 200
                            padding 0,0
                            xalign .5
                            add "#555"
                            add FileScreenshot(slot) xalign 0.5 #at ModZoom(.9)
                            frame:
                                background "#000000cc"
                                xsize 350
                                ysize 60
                                padding 0,0
                                yalign .5
                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Empty slot")):
                                    style "slot_name_text"
                                    color "#fff"
                                text FileSaveName(slot):
                                    style "slot_name_text"
                                    color "#fff"
                            key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            xalign 0.5
            yalign 1.0

            spacing gui.page_spacing
            textbutton _("<") action FilePagePrevious():
                style "nav_buttons"
                text_color "#fff"                
            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto"):
                    style "nav_buttons"
                    text_color "#fff"
            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick"):
                    style "nav_buttons"
                    text_color "#fff"
            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page):
                    style "nav_buttons"
                    text_color "#fff"
            textbutton _(">") action FilePageNext():
                style "nav_buttons"
                text_color "#fff"
                                     
style custom_page_label is gui_label
style custom_page_label_text is gui_label_text
style custom_page_button is gui_button
style custom_page_button_text is gui_button_text

# style custom_slot_button is gui_button
style slot_button is gui_button
style custom_slot_button_text is gui_button_text
style custom_slot_time_text is custom_slot_button_text
style custom_slot_name_text is custom_slot_button_text

style custom_page_label:
    xpadding 75
    ypadding 5

style nav_buttons:
    size 13
    xpadding 4
    color "#fff"

style custom_page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
    color "#fff"

# style custom_slot_button:
#     # properties gui.button_properties("custom_slot_button")
#     xsize 360
#     ysize 220

style custom_slot_button:
    # properties gui.button_properties("custom_slot_button")
    xsize 370
    ysize 330
    background "#f00"


style custom_slot_button_text:
    size 15
    color "#222"

# screen iphone():
#     modal True
#     zorder 800
#     fixed:
#         fit_first True
#         xmaximum 500
#         ymaximum 800  
#         xalign .5
#         yalign .5      
#         hbox:
#             add "images/iphone_white.png" at ModZoom(.5)
#             xalign .5
#             yalign .5
#         hbox:
#             xalign .5
#             yalign .45
#             if not show_icons and not quit_screen:
#                 add "images/iphone_screen_achievement.png" at ModZoom(0.5)
#             else:
#                 add "images/iphone_screen.png" at ModZoom(0.5)
#         hbox:
#             xalign 0.125
#             yalign 0.14 
#             spacing 10          
#             if show_icons:
#                 imagebutton auto "images/iphone_achievement_button_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('display_achievements')] at ModZoom(.45)


screen fs_tablet():
    default ic_num_str = 0
    modal True
    zorder 800
    fixed:
        fit_first True
        xmaximum 600
        ymaximum 800
        xalign .5
        yalign .5
        if len(ic_num) == 4:
            $ ic_num_str = ''.join(map(str, ic_num))
        hbox:
            yalign .5
            xalign .5
            add "images/tablet.png" at ModZoom(.85)
        hbox: #backgrounds
            yalign .5
            xalign .5
            if len(ic_num) == 4:
                $ ic_num_str = ''.join(map(str, ic_num))
                if int(ic_num_str) == tablet_stored_code:
                    $ tablet_code = True
                    $ ic_num = []
                    # add "tablet_background.png" at ModZoom(.85)
                    add "tablet_no_content_warning.png" at ModZoom(.85)
                else:
                    $ ic_num = []
            elif tablet_code:
                add "images/tablet_background.png" at ModZoom(.85)                
        hbox:
            xalign .5
            yalign .5
            imagebutton auto "images/tablet_power_%s.png" focus_mask True action [SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()] at ModZoom(.85)
                # xpos -620

        if not tablet_code:
            hbox:
                imagemap:
                    alpha False
                    if len(ic_num) == 1:
                        add "images/tablet_unlock_1.png"
                    elif len(ic_num) == 2:
                        add "images/tablet_unlock_2.png"
                    elif len(ic_num) == 3:
                        add "images/tablet_unlock_3.png"
                    elif len(ic_num) == 4:
                        add "images/tablet_unlock_4.png"
                    ground "images/tablet_unlock.png"
                    hover "images/tablet_unlock_hover.png"
                    at ModZoom(.85)
                    yalign .5
                    xalign .5
                    if int(ic_num_str) != tablet_stored_code:
                        hotspot (204, 392, 94, 96) action [AddToSet(ic_num,1)]:
                            sensitive True
                        hotspot (318, 392, 94, 96) action [AddToSet(ic_num,2)]:
                            sensitive True
                        hotspot (436, 394, 94, 96) action [AddToSet(ic_num,3)]:
                            sensitive True
                        hotspot (204, 502, 94, 96) action [AddToSet(ic_num,4)]:
                            sensitive True
                        hotspot (318, 502, 94, 96) action [AddToSet(ic_num,5)]:
                            sensitive True
                        hotspot (436, 502, 94, 96) action [AddToSet(ic_num,6)]:
                            sensitive True
                        hotspot (204, 610, 94, 96) action [AddToSet(ic_num,7)]:
                            sensitive True
                        hotspot (318, 610, 94, 96) action [AddToSet(ic_num,8)]:
                            sensitive True
                        hotspot (436, 610, 94, 96) action [AddToSet(ic_num,9)]:
                            sensitive True
                        hotspot (318, 718, 94, 96) action [AddToSet(ic_num,0)]:
                            sensitive True
                        hotspot (464, 839, 71, 33) action [SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()]:
                            sensitive True
        # hbox:
        #     if len(ic_num) == 4:
        #         $ ic_num_str = ''.join(map(str, ic_num))
        #         if int(ic_num_str) == tablet_stored_code:
        #             $ tablet_code = True
        #             $ ic_num = []
        #             frame:
        #                 background "tablet_white_background.png" at ModZoom(.85)
        #                 yalign .5
        #                 xalign .5
        #         else:
        #             $ ic_num = []

# screen iphone():
#     modal True
#     zorder 800
#     fixed:
#         fit_first True
#         xmaximum 500
#         ymaximum 800  
#         xalign .5
#         yalign .5      
#         hbox:
#             add "images/iphone_white.png" at ModZoom(.5)
#             xalign .5
#             yalign .5
#         hbox:
#             xalign .5
#             yalign .45
#             if not show_icons and not quit_screen:
#                 add "images/iphone_screen_achievement.png" at ModZoom(0.5)
#             else:
#                 add "images/iphone_screen.png" at ModZoom(0.5)
#         hbox:
#             xalign 0.125
#             yalign 0.14 
#             spacing 10          
#             if show_icons:
#                 imagebutton auto "images/iphone_achievement_button_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('display_achievements')] at ModZoom(.45)

#         hbox:
#             xalign 0.5
#             yalign .83
#             # yalign 0.22
#             spacing 10
#             if show_icons:
#                 imagebutton auto "images/iphone_main_menu_button_%s.png" focus_mask True action [SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'mainmenu')] at ModZoom(.45)
#                 imagebutton auto "images/iphone_save_button_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('custom_save')] at ModZoom(.45)
#                 imagebutton auto "images/iphone_load_button_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('custom_load')] at ModZoom(.45)
#                 imagebutton auto "images/iphone_settings_button_%s.png" focus_mask True action ShowMenu('preferences') at ModZoom(.45)
#                 imagebutton auto "images/iphone_quit_button_%s.png" focus_mask True action [SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'quit')] at ModZoom(.45)                

#         hbox:
#             imagebutton auto "images/iphone_white_power_%s.png" focus_mask True action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements'),Hide('iphone')] at ModZoom(.5)
#             xalign .5
#             yalign .5
#         hbox:
#             imagebutton auto "images/iphone_white_home_%s.png" focus_mask True action [SetVariable('show_icons',True),Hide('custom_save'),Hide('custom_load'),Hide('custom_confirm'),Hide('display_achievements')] at ModZoom(.5)
#             xalign .5
#             yalign .5
init python:
    def dd_cursor_position(st, at):
        x, y = renpy.get_mouse_pos()
        return Text("{size=-5}%d-%d" % (x, y)), .1

screen debug_tools():
    add DynamicDisplayable(dd_cursor_position)