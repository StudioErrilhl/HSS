init python:

    def info_hover(a,b="hide"):
        # a what to show/hide
        # b show/hide
        c = [left]
        d = 'master'
        if a == "stats_hover":
            c = [left,stats_hover_transform]
            d = 'screens'
        elif a == "tshirt_overlay":
            c = [left,tshirt_overlay_transform]
            d = 'screens'
        if b == "show":
            renpy.show(a,at_list=c,layer=d,zorder=970)
        else:
            renpy.hide(a,layer=d)

    def statschangenotify(a,f,p=False):
        # a = attribute to change
        # f = negative or positive value representing the change
        # p = longer pause or not

        # This function have no reason to be used by anything else, so keep it internal to "statschangenotify".
        def _generateText( what, who, f ):
            if f < 0:
                action = "decreased" if what in [ "dom", "aro", "cor", "att", "bad", "good","money" ] else "deteriorated"
            elif f == 0:
                action = False
            else:
                action = "increased" if what in [ "dom", "aro", "cor", "att", "bad", "good","money" ] else "improved"

            # Each variables in "format" by their order. So {0} = who, {1} = action, {2} = absolute value of "f".
            if what == "rel":
                if not action:
                    return "Your relationship with {0} did not change".format(who)
                else:
                    return "Your relationship with {0} has {1} by {2}".format( who, action, abs( f ) )
            elif what == "dom":
                if not action:
                    return "Your dominance over {0} did not change".format(who)
                else:
                    return "Your dominance over {0} has {1} by {2}".format( who, action, abs( f ) )
            elif what == "aro":
                if not action:
                    return "{0}'s arousal did not change".format(who)
                else:
                    return "{0}'s arousal has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "cor":
                if not action:
                    return "{0}'s corruption did not change".format(who)
                else:
                    return "{0}'s corruption has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "att":
                if not action:
                    return "{0}'s attitude did not change".format(who)
                else:
                    return "{0}'s attitude has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "anal":
                if not action:
                    return "{0}'s acceptance of anal sex did not change".format(who)
                else:
                    return "{0}'s acceptance of anal sex has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "pussy":
                if not action:
                    return "{0}'s acceptance of regular sex did not change".format(who)
                else:
                    return "{0}'s acceptance of regular sex has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "bj":
                if not action:
                    return "{0}'s acceptance of giving blowjobs did not change".format(who)
                else:
                    return "{0}'s acceptance of giving blowjobs has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == 'alignment':
                return "Your alignment changed by {0} to {1}".format(abs(f),getattr(store,a))
            elif what == "bad":
                if not action:
                    return "{0}'s bad influence over you did not change".format(who)
                else:
                    return "{0}'s bad influence over you has {1} by {2}".format(who, action, abs(f)).capitalize()
            elif what == "good":
                if not action:
                    return "{0}'s good influence over you did not change".format(who)
                else:
                    return "{0}'s good influence over you has {1} by {2}".format(who, action, abs(f)).capitalize()
            elif what == "money":
                if not action:
                    return "Your total cash amount did not change"
                else:
                    return "Your total cash amount decreased by {0} to {1}".format(abs(f),getattr(store,"fp_money"))

            return "Ooop's something really weird happened!"

        if a == "mc_b":
            setattr( store, a, min(getattr( store, a) + f,store.mc_b_max))
        else:
            setattr( store, a, getattr( store, a ) + f )

        if a[:2] in [ "fp", "fm", "nk", "fs", "sn" ]:
            if a[:2] in [ "fp", "fm", "fs" ]:
                if a[:2] == 'fm':
                    name = fmName.yourformal
                elif a[:2] == 'fs':
                    name = fsName.yourformal
                else:
                    name = a[:2]
                if a[3:] in [ "aro","cor","att","anal","pussy","bj" ]:
                    if a[:2] == 'fm':
                        name = fmName.Yourformal
                    elif a[:2] == 'fs':
                        name = fsName.Yourformal
                    else:
                        name = a[:2]
            else:
                name = a[:2]
            if name == a[:2]:
                text = _generateText( a[3:], str( getattr(store,name) ), f )
            else:
                text = _generateText( a[3:], str(name), f)
        elif a[:3] in ["lil","aru"]:
            name = a[:3]
            if name == a[:3]:
                text = _generateText(a[4:],str(getattr(store,name)),f)
        elif a == "mc_b":
            if f < 0:
                text = "Your motorcycle build decreased by {0}".format( abs( f ) )
            else:
                text = "Your motorcycle build increased by {0}".format( abs( f ) )
        elif a == "punishment_late":
            text = "You've gotten a mark for being late. Current amount is {0}. If you get more than 5 marks, you will get in trouble".format( store.punishment_late )
        else:
            text = "Ooop's something really weird happened!"

        if not "deteriorated" in text:
            renpy.notify((text))
        else:
            renpy.notify((text,"decrease"))

        if p:
            renpy.pause(1.1)
        else:
            renpy.pause(.1)

    def weighted_choice(choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
            if upto + w >= r:
                return c
            upto += w
        assert False, "Shouldn't get here"

init 10 python:
    def addday(dayamount):
        global day_week,current_month_day,current_month,filth_val
        local_dw = day_week
        day_week = 0 if day_week == 6 else day_week+1
        if local_dw != day_week:
            if current_month_day == months_days[current_month][1]:
                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                current_month_text = months_days[current_month][0]
                current_month_day = 1
            else:
                current_month_day += 1
                day_ahead = True
        if filth_val:
            filth_val += 10
        setattr(store,'current_time','06:00')
        setattr(store,'day_week',day_week)
        setattr(store,'current_month',current_month)
        if not charge_phone and battery_text < 50:
            setattr(store,'battery_text',0)
        elif charge_phone:
            setattr(store,'battery_text',100)
    def addtime(hours=False,minutes=False,update_scene=False,sec_call=False):
        global current_time,day_week,current_month_text,current_month,current_month_day,months_days,day_ahead,current_location,night,day,morning,battery_text,wetshower,not_entered,nc_action_started,nc_action_completed,nc_event,visit_icafe_4,nc_happens,filth_val,tmp_filth_val
        local_dw = day_week
        addhour = False
        not_entered = True
        sethour = hours
        starthour = current_time[:2]
        # wetshower = False
        if hours or minutes:
            local_time = current_time
            if hours:
                if int(current_time[:2])+int(hours) >= 24:
                    update_hour = (int(current_time[:2])+int(hours))-24
                    current_time = str(int(update_hour))+local_time[2:]
                    day_week = 0 if day_week == 6 else day_week+1
                    if local_dw != day_week:
                        if current_month_day == months_days[current_month][1]:
                            current_month = 0 if int(current_month) == 11 else (int(current_month)+1)
                            current_month_text = months_days[current_month][0]
                            current_month_day = 1
                        else:
                            current_month_day += 1
                            day_ahead = True
                else:
                    current_time = str(int(local_time[:2])+int(hours))+local_time[2:]
                if len(current_time) == 4:
                    current_time = '0'+current_time
                setattr(store,'current_time',current_time)
                setattr(store,'battery_text',battery_text -5)

            if minutes:
                if int(current_time[-2:])+int(minutes) >= 60:
                    update_minutes = str("%02d"%((int(local_time[-2:])+int(minutes))-60))
                    if local_time >= '23:30':
                        setattr(store,'current_time','00:00')
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month)+1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                                current_month_day += 1
                                day_ahead = True
                    else:
                        current_time = str(int(local_time[:2])+1)+':'+update_minutes
                    setattr(store,'battery_text',battery_text -5)
                else:
                    if local_time >= '23:30':
                        setattr(store,'current_time','00:00')
                        day_week = 0 if day_week == 6 else day_week+1
                        if filth_val and not tmp_filth_val:
                            tmp_filth_val = True
                            filth_val += 10
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month)+1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                                current_month_day += 1
                                day_ahead = True
                    else:
                        current_time = str(int(local_time[:2]))+':'+str(int(local_time[3:])+minutes)
                if len(current_time) == 4:
                    current_time = '0'+current_time
                setattr(store, 'current_time', current_time)

            if charge_phone:
                total = (int(sethour)+int(starthour))-int(starthour)
                if total >= 1:# and battery_text <= 100:
                    while (total):
                        if battery_text <= 100:
                            battery_text += 25
                            total -= 1
                    if battery_text > 100:
                        battery_text = 100

            if hacker_4 and int(current_time[:2]) == 18:
                renpy.call("nr_talk",'nr_first_visit')

            if nc_action_started >= 7 and int(current_time[:2]) in day:
                nc_action_started = False
                nc_action_completed = True
                visit_icafe_4 = True
                set_message('nc',nc,"Meet me at "+icafe+" tonight. Around 22-23")
                nc_event = 'icafe_talk_7_days'

            if nc_action_completed and nc_action_started >= 4 and (int(current_time[:2]) in [21,22,23]):
                nc_action_started = False
                set_message('nc',nc,""+str(hj)+" is here. You got... maybe an hour")
                nc_event = 'icafe_talk_hj'
                nc_happens = current_time
            if update_scene:
                if int(current_time[:2]) >= 22 or int(current_time[:2]) < 6:
                    current_imgs = list(renpy.get_showing_tags())
                    indices = [i for i, elem in enumerate(current_imgs) if '_morning' in elem]
                    if indices:
                        current_bg = current_imgs[indices[0]].replace('_morning','').replace('_glow','').replace('_build','').replace('_wallet','').replace('_finished','').replace('_with_car','').replace('_scene','').replace('_phone','').replace('_backpack','').replace('_',' ')
                        if current_bg == 'ufbn':
                            setattr(store,"bathroom_light",True)
                        else:
                            if sec_call:
                                renpy.call('change_loc',current_bg,loctrans=True,sec_call=sec_call,prev_loc=current_location)
                            elif current_bg:
                                renpy.call("change_loc",current_bg,loctrans=True,prev_loc=current_location)
                            else:
                                renpy.call('change_loc',current_location,loctrans=True,prev_loc=current_location)
                        indices = [i for i, elem in enumerate(current_imgs) if not '_morning' in elem]
                    else:
                        if sec_call:
                            renpy.call('change_loc',current_location,loctrans=True,sec_call=sec_call,prev_loc=current_location)
                        else:
                            renpy.call("change_loc",current_location,loctrans=True,prev_loc=current_location)
                elif int(current_time[:2]) >= 6 or int(current_time[:2]) < 22:
                    current_imgs = list(renpy.get_showing_tags())
                    indices = [i for i, elem in enumerate(current_imgs) if '_night' in elem]
                    mn_check = False
                    if indices:
                        if mn_check:
                            current_bg = current_imgs[indices[0]]
                        else:
                            current_bg = current_imgs[indices[0]].replace('_night','').replace('_glow','').replace('_build','').replace('_finished','').replace('_with_car','').replace('_scene','').replace('_phone','').replace('_backpack','').replace('_',' ')
                        if sec_call:
                            renpy.call('change_loc',current_bg,loctrans=True,sec_call=sec_call,prev_loc=current_location)
                        else:
                            renpy.call("change_loc",current_bg,loctrans=True,prev_loc=current_location)
                        indices = [i for i, elem in enumerate(current_imgs) if not '_night' in elem]
                    else:
                        if sec_call:
                            renpy.call('change_loc',current_location,loctrans=True,sec_call=sec_call,prev_loc=current_location)
                        else:
                            renpy.call("change_loc",current_location,loctrans=True,prev_loc=current_location)

    def settime(hours=False,minutes=False,update_scene=False,sec_call=False):
        global current_time,wetshower,not_entered
        wetshower = False
        not_entered = True
        if int(current_time[:2]) <= hours:
            if hours:
                if len(str(hours)) == 1:
                    hours = '0'+str(hours)
                current_time = str(hours)+str(current_time[2:])
                setattr(store, 'current_time', current_time)
        if int(current_time[3:]) < minutes:
            if minutes:
                if len(str(minutes)) == 1:
                    minutes = '0'+str(minutes)
                current_time = str(current_time[:3])+str(minutes)
                setattr(store, 'current_time', current_time)
        if update_scene:
            if int(current_time[:2]) >= 22 or int(current_time[:2]) < 6:
                current_imgs = list(renpy.get_showing_tags())
                indices = [i for i, elem in enumerate(current_imgs) if '_morning' in elem]
                if indices:
                    current_bg = current_imgs[indices[0]].replace('_morning','').replace('_glow','').replace('_scene','').replace('_phone','').replace('_',' ')
                    if current_bg == 'ufbn':
                        setattr(store,"bathroom_light",True)
                    else:
                        if sec_call:
                            renpy.call('change_loc',current_bg,sec_call=sec_call,prev_loc=current_location)
                        else:
                            renpy.call("change_loc",current_bg,prev_loc=current_location)
                    indices = [i for i, elem in enumerate(current_imgs) if not '_morning' in elem]
            elif int(current_time[:2]) >= 6 or int(current_time[:2]) < 22:
                current_imgs = list(renpy.get_showing_tags())
                indices = [i for i, elem in enumerate(current_imgs) if '_night' in elem]
                mn_check = False
                if indices:
                    if mn_check:
                        current_bg = current_imgs[indices[0]]
                    else:
                        current_bg = current_imgs[indices[0]].replace('_night','').replace('_glow','').replace('_scene','').replace('_phone','').replace('_',' ')
                    if sec_call:
                        renpy.call('change_loc',current_bg,sec_call=sec_call,prev_loc=current_location)
                    else:
                        renpy.call("change_loc",current_bg,prev_loc=current_location)
                    indices = [i for i, elem in enumerate(current_imgs) if not '_night' in elem]

    def inv_list_fetch():
        global inv_list
        inv_list = []
        for file in renpy.list_files():
            if file.startswith('images/inventory/') and file.endswith('.webp'):
                if 'hover' in file:
                    inv_list.append(file.replace('images/inventory/','').replace('_idle','').replace('_hover','').replace('_insensitive','').replace('.webp',''))
        return inv_list

    def chardesc_fetch(char=False):
        global chars, char_desc, chardesc
        for i in chars:
            if char == i[1]:
                chardesc = char_desc[i]
            else:
                chardesc = False

    def alarm_setting(hour=False,minute=False):
        if hour:
            if alarmhour < 23:
                setattr(store, 'alarmhour', getattr(store,'alarmhour') + 1)
            else:
                setattr(store, 'alarmhour', 0)
        if minute:
            if alarmminute < 50:
                setattr(store, 'alarmminute', getattr(store, 'alarmminute')+10)
            else:
                setattr(store, 'alarmminute', 0)

    def randomize_appstorelists():
        random.shuffle(playstore_recommended)
        random.shuffle(playstore_games)
        random.shuffle(playstore_apps)

    def image_unlock(imagetounlock=None):
        global images_unlocked
        if imagetounlock is not None:
            images_unlocked.append(imagetounlock)
            renpy.notify('Image unlocked')

    def realtime_search(searchterm=False,listname=False):
        if searchterm and listname:
            returnlist = []
            for li in listname:
                currentlist = eval(str(li))
                result = [[l.lower().find(searchterm) >= 0 for l in thisList] for thisList in currentlist]
                indices = [i for i, s in enumerate(result) if True in s]
                if indices:
                    for c in indices:
                        if currentlist[c] not in returnlist:
                            returnlist.append(currentlist[c])
            if returnlist:
                return returnlist
            else:
                return False

    def hide_phone_screens():
        renpy.hide_screen('phonescreen')
        renpy.hide_screen('warning_screen')

    def hide_tablet_screens():
        renpy.hide_screen('tabletscreen')
        renpy.hide_screen('warning_screen')

    def read_hint(hint=False):
        global hints,read_hints
        if hint:
            read_hints.append(hint)
            hints.remove(hint)

    def disable_hint(hint=False):
        global read_hints,disabled_hints
        if hint:
            disabled_hints.append(hint)
            read_hints.remove(hint)

    def delete_hint(hint=False):
        global hints,read_hints,disabled_hints
        if hint in hints:
            hints.remove(hint)
        if hint in read_hints:
            read_hints.remove(hint)
        if hint in disabled_hints:
            deleted_hints.append(hint)
            disabled_hints.remove(hint)

    def restore_hints():
        global hints,disabled_hints
        for hint in disabled_hints:
            if hint not in hints:
                hints.append(hint)
                disabled_hints.remove(hint)
            else:
                disabled_hints.remove(hint)

    def set_hint(hint=False):
        global hints,read_hints,default_hints,jiggle_phone
        if hint:
            if hint not in hints+read_hints+disabled_hints:
                hints.append(hint)
                jiggle_phone = True

    def read_message(char=False,charobj=False,message=False):
        global messages,read_messages
        if char and charobj and message:
            if (char,charobj,message) not in read_messages:
                read_messages.append((char,charobj,message))
            if (char,charobj,message) in messages:
                messages.remove((char,charobj,message))

    def disable_message(message=False):
        global read_messages,disabled_messages
        if message:
            disabled_messages.append(message)
            read_messages.remove(message)

    def delete_message(message=False):
        global messages,read_messages,disabled_messages
        if message in messages:
            messages.remove(message)
        if message in read_messages:
            read_messages.remove(message)
        if message in disabled_messages:
            deleted_messages.append(message)
            disabled_messages.remove(message)

    def restore_messages():
        global messages,disabled_messages
        for message in disabled_messages:
            if message not in messages:
                messages.append(message)
                disabled_messages.remove(message)
            else:
                disabled_messages.remove(message)

    def set_message(char=False,charobj=False,message=False,image=False):
        renpy.notify('You\'ve received a text message')
        global messages,read_messages,default_messages
        if message:
            # if message not in messages+read_messages+disabled_messages:
            messages.append((char,charobj,message))

    def showWeather(cw=False):
        global weather, current_time, night
        if cw:
            if cw > 3:
                cw = weather = 1
            if int(current_time[:2]) in night:
                if cw == 1:
                    img = "gui/night_rain_icon.webp"
                elif cw == 2:
                    img = "gui/night_rain_icon.webp"
                else:
                    img = "gui/night_icon.webp"
            else:
                if cw == 1:
                    img = "gui/morning_rain_icon.webp"
                elif cw == 2:
                    img = "gui/morning_rain_icon.webp"
                else:
                    img = "gui/sun_icon.webp"
            return img

    def fetchMapFiles(prefix=False):
        currentLocationList = []
        if prefix:
            for file in renpy.list_files():
                if file.startswith('gui/map/') and file.endswith('.webp'):
                    if prefix in file:
                        if 'hover' in file:
                            name = file.replace('gui/map/','').replace('_hover','').replace('.webp','').replace('map_','')
                            currentLocationList.append(name)
            return currentLocationList


