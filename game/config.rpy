init python:
    import os
    def define_images(characterImageFolder, excludeFirstXFolders=0, flip=True):
        for path in renpy.list_files():
            if path.startswith(characterImageFolder + "/"):
                path_list = path.split("/")
                path_list[-1] = os.path.splitext(path_list[-1])[0]
                path_list = tuple(path_list[excludeFirstXFolders:])
                renpy.image(path_list, path)
                if flip:
                    renpy.image(path_list + ("flip", ), im.Flip(path, horizontal=True))

init -30 python:
    from datetime import time
    persistent.patch_installed = False
init -10 python:
    if persistent.patch_installed and not persistent.patch_first_time:
        persistent.patch_enabled = True
        persistent.patch_first_time = True
    elif not persistent.patch_installed:
        persistent.patch_first_time = False
        persistent.patch_enabled = False

define fp = Character("[fpinput]")
# define fM = Character("[CapsfM]",image="fm_talkside")
define fm = Character("[fmName.Formal]")
define fs = Character("[fsName.Formal]",image="fs_talkside")
define nb = Character("Bridget")
define nr = Character("Ron") 
define nk = Character("Karen",image="nk_talkside")
define sn = Character("Miss Novak")
define sp = Character("Principal Hudson")
define sj = Character("Jack")
define scn = Character("Natalie")
define scm = Character("Mattie")
#remember to add default color="#000000" if the character do not have a namebox_charname.png in the gui/-directory

default chars = [[fp,"fp"],[fm,"fm"],[fs,"fs"],[nb,"nb"],[nr,"nr"],[nk,"nk"],[sn,"sn"],[sp,"sp"],[sj,"sj"]]
default atts = ['rel','dom','aro','cor','att']

#main character
default fp_att = 0
default fp_aro = 0
default fp_sts = 0
default fpshower = False
default fpsink = False
default punishment_late = 0 #this is the variable for punishment value for lateness at school - reach too high a number, and [fM] is called, and her relationship stat decrease
default shitty_morning = False

#mother
default fm_dom = 0
default fm_rel = 10
default fm_aro = 0
default fm_cor = 0
default fm_anal = 0
default fm_pussy = 0
default fm_bj = 0
default fm_apologize = False
default fm_sex_pref = "BJ"
default fm_lvl = 0

#sister
default fs_dom = 0
default fs_rel = 7.5
default fs_aro = 0
default fs_cor = 0
default fs_anal = 0
default fs_pussy = 0
default fs_bj = 0
default fs_sex_pref = "BJ"
default fs_lvl = 0
define fs_mad = False

#neighbor - Karen
default nk_dom = 0
default nk_rel = 4
default nk_aro = 0
default nk_cor = 0
default nk_anal = 0
default nk_pussy = 0
default nk_bj = 0
default nk_sex_pref = "BJ"
default nk_lvl = 0
default nk_school_assignment_evening = False
default nk_school_assignment_evening_first = True
default nk_driving = False    

#family friend / mother's business partner - Bridget
default nb_dom = 0
default nb_rel = 2.5
default nb_aro = 0
default nb_cor = 0
default nb_anal = 0
default nb_pussy = 0
default nb_bj = 0
default nb_sex_pref = "BJ"
default nb_lvl = 0

#friend - Ron
default nr_rel = 0
default nr_lvl = 0

#school - Miss Novak
default sn_dom = 0
default sn_rel = 2
default sn_aro = 0
default sn_cor = 0
default sn_anal = 0
default sn_pussy = 0
default sn_bj = 0
default sn_sex_pref = "BJ"
default sn_lvl = 0

#school - Principal Hudson
default sp_rel = 0
default sp_lvl = 0

#school - Jack (janitor)
default sj_rel = 0
default sj_lvl = 0

#sex-stats
default total_anal = fm_anal + fs_anal + nk_anal + nb_anal + sn_anal
default total_pussy = fm_pussy + fs_pussy + nk_pussy + nb_pussy + sn_pussy
default total_bj = fm_bj + fs_bj + nk_bj + nb_bj + sn_bj

