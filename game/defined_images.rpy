# image fm_standing ahead:
#     contains fm_standing_ahead_ani
#     zoom .75
#     yalign 1.0
#     xpos .6
#     ypos .55
#     xanchor .5
#     yanchor .5

# image fm_standing blushing:
#     contains fm_standing_blushing_ani
#     zoom .75
#     yalign 1.0
#     xpos .6
#     ypos .55
#     xanchor .5
#     yanchor .5

# image fm_standing crying:
#     contains fm_standing_crying_ani
#     zoom .75
#     yalign 1.0
#     xpos .6
#     ypos .55
#     xanchor .5
#     yanchor .5

# image fm_standing mad:
#     contains fm_standing_mad_ani
#     zoom .75
#     yalign 1.0
#     xpos .6
#     ypos .55
#     xanchor .5
#     yanchor .5

# image fm_standing sad:
#     contains fm_standing_sad_ani
#     zoom .75
#     yalign 1.0
#     xpos .6
#     ypos .55
#     xanchor .5
#     yanchor .5

# image fm_standing smile:
#     contains fm_standing_smile_ani
#     zoom .75
#     yalign 1.0
#     xpos .6
#     ypos .55
#     xanchor .5
#     yanchor .5

# transform active_talk:
#     alpha 0.0
#     linear .5 alpha 1.0
#     zoom 1.0
#     yalign 1.0
#     xpos .6
#     ypos .55
#     xanchor .5
#     yanchor .5
#     linear .4 zoom 1.05
#     linear .4 zoom 1.0

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

# transform fm_standing_blushing_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/blushing_night.webp",
#         True, "images/characters/anne/body/standing/blushing.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/blushing_eyes_closed_night.webp",
#         True, "images/characters/anne/body/standing/blushing_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fm_standing_crying_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/crying_night.webp",
#         True, "images/characters/anne/body/standing/crying.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/crying_eyes_closed_night.webp",
#         True, "images/characters/anne/body/standing/crying_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fm_standing_mad_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/mad_night.webp",
#         True, "images/characters/anne/body/standing/mad.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/mad_eyes_closed_night.webp",
#         True, "images/characters/anne/body/standing/mad_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fm_standing_sad_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/sad_night.webp",
#         True, "images/characters/anne/body/standing/sad.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/sad_eyes_closed_night.webp",
#         True, "images/characters/anne/body/standing/sad_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fm_standing_smile_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/smile_night.webp",
#         True, "images/characters/anne/body/standing/smile.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/anne/body/standing/smile_eyes_closed_night.webp",
#         True, "images/characters/anne/body/standing/smile_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_ahead_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/ahead_night.webp",
#         True, "images/characters/juliette/body/standing/ahead.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/ahead_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/ahead_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_blushing_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/blushing_night.webp",
#         True, "images/characters/juliette/body/standing/blushing.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/blushing_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/blushing_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_blushing_sad_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/blushing_sad_night.webp",
#         True, "images/characters/juliette/body/standing/blushing_sad.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/blushing_sad_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/blushing_sad_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_crying_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/crying_night.webp",
#         True, "images/characters/juliette/body/standing/crying.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/crying_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/crying_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_devious_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/devious_night.webp",
#         True, "images/characters/juliette/body/standing/devious.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/devious_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/devious_eyes_closed.webp"
#         )
#     pause .25
#     repeat


# transform fs_standing_flustered_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/flustered_night.webp",
#         True, "images/characters/juliette/body/standing/flustered.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/flustered_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/flustered_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_mad_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/mad_night.webp",
#         True, "images/characters/juliette/body/standing/mad.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/mad_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/mad_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_sad_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/sad_night.webp",
#         True, "images/characters/juliette/body/standing/sad.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/sad_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/sad_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_smile_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/smile_night.webp",
#         True, "images/characters/juliette/body/standing/smile.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/smile_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/smile_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# transform fs_standing_smile_open_ani:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/smile_open_night.webp",
#         True, "images/characters/juliette/body/standing/smile_open.webp"
#         )
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/smile_open_eyes_closed_night.webp",
#         True, "images/characters/juliette/body/standing/smile_open_eyes_closed.webp"
#         )
#     pause .25
#     repeat

