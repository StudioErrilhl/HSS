screen empty()

screen choice(items):
    style_prefix "choice"
    default evilexists = False
    default goodexists = False
    default choicestatus = None

    vbox:
        yalign .8
        spacing 20
        $ e = 0
        $ g = 0
        for caption, action, chosen in items:
            if action:
                if "(evil)" in caption:
                    $ caption = caption.replace(" (evil)","")
                    $ choicestatus = 'evil'
                elif "(good)" in caption:
                    $ caption = caption.replace(" (good)","")
                    $ choicestatus = 'good'
                if conditions.check(caption):
                    button:
                        # style "choice_button"
                        if choicestatus == 'evil':
                            if e <= 0:
                                ypos 300
                            xpos -50
                            text conditions.text(caption) style "choice_button_disabled_evil":
                                xpos 40
                            $ caption = caption+" (evil)"
                        elif choicestatus == 'good':
                            xpos 50
                            text conditions.text(caption) style "choice_button_disabled_good"
                            $ caption = caption+" (good)"
                        else:
                            text conditions.text(caption) style "choice_button_disabled"
                    if choicestatus == 'evil' and e <= 0:
                        add "gui/demon.webp" at ModZoom(.4):
                            ypos 20
                            xoffset -50
                            xalign 0.0
                        $ e += 1
                    elif choicestatus == 'good' and g <= 0:
                        add "gui/angel.webp" at ModZoom(.4):
                            ypos -260
                            xoffset 50
                            xalign 1.0
                        $ g += 1
                    $ choicestatus = None

                else:
                    button:
                        # style "choice_button"
                        if choicestatus == "evil":
                            if e <= 0:
                                ypos 300
                            xpos -50
                            text caption style "choice_button_evil":
                                xpos 40
                            $ caption = caption+" (evil)"
                        elif choicestatus == "good":
                            xpos 50
                            text caption style "choice_button_good"
                            $ caption = caption+" (good)"
                        else:
                            text caption style "choice_button"
                        action [SetScreenVariable('evilexists',False),SetScreenVariable('goodexists',False),action]
                    if choicestatus == 'evil' and e <= 0:
                        add "gui/demon.webp" at ModZoom(.4):
                            ypos 20
                            xoffset -50
                            xalign 0.0
                        $ e += 1
                    elif choicestatus == 'good' and g <= 0:
                        add "gui/angel.webp" at ModZoom(.4):
                            ypos -260
                            xoffset 50
                            xalign 1.0
                        $ g += 1
                    $ choicestatus = None
            else:
                frame:
                    background "gui/textbox_top.webp"
                    xalign .5
                    xpos -50
                    ypos -650
                    hbox:
                        xalign .5
                        text caption:
                            xpos 650
                            ypos 20

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

screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            if gui.about:
                text "[gui.about!t]\n"
            if gui.about_2_head:
                text "[gui.about_2_head!t]" at center
            if gui.about_2_text:
                text "[gui.about_2_text!t]"

            text _("{size=24}Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]{/size}")

screen load():
    tag menu
    use file_slots(_("Continue"))

screen navigation():
    vbox:
        style_prefix "prefs"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Continue") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Changelog") action ShowMenu("changelog")
        textbutton _("Help") action ShowMenu("help")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        if renpy.variant("pc") and not main_menu:
            textbutton _("Help") action ShowMenu("help")
            textbutton _("Quit") action Quit(confirm=not main_menu)

screen main_menu():
    tag menu

    if main_menu:
        imagemap:
            ground "gui/menu.webp"
            hover "gui/menu_hover.webp"

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
            idle "gui/patreon_idle.webp"
            hover "gui/patreon_hover.webp"
            action OpenURL("./game/test.html")

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
                        pagekeys True
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
                        pagekeys True
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


