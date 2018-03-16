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

define config.version = "0.024-(Alpha)"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("{b}HSS (or HighSchool Shenanigans){/b} is an adult-themed visual novel, with some randomness, and a lot of sexy content. You're playing as <player> (pick your name, or default to Marten), an 18 year old boy who's finishing high school, and is mildly anxious about his exams, the lack of a girlfriend, noone to take to the dance, and how to get his motorcycle rebuilt properly. Add to this an abundance of hot girls in his vicinity, and you got most of the plot right there. At least if you only knew what opportunities you have right at your feet.\n\nThe game is about discovering those opportunities, and realising what you can do, not to mention WHO you can do!\n\nThe game is in very early development, and currently we're working on the game mechanics, how to modify relationships, how to build a believeable story, and how to decide which characters get to do what with whom.\n\n")
#••••••
define gui.changelog = _("{b}0.024:{/b}\n• Added the ability to skip days (click on the calendar date-display)\n• Added another option for regular showers\n• Added criteria that you need to have the carkeys to be able to do TripIt events (duh!)\n• Added a hint to the phone that you need carkeys to drive\n• Added wallet to inventory\n• Added icafe location/scene/background\n• Added a new Narrator-style\n• Added money as a Marten-stat\n• Added characters for \"unknown female\" and \"unknown male\"\n• Added a job-option for Marten during the evenings\n• Added pagekeys to all scrollable displayables\n• Changed the starting name-input to be mid-screen\n• Cleaned up options.rpy and the archive-methods for the game-files\n• Closed #8 - todo - livingroom entrance button too complicated\n• Closed #78 - todo - fix the outside scenes (too dark, not bad weather and so on)\n• Closed #87 - todo - fix a requirement for showers after morning garage-work\n• Closed #81 - todo - fullscreen image from image-gallery\n• Closed #109 - todo - move stats to contacts on phone (as wontfix, due to not being needed)\n• Closed #116 - todo - create menu-colors / glow-colors for the phone in the menu\n• Closed #121 - todd - fix .exe-icons\n• Closed #122 - todo - create a way to get a contact into the contact list\n• Closed #135 - todo - implement cheat-option in the preferences screen\n• Closed #141 - todo - namebox for Catherina\n• Closed #142 - todo - nameboxes for unknown male and unknown female\n• Closed #143 - todo - add the icafe location\n• Closed #144 - todo - add wallet to the inventory, with money info\n• Closed #148 - todo - fix the black car image to fit with the cartoon filter\n• Closed #149 - todo - fix up the TripIt event\n• Closed #150 - todo - modify the weather-system / conditions\n• Closed #153 - todo - modify TripIt-event to happen when clicking car\n• Closed #157 - todo - modify messages and calls to update the menu-glow-state for the phone\n• Continued #3, #39, #56, #57, #99, #107, #125 in 0.025\n• Created new versions of the beach (both morning and night)\n• Expanded on the Catherina-events\n• Fixed a minor bug in change_loc()\n• Fixed a few small issues with the required shower event\n• Fixed a minor GFX-issue with the wine-bottles in the kitchen\n• Fixed a minor issues with the Karen-events in the morning\n• Fixed a few bugs / errors in a couple event-chains preventing the events to unfold as they should\n• Fixed an issue where you could visit Obuko (the internet cafe) before having discovered it in-game\n• Fixed issues with rain and TripIt car/events\n• Fixed a minor issue with the car disappearing during nighttime\n• Fixed a minor bug in the inventory (images showing hovered state instead of idle)\n• Fixed an issue with earnings for TripIt-driving events\n• Fixed so the car is actually behind the rain-graphics if bad weather\n• Fixed a few minor config-issues (disabling the console and such for releases)\n• Fixed a minor bug with the custom quit-screen\n• Fixed #137 - bug - bottles in kitchen possible to click during dialogue / choices\n• Fixed #146 - bug - panties respawns in bathroom after picking them up\n• Fixed #147 - bug - arriving home from school, showing wrong dialogue\n• Fixed #151 - repeat-bug when going outside to do a TripIt-run\n• Fixed #152 - car not showing after menu-choice during TripIt event\n• Fixed #154 - bug - select-buttons on bottom of Achievement-screen isn't there\n• Modified the nameboxes a little bit (size/placement/cropping)\n• Modified the close-button for the inventory to trigger hoverstate for both text and image regardless of what you hover\n• Modified the code for the clock-interface in the calendar widget\n• Redid all the outside-images (outside house)\n• Redid the car-images\n• Remade the carkeys in inventory to match the TripIt car\n• Renamed outside location\n• Started work on #78 - todo - fix outside scenes (nighttime / rainstorm)\n• Updated .gitignore to cater for AON-plugin\n• Updated TV-events (removed the \"placeholder\" text, created a few small choices, no graphics yet)\n• Updated repository to no longer contain image-files\n• Updated night-time backgrounds for upper hallway, school (outside), Principal Hudson's office, beach, entrance, garage, livingroom\n• Updated the call-screen (it should now be possible to use it for any person in the list, although only precreated events will actually play out)")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "HSS0.024"


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

# define config.developer = True

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
    build.classify('game/AON-packages/**.**',None)
    build.classify('game/AON-packages',None)
    build.classify('game/AON.rpa',None)
    build.classify('game/AONvve.rpy',None)
    build.classify('game/AONvve.rpyc',None)

    # ## To archive files, classify them as 'archive'.

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