transform fs_dream_intro_ani:
    "images/dreams/fs_dream_intro.webp"
    pause .5
    Solid("#000")
    pause .5
    repeat(3)

transform fpi_ani:
    "images/characters/fp/introanimation/fpi_1.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_2.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_3.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_4.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_5.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_6.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_7.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_8.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_9.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_8.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_7.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_6.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_5.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_4.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_3.webp"
    pause .1
    "images/characters/fp/introanimation/fpi_2.webp"
    pause .1
    repeat

transform fpi_falling_ani:
    "images/characters/multiple/animations/falling_00.webp" with Dissolve(.25)
    pause .25
    "images/characters/multiple/animations/falling_01.webp" with Dissolve(.25)
    pause .08
    "images/characters/multiple/animations/falling_02.webp" with Dissolve(.25)
    pause .08
    "images/characters/multiple/animations/falling_03.webp" with Dissolve(.25)
    pause .08
    "images/characters/multiple/animations/falling_04.webp" with Dissolve(.25)
    pause .08
    "images/characters/multiple/animations/falling_05.webp" with Dissolve(.25)
    pause .08
    "images/characters/multiple/animations/falling_06.webp" with Dissolve(.25)
    pause .08
    "images/characters/multiple/animations/falling_07.webp" with Dissolve(.25)
    pause .08
    "images/characters/multiple/animations/falling_08.webp" with Dissolve(.25)
    pause .08
    "images/characters/multiple/animations/falling_09.webp"
    pause .08
    block:
        "images/characters/multiple/animations/falling_10.webp"
        pause .08
        "images/characters/multiple/animations/falling_11.webp"
        pause .08
        "images/characters/multiple/animations/falling_12.webp"
        pause .08
        "images/characters/multiple/animations/falling_13.webp"
        pause .08
        "images/characters/multiple/animations/falling_14.webp"
        pause .08
        "images/characters/multiple/animations/falling_15.webp"
        pause .08
        repeat

transform ks_ani_1:
    "images/characters/fm/animations/kitchen_spill_01.webp" with Dissolve(.1)
    pause .08
    "images/characters/fm/animations/kitchen_spill_02.webp" with Dissolve(.1)
    pause .08
    "images/characters/fm/animations/kitchen_spill_03.webp" with Dissolve(.1)
    pause .08
    "images/characters/fm/animations/kitchen_spill_04.webp" with Dissolve(.1)
    pause .08
    "images/characters/fm/animations/kitchen_spill_05.webp" with Dissolve(.1)
    pause .08
    "images/characters/fm/animations/kitchen_spill_06.webp" with Dissolve(.1)
    pause .08

transform ks_ani_2:
    "images/characters/fm/animations/kitchen_spill_07.webp" with Dissolve(.2)
    pause .15
    "images/characters/fm/animations/kitchen_spill_08.webp" with Dissolve(.2)
    pause .15
    "images/characters/fm/animations/kitchen_spill_09.webp" with Dissolve(.2)
    pause .15
    "images/characters/fm/animations/kitchen_spill_10.webp" with Dissolve(.2)
    pause .15
    "images/characters/fm/animations/kitchen_spill_11.webp" with Dissolve(.2)
    pause .15
    "images/characters/fm/animations/kitchen_spill_12.webp" with Dissolve(.2)
    pause .15
    "images/characters/fm/animations/kitchen_spill_13.webp" with Dissolve(.2)
    pause .15
    "images/characters/fm/animations/kitchen_spill_14.webp" with Dissolve(.2)
    pause .15
    "images/characters/fm/animations/kitchen_spill_15.webp" with Dissolve(.2)
    pause .15

image fs_dream_intro:
    contains fs_dream_intro_ani

image fpintro:
    contains fpi_ani

image fpfalling:
    contains fpi_falling_ani

image kitchenspill_1:
    contains ks_ani_1

image kitchenspill_2:
    contains ks_ani_2

image books_on_dresser:
    "images/backgrounds/interaction_items/fp_bedroom_morning_dresser_idle.webp"

image juliette_shower:
    "images/characters/fs/scenes/upper_hallway_bathroom_juliette_shower_bubbles.webp"

image juliette_shower_night:
    "images/backgrounds/ufbn_juliette_shower_bubbles.webp"

image rain:
    "images/rain1.webp"
    0.2
    "images/rain2.webp"
    0.25
    "images/rain3.webp"
    0.2
    repeat

image juliette_intro:
    "images/characters/fs/scenes/juliette_intro_hallway_1_angry.webp"
    zoom .8
    xoffset -320
    yoffset 0

