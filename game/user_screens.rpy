style infoscreen_text:
    size 22
    justify True
    text_align .5

style infoscreen_button_text:
    color "#fff"
    hover_color "#0cf"

style statscreen_text:
    size 20

style tooltip_hover:
    yalign 0.5
    xmaximum 600
    color "#fff"

style red_color:
    color "#f00"

style inventory_text:
    color "#fff"

# style clock_outline:
#     outlines [(absolute(1), "#17d41e", absolute(0), absolute(0))]

style slider:
    ysize 20
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb_cr.webp"

style category_button_text:
    color "#fff"
    hover_color "#0cf"
    selected_color "#0cf"
    xalign .5

style prefs_button_text:
    color "#555"
    hover_color "#0cf"
    selected_color "#0cf"
    xalign .5

style prefs_button:
    xsize 200
    ysize 60
    hover_background Frame("gui/button_background.webp",xalign=.5)

style prefs_text:
    color "#007a99"
    size 20

style contacts_button_text:
    color "#888"
    hover_color "#0cf"
    selected_color "#0cf"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

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
                    background "gui/textbox_top.webp"
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

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

screen load():
    tag menu
    use file_slots(_("Continue"))

screen navigation():
    vbox:
        # style_prefix "navigation"
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
    background "gui/overlay/game_menu.webp"

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
    xpos .040
    yalign 1.0
    yoffset -15

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

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    color "#fff"

screen ingame_menu_display(day_week=day_week,current_month=current_month,current_month_day=current_month_day,current_time=current_time):
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
                            action [ToggleScreen('phone')]
                        at ModZoom(.8)
                        tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more"
                elif calls:
                    imagebutton auto "gui/menu_phone_call_%s.webp" focus_mask True:
                        if renpy.get_screen('phone'):
                            action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),ToggleScreen('phone')]
                        else:
                            action [ToggleScreen('phone'),Show('')]
                        at ModZoom(.8)
                        tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more. And right now, unanswered calls"
                elif messages:
                    imagebutton auto "gui/menu_phone_message_%s.webp" focus_mask True:
                        if renpy.get_screen('phone'):
                            action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),ToggleScreen('phone')]
                        else:
                            action [ToggleScreen('phone')]
                        at ModZoom(.8)
                        tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more. And right now, new messages"
                elif hints:
                    imagebutton auto "gui/menu_phone_hint_%s.webp" focus_mask True:
                        if renpy.get_screen('phone'):
                            action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),ToggleScreen('phone')]
                        else:
                            action [ToggleScreen('phone')]
                        at ModZoom(.8)
                        tooltip "Here's your phone. It contains ingame menus, imagegalleries, achievements and more. And right now, new hints"

                add "gui/menu_phone_overlay.webp" at ModZoom(.9):
                    # xpos -340
                    # ypos -122
                    yoffset -134
                    xoffset -4.5
                    # yalign 0.0
                    # xalign .5
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

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

# screen splash():
#     timer 2.0 action Hide("splash",dissolve)
#     add "#555"
#     text "Errilhl Studios Presents..." size 60 color "#fff" yalign .5 xalign .5

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
                                    if 'panties' in name:
                                        $ tempname = name.replace(' ','_').replace('_-_','_').lower().split('_')
                                        if len(tempname) == 2:
                                            $ imgname = str('fs_'+tempname[1]+'_'+tempname[0])
                                        elif len(tempname) == 3:
                                            $ imgname = str('fs_'+tempname[1]+'_'+tempname[2]+'_'+tempname[0])
                                    else:
                                        $ imgname = str(name.replace(' ','_').replace('_-_','_').lower())
                                    add "images/inventory/outer_ring_insensitive.webp":
                                        xalign .5
                                        yalign .5
                                    add "images/inventory/"+imgname+"_insensitive.webp":
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

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    yalign .2
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size
    color "#fff"

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"
    color "#fff"

