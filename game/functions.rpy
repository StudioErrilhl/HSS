init -100 python:
    import random

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
                action = "deteriorated"
            elif f == 0:
                action = False
            else:
                action = "increased" if what in [ "dom", "aro", "cor", "att" ] else "improved"

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
            return "Oop's something really weird happen !"

        # A single line for all the possible variables, as well as both positive and negative values.
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
        elif a == "mc_b":
            if f < 0:
                text = "Your motorcycle build decreased by {0}".format( abs( f ) )
            else:
                text = "Your motorcycle build increased by {0}".format( abs( f ) )
        elif a == "punishment_late":
            text = "You've gotten a mark for being late. Current amount is {0}. If you get more than 5 marks, you will get in trouble".format( store.punishment_late )
        else:
            text = "Oop's something really weird happen !"

        if not "deteriorated" in text:
            renpy.notify((text))
        else:
            renpy.notify((text,"decrease"))

        if p:
            renpy.pause(.6)
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
    def addtime(hours=False,minutes=False,update_scene=False,seccall=False):
        global current_time,day_week,current_month_text,current_month,current_month_day,months_days,day_ahead,current_location,night,day,morning,battery_text
        local_dw = day_week
        addhour = False
        sethour = hours
        starthour = current_time[:2]
        if hours or minutes:
            local_time = current_time
            if hours:
                if int(local_time[:2])+int(hours) <= 23:
                    if int(local_time[:2])+int(hours) == 24:
                        current_time = str(int(0))+local_time[2:]
                        if len(current_time) == 4:
                            current_time = '0'+current_time
                        setattr(store, 'current_time', current_time)
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                                current_month_day += 1
                                day_ahead = True
                    elif int(local_time[:2])+int(hours) > 24:
                        current_time = str(int(0))+(int(local_time[:2])+int(hours)-24)+local_time[2:]
                        if len(current_time) == 4:
                            current_time = '0'+current_time
                        setattr(store, 'current_time', current_time)                        
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                                current_month_day += 1
                                day_ahead = True
                    else:
                        current_time = str(int(local_time[:2])+int(hours))+local_time[2:]
                        if len(current_time) == 4:
                            current_time = '0'+current_time
                        setattr(store, 'current_time', current_time)                        
                else:
                    if int(local_time[:2])+int(hours) == 24:
                        current_time = str(int(0))+local_time[2:]
                        if len(current_time) == 4:
                            current_time = '0'+current_time
                        setattr(store, 'current_time', current_time)                        
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                                current_month_day += 1
                                day_ahead = True
                    elif int(local_time[:2])+int(hours) > 24:
                        current_time = str(int(0))+str((int(local_time[:2])+int(hours)-24))+str(local_time[2:])
                        update_scene = True
                        if len(current_time) == 4:
                            current_time = '0'+current_time
                        setattr(store, 'current_time', current_time)                        
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                                current_month_day += 1
                                day_ahead = True
                    else:
                        current_time = str(int(local_time[:2])+int(hours))+local_time[2:]
                        if len(current_time) == 4:
                            current_time = '0'+current_time
                        setattr(store, 'current_time', current_time)
            if minutes:
                if int(local_time[-2:])+int(minutes) >= 60:
                    update_minutes = (int(local_time[-2:])+int(minutes))-60
                    if len(str(update_minutes)) == 1:
                        update_minutes = '0'+str(update_minutes)
                    if local_time == '23:30':
                        setattr(store,'current_time','00:00')
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                        
                                current_month_day += 1
                                day_ahead = True                        
                    else:
                        current_time = str(int(local_time[:2])+1)+':'+str(update_minutes)
                    if len(current_time) == 4:
                        current_time = '0'+current_time
                    setattr(store,'current_time',current_time)
                else:
                    if local_time == '23:30':
                        setattr(store,'current_time','00:00')
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                        
                                current_month_day += 1
                                day_ahead = True                        
                    else:
                        current_time = str(local_time[:2])+':'+str(int(local_time[3:])+minutes)
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

            if update_scene:
                print('update_scene')
                if int(current_time[:2]) >= 22 or int(current_time[:2]) < 6:
                    current_imgs = list(renpy.get_showing_tags())
                    indices = [i for i, elem in enumerate(current_imgs) if '_morning' in elem]
                    if indices:
                        current_bg = current_imgs[indices[0]].replace('_morning','').replace('_glow','').replace('_scene','').replace('_phone','').replace('_',' ')
                        if current_bg == 'upper_hallway_bathroom_night':
                            setattr(store,"bathroom_light",True)
                        else:
                            if seccall:
                                print('seccall 1')
                                renpy.call('change_loc',current_bg,sec_call=seccall)
                            else:
                                renpy.call("change_loc",current_bg)
                        indices = [i for i, elem in enumerate(current_imgs) if not '_morning' in elem]
                    else:
                        if seccall:
                            renpy.call('change_loc',current_location,sec_call=seccall)
                        else:
                            renpy.call("change_loc",current_location)
                elif int(current_time[:2]) >= 6 or int(current_time[:2]) < 22:
                    current_imgs = list(renpy.get_showing_tags())
                    indices = [i for i, elem in enumerate(current_imgs) if '_night' in elem]
                    print(indices)
                    mn_check = False
                    if indices:
                        if mn_check:
                            current_bg = current_imgs[indices[0]]
                        else:
                            current_bg = current_imgs[indices[0]].replace('_night','').replace('_glow','').replace('_scene','').replace('_phone','').replace('_',' ')
                        if seccall:
                            print('seccall 2')
                            renpy.call('change_loc',current_bg,sec_call=seccall)
                        else:
                            renpy.call("change_loc",current_bg)
                        indices = [i for i, elem in enumerate(current_imgs) if not '_night' in elem]
                    else:
                        if seccall:
                            renpy.call('change_loc',current_location,sec_call=seccall)
                        else:
                            renpy.call("change_loc",current_location)

    def settime(hours=False,minutes=False,update_scene=False,seccall=False):
        global current_time
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
                    if current_bg == 'upper_hallway_bathroom_night':
                        setattr(store,"bathroom_light",True)
                    else:
                        if seccall:
                            renpy.call('change_loc',current_bg,sec_call=seccall)
                        else:
                            renpy.call("change_loc",current_bg)
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
                    if seccall:
                        renpy.call('change_loc',current_bg,sec_call=seccall)
                    else:
                        renpy.call("change_loc",current_bg)
                    indices = [i for i, elem in enumerate(current_imgs) if not '_night' in elem]

    def inv_list_fetch():
        global inv_list
        inv_list = []
        for file in renpy.list_files():
            if file.startswith('images/inventory/') and file.endswith('.png'):
                if 'hover' in file:
                    if 'panties' in file:
                        tempvar = file.replace('images/inventory/','').replace('_idle','').replace('_hover','').replace('.png','').replace('fs_','').replace('_insensitive','').split('_')
                        if len(tempvar) == 3:
                            temp = tempvar[2]+' - '+tempvar[0]+' '+tempvar[1]
                        elif len(tempvar) == 2:
                            temp = tempvar[1]+' - '+tempvar[0]
                        inv_list.append(temp)
                    else:
                        inv_list.append(file.replace('images/inventory/','').replace('_idle','').replace('_hover','').replace('.png','').replace('fs_','').replace('_',' '))
        # print(inv_list)                        
        return inv_list

    # if day_week <= 4:
    #     $ morning = True if int(current_time[:2]) >= 6 and int(current_time[:2]) < 9 else False
    #     $ day = True if int(current_time[:2]) >= 9 and int(current_time[:2]) <= 17 else False
    #     $ evening = True if int(current_time[:2]) > 17 and int(current_time[:2]) < 22 else False
    #     $ night = True if int(current_time[:2]) >= 22 or int(current_time[:2]) >= 0 and int(current_time[:2]) < 6 else False
    # elif day_week >= 5:
    #     $ morning = True if int(current_time[:2]) >= 7 and int(current_time[:2]) <= 12 else False
    #     $ day = True if int(current_time[:2]) > 12 and int(current_time[:2]) <= 19 else False
    #     $ evening = True if int(current_time[:2]) > 19 and int(current_time[:2]) <= 23 else False
    #     $ night = True if int(current_time[:2]) >= 0 and int(current_time[:2]) < 7 else False
    # return

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

    def hide_phone_screens():
        renpy.hide_screen('phonescreen')

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
#        lex.require(":")
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

        def __getattr__( self, aName ):
            if     aName == "_alls":    return super( DynamicNames, self).__getattribute__( aName )
            if not aName in self._alls: return "I FORGET TO SET THIS"
            aValue = ""
            for atom in self._alls[aName]: aValue += atom() if callable( atom ) else atom
            return aValue if ord( aName[:1] ) >= 97 else aValue[:1].upper() + aValue[1:]    