image juliette_intro_ani:
    "images/characters/fs/scenes/juliette_intro_hallway_1_angry.webp"
    zoom .8
    xoffset -320
    yoffset 0
    .35
    "images/characters/fs/scenes/juliette_intro_hallway_2_embarrassed.webp"
    0.25
    "images/characters/fs/scenes/juliette_intro_hallway_3_turning_away.webp"
    0.2
    "images/characters/fs/scenes/juliette_intro_hallway_4_moving_away.webp"
    zoom .70
    xoffset -400
    yoffset -100
    0.2
    "images/characters/fs/scenes/juliette_intro_hallway_5_moving_away.webp"
    zoom .60
    xoffset -450
    yoffset -150
    0.2
    "images/characters/fs/scenes/juliette_intro_hallway_4_moving_away.webp"
    zoom .55
    xoffset -500
    yoffset -200
    0.1
    "images/characters/fs/scenes/juliette_intro_hallway_5_moving_away.webp"
    zoom .45
    xoffset -550
    yoffset -250
    0.1

layeredimage upper_floor_bathroom_morning:
    always:
        "upfm"

layeredimage upper_floor_bathroom_morning_sink:
    always:
        "upfm_st"

layeredimage fp_garage_fb_morning:
    if mc_b < 15:
        "gm_fb_00"
    elif mc_b < 30:
        "gm_fb_10"
    elif mc_b < 45:
        "gm_fb_20"
    elif mc_b < 60:
        "gm_fb_30"
    elif mc_b < 75:
        "gm_fb_40"
    elif mc_b < 85:
        "gm_fb_50"
    elif mc_b < 95:
        "gm_fb_60"
    elif mc_b < 105:
        "gm_fb_70"
    elif mc_b < 115:
        "gm_fb_80"
    elif mc_b < 125:
        "gm_fb_85"
    elif mc_b < 135:
        "gm_fb_90"
    elif mc_b < 140:
        "gm_fb_95"
    elif mc_b < 150:
        "gm_fb_100"
    elif mc_b == 150:
        "gm_fb_finished"

    if backpack.has_item(toolbox_item) and mc_b < 15:
        "gm_fb_00_toolbox"
    elif backpack.has_item(toolbox_item) and mc_b < 75:
        "gm_fb_10_toolbox"
    elif backpack.has_item(toolbox_item) and mc_b < 125:
        "gm_fb_90_toolbox"
    elif backpack.has_item(toolbox_item) and mc_b < 150:
        "gm_fb_95_toolbox"
    elif backpack.has_item(toolbox_item) and mc_b == 150:
        "gm_fb_finished_toolbox"

layeredimage fp_garage_fb_night:
    if mc_b < 15:
        "gn_fb_00"
    elif mc_b < 30:
        "gn_fb_10"
    elif mc_b < 45:
        "gn_fb_20"
    elif mc_b < 60:
        "gn_fb_30"
    elif mc_b < 75:
        "gn_fb_40"
    elif mc_b < 85:
        "gn_fb_50"
    elif mc_b < 95:
        "gn_fb_60"
    elif mc_b < 105:
        "gn_fb_70"
    elif mc_b < 115:
        "gn_fb_80"
    elif mc_b < 125:
        "gn_fb_85"
    elif mc_b < 135:
        "gn_fb_90"
    elif mc_b < 140:
        "gn_fb_95"
    elif mc_b < 150:
        "gn_fb_100"
    elif mc_b == 150:
        "gn_fb_finished"

    if backpack.has_item(toolbox_item) and mc_b < 15:
        "gn_fb_00_toolbox"
    elif backpack.has_item(toolbox_item) and mc_b < 125:
        "gn_fb_10_toolbox"
    elif backpack.has_item(toolbox_item) and mc_b < 135:
        "gn_fb_90_toolbox"
    elif backpack.has_item(toolbox_item) and mc_b < 150:
        "gn_fb_95_toolbox"
    elif backpack.has_item(toolbox_item) and mc_b == 150:
        "gn_fb_finished_toolbox"

layeredimage fp_bedroom_morning:
    always:
        "fpbm_empty"

    if not carry_phone:
        "fp_bedroom_morning_phone_idle"

    if not carry_backpack:
        "fp_bedroom_day_backpack_idle"

    if not carry_wallet:
        "fp_bedroom_morning_wallet_idle"

    if not backpack.has_item(schoolbooks_item):
        "fp_bedroom_morning_dresser_idle"

    if fp_couch_aquired:
        "fpbm_couch_idle"

    if active_wallart == 'ferrari':
        "wallart_ferrari_morning_idle"

    if active_wallart == 'parkinglot':
        "wallart_parkinglot_morning_idle"

    if active_wallart == 'peekaboo':
        "wallart_peekaboo_morning_idle"

    if active_wallart == 'roadtrip':
        "wallart_roadtrip_morning_idle"

    if active_wallart == 'sincity':
        "wallart_sincity_morning_idle"