style skip_triangle_call:
    font "DejaVuSans.ttf"
    color "#50AF00"

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
    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
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
            imagebutton auto ("images/backgrounds/interactions_move/front_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/front_door_morning_%s.webp") focus_mask True action [SetVariable('trans',True),SetVariable('out_cfs',True),Jump('outside_loc')]:
                tooltip "Go outside"
            imagebutton auto ("images/backgrounds/interactions_move/kitchen_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/kitchen_door_morning_%s.webp") focus_mask True action [SetVariable('kit_cfs',True),Jump('kitchen_loc')]:
                tooltip 'Kitchen'
            imagebutton auto ("images/backgrounds/interactions_move/livingroom_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/livingroom_door_morning_%s.webp") focus_mask True action [SetVariable('lvr_cfs',True),Jump('livingroom_loc')]:
                tooltip "Livingroom"
            imagebutton auto ("images/backgrounds/interactions_move/stairs_up_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/stairs_up_morning_%s.webp") focus_mask True action [SetVariable('uts_cfs',True),Jump('upstairs_topofstairs_loc')]:
                tooltip "Bedrooms / Bathroom"
            imagebutton auto ("images/backgrounds/interactions_move/stairs_basement_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/stairs_basement_morning_%s.webp") focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]:
                tooltip "Downstairs / Garage"

    if room == "fp bedroom":
        if not backpack.has_item(schoolbooks_item):
            if int(current_time[:2]) in night:
                add "images/backgrounds/interactions_item/fp_bedroom_night_dresser_idle.webp"
            else:
                if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                    imagebutton auto ("images/backgrounds/interactions_item/fp_bedroom_night_dresser_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/fp_bedroom_morning_dresser_%s.webp") focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('schoolbooks_added',True),Jump('fp_bedroom_loc')]
        if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
            if not carry_backpack:
                imagebutton auto ("images/backgrounds/interactions_item/fp_bedroom_night_backpack_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/fp_bedroom_day_backpack_%s.webp") focus_mask True action [SetVariable('carry_backpack',True),SetVariable('uhl_fpb_cfs',True),Function(delete_hint,"You should perhaps try to get something to carry all these things you seem to be able to pick up..."),Jump('fp_bedroom_loc')]:
                    yalign .7
                    xalign .7
            if int(current_time[:2]) in hours:
                imagebutton auto "images/backgrounds/interactions_item/fp_bedroom_night_bed_glow_%s.webp" focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]
            else:
                imagebutton auto ("images/backgrounds/interactions_item/fp_bedroom_night_bed_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/fp_bedroom_morning_bed_%s.webp") focus_mask True action [SetVariable('stn_cfs',True),Jump('sleep_the_night')]

            if not carry_wallet:
                if int(current_time[:2]) in hours:
                    $ walletimg = "images/backgrounds/interactions_item/fp_bedroom_night_wallet_glow_%s.webp"
                elif int(current_time[:2]) in night:
                    $ walletimg = "images/backgrounds/interactions_item/fp_bedroom_night_wallet_%s.webp"
                else:
                    $ walletimg = "images/backgrounds/interactions_item/fp_bedroom_morning_wallet_%s.webp"
                imagebutton auto walletimg focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('wallet_added',True),Jump('fp_bedroom_loc')]

            if fp_sofa_aquired:
                imagebutton auto ("images/backgrounds/interactions_item/fpbn_sofa_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/fpbm_sofa_%s.webp") focus_mask True action NullAction()

            if wallart['ferrari']:
                imagebutton auto ("images/backgrounds/interactions_item/wallart_ferrari_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wallart_ferrari_morning_%s.webp") focus_mask True action NullAction()
            if wallart['parkinglot']:
                imagebutton auto ("images/backgrounds/interactions_item/wallart_parkinglot_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wallart_parkinglot_morning_%s.webp") focus_mask True action NullAction()
            if wallart['roadtrip']:
                imagebutton auto ("images/backgrounds/interactions_item/wallart_roadtrip_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wallart_roadtrip_morning_%s.webp") focus_mask True action NullAction()
            if wallart['sincity']:
                imagebutton auto ("images/backgrounds/interactions_item/wallart_sincity_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wallart_sincity_morning_%s.webp") focus_mask True action NullAction()
            if wallart['peekaboo']:
                imagebutton auto ("images/backgrounds/interactions_item/wallart_peekaboo_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wallart_peekaboo_morning_%s.webp") focus_mask True action NullAction()

            if not carry_phone:
                if int(current_time[:2]) in hours:
                    $ phoneimg = "images/backgrounds/interactions_item/fp_bedroom_night_phone_glow_%s.webp"
                elif int(current_time[:2]) in night:
                    $ phoneimg = "images/backgrounds/interactions_item/fp_bedroom_night_phone_%s.webp"
                else:
                    $ phoneimg = "images/backgrounds/interactions_item/fp_bedroom_morning_phone_%s.webp"
                imagebutton auto phoneimg focus_mask True action [SetVariable('uhl_fpb_cfs',True),SetVariable('phone_added',True),Jump('fp_bedroom_loc')]

            imagebutton auto ("images/backgrounds/interactions_move/fp_bedroom_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/fp_bedroom_door_morning_%s.webp") focus_mask True action [SetVariable('ups_cfs',True),Call('upstairs_loc')]:
                tooltip "Upper Hallway"

    if room == "fs bedroom":
        if find_panties:
                imagebutton auto ("images/backgrounds/interactions_item/bedroom_panties_"+gp_bed+"_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/bedroom_panties_"+gp_bed+"_morning_%s.webp") focus_mask True action [SetVariable('find_panties',False),SetVariable('panties_added',True),SetVariable('gp_bed',gp_bed),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if find_tablet:
            imagebutton auto ("images/backgrounds/interactions_item/fs_tablet_bedroom_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/fs_tablet_bedroom_morning_%s.webp") focus_mask True action [SetVariable('find_tablet',False),SetVariable('tablet_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if find_pb:
            if not backpack.has_item(princessplug_item):
                imagebutton auto ("images/backgrounds/interactions_item/pink_buttplug_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/pink_buttplug_morning_%s.webp") focus_mask True action [SetVariable('find_pb',False),SetVariable('pb_added',True),SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event_var = "uts_cfs"
            $ exitdown_event = "upstairs_topofstairs_loc"
            $ exitdown = "Upper hallway"

    if room == "garage":
        if not backpack.has_item(toolbox_item):
            if int(current_time[:2]) in night and not mc_f:
                add "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_night_idle.webp"
            elif not mc_f:
                if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                    imagebutton auto "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_%s.webp" focus_mask True action [SetVariable('gar_cfs',True),SetVariable('toolbox_added',True),Jump('garage_loc')]
                else:
                    add "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_idle.webp"
            else:
                if not mc_f:
                    if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                        imagebutton auto "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_%s.webp" focus_mask True action [SetVariable('gar_cfs',True),Jump('garage_loc')]
                    else:
                        add "images/backgrounds/interactions_item/honda_cx_500_build_toolbox_morning_idle.webp"

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
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',1),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
                else:
                    add ("images/backgrounds/interactions_item/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .31
            elif bottles == 2 or br == 2:
                if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',2),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                            ypos .485
                            xpos .325
                else:
                    add ("images/backgrounds/interactions_item/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .31
                    add ("images/backgrounds/interactions_item/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .325
            elif bottles == 3 or br == 3:
                if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .480
                        xpos .315
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .31
                    imagebutton auto ("images/backgrounds/interactions_item/wine_bottle_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_%s.webp") at ModZoom(.65) focus_mask True action [SetVariable('kit_cfs',True),SetVariable('bottles',3),SetVariable('wine_added',True),Jump('kitchen_loc')]:
                        ypos .485
                        xpos .325
                else:
                    add ("images/backgrounds/interactions_item/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .480
                        xpos .315
                    add ("images/backgrounds/interactions_item/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .31
                    add ("images/backgrounds/interactions_item/wine_bottle_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/wine_bottle_morning_idle.webp"):
                        at ModZoom(.65)
                        ypos .485
                        xpos .325
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            if config.developer:
                imagebutton auto ("images/backgrounds/interactions_item/kitchen_fridge_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_item/kitchen_fridge_door_morning_%s.webp") focus_mask True action [SetVariable('show_fridge',True),Show('fridge_open')]

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
        #imagebutton auto ("images/backgrounds/interactions_move/upper_hallway_fp_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upper_hallway_fp_door_morning_%s.webp") focus_mask True action [SetVariable('uhl_fpb_cfs',True),Jump('fp_bedroom_loc')]:
         #   tooltip "Enter your room"
        if fs_rel >= 30 or fs_invitation:
            imagebutton auto ("images/backgrounds/interactions_move/upstairs_fs_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upstairs_fs_door_morning_%s.webp") focus_mask True action [SetVariable('uhl_fsb_cfs',True),Jump('fs_bedroom_loc')]:
                tooltip "Enter [fsName.yourformal]'s room"
        else:
            imagebutton idle ("images/backgrounds/interactions_move/upstairs_fs_door_night_idle.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upstairs_fs_door_morning_idle.webp") focus_mask True action NullAction():
                tooltip "You need a relationship of 30+ with [fsName.yourformal], or an invitation, to enter her room"
        imagebutton auto ("images/backgrounds/interactions_move/upstairs_bathroom_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upstairs_bathroom_door_morning_%s.webp") focus_mask True action [Call('upper_hallway_bathroom_loc',uhlbcfs=True)]:
            tooltip "Enter bathroom"
        imagebutton auto ("images/backgrounds/interactions_move/upstairs_stairs_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upstairs_stairs_morning_%s.webp") focus_mask True action Jump('entrance_loc'):
            tooltip "Downstairs"
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            # $ exitdown_event_var = "uts_cfs"
            # $ exitdown_event = "upstairs_endofhallway_loc"
            # $ exitdown = "Endofhallway room"
            $ exitright_event_var = "uhl_fpb_cfs"
            $ exitright_event = "fp_bedroom_loc"
            $ exitright = "Enter your room"

    if room == "upstairs topofstairs":
        imagebutton auto ("images/backgrounds/interactions_move/upstairs_topofstairs_bathroom_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upstairs_topofstairs_bathroom_door_morning_%s.webp") focus_mask True action [Call('upper_hallway_bathroom_loc',uhlbcfs=True)]:
            tooltip 'Enter bathroom'
        imagebutton auto ("images/backgrounds/interactions_move/upstairs_topofstairs_fp_door_night_%s.webp" if int(current_time[:2]) in night else "images/backgrounds/interactions_move/upstairs_topofstairs_fp_door_morning_%s.webp") focus_mask True action [SetVariable('uhl_fpb_cfs',True),Call('fp_bedroom_loc')]:
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

    if room == "upper hallway bathroom" or room == "upper hallway bathroom peek":
        if int(current_time[:2]) >= 6 and int(current_time[:2]) <= 14 and not backpack.has_item(small_keys_item) and keys_mentioned:
            if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_keys_morning_%s.webp" focus_mask True action [SetVariable('occupied_bath',False),SetVariable("smallkeys_added",True),Call('upper_hallway_bathroom_loc',uhlbcfs=True)]
            else:
                add "images/backgrounds/interactions_item/upper_hallway_bathroom_keys_morning_idle.webp"

        if int(current_time[:2]) in night:
            # imagebutton auto "images/backgrounds/upper_hallway_bathroom_shower_night_%s.webp" focus_mask True action [SetVariable("fpshower",True),Jump('upper_hallway_bathroom_loc')]
            if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                imagebutton auto ("images/backgrounds/interactions_item/upper_hallway_bathroom_sink_night_light_%s.webp" if bathroom_light else "images/backgrounds/interactions_item/upper_hallway_bathroom_sink_night_%s.webp") focus_mask True action [SetVariable('occupied_bath',False),SetVariable("fpsink",True),Call('upper_hallway_bathroom_loc',uhlbcfs=True)]
                if bathroom_light:
                    imagebutton auto "images/backgrounds/interactions_item/bathroom_lightswitch_night_light_on_%s.webp" focus_mask True action [ToggleVariable('bathroom_light'),SetVariable('occupied_bath',False),Call('upper_hallway_bathroom_loc',uhlbcfs=True)]
                else:
                    imagebutton auto "images/backgrounds/interactions_item/bathroom_lightswitch_night_%s.webp" focus_mask True action [ToggleVariable('bathroom_light'),SetVariable('occupied_bath',False),Call('upper_hallway_bathroom_loc',uhlbcfs=True)]
        else:
            if bathroom_find_panties and room != 'upper hallway bathroom peek':
                if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                    imagebutton auto "images/backgrounds/interactions_item/bathroom_panties_"+gp_bath+"_%s.webp" focus_mask True action [SetVariable('bathroom_find_panties',False),SetVariable('occupied_bath',False),SetVariable('bathroom_panties_added',True),SetVariable('gp_bath',gp_bath),Call('upper_hallway_bathroom_loc',uhlbcfs=True)]
                else:
                    add "images/backgrounds/interactions_item/bathroom_panties_"+gp_bath+"_idle.webp"
            if renpy.get_screen('say') is None and renpy.get_screen('choice') is None and renpy.get_screen('phone') is None:
                imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_shower_morning_%s.webp" focus_mask True action [SetVariable('occupied_bath',False),SetVariable("fpshower",True),Call('upper_hallway_bathroom_loc',uhlbcfs=True)]
                if room == 'upper hallway bathroom peek':
                    add "images/characters/juliette/scenes/upper_hallway_bathroom_juliette_shower_bubbles.webp"
                imagebutton auto "images/backgrounds/interactions_item/upper_hallway_bathroom_sink_morning_%s.webp" focus_mask True action [SetVariable('occupied_bath',False),SetVariable("fpsink",True),Call('upper_hallway_bathroom_loc',uhlbcfs=True)]
            add "images/backgrounds/interactions_item/bathroom_lightswitch_morning_off_idle.webp"
        if wetshower:
            add "images/backgrounds/interactions_item/upper_hallway_bathroom_shower_wet_glass.webp"
        if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
            $ exitdown_event_var = "uts_cfs"
            $ exitdown_event = "upstairs_topofstairs_loc"
            $ exitdown = "Upper hallway"

    if exitdown:
        if exitdown_event_var:
            if current_location == 'upper_hallway_bathroom_loc':
                $ randomchoice = random.choice([True,False])
                $ returnbfp = True if bathroom_find_panties else False
                imagebutton auto "gui/exit_down_%s.webp" focus_mask True:
                    xalign .5
                    yalign 1.0
                    tooltip exitdown
                    if required_shower:
                        action [SetVariable('leave_lock',False),SetVariable('fp_bath_lock',False),SetVariable('occupied_bath',False),SetVariable('bathroom_occupied_fm',False),SetVariable('bathroom_occupied_fs',False),SetVariable('required_shower',True),Call('upper_hallway_bathroom_loc',uhlbcfs=True)]
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

screen phone():
    # modal True
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
        add "gui/phone_background_black.webp" at ModZoom(.85):
            yalign .5
            xalign .5

        hbox:
            if battery_text != 0:
                xalign .5
                xoffset 3
                yalign 0.0
                yoffset 20
                spacing 12
                xsize 370
                if show_icons:
                    imagebutton auto "gui/phone_button_achievement_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('display_achievements')] at ModZoom(.9):
                        tooltip "Open the achievement-screen"
                    imagebutton auto "gui/phone_button_gallery_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_gallery_screen')] at ModZoom(.9):
                        tooltip "Open the image gallery"
                    imagebutton auto "gui/phone_button_call_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_call_screen')] at ModZoom(.9):
                        tooltip "Phonecalls happen here"
                    imagebutton auto "gui/phone_button_help_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_info_screen')] at ModZoom(.9):
                        tooltip "Open the in-game help-screen"
                    if len(hints) > 0:
                        imagebutton auto "gui/phone_button_hint_redglow_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_hint_screen')] at ModZoom(.9):
                            tooltip "New hints available"
                    elif len(read_hints) > 0:
                        imagebutton auto "gui/phone_button_hint_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_hint_screen',None,'read')] at ModZoom(.9):
                            tooltip "No new hints available"
                    else:
                        imagebutton idle "gui/phone_button_hint_insensitive.webp" focus_mask True action NullAction() at ModZoom(.9):
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
                    imagebutton auto "gui/phone_button_text_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_text_screen')] at ModZoom(.9):
                        tooltip "Read your messages"
                    imagebutton auto "gui/phone_button_alarm_clock_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_alarm')] at ModZoom(.9):
                        tooltip "Set the alarm"
                        xoffset -48
                    imagebutton auto "gui/phone_button_playstore_%s.webp" focus_mask True action [SetVariable('show_icons',False),Function(randomize_appstorelists),Show('phone_playstore')] at ModZoom(.9):
                        tooltip "Go to the PlayStore"
                        xoffset -96


        hbox:
            if battery_text != 0:
                xalign 0.5
                xoffset 3
                yalign 1.0
                yoffset -24
                spacing 12
                if show_icons:
                    imagebutton auto "gui/phone_button_menu_%s.webp" focus_mask True action [SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'mainmenu')] at ModZoom(.9):
                        tooltip "Go to the main menu"
                    imagebutton auto "gui/phone_button_save_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('custom_save')] at ModZoom(.9):
                        tooltip "Save your game"
                    imagebutton auto "gui/phone_button_load_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('custom_load')] at ModZoom(.9):
                        tooltip "Continue your game"
                    imagebutton auto "gui/phone_button_preferences_%s.webp" focus_mask True action [SetVariable('pref_screen',True),SetVariable('show_icons',False),Show('custom_preferences')] at ModZoom(.9):
                        tooltip "Show preferences screen"
                    imagebutton auto "gui/phone_button_quit_%s.webp" focus_mask True action [SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'quit')] at ModZoom(.9):
                        tooltip "Quit the game"

    use phone_overlay
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
            pagekeys True
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

screen phone_playstore():
    tag phonescreen
    # modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    $ keyclose = True
    fixed:
        maximum 370,710
        xalign .5
        yalign .525
        add "gui/phone_background_playstore.webp" at ModZoom(.85):
            yalign .5
            xalign .5

        if not playstore_search_saved.strip() and not playstore_search.strip():
            use phone_playstore_main_icons
        elif playstore_search.strip(): # and not playstore_search_saved.strip():
            $ tempsearch = playstore_search.strip() #.lower() #.strip()
            $ realtimesearchresult = realtime_search(tempsearch,[playstore_recommended,playstore_games,playstore_apps]) #,playstore_apps)
            vbox:
                xalign .5
                yalign .23
                spacing -140
                vbox:
                    add "gui/phone_background_playstore_icons.webp" at ModZoom(.85)
                    vbox:
                        xsize 330
                        xalign .5
                        xoffset 7
                        text "{b}Search results{/b}":
                            xalign 0.0
                            text_align 0.0
                            yalign 0.0
                            yoffset -165
                            size 16
                            color "#222"
                    if realtimesearchresult:
                        vpgrid:
                            xsize 330
                            ysize 140
                            scrollbars None
                            mousewheel True
                            draggable True
                            rows 1
                            yoffset -165
                            xoffset 65
                            for r in realtimesearchresult:
                                $ loadval = r
                                hbox:
                                    button:
                                        hover_background "#EEE"
                                        padding 0,0
                                        vbox:
                                            xsize 110
                                            add "gui/appicon_"+r[2]+".webp" at ModZoom(.70):
                                                xalign .5
                                            text "{b}"+r[0]+"{/b}\n by "+r[1]:
                                                xalign .5
                                                text_align .5
                                                size 12
                                                color "#222"
                                        action [SetVariable('keyclose',False),SetVariable('appselect',loadval),Hide('phone_playstore'),Show('phone_playstore_apppage')]
                    else:
                        vpgrid:
                            xsize 330
                            ysize 140
                            scrollbars None
                            mousewheel True
                            draggable True
                            rows 1
                            yoffset -165
                            xoffset 65
                            hbox:
                                text "nothing was found":
                                    color "#F00"
                                    yoffset 50
                                timer 2.0 action [SetVariable('playstore_search','  '),Hide('phone_playstore'),Hide('phone_playstore_apppage'),Show('phone_playstore')]

        vbox:
            xalign .5
            yalign 0.0
            yoffset 24
            xsize 350
            ysize 35
            add Solid("#FFF")
            text "Enter search":
                xalign 0.05
                yalign 0.0
                yoffset -26
                size 17
                color "#777"
            input default "0" length 20 value VariableInputValue('playstore_search'):
                xalign 1.0
                yalign 0.0
                yoffset -46
                size 17
            key "K_RETURN" action [SetVariable('playstore_search',playstore_search)]

    use phone_overlay
    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]

screen phone_playstore_main_icons():
    tag phonescreen
    zorder 960
    # modal True
    default categories = ['Games','Recommended','Apps']
    fixed:
        maximum 380,710
        xalign .5
        yalign .5
        vbox:
            xalign .5
            yalign .5
            yoffset 90
            spacing -140

            for i in categories:
                vbox:
                    add "gui/phone_background_playstore_icons.webp" at ModZoom(.85)
                    vbox:
                        xsize 330
                        # ysize 20
                        xalign .5
                        xoffset 7
                        text "{b}"+i+"{/b}":
                            xalign 0.0
                            text_align 0.0
                            yalign 0.0
                            yoffset -165
                            size 16
                            color "#222"
                    if i.lower() == 'recommended':
                        $ currentlist = playstore_recommended
                        $ listname = 'recommended'
                    elif i.lower() == 'games':
                        $ currentlist = playstore_games
                        $ listname = 'games'
                    elif i.lower() == 'apps':
                        $ currentlist = playstore_apps
                        $ listname = 'apps'
                    vpgrid:
                        xsize 330
                        ysize 140
                        scrollbars None
                        mousewheel True
                        draggable True
                        rows 1
                        yoffset -165
                        xoffset 65
                        for r in currentlist:
                            $ loadval = r
                            hbox:
                                button:
                                    hover_background "#EEE"
                                    padding 0,0
                                    vbox:
                                        xsize 110
                                        add "gui/appicon_"+r[2]+".webp" at ModZoom(.70):
                                            xalign .5
                                        text "{b}"+r[0]+"{/b}\n by "+r[1]:
                                            xalign .5
                                            text_align .5
                                            size 12
                                            color "#222"
                                    action [SetVariable('keyclose',False),SetVariable('appselect',loadval),Hide('phone_playstore'),Show('phone_playstore_apppage')]

screen phone_playstore_apppage():
    tag phonescreen
    # modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0
    $ keyclose = True
    fixed:
        maximum 370,710
        xalign .5
        yalign .525
        add "gui/phone_background_playstore.webp" at ModZoom(.85):
            yalign .5
            xalign .5
        add "gui/phone_background_apppage.webp" at ModZoom(.85):
            yalign .475
            xalign .5
        vbox:
            yoffset 85
            xalign .5
            vbox:
                ysize 40
                yalign .5
                xalign .5
                text "{b}"+appselect[0]+"{/b}":
                    yalign 1.0
                    xalign .5
                    text_align .5
                    color "#333"
                    size 30
            vbox:
                ysize 60
                yalign .5
                xalign .5
                text "by\n"+appselect[1]:
                    yalign .35
                    xalign .5
                    text_align .5
                    color "#333"
                    size 18
            vbox:
                yalign .5
                xalign .5
                ysize 240
                add "gui/appicon_"+appselect[2]+".webp" at ModZoom(1.5):
                    xalign .5
                    yalign .5
            text appselect[3]:
                yalign .5
                xalign .5
                xsize 310
                ysize 150
                color "#333"
                size 18
                justify True
                layout "subtitle"
            if appselect[4]:
                vbox:
                    yalign 1.0
                    xalign .5
                    yoffset 15
                    if 'itch' in appselect[4]:
                        imagebutton:
                            xalign .5
                            idle "gui/itch_idle.webp"
                            hover "gui/itch_hover.webp"
                            at ModZoom(.80)
                            action OpenURL(appselect[4])
                            tooltip "Opens the Itch.io link in your browser"
                    elif 'patreon' in appselect[4]:
                        imagebutton:
                            xalign .5
                            idle "gui/patreon_idle.webp"
                            hover "gui/patreon_hover.webp"
                            at ModZoom(.80)
                            action OpenURL(appselect[4])
                            tooltip "Opens the Patreon link in your browser"
                    else:
                        textbutton appselect[4]:
                            xalign .5
                            action OpenURL(appselect[4])
                            tooltip "Opens the link in your browser"

        vbox:
            xalign .5
            yalign 0.0
            yoffset 24
            xsize 350
            ysize 35
            imagebutton idle "gui/back_arrow.webp" at ModZoom(.5):
                tooltip "Back to applist"
                action [SetVariable('playstore_search','  '),Hide('phone_playstore_apppage'),Show('phone_playstore')]

    use phone_overlay
    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),Hide('phone_playstore_apppage'),Show('phone_playstore')]

screen phone_text_screen():
    tag phonescreen
    # modal True
    zorder 800
    default x = 500
    default y = 400
    default temp_msg_char = []
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
        yalign .525
        add "gui/phone_background_contacts.webp" at ModZoom(.85):
            yalign .5
            xalign .5

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
                yoffset -30
                text "{b}All Messages{/b}":
                    text_align .5
                    xalign .5
                    color "#fff"
                    size 20
            viewport:
                mousewheel True
                pagekeys True
                ypos 28
                vbox:
                    $ c = 0
                    style_prefix "contacts"
                    $ unique = set(x[0] for x in messages+read_messages)
                    for k,b,v in messages+read_messages:
                        if k in unique:
                            if c % 2:
                                $ bg_color_text = '#ddd'
                            else:
                                $ bg_color_text = '#ccc'
                            if not k == 'fp':
                                if k == 'fm':
                                    $ charimg = "images/characters/anne/anne_idle.webp"
                                    $ charimg_hover = "images/characters/anne/anne_hover.webp"
                                elif k == 'fs':
                                    $ charimg = "images/characters/juliette/juliette_idle.webp"
                                    $ charimg_hover = "images/characters/juliette/juliette_hover.webp"
                                elif k == 'nk':
                                    $ charimg = "images/characters/karen/karen_idle.webp"
                                    $ charimg_hover = "images/characters/karen/karen_hover.webp"
                                elif k == 'nr':
                                    $ charimg = "images/characters/ron/ron_idle.webp"
                                    $ charimg_hover = "images/characters/ron/ron_hover.webp"
                                elif k == 'nc':
                                    $ charimg = "images/characters/catherina/catherina_idle.webp"
                                    $ charimg_hover = "images/characters/chatherina/catherina_hover.webp"
                                else:
                                    $ charimg = "gui/question_mark_idle.webp"
                                    $ charimg_hover = "gui/question_mark_hover.webp"
                                button:
                                    if char == k:
                                        background "#fff"
                                    else:
                                        background bg_color_text
                                    hover_background "#fff"
                                    ysize 50
                                    xsize 370
                                    xpadding 0
                                    ypadding 0
                                    hbox:
                                        yalign .5
                                        if char == k:
                                            add charimg_hover at ModZoom(.40):
                                                yalign .5
                                                xpos 5
                                        else:
                                            add charimg at ModZoom(.40):
                                                yalign .5
                                                xpos 5
                                        text "[b]":
                                            ysize 50
                                            yalign .5
                                            xpos 25
                                            if char == k:
                                                color "#0cf"
                                            else:
                                                color "#444"
                                            hover_color "#0cf"
                                    if char and msg:
                                        action [SetScreenVariable('char',False),SetScreenVariable('msg',False),Hide('show_text_msg')]
                                    else:
                                        action [SetScreenVariable('char',k),SetScreenVariable('msg',v),Hide('phone_text_screen'),Show('show_text_msg',None,k,b)]
                                    hovered [SetScreenVariable("char",k),SetScreenVariable('msg',False)]
                                    unhovered [SetScreenVariable("char",False),SetScreenVariable('msg',False)]
                            $ unique.remove(k)
                            $ c += 1
                    if not messages+read_messages:
                        hbox:
                            xsize 370
                            xalign .5
                            yalign .5
                            text "No text-messages received yet":
                                color "#444"
                                xalign .5
                                text_align .5
                                size 20

    use phone_overlay
    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]

screen show_text_msg(compchar=False,char=False):
    tag phonescreen
    # modal True
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
            add "gui/phone_background_contacts.webp" at ModZoom(.85)
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
                text "{b}All Messages from [char]{/b}":
                    text_align .5
                    xalign .5
                    color "#fff"
                    size 20
            viewport:
                mousewheel True
                pagekeys True
                ypos 28
                vbox:
                    spacing 10
                    $ c = 0
                    style_prefix "contacts"
                    for k,b,v in messages+read_messages:
                        if k == compchar:
                            if k == 'fm':
                                $ charimg = "images/characters/anne/anne_idle.webp"
                                $ charimg_hover = "images/characters/anne/anne_hover.webp"
                            elif k == 'fs':
                                $ charimg = "images/characters/juliette/juliette_idle.webp"
                                $ charimg_hover = "images/characters/juliette/juliette_hover.webp"
                            elif k == 'nk':
                                $ charimg = "images/characters/karen/karen_idle.webp"
                                $ charimg_hover = "images/characters/karen/karen_hover.webp"
                            elif k == 'nr':
                                $ charimg = "images/characters/ron/ron_idle.webp"
                                $ charimg_hover = "images/characters/ron/ron_hover.webp"
                            elif k == 'nc':
                                $ charimg = "images/characters/catherina/catherina_idle.webp"
                                $ charimg_hover = "images/characters/chatherina/catherina_hover.webp"
                            else:
                                $ charimg = "gui/question_mark_idle.webp"
                                $ charimg_hover = "gui/question_mark_hover.webp"
                            button:
                                background "#0cf"
                                xsize 370
                                text "[v]"
                                if compchar == 'nr' and nc_number in v:
                                    if 'nc' in not_in_contacts:
                                        action [Function(read_message,k,b,v),Function(not_in_contacts.remove,'nc'),Function(set_hint,"You've gotten the info from "+nr.name+". Maybe you should try calling "+nc.name+""),Hide('show_text_msg'),Show('phone_text_screen')]
                                        tooltip "Click to add to contacts"
                                    else:
                                        action [Function(read_message,k,b,v),Function(set_hint,"You've gotten the info from "+nr.name+". Maybe you should try calling "+nc.name+""),Hide('show_text_msg'),Show('phone_text_screen')]
                                else:
                                    action [Function(read_message,k,b,v),Hide('show_text_msg'),Show('phone_text_screen')]

                        if nc_message_after_hacker:
                            if k == 'nc':
                                $ print('test')

    use phone_overlay
    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

screen phone_call_screen():
    tag phonescreen
    # modal True
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
        yalign .525
        add "gui/phone_background_contacts.webp" at ModZoom(.85):
            yalign .5
            xalign .5
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
                yoffset -30
                text "{b}All Contacts{/b}":
                    text_align .5
                    xalign .5
                    color "#fff"
                    size 20
            viewport:
                mousewheel True
                pagekeys True
                ypos 28
                vbox:
                    style_prefix "contacts"
                    $ c = 0
                    for i in chars:
                        if c % 2:
                            $ bg_color_contacts = '#ddd'
                        else:
                            $ bg_color_contacts = '#ccc'
                        if not i[1] in not_in_contacts:
                            if i[1] == 'fm':
                                $ charimg = "images/characters/anne/anne_idle.webp"
                                $ charimg_hover = "images/characters/anne/anne_hover.webp"
                            elif i[1] == 'fs':
                                $ charimg = "images/characters/juliette/juliette_idle.webp"
                                $ charimg_hover = "images/characters/juliette/juliette_hover.webp"
                            elif i[1] == 'nk':
                                $ charimg = "images/characters/karen/karen_idle.webp"
                                $ charimg_hover = "images/characters/karen/karen_hover.webp"
                            elif i[1] == 'nr':
                                $ charimg = "images/characters/ron/ron_idle.webp"
                                $ charimg_hover = "images/characters/ron/ron_hover.webp"
                            elif i[1] == 'nc':
                                $ charimg = "images/characters/catherina/catherina_idle.webp"
                                $ charimg_hover = "images/characters/catherina/catherina_hover.webp"
                            else:
                                $ charimg = "gui/question_mark_idle.webp"
                                $ charimg_hover = "gui/question_mark_hover.webp"

                            button:
                                background bg_color_contacts
                                hover_background "#fff"
                                ysize 80
                                xsize 370
                                hbox:
                                    ysize 80
                                    spacing 10
                                    if stats == i:
                                        if charimg_hover == 'gui/question_mark_hover.webp':
                                            add charimg_hover at ModZoom(.6):
                                                yalign .5
                                                yoffset -10
                                        else:
                                            add charimg_hover at ModZoom(.65):
                                                yalign .5
                                                yoffset -10
                                        text "[i[0]]":
                                            ysize 80
                                            yalign .5
                                            yoffset -10
                                            color "#0cf"
                                    else:
                                        if charimg == "gui/question_mark_idle.webp":
                                            add charimg at ModZoom(.6):
                                                yalign .5
                                                yoffset -10
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
                                if i[1] == 'nc':
                                    action Show('phone_call_show',None,i[1],'nc_talk',True,'first_talk')
                                elif i[1] == 'nr':
                                    action Show('phone_call_show',None,i[1],'nr_talk',True,'nr_after_nc')
                                elif i[1] == 'nk':
                                    if call_nk_event:
                                        action Show('phone_call_show',None,i[1],'nk_talk',True,call_nk_event)
                                    else:
                                        action Show('phone_call_show',None,i[1],False,True,False)
                                else:
                                    # action Show('warning_screen',None,300,370,"There are no functionality for this person currently implemented")
                                    action Show('phone_call_show',None,i[1],False,True,False)
                            $ c += 1
    use phone_overlay
    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]

screen phone_call_show(char=False,label=False,calling_out=False,event=False):
    tag phonescreen
    zorder 900
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
        $ get_char = getattr(store,char)
        if char == 'fm':
            # $ char_name_lowered = fmName.name.lower()
            $ phone_img = "images/characters/"+fmName.name.lower()+"/"+fmName.name.lower()+"_phone_image.webp"
        elif char == 'fs':
            $ phone_img = "images/characters/"+fsName.name.lower()+"/"+fsName.name.lower()+"_phone_image.webp"
        else:
            # $ char_name_lowered = get_char_name.name.lower().replace(' ','_')
            $ phone_img = "images/characters/"+get_char.name.lower()+"/"+get_char.name.lower()+"_phone_image.webp"
        vbox:
            ysize 500
            yalign 0.0
            yoffset 50
            add phone_img:
                zoom .8
                xalign .5
                yalign .5
            text "[get_char]":
                xalign .5
                text_align .5
                ypos 20

            vbox:
                style_prefix "skip"
                xsize 370
                ysize 100
                yoffset 50
                xalign .5
                if calling:
                    hbox:
                        spacing 9
                        xalign .5
                        text _("Calling") style "skip_triangle_call"
                        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle_call"
                        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle_call"
                        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle_call"
                    $ callrand = renpy.random.random()
                    timer 3.0:
                        if callrand > .35 and char in ['nr','nc','nk']:
                            if label:
                                action [SetVariable('duringcall',True),SetVariable('calling',False),Call(label,event=event,callrand=callrand)]
                            else:
                                # action [SetVariable('duringcall',True),SetVariable('calling',False)]
                                action [SetVariable('duringcall',False),SetVariable('calling',False),Call('no_answer')]
                        # elif char in ['nr','nc','nk']:
                        #     if label:
                        #         action [SetVariable('duringcall',False),SetVariable('calling',True),Call(label,event=event,callrand=callrand)]
                        #     else:
                        #         # action [SetVariable('duringcall',False),SetVariable('calling',True)]
                        #         action [SetVariable('duringcall',False),SetVariable('calling',False),Call('no_answer')]
                        else:
                           action [SetVariable('duringcall',False),SetVariable('calling',False),Call('no_answer')]

                elif duringcall:
                    hbox:
                        spacing 9
                        xalign .5
                        text _("Call connected") style "skip_triangle_call"
                else:
                    hbox:
                        spacing 9
                        xalign .5
                        text _("Calling"):
                            color "#161616"
            hbox:
                xsize 370
                xalign .5
                if not calling and not duringcall:
                    imagebutton auto "gui/phone_call_%s.webp" focus_mask True:
                        action [SetVariable('calling',True)]
                        if not calling_out:
                            xalign .2
                        else:
                            xalign .5
                else:
                    imagebutton auto "gui/phone_hang_up_%s.webp" focus_mask True:
                        if renpy.get_screen('say'):
                            action [Hide('say'),SetVariable('duringcall',False),SetVariable('calling',False),Hide('phone_call_show'),Show('phone_call_screen')]
                        else:
                            action [SetVariable('duringcall',False),SetVariable('calling',False),Hide('phone_call_show'),Show('phone_call_screen')]
                        xalign .5
                if not calling_out:
                    imagebutton auto "gui/phone_hang_up_%s.webp" focus_mask True:
                        action [SetVariable('duringcall',False),SetVariable('calling',False),Hide('phone_call_show'),Show('phone_call_screen')]
                        xalign .8
    hbox:
        imagebutton auto "gui/phone_white_power_%s.webp" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
            tooltip "Shut off the phone"
        xalign .5
        yalign .5
        if keyclose:
            key "K_ESCAPE" action [SetVariable('keyclose',False),Function(hide_phone_screens),Show('phone'),Show('phone_gallery_screen')]
    hbox:
        if battery_text != 0 and not renpy.get_screen('say') and not renpy.get_screen('choice'):
            imagebutton auto "gui/phone_white_home_%s.webp" focus_mask True action [SetVariable('keyclose',False),Function(hide_phone_screens),Show('phone_call_screen')] at ModZoom(.85):
                alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
            xalign .5
            yalign .5
    hbox:
        add "gui/phone_white.webp" at ModZoom(.85)
        xalign .5
        yalign .5

    # use phone_overlay
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
            pagekeys True
            vbox:
                for file in renpy.list_files():
                    if file.startswith('images/phone_gallery/') and file.endswith('.webp'):
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
                    imagebutton idle "gui/imggal_close_hover.webp" focus_mask None action[Hide('phone_gallery_show'),Show('phone_gallery_screen')] at ModZoom(.5):
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
        imagebutton auto "gui/phone_white_power_%s.webp" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
            tooltip "Shut off the phone"
        xalign .5
        yalign .5
        if keyclose:
            key "K_ESCAPE" action [SetVariable('keyclose',False),Function(hide_phone_screens),Show('phone'),Show('phone_gallery_screen')]
    hbox:
        if battery_text != 0 and not renpy.get_screen('say') and not renpy.get_screen('choice'):
            imagebutton auto "gui/phone_white_home_%s.webp" focus_mask True action [SetVariable('keyclose',False),Function(hide_phone_screens),Show('phone_gallery_show')] at ModZoom(.85):
                tooltip "Go back to the home-screen"
                alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
            xalign .5
            yalign .5
    hbox:
        add "gui/phone_white.webp" at ModZoom(.85)
        xalign .5
        yalign .5

    use phone_overlay
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
                idle "gui/phone_white_power_hover.webp"
                hover "gui/phone_white_power_hover.webp"
                focus_mask True
                action [SetField(persistent,'phone_firstshow',False),SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85)
                tooltip "Shut off the phone"
            xalign .5
            yalign .5
        hbox:
            if battery_text != 0 and not renpy.get_screen('say') and not renpy.get_screen('choice'):
                imagebutton:
                    idle "gui/phone_white_home_hover.webp"
                    hover "gui/phone_white_home_hover.webp"
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
        bottom_padding 20
        xalign .5
        yalign .44
        maximum 370,726
        viewport:
            mousewheel True
            pagekeys True
            vbox:
                xfill True
                text "This is the phone-screen. Here you'll find all the game-menus (bottom row on home screen):\n"
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_menu_%s.webp" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'mainmenu')] at ModZoom(.6):
                        yalign .5
                    textbutton "Main menu" action [Hide('phone_info_screen'),Show('custom_confirm',None,'mainmenu')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_save_%s.webp" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),Show('custom_save')] at ModZoom(.6):
                        yalign .5
                    textbutton "Save" action [Hide('phone_info_screen'),Show('custom_save')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_load_%s.webp" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),Show('custom_load')] at ModZoom(.6):
                        yalign .5
                    textbutton "Continue" action [Hide('phone_info_screen'),Show('custom_load')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_preferences_%s.webp" focus_mask True action [Hide('phone_info_screen'),SetVariable('pref_screen',True),SetVariable('show_icons',False),Show('custom_preferences')] at ModZoom(.6):
                        yalign .5
                    textbutton "Preferences" action [Hide('phone_info_screen'),Show('custom_preferences')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_quit_%s.webp" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),SetVariable('quit_screen',True),Show('custom_confirm',None,'quit')] at ModZoom(.6):
                        yalign .5
                    textbutton "Quit game" action [Hide('phone_info_screen'),Show('custom_confirm',None,'quit')]:
                        text_size 22
                        yalign .5
                text "\nand also different other screens, like the:\n"
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_achievement_%s.webp" focus_mask True action [Hide('phone_info_screen'),SetVariable('show_icons',False),Show('display_achievements')] at ModZoom(.6):
                        yalign .5
                    textbutton "Achievement screen" action [Hide('phone_info_screen'),Show('display_achievements')]:
                        text_size 22
                        yalign .5
                hbox:
                    xpos .2
                    imagebutton auto "gui/phone_button_gallery_%s.webp" focus_mask True action [Hide('phone_info_screen'),Show('phone_gallery_screen')] at ModZoom(.6):
                        yalign .5
                    textbutton "Image gallery" action [Hide('phone_info_screen'),Show('phone_gallery_screen')]:
                        text_size 22
                        yalign .5
                vbox:
                    ypos 10
                    hbox:
                        text "While in the gallery, you can click on images to show them in full screen on the phone. While viewing the full-screen image, there will be buttons to navigate and close (depending on amount of images) - to hide/show them, you can press \"h\"":
                            size 22
                            yalign .5
                    vbox:
                        ypos 15
                        hbox:
                            xpos .2
                            imagebutton auto "gui/phone_button_call_%s.webp" focus_mask True action [Hide('phone_info_screen'),Show('phone_call_screen')] at ModZoom(.6):
                                yalign .5
                            textbutton "Call screen" action [Hide('phone_info_screen'),Show('phone_call_screen')]:
                                text_size 22
                                yalign .5
                        hbox:
                            xpos .2
                            imagebutton auto "gui/phone_button_help_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_info_screen')] at ModZoom(.6):
                                yalign .5
                            textbutton "In-game help" action [SetVariable('show_icons',False),Show('phone_info_screen')]:
                                text_size 22
                                yalign .5
                        hbox:
                            xpos .2
                            imagebutton auto "gui/phone_button_hint_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_hint_screen')] at ModZoom(.6):
                                yalign .5
                            textbutton "Game-hints" action [SetVariable('show_icons',False),Show('phone_hint_screen')]:
                                text_size 22
                                yalign .5
                        vbox:
                            ypos 10
                            hbox:
                                text "The hint-screen (and the phone on the top left, in the menu) will glow red when there are new hints"
                            vbox:
                                ypos 10
                                hbox:
                                    xpos .2
                                    imagebutton auto "gui/phone_button_text_%s.webp" focus_mask True action [Hide('phone_info_screen'),Show('phone_text_screen')] at ModZoom(.6):
                                        yalign .5
                                    textbutton "Message screen" action [Hide('phone_info_screen'),Show('phone_text_screen')]:
                                        text_size 22
                                        yalign .5
                                hbox:
                                    xpos .2
                                    imagebutton auto "gui/phone_button_alarm_clock_%s.webp" focus_mask True action [Hide('phone_info_screen'),Show('phone_alarm')] at ModZoom(.6):
                                        yalign .5
                                    textbutton "Alarm Clock" action [Hide('phone_info_screen'),Show('phone_alarm')]:
                                        text_size 22
                                        yalign .5
                                hbox:
                                    xpos .2
                                    imagebutton auto "gui/phone_button_playstore_%s.webp" focus_mask True action [Hide('phone_info_screen'),Show('phone_playstore')] at ModZoom(.6):
                                        yalign .5
                                    textbutton "PlayStore" action [Hide('phone_info_screen'),Show('phone_playstore')]:
                                        text_size 22
                                        yalign .5
                                vbox:
                                    ypos 10
                                    text "\nand more as the game is being developed.\n\nYou close the phone by pressing the power button on the right side of the phone, or by clicking the home-button when on the main screen. If there is an app / screen showing on the phone, the home button takes you back to the main screen. You can also use \"ESC\" to close screens, and the phone itself, if you're on the home-screen. Right-clicking on the home-button / long-pressing (if on touch-screen) (at any time) will close the phone\n\n"
    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetField(persistent,'phone_firstshow',False),Function(hide_phone_screens),SetVariable('show_icons',True),Show('phone')]

screen phone_alarm(pa_chosen=False):
    tag phonescreen
    zorder 900
    $ keyclose = True
    $ usehour = format(alarmhour,"02d")
    $ useminute = format(alarmminute,"02d")
    frame:
        background None
        xpadding 0
        top_padding 40
        bottom_padding 10
        xalign .5
        yalign .44
        maximum 370,686
        vbox:
            xsize 370
            ysize 300
            yoffset 30
            text "Set alarm":
                xalign .5
            hbox:
                xalign .5
                textbutton "[usehour]":
                    action Function(alarm_setting,hour=True)
                    text_size 70
                    text_color "#eee"
                    text_hover_color "#0cf"
                    yalign .5
                text ":":
                    size 40
                    yalign .5
                    color "#eee"
                textbutton "[useminute]":
                    action Function(alarm_setting,minute=True)
                    text_size 70
                    text_color "#eee"
                    text_hover_color "#0cf"
                    yalign .5
            hbox:
                xalign .5
                textbutton "Set alarm":
                    background "#0cf"
                    text_color "#fff"
                    hover_background "#fff"
                    text_hover_color "#000"
                    text_size 24
                    xalign .5
                    action [Function(renpy.notify,"Alarm is set to "+usehour+":"+useminute+""),SetVariable('alarmclock_time',""+usehour+":"+useminute+""),SetVariable('alarmclock_icon',True),SetVariable('alarmclock',True)]
        vbox:
            xalign .5
            yalign .5
            yoffset 30
            textbutton "Turn off alarm":
                background "#f00"
                text_color "#fff"
                hover_background "#fff"
                text_hover_color "#000"
                text_size 18
                xalign .5
                action [Function(renpy.notify,"Alarm is turned off"),SetVariable('alarmclock_time',"00:00"),SetVariable('alarmhour',0),SetVariable('alarmminute',0),SetVariable('alarmclock_icon',False),SetVariable('alarmclock',False)]

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
    # modal True
    zorder 800
    default x = 500
    default y = 400
    python:
        x, y = renpy.get_mouse_pos()
        xval = 1.0 if x > config.screen_width/2 else .0
        yval = 1.0 if y > config.screen_height/2 else .0

    on 'show' action Function(achievement_trophy_case.update)

    use display_achievements_category_panel

    use phone_light_background

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
            pagekeys True
            vbox:
                $ i = 0
                for achievement in achievements:
                    if achievement.category in selected_category:
                        if achievement.hidden:
                            if show_hidden_achievements:
                                fixed:
                                    xsize 370
                                    ysize 100
                                    imagebutton auto "gui/achievement_%s.webp" focus_mask True:
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
                                    add "gui/phone_hidden_idle.webp":
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
                        elif not achievement.unlocked:
                            if show_locked_achievements:
                                fixed:
                                    xsize 370
                                    ysize 100
                                    imagebutton auto "gui/achievement_%s.webp" focus_mask True:
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
                                    add "gui/phone_lock_idle.webp":
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

                        elif achievement.unlocked:
                            if show_unlocked_achievements:
                                fixed:
                                    xsize 370
                                    ysize 100
                                    imagebutton auto "gui/achievement_%s.webp" focus_mask True:
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
                                    add "gui/phone_unlock_idle.webp":
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
                        else:
                            fixed:
                                xsize 370
                                ysize 100
                                imagebutton auto "gui/achievement_%s.webp" focus_mask True:
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
                                    add "gui/phone_unlock_idle.webp":
                                        xpos 300
                                        ypos 35
                                elif not achievement.unlocked:
                                    add "gui/phone_lock_idle.webp":
                                        xpos 300
                                        ypos 35
                                elif achievement.hidden:
                                    add "gui/phone_hidden_idle.webp":
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

    use phone_overlay
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
        # padding 15, 15
        # align 0.03, 0.13
        yalign .5
        xalign .5
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
    use custom_file_slots(_("Continue"))

screen custom_preferences():
    tag phonescreen
    # modal True
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
            pagekeys True
            vbox:
                if renpy.variant("pc"):
                    fixed:
                        style_prefix "category"
                        xsize 370
                        ysize 150
                        hbox:
                            yalign 0.0
                            xalign .5
                            label _("Display"):
                                text_color "#fff"
                        hbox:
                            ypos 40
                            textbutton _("Window") action Preference("display", "window")
                                # foreground "gui/button/check_[prefix_]foreground_white.webp"
                        hbox:
                            ypos 80
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                                # foreground "gui/button/check_[prefix_]foreground_white.webp"
                if not renpy.variant("pc"):
                    fixed:
                        xsize 370
                        ysize 200
                        style_prefix "category"
                        hbox:
                            yalign 0.0
                            xalign .5
                            label _("Rollback Side"):
                                text_color "#fff"
                        hbox:
                            ypos 40
                            textbutton _("Disable") action Preference("rollback side", "disable")
                                # foreground "gui/button/check_[prefix_]foreground_white.webp"
                        hbox:
                            ypos 80
                            textbutton _("Left") action Preference("rollback side", "left")
                                # foreground "gui/button/check_[prefix_]foreground_white.webp"
                        hbox:
                            ypos 120
                            textbutton _("Right") action Preference("rollback side", "right")
                                # foreground "gui/button/check_[prefix_]foreground_white.webp"

                fixed:
                    xsize 370
                    ysize 200
                    style_prefix "category"
                    hbox:
                        yalign 0.0
                        xalign .5
                        label _("Skip"):
                            text_color "#fff"
                    hbox:
                        ypos 40
                        textbutton _("Unseen Text") action Preference("skip", "toggle"):
                            selected preferences.skip_unseen == True
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"
                    hbox:
                        ypos 80
                        textbutton _("After Choices") action Preference("after choices", "toggle"):
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"
                            selected preferences.skip_after_choices == True
                    hbox:
                        ypos 120
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")):
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"
                            selected preferences.transitions == 0

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
                        ysize 100
                        hbox:
                            yalign 0.0
                            xalign .5
                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"
                                text_color "#fff"
                                # foreground "gui/button/check_[prefix_]foreground_white.webp"

                fixed:
                    xsize 370
                    ysize 200
                    style_prefix "category"
                    hbox:
                        yalign 0.0
                        xalign .5
                        label _("Cheats"):
                            text_color "#fff"
                    hbox:
                        ypos 40
                        textbutton _("Disable") action SetField(persistent,"cheat",False)
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"
                    hbox:
                        ypos 80
                        textbutton _("Enable") action SetField(persistent,"cheat",True)
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"

                fixed:
                    xsize 370
                    ysize 200
                    style_prefix "category"
                    hbox:
                        ysize 50
                        xalign .5
                        label _("Zoomed side-images"):
                            text_color "#fff"
                    hbox:
                        ysize 50
                        ypos 50
                        xsize 370
                        textbutton _("Disable") action SetField(persistent,'side_image_zoom',False):
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"
                            yalign .5
                    hbox:
                        ysize 50
                        ypos 100
                        xsize 370
                        textbutton _("Enable") action SetField(persistent,'side_image_zoom',True):
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"
                            yalign .5

                fixed:
                    xsize 370
                    ysize 200
                    style_prefix "category"
                    hbox:
                        ysize 50
                        xalign .5
                        label _("Quick Menu"):
                            text_color "#fff"
                    hbox:
                        ysize 50
                        ypos 50
                        xsize 370
                        textbutton _("Disable") action SetField(persistent,'quick_menu', False):
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"
                            yalign .5
                    hbox:
                        ysize 50
                        ypos 100
                        xsize 370
                        textbutton _("Enable") action SetField(persistent,'quick_menu', True):
                            # foreground "gui/button/check_[prefix_]foreground_white.webp"
                            yalign .5

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
                                # foreground "gui/button/check_[prefix_]foreground_white.webp"
    frame:
        background None
        xalign .5
        yalign .5
        hbox:
            imagebutton auto "gui/phone_white_power_%s.webp" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
                tooltip "Shut off the phone"
            xalign .5
            yalign .5
        hbox:
            if not renpy.get_screen('say') and not renpy.get_screen('choice') and not renpy.get_screen('phone'):
                imagebutton auto "gui/phone_white_home_%s.webp" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)] at ModZoom(.85):
                    tooltip "Go back to the home-screen"
                    alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
            xalign .5
            yalign .5

    use phone_overlay
    if GetTooltip() is not None:
        frame:
            pos(x, y)
            anchor (xval, yval)
            text GetTooltip() style "tooltip_hover"

    if keyclose:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone')]


screen phone_light_background():
    hbox:
        xalign .5
        yalign .5
        add "gui/phone_background_light.webp" at ModZoom(.85)

screen phone_overlay():
    zorder 990
    $ keyclose = True
    hbox: #notification-bar
        if battery_text != 0:
            add "gui/phone_notification_bar.webp" at ModZoom(.85)
            xalign .5
            yalign .5
    hbox: #battery-indicator
        if battery_text != 0:
            if battery_text == 100:
                add "gui/phone_battery_100.webp"
            elif battery_text < 100 and battery_text >= 90:
                add "gui/phone_battery_90.webp"
            elif battery_text < 90 and battery_text >= 80:
                add "gui/phone_battery_80.webp"
            elif battery_text < 80 and battery_text >= 70:
                add "gui/phone_battery_70.webp"
            elif battery_text < 70 and battery_text >= 60:
                add "gui/phone_battery_60.webp"
            elif battery_text < 60 and battery_text >= 50:
                add "gui/phone_battery_50.webp"
            elif battery_text < 50 and battery_text >= 40:
                add "gui/phone_battery_40.webp"
            elif battery_text < 40 and battery_text >= 30:
                add "gui/phone_battery_30.webp"
            elif battery_text < 30 and battery_text >= 20:
                add "gui/phone_battery_20.webp"
            elif battery_text < 20 and battery_text >= 10:
                add "gui/phone_battery_10.webp"
            else:
                add "gui/phone_battery_0.webp"
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
    hbox:
        if alarmclock_icon:
            add "gui/phone_alarmclock_icon.webp" at ModZoom(.48)
            xalign .556
            yalign .179
    frame:
        background None
        xalign .5
        yalign .5
        vbox:
            add "gui/phone_white.webp" at ModZoom(.85)
            xalign .5
            yalign .5
        vbox:
            xalign .5
            yalign .5
            imagebutton auto "gui/phone_white_power_%s.webp" focus_mask True action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')] at ModZoom(.85):
                tooltip "Shut off the phone"
        vbox:
            xalign .5
            yalign .5
            if battery_text != 0 and not renpy.get_screen('say') and not renpy.get_screen('choice'):
                imagebutton auto "gui/phone_white_home_%s.webp" focus_mask True:
                    at ModZoom(.85)
                    alternate [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                    if renpy.get_screen('phone_playstore_apppage'):
                        action [SetVariable('keyclose',False),Hide('phone_playstore_apppage'),Show('phone_playstore')]
                        tooltip "Go back to the store"
                    elif renpy.get_screen('phonescreen'):
                        action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)]
                        tooltip "Go back to the home-screen"
                    else:
                        action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]
                        tooltip "Turn off the phone"
        if renpy.get_screen('display_achievements'):
            hbox:
                xalign .5
                yalign .5
                add "gui/phone_bottom_overlay.webp" at ModZoom(.85)
            hbox:
                xalign .5
                yalign .818
                imagebutton auto "gui/phone_unlock_%s.webp":
                    action ToggleVariable('show_unlocked_achievements')
                    xpos -100
                imagebutton auto "gui/phone_lock_%s.webp":
                    action ToggleVariable('show_locked_achievements')
                    xalign .5
                imagebutton auto "gui/phone_hidden_%s.webp":
                    action ToggleVariable('show_hidden_achievements')
                    xpos 100

    if keyclose and renpy.get_screen('phonescreen'):
        if renpy.get_screen('show_text_msg'):
            key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Show('phone_text_screen')]
        else:
            key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens)]
    elif keyclose and renpy.get_screen('phone_playstore_apppage'):
        key "K_ESCAPE" action [SetVariable('keyclose',False),Hide('phone_playstore_apppage'),Show('phone_playstore')]
    else:
        key "K_ESCAPE" action [SetVariable('keyclose',False),SetVariable('show_icons',True),Function(hide_phone_screens),Hide('phone')]

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
            pagekeys True
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
                            if title == "Continue":
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


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    # properties gui.button_text_properties("help_button")
    color "#555"
    hover_color "#0cf"
    selected_color "#0cf"
    xalign .5

style help_label:
    xsize 375
    right_padding 30
    yalign .5

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

style help_text:
    yalign .5

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


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")