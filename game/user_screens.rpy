style infoscreen_text:
    size 22
    justify True

style infoscreen_button_text:
    color "#fff"
    hover_color "#0cf"

style tooltip_hover:
    yalign 0.5
    xmaximum 600
    color "#fff"

style red_color:
    color "#f00"

style inventory_text:
    color "#fff"

style category_button_text:
    color "#fff"
    hover_color "#0cf"
    selected_color "#0cf"
    xalign .5

style contacts_button_text:
    color "#888"
    hover_color "#0cf"
    selected_color "#0cf"

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

    style choice_button is default:
        properties gui.button_properties("choice_button")
        hover_color "#000"

    style choice_button_disabled is default:
        properties gui.button_properties("choice_button_disabled")

    style choice_button_disabled is default:
        properties gui.button_text_properties("choice_button_disabled")
        color "#aaaaaa"
    style menu_window is default

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        ## Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        ## Display a menu, if given.
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
            xpos -730
            ypos 65

        imagebutton:
            idle "gui/patreon_idle.png"
            hover "gui/patreon_hover.png"
            action OpenURL("./game/test.html")

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
    color "#fff"
    size 40

style gm_label_text:
    color "#fff"
    yalign 0.25
    xoffset -40

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0

style white_color:
    color "#fff"

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
    default x = 500
    default y = 400
    ## Get mouse coords:
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    hbox xalign 0 yalign 0:
        imagebutton auto "gui/stats_%s.png" focus_mask True action Show('stat_screen'):
            tooltip "Here you'll find all the stats for all the characters in the game. Some characters doesn't have a lot of stats currently, this may change with the coming updates"
        add "gui/stats_overlay.png":
            xpos -128
            if int(current_time[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5
        if filth_val == 0: ## filth-meter
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

    if not backpack_carry:
        add "gui/backpack_outline.png"
    if backpack_carry:
        vbox xalign .99 yalign .99: #backpack / inventory
            imagebutton auto "gui/backpack_%s.png":
                xalign 0.8
                ypos 100
                focus_mask True
                action [Show("inventory_screen")]
                tooltip "Here you'll be able to see what you have in your backpack"
            add "gui/backpack_overlay.png":
                ypos -16
                if int(current_time[:2]) not in night:
                    alpha 0.0
                else:
                    alpha 0.5

    frame: ## phone-menu
        xpos 1700
        ypos 15
        xpadding 0
        ypadding 0
        background None
        vbox:
            if carry_phone:
                if not hints:
                    imagebutton auto "gui/menu_phone_%s.png" focus_mask True action Show('phone') at ModZoom(.8):
                        tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more"
                else:
                    imagebutton auto "gui/menu_phone_redglow_%s.png" focus_mask True action Show('phone') at ModZoom(.8):
                        tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more. And right now, new hints"

                add "gui/menu_phone_overlay.png" at ModZoom(.8):
                    xpos -340
                    if int(current_time[:2]) not in night:
                        alpha 0.0
                    else:
                        alpha 0.5
            else:
                add "gui/menu_phone_outline.png" at ModZoom(.8)

    frame: #calendar-display
        xpos 1810
        xpadding 0
        ypadding 0
        background Image("gui/calendar.png")
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
                add "gui/night_rain_icon.png":
                    xalign .5
                    ypos -15
            elif bad_weather and rainstorm:
                add "gui/morning_rain_icon.png":
                    xalign .5
                    ypos -15
            elif int(current_time[:2]) in night:
                add "gui/night_icon.png":
                    xalign .5
                    ypos -15
            else:
                add "gui/sun_icon.png":
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

            add "gui/calendar_overlay.png":
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
        background Image('gui/clock_idle.png')
        hbox: #hour-display
            xsize 50
            $ hour = current_time[:2]
            textbutton "[hour]":
                text_color "#ffffff"
                xalign .5
                ypos -10
                text_font "gui/fonts/digital_dismay.otf"
                text_size 25
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
                ypos -10
                text_font "gui/fonts/digital_dismay.otf"
                text_size 25
                action Function(addtime,False,30,True)

        add "gui/clock_overlay.png":
            if int(current_time[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    key "meta_K_q" action [Show('phone'),SetVariable('show_icons',False),Show('custom_confirm',None,'quit')]


screen changelog():
    tag menu

    use game_menu(_("Changelog"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if gui.changelog:
                text "[gui.changelog!t]\n":
                    color "#555"

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

screen splash():
    timer 2.0 action Hide("splash",dissolve)
    add "#555"
    text "Errilhl Studios Presents..." size 60 color "#fff" yalign .5 xalign .5

screen statscreen_infotext():
    modal True
    zorder 960
    $ keyclose = True
    frame:
        xsize 900
        ysize 300
        yalign .5
        xalign .5
        text "The statscreen consists of thumbnails for each character. When hovering over an image, it will display the stats for that character. The stats change over time, so you might wanna keep an eye on them. If you click on a character image, the stats for that character will show permanently and revert back to that character if you hover over another character."
        if cheat:
            text "If you have enabled the cheat-mode, this will allow you to manipulate stats."
        imagebutton auto "gui/closebutton_%s.png" xalign 1.0 yalign 1.0 focus_mask True action [SetVariable('keyclose',False),SetField(persistent,'statscreen_infotext',False),Hide("statscreen_infotext")]
        if keyclose:
            key 'K_ESCAPE' action [SetVariable('keyclose',False),SetField(persistent,'statscreen_infotext',False),Hide("statscreen_infotext")]

screen stat_screen():
    modal True
    if persistent.statscreen_infotext:
        on "show" action Show('statscreen_infotext')
    zorder 800
    default stats = None
    default clicked = None
    $ keyclose = True
    frame:
        xalign .5 ypos .1
        xsize 800
        ysize 800
        padding 40,40
        viewport:
            mousewheel True
            ysize 500
            vpgrid:
                cols 6
                spacing 20
                for i in chars:
                    if i[1] == "fp":
                        imagebutton auto "images/characters/marten/marten_%s.png" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable('setstate',i[1]),SetScreenVariable('stats',i)]:
                            hovered SetScreenVariable('stats',i)
                            if not setstate == i[1]:
                                unhovered SetScreenVariable('stats',clicked)
                        text "[i[0]]" ypos 25
                    elif i[1] == "fs":
                        imagebutton auto "images/characters/juliette/juliette_%s.png" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                            hovered SetScreenVariable("stats",i)
                            if not setstate == i[1]:
                                unhovered SetScreenVariable("stats",clicked)
                        text "[i[0]]" ypos 25
                    elif i[1] == "fm":
                        imagebutton auto "images/characters/anne/anne_%s.png" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                            hovered SetScreenVariable("stats",i)
                            if not setstate == i[1]:
                                unhovered SetScreenVariable("stats",clicked)
                        text "[i[0]]" ypos 25
                    elif i[1] == "nk":
                        imagebutton auto "images/characters/karen/karen_%s.png" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                            hovered SetScreenVariable("stats",i)
                            if not setstate == i[1]:
                                unhovered SetScreenVariable("stats",clicked)
                        text "[i[0]]" ypos 25
                    elif i[1] == "nr":
                        imagebutton auto "images/characters/ron/ron_%s.png" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable('setstate',i[1]),SetScreenVariable('stats',i)]:
                            hovered SetScreenVariable('stats',i)
                            if not setstate == i[1]:
                                unhovered SetScreenVariable('stats',clicked)
                        text "[i[0]]" ypos 25
                    else:
                        imagebutton auto "gui/question_mark_%s.png" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                            hovered SetScreenVariable("stats",i)
                            if not setstate == i[1]:
                                unhovered SetScreenVariable("stats",clicked)
                        if i[1] == "sn" or i[1] == "sp":
                            text "[i[0]]" ypos 25
                        else:
                            text "[i[0]]" ypos 35
        imagebutton auto "gui/closebutton_%s.png" xalign 1.0 yalign 1.0 focus_mask True action [SetVariable('keyclose',False),SetScreenVariable('stats',False),Hide("stat_screen")]
        if keyclose:
            key 'K_ESCAPE' action [SetVariable('keyclose',False),SetScreenVariable('stats',False),Hide("stat_screen")]

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
                elif stats[1] in ["nr","se","sp","sj","scn","scm"]:
                    text "Rel: ["+stats[1]+"_rel]"
                else:
                    hbox:
                        hbox:
                            xsize 200
                            text "Dom:"
                            text "["+stats[1]+"_dom]":
                                xpos 10
                        if cheat:
                            imagebutton auto "gui/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_dom",math.floor(getattr(store,stats[1]+"_dom")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "gui/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_dom",math.floor(getattr(store,stats[1]+"_dom")+1)):
                                ypos 5
                                xpos 50
                    hbox:
                        hbox:
                            xsize 200
                            text "Rel:"
                            text "["+stats[1]+"_rel]":
                                xpos 20
                        if cheat:
                            imagebutton auto "gui/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_rel",math.floor(getattr(store,stats[1]+"_rel")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "gui/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_rel",math.floor(getattr(store,stats[1]+"_rel")+1)):
                                ypos 5
                                xpos 50
                    hbox:
                        hbox:
                            xsize 200
                            text "Aro:"
                            text "["+stats[1]+"_aro]":
                                xpos 20
                        if cheat:
                            imagebutton auto "gui/minusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_aro",math.floor(getattr(store,stats[1]+"_aro")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "gui/plusbutton_small_%s.png" focus_mask True action SetVariable(stats[1]+"_aro",math.floor(getattr(store,stats[1]+"_aro")+1)):
                                ypos 5
                                xpos 50
                    if getattr(store, ""+stats[1]+"_cor") > 10:
                        text "BJ: ["+stats[1]+"_bj] / 20"
                        text "Sex: ["+stats[1]+"_pussy] / 30"
                        text "Anal: ["+stats[1]+"_anal] / 40"

screen inventory_screen():
    zorder 970
    modal True
    $ keyclose = True
    default x = 500
    default y = 400
    ## Get mouse coords:
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    frame:
        style_prefix "infoscreen"
        background "gui/inventory_background.png"
        xalign .5 yalign .5
        xsize 1920
        ysize 1080
        xpadding 20
        ypadding 20
        $ current_items = set()
        $ i = 0
        hbox:
            xsize 700
            vpgrid:
                style_prefix "inventory"
                cols 1
                scrollbars None
                edgescroll 100,500
                mousewheel True
                spacing 5
                $ inv_list = inv_list_fetch()
                for name in sorted(inv_list):
                    if i % 2:
                        $ bg_c = "#565656"
                    else:
                        $ bg_c = "#444"
                    for item in backpack:
                        $ check_item_name = item.name.replace('fs_','').replace('_',' ').capitalize()
                        if 'panties' in check_item_name.lower():
                            $ tempname = check_item_name.replace(' - ',' ').split(' ')
                            if len(tempname) == 2:
                                $ check_item_name = tempname[1]+' - '+tempname[0]
                            else:
                                $ check_item_name = tempname[2]+' - '+tempname[0]+' '+tempname[1]
                        if check_item_name.lower() == name:
                            fixed:
                                xsize 600
                                ysize 160
                                button:
                                    padding 0,0
                                    background bg_c
                                    hover_background "#ddd"
                                    hbox:
                                        xsize 160
                                        ysize 160
                                        $ current_items = check_item_name.lower()
                                        add "images/inventory/outer_ring.png"
                                        add "images/inventory/"+item.name+"_hover.png":
                                            xalign .5
                                            xoffset -140
                                            yalign .5
                                    hbox:
                                        xsize 375
                                        xpos 160
                                        ysize 160
                                        text "[item.displayname]":
                                            hover_color "#222"
                                            xalign 0.0
                                            xoffset 10
                                            yalign .5
                                    hbox:
                                        xsize 65
                                        xpos 535
                                        ysize 160
                                        text "[item.amount]":
                                            hover_color "#222"
                                            xalign .5
                                            yalign .5
                                    action [SetVariable('selecteditemdesc',item.desc),SetVariable('selecteditemweight',item.weight),SetVariable('selecteditemamount',item.amount),SetVariable('selecteditemname',item.displayname),SetVariable('selecteditem',item.name)]

                    if not name in current_items:
                        fixed:
                            xsize 600
                            ysize 160
                            button:
                                background bg_c
                                padding 0,0
                                hbox:
                                    xsize 160
                                    ysize 160
                                    if 'panties' in name:
                                        $ tempname = name.replace(' ','_').replace('_-_','_').lower().split('_')
                                        if len(tempname) == 2:
                                            $ imgname = str('fs_'+tempname[1]+'_'+tempname[0])
                                        elif len(tempname) == 3:
                                            $ imgname = str('fs_'+tempname[1]+'_'+tempname[2]+'_'+tempname[0])
                                    else:
                                        $ imgname = str(name.replace(' ','_').replace('_-_','_').lower())
                                    add "images/inventory/outer_ring_insensitive.png":
                                        xalign .5
                                        yalign .5
                                    add "images/inventory/"+imgname+"_insensitive.png":
                                        xalign .5
                                        xoffset -140
                                        yalign .5
                                hbox:
                                    xsize 375
                                    xpos 160
                                    ysize 160
                                    $ displayname = name.replace('fs_','').replace('_',' ').capitalize()
                                    text "[displayname]":
                                        xalign 0.0
                                        xoffset 10
                                        yalign .5
                                hbox:
                                    xsize 65
                                    xpos 535
                                    ysize 160
                                    text "0":
                                        xalign .5
                                        yalign .5
                    $ i += 1
        hbox:
            xpos 700
            xsize 1130
            ysize 600
            frame:
                xsize 1130
                background Frame("images/inventory/outer_ring_large.png")
                hbox:
                    xsize 158
                    vbox:
                        ysize 158
                        xsize 158
                        add "images/inventory/outer_ring.png"
                    if selecteditem:
                        vbox:
                            ysize 158
                            xsize 158
                            xpos -158
                            add "images/inventory/"+selecteditem+"_idle.png":
                                xalign .5
                                yalign .5
                    vbox:
                        ysize 70
                        xsize 158
                        if selecteditem:
                            xpos -316
                        else:
                            xpos -158
                        ypos 158
                        text "{b}Quantity{/b}" at center
                        text "{0}".format(selecteditemamount if selecteditemamount else '0') at center
                    vbox:
                        ysize 70
                        xsize 158
                        if selecteditem:
                            xpos -474
                        else:
                            xpos -316
                        ypos 228
                        text "{b}Weight{/b}" at center
                        textbutton "{0} / {1}".format(selecteditemweight if selecteditemweight else '0',selecteditemweight*selecteditemamount if selecteditemweight and selecteditemamount else '0'):
                            at center
                            tooltip "Item weight / Total weight"
                            text_size 20
                            action NullAction()
                    vbox:
                        xsize 158
                        ysize 158
                        if selecteditem:
                            xpos -632
                        else:
                            xpos -474
                        ypos 400
                        if selecteditemname and selecteditemname.lower() == 'phone':
                            if battery_text <= 20:
                                $ charge_batt_img = "gui/inventory_charge_phone_red_%s.png"
                            elif battery_text <= 50:
                                $ charge_batt_img = "gui/inventory_charge_phone_orange_%s.png"
                            else:
                                $ charge_batt_img = "gui/inventory_charge_phone_%s.png"
                            imagebutton auto charge_batt_img focus_mask True:
                                at ModZoom(.8)
                                xalign .5
                                yalign .5
                                action [SetVariable('selecteditem',False),SetVariable('selecteditemname',False),SetVariable('selecteditemweight',False),SetVariable('selecteditemamount',False),SetVariable('charge_phone',True),SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]
                                tooltip "Charge your phone"
                hbox:
                    xsize 925
                    vbox:
                        xsize 910
                        xpos 170
                        ysize 40
                        if selecteditemname:
                            text "{b}{size=30}[selecteditemname]{/size}{/b}" at center
                    vbox:
                        xsize 910
                        xpos -740
                        ypos 40
                        if selecteditemdesc:
                            text "[selecteditemdesc]":
                                justify True
                        else:
                            text "This is some flavor text for the item currently shown. It will contain mostly completely irrelevant information, and sometimes it might even include something useful about a completely different item...":
                                justify True


        textbutton "Close inventory" action [SetVariable('selecteditemdesc',False),SetVariable('selecteditem',False),SetVariable('selecteditemname',False),SetVariable('selecteditemweight',False),SetVariable('selecteditemamount',False),SetVariable('keyclose',False),Hide("inventory_screen")] xalign .95 yalign 1.0
        imagebutton auto "gui/closebutton_%s.png" xalign 1.0 yalign 1.0 focus_mask True action [SetVariable('selecteditemdesc',False),SetVariable('selecteditem',False),SetVariable('selecteditemname',False),SetVariable('selecteditemweight',False),SetVariable('selecteditemamount',False),SetVariable('keyclose',False),Hide("inventory_screen")]
        if keyclose:
            key 'K_ESCAPE' action [SetVariable('selecteditemdesc',False),SetVariable('selecteditem',False),SetVariable('selecteditemname',False),SetVariable('selecteditemweight',False),SetVariable('selecteditemamount',False),SetVariable('keyclose',False),Hide("inventory_screen")]

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9

            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    # ypos gui.skip_ypos
    yalign .2
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size
    color "#fff"

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"
    color "#fff"

screen say(who, what):
    style_prefix "say"
    # default side_xalign = 0.0
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
                elif who.upper() == fmName.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_fm.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == fsName.name.upper():
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

        # If there's a side image, display it above the text. Do not display on the
        # phone variant - there's no room.
        if not renpy.variant("small"):
            if who is not None:
                if who.upper() == fpinput.upper():
                    add SideImage() xalign 1.0 yalign 1.0
                else:
                    add SideImage() xalign .5 xpos 250 yalign 1.0

# Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

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
            imagebutton auto ("images/backgrounds/interactions_move/front_door_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/front_door_morning_%s.png") focus_mask True action [SetVariable('trans',True),SetVariable('out_cfs',True),Jump('outside_loc')]:
                tooltip "Go outside"
            imagebutton auto ("images/backgrounds/interactions_move/kitchen_door_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/kitchen_door_morning_%s.png") focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]:
                tooltip 'Kitchen'
            imagebutton auto ("images/backgrounds/interactions_move/livingroom_door_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/livingroom_door_morning_%s.png") focus_mask True action [SetVariable('lvr_cfs',True),Jump('livingroom_loc')]:
                tooltip "Livingroom"
            imagebutton auto ("images/backgrounds/interactions_move/stairs_up_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/stairs_up_morning_%s.png") focus_mask True action [SetVariable('uhl_cfs',True),Jump('upper_hallway_loc')]:
                tooltip "Bedrooms / Bathroom"
            imagebutton auto ("images/backgrounds/interactions_move/stairs_basement_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/stairs_basement_morning_%s.png") focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]:
                tooltip "Downstairs / Garage"

    if room == "fp bedroom":
        if day_week <= 4:
            if not backpack.has_item(schoolbooks_item):
                if int(current_time[:2]) in night:
                    add "images/backgrounds/interactions_item/fp_bedroom_night_dresser_idle.png"
                else:
                    imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_morning_dresser_%s.png" focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('schoolbooks_added',True),Jump('fp_bedroom_loc')]
        if not backpack_carry:
            imagebutton auto ("images/backgrounds/interactions_item/fp_bedroom_night_backpack_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/fp_bedroom_day_backpack_%s.png") focus_mask True action [SetVariable('backpack_carry',True),SetVariable('uhl_fpb_cfs',True),Function(delete_hint,"You should perhaps try to get something to carry all these things you seem to be able to pick up..."),Jump('fp_bedroom_loc')]:
                yalign .7
                xalign .7
        if int(current_time[:2]) == 22 or int(current_time[:2]) == 23 or current_time[:2] == 0 or int(current_time[:2]) == 1:
            imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_night_bed_glow_%s.png" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]
        else:
            imagebutton auto ("images/backgrounds/interactions_item/fp_bedroom_night_bed_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/fp_bedroom_morning_bed_%s.png") focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]

        if not carry_phone:
            if int(current_time[:2]) in night:
                $ phoneimg = "images/backgrounds/interactions_item/fp_bedroom_night_phone_%s.png"
            elif int(current_time[:2]) == 22 or int(current_time[:2]) == 23 or current_time[:2] == 0 or int(current_time[:2]) == 1:
                $ phoneimg = "images/backgrounds/interactions_item/fp_bedroom_night_phone_glow_%s.png"
            else:
                $ phoneimg = "images/backgrounds/interactions_item/fp_bedroom_morning_phone_%s.png"
            imagebutton auto phoneimg focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('phone_added',True),Jump('fp_bedroom_loc')]
        if not renpy.get_screen('say'):
            $ exitdown_event_var = "uhl_cfs"
            $ exitdown_event = "upper_hallway_loc"
            $ exitdown = "Upper hallway"

    if room == "fs bedroom":
        if find_panties:
                imagebutton auto ("images/backgrounds/interactions_item/bedroom_panties_"+gp_bed+"_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/bedroom_panties_"+gp_bed+"_morning_%s.png") focus_mask True action [SetVariable('find_panties',False),SetVariable('panties_added',True),SetVariable('gp_bed',gp_bed),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if find_tablet:
            imagebutton auto ("images/backgrounds/interactions_item/fs_tablet_bedroom_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/fs_tablet_bedroom_morning_%s.png") focus_mask True action [SetVariable('find_tablet',False),SetVariable('tablet_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if find_pb:
            if not backpack.has_item(princessplug_item):
                imagebutton auto ("images/backgrounds/interactions_item/pink_buttplug_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/pink_buttplug_morning_%s.png") focus_mask True action [SetVariable('find_pb',False),SetVariable('pb_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if not renpy.get_screen('say'):
            $ exitdown_event_var = "uhl_cfs"
            $ exitdown_event = "upper_hallway_loc"
            $ exitdown = "Upper hallway"

    if room == "garage":
        if not backpack.has_item(toolbox_item):
            if int(current_time[:2]) in night:
                add "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_night_idle.png"
            elif not end_bike_repair:
                if not renpy.get_screen('say'):
                    imagebutton auto "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('toolbox_added',True),Jump('garage_loc')]
                else:
                    add "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_idle.png"
            else:
                if not renpy.get_screen('say'):
                    imagebutton auto "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]
                else:
                    add "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_idle.png"

        if int(current_time[:2]) not in night and not end_bike_repair and not mc_f:
            imagebutton auto "gui/tools_1_morning_%s.png" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('wmc_cfs',True),Jump('w_mc')]:
                xalign .5
                yalign .5

        $ exitleft_event = "entrance_loc"
        $ exitleft = "Upstairs / Entrance"

        if not renpy.get_screen('say'):
            $ exitdown_event_var = "out_cfs"
            $ exitdown_event = "outside_loc"
            $ exitdown = "Go outside"

    if room == "livingroom":
        $ exitright_event_var = "kit_cfs"
        $ exitright_event = "kitchen_loc"
        $ exitright = "Kitchen"
        if not renpy.get_screen('say'):
            $ exitdown_event = "entrance_loc"
            $ exitdown = "Entrance"

    if room == "kitchen":
        if wcount == 5:
            if bottles == 1 or br == 1 and int(current_time[:2]) in (day or night):
                imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.png") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',1),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                    ypos .485
                    xpos .31
            elif bottles == 2 or br == 2:
                imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.png") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                    ypos .485
                    xpos .31
                imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.png") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .325
            elif bottles == 3 or br == 3:
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.png") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .480
                        xpos .315
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.png") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.png") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .325

        $ exitleft_event_var = "lvr_cfs"
        $ exitleft_event = "livingroom_loc"
        $ exitleft = "Livingroom"
        if not renpy.get_screen('say'):
            $ exitdown_event = "entrance_loc"
            $ exitdown = "Entrance"

    if room == "outside":
        if not renpy.get_screen('say'):
            $ exitdown_event = "entrance_loc"
            $ exitdown = "Back into the house"
        $ exitleft_event_var = "gar_cfs"
        $ exitleft_event = "garage_loc"
        $ exitleft = "Garage"
        if mc_f:
            $ exitright_event = "beach_ride"
            $ exitright = "Go to the beach"

    if room == "upper hallway":
            imagebutton auto ("images/backgrounds/interactions_move/upper_hallway_fp_door_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upper_hallway_fp_door_morning_%s.png") focus_mask True action [SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]:
                tooltip "Enter your room"
            if fs_rel >= 40 or fs_invitation:
                imagebutton auto ("images/backgrounds/interactions_move/upper_hallway_fs_door_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upper_hallway_fs_door_morning_%s.png") focus_mask True action [SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]:
                    tooltip "Enter [fsName.yourformal]'s room"
            else:
                imagebutton idle ("images/backgrounds/interactions_move/upper_hallway_fs_door_night_idle.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upper_hallway_fs_door_morning_idle.png") focus_mask True action NullAction():
                    tooltip "You need a relationship of 40+ with [fsName.yourformal], or an invitation, to enter her room"
            imagebutton auto ("images/backgrounds/interactions_move/upper_hallway_bathroom_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upper_hallway_bathroom_morning_%s.png") focus_mask True action [SetVariable('uhl_bl_cfs',True),Jump('upper_hallway_bathroom_loc')]:
                tooltip "Enter bathroom"
            imagebutton auto ("images/backgrounds/interactions_move/stairs_down_night_%s.png" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/stairs_down_morning_%s.png") focus_mask True action Jump('entrance_loc'):
                tooltip "Downstairs"

    if room == "upper hallway bathroom" or room == "upper hallway bathroom peek":
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
            if room == "upper hallway bathroom":
                imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_shower_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("fpshower",True),Jump('upper_hallway_bathroom_loc')]
                imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_sink_morning_%s.png" focus_mask True action [SetVariable('uhl_bl_cfs',True),SetVariable("fpsink",True),Jump('upper_hallway_bathroom_loc')]
            add "images/backgrounds/interactions_item/bathroom_lightswitch_morning_off_idle.png"
        if not renpy.get_screen('say'):
            $ exitdown_event_var = "uhl_cfs"
            $ exitdown_event = "upper_hallway_loc"
            $ exitdown = "Upper hallway"

    if exitdown:
        if exitdown_event_var:
            if current_location == 'upper_hallway_bathroom_loc' and (bathroom_panties_added or fpshower):
                imagebutton auto "gui/exit_down_%s.png" focus_mask True action [SetVariable('fpshower',False),SetVariable('bathroom_panties_added',False),SetVariable('bathroom_find_panties',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
            elif current_location == 'fs_bedroom_loc' and (panties_added or pb_added):
                if panties_added and not pb_added:
                    imagebutton auto "gui/exit_down_%s.png" focus_mask True action [SetVariable('panties_added',False),SetVariable('find_panties',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
                elif not panties_added and pb_added:
                    imagebutton auto "gui/exit_down_%s.png" focus_mask True action [SetVariable('pb_added',False),SetVariable('find_pb',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
                else:
                    imagebutton auto "gui/exit_down_%s.png" focus_mask True action [SetVariable('pb_added',False),SetVariable('find_pb',True),SetVariable('panties_added',False),SetVariable('find_panties',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
            else:
                imagebutton auto "gui/exit_down_%s.png" focus_mask True action [SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
        else:
            if current_location == 'kitchen_loc' and wine_added:
                imagebutton auto "gui/exit_down_%s.png" focus_mask True action [SetVariable('wine_added',False),Jump(exitdown_event)]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
            else:
                imagebutton auto "gui/exit_down_%s.png" focus_mask True action Jump(exitdown_event):
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
    if exitleft:
        if exitleft_event_var:
            if current_location == 'kitchen_loc' and wine_added:
                imagebutton auto "gui/exit_left_%s.png" focus_mask True action [SetVariable('wine_added',False),SetVariable(exitleft_event_var,True),Jump(exitleft_event)]:
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
            else:
                imagebutton auto "gui/exit_left_%s.png" focus_mask True action [SetVariable(exitleft_event_var,True),Jump(exitleft_event)]:
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
        else:
            if current_location == 'kitchen_loc' and wine_added:
                imagebutton auto "gui/exit_left_%s.png" focus_mask True action [SetVariable('wine_added',False),Jump(exitleft_event)]:
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
            else:
                imagebutton auto "gui/exit_left_%s.png" focus_mask True action Jump(exitleft_event):
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
    if exitup:
        if exitup_event_var:
            imagebutton auto "gui/exit_up_%s.png" focus_mask True action [SetVariable(exitup_event_var,True),Jump(exitup_event)]:
                xalign .5
                yalign 0.0
                tooltip exitup
        else:
            imagebutton auto "gui/exit_up_%s.png" focus_mask True action Jump(exitup_event):
                xalign .5
                yalign 0.0
                tooltip exitup
    if exitright:
        if exitright_event_var:
            imagebutton auto "gui/exit_right_%s.png" focus_mask True action [SetVariable(exitright_event_var,True),Jump(exitright_event)]:
                xalign 1.0
                yalign .5
                tooltip exitright
        else:
            imagebutton auto "gui/exit_right_%s.png" focus_mask True action Jump(exitright_event):
                xalign 1.0
                yalign .5
                tooltip exitright

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

screen phone():
    modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    if persistent.phone_firstshow:
        on 'show' action [SetVariable('show_icons',False),Show('phone_info_screen')]
    $ keyclose = True
    fixed:
        maximum 370,686
        xalign .5
        yalign .5
        add "gui/phone_background_black.png" at ModZoom(.85):
            yalign .5
            xalign .5
        vbox: #notification-bar
            xalign .5
            yalign .5
            if battery_text != 0:
                add "gui/phone_notification_bar.png" at ModZoom(.85)
        hbox: #battery-indicator
            xalign .5
            yalign .5
            if battery_text != 0:
                if battery_text == 100:
                    add "gui/phone_battery_100.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 100 and battery_text >= 90:
                    add "gui/phone_battery_90.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 90 and battery_text >= 80:
                    add "gui/phone_battery_80.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 80 and battery_text >= 70:
                    add "gui/phone_battery_70.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 70 and battery_text >= 60:
                    add "gui/phone_battery_60.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 60 and battery_text >= 50:
                    add "gui/phone_battery_50.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 50 and battery_text >= 40:
                    add "gui/phone_battery_40.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 40 and battery_text >= 30:
                    add "gui/phone_battery_30.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 30 and battery_text >= 20:
                    add "gui/phone_battery_20.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 20 and battery_text >= 10:
                    add "gui/phone_battery_10.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                else:
                    add "gui/phone_battery_0.png" at ModZoom(.85):
                        xalign .5
                        yalign .5

        hbox: #clock
            if battery_text != 0:
                xalign .5
                yalign 0.0
                yoffset -10
                text "[current_time]":
                    font "gui/fonts/texgyreheroes_regular.otf"
                    size 18
                    color "#000"
        hbox: #battery-text
            if battery_text != 0:
                xalign 1.0
                xoffset -34
                yalign 0.0
                yoffset -6
                text "[battery_text]":
                    font "gui/fonts/texgyreheroes_regular.otf"
                    size 13
                    color "#000"
        hbox:
            if battery_text != 0:
                xalign .5
                xoffset 3
                yalign 0.0
                yoffset 20
                spacing 12
                xsize 370
                if show_icons:
                    imagebutton auto "gui/phone_button_achievement_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('display_achievements')] at ModZoom(.9):
                        tooltip "Open the achievement-screen"
                    imagebutton auto "gui/phone_button_gallery_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('phone_gallery_screen')] at ModZoom(.9):
                        tooltip "Open the image gallery"
                    imagebutton auto "gui/phone_button_call_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('phone_call_screen')] at ModZoom(.9):
                        tooltip "Phonecalls happen here"
                    imagebutton auto "gui/phone_button_help_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('phone_info_screen')] at ModZoom(.9):
                        tooltip "Open the in-game help-screen"
                    if len(hints) > 0:
                        imagebutton auto "gui/phone_button_hint_redglow_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('phone_hint_screen')] at ModZoom(.9):
                            tooltip "New hints available"
                    elif len(read_hints) > 0:
                        imagebutton auto "gui/phone_button_hint_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('phone_hint_screen',None,'read')] at ModZoom(.9):
                            tooltip "No new hints available"
                    else:
                        imagebutton idle "gui/phone_button_hint_insensitive.png" focus_mask True action NullAction() at ModZoom(.9):
                            tooltip "No hints available at the current time"
        hbox:
            if battery_text != 0:
                xalign .5
                xoffset 3
                yalign 0.1
                yoffset 30
                spacing 12
                xsize 370
                if show_icons:
                    imagebutton auto "gui/phone_button_text_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('phone_text_screen')] at ModZoom(.9):
                        tooltip "Read your messages"
                        xalign .5
                        xoffset 4

        hbox:
            if battery_text != 0:
                xalign 0.5
                xoffset 3
                yalign 1.0
                yoffset -24
                spacing 12
                if show_icons:
                    imagebutton auto "gui/phone_button_menu_%s.png" focus_mask True action [SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'mainmenu')] at ModZoom(.9):
                        tooltip "Go to the main menu"
                    imagebutton auto "gui/phone_button_save_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('custom_save')] at ModZoom(.9):
                        tooltip "Save your game"
                    imagebutton auto "gui/phone_button_load_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('custom_load')] at ModZoom(.9):
                        tooltip "Load your game"
                    imagebutton auto "gui/phone_button_preferences_%s.png" focus_mask True action [SetVariable('pref_screen',True),SetVariable('show_icons',False),Show('custom_preferences')] at ModZoom(.9):
                        tooltip "Show preferences screen"
                    imagebutton auto "gui/phone_button_quit_%s.png" focus_mask True action [SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'quit')] at ModZoom(.9):
                        tooltip "Quit the game"
        vbox:
            add "gui/phone_white.png" at ModZoom(.85)
            xalign .5
            yalign .5
        vbox:
            xalign .5
            yalign .5
            imagebutton auto "gui/phone_white_power_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            if keyclose:
                key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
        vbox:
            xalign .5
            yalign .5
            if battery_text != 0:
                imagebutton auto "gui/phone_white_home_%s.png" focus_mask True:
                    at ModZoom(.85)
                    alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                    if renpy.get_screen('phonescreen'):
                        action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)]
                        tooltip "Go back to the home-screen"
                    else:
                        action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                        tooltip "Turn off the phone"

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

screen phone_hint_screen(hintselect='new'):
    tag phonescreen
    zorder 950
    $ keyclose = True
    frame:
        style_prefix "category"
        background None
        xpadding 0
        top_padding 35
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686
        hbox:
            textbutton "New" action [Show('phone_hint_screen',None,'new')]:
                xsize 185
                text_size 18
                selected hintselect == 'new'
            textbutton "Read" action [Show('phone_hint_screen',None,'read')]:
                xsize 185
                text_size 18
                selected hintselect == 'read'
        viewport:
            mousewheel True
            ypos 40
            vbox:
                if hintselect == 'new':
                    for hint in hints:
                        textbutton "[hint]" action Function(read_hint,hint):
                            text_color "#fff"
                            text_size 18
                elif hintselect == 'read':
                    for read_hint in read_hints:
                        textbutton "[read_hint]" action Function(disable_hint,read_hint):
                            text_color "#fff"
                            text_size 18
    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]

screen phone_text_screen():
    tag phonescreen
    modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    $ keyclose = True
    default char = False
    default msg = False
    fixed:
        maximum 370,686
        xalign .5
        yalign .5
        vbox:
            xalign .5
            yalign .5
            yoffset 20
            add "gui/phone_background_contacts.png" at ModZoom(.85)
        vbox: #notification-bar
            xalign .5
            yalign .5
            if battery_text != 0:
                add "gui/phone_notification_bar.png" at ModZoom(.85)
        hbox: #battery-indicator
            xalign .5
            yalign .5
            if battery_text != 0:
                if battery_text == 100:
                    add "gui/phone_battery_100.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 100 and battery_text >= 90:
                    add "gui/phone_battery_90.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 90 and battery_text >= 80:
                    add "gui/phone_battery_80.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 80 and battery_text >= 70:
                    add "gui/phone_battery_70.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 70 and battery_text >= 60:
                    add "gui/phone_battery_60.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 60 and battery_text >= 50:
                    add "gui/phone_battery_50.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 50 and battery_text >= 40:
                    add "gui/phone_battery_40.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 40 and battery_text >= 30:
                    add "gui/phone_battery_30.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 30 and battery_text >= 20:
                    add "gui/phone_battery_20.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 20 and battery_text >= 10:
                    add "gui/phone_battery_10.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                else:
                    add "gui/phone_battery_0.png" at ModZoom(.85):
                        xalign .5
                        yalign .5

        hbox: #clock
            if battery_text != 0:
                xalign .5
                yalign 0.0
                yoffset -10
                text "[current_time]":
                    font "gui/fonts/texgyreheroes_regular.otf"
                    size 18
                    color "#000"
        hbox: #battery-text
            if battery_text != 0:
                xalign 1.0
                xoffset -34
                yalign 0.0
                yoffset -6
                text "[battery_text]":
                    font "gui/fonts/texgyreheroes_regular.otf"
                    size 13
                    color "#000"
        frame:
            background None
            xpadding 0
            top_padding 50
            bottom_padding 40
            xalign .5
            yalign .5
            maximum 370,686
            minimum 370,686
            vbox:
                ysize 20
                xsize 370
                yalign 0.0
                yoffset -20
                text "{b}All Messages{/b}":
                    text_align .5
                    xalign .5
                    color "#fff"
                    size 20
            viewport:
                mousewheel True
                ypos 28
                vbox:
                    $ c = 0
                    style_prefix "contacts"
                    for k,b,v in text_msg_received:
                        if c % 2:
                            $ bg_color_text = '#ddd'
                        else:
                            $ bg_color_text = '#ccc'
                        if not k == 'fp':
                            if k == 'fm':
                                $ charimg = "images/characters/anne/anne_idle.png"
                                $ charimg_hover = "images/characters/anne/anne_hover.png"
                            elif k == 'fs':
                                $ charimg = "images/characters/juliette/juliette_idle.png"
                                $ charimg_hover = "images/characters/juliette/juliette_hover.png"
                            elif k == 'nk':
                                $ charimg = "images/characters/karen/karen_idle.png"
                                $ charimg_hover = "images/characters/karen/karen_hover.png"
                            elif k == 'nr':
                                $ charimg = "images/characters/ron/ron_idle.png"
                                $ charimg_hover = "images/characters/ron/ron_hover.png"
                            else:
                                $ charimg = "gui/question_mark_idle.png"
                                $ charimg_hover = "gui/question_mark_hover.png"

                            button:
                                if char == k:
                                    background "#fff"
                                else:
                                    background bg_color_text
                                hover_background "#fff"
                                ysize 50
                                xsize 370
                                xpadding 0
                                hbox:
                                    if char == k:
                                        add charimg_hover at ModZoom(.40):
                                            yalign .5
                                    else:
                                        add charimg at ModZoom(.40):
                                            yalign .5
                                    text "[b]":
                                        ysize 50
                                        yalign .5
                                        if char == k:
                                            color "#0cf"
                                        else:
                                            color "#444"
                                        hover_color "#0cf"
                                if char and msg:
                                    action [SetScreenVariable('char',False),SetScreenVariable('msg',False)]
                                else:
                                    action [SetScreenVariable("char",k),SetScreenVariable('msg',v),Function(set_hint,"You've gotten the info from "+nr.name+" - unfortunately, that's as far as this storyline goes for now")]
                                    hovered [SetScreenVariable("char",k),SetScreenVariable('msg',False)]
                                    unhovered [SetScreenVariable("char",False),SetScreenVariable('msg',False)]
                                if msg:
                                    frame:
                                        xsize 390
                                        xalign .5
                                        ypos 40
                                        background "#0cf"
                                        text "[msg]"
                        $ c += 1
                    if not text_msg_received:
                        hbox:
                            xsize 370
                            xalign .5
                            yalign .5
                            text "No text-messages received yet":
                                color "#444"
                                xalign .5
                                text_align .5
                                size 20
        vbox:
            add "gui/phone_white.png" at ModZoom(.85)
            xalign .5
            yalign .5
        vbox:
            xalign .5
            yalign .5
            imagebutton auto "gui/phone_white_power_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            if keyclose:
                key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
        vbox:
            xalign .5
            yalign .5
            if battery_text != 0:
                imagebutton auto "gui/phone_white_home_%s.png" focus_mask True:
                    at ModZoom(.85)
                    alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                    if renpy.get_screen('phonescreen'):
                        action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)]
                        tooltip "Go back to the home-screen"
                    else:
                        action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                        tooltip "Turn off the phone"

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]


screen phone_call_screen():
    tag phonescreen
    modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    $ keyclose = True
    default stats = None
    default clicked = None
    fixed:
        maximum 370,686
        xalign .5
        yalign .5
        vbox:
            xalign .5
            yalign .5
            yoffset 20
            add "gui/phone_background_contacts.png" at ModZoom(.85)
        vbox: #notification-bar
            xalign .5
            yalign .5
            if battery_text != 0:
                add "gui/phone_notification_bar.png" at ModZoom(.85)
        hbox: #battery-indicator
            xalign .5
            yalign .5
            if battery_text != 0:
                if battery_text == 100:
                    add "gui/phone_battery_100.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 100 and battery_text >= 90:
                    add "gui/phone_battery_90.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 90 and battery_text >= 80:
                    add "gui/phone_battery_80.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 80 and battery_text >= 70:
                    add "gui/phone_battery_70.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 70 and battery_text >= 60:
                    add "gui/phone_battery_60.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 60 and battery_text >= 50:
                    add "gui/phone_battery_50.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 50 and battery_text >= 40:
                    add "gui/phone_battery_40.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 40 and battery_text >= 30:
                    add "gui/phone_battery_30.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 30 and battery_text >= 20:
                    add "gui/phone_battery_20.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                elif battery_text < 20 and battery_text >= 10:
                    add "gui/phone_battery_10.png" at ModZoom(.85):
                        xalign .5
                        yalign .5
                else:
                    add "gui/phone_battery_0.png" at ModZoom(.85):
                        xalign .5
                        yalign .5

        hbox: #clock
            if battery_text != 0:
                xalign .5
                yalign 0.0
                yoffset -10
                text "[current_time]":
                    font "gui/fonts/texgyreheroes_regular.otf"
                    size 18
                    color "#000"
        hbox: #battery-text
            if battery_text != 0:
                xalign 1.0
                xoffset -34
                yalign 0.0
                yoffset -6
                text "[battery_text]":
                    font "gui/fonts/texgyreheroes_regular.otf"
                    size 13
                    color "#000"
        frame:
            background None
            xpadding 0
            top_padding 50
            bottom_padding 40
            xalign .5
            yalign .5
            maximum 370,686
            minimum 370,686
            vbox:
                ysize 20
                xsize 370
                yalign 0.0
                yoffset -20
                text "{b}All Contacts{/b}":
                    text_align .5
                    xalign .5
                    color "#fff"
                    size 20
            viewport:
                mousewheel True
                ypos 28
                vbox:
                    style_prefix "contacts"
                    $ c = 0
                    for i in chars:
                        if c % 2:
                            $ bg_color_contacts = '#ddd'
                        else:
                            $ bg_color_contacts = '#ccc'
                        if not i[1] == 'fp':
                            if i[1] == 'fm':
                                $ charimg = "images/characters/anne/anne_idle.png"
                                $ charimg_hover = "images/characters/anne/anne_hover.png"
                            elif i[1] == 'fs':
                                $ charimg = "images/characters/juliette/juliette_idle.png"
                                $ charimg_hover = "images/characters/juliette/juliette_hover.png"
                            elif i[1] == 'nk':
                                $ charimg = "images/characters/karen/karen_idle.png"
                                $ charimg_hover = "images/characters/karen/karen_hover.png"
                            elif i[1] == 'nr':
                                $ charimg = "images/characters/ron/ron_idle.png"
                                $ charimg_hover = "images/characters/ron/ron_hover.png"
                            else:
                                $ charimg = "gui/question_mark_idle.png"
                                $ charimg_hover = "gui/question_mark_hover.png"

                            button:
                                background bg_color_contacts
                                hover_background "#fff"
                                ysize 80
                                xsize 370
                                hbox:
                                    ysize 80
                                    spacing 10
                                    if stats == i:
                                        add charimg_hover at ModZoom(.65):
                                            yalign .5
                                            yoffset -10
                                        text "[i[0]]":
                                            ysize 80
                                            yalign .5
                                            yoffset -10
                                            color "#0cf"
                                    else:
                                        add charimg at ModZoom(.65):
                                            yalign .5
                                            yoffset -10
                                        text "[i[0]]":
                                            ysize 80
                                            yalign .5
                                            yoffset -10
                                            color "#777"
                                hovered SetScreenVariable("stats",i)
                                unhovered SetScreenVariable("stats",False)
                                # action NullAction()
                                action Show('warning_screen',None,300,370,"There are no functionality for the call-screen at the current time")
                        $ c += 1
        vbox:
            add "gui/phone_white.png" at ModZoom(.85)
            xalign .5
            yalign .5
        vbox:
            xalign .5
            yalign .5
            imagebutton auto "gui/phone_white_power_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            if keyclose:
                key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
        vbox:
            xalign .5
            yalign .5
            if battery_text != 0:
                imagebutton auto "gui/phone_white_home_%s.png" focus_mask True:
                    at ModZoom(.85)
                    alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                    if renpy.get_screen('phonescreen'):
                        action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)]
                        tooltip "Go back to the home-screen"
                    else:
                        action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                        tooltip "Turn off the phone"

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]


screen warning_screen(height=0,width=0,txt=False):
    zorder 980
    if txt:
        frame:
            xalign .5
            yalign .5
            xsize width
            ysize height
            text txt:
                color "#fff"
                yalign .5
                xalign .5


screen phone_gallery_screen():
    tag phonescreen
    zorder 950
    $ keyclose = True
    frame:
        background None
        xpadding 0
        top_padding 40
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686
        $ pgsxp = 0
        $ pgsyp = 0
        $ pgs = 0
        viewport:
            mousewheel True
            vbox:
                for file in renpy.list_files():
                    if file.startswith('images/phone_gallery/') and file.endswith('.png'):
                        $ name = file.replace('images/phone_gallery/','')
                        if name in images_unlocked:
                            imagebutton idle Transform(file,maxsize=(215,215)):
                                xpos pgsxp
                                if not 'portrait' in name:
                                    ypos pgsyp +50
                                else:
                                    ypos pgsyp
                                action [SetVariable('current_file',file),SetVariable('show_icons',False),Hide('phone_gallery_screen'),Show('phone_gallery_show')]
                        else:
                            imagebutton idle Transform(file,maxsize=(215,215),alpha=.2):
                                xpos pgsxp
                                if not 'portrait' in name:
                                    ypos pgsyp +50
                                else:
                                    ypos pgsyp
                                # action [SetVariable('current_file',file),SetVariable('show_icons',False),Hide('phone_gallery_screen'),Show('phone_gallery_show')]
                                action NullAction()
                        if 'portrait' in name:
                            $ pgsxp += 125
                        else:
                            $ pgsxp += 215
                        if not 'portrait' in name:
                            $ pgsyp -= 115
                        else:
                            $ pgsyp -= 215
                        if 'portrait' in name:
                            $ pgs += 1
                        else:
                            $ pgs += 2
                        if pgs >= 3:
                            $ pgs = 0
                            $ pgsxp = 0
                            $ pgsyp += 220
                if keyclose:
                    key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]

screen phone_gallery_show():
    tag phonescreen
    zorder 950
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    $ keyclose = True
    frame:
        style_prefix "infoscreen"
        background None
        xpadding 0
        top_padding 60
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686
        if current_file:
            $ filename = current_file
            button:
                add filename at Transform(maxsize=(410,700)):
                    xalign .5
                    yalign .5
                if imggal_showbuttons:
                    imagebutton auto "gui/imggal_close_%s.png" focus_mask None action[Hide('phone_gallery_show'),Show('phone_gallery_screen')] at ModZoom(.65):
                        ypos -30
                else:
                    imagebutton idle "gui/imggal_transparent_idle.png" focus_mask None action NullAction() at ModZoom(.65):
                        ypos -30
                action NullAction()
            if imggal_showbuttons:
                key "K_h" action SetVariable('imggal_showbuttons',False)
            else:
                key "K_h" action SetVariable('imggal_showbuttons',True)
    hbox:
        imagebutton auto "gui/phone_white_power_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
            tooltip "Shut off the phone"
        xalign .5
        yalign .5
        if keyclose:
            key "K_ESCAPE" action [SetVariable('keyclose',False),Function(hide_phone_screens),Show('phone'),Show('phone_gallery_screen')]
    hbox:
        if battery_text != 0:
            imagebutton auto "gui/phone_white_home_%s.png" focus_mask True action [SetVariable('keyclose',False),Function(hide_phone_screens),Show('phone_gallery_show')] at ModZoom(.85):
                tooltip "Go back to the home-screen"
                alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
            xalign .5
            yalign .5
    hbox:
        add "gui/phone_white.png" at ModZoom(.85)
        xalign .5
        yalign .5

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

screen phone_info_screen():
    tag phonescreen
    zorder 950
    $ keyclose = True
    if persistent.phone_firstshow:
        hbox:
            imagebutton:
                idle "gui/phone_white_power_hover.png"
                hover "gui/phone_white_power_hover.png"
                focus_mask True
                action [SetField(persistent,'phone_firstshow',False),SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85)
                tooltip "Shut off the phone"
            xalign .5
            yalign .5
        hbox:
            if battery_text != 0:
                imagebutton:
                    idle "gui/phone_white_home_hover.png"
                    hover "gui/phone_white_home_hover.png"
                    focus_mask True
                    alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                    action [SetField(persistent,'phone_firstshow',False),SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)] at ModZoom(.85)
                    tooltip "Go back to the home-screen"
                xalign .5
                yalign .5
    frame:
        style_prefix "infoscreen"
        background None
        xpadding 0
        top_padding 60
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686
        viewport:
            mousewheel True
            vbox:
                text "This is the phone-screen. Here you'll find all the game-menus:\n"
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_menu_%s.png" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'mainmenu')] at ModZoom(.6):
                        yalign .5
                    textbutton "Main menu" action [Hide('phone_info_screen'),Show('custom_confirm',None,'mainmenu')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_save_%s.png" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),Show('custom_save')] at ModZoom(.6):
                        yalign .5
                    textbutton "Save" action [Hide('phone_info_screen'),Show('custom_save')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_load_%s.png" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),Show('custom_load')] at ModZoom(.6):
                        yalign .5
                    textbutton "Load" action [Hide('phone_info_screen'),Show('custom_load')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_preferences_%s.png" focus_mask True action [Hide('phone_info_screen'),SetVariable('pref_screen',True),SetVariable('show_icons',False),Show('custom_preferences')] at ModZoom(.6):
                        yalign .5
                    textbutton "Preferences" action [Hide('phone_info_screen'),Show('custom_preferences')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_quit_%s.png" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'quit')] at ModZoom(.6):
                        yalign .5
                    textbutton "Quit game" action [Hide('phone_info_screen'),Show('custom_confirm',None,'quit')]:
                        text_size 22
                        yalign .5
                text "\nand also different other screens, like the:\n"
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_achievement_%s.png" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),Show('display_achievements')] at ModZoom(.6):
                        yalign .5
                    textbutton "Achievement screen" action [Hide('phone_info_screen'),Show('display_achievements')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_gallery_%s.png" focus_mask True action [Hide('phone_info_screen'),Show('phone_gallery_screen')] at ModZoom(.6):
                        yalign .5
                    textbutton "Image gallery" action [Hide('phone_info_screen'),Show('phone_gallery_screen')]:
                        text_size 22
                        yalign .5
                hbox:
                    text "While in the gallery, you can click on images to show them in full screen on the phone. While viewing the full-screen image, there will be buttons to navigate and close (depending on amount of images) - to hide/show them, you can press \"h\"":
                        size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_call_%s.png" focus_mask True action [Hide('phone_info_screen'),Show('phone_call_screen')] at ModZoom(.6):
                        yalign .5
                    textbutton "Call screen" action [Hide('phone_info_screen'),Show('phone_call_screen')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_text_%s.png" focus_mask True action [Hide('phone_info_screen'),Show('phone_text_screen')] at ModZoom(.6):
                        yalign .5
                    textbutton "Message screen" action [Hide('phone_info_screen'),Show('phone_text_screen')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_help_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('phone_info_screen')] at ModZoom(.6):
                        yalign .5
                    textbutton "In-game help" action [SetVariable('show_icons',False),Show('phone_info_screen')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_hint_%s.png" focus_mask True action [SetVariable('show_icons',False),Show('phone_hint_screen')] at ModZoom(.6):
                        yalign .5
                    textbutton "Game-hints" action [SetVariable('show_icons',False),Show('phone_hint_screen')]:
                        text_size 22
                        yalign .5

                text "\nand more as the game is being developed.\n\nYou close the phone by pressing the power button on the right side of the phone, or by clicking the home-button when on the main screen. If there is an app / screen showing on the phone, the home button takes you back to the main screen. You can also use \"ESC\" to close screens, and the phone itself, if you're on the home-screen. Right-clicking on the home-button / long-pressing (if on touch-screen) (at any time) will close the phone"
    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetField(persistent,'phone_firstshow',False),Function(hide_phone_screens),SetVariable('show_icons',True),Show('phone')]

screen custom_confirm(cc_chosen=False):
    tag phonescreen
    zorder 900
    $ keyclose = True
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
            if keyclose:
                key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]

screen display_achievements():
    tag phonescreen
    modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    $ keyclose = True
    on 'show' action Function(achievement_trophy_case.update)

    use display_achievements_category_panel

    hbox:
        xalign .5
        yalign .5
        add "gui/phone_background_light.png" at ModZoom(.85)
    hbox: #notification-bar
        if battery_text != 0:
            add "gui/phone_notification_bar.png" at ModZoom(.85)
            xalign .5
            yalign .5
    hbox: #battery-indicator
        if battery_text != 0:
            if battery_text == 100:
                add "gui/phone_battery_100.png"
            elif battery_text < 100 and battery_text >= 90:
                add "gui/phone_battery_90.png"
            elif battery_text < 90 and battery_text >= 80:
                add "gui/phone_battery_80.png"
            elif battery_text < 80 and battery_text >= 70:
                add "gui/phone_battery_70.png"
            elif battery_text < 70 and battery_text >= 60:
                add "gui/phone_battery_60.png"
            elif battery_text < 60 and battery_text >= 50:
                add "gui/phone_battery_50.png"
            elif battery_text < 50 and battery_text >= 40:
                add "gui/phone_battery_40.png"
            elif battery_text < 40 and battery_text >= 30:
                add "gui/phone_battery_30.png"
            elif battery_text < 30 and battery_text >= 20:
                add "gui/phone_battery_20.png"
            elif battery_text < 20 and battery_text >= 10:
                add "gui/phone_battery_10.png"
            else:
                add "gui/phone_battery_0.png"
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
                color "#000"
    hbox: #clock
        if battery_text != 0:
            xalign .5
            yalign .177
            text "[current_time]":
                font "gui/fonts/texgyreheroes_regular.otf"
                size 18
                color "#000"
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
                $ i = 0
                for achievement in achievements:
                    if achievement.category in selected_category:
                        if achievement.hidden:
                            if show_hidden_achievements:
                                fixed:
                                    xsize 370
                                    ysize 100
                                    imagebutton auto "gui/achievement_%s.png" focus_mask True:
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
                                    add "gui/phone_hidden_idle.png":
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
                        # else:
                        elif not achievement.unlocked:
                            # if show_unlocked_achievements and show_locked_achievements:
                                # pass
                            # el
                            if show_unlocked_achievements: # or (show_unlocked_achievements and show_locked_achievements):
                                # if not achievement.unlocked:
                                fixed:
                                    xsize 370
                                    ysize 100
                                    imagebutton auto "gui/achievement_%s.png" focus_mask True:
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
                                    add "gui/phone_lock_idle.png":
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

                        elif achievement.unlocked:
                            if show_locked_achievements: # or (show_unlocked_achievements and show_locked_achievements):
                                # if achievement.unlocked:
                                fixed:
                                    xsize 370
                                    ysize 100
                                    imagebutton auto "gui/achievement_%s.png" focus_mask True:
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
                                    add "gui/phone_unlock_idle.png":
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
                                imagebutton auto "gui/achievement_%s.png" focus_mask True:
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
                                    add "gui/phone_unlock_idle.png":
                                        xpos 300
                                        ypos 35
                                elif not achievement.unlocked:
                                    add "gui/phone_lock_idle.png":
                                        xpos 300
                                        ypos 35
                                elif achievement.hidden:
                                    add "gui/phone_hidden_idle.png":
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
            imagebutton auto "gui/phone_white_power_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            xalign .5
            yalign .5
            if keyclose:
                key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]
        hbox:
            imagebutton auto "gui/phone_white_home_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)] at ModZoom(.85):
                tooltip "Go back to the home-screen"
                alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
            xalign .5
            yalign .5
        hbox:
            xalign .5
            yalign .5
            add "gui/phone_bottom_overlay.png" at ModZoom(.85)
        hbox:
            xalign .5
            yalign .818
            imagebutton auto "gui/phone_lock_%s.png":
                action ToggleVariable('show_unlocked_achievements')
                xpos -100
            imagebutton auto "gui/phone_unlock_%s.png":
                action ToggleVariable('show_locked_achievements')
                xalign .5
            imagebutton auto "gui/phone_hidden_%s.png":
                action ToggleVariable('show_hidden_achievements')
                xpos 100

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"


# This allows the user to view achievements based on their category
screen display_achievements_category_panel():
    tag phonescreen
    frame:
        style_prefix "category"
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
    python:
        show_length = len(achievement_notification_queue[0].name + achievement_notification_queue[0].description) * 0.1
        if show_length < 3.0:
            show_length = 3.0
        elif show_length > 7.0:
            show_length = 7.0

    frame:
        at achievement_transform
        padding 15,15
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
            text "{size=30}{color=#fff}HSS - High School Shenanigans is a story about a very hot summer, where you'll play as <your name here> (You can name your own character, but the default is \"Marten\", so let's just go with that for now). So, you play as Marten, on his last stretch of high school, aiming to finish school, have some fun, fix his bike, and take his dream cross-country trip on it - but first, there's the exams. And the hot chicks... (among them, his [fmName.role] and [fsName.role], who is both hot, and definitely part of his nighttime jerk-off sessions), the pool, the neighbor girl, and so much more - pretty much like there is in every teenager's life. You control what happens, who you eventually hook up with, what you end up doing with them, and so on and so forth. \n\n{b}Note that this is a very early Alpha-release, and that quite a lot of the events haven't been added yet, and those that have been, might abruptly end. The game is playable, but you won't reach a fulfilling conclusion as of yet!{/b}{/color}{/size}"
    textbutton "{size=25}{color=#fff}Click to continue{/click}{/size}":
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
            text "{size=30}{color=#fff}The story is purely fictional, and does not reflect the creator's worldview.\nWe do not condone, nor support the actions and opinions of the characters{/color}{/size}"


screen custom_save():
    tag phonescreen
    zorder 900
    $ keyclose = True
    use custom_file_slots(_("Save"))

screen custom_load():
    tag phonescreen
    zorder 900
    use custom_file_slots(_("Load"))

screen custom_preferences():
    tag phonescreen
    modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    $ keyclose = True
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
                        hbox:
                            yalign 0.0
                            xalign .5
                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"
                                text_color "#fff"
                                foreground "gui/button/check_[prefix_]foreground_white.png"

                if disabled_hints:
                    fixed:
                        xsize 370
                        ysize 200
                        hbox:
                            yalign 0.0
                            xalign .5
                            textbutton _("Restore hints"):
                                action Function(restore_hints)
                                style "mute_all_button"
                                text_color "#fff"
                                foreground "gui/button/check_[prefix_]foreground_white.png"
    frame:
        background None
        xalign .5
        yalign .5
        hbox:
            imagebutton auto "gui/phone_white_power_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            xalign .5
            yalign .5
        hbox:
            imagebutton auto "gui/phone_white_home_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)] at ModZoom(.85):
                tooltip "Go back to the home-screen"
                alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
            xalign .5
            yalign .5

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]

screen custom_file_slots(title):
    tag phonescreen
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    $ keyclose = True
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
                            add FileScreenshot(slot) xalign 0.5
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
    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]

style custom_page_label is gui_label
style custom_page_label_text is gui_label_text
style custom_page_button is gui_button
style custom_page_button_text is gui_button_text

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

style custom_slot_button:
    xsize 370
    ysize 330
    background "#f00"

style custom_slot_button_text:
    size 15
    color "#222"

screen fs_tablet():
    default ic_num_str = 0
    modal True
    zorder 800
    $ keyclose = True
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
            add "gui/tablet.png" at ModZoom(.85)
        hbox: #backgrounds
            yalign .5
            xalign .5
            if len(ic_num) == 4:
                $ ic_num_str = ''.join(map(str, ic_num))
                if int(ic_num_str) == tablet_stored_code:
                    $ tablet_code = True
                    $ ic_num = []
                    add "tablet_no_content_warning.png" at ModZoom(.85)
                else:
                    $ ic_num = []
            elif tablet_code:
                add "gui/tablet_background.png" at ModZoom(.85)
        hbox:
            xalign .5
            yalign .5
            imagebutton auto "gui/tablet_power_%s.png" focus_mask True action [SetVariable('keyclose',False),SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()] at ModZoom(.85)
            if keyclose:
                key 'K_ESCAPE' action [SetVariable('keyclose',False),Hide('phone_info_screen'),SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()]

        if not tablet_code:
            hbox:
                imagemap:
                    alpha False
                    if len(ic_num) == 1:
                        add "gui/tablet_unlock_1.png"
                    elif len(ic_num) == 2:
                        add "gui/tablet_unlock_2.png"
                    elif len(ic_num) == 3:
                        add "gui/tablet_unlock_3.png"
                    elif len(ic_num) == 4:
                        add "gui/tablet_unlock_4.png"
                    ground "gui/tablet_unlock.png"
                    hover "gui/tablet_unlock_hover.png"
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

screen maininfo():
    frame:
        if persistent.maininfo:
            style_prefix "infoscreen"
            xalign .5
            yalign .5
            xsize 800
            ysize 800
        else:
            background None
            xpadding 0
            top_padding 40
            bottom_padding 10
            xalign .5
            yalign .44
            maximum 370,686
        $ keyclose = True
        viewport:
            mousewheel True
            vbox:
                text "{b}{size=40}How to play{/size}{/b}\n":
                    xalign .5
                text "This game is not a VN. It's more of a sandbox, where you can roam semi-freely around the environment, and do what you please, more or less, with choices depending on what you know and what you've experienced. Of course, there are events that are fully scripted, of which you have no real control (apart from deciding what to do, when).\n"
                text "You will need to apply some adventure-game playstyles - first of all, there are outlines on everything you can pick up, look at and otherwise interact with - it will light up blue when hovered if you can interact with it. If you're stuck in a screen, or can't find anything worth doing, revisit and make sure you check every item.\n"
                text "{b}The regular quick menu and even the regular right-click menu / ESC-menu has been disabled. They have been replaced by an in-game menu (which you will have to find the appropriate item to be able to use). The same goes for the inventory (also an item you need to pick up to be able to use).{/b}\n"
                text "There will be short info-screens for the different objects you can pick up and use in particular ways as well, as the game progresses.\n"
                text "Up left you have a button for\n ":
                    justify True
                textbutton "{u}stats for each NPC{/u}":
                    text_size 20
                    ypos -58
                    xpos 318
                    action NullAction()
                    hovered Function(info_hover,"stats_hover","show")
                    unhovered Function(info_hover,"stats_hover")
                text " you meet in-game":
                    ypos -94
                    xpos 520
                    justify True
                text "and a":
                    ypos -94
                textbutton "{u}t-shirt{/u}":
                    text_size 20
                    ypos -128
                    xpos 58
                    action NullAction()
                    hovered Function(info_hover,"tshirt_overlay","show")
                    unhovered Function(info_hover,"tshirt_overlay")
                text "which changes color based on how dirty you are. If you get too dirty, you will not be able to interact with some of the people in game, and you will have to clean up to progress the story and events.\n":
                    ypos -164
                    first_indent 130
                text "Up to the right there is a calendar, showing month, date, weather, day and time. {b}The time / clock is clickable, to advance time - clicking on the hour advances time by 1 hour, clicking on the minutes advances time by 30 minutes{/b}\n":
                    ypos -170
                if persistent.maininfo:
                    text "{color=#f00}{size=28}Once closed, this infoscreen will not show again like this, but the info will be available via the help-screen in-game.{/size}{/color}":
                        xalign .5
                        ypos -180
        if persistent.maininfo:
            imagebutton auto "gui/closebutton_%s.png" xalign 1.0 yalign 1.0 focus_mask True action [SetField(persistent,'maininfo',False),Hide("maininfo"),Return()]
            if keyclose:
                key 'K_ESCAPE' action [SetVariable('keyclose',False),Hide('phone_info_screen'),SetField(persistent,'maininfo',False),Hide("maininfo"),Return()]

init python:
    def dd_cursor_position(st, at):
        x, y = renpy.get_mouse_pos()
        return Text("{size=-5}%d-%d" % (x, y)), .1

screen debug_tools():
    zorder 999
    add DynamicDisplayable(dd_cursor_position)