## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("High School Shenaningans")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.021.5-(Alpha)-(bugfix)"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("{b}HSS (or HighSchool Shenanigans){/b} is an adult-themed visual novel, with some randomness, and a lot of sexy content. You're playing as <player> (pick your name, or default to Marten), an 18 year old boy who's finishing high school, and is mildly anxious about his exams, the lack of a girlfriend, noone to take to the dance, and how to get his motorcycle rebuilt properly. Add to this an abundance of hot girls in his vicinity, and you got most of the plot right there. At least if you only knew what opportunities you have right at your feet.\n\nThe game is about discovering those opportunities, and realising what you can do, not to mention WHO you can do!\n\nThe game is in very early development, and currently we're working on the game mechanics, how to modify relationships, how to build a believeable story, and how to decide which characters get to do what with whom.\n\n")
#••••••
define gui.changelog = _("0.021.5 BUGFIX:\n• Added a warning about no content on the tablet\n• Closed #50 - bug - problem with honda-scene - not able to reproduce, closed for now\n• Fixed a minor issue in the morning / wake up, when already late\n• Fixed a missing call to go to school in the morning (for specific events in the morning)\n• Fixed #46 - bug - advancing time via minutes doesn't update hours correctly\n• Fixed #47 - bug - advancing time via minutes doesn't scene correctly\n• Fixed #48 - bug - flashing between scenes\n• Fixed #49 - bug - panties-action triggers when entering room\n• Fixed #51 - bug - psd-files in images folder\n• Fixed #52 - bug - issues when picking up too many items (weight-limit exceeded)\n• Fixed #53 - bug - panties flashing in bathroom if left (this can be extended to other instances if the same flashing occurs)\n• Fixed #54 - bug - going to school-event doesn't always happen when going outside\n• Fixed #55 - bug - temporarily fixed looping talk with fs by removing it from the game - will be reinstated in next release\n• Increased weight-limit temporarily, to circumvent the problem with weigh-limit being reached, preventing picking up more items (this will be updated next release)\nREGULAR 0.021 RELEASE:\n• Added hover-functionality (together with click for the stat-screen)\n• Added a tablet in fs' room, and a phone for the MC for different purposes (none implemented as of yet)\n• Added save/load functionality to the phone-UI\n• Added ability to collect panties from the bathroom as well as the bedroom (different chance of finding them, the chance is not the same for both places)\n• Added multiple, random responses for item discovery in specific locations (will not pick certain responses if that item is already found/picked up)\n• Added versions of the MC bedroom with phone present for all hours of the day\n• Added tooltips to the phone-interface (currently a bit WIP)\n• Added a way to go directly to the garage from inside (entrance <-> garage)\n• Added the ability to go between kitchen/livingroom\n• Added a cleanliness / dirty modifier / status (basically, you get dirty, then you need to wash)\n• Added a notification bar to the phone, with working time and battery indicator (the battery will be used for events in the game, depending on amount of charge left at any particular time)\n• Closed #1 - bug - missing content on Sunday (this has been closed, this is not a bug, although there should be more content coming in future updates)   \n• Changed the entrance and the upper hallway\n• Fixed a minor bug with achievements (wrong name used for an update-statement in locations.rpy)\n• Fixed a minor bug with looping on the bike-repair\n• Fixed a bug in the remove_item-function for the inventory (the notification didn't pop up, due to an error in the assigned variables used)\n• Fixed some issues with the upper hallway background\n• Fixed an issue with the scenes changing from night/day, where buttons wouldn't repopulate\n• Fixed some issues with scenes starting before scene-changes happened\n• Fixed an issue with garage-choices showing after going to the kitchen after an early start in the garage\n• Fixed issues with naming of tablet-images\n• Fixed a random placement outside after talking to fs\n• Fixed some misplaced variable declarations in dialogue\n• Fixed some issues during morning events where there wouldn't be a \"you're late\" situation based on time\n• Fixed a minor bug where the variable \"end_game\" wasn't defined, crashing the game\n• Fixed some wrong name-assignments in the dialogue\n• Fixed the upstairs/downstairs hover-events in the entrance-location (hoverstate was slightly overlapping)\n• Fixed a couple glitches occurring during location-transitions\n• Fixed #9 - bug - issue with wrong menu-statement if going to garage after school\n• Fixed #10 - bug - issue with detention dialogue repeating after coming home after school\n• Fixed #11 - bug - jumping to wrong location issue\n• Fixed #12 - bug - triggering repair event after kitchen dialogue (weekend) doesn't go to garage\n• Fixed #13 - bug - going to fs' bedroom at night crashes the game\n• Fixed #14 - bug - bug in not defined breakfast items\n• Fixed #15 - bug - watching intro quits to menu\n• Fixed #17 - bug - help mom triggering outside (or any other location than kitchen / living room)\n• Fixed #18 - bug - UI problem with phone\n• Fixed #19 - bug - trophy case achievement triggering multiple times\n• Fixed #20 - bug - all hidden achievement is showing when selecting one\n• Fixed #21 - bug - repeated morning events / breakfast events\n• Fixed #23 - bug - shower-event triggering after talking to the Principal at school\n• Fixed #24 - bug - school day triggers on weekends - closed, not able to reproduce\n• Fixed #25 - todo - fixed issues with the game_menu save/load looks (also fixed some minor issues with the in-game phone save/load screen)\n• Fixed #26 - todo - created custom preferences screen\n• Fixed #27 - todo - create custom confirm screens for quit and main menu\n• Fixed #29 - bug - jumping to outside house after studying for the algebra test\n• Fixed #30 - bug - background not updating on manual time-skipping\n• Fixed #31 - bug - load savegame on the custom load-screen on the phone saved instead of loaded\n• Fixed #32 - bug - panties left in the bathroom didn't show on the floor (disappeared)\n• Fixed #33 - bug - random selection of panties responses was out of bound\n• Fixed #35 - bug/todo - fixed the overlapping tooltips\n• Fixed #36 - bug - game crashes in the skip-breakfast chain\n• Fixed #37 - bug - issue with settime\n• Fixed #38 - bug - day restarting after going to kitchen after garage/intro\n• Fixed #41 - bug - arriving late to school doesn't trigger \"you're late\" event\n• Fixed #43 - bug - looping on day-events\n• Fixed #44 - bug - clicking the repair-icon in the garage crashed the game\n• Fixed #45 - bug - clicking back into house returned you to garage\n• Modified tooltips to utilize the new version in Renpy 6.99.14\n• Modified the splash-screen a little bit (tweaked timings for disclaimer)\n• Modified the amount of clean a shower gives\n• Modified the placement of specific items in the in-game menu (moved phone to the right, and cleanliness-icon to the left besides the stat-icon)\n• Modified how the bike-repair functions - it now gets easier over time, as you gain more knowledge about he bike / more experience\n• Modified the addtime() function to allow it to be used by other means than just calling it\n• Removed a bit of superflous commented code\n• Removed the old lower hallway (everything is now reachable from entrance)\n• Rewrote the whole game-logic (still a WIP)\n• Started work on an Achievement system (WIP) (accessible via the phone)\n• Updated the look of the phone-interface / phone itself\n• Updated most of the image-files for use in the in-game gadgets (smaller filesizes, among other things)")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "HSS"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = False
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None