# image fs_standing ahead:
#     contains fs_standing_ahead_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing annoyed:
#     ConditionSwitch(
#         "int(current_time[:2]) in night","images/characters/juliette/body/standing/annoyed_night.webp",
#         True, "images/characters/juliette/body/standing/annoyed.webp"
#         )
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing blushing:
#     contains fs_standing_blushing_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing blushing_sad:
#     contains fs_standing_blushing_sad_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing crying:
#     contains fs_standing_crying_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing devious:
#     contains fs_standing_devious_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing flustered:
#     contains fs_standing_flustered_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing mad:
#     contains fs_standing_mad_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing sad:
#     contains fs_standing_sad_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing smile:
#     contains fs_standing_smile_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image fs_standing smile_open:
#     contains fs_standing_smile_open_ani
#     zoom .65
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# transform nk_standing_ahead_ani:
#     "images/characters/karen/body/standing/ahead.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/ahead_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_blushing_ani:
#     "images/characters/karen/body/standing/blushing.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/blushing_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_blushing_sad_ani:
#     "images/characters/karen/body/standing/blushing_sad.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/blushing_sad_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_crying_ani:
#     "images/characters/karen/body/standing/crying.webp"
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/crying_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_devious_ani:
#     "images/characters/karen/body/standing/devious.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/devious_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_flustered_ani:
#     "images/characters/karen/body/standing/flustered.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/flustered_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_mad_ani:
#     "images/characters/karen/body/standing/mad.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/mad_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_sad_ani:
#     "images/characters/karen/body/standing/sad.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/sad_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_smile_ani:
#     "images/characters/karen/body/standing/smile.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/smile_eyes_closed.webp"
#     pause .25
#     repeat

# transform nk_standing_smile_open_ani:
#     "images/characters/karen/body/standing/smile_open.webp"
#     choice:
#         pause 2
#     choice:
#         pause 4
#     choice:
#         pause 6
#     "images/characters/karen/body/standing/smile_open_eyes_closed.webp"
#     pause .25
#     repeat

# image nk_standing ahead:
#     contains nk_standing_ahead_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing annoyed:
#     "images/characters/karen/body/standing/annoyed.webp"
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing blushing:
#     contains nk_standing_blushing_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing blushing_sad:
#     contains nk_standing_blushing_sad_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing crying:
#     contains nk_standing_crying_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing devious:
#     contains nk_standing_devious_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing flustered:
#     contains nk_standing_flustered_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing mad:
#     contains nk_standing_mad_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing sad:
#     contains nk_standing_sad_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing smile:
#     contains nk_standing_smile_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image nk_standing smile_open:
#     contains nk_standing_smile_open_ani
#     zoom .6
#     xpos .7
#     ypos 1.0
#     xanchor .5
#     yanchor .75

# image side fp_talkside:
#     "images/characters/marten/expressions/marten_hair_parted_ahead.webp"
#     zoom .7

# image side nr_talkside:
#     "images/characters/ron/expressions/ahead.webp"
#     zoom .7

# image side nr_talkside blushing:
#     "images/characters/ron/expressions/blushing.webp"
#     zoom .7

# image side fm_talkside ahead:
#     "images/characters/anne/expressions/ahead.webp"
#     zoom .7
# image side fm_talkside ahead_eyes_closed:
#     "images/characters/anne/expressions/ahead_eyes_closed.webp"
#     zoom .7
# image side fm_talkside blushing:
#     "images/characters/anne/expressions/blushing.webp"
#     zoom .7
# image side fm_talkside crying:
#     "images/characters/anne/expressions/crying.webp"
#     zoom .7
# image side fm_talkside mad:
#     "images/characters/anne/expressions/mad.webp"
#     zoom .7
# image side fm_talkside sad:
#     "images/characters/anne/expressions/sad.webp"
#     zoom .7
# image side fm_talkside smile:
#     "images/characters/anne/expressions/smile.webp"
#     zoom .7

