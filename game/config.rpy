init python:
    import os, math, re
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

# persistent variables
default persistent.first_playthrough = True
default persistent.skipintro = False
default persistent.iphone_info = True
default persistent.splash_screen = False

# character definitions
define fp = Character("[fpinput]")
define fm = Character("[fmName.Formal]")
define fs = Character("[fsName.Formal]",image="fs_talkside")
define nb = Character("Bridget")
define nr = Character("Ron") 
define nk = Character("Karen",image="nk_talkside")
define sn = Character("Miss Novak")
define se = Character("Miss Elliot")
define sp = Character("Principal Hudson")
define sj = Character("Jack")
define scn = Character("Natalie")
define scm = Character("Mattie")
#remember to add default color="#000000" if the character do not have a namebox_charname.png in the gui/-directory

default chars = [[fp,"fp"],[fm,"fm"],[fs,"fs"],[nb,"nb"],[nr,"nr"],[nk,"nk"],[sn,"sn"],[sp,"sp"],[sj,"sj"]]
default atts = ['rel','dom','aro','cor','att']

#fp
default fp_att = 0
default fp_aro = 0
default fp_sts = 0
default fpshower = False
default fpsink = False
default fp_creep = 0
default punishment_late = 0 #this is the variable for punishment value for lateness at school - reach too high a number, and [fM] is called, and her relationship stat decrease
default filth_val = 0

#fm
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

#fs
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

#nk
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

#nb
default nb_dom = 0
default nb_rel = 2.5
default nb_aro = 0
default nb_cor = 0
default nb_anal = 0
default nb_pussy = 0
default nb_bj = 0
default nb_sex_pref = "BJ"
default nb_lvl = 0

#nr
default nr_rel = 0
default nr_lvl = 0

#sn
default sn_dom = 0
default sn_rel = 2
default sn_aro = 0
default sn_cor = 0
default sn_anal = 0
default sn_pussy = 0
default sn_bj = 0
default sn_sex_pref = "BJ"
default sn_lvl = 0

#sp
default sp_rel = 0
default sp_lvl = 0

#sj
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

# environment
default early_morning_we = False #check this to see if needed
default overslept = False
default talk_later = False #this should probably be renamed to fs_talk_later
default skip_breakfast = False
default late_oh_shit = False
default detention_served = False
default school_walk_late_event = False
default breakfast_jump = False
default evening_event = False
default already_late = False
default firstday_talk = False
default firstday_after_talk = False
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
default morning_event_done = False
default after_sleep = False
default has_cabin = False
default had_breakfast = False # check to see if needed
default dinner_event = True
default after_principal_talk = False
default shitty_morning = False
default call_nr = False
# default nr_involved = False #not in use atm

# fs events
default fs_si = True
default fs_si_2 = False
default hacker = False
default hacker_2 = False
default hacker_3 = False
default hacker_first_thought = True
default scs = False
default scs_2 = False
default scs_3 = False
default clerk_talked_to = scn.name
default fs_party = False

# items
default fs_pale_pink_panties = False
default fs_light_blue_panties = False
default fs_bright_pink_panties = False
default fs_yellow_panties = False
default find_panties = True
default bathroom_find_panties = True
default find_pb = False
default panties_added = False
default bathroom_panties_added = False
default schoolbooks_added = False
default smallkeys_added = False
default toolbox_added = False
default wine_added = False
default pb_added = False
default pb_return = False
default bottles = False
default wcount = 5
default keys_mentioned = False
default gp_bed = False
default gp_bath = False
default br = False

# tablet
default fs_tablet_bedroom = False
default find_tablet = False
default tablet_always_look = False
default tablet_added = False
default tablet_code = False
default tablet_home = True
default ic_num = []
default tablet_stored_code = 2625
default fsi_cfs = False

# phone
default phone_added = False
default carry_phone = False
default showclosebutton_iphone = True
default show_icons = True
default quit_screen = False
default charge_phone_now = False
default battery_text = 100
default charge_phone = False

#call locations from other screens
default uhl_fpb_cfs = False
default uhl_fsb_cfs = False
default gar_cfs = False
default kit_cfs = False
default uhl_cfs = False
default uhl_bl_cfs = False
default out_cfs = False
default lvr_cfs = False
default tfs_cfs = False
default end_cfs = False
default stn_cfs = False
default wmc_cfs = False

default exitdown_event_var = False
default exitup_event_var = False
default exitleft_event_var = False
default exitright_event_var = False

# achievement variables
default beer_pickup = False
default carkeys_pickup = False
default bright_pink_panties_pickup = False
default light_blue_panties_pickup = False
default pale_pink_panties_pickup = False
default yellow_panties_pickup = False
default gin_pickup = False            
default phone_pickup = False
default princessplug_pickup = False
default roses_pickup = False
default schoolbooks_pickup = False
default smallkeys_pickup = False
default toolbox_pickup = False
default vodka_pickup = False
default whiskey_pickup = False
default wine_pickup = False
default pref_screen = False 
default trans = False
default fdtfs_after = True

default fp_bedroom_ach = True
default fs_bedroom_ach = False
default uhl_bathroom_ach = False
default uhl_ach = False
default entrance_ach = False
default livingroom_ach = False
default kitchen_ach = False
default outside_ach = False
default garage_ach = False
default school_ach = False
default beach_ach = False

default selected_number = 0
default panties_sniffer = False

# lists 
default firstday_talk_list = ['livingroom','fp bedroom','fs bedroom','kitchen','entrance','outside']
default fs_p = ['fs_yellow','fs_light_blue','fs_pale_pink','fs_bright_pink']
default p_response = ["Hm... "+fsName.formal+"s panties...\n{b}sniffs them{/b}\nShould I take them with me?",
                        "Oh, "+fsName.myinformal+" left her panties...",
                        "Right-o! I don't think I have this color...",
                        "{b}Sniffs panties{/b} I love her smell"
        ] 
default fs_present = [0,1,2,3,4,5,6,7,8,15,16,17,18,19,20,21,22,23]
default fs_present_we = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] if fs_party else [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]


# motorcycle
default mc_b = 0 #motorcycle build - shows how far along the main character is with fixing the bike
default mc_b_max = 150 #default max for the MC build to be finished - ie, when mc_b reaches this number, mc_f goes from False to True
default mc_p = 0
default mc_f = False # true / false status on whether the bike is finished or not
default count = 0
default maxcount = 2
default end_bike_repair = False
default sc = 0

# date and time
default first_day = True
default day_week = 5
define week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
define months_days = [['January',31],['February',28],['March',31],['April',30],['May',31],['June',30],['July',31],['August',31],['September',30],['October',31],['November',30],['December',31]]
default current_month_day = 1
default current_month = 3
default current_month_text = months_days[current_month][0]
default current_day = week_days[day_week]
define morning = [6,7,8,9,10,11]
define day = [11,12,13,14,15,16,17,18,19,20,21,22]
define night = [22,23,0,1,2,3,4,5]

default current_time = "06:00"
default addhour = False
default addminute = False

default wend_sat = False
default wend_sun = False
default sun_event = False

#UI / game
default showStats = False
default setstate = False
default end_game = False
default current_location = 'fp_bedroom_loc'
# default cc_chosen = False

init python:
    _game_menu_screen = None