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

define config.name = _("HSS")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False

## The version of the game.

define config.version = "0.1_(new_version_number)"

## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("{b}HSS{/b} is an adult-themed visual novel, with a non-linear story, plenty of sexy content, and an actual story as well. You're playing as <player> (pick your name, or default to Marten), an 18 year old boy who's finishing high school, and is mildly anxious about his exams, the lack of a girlfriend, noone to take to the after-graduation party, and how to get his motorcycle rebuilt properly. Add to this an abundance of hot girls in his vicinity, and you got most of the plot right there. At least on the surface... and if you only knew what opportunities you have... right at your feet.\n\nThe game is about discovering those opportunities, figuring out the real story, and realising what you can do, not to mention {i}who{/i} you can do!")

define gui.about_2_head = _("{b}Disclaimer!{/b}")

define gui.about_2_text = _("The game is in very early development, and currently we're working on the game mechanics, how to modify relationships, how to build a believeable story, and how to decide which characters get to do what with whom.\n\n")

define gui.credits = _("Credit where credit's due - this game wouldn't have been possible without the use of {a=https://www.renpy.org/}{b}Ren'Py{/b}{/a}, and by proxy, {a=https://www.patreon.com/renpytom}{b}RenpyTom{/b}{/a}, the creator of Ren'py.\n\nOther worthy of mentioning is: {b}Remix{/b}, whom you can find on the Renpy Discord, and other places. He's been kind enough to help with some of the more advanced code. (More names to come)")

define gui.credits_2_head = False

define gui.credits_2_text = False