# image side fs_talkside ahead:
#     "images/characters/juliette/expressions/ahead.webp"
#     zoom .7
# image side fs_talkside ahead_eyes_closed:
#     "images/characters/juliette/expressions/ahead_eyes_closed.webp"
#     zoom .7
# image side fs_talkside annoyed:
#     "images/characters/juliette/expressions/annoyed.webp"
#     zoom .7
# image side fs_talkside blushing:
#     "images/characters/juliette/expressions/blushing.webp"
#     zoom .7
# image side fs_talkside blushing_sad:
#     "images/characters/juliette/expressions/blushing_sad.webp"
#     zoom .7
# image side fs_talkside crying:
#     "images/characters/juliette/expressions/crying.webp"
#     zoom .7
# image side fs_talkside devious:
#     "images/characters/juliette/expressions/devious.webp"
#     zoom .7
# image side fs_talkside flustered:
#     "images/characters/juliette/expressions/flustered.webp"
#     zoom .7
# image side fs_talkside mad:
#     "images/characters/juliette/expressions/mad.webp"
#     zoom .7
# image side fs_talkside sad:
#     "images/characters/juliette/expressions/sad.webp"
#     zoom .7
# image side fs_talkside smile:
#     "images/characters/juliette/expressions/smile.webp"
#     zoom .7
# image side fs_talkside smile_open:
#     "images/characters/juliette/expressions/smile_open.webp"
#     zoom .7

# image side nk_talkside ahead:
#     "images/characters/karen/expressions/ahead.webp"
#     zoom .7
# image side nk_talkside annoyed:
#     "images/characters/karen/expressions/annoyed.webp"
#     zoom .7
# image side nk_talkside blushing:
#     "images/characters/karen/expressions/blushing.webp"
#     zoom .7
# image side nk_talkside blushing_sad:
#     "images/characters/karen/expressions/blushing_sad.webp"
#     zoom .7
# image side nk_talkside crying:
#     "images/characters/karen/expressions/crying.webp"
#     zoom .7
# image side nk_talkside devious:
#     "images/characters/karen/expressions/devious.webp"
#     zoom .7
# image side nk_talkside flustered:
#     "images/characters/karen/expressions/flustered.webp"
#     zoom .7
# image side nk_talkside mad:
#     "images/characters/karen/expressions/mad.webp"
#     zoom .7
# image side nk_talkside sad:
#     "images/characters/karen/expressions/sad.webp"
#     zoom .7
# image side nk_talkside smile:
#     "images/characters/karen/expressions/smile.webp"
#     zoom .7
# image side nk_talkside smile_open:
#     "images/characters/karen/expressions/smile_open.webp"
#     zoom .7

# image juliette_mad_pantless:
#     "images/characters/juliette/mad_pantless.webp"

# image juliette_reflection:
#     "images/backgrounds/upper_hallway_juliette_reflection.webp"

image books_on_dresser:
    "images/backgrounds/interactions_item/fp_bedroom_morning_dresser_idle.webp"

image livingroom_morning_bad_weather_windows:
    "images/backgrounds/livingroom_morning_bad_weather_windows.webp"

image juliette_shower:
    "images/backgrounds/upper_hallway_bathroom_juliette_shower_bubbles.webp"

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
    1
    "images/characters/juliette/scenes/juliette_intro_hallway_2_embarrassed.webp"
    0.5
    "images/characters/juliette/scenes/juliette_intro_hallway_3_turning_away.webp"
    0.5
    "images/characters/juliette/scenes/juliette_intro_hallway_4_moving_away.webp"
    zoom .70
    xoffset -400
    yoffset -100
    0.35
    "images/characters/juliette/scenes/juliette_intro_hallway_5_moving_away.webp"
    zoom .60
    xoffset -450
    yoffset -150
    0.4
    "images/characters/juliette/scenes/juliette_intro_hallway_4_moving_away.webp"
    zoom .55
    xoffset -500
    yoffset -200
    0.4
    "images/characters/juliette/scenes/juliette_intro_hallway_5_moving_away.webp"
    zoom .45
    xoffset -550
    yoffset -250
    0.4


layeredimage anne:
    pos(.75, 1.0)
    yoffset 180
    group base auto:
        attribute redcasual default

    group head auto:
        xoffset 188
        yoffset 26
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


image stats_hover:
    "gui/stats_hover.webp"

image tshirt_overlay:
    "gui/tshirt_overlay.webp"

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