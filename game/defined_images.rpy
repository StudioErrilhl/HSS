# transform fm_standing_ahead_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/ahead_night.webp",
#         True,"images/characters/anne/body/standing/ahead.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/ahead_eyes_closed_night.webp",
#         True,"images/characters/anne/body/standing/ahead_eyes_closed.webp"
#     )
#     pause .25
#     repeat

transform fpi_ani:
    "images/characters/marten/introanimation/fpi_1.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_2.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_3.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_4.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_5.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_6.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_7.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_8.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_9.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_8.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_7.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_6.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_5.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_4.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_3.webp"
    pause .1
    "images/characters/marten/introanimation/fpi_2.webp"
    pause .1
    repeat

transform fpi_falling_ani:
    "images/characters/multiple/animations/falling_00.webp" with Dissolve(.25)
    pause .5
    "images/characters/multiple/animations/falling_01.webp" with Dissolve(.25)
    pause .15
    "images/characters/multiple/animations/falling_02.webp" with Dissolve(.25)
    pause .15
    "images/characters/multiple/animations/falling_03.webp" with Dissolve(.25)
    pause .15
    "images/characters/multiple/animations/falling_04.webp" with Dissolve(.25)
    pause .15
    "images/characters/multiple/animations/falling_05.webp" with Dissolve(.25)
    pause .15
    "images/characters/multiple/animations/falling_06.webp" with Dissolve(.25)
    pause .15
    "images/characters/multiple/animations/falling_07.webp" with Dissolve(.25)
    pause .15
    "images/characters/multiple/animations/falling_08.webp" with Dissolve(.25)
    pause .15
    "images/characters/multiple/animations/falling_09.webp"
    pause .15
    block:
        "images/characters/multiple/animations/falling_10.webp"
        pause .1
        "images/characters/multiple/animations/falling_11.webp"
        pause .1
        "images/characters/multiple/animations/falling_12.webp"
        pause .1
        "images/characters/multiple/animations/falling_13.webp"
        pause .1
        "images/characters/multiple/animations/falling_14.webp"
        pause .1
        "images/characters/multiple/animations/falling_15.webp"
        pause .1
        repeat

transform ks_ani_1:
    "images/characters/anne/animations/kitchen_zoom_01.webp" with Dissolve(.1)
    pause .08
    "images/characters/anne/animations/kitchen_zoom_02.webp" with Dissolve(.1)
    pause .08
    "images/characters/anne/animations/kitchen_zoom_03.webp" with Dissolve(.1)
    pause .08
    "images/characters/anne/animations/kitchen_zoom_04.webp" with Dissolve(.1)
    pause .08
    "images/characters/anne/animations/kitchen_zoom_05.webp" with Dissolve(.1)
    pause .08
    "images/characters/anne/animations/kitchen_zoom_06.webp" with Dissolve(.1)
    pause .08

transform ks_ani_2:
    "images/characters/anne/animations/kitchen_zoom_07.webp" with Dissolve(.2)
    pause .15
    "images/characters/anne/animations/kitchen_zoom_08.webp" with Dissolve(.2)
    pause .15
    "images/characters/anne/animations/kitchen_zoom_09.webp" with Dissolve(.2)
    pause .15
    "images/characters/anne/animations/kitchen_zoom_10.webp" with Dissolve(.2)
    pause .15
    "images/characters/anne/animations/kitchen_zoom_11.webp" with Dissolve(.2)
    pause .15
    "images/characters/anne/animations/kitchen_zoom_12.webp" with Dissolve(.2)
    pause .15
    "images/characters/anne/animations/kitchen_zoom_13.webp" with Dissolve(.2)
    pause .15
    "images/characters/anne/animations/kitchen_zoom_14.webp" with Dissolve(.2)
    pause .15
    "images/characters/anne/animations/kitchen_zoom_15.webp" with Dissolve(.2)
    pause .15

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

image livingroom_morning_bad_weather_windows:
    "images/backgrounds/livingroom_morning_bad_weather_windows.webp"

image juliette_shower:
    "images/characters/juliette/scenes/upper_hallway_bathroom_juliette_shower_bubbles.webp"

image juliette_shower_night:
    "images/backgrounds/upper_hallway_bathroom_night_juliette_shower_bubbles.webp"

image rain:
    "images/rain1.webp"
    0.2
    "images/rain2.webp"
    0.25
    "images/rain3.webp"
    0.2
    repeat

image black_car:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/black_car_night_idle.webp",
        True,"images/black_car_morning_idle.webp"
        )

image juliette_intro:
    "images/characters/juliette/scenes/juliette_intro_hallway_1_angry.webp"
    zoom .8
    xoffset -320
    yoffset 0

image juliette_intro_ani:
    "images/characters/juliette/scenes/juliette_intro_hallway_1_angry.webp"
    zoom .8
    xoffset -320
    yoffset 0
    .35
    "images/characters/juliette/scenes/juliette_intro_hallway_2_embarrassed.webp"
    0.25
    "images/characters/juliette/scenes/juliette_intro_hallway_3_turning_away.webp"
    0.2
    "images/characters/juliette/scenes/juliette_intro_hallway_4_moving_away.webp"
    zoom .70
    xoffset -400
    yoffset -100
    0.2
    "images/characters/juliette/scenes/juliette_intro_hallway_5_moving_away.webp"
    zoom .60
    xoffset -450
    yoffset -150
    0.2
    "images/characters/juliette/scenes/juliette_intro_hallway_4_moving_away.webp"
    zoom .55
    xoffset -500
    yoffset -200
    0.1
    "images/characters/juliette/scenes/juliette_intro_hallway_5_moving_away.webp"
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

    if fp_sofa_aquired:
        "fpbm_sofa_idle"

    if wallart['ferrari']:
        "wallart_ferrari_morning_idle"

    if wallart['parkinglot']:
        "wallart_parkinglot_morning_idle"

    if wallart['peekaboo']:
        "wallart_peekaboo_morning_idle"

    if wallart['roadtrip']:
        "wallart_roadtrip_morning_idle"

    if wallart['sincity']:
        "wallart_sincity_morning_idle"

layeredimage fp_bedroom_night:
    always:
        "fpbn_empty"

    if not carry_phone:
        "fp_bedroom_night_phone_idle"

    if not carry_backpack:
        "fp_bedroom_day_backpack_idle"

    if not carry_wallet:
        "fp_bedroom_night_wallet_idle"

    if not backpack.has_item(schoolbooks_item):
        "fp_bedroom_night_dresser_idle"

    if fp_sofa_aquired:
        "fpbn_sofa_idle"

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

    # group eyes auto:
    #     attribute eo default

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