default fp_sex_pref = "BJ"
if total_bj >= total_pussy >= total_anal:
    $ fp_sex_pref = "BJ"
elif total_pussy >= total_bj >= total_anal:
    $ fp_sex_pref = "Pussy"
else:
    $ fp_sex_pref = "Anal"

#environment
default early_morning_we = False
default overslept = False
default talk_later = False
default evening_event = False
default firstday_view = renpy.random.randint(10,50)
default firstday_talk = False
default firstday_after_talk = False
default skip_breakfast = False
default late_oh_shit = False
default detention_served = False
default splash_screen = False
default school_walk_late_event = False
default breakfast_jump = False
default schoolbooks_added = False
default panties_added = False
default smallkeys_added = False
default toolbox_added = False
default cheat = False
default light_on = False
default hallway_pot_enable = False
default day_ahead = False
default shopping_with_fm = False
default bathroom_light = False
default goto_beach = False
default debug = False
default bad_weather = False
default rainstorm = False
default school_walk_late_arrival = False
default sis_school_issue = True
default sis_school_issue_2 = False
default school_hacker = False
default school_hacker_2 = False
default school_hacker_3 = False
default school_hacker_first_thought = True
default school_clues_search = False
default school_clues_search_2 = False
default school_clues_search_3 = False
default clerk_talked_to = 'Natalie'
default fs_pale_pink_panties = False
default fs_light_blue_panties = False
default fs_bright_pink_panties = False
default fs_yellow_panties = False
default find_panties = True
default morning_event_done = False
default wine_added = False
# default bottles = 99
default bottles = False
default after_sleep = False
default called = False
default has_cabin = False
default wcount = 5
default already_late = False
default keys_mentioned = False
default setstate = False
default had_breakfast = False

default fs_p = ['fs_yellow_panties','fs_light_blue_panties','fs_pale_pink_panties','fs_bright_pink_panties']
default gp = False
default br = False

#call locations from other screens
default uhl_fpb_cfs = False
default uhl_fsb_cfs = False
default gar_cfs = False
default kit_cfs = False
default uhl_cfs = False
default uhl_bl_cfs = False

default end_cfs = False
default stn_cfs = False
default wmc_cfs = False

default exitdown_event_var = False
default exitup_event_var = False
default exitleft_event_var = False
default exitright_event_var = False

#motorcycle stats
default mc_b = 0 #motorcycle build - shows how far along the main character is with fixing the bike
default mc_b_max = 150 #default max for the MC build to be finished - ie, when mc_b reaches this number, mc_f goes from False to True
default mc_p = 0
default mc_f = False # true / false status on whether the bike is finished or not
default count = 0
default maxcount = 2
default end_bike_repair = False
default sc = 0
# default sun_count = 0

# inventory system
# init python:
#     for file in renpy.list_files():
#         if file.startswith('images/inventory/') and file.endswith('.png'):
#             if 'hover' in file:
#                 name = file.replace('images/inventory/','').replace('_idle','').replace('_hover','').replace('.png','')
#                 setattr(store,""+name+"_item",Item(name,5))

#date and time stats
default first_day = True
default day_week = 5
define week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
define months_days = [['January',31],['February',28],['March',31],['April',30],['May',31],['June',30],['July',31],['August',31],['September',30],['October',31],['November',30],['December',31]]
# default start_month = 4
# default start_month_day = 1
# default start_month_text = months_days[4][0]

default current_month_day = 1
default current_month = 3
default current_month_text = months_days[current_month][0]
default current_day = week_days[day_week]
define morning = [6,7,8,9,10,11]
define day = [12,13,14,15,16,17,18,19,20,21]
define night = [22,23,0,1,2,3,4,5]

default current_hour = "06:00"
default addhour = False
default addminute = False

default wend_sat = False
default wend_sun = False

# default time of day variables (used for calling specific elements each day)
# default morning = True
# default schoolday = False
# default day = False
# default evening = False
# default night = False

#UI / game
default showStats = False
default persistent.skipintro = False

# define patchload = False