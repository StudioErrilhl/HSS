image fm_standing ahead:
    contains fm_standing_ahead_ani
    zoom .75
    yalign 1.0
    xpos .6
    ypos .55
    xanchor .5
    yanchor .5

image fm_standing blushing:
    contains fm_standing_blushing_ani
    zoom .75
    yalign 1.0
    xpos .6
    ypos .55
    xanchor .5
    yanchor .5

image fm_standing crying:
    contains fm_standing_crying_ani
    zoom .75
    yalign 1.0
    xpos .6
    ypos .55
    xanchor .5
    yanchor .5

image fm_standing mad:
    contains fm_standing_mad_ani
    zoom .75
    yalign 1.0
    xpos .6
    ypos .55
    xanchor .5
    yanchor .5

image fm_standing sad:
    contains fm_standing_sad_ani
    zoom .75
    yalign 1.0
    xpos .6
    ypos .55
    xanchor .5
    yanchor .5

image fm_standing smile:
    contains fm_standing_smile_ani
    zoom .75
    yalign 1.0
    xpos .6
    ypos .55
    xanchor .5
    yanchor .5

transform active_talk:
    alpha 0.0
    linear .5 alpha 1.0
    zoom 1.0
    yalign 1.0
    xpos .6
    ypos .55
    xanchor .5
    yanchor .5
    linear .4 zoom 1.05
    linear .4 zoom 1.0

transform fm_standing_ahead_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/ahead_night.png",
        True,"images/characters/anne/body/standing/ahead.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/ahead_eyes_closed_night.png",
        True,"images/characters/anne/body/standing/ahead_eyes_closed.png"
    )
    pause .25
    repeat

transform fm_standing_blushing_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/blushing_night.png",
        True, "images/characters/anne/body/standing/blushing.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/blushing_eyes_closed_night.png",
        True, "images/characters/anne/body/standing/blushing_eyes_closed.png"
        )
    pause .25
    repeat

transform fm_standing_crying_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/crying_night.png",
        True, "images/characters/anne/body/standing/crying.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/crying_eyes_closed_night.png",
        True, "images/characters/anne/body/standing/crying_eyes_closed.png"
        )
    pause .25
    repeat

transform fm_standing_mad_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/mad_night.png",
        True, "images/characters/anne/body/standing/mad.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/mad_eyes_closed_night.png",
        True, "images/characters/anne/body/standing/mad_eyes_closed.png"
        )
    pause .25
    repeat

transform fm_standing_sad_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/sad_night.png",
        True, "images/characters/anne/body/standing/sad.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/sad_eyes_closed_night.png",
        True, "images/characters/anne/body/standing/sad_eyes_closed.png"
        )
    pause .25
    repeat

transform fm_standing_smile_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/smile_night.png",
        True, "images/characters/anne/body/standing/smile.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/anne/body/standing/smile_eyes_closed_night.png",
        True, "images/characters/anne/body/standing/smile_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_ahead_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/ahead_night.png",
        True, "images/characters/juliette/body/standing/ahead.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/ahead_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/ahead_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_blushing_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/blushing_night.png",
        True, "images/characters/juliette/body/standing/blushing.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/blushing_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/blushing_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_blushing_sad_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/blushing_sad_night.png",
        True, "images/characters/juliette/body/standing/blushing_sad.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/blushing_sad_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/blushing_sad_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_crying_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/crying_night.png",
        True, "images/characters/juliette/body/standing/crying.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/crying_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/crying_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_devious_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/devious_night.png",
        True, "images/characters/juliette/body/standing/devious.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/devious_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/devious_eyes_closed.png"
        )
    pause .25
    repeat


transform fs_standing_flustered_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/flustered_night.png",
        True, "images/characters/juliette/body/standing/flustered.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/flustered_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/flustered_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_mad_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/mad_night.png",
        True, "images/characters/juliette/body/standing/mad.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/mad_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/mad_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_sad_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/sad_night.png",
        True, "images/characters/juliette/body/standing/sad.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/sad_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/sad_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_smile_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/smile_night.png",
        True, "images/characters/juliette/body/standing/smile.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/smile_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/smile_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_smile_open_ani:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/smile_open_night.png",
        True, "images/characters/juliette/body/standing/smile_open.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/smile_open_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/smile_open_eyes_closed.png"
        )
    pause .25
    repeat

image fs_standing ahead:
    contains fs_standing_ahead_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing annoyed:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/characters/juliette/body/standing/annoyed_night.png",
        True, "images/characters/juliette/body/standing/annoyed.png"
        )
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing blushing:
    contains fs_standing_blushing_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing blushing_sad:
    contains fs_standing_blushing_sad_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing crying:
    contains fs_standing_crying_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing devious:
    contains fs_standing_devious_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing flustered:
    contains fs_standing_flustered_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing mad:
    contains fs_standing_mad_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing sad:
    contains fs_standing_sad_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing smile:
    contains fs_standing_smile_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image fs_standing smile_open:
    contains fs_standing_smile_open_ani
    zoom .65
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

transform nk_standing_ahead_ani:
    "images/characters/karen/body/standing/ahead.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/ahead_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_blushing_ani:
    "images/characters/karen/body/standing/blushing.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/blushing_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_blushing_sad_ani:
    "images/characters/karen/body/standing/blushing_sad.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/blushing_sad_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_crying_ani:
    "images/characters/karen/body/standing/crying.png"
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/crying_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_devious_ani:
    "images/characters/karen/body/standing/devious.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/devious_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_flustered_ani:
    "images/characters/karen/body/standing/flustered.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/flustered_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_mad_ani:
    "images/characters/karen/body/standing/mad.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/mad_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_sad_ani:
    "images/characters/karen/body/standing/sad.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/sad_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_smile_ani:
    "images/characters/karen/body/standing/smile.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/smile_eyes_closed.png"
    pause .25
    repeat

