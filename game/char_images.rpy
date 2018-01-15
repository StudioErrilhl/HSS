# image side fm_talkside ahead = ConditionSwitch(
#                                 "fm_aro >= 30", im.Flip("images/characters/anne/expressions/unbuttoned_straight_ahead.png",horizontal=True),
#                                 True, im.Flip("images/characters/anne/expressions/buttoned_straight_ahead.png",horizontal=True)
#                                 )

image fm_standing ahead:
    ConditionSwitch(
        "fm_aro >= 30", "images/characters/anne/body/standing/unbuttoned_straight_ahead.png",
        True, "images/characters/anne/body/standing/buttoned_straight_ahead.png",
        )
    zoom .7
    yalign 1.0
    xpos .6
    ypos .70
    xanchor .5
    yanchor .5

image fm_standing ahead flip:
    ConditionSwitch(
        "fm_aro >= 30", im.Flip("images/characters/anne/body/standing/unbuttoned_straight_ahead.png",horizontal=True),
        True, im.Flip("images/characters/anne/body/standing/buttoned_straight_ahead.png",horizontal=True)
        )
    zoom .7
    yalign 1.0
    xpos .6
    ypos .70
    xanchor .5
    yanchor .5

transform fs_standing_ahead_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/ahead_night.png",
        True, "images/characters/juliette/body/standing/ahead.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/ahead_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/ahead_eyes_closed.png"
        )
    pause .25
    repeat

# transform fs_talkside_ahead:
#     "images/characters/juliette/expressions/ahead.png"
#     choice:
#         pause 2
#         # c = 2
#     choice:
#         pause 4
#         # c = 4
#     choice:
#         pause 6
#         # c = 6
#     "images/characters/juliette/expressions/ahead_eyes_closed.png"
#     pause .25
#     repeat

transform fs_standing_blushing_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/blushing_night.png",
        True, "images/characters/juliette/body/standing/blushing.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/blushing_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/blushing_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_blushing_sad_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/blushing_sad_night.png",
        True, "images/characters/juliette/body/standing/blushing_sad.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/blushing_sad_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/blushing_sad_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_crying_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/crying_night.png",
        True, "images/characters/juliette/body/standing/crying.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/crying_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/crying_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_devious_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/devious_night.png",
        True, "images/characters/juliette/body/standing/devious.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/devious_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/devious_eyes_closed.png"
        )
    pause .25
    repeat


transform fs_standing_flustered_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/flustered_night.png",
        True, "images/characters/juliette/body/standing/flustered.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/flustered_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/flustered_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_mad_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/mad_night.png",
        True, "images/characters/juliette/body/standing/mad.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/mad_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/mad_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_sad_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/sad_night.png",
        True, "images/characters/juliette/body/standing/sad.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/sad_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/sad_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_smile_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/smile_night.png",
        True, "images/characters/juliette/body/standing/smile.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/smile_eyes_closed_night.png",
        True, "images/characters/juliette/body/standing/smile_eyes_closed.png"
        )
    pause .25
    repeat

transform fs_standing_smile_open_ani:
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/smile_open_night.png",
        True, "images/characters/juliette/body/standing/smile_open.png"
        )
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    ConditionSwitch(
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/smile_open_eyes_closed_night.png",
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
        "int(current_hour[:2]) in night","images/characters/juliette/body/standing/annoyed_night.png",
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

# image fm_standing ahead:
#     ConditionSwitch(
#         "fm_aro >= 30", "images/characters/anne/body/standing/unbuttoned_straight_ahead.png",
#         True, "images/characters/anne/body/standing/buttoned_straight_ahead.png"
#         )
#     zoom .7
#     yalign 1.0
#     xpos .6
#     ypos .70
#     xanchor .5
#     yanchor .5

image side fs_talkside ahead:
    "images/characters/juliette/expressions/ahead.png"
    zoom .8
image side fs_talkside ahead_eyes_closed:
    "images/characters/juliette/expressions/ahead_eyes_closed.png"
    zoom .8
image side fs_talkside annoyed:
    "images/characters/juliette/expressions/annoyed.png"
    zoom .8
image side fs_talkside blushing:
    "images/characters/juliette/expressions/blushing.png"
    zoom .8
image side fs_talkside blushing_sad:
    "images/characters/juliette/expressions/blushing_sad.png"
    zoom .8
image side fs_talkside crying:
    "images/characters/juliette/expressions/crying.png"
    zoom .8
image side fs_talkside devious:
    "images/characters/juliette/expressions/devious.png"
    zoom .8
image side fs_talkside flustered:
    "images/characters/juliette/expressions/flustered.png"
    zoom .8
image side fs_talkside mad:
    "images/characters/juliette/expressions/mad.png"
    zoom .8
image side fs_talkside sad:
    "images/characters/juliette/expressions/sad.png"
    zoom .8
image side fs_talkside smile:
    "images/characters/juliette/expressions/smile.png"
    zoom .8
image side fs_talkside smile_open:
    "images/characters/juliette/expressions/smile_open.png"
    zoom .8

image side nk_talkside ahead:
    "images/characters/karen/expressions/ahead.png"
    zoom .8
image side nk_talkside annoyed:
    "images/characters/karen/expressions/annoyed.png"
    zoom .8
image side nk_talkside blushing:
    "images/characters/karen/expressions/blushing.png"
    zoom .8
image side nk_talkside blushing_sad:
    "images/characters/karen/expressions/blushing_sad.png"
    zoom .8
image side nk_talkside crying:
    "images/characters/karen/expressions/crying.png"
    zoom .8
image side nk_talkside devious:
    "images/characters/karen/expressions/devious.png"
    zoom .8
image side nk_talkside flustered:
    "images/characters/karen/expressions/flustered.png"
    zoom .8
image side nk_talkside mad:
    "images/characters/karen/expressions/mad.png"
    zoom .8
image side nk_talkside sad:
    "images/characters/karen/expressions/sad.png"
    zoom .8
image side nk_talkside smile:
    "images/characters/karen/expressions/smile.png"
    zoom .8
image side nk_talkside smile_open:
    "images/characters/karen/expressions/smile_open.png"
    zoom .8

image juliette_mad_pantless:
    "images/characters/juliette/mad_pantless.png"

image juliette_reflection:
    "images/backgrounds/upper_hallway_juliette_reflection.png"    

image books_on_dresser:
    "images/backgrounds/interactions_item/fp_bedroom_morning_dresser_idle.png"

image rain:
    "images/rain1.png"
    0.2
    "images/rain2.png"
    0.25
    "images/rain3.png"
    0.2
    repeat

transform ModZoom(z):
    zoom z    