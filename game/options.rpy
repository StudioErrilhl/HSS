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

define config.version = "0.023-(Alpha)"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("{b}HSS (or HighSchool Shenanigans){/b} is an adult-themed visual novel, with some randomness, and a lot of sexy content. You're playing as <player> (pick your name, or default to Marten), an 18 year old boy who's finishing high school, and is mildly anxious about his exams, the lack of a girlfriend, noone to take to the dance, and how to get his motorcycle rebuilt properly. Add to this an abundance of hot girls in his vicinity, and you got most of the plot right there. At least if you only knew what opportunities you have right at your feet.\n\nThe game is about discovering those opportunities, and realising what you can do, not to mention WHO you can do!\n\nThe game is in very early development, and currently we're working on the game mechanics, how to modify relationships, how to build a believeable story, and how to decide which characters get to do what with whom.\n\n")
#••••••
define gui.changelog = _("{b}0.023:{/b}\n•Added Anne's image to the stats-screen\n•Added an image-gallery to the phone (WIP)\n•Added an icon for the .exe (and hopefully for the .app as well)\n•Added a total-weight (per item) for the inventory\n•Added the first side-image of Marten\n•Added side-image of Ron (and stats-image)\n•Added a description for each item in the inventory\n•Added a list-color for every other list-item (so the list is alternating background colors per item)\n•Added a small event to the bathroom\n•Added a way to close the phone with the home-button if on main screen\n•Added more background-images of Marten's bedroom, to cater for backpack and phone being present simultaneously, or separate\n•Added some more functionality for the full-size image view in gallery\n•Added a preference in the custom preference menu on the phone to restore deleted hints\n•Added new icons to the phone\n•Added a call-button to the phone\n•Added a contact-list to the phone, which pops up when you click the call-button\n•Added more hints to the game, which will be shown on the phone\n•Added ESC-key closing for screens \n•Added nr_events.rpy (Ron's events goes here)\n•Added a few conditionals to help with development\n•Changed the phone-icon on the main phone-screen\n•Closed #2 - todo - expand on Juliette's issues with school\n•Closed #4 - todo - in-game menu (performed by the Preference menu on the phone)\n•Closed #7 - todo - Marten's side-image on right\n•Closed #61 - todo - clean up image folder\n•Closed #65 - todo - modify story-logic / interactions in game\n•Closed #67 - todo - get Natalie a namebox\n•Closed #70 - todo - set hover-state for achievements selectors\n•Closed #72 - todo - adding Anne's sprites to game\n•Closed #82 - todo - fix the arriving late to school\n•Closed #92 - todo - add outlines of the phone and backpack when they're not picked up\n•Closed #102 - todo - new charge-phone icon in inventory\n•Closed #103 - todo - bathroom-events\n•Closed #106 - todo - change color and position of skip-message\n•Closed #110 - todo - set up text-messaging on the phone\n•Closed #111 - todo - finish the first shower-scene\n•Closed #112 - todo - finish the first talk with Ron\n•Closed #113 - todo - add second image to gallery\n•Closed #114 - todo - size of Ron's blushing side-image\n•Closed #115 - todo - check all events / dialogues so no buttons are available to be clicked during\n•Closed #117 - todo - polish the message / text screen\n•Closed #118 - todo - menu for short / long shower\n•Closed #130 - bug - hint from Ron triggering prematurely (not able to recreate)\n•Continued #2, #4, #56, #57, #72 in project 0.023\n•Continued #3, #6, #39, #56, #57, #70, #72 in 0.024\n•Continued work on the inventory screen\n•Decided to rebuild a bit of logic (moving stuff together into fewer labels / using fewer files)\n•Did more work on the image-gallery in-game\n•Added function to show the image full-screen\n•Added a \"back to gallery\"-button\n•Fixed a minor bug in the descriptions for inventory items where the names weren't being parsed\n•Fixed that Catherina is in your contact list before having gotten her number / info\n•Fixed a few minor GFX-bugs in different locations\n•Fixed overlays on the tshirt and phone in the menu during night-time\n•Fixed a bug in the first play intro where images where in the wrong place\n•Fixed a bug where shower-scene never happens\n•Fixed a bug with the first info-screen, where text overlapped\n•Fixed an issue where hints from the text-message screen kept coming without stop\n•Fixed a bug with the ingame phone gallery\n•Fixed some issues with buttons behind say-screens getting triggered\n•Fixed a minor issue with the skip-background (it was still the old style)\n•Fixed the gallery on the phone, so only the correct image is available to click/view\n•Fixed an issue with calling scenes via addtime() (they didn't update unless there was a specific index present)\n•Fixed a minor bug with the Karen-dialogue in the morning (nk showed instead of Karen)\n•Fixed a name-bug in the fs-events file, naming Anne instead of Juliette while talking to Natalie\n•Fixed a minor issue with the fixed breakfast-lists\n•Fixed an issue with skipping time when Juliette is still mad at you\n•Fixed an issue with Juliette's talk, and her still being mad at you afterwards\n•Fixed a bug where the clock and battery-percentage didn't show on the phone notification bar\n•Fixed #40 - todo - ending up outside garage after finishing working on bike\n•Fixed #69 - todo - add proper images for backpack in Martens bedroom\n•Fixed #74 - todo - help screen on phone\n•Fixed #75 - bug - the confirm-box text nearly unreadable\n•Fixed #76 - bug - after_fs_mad_morning no longer working in game\n•Fixed #77 - todo - new icons for save and load on phone\n•Fixed #79 - todo - new close-button for full-screen image view on the phone\n•Fixed #83 - bug - side-images not showing\n•Fixed #84 - todo - change stat-screen so clicked characters stays selected\n•Fixed #86 - bug - travel to and from school events\n•Fixed #88 - bug - panties not showing up in inventory\n•Fixed #89 - todo - create backpack images for backgrounds when Anne is talking in Marten's bedroom\n•Fixed #90 - bug - picking up one bottle in the kitchen crashed the game\n•Fixed #91 - bug - school_on_time called\n•Fixed #93 - todo - night version of Marten's backpack\n•Fixed #94 - todo - make the phone always possible to pick up\n•Fixed #100 - bug - call to non-existing labels\n•Fixed #101 - todo - make it possible to put phone on charge from inventory\n•Fixed #104 - bug - advancing time with scene-changes triggered an error (missing replacement for _background in filename)\n•Fixed #119 - bug - inventory duplicating items in list\n•Fixed #120 - bug - custom confirm doesn't show up correctly when using Alt+F4 or X on UI to close game\n•Fixed #123 - bug - info-screen having overlapping text\n•Fixed #124 - bug - staying home from school and working on the bike triggers the \"shower and get ready for school\" choice\n•Fixed #127 - bug - advancing time removes buttons / doors / movement on upper level\n•Fixed #128 - bug - clicking lightswitch in bathroom potentially triggered the \"bathroom occupied\"\n•Fixed #129 - bug - wrong color for the lights on bathroom during nighttime\n•Fixed #131 - bug - wrong size for second image in phone gallery\n•Fixed #132 - bug - all-caps names (switch) is not working\n•Lowered the limit for when you can enter Juliettes bedroom\n•Modified the user_screens.rpy to utilize more use-statements for repeated screens\n•Modified the quit-screen to load the custom phone-quit screen instead of the default\n•Modified the phone-screens to use a tag-system for hiding (makes it a lot easier to hide screens when opening new ones)\n•Modified the statschangenotify-function to provide a separate notification if no change in stats occurred\n•Moved quite a bit of images around, mostly from images/ to gui/\n•Moved #3, #5, #6, #7, #8, #22, #28, #34, #39, #40, #61, #63, #67, #73 to the project for 0.023\n•Removed char_images.rpy (replaced by defined_images.rpy)\n•Rewrote the breakfast-event, so you can now chose to be mean or nice\n•Started #3 - todo - expand on driving with Karen to school (WIP)\n•Started #57 - todo - fix / finish the inventory (weight limits etc)\n•Started work on #103 - todo - create bathroom events\n•Started on a hints-screen (on the phone)\n•Updated the help-text on the phone")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "HSS0.023"


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

    # ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')
    # build.archive('scripts','all')
    # build.archive('images','all')
    # build.archive('backgrounds','all')
    # build.archive('characters','all')
    # build.archive('fonts','all')
    # build.archive('classes','all')

    # build.classify('game/images/backgrounds/**.jpg', 'backgrounds')
    # build.classify('game/images/backgrounds/**.jpeg','backgrounds')
    # build.classify('game/images/backgrounds/**.mkv', 'backgrounds')
    # build.classify('game/images/backgrounds/**.png', 'backgrounds')
    # build.classify('game/images/characters/**.jpg', 'characters')
    # build.classify('game/images/characters/**.jpeg','characters')
    # build.classify('game/images/characters/**.mkv', 'characters')
    # build.classify('game/images/characters/**.png', 'characters')
    # build.classify('game/images/**.jpg', 'images')
    # build.classify('game/images/**.jpeg','images')
    # build.classify('game/images/**.mkv', 'images')
    # build.classify('game/images/**.png', 'images')
    # build.classify('game/classes/**.rpy','classes')
    # build.classify('game/classes/**.rpyc','classes')
    # build.classify('game/**.rpy', 'scripts')
    # build.classify('game/**.rpyc', 'scripts')
    # build.classify('game/gui/fonts/**.otf','fonts')
    # build.classify('game/gui/fonts/**.ttf','fonts')

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