#••••••
define gui.changelog = _("{b}0.026:{/b}\n• Added new graphics for Anne\n• Added new graphics for Catherina\n• Added new graphics for Jules\n• Added new graphics for Karen\n• Added new graphics for Marten\n• Added new graphics for Ron\n• Added a cheat-mode for money (click on the money under the calendar to add $100)\n• Fixed the call-screen\n• Fixed #182 - bug - \"Marten\" shows up during dinner events even when another name is picked\n• Fixed some minor graphical bugs due to missing transparancies after changing to .webp for the graphics\n• Fixed a bug where finishing the bike didn't trigger the achievement\n• Fixed a position issue with the carkeys in the livingroom\n• Fixed a position issue with the overlay for the phone in the menu\n• Fixed some issues going from daytime to nighttime in the livingroom\n• Fixed some issues with advancing time in the garage and outside\n• Fixed the nighttime bad weather functionality in the livingroom\n• Modified the phone in the menu so it will hide the phone if it's showing\n• Moved the money under the calender\n• Realigned the menu-text on the game-menu (before game-start)\n• Redid the livingroom graphics\n• Rewrote a bit of the convo from the Internet Cafe, to better match the characters\n• Started converting all sprite-images to layeredimage\n• Updated the gallery-screen and bathroom event with Jules with new graphics\n\n{b}0.025-final:{/b}\n• Added the missing background-images for Marten's bedroom\n• Closed #136 - bug - rollback not working correctly - not able to reproduce\n• Closed #160 - bug - settime adding an hour in the morning - not a bug, intentional, only happening on weekends\n• Fixed #174 - bug - occupied bathroom at night not showing correctly\n• Moved the unfinished items from the 0.025 project to the 0.026 project on Github\n\n{b}0.025-rc4:{/b}\n• Added max-stats for main NPCs (just the stats, the logic is not implemented yet)\n• Added that you get dirty walking to school in bad weather and/or rainstorms\n• Added that if you're dirty when going to bed, you add 10 to filth_val (regardless if you skip to next day, or sleep in normal way)\n• Changed all the graphics from .png to .webp - should definitely affect the overall game-size\n• Closed #39 - todo - expand on cleanliness in-game\n• Fixed #133 - todo - redo the wall on the upper hallway, and change image on wall\n• Fixed #139 - todo - create phone-images for characters\n• Fixed #155 - todo - lightswitch in bathroom had small GFX-issue\n• Fixed #156 - todo - recreate phone-menu visuals\n• Fixed #165 - todo - Marten's bedroom in the morning was lacking the wallet (if not picked up)\n• Fixed #178 - bug - no dissolve on Changelog in menu\n• Modified the preferences screen to use persistent variables\n• Modified the preferences screen to use a hover-state on buttons to distinguish them better\n• Redid the Help-page\n• Redid the game-menu (Load, preferences and so on)\n• Redefined persistent. to p.\n• Removed some superfluous bathroom lightswitch images\n• Set up pygame to check screen-resolution before allowing different windowed modes\n• Sorted the contact-list on the phone\n• Updated the About-page\n• Updated the preferences page\n\n{b}0.025-rc3:{/b}\n• Closed #172 - todo - create rain/bad weather outside livingroom\n• Closed #173 - todo - create alarm clock icon for the phone\n• Fixed a minor issue where Ron's same-day visit didn't happen\n• Redid the preferences menu in the main menu\n• Setup a choice before ending days\n• Updated the in-game help screen on the phone\n\n{b}0.025-rc2:{/b}\n• Added logic and variables for alarmclock (so it can be used, there just isn't a method for changing it)\n• Fixed #105 - todo - create an alarm-screen\n• Fixed an issue with time when arriving late to\n• Fixed a minor glitch with the \"end of day\" event, where the background wouldn't update to night-time\n\n{b}0.025-rc1:{/b}\n• Added event-variables so only one event can happen per person per day\n• Fixed an issue where you couldn't pick up the toolbox after completing that day's repair-events\n• Fixed #134 - bug - Karen-events doesn't always trigger after deciding to meet up in the evening\n• Fixed #159 - bug - icafe event chain\n• Fixed #161 - bug - rain stops during dialogue / choices outside\n• Fixed #164 - bug - multiple events on the same day\n\n{b}0.024-hotfix:{/b}\n• Fixed #164 - bug - tooltips under char image on phone-call\n• Fixed #167 - bug - problems going to beach after fixing bike\n• Fixed #168 - bug - gfx-issues entrance during nighttime\n• Fixed #169 - bug - tablet_no_content_warning.webp not found\n• Fixed #170 - bug - bike-stat doesn't stop at 150\n• Fixed #171 - bug - panties disappearing (no choice menu) in bathroom\n• Fixed an issue with the wet shower not \"sticking\"\n• Fixed a wrongly named bedroom-background for Martens bedroom\n• Fixed a minor issue with the toolbox still showing when the bike is finished\n• Modified the options.rpy to not use .rpa-archives for the beta-builds\n• Modified the exit code for the upper hallway bathroom\n• Rewrote Marten's bedroom scenes (background code)\n\n{b}0.024-rc6:{/b}\n• Added the ability to skip days (click on the calendar date-display)\n• Continued #3, #39, #56, #57, #99, #107, #125 in 0.025\n• Fixed a minor bug in change_loc()\n• Updated TV-events (removed the \"placeholder\" text, created a few small choices, no graphics yet)    \n\n{b}0.024-rc5:{/b}\n• Added another option for regular showers\n• Closed #8 - todo - livingroom entrance button too complicated\n• Closed #78 - todo - fix the outside scenes (too dark, not bad weather and so on)\n• Closed #87 - todo - fix a requirement for showers after morning garage-work\n• Closed #143 - todo - add the icafe location\n• Closed #157 - todo - modify messages and calls to update the menu-glow-state for the phone\n• Fixed #154 - bug - select-buttons on bottom of Achievement-screen isn't there\n• Fixed a few small issues with the required shower event\n• Fixed a minor GFX-issue with the wine-bottles in the kitchen\n• Fixed a minor issues with the Karen-events in the morning\n• Fixed a few bugs / errors in a couple event-chains preventing the events to unfold as they should\n• Fixed an issue where you could visit Obuko (the internet cafe) before having discovered it in-game\n• Modified the close-button for the inventory to trigger hoverstate for both text and image regardless of what you hover\n• Modified the code for the clock-interface in the calendar widget\n• Updated .gitignore to cater for AON-plugin\n\n{b}0.024-rc4:{/b}\n• Added criteria that you need to have the carkeys to be able to do TripIt events (duh!)\n• Added a hint to the phone that you need carkeys to drive\n• Started work on #78 - todo - fix outside scenes (nighttime / rainstorm)\n• Changed the starting name-input to be mid-screen\n• Closed #121 - todd - fix .exe-icons\n• Closed #149 - todo - fix up the TripIt event\n• Closed #150 - todo - modify the weather-system / conditions\n• Closed #153 - todo - modify TripIt-event to happen when clicking car\n• Fixed issues with rain and TripIt car/events\n• Fixed a minor issue with the car disappearing during nighttime\n• Fixed a minor bug in the inventory (images showing hovered state instead of idle)\n• Fixed #151 - repeat-bug when going outside to do a TripIt-run\n• Fixed #152 - car not showing after menu-choice during TripIt event\n• Redid all the outside-images (outside house)\n• Redid the car-images\n• Update repository to no longer contain image-files\n\n{b}0.024-rc3:{/b}\n• Added wallet to inventory\n• Added icafe location/scene/background\n• Closed #116 - todo - create menu-colors / glow-colors for the phone in the menu\n• Closed #141 - todo - namebox for Catherina\n• Closed #142 - todo - nameboxes for unknown male and unknown female\n• Closed #144 - todo - add wallet to the inventory, with money info\n• Closed #148 - todo - fix the black car image to fit with the cartoon filter\n• Created new versions of the beach (both morning and night)\n• Fixed an issue with earnings for TripIt-driving events\n• Fixed so the car is actually behind the rain-graphics if bad weather\n• Modified the nameboxes a little bit (size/placement/cropping)\n• Renamed outside location\n• Remade the carkeys in inventory to match the TripIt car\n• Updated night-time backgrounds for upper hallway, school (outside), Principal Hudson's office, beach, entrance, garage, livingroom  \n\n{b}0.024-rc2:{/b}\n• Updated the call-screen (it should now be possible to use it for any person in the list, although only precreated events will actually play out)\n• Added a new Narrator-style\n• Added money as a Marten-stat\n• Added characters for \"unknown female\" and \"unknown male\"\n• Added a job-option for Marten during the evenings\n• Cleaned up options.rpy and the archive-methods for the game-files\n• Expanded on the Catherina-events\n• Fixed #146 - bug - panties respawns in bathroom after picking them up\n• Fixed #147 - bug - arriving home from school, showing wrong dialogue\n\n{b}0.024-rc1:{/b}\n• Added pagekeys to all scrollable displayables\n• Closed #81 - todo - fullscreen image from image-gallery\n• Closed #109 - todo - move stats to contacts on phone (as wontfix, due to not being needed)\n• Closed #122 - todo - create a way to get a contact into the contact list\n• Closed #135 - todo - implement cheat-option in the preferences screen\n• Fixed a few minor config-issues (disabling the console and such for releases)\n• Fixed #137 - bug - bottles in kitchen possible to click during dialogue / choices\n• Fixed a minor bug with the custom quit-screen\n\n{b}0.023-rc8:{/b}\n• Closed #72 - todo - adding Anne's sprites to game\n• Closed #115 - todo - check all events / dialogues so no buttons are available to be clicked during\n• Closed #117 - todo - polish the message / text screen\n• Closed #118 - todo - menu for short / long shower\n• Closed #130 - bug - hint from Ron triggering prematurely (not able to recreate)\n• Fixed #128 - bug - clicking lightswitch in bathroom potentially triggered the \"bathroom occupied\"\n• Fixed #129 - bug - wrong color for the lights on bathroom during nighttime\n• Fixed #131 - bug - wrong size for second image in phone gallery\n• Fixed #132 - bug - all-caps names (switch) is not working\n• Fixed a minor bug in the descriptions for inventory items where the names weren't being parsed\n• Fixed that Catherina is in your contact list before having gotten her number / info\n• Fixed a few minor GFX-bugs in different locations\n• Fixed overlays on the tshirt and phone in the menu during night-time\n• Lowered the limit for when you can enter Juliettes bedroom\n• Modified the user_screens.rpy to utilize more use-statements for repeated screens\n\n{b}0.023-rc7{/b} (with beta-test):\n• Added an icon for the .exe (and hopefully for the .app as well)\n• Closed #70 - todo - set hover-state for achievements selectors\n• Closed #106 - todo - change color and position of skip-message\n• Closed #111 - todo - finish the first shower-scene\n• Fixed #120 - bug - custom confirm doesn't show up correctly when using Alt+F4 or X on UI to close game\n• Fixed #123 - bug - info-screen having overlapping text\n• Fixed #124 - bug - staying home from school and working on the bike triggers the \"shower and get ready for school\" choice\n• Fixed #127 - bug - advancing time removes buttons / doors / movement on upper level\n• Fixed a bug in the first play intro where images where in the wrong place\n• Fixed a bug where shower-scene never happens\n• Fixed a bug with the first info-screen, where text overlapped\n\n{b}0.023-rc6:{/b}\n• Added a total-weight (per item) for the inventory\n• Added the first side-image of Marten\n• Added side-image of Ron (and stats-image)\n• Added a description for each item in the inventory\n• Added a list-color for every other list-item (so the list is alternating background colors per item)\n• Added a small event to the bathroom\n• Changed the phone-icon on the main phone-screen\n• Continued #3, #6, #39, #56, #57, #70, #72 in 0.024\n• Fixed an issue where hints from the text-message screen kept coming without stop\n• Fixed a bug with the ingame phone gallery\n• Fixed some issues with buttons behind say-screens getting triggered\n• Fixed a minor issue with the skip-background (it was still the old style)\n• Closed #2 - todo - expand on Juliette's issues with school\n• Closed #4 - todo - in-game menu (performed by the Preference menu on the phone)\n• Closed #7 - todo - Marten's side-image on right\n• Closed #61 - todo - clean up image folder\n• Closed #65 - todo - modify story-logic / interactions in game\n• Closed #67 - todo - get Natalie a namebox\n• Closed #82 - todo - fix the arriving late to school\n• Closed #92 - todo - add outlines of the phone and backpack when they're not picked up\n• Closed #102 - todo - new charge-phone icon in inventory\n• Closed #103 - todo - bathroom-events\n• Fixed #104 - bug - advancing time with scene-changes triggered an error (missing replacement for _background in filename)\n• Closed #110 - todo - set up text-messaging on the phone\n• Closed #112 - todo - finish the first talk with Ron\n• Closed #113 - todo - add second image to gallery\n• Closed #114 - todo - size of Ron's blushing side-image\n• Fixed #119 - bug - inventory duplicating items in list\n• Started #3 - todo - expand on driving with Karen to school (WIP)\n• Started #57 - todo - fix / finish the inventory (weight limits etc)\n• Moved quite a bit of images around, mostly from images/ to gui/\n• Removed char_images.rpy (replaced by defined_images.rpy)\n\n{b}0.023-rc5:{/b}\n• Added a way to close the phone with the home-button if on main screen\n• Added more background-images of Marten's bedroom, to cater for backpack and phone being present simultaneously, or separate\n• Added some more functionality for the full-size image view in gallery\n• Fixed the gallery on the phone, so only the correct image is available to click/view\n• Fixed #79 - todo - new close-button for full-screen image view on the phone\n• Fixed #86 - bug - travel to and from school events\n• Fixed #89 - todo - create backpack images for backgrounds when Anne is talking in Marten's bedroom\n• Fixed #91 - bug - school_on_time called\n• Fixed #93 - todo - night version of Marten's backpack\n• Fixed #94 - todo - make the phone always possible to pick up\n• Fixed #101 - todo - make it possible to put phone on charge from inventory\n• Modified the quit-screen to load the custom phone-quit screen instead of the default\n• Started work on #103 - todo - create bathroom events\n• Updated the help-text on the phone\n\n{b}0.023-rc4:{/b}\n• Added a preference in the custom preference menu on the phone to restore deleted hints\n• Added new icons to the phone\n• Added a call-button to the phone\n• Added a contact-list to the phone, which pops up when you click the call-button\n• Added more hints to the game, which will be shown on the phone\n• Fixed an issue with calling scenes via addtime() (they didn't update unless there was a specific index present)\n• Fixed #69 - todo - add proper images for backpack in Martens bedroom\n• Fixed #88 - bug - panties not showing up in inventory\n• Fixed #90 - bug - picking up one bottle in the kitchen crashed the game\n• Fixed #100 - bug - call to non-existing labels\n• Modified the phone-screens to use a tag-system for hiding (makes it a lot easier to hide screens when opening new ones)\n\n{b}0.023-rc3:{/b}\n• Added ESC-key closing for screens \n• Continued work on the inventory screen\n• Decided to rebuild a bit of logic (moving stuff together into fewer labels / using fewer files)\n• Fixed a minor bug with the Karen-dialogue in the morning (nk showed instead of Karen)\n• Fixed a name-bug in the fs-events file, naming Anne instead of Juliette while talking to Natalie\n• Fixed #40 - todo - ending up outside garage after finishing working on bike\n• Fixed #77 - todo - new icons for save and load on phone\n• Fixed #84 - todo - change stat-screen so clicked characters stays selected\n• Started on a hints-screen (on the phone)\n\n{b}0.023-rc2:{/b}\n• Did more work on the image-gallery in-game   \n• Added function to show the image full-screen    \n• Added a \"back to gallery\"-button\n• Added nr_events.rpy (Ron's events goes here)\n• Added a few conditionals to help with development\n• Fixed a minor issue with the fixed breakfast-lists\n• Fixed an issue with skipping time when Juliette is still mad at you\n• Fixed an issue with Juliette's talk, and her still being mad at you afterwards\n• Fixed #83 - bug - side-images not showing\n• Modified the statschangenotify-function to provide a separate notification if no change in stats occurred\n• Removed char_images.rpy (replaced by defined.rpy)\n\n{b}0.23-rc1:{/b}\n• Added Anne's image to the stats-screen\n• Added an image-gallery to the phone (WIP)\n• Continued #2, #4, #56, #57, #72 in project 0.023\n• Fixed a bug where the clock and battery-percentage didn't show on the phone notification bar\n• Fixed #74 - todo - help screen on phone\n• Fixed #75 - bug - the confirm-box text nearly unreadable\n• Fixed #76 - bug - after_fs_mad_morning no longer working in game\n• Rewrote the breakfast-event, so you can now chose to be mean or nice\n• Moved #3, #5, #6, #7, #8, #22, #28, #34, #39, #40, #61, #63, #67, #73 to the project for 0.023\n\n{b}0.022-rc3:{/b}\n• Added a main info-screen on first game-load / startup, introducing some concepts\n• Added a help-screen to the phone\n• Added a check to see if you're 100% clean before allowing a shower\n• Added random dinner-events\n• Added a minimum relationship limit for entering Juliette's room\n• Added nk_events.rpy for events pertaining to Karen\n• Added that you need to pick up your backpack to keep an inventory (WIP)\n• Added Anne character images/expressions (ahead,blushing,crying,mad,sad,smile)\n• Added a principal's office at the school\n• Added the help-button to the phone-screen (previously it was just a textbutton with \"Help\")\n• Fixed a minor bug in image-declaration for an image button in the upper hallway\n• Fixed some issues popping up due to the rewrite of the inventory screen\n• Fixed some flashing / loading issues on kitchen events\n• Fixed some achievements issues (the been-everywhere achievement)\n• Fixed a bug in the addtime-function\n• Fixed #64 - bug - going to kitchen after working on bike in the morning renders no exit-buttons\n• Fixed #66 - bug - flashing bottles in the kitchen\n• Fixed #73 - bug - the one-hour garage bit leaves the kitchen unavailable\n• Modified user_screens to a more concise way of switching between day/night for buttons and other on-screen items\n• Modified the change_loc to remove \"_loc\" if present as well (to cater for less errors)\n• Started remaking the inventory-screen (there will be more functionality here in future updates, like item descriptions, ability modifiers if used, and so on)\n• Updated the settime-label to a function, and added scene-change ability (day/night), same as addtime() has\n\n{b}0.022-rc2:{/b}\n• Cleaned up config.rpy\n• Closed #60 - bug - duplicate issue\n• Fixed a few minor issues with alignment/positioning on the calendar\n• Fixed a few issues with missing capitals for specific names in specific events\n• Fixed a minor bug in morning-events\n• Fixed a bug with the phone charging event in the MCs bedroom\n• Fixed #16 - todo - fix the inventory background + scroll\n• Fixed #42 - todo - redo GUI\n• Fixed #62 - bug - not showing dayname in the calendar\n• Fixed #63 - bug - first day talk, finding sister didn't do anything\n• Modified the colors for choice-menu, as the hover-text sort of faded into the background\n• Reinstated the talk with the sister in the upper hallway (after stealing her princess plug)\n• Started work on the new event-functionality, with separation per character more than location and other shifting criteria\n• Updated more of the GUI\n\n{b}0.022-rc1:{/b}\n• Fixed #58 - bug - phone-background not updating/changing when switching from window to fullscreen, or vice versa\n• Fixed #59 - bug - shower scene not exiting properly if not finished before going out of bathroom\n• Updated the GUI in-game\n\n{b}0.021.5{/b} bug fix:\n• Added a warning about no content on the tablet\n• Closed #50 - bug - problem with honda-scene - not able to reproduce, closed for now\n• Fixed a minor issue in the morning / wake up, when already late\n• Fixed a missing call to go to school in the morning (for specific events in the morning)\n• Fixed #46 - bug - advancing time via minutes doesn't update hours correctly\n• Fixed #47 - bug - advancing time via minutes doesn't scene correctly\n• Fixed #48 - bug - flashing between scenes\n• Fixed #49 - bug - panties-action triggers when entering room\n• Fixed #51 - bug - psd-files in images folder\n• Fixed #52 - bug - issues when picking up too many items (weight-limit exceeded)\n• Fixed #53 - bug - panties flashing in bathroom if left (this can be extended to other instances if the same flashing occurs)\n• Fixed #54 - bug - going to school-event doesn't always happen when going outside\n• Fixed #55 - bug - temporarily fixed looping talk with sister by removing it from the game - will be reinstated in next release\n• Increased weight-limit temporarily, to circumvent the problem with weigh-limit being reached, preventing picking up more items (this will be updated next release)\n\n{b}0.021-rc.b:{/b}\n• Added a way to go directly to the garage from inside (entrance <-> garage)\n• Added the ability to go between kitchen/livingroom\n• Added a cleanliness / dirty modifier / status (basically, you get dirty, then you need to wash)\n• Added a notification bar to the phone, with working time and battery indicator (the battery will be used for events in the game, depending on amount of charge left at any particular time)\n• Closed #1 - bug - missing content on Sunday (this has been closed, this is not a bug, although there should be more content coming in future updates)    \n• Fixed an issue with the scenes changing from night/day, where buttons wouldn't repopulate\n• Fixed some issues with scenes starting before scene-changes happened\n• Fixed an issue with garage-choices showing after going to the kitchen after an early start in the garage\n• Fixed issues with naming of tablet-images\n• Fixed a random placement outside after talking to fs\n• Fixed some misplaced variable declarations in dialogue\n• Fixed some issues during morning events where there wouldn't be a \"you're late\" situation based on time\n• Fixed a minor bug where the variable \"end_game\" wasn't defined, crashing the game\n• Fixed some wrong name-assignments in the dialogue\n• Fixed the upstairs/downstairs hover-events in the entrance-location (hoverstate was slightly overlapping)\n• Fixed a couple glitches occurring during location-transitions\n• Fixed #24 - bug - school day triggers on weekends - closed, not able to reproduce\n• Fixed #26 - todo - created custom preferences screen\n• Fixed #27 - bug - travel to school triggers on sunday\n• Fixed #29 - bug - jumping to outside house after studying for the algebra test\n• Fixed #30 - bug - clicking through time didn't update backgrounds\n• Fixed #35 - bug/todo - fixed the overlapping tooltips\n• Fixed #36 - bug - game crashes in the skip-breakfast chain\n• Fixed #37 - bug - issue with settime\n• Fixed #38 - bug - day restarting after going to kitchen after garage/intro\n• Fixed #41 - bug - arriving late to school doesn't trigger \"you're late\" event\n• Fixed #43 - bug - looping on day-events\n• Fixed #44 - bug - clicking the repair-icon in the garage crashed the game\n• Fixed #45 - bug - clicking back into house returned you to garage\n• Modified tooltips to utilize the new version in Renpy 6.99.14\n• Modified the splash-screen a little bit (tweaked timings for disclaimer)\n• Modified the amount of clean a shower gives\n• Modified the placement of specific items in the in-game menu (moved phone to the right, and cleanliness-icon to the left besides the stat-icon)\n• Removed a bit of superflous commented code\n• Updated most of the image-files for use in the in-game gadgets (smaller filesizes, among other things)\n\n{b}0.021-rc.a:{/b}\n• Added hover-functionality (together with click for the stat-screen)\n• Added a tablet in fs' room, and a phone for the MC for different purposes (none implemented as of yet)\n• Added save/load functionality to the phone-UI\n• Added ability to collect panties from the bathroom as well as the bedroom (different chance of finding them, the chance is not the same for both places)\n• Added multiple, random responses for item discovery in specific locations (will not pick certain responses if that item is already found/picked up)\n• Added versions of the MC bedroom with phone present for all hours of the day\n• Added tooltips to the phone-interface (currently a bit WIP)\n• Changed the entrance and the upper hallway\n• Closed #1 - bug - no content on Sunday after breakfast - this will be added in future updates, and is not a bug\n• Fixed a minor bug with achievements (wrong name used for an update-statement in locations.rpy)\n• Fixed a minor bug with looping on the bike-repair\n• Fixed a bug in the remove_item-function for the inventory (the notification didn't pop up, due to an error in the assigned variables used)\n• Fixed some issues with the upper hallway background\n• Fixed #9 - bug - issue with wrong menu-statement if going to garage after school\n• Fixed #10 - bug - issue with detention dialogue repeating after coming home after school\n• Fixed #11 - bug - jumping to wrong location issue\n• Fixed #12 - bug - triggering repair event after kitchen dialogue (weekend) doesn't go to garage\n• Fixed #13 - bug - going to sis' bedroom at night crashes the game \n• Fixed #14 - bug - bug in not defined breakfast items\n• Fixed #15 - bug - watching intro quits to menu\n• Fixed #17 - bug - help mom triggering outside (or any other location than kitchen / living room)\n• Fixed #18 - bug - UI problem with phone\n• Fixed #19 - bug - trophy case achievement triggering multiple times\n• Fixed #20 - bug - all hidden achievement is showing when selecting one\n• Fixed #21 - bug - repeated morning events / breakfast events\n• Fixed #23 - bug - shower-event triggering after talking to the Principal at school\n• Fixed #25 - todo - fixed issues with the game_menu save/load looks (also fixed some minor issues with the in-game phone save/load screen)\n• Fixed #27 - todo - create custom confirm screens for quit and main menu\n• Fixed #30 - bug - background not updating on manual time-skipping\n• Fixed #31 - bug - load savegame on the custom load-screen on the phone saved instead of loaded\n• Fixed #32 - bug - panties left in the bathroom didn't show on the floor (disappeared)\n• Fixed #33 - bug - random selection of panties responses was out of bound\n• Fixed #36 - bug - sunday events repeats / quit to menu\n• Modified how the bike-repair functions - it now gets easier over time, as you gain more knowledge about he bike / more experience\n• Modified the addtime() function to allow it to be used by other means than just calling it\n• Removed the old lower hallway (everything is now reachable from entrance)\n• Rewrote the whole game-logic (still a WIP)\n• Started work on an Achievement system (WIP) (accessible via the phone)\n• Updated the look of the phone-interface / phone itself\n\n{b}0.020:{/b}\n• Added / modified the inventory-system\n• Added on-screen navigation for the main bedroom (WIP) (both morning / night)\n• Added a cheat-system for characters (currenly you enable it via the console: cheat = True)\n• Added a kitchen for the morning breakfast and other scenes\n• Added an extra version of the bedroom, so that you can actually spot that items have been moved / picked up\n• Added nighttime versions of all rooms and other backgrounds\n• Added more expressions for Juliette\n• Added a first view of Anne (character sprite and side image)\n• Added a selection of inventory items\n• Fixed a minor bug in the menu (sub-menus didn't show up when opened directly from the main menu)\n• Fixed a bug in the morning where Marten would arrive in time for school, but still get punished\n• Fixed an issue with the inventory where items exceeding the width of the frame went outside, instead on down on a new line\n• Fixed another issue with the inventory system, where instead of increasing the amount of any given item, it would add another of the same item, messing up mostly everything\n• Fixed the inventory system so that it doesn't crash the game, and actually work with adding and removing items\n• Modified the intro / splashscreen\n• Modified the scene-picker to account for time of day and display the correct background\n\n{b}0.019:{/b}\n• Added a nighttime / evening version of the protagonist's bedroom\n• Added a weighted distribution for randomness (a function) so as to give things that are more likely to happen a greater chance to happen\n• Added backgrounds for each character namebox\n• Added a splashscreen (runs mostly one time, only the \"Studio Errilhl Presents\" is shown each time you start)\n• Added a bit more graphics of Juliette (she now shows a character image and a representation of herself when talking to her)\n• Fixed a dialogue-issue when talking to Juliette after 1 day had passed\n• Fixed a bug where, after talking to Jules on the first day, you went straight back to fixing your bike (the day is supposed to end)\n• Fixed a minor bug / issue where empty textboxes sometimes showed up without reason\n• Fixed a bug where the time would show :60 (for minutes) instead of \"ticking over\" to :00 and up the hour\n• Fixed a bug where hitting 60 on the minutes exactly would update the hour, but not change the minutes to 00 (instead of whatever they were previously)\n• Introduced new storylines, only the very start of them is added thus far\n• Modified the timing for the dialogue-text - it will now flow from start to finish, instead of showing up all at once\n• Redid the in-game menu (WIP)\n• Updated frames to also be transparent, like the rest of the UI\n• Updated the game-menu background to match the new UI\n• Updated the nvl-background to match the new UI\n• Updated the skip-background to match the new UI\n• Updated the color of the mainmenu buttons to match the new logo color\n\n{b}0.018:{/b}\n• Added a Patreon-button on the main starting page\n• Removed the text-title (basing on the logo title on the main screen now)\n• Kept the version-text\n• Fixed the look of the list-items in the changelog-page\n• Added a character image (when speaking) for Juliette\n• Redid the stats-screen, so there's now images for each character (together with name)\n• Redid the main menu - start of an ongoing project of redesigning the UI of the game\n• Redid the logo in Illustrator, to get a bigger, crispier logo\n• Rewrote the statusinfo function, after getting some tips regarding methods and easier usage\n• Added a way to patch the game for... specific functionality (you know what I mean!)\n• Started on an inventory system, but due to unforeseen problems, this is currently not working (the button is there, and it loads a screen that is meant for inventory items, but the adding, removing and showing of items doesn't currently work as it should)\n• Modified stats-screen to show current status for different modifiers instead of an overall preference for the romantic interests\n• Added different textboxes for named characters vs unknown / narrator\n\n{b}0.017:{/b}\n• Fixed the extra background showing up when showing the quit-confirmation\n• Updated the stats-screens\n• Fixed some minor code-issues (missing end-tags and such)\n• Added content (choices / dialogue)\n• Added more character variables\n• Redid the adding and subtracting points from Character traits (basically I've reduced the values, so to make the build-up a little longer and not reach ridiculous numbers)\n• Renamed some values (which makes savegames not work properly)\n• Changed the morning breakfast event to random elements showing up (still missing the attribute modifiers)\n• Redid the intro\n• Added a way to skip the intro if seen\n• Modified stats-screen\n• Added a progress in the stat-screen for the motorcycle rebuild\n• Added a pause-statement after / between stat-updates - this means some scenes lags a little bit, but I felt it was better to show the information for at least a little bit of time, so the player can get a clue as to what happened - the pause is only half a second for the notifications, bar the last, which has a very short pause just so that it doesn't disappear if the scene changes (.1 seconds)\n• Fixed a bug with motorcycle repair over the weekend, where the protagonist would continue to school after working on his bike - this does no longer happen\n• Added a changelog-screen on the main menu\n• Modifed the notify-function / screen\n• Created a notification-function, so I can use one line for most of the notification happening when something happens to character stats (reduced the amount of code-lines from 792 to 700, so quite a few lines less messy\n• Added a logo for the main menu page (it's not meant to be the actual logo, a better version will be coming)")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "HSS"

## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


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

# define config.character_id_prefixes = ["namebox"]

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

define config.window_icon = "gui/window_icon.webp"

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
    # build.classify('game/classes/**.rpy',None)
    build.classify('**patch.**',None)
    # build.classify('saves/**.**',None)
    # build.classify('cache/**.**',None)
    build.classify('game/AON-packages/**.**',None)
    build.classify('game/AON-packages',None)
    build.classify('game/AON.rpa',None)
    # build.classify('game/AONvve.rpy',None)
    build.classify('game/AONvve.rpyc',None)

    # ## To archive files, classify them as 'archive'.
    # ## The archive ability is currently turned off, to make it easier to make hotfixes for game-releases
    build.archive('scripts','all')
    build.archive('images','all')
    build.archive('gui','all')
    build.archive('backgrounds','all')
    build.archive('characters','all')
    build.archive('fonts','all')
    build.archive('classes','all')
    build.archive('events','all')

    build.classify('game/images/backgrounds/**.**', 'backgrounds')
    build.classify('game/images/backgrounds/**.jpeg','backgrounds')
    build.classify('game/images/backgrounds/**.mkv', 'backgrounds')
    build.classify('game/images/backgrounds/**.webp', 'backgrounds')
    build.classify('game/images/backgrounds/**.png','backgrounds')
    build.classify('game/images/characters/**.**', 'characters')
    build.classify('game/images/characters/**.jpeg','characters')
    build.classify('game/images/characters/**.mkv', 'characters')
    build.classify('game/images/characters/**.webp', 'characters')
    build.classify('game/images/characters/**.png','characters')
    build.classify('game/images/**.**', 'images')
    build.classify('game/images/**.jpeg','images')
    build.classify('game/images/**.mkv', 'images')
    build.classify('game/images/**.webp', 'images')
    build.classify('game/images/**.png','images')
    build.classify('game/classes/**.rpyc','classes')
    build.classify('game/events/**.rpyc','events')
    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/gui/fonts/**.otf','fonts')
    build.classify('game/gui/fonts/**.ttf','fonts')
    build.classify('game/gui/**.**','gui')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('README.txt')
    build.documentation('changelog.txt')

    build.classify('**.txt', None)

    # build.classify('game/**.webp', 'archive')
    # build.classify('game/**.jpg', 'archive')


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