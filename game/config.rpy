init python:
    _game_menu_screen = None #this disables the right-click functionality of the game menu screen

init -1500 python:
    @renpy.pure
    class HideInterface_new(Action, DictEquality):
        """
         Causes the interface to be hidden until the user clicks.
         This is an override for the original HideInterface() in renpy/common/00action_other.rpy
         """
        def __call__(self):
            renpy.call_in_new_context("_hide_windows_new")

label _hide_windows_new:
    # This is an override of the label _hide_windows in the renpy/common/00keymap.rpy

    if renpy.context()._menu:
        return
    if _windows_hidden:
        return

    python:
        _windows_hidden = True
        hide_exit_buttons = True
        voice_sustain()
        ui.saybehavior(dismiss=['dismiss', 'hide_windows'])
        ui.interact(suppress_overlay=True, suppress_window=True)
        _windows_hidden = False
        hide_exit_buttons = False
    return

init -10 python:
    import os, math, re, pygame_sdl2, random
    pygame_sdl2.init()
    pydisp = pygame_sdl2.display.list_modes()

    get_max_res = pydisp[0]

    # def define_images(characterImageFolder, excludeFirstXFolders=0, flip=True):
    #     for path in renpy.list_files():
    #         if path.startswith(characterImageFolder + "/"):
    #             path_list = path.split("/")
    #             path_list[-1] = os.path.splitext(path_list[-1])[0]
    #             path_list = tuple(path_list[excludeFirstXFolders:])
    #             renpy.image(path_list, path)
    #             if flip:
    #                 renpy.image(path_list + ("flip", ), im.Flip(path, horizontal=True))

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
        persistent.patch_enabled = False
# defined config-variables
define config.quit_action = [Show('phone'),SetVariable('show_icons',False),Show('custom_confirm',None,'quit')]
if config.developer:
    if renpy.windows:
        define config.screenshot_pattern = "D:\Dropbox\RenPy-games\Screenshots\HSS-screenshot%04d.png"
if not config.developer:
    define config.console = True

# define config.missing_scene = "images/psa_renders.webp"

define config.default_music_volume = .5
define config.default_sfx_volume = .5
define config.default_voice_volume = .5

define dynamic_animation_list = {}
# persistent variables
default persistent.change_menu = False
default persistent.first_playthrough = True
default persistent.skipintro = False
default persistent.splash_screen = False
default persistent.maininfo = True
default persistent.phone_firstshow = True
default persistent.statscreen_infotext = True
default persistent.backpack_info = True
default persistent.cheat = False
default persistent.side_image_zoom = True
default persistent.achievement_cheat = False
default persistent.quick_menu = False
default persistent.selectedmenu = False
default persistent.displayresolutions = False
default persistent.soundmuted = False
default persistent.musicmuted = False
default persistent.sfxmuted = False
default persistent.voicemuted = False
default persistent.skipunseen = False
default persistent.skipafterchoices = False
default persistent.skiptransitions = False
default persistent.seenintro = False
# persistent kink-variables
default persistent.prefpiss = False
default persistent.prefanal = False
default persistent.preffeet = False
default persistent.prefmilf = False
default persistent.prefbdsm = False
default persistent.prefmilk = False
default persistent.preftran = False
default persistent.prefpreg = False
default persistent.preffist = False
default persistent.prefmult = False

#preferences
default preferences.prefwetting = False
default preferences.prefanal = False
default preferences.preffeet = False
default preferences.prefmilf = False
default preferences.prefbdsm = False