define config.end_splash_transition = dissolve

## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

define config.developer = True

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 20


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "HSS-1510067763"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**patch.**',None)
    build.classify('saves/**.**',None)
    build.classify('cache/**.**',None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.archive('scripts','all')    
    build.archive('images','all')
    build.archive('backgrounds','all')
    build.archive('characters','all')
    build.archive('fonts','all')
    build.archive('classes','all')

    build.classify('game/images/backgrounds/**.jpg', 'backgrounds')
    build.classify('game/images/backgrounds/**.jpeg','backgrounds')
    build.classify('game/images/backgrounds/**.mkv', 'backgrounds')
    build.classify('game/images/backgrounds/**.png', 'backgrounds')
    build.classify('game/images/characters/**.jpg', 'characters')
    build.classify('game/images/characters/**.jpeg','characters')
    build.classify('game/images/characters/**.mkv', 'characters')
    build.classify('game/images/characters/**.png', 'characters')
    build.classify('game/images/**.jpg', 'images')
    build.classify('game/images/**.jpeg','images')
    build.classify('game/images/**.mkv', 'images')
    build.classify('game/images/**.png', 'images')
    build.classify('game/classes/**.rpy','classes')
    build.classify('game/classes/**.rpyc','classes')
    build.classify('game/**.rpy', 'scripts')
    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/gui/fonts/**.otf','fonts')
    build.classify('game/gui/fonts/**.ttf','fonts')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    
    # Include README.txt
    build.classify('README.txt', 'all')
    build.classify('changelog.txt','all')

    # But exclude all other txt files.
    build.classify('**.txt', None)

    # Add png and jpg files in the game directory into an archive.
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


    

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

define build.itch_project = "errilhl/hss-highschool-shenanigans"

# define config.archives = ['patch']