init -100 python:
    import random


init python:
    def statschangenotify(a,f,p=False):
        # a = attribute to change
        # f = negative or positive value representing the change
        # p = longer pause or not

        # This function have no reason to be used by anything else, so keep it internal to "statschangenotify".
        def _generateText( what, who, f ):
            if f < 0:
                action = "deteriorated"
            else:
                action = "increased" if what in [ "dom", "aro", "cor", "att" ] else "improved"

            # Each variables in "format" by their order. So {0} = who, {1} = action, {2} = absolute value of "f".
            if what == "rel":
                return "Your relationship with {0} has {1} by {2}".format( who, action, abs( f ) )
            elif what == "dom":
                return "Your dominance over {0} has {1} by {2}".format( who, action, abs( f ) )
            elif what == "aro":
                return "{0}'s arousal has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "cor":
                return "{0}'s corruption has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "att":
                return "{0}'s attitude has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "anal":
                return "{0}'s acceptance of anal sex has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "pussy":
                return "{0}'s acceptance of regular sex has {1} by {2}".format( who, action, abs( f ) ).capitalize()
            elif what == "bj":
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
    def addtime(hours=False,minutes=False):
        global current_hour,day_week,current_month_text,current_month,current_month_day,months_days,day_ahead,current_location,night,day,morning
        local_dw = day_week
        addhour = False
        if minutes:
            hour = current_hour
            if int(hour[3:])+int(minutes) >= int('60'):
                if debug:
                    "minutes happened"
                update_minutes = str((int(hour[3:])+int(minutes))-60)
                if len(update_minutes) == 1:
                    update_minutes = '0'+update_minutes
                addhour = True
                current_hour = current_hour[:3]+str(update_minutes)
                setattr(store, 'current_hour', current_hour)                
            else:
                update_minutes = str(int(hour[3:])+minutes)
                hour = hour[:3]
                if len(hour) == 2:
                    hour = '0'+str(hour)
                current_hour = str(hour)+str(update_minutes)
                setattr(store, 'current_hour', current_hour)
        if hours:
            if debug:
                "hours happened"
            hour = current_hour
            if addhour:
                if debug:
                    "addhour - hours happened first"
                if int(hour[:2])+hours+1 <= '23':
                    if debug:
                        "addhour - hours happened second"
                    current_hour = str(int(hours)+1)+hour[2:]
                    setattr(store, 'current_hour', current_hour)                    
                else:
                    if debug:
                        "addhour - hours happened third"
                    current_hour = str(int(hour[:2])+int(hours)+1)+hour[2:]
                    setattr(store, 'current_hour', current_hour)                    
            else:
                if int(hour[:2])+hours <= '23':
                    if debug:
                        "addhour - hours happened fourth"
                    if int(hour[:2])+int(hours) == 24:
                        current_hour = str(int(0))+hour[2:]
                        setattr(store, 'current_hour', current_hour)                        
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                                current_month_day += 1
                                day_ahead = True
                    elif int(hour[:2])+int(hours) > 24:
                        current_hour = str(int(0))+(int(hour[:2])+int(hours)-24)+hour[2:]
                        setattr(store, 'current_hour', current_hour)                        
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
                        current_hour = str(int(hour[:2])+int(hours))+hour[2:]
                        setattr(store, 'current_hour', current_hour)                        
                else:
                    if debug:
                        "addhour - hours happened fifth" 
                    if int(hour[:2])+int(hours) == 24:
                        current_hour = str(int(0))+hour[2:]
                        setattr(store, 'current_hour', current_hour)                        
                        day_week = 0 if day_week == 6 else day_week+1
                        if local_dw != day_week:
                            if current_month_day == months_days[current_month][1]:
                                current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                                current_month_text = months_days[current_month][0]
                                current_month_day = 1
                            else:
                                current_month_day += 1
                                day_ahead = True
                    elif int(hour[:2])+int(hours) > 24:
                        current_hour = str(int(0))+(int(hour[:2])+int(hours)-24)+hour[2:]
                        setattr(store, 'current_hour', current_hour)                        
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
                        current_hour = str(int(hour[:2])+int(hours))+hour[2:]
                        setattr(store, 'current_hour', current_hour)                        
            if len(current_hour) < 5:
                if debug:
                    "addhour - hours happened sixth"
                current_hour = '0'+current_hour
                setattr(store, 'current_hour', current_hour)                

        if addhour:
            if debug:
                "addhour happened"
            hour = current_hour
            if int(hour[:2])+int(hours)+1 <= '23':
                if debug:
                    "first addhour clause"
                if hours:
                    current_hour = str(int(hours)+1)+hour[2:]
                    setattr(store, 'current_hour', current_hour)                    
                else:
                    current_hour = str(int(hour[:2])+1)+str(hour[2:])
                    setattr(store, 'current_hour', current_hour)                    
            elif int(hour[:2])+hours+1 == '24':
                if debug:
                    "second addhour clause"
                current_hour = str(00)+hour[2:]
                setattr(store, 'current_hour', current_hour)                
            else:
                if debug:
                    "third addhour clause"
                current_hour = str(int(hour[:2])+hours+1)+hour[2:]
                setattr(store, 'current_hour', current_hour)                
            if len(current_hour) < 5:
                if debug:
                    "fourth addhour clause"
                current_hour = '0'+current_hour
                setattr(store, 'current_hour', current_hour)                

    # if day_week <= 4:
    #     $ morning = True if int(current_hour[:2]) >= 6 and int(current_hour[:2]) < 9 else False
    #     $ day = True if int(current_hour[:2]) >= 9 and int(current_hour[:2]) <= 17 else False
    #     $ evening = True if int(current_hour[:2]) > 17 and int(current_hour[:2]) < 22 else False
    #     $ night = True if int(current_hour[:2]) >= 22 or int(current_hour[:2]) >= 0 and int(current_hour[:2]) < 6 else False
    # elif day_week >= 5:
    #     $ morning = True if int(current_hour[:2]) >= 7 and int(current_hour[:2]) < 12 else False
    #     $ day = True if int(current_hour[:2]) >= 12 and int(current_hour[:2]) <= 19 else False
    #     $ evening = True if int(current_hour[:2]) > 19 and int(current_hour[:2]) <= 23 else False
    #     $ night = True if int(current_hour[:2]) >= 0 and int(current_hour[:2]) < 7 else False
    # return

label settime(hours=False,minutes=False):
    if hours:
        if len(str(hours)) == 1:
            $ hours = '0'+str(hours)
        $ current_hour = str(hours)+current_hour[2:]
    if minutes:
        $ current_hour = str(current_hour[:3])+str(minutes)
    # if day_week <= 4:
    #     $ morning = True if int(current_hour[:2]) >= 6 and int(current_hour[:2]) < 9 else False
    #     $ day = True if int(current_hour[:2]) >= 9 and int(current_hour[:2]) <= 17 else False
    #     $ evening = True if int(current_hour[:2]) > 17 and int(current_hour[:2]) < 22 else False
    #     $ night = True if int(current_hour[:2]) >= 22 or int(current_hour[:2]) >= 0 and int(current_hour[:2]) < 6 else False
    # elif day_week >= 5:
    #     $ morning = True if int(current_hour[:2]) >= 7 and int(current_hour[:2]) <= 12 else False
    #     $ day = True if int(current_hour[:2]) > 12 and int(current_hour[:2]) <= 19 else False
    #     $ evening = True if int(current_hour[:2]) > 19 and int(current_hour[:2]) <= 23 else False
    #     $ night = True if int(current_hour[:2]) >= 0 and int(current_hour[:2]) < 7 else False
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