layeredimage fp_bedroom_night:
    always:
        "fpbn_empty"

    if not carry_phone:
        "fp_bedroom_night_phone_idle"

    if not carry_backpack:
        "fp_bedroom_night_backpack_idle"

    if not carry_wallet:
        "fp_bedroom_night_wallet_idle"

    if not backpack.has_item(schoolbooks_item):
        "fp_bedroom_night_dresser_idle"

    if fp_couch_aquired:
        "fpbn_couch_idle"

    if wallart['ferrari']:
        "wallart_ferrari_night_idle"

    if wallart['parkinglot']:
        "wallart_parkinglot_night_idle"

    if wallart['peekaboo']:
        "wallart_peekaboo_night_idle"

    if wallart['roadtrip']:
        "wallart_roadtrip_night_idle"

    if wallart['sincity']:
        "wallart_sincity_night_idle"

layeredimage marten:
    pos(.25,1.0)
    yoffset 180
    group base auto:
        attribute regoutfit default

    group head auto:
        xoffset 195
        yoffset 32
        attribute ahead default null

    group eyes if_any "angry" auto variant "closed" prefix "angry"
    group eyes if_any "ahead" auto variant "closed" prefix "ahead"

layeredimage anne:
    pos(.75, 1.0)
    yoffset 180
    group base auto:
        attribute redcasual default

    group head auto:
        xoffset 202
        yoffset 12
        attribute ahead default null

    group eyes if_any "angry" auto variant "closed" prefix "angry"
    group eyes if_any "ahead" auto variant "closed" prefix "ahead"

layeredimage jules:
    pos (.75, 1.0)
    yoffset 140
    group base auto:
        attribute jeans default

    group head auto:
        xoffset 188
        yoffset 26
        attribute ahead default null

    group eyes if_any "angry" auto variant "closed" prefix "angry"
    group eyes if_any "ahead" auto variant "closed" prefix "ahead"

layeredimage side jules:
    group outfit auto:
        attribute jeans default

    group head auto:
        xoffset 164
        yoffset 106
        attribute ahead default

    group eyes if_any "angry" auto variant "closed" prefix "angry"
    group eyes if_any "ahead" auto variant "closed" prefix "ahead"

layeredimage karen:
    pos (.75,1.0)
    yoffset 140
    group base auto:
        attribute outside default

    group head auto:
        xoffset 190
        yoffset 60
        attribute ahead default null

    group eyes if_any "angry" auto variant "closed" prefix "angry"
    group eyes if_any "ahead" auto variant "closed" prefix "ahead"

layeredimage ron:
    pos (.75,1.0)
    yoffset 140
    group base auto:
        attribute regoutfit default

    group head auto:
        xoffset 190
        yoffset 60
        attribute ahead default null

    group eyes if_any "angry" auto variant "closed" prefix "angry"
    group eyes if_any "ahead" auto variant "closed" prefix "ahead"

image bar_fill:
    "gui/animated_bar_value_fill.webp"
    zoom .5
image bar_empty:
    "gui/animated_bar_value_empty.webp"
    zoom .5

image stats_hover:
    "gui/stats_hover.webp"

image tshirt_overlay:
    "gui/tshirt_overlay.webp"

define flash = Fade(0.1, 1.0, 0.5, color="#000")

define cumflash = MultipleTransition([
    False, Fade(0.1,0.0,0.5, color="#FFF"),
    True, Fade(0.1,0.0,0.5, color="#FFF"),
    True, Fade(0.1,0.0,0.5, color="#FFF"),
    True])

transform alpha_transform(a):
    alpha a

transform ModZoom(z):
    zoom z

transform Shake(z):
    block:
        linear 0.075 zoom z-.1
        linear 0.075 zoom z+.1
        repeat(5)
    zoom z

transform ModOffsetX(x):
    xoffset x

transform ModOffsetY(y):
    yoffset y

transform easeIn(t):
    # easein t
    linear .35 zoom 1.05

transform stats_hover_transform:
    yalign 0.0

transform tshirt_overlay_transform:
    yalign 0.0
    yoffset 9
    xoffset 105

transform diagonal_pan_up:
    zoom .8
    yalign 1.0
    xalign 1.0
    linear 5.0 yalign 0.0 xalign 0.0

transform diagonal_pan_down:
    zoom .8
    yalign 0.0
    xalign 0.0
    linear 5.0 yalign 1.0 xalign 1.0

transform vertical_pan_from_bottom:
    yalign 1.0
    linear 4.0 yalign 0.0

transform center_transform:
    yalign 1.0
    xpos .6
    ypos .55
    xanchor .5
    yanchor .5

transform achievement_transform:
    on show:
        xalign 1.2
        yalign .22
        linear 1.0 xalign 0.9 yalign .22
    on hide:
        linear 1.2 alpha 0.0

transform hide_transform:
    on show:
        xalign .5
        yalign 1.2
        linear 1.0 xalign .5 yalign 1.0
    on hide:
        linear 1.0 alpha 0.0