# Copyright 2017  Anne O'Nymous - AON/SC4X
#
#  Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

init python hide:
    notice = """
    (c) 2017  Anne O'Nymous - AON/SC4X
    All the code is under the simplified BSD license :
    http://opensource.org/licenses/BSD-2-Clause
    """

python early:
    #  In version previous to 6.99.13, lex.require can generate a crash if the
    # file is in UTF. Prefer the following line (lex.match) unless you use
    # Ren'py 6.99.13 or further. Note that it's always one or the other, never
    # both.
    def dynamicNamesParse( lex ):
        vName = lex.require( lex.word )
        if lex.match(":") is None: lex.error( "':' expected." )
        lex.expect_eol()
        kwargs = {}
        lex.expect_block('dynamicNames statement')
        sLex = lex.subblock_lexer()
        sLex.advance()
        while sLex.eob is False:
            k = sLex.match(r'[_A-Za-z]\w+')
            if k is None: sLex.error( "Not a valid ID." )
            if sLex.eol() is True: sLex.error( "Can't be empty." )
            kwargs[k] = sLex.rest()
            sLex.advance()
        return ( vName, kwargs )

    def dynamicNamesExecute( t ):
        ( vName, kwargs ) = t
        setattr( store, vName, DynamicNames( **kwargs ) )

    renpy.register_statement( 'defineDynamicName', parse=dynamicNamesParse, execute=dynamicNamesExecute, block=True, init=True )
    renpy.register_statement( 'define_dynamic_name', parse=dynamicNamesParse, execute=dynamicNamesExecute, block=True, init=True )
    renpy.register_statement( 'dynamicName', parse=dynamicNamesParse, execute=dynamicNamesExecute, block=True )
    renpy.register_statement( 'dynamic_name', parse=dynamicNamesParse, execute=dynamicNamesExecute, block=True )

    class DynamicNames( object ):
        def __init__( self, **kwargs ):
            self._alls = {}
            for k in kwargs:
                v = eval( kwargs[k] )
                if not isinstance( v, tuple ): v = ( v, )
                self._alls[k] = v
                self._alls[k[:1].upper() + k[1:]] = v
                self._alls[k.upper()] = v

        def __getattr__( self, aName ):
            if     aName == "_alls":    return super( DynamicNames, self).__getattribute__( aName )
            if not aName in self._alls: return "I FORGET TO SET THIS"
            aValue = ""
            for atom in self._alls[aName]: aValue += atom() if callable( atom ) else atom
            if ord(aName[:1]) >= 97:
                return aValue
            elif (65 < ord(aName[:1]) < 90) and (65 < ord(aName[-1:]) < 90):
                return aValue.upper()
            else:
                return aValue[:1].upper() + aValue[1:]