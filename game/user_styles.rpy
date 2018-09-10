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

    style choice_button_disabled_evil:
        properties gui.button_properties('choice_button_disabled')
        # color "#F00"
        outlines [(absolute(1),"#F00",absolute(0),absolute(0))]

    style choice_button_disabled_good:
        properties gui.button_properties('choice_button_disabled')
        outlines [(absolute(1),"#3D3",absolute(0),absolute(0))]
        # color "#0F0"

    style choice_button_evil:
        properties gui.button_properties('choice_button')
        # color "#F00"
        outlines [(absolute(1),"#F00",absolute(0),absolute(0))]

    style choice_button_good:
        properties gui.button_properties('choice_button')
        outlines [(absolute(1),"#3D3",absolute(0),absolute(0))]
        # color "#0F0"

    style choice_button_disabled is default:
        properties gui.button_text_properties("choice_button_disabled")
        color "#aaaaaa"
    style menu_window is default

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

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

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    color "#fff"

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

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