screen ingame_menu_display(day_week=day_week,current_month=current_month,current_month_day=current_month_day,current_time=current_time):
    # tag menu
    zorder 300
    default x = 500
    default y = 400
    ## Get mouse coords:
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    hbox xalign 0 yalign 0:
        imagebutton auto "gui/stats_%s.webp" focus_mask True action Show('stat_screen'):
            tooltip "Here you'll find all the stats for all the characters in the game. Some characters doesn't have a lot of stats currently, this may change with the coming updates"
        add "gui/stats_overlay.webp":
            xpos -128
            if int(current_time[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5
        if filth_val == 0: ## filth-meter
            imagebutton idle "gui/tshirt.webp":
                xpos -150
                ypos 10
                tooltip "You're clean as a whistle"
                action NullAction()
            add "gui/tshirt_overlay.webp":
                ypos 10
                xpos -250
                if int(current_time[:2]) not in night:
                    alpha 0.0
                else:
                    alpha .5
        else:
            add "gui/tshirt.webp":
                xpos -150
                ypos 10
            imagebutton idle "gui/tshirt_overlay.webp":
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
            add "gui/tshirt_overlay.webp":
                ypos 10
                xpos -350
                if int(current_time[:2]) not in night:
                    alpha 0.0
                else:
                    alpha .5

    if not carry_backpack:
        add "gui/backpack_outline.webp"
    if carry_backpack:
        vbox xalign .99 yalign .99: #backpack / inventory
            imagebutton auto "gui/backpack_%s.webp":
                xalign 0.8
                ypos 100
                focus_mask True
                action [Show("inventory_screen")]
                tooltip "Here you'll be able to see what you have in your backpack"
            add "gui/backpack_overlay.webp":
                ypos -16
                if int(current_time[:2]) not in night:
                    alpha 0.0
                else:
                    alpha 0.0

    frame: ## phone-menu
        xpos 1720
        ypos 15
        xpadding 0
        ypadding 0
        background None
        vbox:
            if carry_phone:
                if not (hints or calls or messages):
                    imagebutton auto "gui/menu_phone_%s.webp" focus_mask True:
                        if renpy.get_screen('phone'):
                            action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),ToggleScreen('phone')]
                        else:
                            action [FileTakeScreenshot(),ToggleScreen('phone')]
                        at ModZoom(.8)
                        # tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more"
                elif calls:
                    imagebutton auto "gui/menu_phone_call_%s.webp" focus_mask True:
                        if renpy.get_screen('phone'):
                            action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),ToggleScreen('phone')]
                        else:
                            action [FileTakeScreenshot(),ToggleScreen('phone'),Show('')]
                        at ModZoom(.8)
                        # tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more. And right now, unanswered calls"
                elif messages:
                    imagebutton auto "gui/menu_phone_message_%s.webp" focus_mask True:
                        if renpy.get_screen('phone'):
                            action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),ToggleScreen('phone')]
                        else:
                            action [FileTakeScreenshot(),ToggleScreen('phone')]
                        at ModZoom(.8)
                        # tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more. And right now, new messages"
                elif hints:
                    imagebutton auto "gui/menu_phone_hint_%s.webp" focus_mask True:
                        if renpy.get_screen('phone'):
                            action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),ToggleScreen('phone')]
                        else:
                            action [FileTakeScreenshot(),ToggleScreen('phone')]
                        at ModZoom(.8)
                        # if tooltipcounterforphone <= 5:
                        #     tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more. And right now, new hints"

                add "gui/menu_phone_overlay.webp" at ModZoom(.87):
                    yoffset -134
                    xoffset -4.5
                    if int(current_time[:2]) not in night:
                        alpha 0.0
                    else:
                        alpha .5
            else:
                add "gui/menu_phone_outline.webp" at ModZoom(.8)

    frame: #calendar_display
        xpos 1810
        xpadding 0
        ypadding 0
        background Image("gui/calendar.webp")
        vbox: #month and date and dayname
            xsize 100
            xalign .5
            $ current_day = week_days[day_week]
            $ current_month = months_days[current_month][0]
            $ current_month_day = current_month_day
            text "[current_month]":
                xalign .5
                color "#fff"
                size 20
            textbutton "[current_month_day]":
                xalign .5
                text_color "#000"
                ypos -5
                padding 0,0
                text_size 55
                action [Function(addday,1),Jump('day_start')] focus_mask None
            if bad_weather and rainstorm and int(current_time[:2]) in night:
                add "gui/night_rain_icon.webp":
                    xalign .5
                    ypos -15
            elif bad_weather and rainstorm:
                add "gui/morning_rain_icon.webp":
                    xalign .5
                    ypos -15
            elif int(current_time[:2]) in night:
                add "gui/night_icon.webp":
                    xalign .5
                    ypos -15
            else:
                add "gui/sun_icon.webp":
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

            add "gui/calendar_overlay.webp":
                ypos -140
                if int(current_time[:2]) not in night:
                    alpha 0.0
                else:
                    alpha 0.5

    frame: #clock-display
        xpos 1810
        ysize 30
        xsize 100
        ypos 120
        xpadding 0
        ypadding 0
        background Image('gui/clock_idle.webp')
        hbox: #hour-display
            xalign 0.0
            yalign .5
            $ hour = current_time[:2]
            textbutton "[hour]":
                text_color "#fff"
                text_font "gui/fonts/digital_dismay.otf"
                text_size 25
                action Function(addtime,1,False,True)
        hbox: #: - separates hours and minutes
            xalign .5
            yalign .5
            text ":":
                color "#ffffff"
                yoffset 1
                font "gui/fonts/digital_dismay.otf"
                size 34
        hbox: #minute-display
            xalign 1.0
            yalign .5
            $ minute = current_time[3:]
            textbutton "[minute]":
                text_color "#fff"
                text_font "gui/fonts/digital_dismay.otf"
                text_size 25
                action Function(addtime,False,30,True)

        add "gui/clock_overlay.webp":
            if int(current_time[:2]) not in night:
                alpha 0.0
            else:
                alpha 0.5

        if backpack.has_item(wallet_item):
            vbox:
                xsize 100
                ysize 30
                ypos 30
                if persistent.cheat:
                    textbutton "$ [fp_money]" action SetVariable('fp_money',int(math.floor(getattr(store,"fp_money")+100))):
                        text_size 20
                        yalign .5
                        xalign .5
                        text_color "#fff"
                else:
                    text "$ [fp_money]":
                        size 20
                        yalign .5
                        xalign .5

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
        if persistent.cheat:
            text "If you have enabled the cheat-mode, this will allow you to manipulate stats."
        imagebutton auto "gui/closebutton_%s.webp" xalign 1.0 yalign 1.0 focus_mask True action [SetVariable('keyclose',False),SetField(persistent,'statscreen_infotext',False),Hide("statscreen_infotext")]
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
        style_prefix "statscreen"
        xalign .5 ypos .1
        xsize 800
        ysize 800
        padding 40,40
        viewport:
            mousewheel True
            pagekeys True
            ysize 650
            # scrollbars "vertical"
            vpgrid:
                cols 6
                mousewheel True
                spacing 20
                scrollbars "vertical"
                for i in chars:
                    if i[1] == "fp":
                        imagebutton auto "images/characters/marten/marten_%s.webp" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable('setstate',i[1]),SetScreenVariable('stats',i)]:
                            hovered SetScreenVariable('stats',i)
                            if clicked:
                                selected clicked[1] == 'fp'
                            if not setstate == i[1]:
                                unhovered SetScreenVariable('stats',clicked)
                        text "[i[0]]" ypos 35
                    elif i[1] == "fs":
                        imagebutton auto "images/characters/juliette/juliette_%s.webp" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                            hovered SetScreenVariable("stats",i)
                            if clicked:
                                selected clicked[1] == 'fs'
                            if not setstate == i[1]:
                                unhovered SetScreenVariable("stats",clicked)
                        text "[i[0]]" ypos 35
                    elif i[1] == "fm":
                        imagebutton auto "images/characters/anne/anne_%s.webp" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                            hovered SetScreenVariable("stats",i)
                            if clicked:
                                selected clicked[1] == 'fm'
                            if not setstate == i[1]:
                                unhovered SetScreenVariable("stats",clicked)
                        text "[i[0]]" ypos 35
                    elif i[1] == "nk":
                        imagebutton auto "images/characters/karen/karen_%s.webp" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                            hovered SetScreenVariable("stats",i)
                            if clicked:
                                selected clicked[1] == 'nk'
                            if not setstate == i[1]:
                                unhovered SetScreenVariable("stats",clicked)
                        text "[i[0]]" ypos 35
                    elif i[1] == "nr":
                        imagebutton auto "images/characters/ron/ron_%s.webp" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable('setstate',i[1]),SetScreenVariable('stats',i)]:
                            hovered SetScreenVariable('stats',i)
                            if clicked:
                                selected clicked[1] == 'nr'
                            if not setstate == i[1]:
                                unhovered SetScreenVariable('stats',clicked)
                        text "[i[0]]" ypos 35
                    else:
                        imagebutton auto "gui/question_mark_%s.webp" focus_mask True action [SetScreenVariable('clicked',i),SetScreenVariable("setstate",i[1]),SetScreenVariable("stats",i)]:
                            hovered SetScreenVariable("stats",i)
                            if not setstate == i[1]:
                                unhovered SetScreenVariable("stats",clicked)
                        if i[1] == "sn" or i[1] == "sp":
                            text "[i[0]]" ypos 35
                        else:
                            text "[i[0]]" ypos 35
        imagebutton auto "gui/closebutton_%s.webp" xalign 1.0 yalign 1.0 focus_mask True action [SetVariable('keyclose',False),SetScreenVariable('stats',False),Hide("stat_screen")]
        if keyclose:
            key 'K_ESCAPE' action [SetVariable('keyclose',False),SetScreenVariable('stats',False),Hide("stat_screen")]

        if stats:
            vbox:
                xalign .5
                yalign 1.0
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
                    text "Bad: [fp_demon] | Good: [fp_angel]"
                elif stats[1] in ["nr","se","sp","sj","scn","scm"]:
                    text "Rel: ["+stats[1]+"_rel]"
                else:
                    hbox:
                        hbox:
                            xsize 200
                            text "Dom:"
                            text "["+stats[1]+"_dom]":
                                xpos 10
                        if persistent.cheat:
                            imagebutton auto "gui/minusbutton_small_%s.webp" focus_mask True action SetVariable(stats[1]+"_dom",math.floor(getattr(store,stats[1]+"_dom")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "gui/plusbutton_small_%s.webp" focus_mask True action SetVariable(stats[1]+"_dom",math.floor(getattr(store,stats[1]+"_dom")+1)):
                                ypos 5
                                xpos 50
                    hbox:
                        hbox:
                            xsize 200
                            text "Rel:"
                            text "["+stats[1]+"_rel]":
                                xpos 20
                        if persistent.cheat:
                            imagebutton auto "gui/minusbutton_small_%s.webp" focus_mask True action SetVariable(stats[1]+"_rel",math.floor(getattr(store,stats[1]+"_rel")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "gui/plusbutton_small_%s.webp" focus_mask True action SetVariable(stats[1]+"_rel",math.floor(getattr(store,stats[1]+"_rel")+1)):
                                ypos 5
                                xpos 50
                    hbox:
                        hbox:
                            xsize 200
                            text "Aro:"
                            text "["+stats[1]+"_aro]":
                                xpos 20
                        if persistent.cheat:
                            imagebutton auto "gui/minusbutton_small_%s.webp" focus_mask True action SetVariable(stats[1]+"_aro",math.floor(getattr(store,stats[1]+"_aro")-1)):
                                ypos 5
                                xpos 40
                            imagebutton auto "gui/plusbutton_small_%s.webp" focus_mask True action SetVariable(stats[1]+"_aro",math.floor(getattr(store,stats[1]+"_aro")+1)):
                                ypos 5
                                xpos 50
                    if getattr(store, ""+stats[1]+"_cor") > 10:
                        text "BJ: ["+stats[1]+"_bj] / 20"
                        text "Sex: ["+stats[1]+"_pussy] / 30"
                        text "Anal: ["+stats[1]+"_anal] / 40"

screen fullscreen_image(fullscreenimage=False):
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
        background "gui/inventory_background.webp"
        xalign .5 yalign .5
        xsize 1920
        ysize 1080
        xpadding 20
        ypadding 20
        $ i = 0
        if fullscreenimage:
            add fullscreenimage:
                xalign .5
                yalign .5

        textbutton "Close image" action [SetVariable('keyclose',False),Hide("fullscreen_image")] xalign .95 yalign 1.0
        imagebutton auto "gui/closebutton_%s.webp" xalign 1.0 yalign 1.0 focus_mask True action [SetVariable('keyclose',False),Hide("fullscreen_image")]
        if keyclose:
            key 'K_ESCAPE' action [SetVariable('keyclose',False),Hide("fullscreen_image")]


screen inventory_screen():
    zorder 970
    modal True
    $ keyclose = True
    default x = 500
    default y = 400
    default cb_hs = False
    ## Get mouse coords:
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    frame:
        style_prefix "infoscreen"
        background "gui/inventory_background.webp"
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
                # scrollbars None
                edgescroll 100,500
                mousewheel True
                pagekeys True
                spacing 5
                $ inv_list = inv_list_fetch()
                for name in sorted(inv_list):
                    if i % 2:
                        $ bg_c = "#565656"
                    else:
                        $ bg_c = "#414141"
                    for item in backpack:
                        if item.name.lower() == name:
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
                                        $ current_items = item.name.lower()
                                        add "images/inventory/outer_ring.webp"
                                        add "images/inventory/"+item.name+"_idle.webp":
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
                                    add "images/inventory/outer_ring_insensitive.webp":
                                        xalign .5
                                        yalign .5
                                    add "images/inventory/"+name+"_insensitive.webp":
                                        xalign .5
                                        xoffset -140
                                        yalign .5
                                hbox:
                                    xsize 375
                                    xpos 160
                                    ysize 160
                                    if 'fsp_' in name:
                                        $ ptmp = name.replace('fsp_','panties_').replace('_',' ').split(' ')
                                        if len(ptmp) == 2:
                                            $ pname = ptmp[0]+' - '+ptmp[1]
                                        elif len(ptmp) == 3:
                                            $ pname = str(ptmp[0]+' - '+ptmp[1]+' '+ptmp[2])
                                        else:
                                            $ pname = str(ptmp[0])
                                        $ displayname = pname.capitalize()
                                    else:
                                        $ displayname = name.replace('fs_','').replace('fsp_','panties_').replace('_',' ').capitalize()
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
                background Frame("images/inventory/outer_ring_large.webp")
                hbox:
                    xsize 158
                    vbox:
                        ysize 158
                        xsize 158
                        add "images/inventory/outer_ring.webp"
                    if selecteditem:
                        vbox:
                            ysize 158
                            xsize 158
                            xpos -158
                            add "images/inventory/"+selecteditem+"_idle.webp":
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
                                $ charge_batt_img = "gui/inventory_charge_phone_red_%s.webp"
                            elif battery_text <= 50:
                                $ charge_batt_img = "gui/inventory_charge_phone_orange_%s.webp"
                            else:
                                $ charge_batt_img = "gui/inventory_charge_phone_%s.webp"
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
                        else:
                            text "{b}{size=30}Here be dragons!{/size}{/b}" at center
                    vbox:
                        xsize 910
                        xpos -740
                        ypos 40
                        if selecteditemdesc:
                            text "[selecteditemdesc]":
                                justify True
                                text_align .5
                            if selecteditemname and selecteditemname.lower() == 'wallet':
                                text "\n\n{b}Total cash amount: $[fp_money]{/b}" at center

                        else:
                            text "Or, rather, you haven't selected anything yet. Yup. That was what I meant to say!" at center:
                                justify True
                                text_align .5


        button:
            xsize 330
            ysize 75
            yalign 1.0
            xalign 1.0
            padding 0,0
            hover_background "#ffffff"
            hbox:
                xsize 350
                ysize 75
                yalign .5
                xalign .5
                spacing 0
                text "Close inventory":
                    xsize 300
                    size 26
                    yalign .5
                    xalign .5
                    text_align .5
                    xoffset 10
                    # xpos -20
                    hover_color "#0cf"
                if cb_hs:
                    add "gui/closebutton_hover.webp" yalign .5 xpos 20
                else:
                    add "gui/closebutton_idle.webp" yalign .5 xpos 20
            action [SetVariable('selecteditemdesc',False),SetVariable('selecteditem',False),SetVariable('selecteditemname',False),SetVariable('selecteditemweight',False),SetVariable('selecteditemamount',False),SetVariable('keyclose',False),Hide("inventory_screen")]
            hovered [SetScreenVariable("cb_hs",True)]
            unhovered [SetScreenVariable("cb_hs",False)]

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

# style skip_frame is empty
# style skip_text is gui_text
# style skip_triangle is skip_text

# style skip_frame:
#     yalign .2
#     background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
#     padding gui.skip_frame_borders.padding

# style skip_text:
#     size gui.notify_text_size
#     color "#fff"

# style skip_triangle:
#     ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
#     ## glyph in it.
#     font "DejaVuSans.ttf"
#     color "#fff"

# style skip_triangle_call:
#     font "DejaVuSans.ttf"
#     color "#50AF00"

screen say(who, what):
    zorder 999
    style_prefix "say"
    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
                if who.upper() == fpinput.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_fp.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == fmName.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_fm.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == fsName.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_fs.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == nb.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_nb.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == nc.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_nc.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == nk.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_nk.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == nr.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_nr.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == sn.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_sn.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == sp.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_sp.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == sj.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_sj.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == unk_f.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_unkf.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                elif who.upper() == unk_m.name.upper():
                    style "namebox_char"
                    background Frame("gui/namebox_unkm.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

        if who is not None and what:
            background Image("gui/textbox_cutout.webp", xalign=0.5, yalign=1.0)
        elif not what:
            background Image("gui/textbox_transparent.webp", xalign=0.5,yalign=1.0)
        else:
            background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

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
                    if persistent.side_image_zoom:
                        add SideImage() xalign 1.0 yalign 1.0 at easeIn(.5)
                    else:
                        add SideImage() xalign 1.0 yalign 1.0
                else:
                    if persistent.side_image_zoom:
                        add SideImage() xalign .5 xpos 250 yalign 1.0 at easeIn(.5)
                    else:
                        add SideImage() xalign .5 xpos 250 yalign 1.0

# Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

# style window is default
# style say_label is default
# style say_dialogue is default
# style say_thought is say_dialogue

# style namebox is default
# style namebox_label is say_label

# style window:
#     xalign 0.5
#     xfill True
#     yalign gui.textbox_yalign
#     ysize gui.textbox_height
#     background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

# style namebox:
#     xpos gui.name_xpos
#     xanchor gui.name_xalign
#     xsize gui.namebox_width
#     ypos gui.name_ypos
#     ysize gui.namebox_height

#     background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
#     padding gui.namebox_borders.padding

# style namebox_char:
#     xpos gui.name_xpos
#     xanchor gui.name_xalign
#     xsize gui.namebox_width
#     ypos gui.name_ypos
#     ysize gui.namebox_height

#     padding gui.namebox_borders.padding

# style say_label:
#     properties gui.text_properties("name", accent=False)
#     xalign gui.name_xalign
#     yalign 0.5
#     color "#ffffff"

# style say_dialogue:
#     properties gui.text_properties("dialogue")
#     xpos gui.dialogue_xpos
#     xsize gui.dialogue_width
#     ypos gui.dialogue_ypos

screen location(room=False):
    $ print('room: '+room)
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
            imagebutton auto ("images/backgrounds/interaction_moves/front_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/front_door_morning_%s.webp") focus_mask True action [SetVariable('trans',True),SetVariable('out_cfs',True),Jump('outside_loc')]:
                tooltip "Go outside"
            imagebutton auto ("images/backgrounds/interaction_moves/kitchen_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/kitchen_door_morning_%s.webp") focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]:
                tooltip 'Kitchen'
            imagebutton auto ("images/backgrounds/interaction_moves/livingroom_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/livingroom_door_morning_%s.webp") focus_mask True action [SetVariable('lvr_cfs',True),Jump('livingroom_loc')]:
                tooltip "Livingroom"
            imagebutton auto ("images/backgrounds/interaction_moves/stairs_up_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/stairs_up_morning_%s.webp") focus_mask True action [SetVariable('uts_cfs',True),Jump('upstairs_topofstairs_loc')]:
                tooltip "Bedrooms / Bathroom"
            imagebutton auto ("images/backgrounds/interaction_moves/stairs_basement_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/stairs_basement_morning_%s.webp") focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]:
                tooltip "Downstairs / Garage"

    if room == "fp bedroom":
        if not backpack.has_item(schoolbooks_item):
            if int(current_time[:2]) in night:
                add "images/backgrounds/interaction_items/fp_bedroom_night_dresser_idle.webp"
            else:
                if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                    imagebutton auto ("images/backgrounds/interaction_items/fp_bedroom_night_dresser_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/fp_bedroom_morning_dresser_%s.webp") focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('schoolbooks_added',True),Jump('fp_bedroom_loc')]
        if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
            if not carry_backpack:
                imagebutton auto ("images/backgrounds/interaction_items/fp_bedroom_night_backpack_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/fp_bedroom_day_backpack_%s.webp") focus_mask True action [SetVariable('carry_backpack',True),SetVariable('uhl_fpb_cfs',True),Function(delete_hint,"You should perhaps try to get something to carry all these things you seem to be able to pick up..."),Jump('fp_bedroom_loc')]:
                    yalign .7
                    xalign .7
            if int(current_time[:2]) in hours:
                imagebutton auto "images/backgrounds/interaction_items/fp_bedroom_night_bed_glow_%s.webp" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]
            else:
                imagebutton auto ("images/backgrounds/interaction_items/fp_bedroom_night_bed_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/fp_bedroom_morning_bed_%s.webp") focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]

            if not carry_wallet:
                if int(current_time[:2]) in hours:
                    $ walletimg = "images/backgrounds/interaction_items/fp_bedroom_night_wallet_glow_%s.webp"
                elif int(current_time[:2]) in night:
                    $ walletimg = "images/backgrounds/interaction_items/fp_bedroom_night_wallet_%s.webp"
                else:
                    $ walletimg = "images/backgrounds/interaction_items/fp_bedroom_morning_wallet_%s.webp"
                imagebutton auto walletimg focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('wallet_added',True),Jump('fp_bedroom_loc')]

            if fp_sofa_aquired:
                imagebutton auto ("images/backgrounds/interaction_items/fpbn_sofa_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/fpbm_sofa_%s.webp") focus_mask True action NullAction()

            if wallart['ferrari']:
                imagebutton auto ("images/backgrounds/interaction_items/wallart_ferrari_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wallart_ferrari_morning_%s.webp") focus_mask True action NullAction()
            if wallart['parkinglot']:
                imagebutton auto ("images/backgrounds/interaction_items/wallart_parkinglot_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wallart_parkinglot_morning_%s.webp") focus_mask True action NullAction()
            if wallart['roadtrip']:
                imagebutton auto ("images/backgrounds/interaction_items/wallart_roadtrip_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wallart_roadtrip_morning_%s.webp") focus_mask True action NullAction()
            if wallart['sincity']:
                imagebutton auto ("images/backgrounds/interaction_items/wallart_sincity_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wallart_sincity_morning_%s.webp") focus_mask True action NullAction()
            if wallart['peekaboo']:
                imagebutton auto ("images/backgrounds/interaction_items/wallart_peekaboo_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wallart_peekaboo_morning_%s.webp") focus_mask True action NullAction()

            if not carry_phone:
                if int(current_time[:2]) in hours:
                    $ phoneimg = "images/backgrounds/interaction_items/fp_bedroom_night_phone_glow_%s.webp"
                elif int(current_time[:2]) in night:
                    $ phoneimg = "images/backgrounds/interaction_items/fp_bedroom_night_phone_%s.webp"
                else:
                    $ phoneimg = "images/backgrounds/interaction_items/fp_bedroom_morning_phone_%s.webp"
                imagebutton auto phoneimg focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('phone_added',True),Jump('fp_bedroom_loc')]

            imagebutton auto ("images/backgrounds/interaction_moves/fp_bedroom_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/fp_bedroom_door_morning_%s.webp") focus_mask True action [SetVariable('ups_cfs',True),Call('upstairs_loc')]:
                tooltip "Upper Hallway"

    if room == "fs bedroom":
        if find_panties:
                imagebutton auto ("images/backgrounds/interaction_items/bedroom_panties_"+gp_bed+"_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/bedroom_panties_"+gp_bed+"_morning_%s.webp") focus_mask True action [SetVariable('find_panties',False),SetVariable('panties_added',True),SetVariable('gp_bed',gp_bed),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if find_tablet:
            imagebutton auto ("images/backgrounds/interaction_items/fs_tablet_bedroom_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/fs_tablet_bedroom_morning_%s.webp") focus_mask True action [SetVariable('find_tablet',False),SetVariable('tablet_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if find_pb:
            if not backpack.has_item(princessplug_item):
                imagebutton auto ("images/backgrounds/interaction_items/pink_buttplug_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/pink_buttplug_morning_%s.webp") focus_mask True action [SetVariable('find_pb',False),SetVariable('pb_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event_var = "uts_cfs"
            $ exitdown_event = "upstairs_topofstairs_loc"
            $ exitdown = "Upper hallway"

    if room == "garage":
        if not backpack.has_item(toolbox_item):
            if int(current_time[:2]) in night and not mc_f:
                add "images/backgrounds/interaction_items/honda_cx_500_build_toolbox_night_idle.webp"
            elif not mc_f:
                if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                    imagebutton auto "images/backgrounds/interaction_items/honda_cx_500_build_toolbox_morning_%s.webp" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('toolbox_added',True),Jump('garage_loc')]
                else:
                    add "images/backgrounds/interaction_items/honda_cx_500_build_toolbox_morning_idle.webp"
            else:
                if not mc_f:
                    if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                        imagebutton auto "images/backgrounds/interaction_items/honda_cx_500_build_toolbox_morning_%s.webp" focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]
                    else:
                        add "images/backgrounds/interaction_items/honda_cx_500_build_toolbox_morning_idle.webp"

        if int(current_time[:2]) not in night and not end_bike_repair and not mc_f:
            imagebutton auto "gui/tools_1_morning_%s.webp" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('wmc_cfs',True),Jump('w_mc')]:
                xalign .5
                yalign .5

        $ exitleft_event = "entrance_loc"
        $ exitleft = "Upstairs / Entrance"

        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event_var = "out_cfs"
            $ exitdown_event = "outside_loc"
            $ exitdown = "Go outside"

    if room == "livingroom":
        if not backpack.has_item(carkeys_item) and int(current_time[:2]) > 15:
            imagebutton auto "images/inventory/carkeys_%s.webp" focus_mask True action [SetVariable('carkeys_added',True),SetVariable('lvr_cfs',True),Jump('livingroom_loc')] at ModZoom(.6):
                if bad_weather:
                    yalign .78
                else:
                    yalign .9
                xalign .65
        $ exitright_event_var = "kit_cfs"
        $ exitright_event = "kitchen_loc"
        $ exitright = "Kitchen"
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event = "entrance_loc"
            $ exitdown = "Entrance"

    if room == "kitchen":
        if wcount == 5:
            if bottles == 1 or br == 1 and int(current_time[:2]) in (day or night):
                if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                    imagebutton auto ("images/backgrounds/interaction_items/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',1),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
                else:
                    add ("images/backgrounds/interaction_items/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .31
            elif bottles == 2 or br == 2:
                if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                    imagebutton auto ("images/backgrounds/interaction_items/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
                    imagebutton auto ("images/backgrounds/interaction_items/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                            ypos .485
                            xpos .325
                else:
                    add ("images/backgrounds/interaction_items/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .31
                    add ("images/backgrounds/interaction_items/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .325
            elif bottles == 3 or br == 3:
                if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                    imagebutton auto ("images/backgrounds/interaction_items/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .480
                        xpos .315
                    imagebutton auto ("images/backgrounds/interaction_items/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
                    imagebutton auto ("images/backgrounds/interaction_items/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .325
                else:
                    add ("images/backgrounds/interaction_items/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .480
                        xpos .315
                    add ("images/backgrounds/interaction_items/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .31
                    add ("images/backgrounds/interaction_items/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .325
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            if config.developer:
                imagebutton auto ("images/backgrounds/interaction_items/kitchen_fridge_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_items/kitchen_fridge_door_morning_%s.webp") focus_mask True action [SetVariable('show_fridge',True),Show('fridge_open')]

        $ exitleft_event_var = "lvr_cfs"
        $ exitleft_event = "livingroom_loc"
        $ exitleft = "Livingroom"
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event = "entrance_loc"
            $ exitdown = "Entrance"

    if room == "outside":
        if int(current_time[:2]) in day+night:
            if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                if int(current_time[:2]) in day and (int(current_time[:2]) > 15 and int(current_time[:2]) < 22):
                    imagebutton auto "images/black_car_morning_%s.webp" focus_mask True:
                        if backpack.has_item(carkeys_item):
                            action [SetVariable('out_cfs',True),SetVariable('bc_clicked',True),Jump('outside_loc')]
                        else:
                            action [Function(renpy.notify,"You need to find the car-keys"),Function(set_hint,"You need to find the carkeys to drive the car")]
                elif int(current_time[:2]) in night:
                    if int(current_time[:2]) >= 22 or int(current_time[:2]) < 4:
                        imagebutton auto "images/black_car_night_%s.webp" focus_mask True:
                            if backpack.has_item(carkeys_item):
                                action [SetVariable('out_cfs',True),SetVariable('bc_clicked',True),Jump('outside_loc')]
                            else:
                                action [Function(renpy.notify,"You need to find the car-keys"),Function(set_hint,"You need to find the carkeys to drive the car")]

        if bad_weather:
            if rainstorm:
                add "rain"
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event = "entrance_loc"
            $ exitdown = "Back into the house"
        $ exitleft_event_var = "gar_cfs"
        $ exitleft_event = "garage_loc"
        $ exitleft = "Garage"
        if mc_f:
            $ exitright_event_var = 'br_cfs'
            $ exitright_event = "beach_loc"
            $ exitright = "Go to the beach"

    if room == 'beach':
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event_var = 'out_cfs'
            $ exitdown_event = 'outside_loc'
            $ exitdown = "Go back home"

    if room == 'icafe':
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event_var = 'out_cfs'
            $ exitdown_event = 'outside_loc'
            $ exitdown = "Outside"

    if room == "upstairs":
        #imagebutton auto ("images/backgrounds/interaction_moves/upper_hallway_fp_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/upper_hallway_fp_door_morning_%s.webp") focus_mask True action [SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]:
         #   tooltip "Enter your room"
        if fs_rel >= 30 or fs_invitation:
            imagebutton auto ("images/backgrounds/interaction_moves/upstairs_fs_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/upstairs_fs_door_morning_%s.webp") focus_mask True action [SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]:
                tooltip "Enter [fsName.yourformal]'s room"
        else:
            imagebutton idle ("images/backgrounds/interaction_moves/upstairs_fs_door_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/upstairs_fs_door_morning_idle.webp") focus_mask True action NullAction():
                tooltip "You need a relationship of 30+ with [fsName.yourformal], or an invitation, to enter her room"
        imagebutton auto ("images/backgrounds/interaction_moves/upstairs_bathroom_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/upstairs_bathroom_door_morning_%s.webp") focus_mask True action [Call('ufbm_loc',uhlbcfs=True)]:
            tooltip "Enter bathroom"
        imagebutton auto ("images/backgrounds/interaction_moves/upstairs_stairs_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/upstairs_stairs_morning_%s.webp") focus_mask True action Jump('entrance_loc'):
            tooltip "Downstairs"
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            # $ exitdown_event_var = "uts_cfs"
            # $ exitdown_event = "upstairs_endofhallway_loc"
            # $ exitdown = "Endofhallway room"
            $ exitright_event_var = "uhl_fpb_cfs"
            $ exitright_event = "fp_bedroom_loc"
            $ exitright = "Enter your room"

    if room == "upstairs topofstairs":
        imagebutton auto ("images/backgrounds/interaction_moves/upstairs_topofstairs_bathroom_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/upstairs_topofstairs_bathroom_door_morning_%s.webp") focus_mask True action [Call('ufbm_loc',uhlbcfs=True)]:
            tooltip 'Enter bathroom'
        imagebutton auto ("images/backgrounds/interaction_moves/upstairs_topofstairs_fp_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interaction_moves/upstairs_topofstairs_fp_door_morning_%s.webp") focus_mask True action [SetVariable('uhl_fpb_cfs',True),Call('fp_bedroom_loc')]:
            tooltip "Enter your room"
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
        # $ exitdown_event_var = "uts_cfs"
            # $ exitdown_event = "upstairs_endofhallway_loc"
            # $ exitdown = "Endofhallway room"
            if fs_rel >= 30 or fs_invitation:
                $ exitleft_event_var = "uhl_fsb_cfs"
                $ exitleft_event = "fs_bedroom_loc"
                $ exitleft = "Enter [fsName.yourformal]'s room"
            else:
                $ exitleft_event_var = "uhl_fsb_cfs"
                $ exitleft_event = "fs_bedroom_loc"
                $ exitleft = "You need a relationship of 30+ with [fsName.yourformal], or an invite, to enter her room"
            $ exitdown_event = "entrance_loc"
            $ exitdown = "Downstairs"

    if room == 'ufbm toilet':
        if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
            if int(current_time[:2]) in night:
                imagebutton auto ("images/backgrounds/interaction_items/ufbn_toilet_sink_%s.webp" if bathroom_light else "images/backgrounds/interaction_items/ufbn_toilet_sink_%s.webp") focus_mask True action [SetVariable('occupied_bath',False),SetVariable('fpsink',True),Call('ufbm_toilet_loc',ufbtcfs=True)]
                imagebutton auto ("images/backgrounds/interaction_items/ufbn_toilet_%s.webp" if bathroom_light else "images/backgrounds/interaction_items/ufbn_toilet_%s.webp") focus_mask True action [NullAction()]
            else:
                imagebutton auto ("images/backgrounds/interaction_items/ufbm_toilet_sink_%s.webp" if bathroom_light else "images/backgrounds/interaction_items/ufbm_toilet_sink_%s.webp") focus_mask True action [SetVariable('occupied_bath',False),SetVariable('fpsink',True),Call('ufbm_toilet_loc',ufbtcfs=True)]
                imagebutton auto ("images/backgrounds/interaction_items/ufbm_toilet_%s.webp" if bathroom_light else "images/backgrounds/interaction_items/ufbm_toilet_%s.webp") focus_mask True action [NullAction()]

            $ exitright_event_var = "uhlbcfs"
            $ exitright_event = "ufbm_loc"
            $ exitright = "Use the bathroom"
            $ exitdown_event_var = "uts_cfs"
            $ exitdown_event = "upstairs_topofstairs_loc"
            $ exitdown = "Upper hallway"

    if room == "ufbm" or room == "upper hallway bathroom peek":
        if int(current_time[:2]) >= 6 and int(current_time[:2]) <= 14 and not backpack.has_item(small_keys_item) and keys_mentioned:
            if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                imagebutton auto "images/backgrounds/interaction_items/upper_hallway_bathroom_keys_morning_%s.webp" focus_mask True action [SetVariable('occupied_bath',False),SetVariable("smallkeys_added",True),Call('ufbm_loc',uhlbcfs=True)]
            else:
                add "images/backgrounds/interaction_items/upper_hallway_bathroom_keys_morning_idle.webp"

        if int(current_time[:2]) in night:
            # imagebutton auto "images/backgrounds/upper_hallway_bathroom_shower_night_%s.webp" focus_mask True action [SetVariable("fpshower",True),Jump('ufbm_loc')]
            if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                imagebutton auto ("images/backgrounds/interaction_items/ufbn_sink_%s.webp" if bathroom_light else "images/backgrounds/interaction_items/ufbn_sink_%s.webp") focus_mask True action [SetVariable('occupied_bath',False),SetVariable("fpsink",True),Call('ufbm_loc',uhlbcfs=True)]
                # if bathroom_light:
                #     imagebutton auto "images/backgrounds/interaction_items/bathroom_lightswitch_night_light_on_%s.webp" focus_mask True action [ToggleVariable('bathroom_light'),SetVariable('occupied_bath',False),Call('ufbm_loc',uhlbcfs=True)]
                # else:
                #     imagebutton auto "images/backgrounds/interaction_items/bathroom_lightswitch_night_%s.webp" focus_mask True action [ToggleVariable('bathroom_light'),SetVariable('occupied_bath',False),Call('ufbm_loc',uhlbcfs=True)]
        else:
            if bathroom_find_panties and room != 'upper hallway bathroom peek':
                if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                    imagebutton auto "images/backgrounds/interaction_items/bathroom_panties_"+gp_bath+"_%s.webp" focus_mask True action [SetVariable('bathroom_find_panties',False),SetVariable('occupied_bath',False),SetVariable('bathroom_panties_added',True),SetVariable('gp_bath',gp_bath),Call('ufbm_loc',uhlbcfs=True)]
                else:
                    add "images/backgrounds/interaction_items/bathroom_panties_"+gp_bath+"_idle.webp"
            if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                imagebutton auto "images/backgrounds/interaction_items/ufbm_bathtub_%s.webp" focus_mask True action [SetVariable('occupied_bath',False),SetVariable("fpshower",True),Call('ufbm_loc',uhlbcfs=True)]
                if room == 'upper hallway bathroom peek':
                    add "images/characters/juliette/scenes/upper_hallway_bathroom_juliette_shower_bubbles.webp"
                imagebutton auto "images/backgrounds/interaction_items/ufbm_sink_%s.webp" focus_mask True action [SetVariable('occupied_bath',False),SetVariable("fpsink",True),Call('ufbm_loc',uhlbcfs=True)]
            # add "images/backgrounds/interaction_items/bathroom_lightswitch_morning_off_idle.webp"
        # if wetshower:
            # add "images/backgrounds/interaction_items/upper_hallway_bathroom_shower_wet_glass.webp"
        if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
            $ exitleft_event_var = "ufbtcfs"
            $ exitleft_event = "ufbm_toilet_loc"
            $ exitleft = "Use the toilet"
            $ exitdown_event_var = "uts_cfs"
            $ exitdown_event = "upstairs_topofstairs_loc"
            $ exitdown = "Upper hallway"

    if exitdown:
        if exitdown_event_var:
            if current_location == 'ufbm_loc' or current_location == 'ufbm_toilet_loc':
                $ randomchoice = random.choice([True,False])
                $ returnbfp = True if bathroom_find_panties else False
                imagebutton auto "gui/exit_down_%s.webp" focus_mask True:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
                    if required_shower:
                        action [SetVariable('leave_lock',False),SetVariable('fp_bath_lock',False),SetVariable('occupied_bath',False),SetVariable('bathroom_occupied_fm',False),SetVariable('bathroom_occupied_fs',False),SetVariable('required_shower',True),Call('ufbm_loc',uhlbcfs=True)]
                    else:
                        action [SetVariable('leave_lock',False),SetVariable('fp_bath_lock',False),SetVariable('occupied_bath',randomchoice),SetVariable('fpshower',False),SetVariable('bathroom_panties_added',False),SetVariable('bathroom_find_panties',returnbfp),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]
            elif current_location == 'beach_loc':
                imagebutton auto "gui/exit_down_%s.webp" focus_mask True action [SetVariable(exitdown_event_var,True),Function(addtime,1,30),Jump('outside_loc')]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
            elif current_location == 'icafe_loc':
                imagebutton auto "gui/exit_down_%s.webp" focus_mask True action [SetVariable(exitdown_event_var,True),Function(addtime,False,25),Jump('outside_loc')]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
            elif current_location == 'fs_bedroom_loc' and (panties_added or pb_added):
                if panties_added and not pb_added:
                    imagebutton auto "gui/exit_down_%s.webp" focus_mask True action [SetVariable('panties_added',False),SetVariable('find_panties',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
                elif not panties_added and pb_added:
                    imagebutton auto "gui/exit_down_%s.webp" focus_mask True action [SetVariable('pb_added',False),SetVariable('find_pb',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
                else:
                    imagebutton auto "gui/exit_down_%s.webp" focus_mask True action [SetVariable('pb_added',False),SetVariable('find_pb',True),SetVariable('panties_added',False),SetVariable('find_panties',True),SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                        xalign .5
                        yalign 1.0
                        tooltip exitdown
            else:
                imagebutton auto "gui/exit_down_%s.webp" focus_mask True action [SetVariable(exitdown_event_var,True),Jump(exitdown_event)]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
        else:
            if current_location == 'kitchen_loc' and wine_added:
                imagebutton auto "gui/exit_down_%s.webp" focus_mask True action [SetVariable('wine_added',False),Jump(exitdown_event)]:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
            else:
                imagebutton auto "gui/exit_down_%s.webp" focus_mask True action Jump(exitdown_event):
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
    if exitleft:
        if exitleft_event_var:
            if current_location == 'kitchen_loc' and wine_added:
                imagebutton auto "gui/exit_left_%s.webp" focus_mask True action [SetVariable('wine_added',False),SetVariable(exitleft_event_var,True),Jump(exitleft_event)]:
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
            elif current_location == 'upstairs_topofstairs_loc' and fs_rel <= 30:
                imagebutton auto "gui/exit_left_%s.webp" focus_mask True action NullAction():
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
            else:
                $ print('exitleft happened: '+exitleft_event_var)
                imagebutton auto "gui/exit_left_%s.webp" focus_mask True action [SetVariable(exitleft_event_var,True),Jump(exitleft_event)]:
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
        else:
            if current_location == 'kitchen_loc' and wine_added:
                imagebutton auto "gui/exit_left_%s.webp" focus_mask True action [SetVariable('wine_added',False),Jump(exitleft_event)]:
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
            else:
                imagebutton auto "gui/exit_left_%s.webp" focus_mask True action Jump(exitleft_event):
                    xalign 0.0
                    yalign .5
                    tooltip exitleft
    if exitup:
        if exitup_event_var:
            imagebutton auto "gui/exit_up_%s.webp" focus_mask True action [SetVariable(exitup_event_var,True),Jump(exitup_event)]:
                xalign .5
                yalign 0.0
                tooltip exitup
        else:
            imagebutton auto "gui/exit_up_%s.webp" focus_mask True action Jump(exitup_event):
                xalign .5
                yalign 0.0
                tooltip exitup
    if exitright:
        if exitright_event_var:
            imagebutton auto "gui/exit_right_%s.webp" focus_mask True action [SetVariable(exitright_event_var,True),Jump(exitright_event)]:
                xalign 1.0
                yalign .5
                tooltip exitright
        else:
            imagebutton auto "gui/exit_right_%s.webp" focus_mask True action Jump(exitright_event):
                xalign 1.0
                yalign .5
                tooltip exitright

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"


screen fridge_open():
    if show_fridge:
        $ show_fridge = False
        frame:
            background "images/fridge_open.jpg"
            xalign .5
            yalign .5

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


# style custom_page_label is gui_label
# style custom_page_label_text is gui_label_text
# style custom_page_button is gui_button
# style custom_page_button_text is gui_button_text

# style slot_button is gui_button
# style custom_slot_button_text is gui_button_text
# style custom_slot_time_text is custom_slot_button_text
# style custom_slot_name_text is custom_slot_button_text

# style custom_page_label:
#     xpadding 75
#     ypadding 5

# style nav_buttons:
#     size 13
#     xpadding 4
#     color "#fff"

# style custom_page_label_text:
#     text_align 0.5
#     layout "subtitle"
#     hover_color gui.hover_color
#     color "#fff"

# style custom_slot_button:
#     xsize 370
#     ysize 330
#     background "#f00"

# style custom_slot_button_text:
#     size 15
#     color "#222"

screen fs_tablet():
    default ic_num_str = 0
    modal True
    zorder 800
    $ keyclose = True
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
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
            add "gui/tablet.webp" at ModZoom(.85)
        add "gui/tablet_background.webp" at ModZoom(.85)
        hbox: #backgrounds
            yalign .5
            xalign .5
            text str(len(ic_num))
            if (len(ic_num) == 4):
                $ ic_num_str = ''.join(map(str, ic_num))
                if int(ic_num_str) == tablet_stored_code:
                    $ tablet_code = True
                    $ ic_num = []
                    imagebutton auto "gui/phone_button_gallery_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('tablet_gallery_screen')] at ModZoom(.9):
                        tooltip "Open the image gallery"
                else:
                    $ ic_num = []
            elif tablet_code:
                imagebutton auto "gui/phone_button_gallery_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('tablet_gallery_screen')] at ModZoom(.9):
                    tooltip "Open the image gallery"

        hbox:
            xalign .5
            yalign .5
            imagebutton auto "gui/tablet_power_%s.webp" focus_mask True action [SetVariable('keyclose',False),SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()] at ModZoom(.85)
            if keyclose:
                key 'K_ESCAPE' action [SetVariable('keyclose',False),Hide('phone_info_screen'),SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()]

        if not tablet_code:
            hbox:
                imagemap:
                    alpha False
                    if len(ic_num) == 1:
                        add "gui/tablet_unlock_1.webp"
                    elif len(ic_num) == 2:
                        add "gui/tablet_unlock_2.webp"
                    elif len(ic_num) == 3:
                        add "gui/tablet_unlock_3.webp"
                    elif len(ic_num) == 4:
                        add "gui/tablet_unlock_4.webp"
                    ground "gui/tablet_unlock.webp"
                    hover "gui/tablet_unlock_hover.webp"
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

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

screen tablet_gallery_screen():
    tag tabletscreen
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
            pagekeys True
            vbox:
                for file in renpy.list_files():
                    if file.startswith('images/tablet_gallery/') and file.endswith('.webp'):
                        $ name = file.replace('images/tablet_gallery/','')
                        if name in images_unlocked:
                            imagebutton idle Transform(file,maxsize=(215,215)):
                                xpos pgsxp
                                if not 'portrait' in name:
                                    ypos pgsyp +50
                                else:
                                    ypos pgsyp
                                action [SetVariable('current_file',file),SetVariable('show_icons',False),Hide('tablet_gallery_screen'),Show('tablet_gallery_show')]
                        else:
                            imagebutton idle Transform(file,maxsize=(215,215),alpha=.2):
                                xpos pgsxp
                                if not 'portrait' in name:
                                    ypos pgsyp +50
                                else:
                                    ypos pgsyp
                                # action [SetVariable('current_file',file),SetVariable('show_icons',False),Hide('tablet_gallery_screen'),Show('tablet_gallery_show')]
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
                    key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_tablet_icons',True),Function(hide_tablet_screens),Show('fs_tablet')]

screen tablet_gallery_show():
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
                    imagebutton idle "gui/imggal_close_hover.webp" focus_mask None action[Hide('tablet_gallery_show'),Show('tablet_gallery_screen')] at ModZoom(.5):
                        xalign 1.0
                        ypos -30
                        xoffset 15
                else:
                    imagebutton idle "gui/imggal_transparent_idle.webp" focus_mask None action NullAction() at ModZoom(.65):
                        ypos -30
                action [Show('fullscreen_image',None,filename)]
            if imggal_showbuttons:
                key "K_h" action SetVariable('imggal_showbuttons',False)
            else:
                key "K_h" action SetVariable('imggal_showbuttons',True)
    hbox:
        imagebutton auto "gui/tablet_white_power_%s.webp" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_tablet_screens),Hide('fs_tablet')] at ModZoom(.85):
            tooltip "Shut off the tablet"
        xalign .5
        yalign .5
        if keyclose:
            key "K_ESCAPE" action [SetVariable('keyclose',False),Function(hide_tablet_screens),Show('fs_tablet'),Show('tablet_gallery_screen')]
    hbox:
        if battery_text != 0 and not renpy.get_screen('say') and not renpy.get_screen('choice'):
            imagebutton auto "gui/tablet_white_home_%s.webp" focus_mask True action [SetVariable('keyclose',False),Function(hide_tablet_screens),Show('tablet_gallery_show')] at ModZoom(.85):
                tooltip "Go back to the home-screen"
                alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_tablet_screens),Hide('fs_tablet')]
            xalign .5
            yalign .5
    hbox:
        add "gui/tablet_white.webp" at ModZoom(.85)
        xalign .5
        yalign .5

    use tablet_overlay
    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"



screen tablet_overlay():
    # default ic_num_str = 0
    # modal True
    zorder 800
    $ keyclose = True
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    fixed:
        # fit_first True
        # xmaximum 600
        # ymaximum 800
        # xalign .5
        # yalign .5
        # if len(ic_num) == 4:
        #     $ ic_num_str = ''.join(map(str, ic_num))
        # hbox:
        #     yalign .5
        #     xalign .5
        #     add "gui/tablet.webp" at ModZoom(.85)
        # hbox: #backgrounds
        #     yalign .5
        #     xalign .5
        #     if len(ic_num) == 4:
        #         $ ic_num_str = ''.join(map(str, ic_num))
        #         if int(ic_num_str) == tablet_stored_code:
        #             $ tablet_code = True
        #             $ ic_num = []
        #             # add "gui/tablet_no_content_warning.webp" at ModZoom(.85)
        #             # if fs_rel > 30 and fs_aro > 10:
        #             imagebutton auto "gui/phone_button_gallery_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('tablet_gallery_screen')] at ModZoom(.9):
        #                 tooltip "Open the image gallery"
        #         else:
        #             $ ic_num = []
        #     elif tablet_code:
        #         add "gui/tablet_background.webp" at ModZoom(.85)
        hbox:
            xalign .5
            yalign .5
            imagebutton auto "gui/tablet_power_%s.webp" focus_mask True action [SetVariable('keyclose',False),SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()] at ModZoom(.85)
            if keyclose:
                key 'K_ESCAPE' action [SetVariable('keyclose',False),SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()]

        # if not tablet_code:
        #     hbox:
        #         imagemap:
        #             alpha False
        #             if len(ic_num) == 1:
        #                 add "gui/tablet_unlock_1.webp"
        #             elif len(ic_num) == 2:
        #                 add "gui/tablet_unlock_2.webp"
        #             elif len(ic_num) == 3:
        #                 add "gui/tablet_unlock_3.webp"
        #             elif len(ic_num) == 4:
        #                 add "gui/tablet_unlock_4.webp"
        #             ground "gui/tablet_unlock.webp"
        #             hover "gui/tablet_unlock_hover.webp"
        #             at ModZoom(.85)
        #             yalign .5
        #             xalign .5
        #             if int(ic_num_str) != tablet_stored_code:
        #                 hotspot (204, 392, 94, 96) action [AddToSet(ic_num,1)]:
        #                     sensitive True
        #                 hotspot (318, 392, 94, 96) action [AddToSet(ic_num,2)]:
        #                     sensitive True
        #                 hotspot (436, 394, 94, 96) action [AddToSet(ic_num,3)]:
        #                     sensitive True
        #                 hotspot (204, 502, 94, 96) action [AddToSet(ic_num,4)]:
        #                     sensitive True
        #                 hotspot (318, 502, 94, 96) action [AddToSet(ic_num,5)]:
        #                     sensitive True
        #                 hotspot (436, 502, 94, 96) action [AddToSet(ic_num,6)]:
        #                     sensitive True
        #                 hotspot (204, 610, 94, 96) action [AddToSet(ic_num,7)]:
        #                     sensitive True
        #                 hotspot (318, 610, 94, 96) action [AddToSet(ic_num,8)]:
        #                     sensitive True
        #                 hotspot (436, 610, 94, 96) action [AddToSet(ic_num,9)]:
        #                     sensitive True
        #                 hotspot (318, 718, 94, 96) action [AddToSet(ic_num,0)]:
        #                     sensitive True
        #                 hotspot (464, 839, 71, 33) action [SetVariable('tablet_added',False),SetVariable('find_tablet',True),Return()]:
        #                     sensitive True

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"


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
            pagekeys True
            vbox:
                text "{b}{size=40}How to play{/size}{/b}\n":
                    xalign .5
                text "This game is not a VN. It's more of a sandbox, where you can roam semi-freely around the environment, and do what you please, more or less, with choices depending on what you know and what you've experienced. Of course, there are events that are fully scripted, of which you have no real control (apart from deciding what to do, when).\n"
                text "You will need to apply some adventure-game playstyles - first of all, there are outlines on everything you can pick up, look at and otherwise interact with - it will light up blue when hovered if you can interact with it. If you're stuck in a screen, or can't find anything worth doing, revisit and make sure you check every item.\n"
                text "{b}The regular quick menu and even the regular right-click menu / ESC-menu has been disabled. They have been replaced by an in-game menu (which you will have to find the appropriate item to be able to use). The same goes for the inventory (also an item you need to pick up to be able to use).{/b}\n"
                text "There will be short info-screens for the different objects you can pick up and use in particular ways as well, as the game progresses.\n"
                text "Up left you have a button for\n ":
                    justify True
                    text_align .5
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
                    text_align .5
                text "and a":
                    ypos -94
                textbutton "{u}t-shirt{/u}":
                    text_size 20
                    ypos -128
                    xpos 58
                    action NullAction()
                    hovered Function(info_hover,"tshirt_overlay","show")
                    unhovered Function(info_hover,"tshirt_overlay")
                text " which changes color based on how dirty you are. If you get too dirty, you will not be able to interact with some of the people in game, and you will have to clean up to progress the story and events.\n":
                    ypos -164
                    first_indent 130
                text "Up to the right there is a calendar, showing month, date, weather, day and time. {b}The day and time/clock is clickable, to advance time - clicking on the day puts you at wake-up time the next day, hour advances time by 1 hour, the minutes advances time by 30 minutes{/b}\n":
                    ypos -170
                if persistent.maininfo:
                    text "{color=#f00}{size=28}Once closed, this infoscreen will not show again like this, but the info will be available via the help-screen in-game.{/size}{/color}":
                        xalign .5
                        ypos -180
        if persistent.maininfo:
            imagebutton auto "gui/closebutton_%s.webp" xalign 1.0 yalign 1.0 focus_mask True action [SetField(persistent,'maininfo',False),Hide("maininfo"),Return()]
            if keyclose:
                key 'K_ESCAPE' action [SetVariable('keyclose',False),Hide('phone_info_screen'),SetField(persistent,'maininfo',False),Hide("maininfo"),Return()]

init python:
    def dd_cursor_position(st, at):
        x, y = renpy.get_mouse_pos()
        return Text("{size=-5}%d-%d" % (x, y)), .1

screen debug_tools():
    zorder 999
    add DynamicDisplayable(dd_cursor_position)

screen input(prompt):
    style_prefix "input"

    frame:
        xalign .5
        yalign .5
        xsize 800
        ysize 200

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            yalign .4

            text prompt style "input_prompt"
            text "\n"
            input id "input" color "#fff"

screen preferences():
    tag menu
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            style_prefix "prefs"
            xfill True
            hbox:
                xalign .5
                spacing 80
                if renpy.variant("pc"):
                    textbutton _("Display") action SetField(persistent,'selectedmenu','displaycontrol'):
                        xsize 200
                        ysize 60
                        if persistent.selectedmenu == 'displaycontrol':
                            text_size 40
                    textbutton _("Skip and Speed settings") action SetField(persistent,'selectedmenu','skipcontrol'):
                        xsize 600
                        ysize 60
                        if persistent.selectedmenu == 'skipcontrol':
                            text_size 40
                    textbutton _("Sound") action SetField(persistent,'selectedmenu','soundsettings'):
                        xsize 200
                        ysize 60
                        if persistent.selectedmenu == "soundsettings":
                            text_size 40

            if persistent.selectedmenu:
                if persistent.selectedmenu == 'displaycontrol':
                    vbox:
                        ypos 100
                        xfill True
                        label _("Display Mode"):
                            xalign .5
                        hbox:
                            ypos 25
                            spacing 130
                            xalign .5
                            textbutton _("Window") action [Preference("display","window"),SetField(persistent,'displayresolutions',True)]:
                                selected not preferences.fullscreen
                            textbutton _("Fullscreen") action [Preference("display", "fullscreen"),SetField(persistent,'displayresolutions',False)]:
                                selected preferences.fullscreen

                    if persistent.displayresolutions or not preferences.fullscreen:
                        vbox:
                            ypos 175
                            xfill True
                            label _("Window Size"):
                                xalign .5
                            hbox:
                                ypos 25
                                xalign .5
                                spacing 50
                                $ availres = [(960,540,.5),(1280,720,.6666666666667),(1366,768,.71175117511751175),(1600,900,.8333333333333334),(1920,1080,1)]
                                for x,y,r in availres:
                                    if get_max_res[1] > y and get_max_res[0] != x:
                                        textbutton "[x]x[y]" action [Preference("display",r)]:
                                            if pygame_sdl2.display.Info().current_w != 1365:
                                                selected x == pygame_sdl2.display.Info().current_w
                                            elif pygame_sdl2.display.Info().current_w == 1365 and pygame_sdl2.display.Info().current_h == 768:
                                                selected x == 1366
                                    elif get_max_res[0] == x:
                                        textbutton "[x]x[y]" action [Preference("display","fullscreen"),SetField(persistent,'displayresolutions',False)]

                if persistent.selectedmenu == 'skipcontrol':
                    vbox:
                        ypos 100
                        xfill True
                        label _("Skip Interactions"):
                            xalign .5
                        hbox:
                            ypos 25
                            xalign .5
                            spacing 110
                            hbox:
                                xsize 365
                                # ysize 60
                                textbutton _("Skip Unseen Text") action [ToggleField(persistent,'skipunseen',True,False),Preference("skip", "toggle")]:
                                    xsize 310
                                if persistent.skipunseen:
                                    add "gui/blue_checkmark.webp" at ModZoom(.2)
                            hbox:
                                xsize 365
                                # ysize 60
                                textbutton _("Skip After Choices") action [ToggleField(persistent,'skipafterchoices',True,False),Preference("after choices", "toggle")]:
                                    xsize 310
                                if persistent.skipafterchoices:
                                    add "gui/blue_checkmark.webp" at ModZoom(.2)
                            hbox:
                                xsize 365
                                # ysize 60
                                textbutton _("Skip Transitions") action [ToggleField(persistent,'skiptransitions',True,False),InvertSelected(Preference("transitions", "toggle"))]:
                                    xsize 310
                                if persistent.skiptransitions:
                                    add "gui/blue_checkmark.webp" at ModZoom(.2)
                    vbox:
                        ypos 175
                        xfill True
                        label _("Adjust Speed"):
                            xalign .5
                        hbox:
                            ypos 25
                            xalign .5
                            spacing 70
                            style_prefix "slider"
                            vbox:
                                maximum 300,40
                                label _("Text Speed"):
                                    xalign .5
                                    text_size 20
                                bar value Preference("text speed")
                            vbox:
                                maximum 300,40
                                label _("Auto-Forward Time"):
                                    xalign .5
                                    text_size 20
                                bar value Preference("auto-forward time")

                if persistent.selectedmenu == 'soundsettings':
                    vbox:
                        ypos 100
                        xfill True
                        label _("Adjust Sound"):
                            xalign .5
                        hbox:
                            ypos 25
                            xalign .5
                            spacing 130
                            if config.has_music:
                                vbox:
                                    maximum 325,100
                                    label _("Music Volume"):
                                        xalign .5
                                        text_size 20
                                    bar value Preference("music volume"):
                                        ysize 20
                                    $ musicvolume = int(_preferences.volumes['music']*100) if not persistent.soundmuted and not persistent.musicmuted else 0
                                    hbox:
                                        xalign .5
                                        spacing 20
                                        text "[musicvolume]":
                                            ypos 8
                                        if persistent.musicmuted:
                                            imagebutton idle "gui/speaker_muted.webp" focus_mask True:
                                                at ModZoom(.6)
                                                ypos 5
                                                action [SetField(persistent,'musicmuted',False),ToggleMute('music')]
                                        else:
                                            imagebutton idle "gui/speaker_unmuted.webp" focus_mask True:
                                                at ModZoom(.6)
                                                ypos 5
                                                action [SetField(persistent,'musicmuted',True),ToggleMute('music')]
                            if config.has_sound:
                                vbox:
                                    maximum 325,100
                                    label _("Sound Volume"):
                                        xalign .5
                                        text_size 20
                                    bar value Preference("sound volume"):
                                        ysize 20
                                    $ soundvolume = int(_preferences.volumes['sfx']*100) if not persistent.soundmuted and not persistent.sfxmuted else 0
                                    hbox:
                                        xalign .5
                                        spacing 20
                                        text "[soundvolume]":
                                            ypos 8
                                        if persistent.sfxmuted:
                                            imagebutton idle "gui/speaker_muted.webp" focus_mask True:
                                                at ModZoom(.6)
                                                ypos 5
                                                action [SetField(persistent,'sfxmuted',False),ToggleMute('sfx')]
                                        else:
                                            imagebutton idle "gui/speaker_unmuted.webp" focus_mask True:
                                                at ModZoom(.6)
                                                ypos 5
                                                action [SetField(persistent,'sfxmuted',True),ToggleMute('sfx')]
                                    if config.sample_sound:
                                        imagebutton idle "gui/media_playback.webp" action Play('sound', config.sample_sound):
                                            at ModZoom(.20)
                                            ypos 15
                                            xalign .5

                            if config.has_voice:
                                vbox:
                                    maximum 325,100
                                    label _("Voice Volume"):
                                        xalign .5
                                        text_size 20
                                    bar value Preference("voice volume"):
                                        ysize 20
                                    $ voicevolume = int(_preferences.volumes['voice']*100) if not persistent.soundmuted and not persistent.voicemuted else 0
                                    hbox:
                                        xalign .5
                                        spacing 20
                                        text "[voicevolume]":
                                            ypos 8
                                        if persistent.voicemuted:
                                            imagebutton idle "gui/speaker_muted.webp" focus_mask True:
                                                at ModZoom(.6)
                                                ypos 5
                                                action [SetField(persistent,'voicemuted',False),ToggleMute('voice')]
                                        else:
                                            imagebutton idle "gui/speaker_unmuted.webp" focus_mask True:
                                                at ModZoom(.6)
                                                ypos 5
                                                action [SetField(persistent,'voicemuted',True),ToggleMute('voice')]

                                    if config.sample_voice:
                                        imagebutton idle "gui/media_playback.webp" action Play('voice', config.sample_voice):
                                            at ModZoom(.20)
                                            ypos 15
                                            xalign .5


                        if config.has_music or config.has_sound or config.has_voice:
                            hbox:
                                ypos 200
                                xalign .5
                                if persistent.soundmuted or (persistent.musicmuted and persistent.voicemuted and persistent.sfxmuted):
                                    vbox:
                                        imagebutton idle "gui/speaker_muted.webp" focus_mask True:
                                            xalign .5
                                            action [SetField(persistent,'soundmuted',False),SetField(persistent,'musicmuted',False),SetField(persistent,'voicemuted',False),SetField(persistent,'sfxmuted',False),Preference("all mute","toggle")]
                                        text "Sound muted"
                                else:
                                    vbox:
                                        imagebutton idle "gui/speaker_unmuted.webp" focus_mask True:
                                            xalign .5
                                            action [SetField(persistent,'soundmuted',True),SetField(persistent,'musicmuted',True),SetField(persistent,'voicemuted',True),SetField(persistent,'sfxmuted',True),Preference("all mute","toggle")]
                                        text "Mute all sound"
            else:
                text "Select one of the preference subpages from the menu above":
                    at center
                    yoffset 100
                    size 30

    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"


screen help():
    tag menu
    default device = "keyboard"
    use game_menu(_("Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            xfill True
            # spacing 23
            first_spacing 50
            hbox:
                xalign .5
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():
    vbox:
        spacing 15
        hbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Space")
            text _("Advances dialogue without selecting choices.")

        hbox:
            label _("Arrow Keys")
            text _("Navigate the interface.")

        hbox:
            label _("Escape")
            text _("Accesses the game menu.")

        hbox:
            label _("Ctrl")
            text _("Skips dialogue while held down.")

        hbox:
            label _("Tab")
            text _("Toggles dialogue skipping.")

        hbox:
            label _("Page Up")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Page Down")
            text _("Rolls forward to later dialogue.")

        hbox:
            label "H"
            text _("Hides the user interface.")

        hbox:
            label "S"
            text _("Takes a screenshot.")

        hbox:
            label "V"
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

screen mouse_help():
    vbox:
        spacing 15
        hbox:
            label _("Left Click")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Middle Click")
            text _("Hides the user interface.")

        hbox:
            label _("Right Click")
            text _("Accesses the game menu.")

        hbox:
            label _("Mouse Wheel Up\nClick Rollback Side")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Mouse Wheel Down")
            text _("Rolls forward to later dialogue.")

screen gamepad_help():
    vbox:
        spacing 15
        hbox:
            label _("Right Trigger\nA/Bottom Button")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Left Trigger\nLeft Shoulder")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Right Shoulder")
            text _("Rolls forward to later dialogue.")

        hbox:
            label _("D-Pad, Sticks")
            text _("Navigate the interface.")

        hbox:
            label _("Start, Guide")
            text _("Accesses the game menu.")

        hbox:
            label _("Y/Top Button")
            text _("Hides the user interface.")

        textbutton _("Calibrate") action GamepadCalibrate()


# style help_button is gui_button
# style help_button_text is gui_button_text
# style help_label is gui_label
# style help_label_text is gui_label_text
# style help_text is gui_text

# style help_button:
#     properties gui.button_properties("help_button")
#     xmargin 12

# style help_button_text:
#     # properties gui.button_text_properties("help_button")
#     color "#555"
#     hover_color "#0cf"
#     selected_color "#0cf"
#     xalign .5

# style help_label:
#     xsize 375
#     right_padding 30
#     yalign .5

# style help_label_text:
#     size gui.text_size
#     xalign 1.0
#     text_align 1.0

# style help_text:
#     yalign .5

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:
            hbox:
                xalign .5
                ## This ensures the input will get the enter event before any of the
                ## buttons do.
                order_reverse True
                textbutton _("<") action FilePagePrevious():
                    yalign .5
                ## The page name, which can be edited by clicking on a button.
                button:
                    xsize 600
                    style "page_label"

                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        xalign .5
                        yalign .5
                        yoffset 7
                        style "page_label_text"
                        value page_name_value

                textbutton _(">") action FilePageNext():
                    yalign .5
                ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.4

                xspacing 20
                yspacing 50

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


# style page_label is gui_label
# style page_label_text is gui_label_text
# style page_button is gui_button
# style page_button_text is gui_button_text

# style slot_button is gui_button
# style slot_button_text is gui_button_text
# style slot_time_text is slot_button_text
# style slot_name_text is slot_button_text

# style page_label:
#     xpadding 75
#     ypadding 5

# style page_label_text:
#     text_align 0.5
#     layout "subtitle"
#     hover_color gui.hover_color

# style page_button:
#     properties gui.button_properties("page_button")

# style page_button_text:
#     properties gui.button_text_properties("page_button")

# style slot_button:
#     properties gui.button_properties("slot_button")

# style slot_button_text:
#     properties gui.button_text_properties("slot_button")