# character definitions
define narrator = Character(None, what_italic=True)
define unk_f = Character('Unknown female',who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define unk_m = Character('Unknown male',who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define unk = Character('???',who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define fp = Character("[fpinput]",image="fp_talkside",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define fm = Character("[fmName.Name]",image="fm_talkside",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define fs = Character("[fsName.Name]",image="jules",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define hj = Character("Jizzer",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define nb = Character("Bridget",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define nr = Character("Ron",image="nr_talkside",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define nk = Character("Karen",image="nk_talkside",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define nc = Character("Catherina",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define nk2 = Character("Kate",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define sn = Character("Miss Novak",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define se = Character("Miss Elliot",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define sp = Character("Principal Hudson",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define sj = Character("Jack",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define scn = Character("Natalie",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define scm = Character("Mattie",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define lil = Character("Lilim",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])
define aru = Character("Aruru",who_outlines=[(absolute(1),"#999",absolute(0),absolute(0))])

#remember to add default color="#000000" if the character do not have a namebox_charname.webp in the gui/-directory

default chars = [[fp,'fp'],[fs,'fs'],[fm,'fm'],[nk,'nk'],[nc,'nc'],[nb,'nb'],[nr,'nr'],[sn,'sn'],[se,'se'],[sp,'sp'],[scm,'scm'],[scn,'scn'],[sj,'sj'],[lil,"lil"],[aru,"aru"]]

default chardesc = False
default char_desc = [
    ["This is you. You're a ruggedly handsome young man, and that's about what you know, for now"],
    ["[fsName.name] is [fp]s [fsName.formal], and is living at the other end of the mezzanine. She's hot, definitely so, and (from what you've become familiar with, due to recent events), a rather horny creature"],
    ["[fmName.name] is [fp]s [fmName.formal], and has a bedroom on the ground floor. She's what you'd definitely call a MILF, and does seem relatively relaxed about skimpy clothing and the occassional slip-up when it comes to modesty..."],
    ["[nk] is your age, and you've been dating / hooking up / been a couple for a year or so, from a few months after you moved here.\n\nShe's cute, whimsy, and kinda naive about the world and what goes on in it. She's also quite petite, and more often than not dresses down, instead of flaunting her goods. Not exactly your type, but you got to know her, and she {i}is{/i} very nice."],
    ["[nc] was born in Prague, but moved here with her mom and brother when she was only a baby. She is supposed to go to highschool... Basically, what she does is hack the system to make sure her grades are okay, her attendance record is decent, and that she isn't kicked out due to someone checking her records.\n\nMostly, she hangs around at [icafe], where she has her own spot - I suggest you don't try to take that away from her... She knows a lot of shady people, and if you need something fixed (or someone, for that matter), she can probably make that happen. For a fee.\n\nShe's got a goth look to her, although she's not that into the whole depressed, \"the world is horrible\" view. She mostly just likes the look, and that it usually makes people cross the street when she comes walking. Easy way to avoid most humans can't be that bad!\n\nAnd her brother... is [nr]"],
    ["[nb] is..."],
    ["[nr] is [fp]'s best friend. You've been friends since about 1 day after you moved here, due to... let's say some \"questionable choices\" you made... He's also [nc]'s brother"],
    ["[sn] is your homeroom teacher, and also your English and Science teacher. She's originally from the Czech Republic, but have been living her since she was a little girl, and you'd never tell besides her name. She's usually strict about the \"Miss Novak\" bit, but you've learned her first name is Evelínka, which she's shortened to Evelyn to make it less... foreign.\n\nShe's been working at HSS for 8 years, and have been known for her strict, formal behavior, and yet still managing to keep a job as the homeroom teacher for the last 3 years. If you tell her something, or have a problem, she'll do her best to comfort you, or solve the issues at hand.\n\nYou've always had a thing for Evelyn, but you think you've managed to keep her from recognizing that fact. You might be wrong about that, though..."],
    ["[se] is..."],
    ["[sp] is..."],
    ["[scm] is..."],
    ["[scn] is..."],
    ["[sj] is..."],
    ["[lil] is..."],
    ["[aru] is..."]
    ]

default atts = ['rel','dom','aro','cor','att']

#fp
default fpinput = "Marten"
default fp_att = 0
default fp_aro = 0
default fp_sts = 0
default fpshower = False
default fpsink = False
default fp_bath_lock = False
default leave_lock = False
default fp_creep = 0
default fp_money = 200
default punishment_late = 0 #this is the variable for punishment value for lateness at school - reach too high a number, and [fM] is called, and her relationship stat decrease
default filth_val = 0
default tmp_filth_val = False
default fpe = False
default fp_couch_aquired = False
default lil_bad = 0
default aru_good = 0
default fp_alignment_text = "evil" if lil_bad > aru_good else "good"
default fp_alignment = 0
default choicestatus = None
default dream_event = False

#aru
default aru_dom = 0
default aru_rel = 0
default aru_aro = 0
default aru_cor = 0

#lil
default lil_dom = 0
default lil_rel = 0
default lil_aro = 0
default lil_cor = 0

#fm
default fm_dom = 0
default fm_rel = 20
default fm_aro = 0
default fm_cor = 0
default fm_dom_max = 15
default fm_rel_max = 50
default fm_aro_max = 15
default fm_cor_max = 10
default fm_anal = 0
default fm_pussy = 0
default fm_bj = 0
default fm_apologize = False
default fm_sex_pref = "BJ"
default fm_lvl = 0
default fme = False
default fm_seen = False

#fs
default fs_dom = 0
default fs_rel = 15
default fs_aro = 0
default fs_cor = 0
default fs_dom_max = 15
default fs_rel_max = 50
default fs_aro_max = 15
default fs_cor_max = 10
default fs_anal = 0
default fs_pussy = 0
default fs_bj = 0
default fs_sex_pref = "BJ"
default fs_lvl = 0
default fs_mad = 0
default fse = False

#nk
default nk_mad = False
default nk_dom = 3
default nk_rel = 20
default nk_aro = 4
default nk_cor = 0
default nk_dom_max = 15
default nk_rel_max = 50
default nk_aro_max = 15
default nk_cor_max = 10
default nk_anal = 0
default nk_pussy = 0
default nk_bj = 0
default nk_sex_pref = "BJ"
default nk_lvl = 0
default nk_school_assignment_evening = False
default nk_school_assignment_evening_first = True
default nk_driving = False
default nk_sa_status = False
default nke = False
default call_nk = False
default call_nk_event = False
default nk_first_date = False
default nk_day_date = False

#nc
default nc_dom = 0
default nc_rel = 0
default nc_aro = 0
default nc_cor = 0
default nc_dom_max = 15
default nc_rel_max = 50
default nc_aro_max = 15
default nc_cor_max = 10
default nc_anal = 0
default nc_pussy = 0
default nc_bj = 0
default nc_sex_pref = "BJ"
default nc_lvl = 0
default nc_number = '111-555-3369'
default nc_event = False
default nc_happens = False
default nc_call_after_hacker = False
default nce = False

#nb
default nb_dom = 0
default nb_rel = 2.5
default nb_aro = 0
default nb_cor = 0
default nb_dom_max = 15
default nb_rel_max = 50
default nb_aro_max = 15
default nb_cor_max = 10
default nb_anal = 0
default nb_pussy = 0
default nb_bj = 0
default nb_sex_pref = "BJ"
default nb_lvl = 0
default nbe = False

#nr
default nr_rel = 10
default nr_lvl = 0
default nre = False

#sn
default sn_dom = 0
default sn_rel = 2
default sn_aro = 0
default sn_cor = 0
default sn_dom_max = 15
default sn_rel_max = 50
default sn_aro_max = 15
default sn_cor_max = 10
default sn_anal = 0
default sn_pussy = 0
default sn_bj = 0
default sn_sex_pref = "BJ"
default sn_lvl = 0
default sne = False

#se
default se_rel = 0
default se_lvl = 0
default see = False

#sp
default sp_rel = 0
default sp_lvl = 0
default spe = False

#sj
default sj_rel = 0
default sj_lvl = 0
default sje = False

#scn
default scn_rel = 0
default scn_lvl = 0
default scne = False

#scm
default scm_rel = 0
default scm_lvl = 0
default scme = False

#dreamevents
default dreameventsChars = []
default fs_dream_event = 1
default fm_dream_event = 1
default nc_dream_event = 1
default nk_dream_event = 1
default nb_dream_event = 1
default sn_dream_event = 1

#sex-stats
default total_anal = fm_anal + fs_anal + nk_anal + nb_anal + sn_anal
default total_pussy = fm_pussy + fs_pussy + nk_pussy + nb_pussy + sn_pussy
default total_bj = fm_bj + fs_bj + nk_bj + nb_bj + sn_bj

default fp_sex_pref = "BJ"
if (total_bj >= (total_pussy + total_anal)):
    $ fp_sex_pref = "BJ"
elif (total_pussy >= (total_bj + total_anal)):
    $ fp_sex_pref = "Pussy"
else:
    $ fp_sex_pref = "Anal"

# sunscreen
default i_s = {
    'pos_back':[],
    'pos_front':[]
}

default sunscreen_text = "So, you should put on some sunscreen - where to start?"
default first_sunscreen = True

default total_fs_sunscreen_points = 0

# environment
default fpmc_r = False
default hide_exit_buttons = False
default early_morning_we = False #check this to see if needed
default overslept = False
default overslept_time = False
default armybox_open = False
default broken_ufb_lock = False
# default talk_later = False #this should probably be renamed to fs_talk_later
default skip_breakfast = False
default late_oh_shit = False
default detention_served = False
default school_walk_late_event = False
default breakfast_jump = False
default evening_event = False
default already_late = False
default firstday_talk = False
default firstday_after_talk = False
default light_on = False
default day_ahead = False
default shopping_with_fm = False
default bathroom_light = False
default goto_beach = False
default debug = False
default school_walk_late_arrival = False
default morning_out_of_bed = False
default morning_event_done = False
default after_sleep = False
default has_cabin = False
default tooltipcounterforphone = 0
default boat_at_marina = False
default had_breakfast = False # check to see if needed
default dinner_event = True
default after_principal_talk = False
default shitty_morning = False
default call_nr = False
default home_from_school = False
# default nr_involved = False #not in use atm
default icafe = 'Obuko'
default icafe_discovered = False
default visit_icafe_1 = False
default visit_icafe_2 = False
default visit_icafe_3 = False
default visit_icafe_4 = False
default wetshower = False
default drivingcmp = _('TripIt Black')
default bc_clicked = False
default show_fridge = False
default required_shower = False
default alarmclock = False
default alarmclock_time = "07:00"
default alarmhour = 0
default alarmminute = 0
default walk_to_school = False
default jiggle_phone = False

# fs events
default fs_si = True
default fs_si_2 = False
default hacker_1 = False
default hacker_2 = False
default hacker_3 = False
default hacker_4 = False
default hacker_5 = False
default hacker_6 = False
default hacker_first_thought = True
default scs = False
default scs_2 = False
default scs_3 = False
default clerk_talked_to = scn.name
default fs_party = False
default fs_invitation = False
default bathroom_occupied_fs = False

# fm events
default bathroom_occupied_fm = False
default not_entered = True

# nc events
default nc_owed = 0
default tmp_nc_owed = 0
default nc_action_started = False
default nc_action_completed = False
default nc_payment_made = False
default check_nc_event_status = 0
default hacker_event_not_happen = False

# items
default fsp_black = False
default fsp_light_blue = False
default fsp_hot_pink = False
default fsp_red = False
default fsp_yellow = False
default find_panties = True
default bathroom_find_panties = True
default find_pb = False
default find_keys = False
default panties_added = False
default carkeys_added = False
default carry_carkeys = False
default bathroom_panties_added = False
default returnbfp = False
default schoolbooks_added = False
default smallkeys_added = False
default toolbox_added = False
default wine_added = False
default carry_wallet = False
default wallet_added = False
default pb_added = False
default pb_return = False
default bottles = False
default wcount = 5
default keys_mentioned = False
default gp_bed = False
default gp_bath = False
default br = False
default carry_backpack = False
default selecteditem = False
default selecteditemname = False
default selecteditemamount = False
default selecteditemweight = False
default selecteditemdesc = False
default total_weight = 0

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
default showclosebutton_phone = True
default show_icons = True
default quit_screen = False
default charge_phone_now = False
default battery_text = 100
default alarmclock_icon = False
default charge_phone = False
default imggal_showbuttons = True
default textmsg = False
default textchar = False
default calling = False
default duringcall = False
default nc_after_ft = False
default app_list = ['friendfinder']
default showapppage = False
default appselect = None
default playstore_search_saved = '  '
default playstore_search = '  '
default contacts_search = '  '
default installedFF = False

#call locations from other screens
default br_cfs = False
default fmb_cfs = False
default uhl_fpb_cfs = False
default uhl_fsb_cfs = False
default gar_cfs = False
default gar_fb_cfs = False
default kit_cfs = False
default pat_cfs = False
default ufbm = False
default ufbmcfs = False
default uts_cfs = False
default ups_cfs = False
default upscd_cfs = False
default uhaf_cfs = False
default out_cfs = False
default lvr_cfs = False
default tfs_cfs = False
default end_cfs = False
default stn_cfs = False
default wmc_cfs = False
default ufbmtcfs = False
default current_file = False
default keyclose = False
default ic_cfs = False

default exitdown_event_var = False
default exitup_event_var = False
default exitleft_event_var = False
default exitright_event_var = False

# achievement variables
default beer_pickup = False
default carkeys_pickup = False
default fsp_black_pickup = False
default fsp_hot_pink_pickup = False
default fsp_light_blue_pickup = False
default fsp_yellow_pickup = False
default fsp_red_pickup = False
default gin_pickup = False
default phone_pickup = False
default princessplug_pickup = False
default roses_pickup = False
default schoolbooks_pickup = False
default smallkeys_pickup = False
default toolbox_pickup = False
default vodka_pickup = False
default wallet_pickup = False
default whiskey_pickup = False
default wine_pickup = False
default pref_screen = False
default trans = False
default fdtfs_after = True
default occupied_bath = True

default fp_bedroom_fp_ach = False
default fp_bedroom_fs_ach = False
default fp_bedroom_fm_ach = False
default fp_topofstairs_ach = False
default fp_ufb_ach = False
default fp_entrance_ach = False
default fp_livingroom_ach = False
default fp_kitchen_ach = False
default fp_outside_ach = False
default fp_patio_ach = False
default fp_pool_ach = False
default fp_garage_ach = False
default fp_garage_gym = False
default fp_garage_bathroom = False
default fp_garage_sauna = False
default fp_school_outside_ach = False
default fp_school_classroom_ach = False
default fp_school_bathroom_ach = False
default fp_school_office_ach = False
default fp_school_po_ach = False
default fp_beach_ach = False
default fp_marina_ach = False
default fp_icafe_ach = False
default fp_cabin_ach = False
default fp_store_ach = False
default fp_docks_ach = False
default fp_container_ach = False
default fp_highway_overpass = False
default fp_sn_house_ach = False
default fp_nk_house_ach = False
default fp_nr_house_ach = False
default fp_nb_house_ach = False

default selected_number = 0
default panties_sniffer = False

# lists
default hints = []
default read_hints = []
default disabled_hints = []
default deleted_hints = []
default calls = []
default read_calls = []
default disabled_calls = []
default deleted_calls = []
default messages = []
default read_messages = []
default disabled_messages = []
default deleted_messages = []
default hintselect = 'new'
default fp_jobs = [drivingcmp]
default firstday_talk_list = ['fp_livingroom','fp_bedroom_fp','fp_bedroom_fs','fp_kitchen','fp_entrance','fp_outside']
default fs_p = ['fsp_yellow','fsp_light_blue','fsp_hot_pink','fsp_black','fsp_red']
default p_response = ["Hm... "+fsName.myformal+"s panties...\n{b}sniffs them{/b}\nShould I take them with me?",
                        "Oh, "+fsName.myformal+" left her panties...",
                        "Right-o! I don't think I have this color...",
                        "{b}Sniffs panties{/b} I love her smell"
        ]

default playstore_games = [
            ['Making Movies','Droid Productions','makingmovies','Sometimes you find new beginnings from the wreckage of past mistakes. Making Movies is a game about paying rent, finding love and making pornography.','https://droid-productions.itch.io/making-movies'],
            ['Life','Fasder','life','A story driven sandbox game about Mark and his day to day life.','https://fasder.itch.io/life'],
            ['xMassTransitx','xMTx','xmasstransitx','A typical cyberpunk, time-travel, zombie survival, adult game with hot girls.','https://www.patreon.com/xMassTransitx'],
            ['Parental Love','Luxee','parentallove','Help mend the relationship of a broken man and his ex-wife. Or don\'t?','https://www.patreon.com/Luxee'],
            ['A Broken Family','KinneyX23','abrokenfamily','In the year 2034 the world is in ruins, it is dominated by machines and humans serve as their slaves. One of those machines was reprogrammed and sent to the past to protect John O\'Connor','https://kinneyx23.itch.io/a-broken-family'],
            ['Inevitable Relations','KinneyX23','inevitablerelations','Charlie and Eva were pretty close, too close for Beth and Alex, so they sent Charlie to California, to live with Beth‘s brother Leo. After one year he returns, and the story starts there','https://www.patreon.com/KinneyX23'],
            ['The DeLuca Family','HopesGaming','thedelucafamily','You live a peaceful life, until you get a letter from a mafioso, telling you that due to your parent\'s past, you\'re in his debt. You will serve a The DeLuca family, the most dangerous and infamous criminal organisation in the country','https://www.patreon.com/HopesGaming'],
            ['A Cowboy\'s Story','Noller72','acowboysstory','You take the role of a lonesome Cowboy who travel to this little town, and there the adventures begin','https://www.patreon.com/Noller72'],
            ['Retrieving the Past','MrKnobb','retrievingthepast','Journey with Jensen to find out what he needs to retrieve from his past to make sense of it all. Why is all this happening now?','https://www.patreon.com/mrknobb']
]

default playstore_recommended = [
            ['HSS','Studio Errilhl','hss','You\'re on your last stretch of high-school, just trying to graduate, have some fun, get some pussy... all the regular stuff. Although... something is not quite as it seems in your peaceful little town...','https://www.patreon.com/errilhl'],
            ['Making Movies','Droid Productions','makingmovies','Sometimes you find new beginnings from the wreckage of past mistakes. Making Movies is a game about paying rent, finding love and making pornography.','https://droid-productions.itch.io/making-movies'],
            ['Life','Fasder','life','A story driven sandbox game about Mark and his day to day life.','https://fasder.itch.io/life'],
            ['xMassTransitx','xMTx','xmasstransitx','A typical cyberpunk, time-travel, zombie survival, adult game with hot girls.','https://www.patreon.com/xMassTransitx'],
            ['Parental Love','Luxee','parentallove','Help mend the relationship of a broken man and his ex-wife. Or don\'t?','https://www.patreon.com/Luxee'],
            ['A Broken Family','KinneyX23','abrokenfamily','In the year 2034 the world is in ruins, it is dominated by machines and humans serve as their slaves. One of those machines was reprogrammed and sent to the past to protect John O\'Connor','https://kinneyx23.itch.io/a-broken-family'],
            ['Inevitable Relations','KinneyX23','inevitablerelations','Charlie and Eva were pretty close, too close for Beth and Alex, so they sent Charlie to California, to live with Beth‘s brother Leo. After one year he returns, and the story starts there','https://www.patreon.com/KinneyX23'],
            ['The DeLuca Family','HopesGaming','thedelucafamily','You live a peaceful life, until you get a letter from a mafioso, telling you that due to your parent\'s past, you\'re in his debt. You will serve a The DeLuca family, the most dangerous and infamous criminal organisation in the country','https://www.patreon.com/HopesGaming'],
            ['A Cowboy\'s Story','Noller72','acowboysstory','You take the role of a lonesome Cowboy who travel to this little town, and there the adventures begin','https://www.patreon.com/Noller72'],
            ['Retrieving the Past','MrKnobb','retrievingthepast','Journey with Jensen to find out what he needs to retrieve from his past to make sense of it all. Why is all this happening now?','https://www.patreon.com/mrknobb']
]

default playstore_apps = [
            ['Birdie','Birdie Bots','birdie','This is where you\'ll find the latest short blurbs about nothing important at all','not_a_link'],
            ['Video','Video Makers','video','Wanna watch the hottest girl-on-girl videos on your phone? Get "VIDEO", the best porn-player out there','not_a_link'],
            ['ChitChat','Chirpies','chat','Text your friends, chat with strangers. What can possibly go wrong?','not_a_link'],
            ['Friend Finder','Stalker Inc','friendfinder','Wanna know where your friends are? Just have them install this little app, and their life is an open book!','not_a_link'],
            ['Voice Chat','TOG','voice','Wanna talk to anyone who\'s got a dataplan without other costs? Then VOICE is the app for you!','not_a_link']
]
default wallart = {
            "parkinglot":False,
            "ferrari":False,
            "roadtrip":False,
            "sincity":False,
            "peekaboo":False
}
default active_wallart = False
default achievement_wallart_set = False

# breakfast choices - the bf_weights is updated when you pick something, and will change the weight depending on whether or not you benefit or not
# default bf_weights = [(0,5),(1,4),(2,2),(3,1),(4,5),(5,2),(6,2),(7,4),(8,1),(9,4),(10,2)]
# default breakfast = [ #food, reply, modifier, stat, weight-mod
#             ["pancakes","I love your pancakes",2,"fm_rel",.5],
#             ["bacon and eggs","I'm gonna get fat if I continue eating this",1,"fm_rel",.25],
#             ["scones","I don't really like scones",-1,"fm_rel",.25],
#             ["scones","Ah, scones again... okay, I guess they'll do",0,"fm_rel",.25],
#             ["sandwiches","Ah, I just love those sandwiches",2,"fm_rel",.5],
#             ["beans and bacon","What am I? A cowboy? Seriously",-1,"fm_rel",.25],
#             ["cereal","Well, if there's nothing else...",-1,"fm_rel",.25],
#             ["cereal","Cereal is fine",1,"fm_rel",.25],
#             ["muffins","I'm not in the mood for anything sweet. I'll just have coffee",0,"fm_rel",.25],
#             ["muffins","Sure, lemme have them",1,"fm_rel",.25],
#             ["muffins","These muffins taste... I'll just have coffe, thanks",-1,"fm_rel",.25]
#         ]
default breakfast_food_list = ['pancakes','bacon and eggs','scones','sandwiches','beans and bacon','quiche','cereal','muffins']
default breakfast_nice_list = [
                ['I love your {0}',2,'fm_rel'],
                ['I\'m gonna get fat if I keep eating this',1,'fm_rel'],
                ['Ah, I just love those {0}',2,'fm_rel'],
                ['{0} is fine',1,'fm_rel'],
                ['Sure, lemme have them',1,'fm_rel'],
                ['Not really in the mood for food this morning, I\'ll just have coffee',0,'fm_rel']
]
default breakfast_mean_list = [
                ['I don\'t really like {0}',-1,'fm_rel',1,'fm_dom'],
                ['{0} again?',-1,'fm_rel',1,'fm_dom'],
                ['You know I don\'t like {0}',0,'fm_rel',1,'fm_dom']
]

default dinner_weights = [(0,3),(1,2),(2,5),(3,1)]

default images_unlocked = []

default home_events = [
                ["You arrive home. Nobody is there at the moment, it seems, as "+fmName.informal+"'s car is gone, and "+fsName.yourinformal+" is nowhere to be seen.",False],
                ["When you arrive home, the door is locked, and you realise you've forgotten your key. Noone is answering the door when you try the doorbell, so both "+fmName.yourinformal+" and "+fmName.yourinformal+" must be out. You weren't really that keen on sitting outside all day, waiting for them, so you're pondering what else you can do instead",False],
                ["Arriving home, you see "+fmName.yourinformal+"'s car in the driveway.",False],
                ["When you arrive home, you catch a glimpse of "+fsName.yourformal+" by the pool, but "+fmName.yourformal+" is nowhere to be seen. Her car is still here, though.",True]
            ] ## create more events here

# default text_msg_received = []

default not_in_contacts = ['fp','nc','lil','aru']

default item_weights = {'beer':2,'carkeys':.2,'fsp_red':.1,'fsp_hot_pink':.1,'fsp_black':.1,'fsp_yellow':.1,'fsp_light_blue':.1,'gin':1,'phone':.3,'princessplug':.4,'roses':.5,'schoolbooks':5,'small_keys':.2,'toolbox':10,'vodka':1,'wallet':.5,'whiskey':1,'wine':1}

default item_desc = {
            'beer':'What a tasty, delicious beverage! Exactly what you need to kick off a party, slacking on the couch, or just getting slightly wasted. One beer won\'t do much damage, but as soon as you drink a few...',
            'carkeys':'Keys to the car out front.',
            'fsp_red':'Red lace panties. Seductive and hot, pretty much fitting the owner to a t!',
            'fsp_hot_pink':'Hot pink panties. Smelling of '+fsName.yourformal+'! Definitely worth hanging on to!',
            'fsp_black':'Black lace panties. These are sexy and hot, and you\'re definitely gonna hang on to these.',
            'fsp_yellow':'Yellow panties. Bright colored, fun and cute.',
            'fsp_light_blue':'Light blue panties. Innocent and cute. Not very representative of the owner...',
            'gin':'Time to hit it off with a bit of G&T.',
            'phone':'Your dayplanner, your internet-connection, your contact-list, your camera, your pretty much everything. Oh, and a phone, too!',
            'princessplug':'This thing has actually been up '+fsName.yourformal+'\'s butt...',
            'roses':'Beautiful roses. You should give this to someone!',
            'schoolbooks':'The books you need for school. They should really think of putting up some lockers at school, so you didn\'t have to drag these with you all the time',
            'small_keys':'A set of small keys. What they unlock, you have no idea...',
            'toolbox':'Essential tools for fixing your bike',
            'vodka':'{b}This{/b} is the right tool for getting utterly, completely wasted. Not that you have any need for that, of course... not right now, anyway...',
            'wallet':'Your wallet. As long as you have this, you have money. Or, also known as credit cards. But they\'re paid by someone else, so... free money, right?',
            'whiskey':'Ah! The grown man\'s drink. One sip of this, and you\re pretty sure your throat\'s on fire!',
            'wine':'The preferred drinks of any posh girl out there. You should keep some on hand!'
}

default location_list = {
        'fp_house':['fp_outside','fp_entrance','fp_livingroom','fp_kitchen','fp_bedroom_fm','fp_topofstairs','fp_upstairs','fp_bedroom_fp','fp_bedroom_fs','fp_ufb','fp_pool','fp_garage','fp_garage_gym','fp_garage_bathroom','fp_garage_sauna'],
        'school':['school_outside','school_gym','school_track','school_classroom','school_office_principal','school_office_staff'],
        'icafe':['icafe_outside','icafe_inside'],
        'beach':['beach_outside'],
        'marina':['marina_outside'],
        'cabin':['cabin_outside'],
        'grocerystore':['store_outside']
}

default location_names = {
    'fp_outside':'Outside',
    'fp_entrance':'Entrance',
    'fp_livingroom':'Livingroom',
    'fp_kitchen':'Kitchen',
    'fp_bedroom_fm':'[fmName.name]\'s bedroom',
    'fp_topofstairs':'Top of stairs',
    'fp_upstairs':'Top of stairs',
    'fp_bedroom_fp':'[fp]\'s bedroom',
    'fp_bedroom_fs':'[fsName.name]\'s bedroom',
    'fp_ufb':'Upper floor bathroom',
    'fp_pool':'Pool',
    'fp_garage':'Garage',
    'fp_garage_gym':'Gym',
    'fp_garage_bathroom':'Garage bathroom',
    'fp_garage_sauna':'Sauna'
}

default fs_present = [0,1,2,3,4,5,6,7,8,15,16,17,18,19,20,21,22,23]
default fs_present_we = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] if fs_party else [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

default inv_list = []

# motorcycle
default mc_b = 0 #motorcycle build - shows how far along the main character is with fixing the bike
default mc_b_max = 150 #default max for the MC build to be finished - ie, when mc_b reaches this number, mc_f goes from False to True
default mc_p = 0
default mc_f = False # true / false status on whether the bike is finished or not
default count = 0
default maxcount = 2
default end_fp_fb = False
default sc = 0
default fb_steplist_selected = 0
default fb_steplist = [0,15,30,45,60,75,85,95,105,115,125,135,140,150]

# date and time
default first_day = True
default day_week = 5
define week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
define months_days = [['January',31],['February',28],['March',31],['April',30],['May',31],['June',30],['July',31],['August',31],['September',30],['October',31],['November',30],['December',31]]
default daycount = 0
default current_month_day = 1
default current_month = 3
default current_month_text = months_days[current_month][0]
default current_day = week_days[day_week]
define morning = [6,7,8,9,10,11]
define day = [11,12,13,14,15,16,17,18,19,20,21,22]
define evening = [20,21,22]
define night = [22,23,0,1,2,3,4,5]
define hours = [0,1,22,23] # these are the "glowhours" before night-time, when lights are on

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
default current_location = 'fp_bedroom_fp'
default previous_location = 'fp_bedroom_fp'