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

define config.version = "0.022-(Alpha)"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("{b}HSS (or HighSchool Shenanigans){/b} is an adult-themed visual novel, with some randomness, and a lot of sexy content. You're playing as <player> (pick your name, or default to Marten), an 18 year old boy who's finishing high school, and is mildly anxious about his exams, the lack of a girlfriend, noone to take to the dance, and how to get his motorcycle rebuilt properly. Add to this an abundance of hot girls in his vicinity, and you got most of the plot right there. At least if you only knew what opportunities you have right at your feet.\n\nThe game is about discovering those opportunities, and realising what you can do, not to mention WHO you can do!\n\nThe game is in very early development, and currently we're working on the game mechanics, how to modify relationships, how to build a believeable story, and how to decide which characters get to do what with whom.\n\n")
#••••••
define gui.changelog = _("{b}0.022:{/b}\n• Added a main info-screen on first game-load / startup, introducing some concepts\n• Added a help-screen to the phone\n• Added a check to see if you're 100% clean before allowing a shower\n• Added random dinner-events\n• Added a minimum relationship limit for entering Juliette's room\n• Added nk_events.rpy for events pertaining to Karen\n• Added that you need to pick up your backpack to keep an inventory (WIP)\n• Added Anne character images/expressions (ahead,blushing,crying,mad,sad,smile)\n• Added a principal's office at the school\n• Added the help-button to the phone-screen (previously it was just a textbutton with \"Help\")\n• Cleaned up config.rpy\n• Closed #60 - bug - duplicate issue\n• Fixed a few minor issues with alignment/positioning on the calendar\n• Fixed a few issues with missing capitals for specific names in specific events\n• Fixed a minor bug in morning-events\n• Fixed a bug with the phone charging event in the MCs bedroom\n• Fixed a minor bug in image-declaration for an image button in the upper hallway\n• Fixed some issues popping up due to the rewrite of the inventory screen\n• Fixed some flashing / loading issues on kitchen events\n• Fixed some achievements issues (the been-everywhere achievement)\n• Fixed a bug in the addtime-function\n• Fixed #16 - todo - fix the inventory background + scroll\n• Fixed #42 - todo - redo GUI\n• Fixed #58 - bug - phone-background not updating/changing when switching from window to fullscreen, or vice versa\n• Fixed #59 - bug - shower scene not exiting properly if not finished before going out of bathroom\n• Fixed #62 - bug - not showing dayname in the calendar\n• Fixed #63 - bug - first day talk, finding sister didn't do anything\n• Fixed #64 - bug - going to kitchen after working on bike in the morning renders no exit-buttons\n• Fixed #66 - bug - flashing bottles in the kitchen\n• Fixed #73 - bug - the one-hour garage bit leaves the kitchen unavailable\n• Modified user_screens to a more concise way of switching between day/night for buttons and other on-screen items\n• Modified the colors for choice-menu, as the hover-text sort of faded into the background\n• Modified the change_loc to remove \"_loc\" if present as well (to cater for less errors)\n• Reinstated the talk with the sister in the upper hallway (after stealing her princess plug)\n• Started remaking the inventory-screen (there will be more functionality here in future updates, like item descriptions, ability modifiers if used, and so on)\n• Started work on the new event-functionality, with separation per character more than location and other shifting criteria\n• Updated the settime-label to a function, and added scene-change ability (day/night), same as addtime() has\n• Updated more of the GUI\n• Updated the GUI in-game")

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