transform nk_standing_smile_open_ani:
    "images/characters/karen/body/standing/smile_open.png"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "images/characters/karen/body/standing/smile_open_eyes_closed.png"
    pause .25
    repeat

image nk_standing ahead:
    contains nk_standing_ahead_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing annoyed:
    "images/characters/karen/body/standing/annoyed.png"
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing blushing:
    contains nk_standing_blushing_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing blushing_sad:
    contains nk_standing_blushing_sad_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing crying:
    contains nk_standing_crying_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing devious:
    contains nk_standing_devious_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing flustered:
    contains nk_standing_flustered_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing mad:
    contains nk_standing_mad_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing sad:
    contains nk_standing_sad_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing smile:
    contains nk_standing_smile_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image nk_standing smile_open:
    contains nk_standing_smile_open_ani
    zoom .6
    xpos .7
    ypos 1.0
    xanchor .5
    yanchor .75

image side fp_talkside:
    "images/characters/marten/expressions/marten_hair_parted_ahead.png"
    zoom .7

image side nr_talkside:
    "images/characters/ron/expressions/ahead.png"
    zoom .7

image side nr_talkside blushing:
    "images/characters/ron/expressions/blushing.png"
    zoom .7

image side fm_talkside ahead:
    "images/characters/anne/expressions/ahead.png"
    zoom .7
image side fm_talkside ahead_eyes_closed:
    "images/characters/anne/expressions/ahead_eyes_closed.png"
    zoom .7
image side fm_talkside blushing:
    "images/characters/anne/expressions/blushing.png"
    zoom .7
image side fm_talkside crying:
    "images/characters/anne/expressions/crying.png"
    zoom .7
image side fm_talkside mad:
    "images/characters/anne/expressions/mad.png"
    zoom .7
image side fm_talkside sad:
    "images/characters/anne/expressions/sad.png"
    zoom .7
image side fm_talkside smile:
    "images/characters/anne/expressions/smile.png"
    zoom .7

image side fs_talkside ahead:
    "images/characters/juliette/expressions/ahead.png"
    zoom .7
image side fs_talkside ahead_eyes_closed:
    "images/characters/juliette/expressions/ahead_eyes_closed.png"
    zoom .7
image side fs_talkside annoyed:
    "images/characters/juliette/expressions/annoyed.png"
    zoom .7
image side fs_talkside blushing:
    "images/characters/juliette/expressions/blushing.png"
    zoom .7
image side fs_talkside blushing_sad:
    "images/characters/juliette/expressions/blushing_sad.png"
    zoom .7
image side fs_talkside crying:
    "images/characters/juliette/expressions/crying.png"
    zoom .7
image side fs_talkside devious:
    "images/characters/juliette/expressions/devious.png"
    zoom .7
image side fs_talkside flustered:
    "images/characters/juliette/expressions/flustered.png"
    zoom .7
image side fs_talkside mad:
    "images/characters/juliette/expressions/mad.png"
    zoom .7
image side fs_talkside sad:
    "images/characters/juliette/expressions/sad.png"
    zoom .7
image side fs_talkside smile:
    "images/characters/juliette/expressions/smile.png"
    zoom .7
image side fs_talkside smile_open:
    "images/characters/juliette/expressions/smile_open.png"
    zoom .7

image side nk_talkside ahead:
    "images/characters/karen/expressions/ahead.png"
    zoom .7
image side nk_talkside annoyed:
    "images/characters/karen/expressions/annoyed.png"
    zoom .7
image side nk_talkside blushing:
    "images/characters/karen/expressions/blushing.png"
    zoom .7
image side nk_talkside blushing_sad:
    "images/characters/karen/expressions/blushing_sad.png"
    zoom .7
image side nk_talkside crying:
    "images/characters/karen/expressions/crying.png"
    zoom .7
image side nk_talkside devious:
    "images/characters/karen/expressions/devious.png"
    zoom .7
image side nk_talkside flustered:
    "images/characters/karen/expressions/flustered.png"
    zoom .7
image side nk_talkside mad:
    "images/characters/karen/expressions/mad.png"
    zoom .7
image side nk_talkside sad:
    "images/characters/karen/expressions/sad.png"
    zoom .7
image side nk_talkside smile:
    "images/characters/karen/expressions/smile.png"
    zoom .7
image side nk_talkside smile_open:
    "images/characters/karen/expressions/smile_open.png"
    zoom .7

image juliette_mad_pantless:
    "images/characters/juliette/mad_pantless.png"

image juliette_reflection:
    "images/backgrounds/upper_hallway_juliette_reflection.png"

image books_on_dresser:
    "images/backgrounds/interactions_item/fp_bedroom_morning_dresser_idle.png"

image livingroom_morning_bad_weather_windows:
    "images/backgrounds/livingroom_morning_bad_weather_windows.png"

image rain:
    "images/rain1.png"
    0.2
    "images/rain2.png"
    0.25
    "images/rain3.png"
    0.2
    repeat

image black_car:
    ConditionSwitch(
        "int(current_time[:2]) in night","images/black_car_night_idle.png",
        True,"images/black_car_morning_idle.png"
        )

image stats_hover:
    "gui/stats_hover.png"

image tshirt_overlay:
    "gui/tshirt_overlay.png"

transform alpha_transform(a):
    alpha a

transform ModZoom(z):
    zoom z

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