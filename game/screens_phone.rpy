screen phone():
    # modal True
    add Solid("#000000DF")
    tag menu
    zorder 999
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
            yoffset -8

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
                        xoffset 4
                    imagebutton auto "gui/phone_button_alarm_clock_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_alarm')] at ModZoom(.9):
                        tooltip "Set the alarm"
                        # xoffset -48
                        xoffset 4
                    imagebutton auto "gui/phone_button_playstore_%s.webp" focus_mask True action [SetVariable('show_icons',False),Function(randomize_appstorelists),Show('phone_playstore')] at ModZoom(.9):
                        tooltip "Go to the PlayStore"
                        # xoffset -96
                        xoffset 4
                    if installedFF:
                        imagebutton auto "gui/phone_button_friendfinder_%s.webp" focus_mask True action [SetVariable('show_icons',False),Show('phone_friendfinder')] at ModZoom(.9):
                            tooltip "Open FriendFinder"
                            xsize 70
                    else:
                        imagebutton idle "gui/phone_button_empty_idle.webp" focus_mask True action NullAction()
                    imagebutton idle "gui/phone_button_empty_idle.webp" focus_mask True action NullAction()

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
    default updatepercentage = False
    default installedapp = False
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
                    if appselect[4] != 'not_a_link':
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
                    else:
                        if updatepercentage:
                            text "Installing: ":
                                xalign .25
                                color "#333"
                                size 16
                                xoffset -25
                            bar value AnimatedValue(100.0,100.0,4.0,0.0) at ModZoom(.5):
                                xalign .75
                                yoffset -20
                            timer 4.0 action [SetScreenVariable('installedapp',True),SetVariable('installedFF',True)]
                        if not installedapp:
                            button:
                                add "gui/phone_button_install_idle.webp":
                                    xalign .5
                                text "Install app":
                                    size 18
                                    yoffset 10
                                    xalign .5
                                action SetScreenVariable('updatepercentage',True)
                        else:
                            button:
                                add "gui/phone_button_installed_idle.webp":
                                    xalign .5
                                text "App is installed":
                                    color "#333"
                                    size 20
                                    xalign .5
                                action NullAction()

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
        yalign .55
        add "gui/phone_background_contacts.webp" at ModZoom(.9):
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
                yoffset -45
                text "{b}All Messages{/b}":
                    text_align .5
                    xalign .5
                    color "#fff"
                    size 20
            viewport:
                mousewheel True
                pagekeys True
                # ypos 28
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
        yalign .55
        add "gui/phone_background_contacts.webp" at ModZoom(.9):
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
                yoffset -45
                text "{b}All Messages from [char]{/b}":
                    text_align .5
                    xalign .5
                    color "#fff"
                    size 20
            viewport:
                mousewheel True
                pagekeys True
                # ypos 28
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
                                        action [Function(read_message,k,b,v),Function(not_in_contacts.remove,'nc'),Function(disable_hint,"You need to wait for "+nr.name+" to send you "+nc.name+"'s info"),Function(set_hint,"You've gotten the info from "+nr.name+". Maybe you should try calling "+nc.name+""),Hide('show_text_msg'),Show('phone_text_screen')]
                                        tooltip "Click to add to contacts"
                                    else:
                                        action [Function(read_message,k,b,v),Function(disable_hint,"You need to wait for "+nr.name+" to send you "+nc.name+"'s info"),Function(set_hint,"You've gotten the info from "+nr.name+". Maybe you should try calling "+nc.name+""),Hide('show_text_msg'),Show('phone_text_screen')]
                                else:
                                    action [Function(read_message,k,b,v),Hide('show_text_msg'),Show('phone_text_screen')]

                        # if nc_call_after_hacker:
                        #     if k == 'nc':
                        #         $ print('test')

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
        # background None
        add "gui/phone_background_black.webp" at ModZoom(.85):
            yalign .5
            xalign .5
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
            if not calling_out:
                vbox:
                    style_prefix "skip"
                    xsize 370
                    ysize 100
                    yoffset 50
                    xalign .5
                if duringcall:
                    hbox:
                        spacing 9
                        xalign .5
                        text _("Call connected") style "skip_triangle_call"
                if not calling and not duringcall:
                    imagebutton auto "gui/phone_call_%s.webp" focus_mask True:
                        action [SetVariable('duringcall',True),Call(label,event=event)]
                        xalign .5
            else:
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
            tooltip "Put the phone down"
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
            xalign .5
            vpgrid:
                cols 3
                spacing 4
                xalign .5
                for file in renpy.list_files():
                    if file.startswith('images/phone_gallery/') and file.endswith('.webp'):
                        $ name = file.replace('images/phone_gallery/','')
                        frame:
                            background None
                            xsize 120
                            ysize 120
                            if name in images_unlocked:
                                imagebutton idle Transform(file,maxsize=(110,110)):
                                    xalign .5
                                    yalign .5
                                    action [SetVariable('current_file',file),SetVariable('show_icons',False),Hide('phone_gallery_screen'),Show('phone_gallery_show')]
                            else:
                                imagebutton idle Transform(file,maxsize=(110,110),alpha=.2):
                                    xalign .5
                                    yalign .5
                                    action NullAction()
                        if 'portrait' in name:
                            $ pgs += 1
                        else:
                            $ pgs += 2
                        if pgs >= 3:
                            $ pgs = 0
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
            tooltip "Put the phone down"
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
                tooltip "Put the phone down"
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
                                if installedFF:
                                    hbox:
                                        xpos .2
                                        imagebutton auto "gui/phone_button_friendfinder_%s.webp" focus_mask True action [Hide('phone_info_screen'),Show('phone_friendfinder')] at ModZoom(.6):
                                            yalign .5
                                        textbutton "Friendfinder" action [Hide('phone_info_screen'),Show('phone_friendfinder')]:
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
    zorder 999
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
                                        ysize 180
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
                                    add "gui/phone_lock_red_idle.webp":
                                        xpos 300
                                        ypos 35
                                    if selected_achievement == achievement:
                                        ysize 180
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
                                    add "gui/phone_unlock_green_idle.webp":
                                        xpos 300
                                        ypos 35
                                    if selected_achievement == achievement:
                                        ysize 180
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
    zorder 999
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
                tooltip "Put the phone down"
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
                tooltip "Put the phone down"
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
                        tooltip "Put the phone down"
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
                    tooltip "Show unlocked achievements"
                imagebutton auto "gui/phone_lock_%s.webp":
                    action ToggleVariable('show_locked_achievements')
                    xalign .5
                    tooltip "Show locked achievements"
                imagebutton auto "gui/phone_hidden_%s.webp":
                    action ToggleVariable('show_hidden_achievements')
                    xpos 100
                    tooltip "Show hidden achievements"

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