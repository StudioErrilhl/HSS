label fs_talk(fst_called=False):
    if fst_called:
        $ fst_called = False
        if fs_mad != 1:
            if fs_si and day_week <= 4 and not fse:
                show jules ahead
                fp "How you doing today?"
                show jules annoyed
                $ text = "Bah. It's a crappy day, and I have to go to school {0}and talk to my teacher. Something about maybe not being allowed to take one of my finals".format('tomorrow ' if int(current_time[:2]) > 15 else '')
                show jules sad
                fs sad "[text]"
                fp "Seriously? That sounds bad"
                show jules annoyed
                fs annoyed "It's an error on their part, not on mine. I've been good all year, done all my work, behaved. But for some reason their system says I've gotten a written warning, and that I've gotten 3 or 4 calls home. I've gotten [fmName.informal] to come with, so she can tell them in person that it's wrong"
                show jules sad
                pause(1)
                show jules crying
                fs crying "It's bloody annoying! I've been good. Done everything, behaved, been nice. Nothing to deserve this, not one single thing! And nobody wants to listen to me, claiming that their system is fail-proof. I hope bringing [fmName.informal] will at least make them look over it again."
                fp "I'm sorry that you have so much trouble. It's probably just a computer-glitch, or something like that. Somebody hit the wrong button for an ID, or something."
                show jules sad
                fs sad "Yeah... Thanks, [fp] {i}She sounds defeated...{/i}"
                fp "Don't let it get you down, [fsName.informal]"
                fp "You'll get it fixed, I'm sure of it!"
                show jules ahead
                fs ahead "I hope so. Thanks, [fp]"
                $ statschangenotify("fs_rel",1)
                $ fse = True
                $ fs_si = False
                $ fs_si_2 = True
                hide jules
                return
            if fs_si_2 and not fse:
                show jules ahead
                fp "How did it go with the issue you had with the school?"
                if persistent.first_playthrough:
                    fs ahead "Oh, it was nothing, really. We talked, and ended up going through all the entries made about me the last year. [fmName.Informal] confirmed she hadn't received any of the notes or calls that were registered in the system, which sort of made my teacher go a little pale, and become a little upset."
                    fp "Who?"
                    fs annoyed "Oh, [se]. She can be a real bitch!"
                    fp "Oh, yeah, I've heard about her..."
                    fs ahead "Anyway. We ended up going to the principal's office, and talked to one of the clerks there, and she was able to look at the records, and figure out that someone had made a boo-boo, registering complaints for another student on me. She couldn't say for sure who'd done it, though, so they were gonna look into it."
                    fp "But you're off the hook?"
                    fs smile "Yeah, all is good now, I'm gonna be allowed to take my exams and everything."
                    fp "{i}Hmm... sounds weird that they would make so many mistakes, all pertaining to [fsName.myformal]. Either they're completely incompetent, or there is something else going on...{/i}"
                    $ fs_si_2 = False
                    $ hacker_1 = True
                    $ statschangenotify('fs_rel',1)
                    hide jules
                else:
                    fs angry "Oh, the damn idiots didn't even wanna listen to me. Or [fmName.informal], for that matter. Just went on about how their system didn't make mistakes."
                    fp "Okay...? So, they're still threathening with disallowing you for your finals?"
                    fs angry "Yeah. Bloody [se] had the audacity to say, to my face, that if I wasn't causing so much trouble, she wouldn't need to make such a harsh judgement. I think she's getting senile - I haven't even raised my voice in her classroom {b}once{/b}!"
                    fp "Did you have a talk to [scn] or [scm] at the principal's office?"
                    fs annoyed "No. Don't even know who they are, [fp]!"
                    fp "Okay, sorry... they're both on the office staff. They're the ones keeping the books, doing all the grunt-work. They would normally know if anything fishy was going on"
                    "{i}Hm... maybe I can score some points with [fsName.myformal], if I figure this out?{/i}"
                    fp "I can talk to [scn] and see if there's anything she can tell me, if you want?"
                    fs "Really?"
                    fp "Sure, it's no problem. She has a soft-spot for me, so I might be able to get something, at least"
                    fs smile "Oh, that's awesome, [fp]"
                    $ statschangenotify('fs_rel',1)
                    $ fs_si_2 = False
                    $ scs = True
                    hide jules
                $ fse = True
                return
            label school_hacker_talk(sht_called=False):
                if hacker_1 and day_week <= 4 and current_location == 'schoolbuilding_loc':
                    if hacker_first_thought:
                        "{i}You've been thinking about what happened with [fsName.yourformal], and you were almost sure that it wouldn't be possible to manage that many mistakes by accident. Also, they hadn't found out who had updated the records... that's usually registered...{/i}"
                        $ hacker_first_thought = False
                        fp "I should go talk to [scn]. She adores me, and I'm sure I'd be able to get some information out of her!"
                        menu:
                            "Nah, not today, I'll do it tomorrow instead":
                                call evening_home(True) from _call_evening_home
                            "Go talk to [scn], try to find out more about what happened to [fsName.yourformal]":
                                fp "Hi, [scn]!"
                                scn "Hi, [fp] - did you have an appointment today? I don't have anything in the book, it seems? Or did you do something again...? {i}She sounds a bit exasperated{/i}"
                                fp "Nah, [scn] - I just swung by to say hi to the most beautiful woman here! {i}You give [scn] a quick wink{/i}"
                                #show scn blushing #here there should be an image of the clerk blushing
                                "{i}[scn] is blushing a bit{/i}"
                                scn "Oh, you silly boy! You shouldn't flirt with women more than twice your age!\n{i}She's trying to sound scolding, but she's not very successful. Her slight smile gives away that she's mostly pleased with the situation{/i}"
                                fp "{i}Trying to look sad and apologetic{/i}\nOkay, [scn]. I promise I won't do it again!"
                                scn "..."
                                fp "Ah, who am I kidding! I'm definitely gonna be doing it again!"
                                "{i}[scn] looks pleased, although she's still blushing slightly{/i}"
                                fp "Oh, and I wanted to ask you about something. I know you're not supposed to talk about other students, but it's about [fsName.myformal]. She was in here the other day, about some issues with her getting written up and such, and I just thought what she told me after the meeting sounded... a bit weird."
                                scn "Yeah, I remember. I'm not really supposed to say anything, but... The whole thing is a bit embarrassing, to be honest"
                                fp "Oh?"
                                scn "Yeah... {i}She lowers her voice, obviously not wanting to be overheard{/i}\nYou see, it seems that none of the teachers have been making the changes, writing her up. Nothing in the system logs shows any real logins when the changes were made"
                                fp "Oh... kay? So, none of the teachers, huh? Wait... does that mean...\n{i}You lower your voice{/i}\nSomebody hacked the school system?"
                                scn "Yeah... probably. We dunno yet. Something is wrong, at least. Could be there is a system issue, but we haven't gotten word back from LRG yet"
                                fp "LRG?"
                                scn "Oh, yeah, they're the ones who've developed the system"
                                fp "Thanks, [scn]. I know you're breaking some rules by telling me. {i}You lean across the counter and kisses her forehead{/i}"
                                scn "[fp]!\n{i}She looks around{/i}\n Don't do that, please? I could get in trouble"
                                fp "Sorry, [scn]. I didn't think. Still grateful, though!"
                                # scn smiles
                                # scene change to outside school?
                                call schoolbuilding_scene from _call_schoolbuilding_scene_2
                                fp "{i}So, there {b}is{/b} a chance someone did this on purpose - or, maybe even just by accident, messing with the internal systems. Damn, I wish I was a computer geek... No idea how this could be done. I need to talk to [nr]. If he doesn't know, I'm sure he'll know someone who does.{/i}"
                                $ hacker_1 = False
                                $ hacker_2 = True
                                return
            if hacker_2 and not fse:
                show jules ahead with dissolve
                fp "How you doing today?"
                fs sad "Okay, I guess. A bit worried about finals"
                fp "Well, at least you get to take them!"
                fs ahead "Oh, shut it. You know I didn't do anything wrong!"
                fp "I know, I know! But unless you had gotten in their face about it, it would've probably not ended well, and you might have had to take summer-school or something to make it up"
                fs ahead "Yeah. That would have totally sucked!"
                fp "Well, I'm glad that all you have to worry about now is your exams"
                show jules smile with dissolve
                fs smile "You can't help it, can you. Just have to rub it in!"
                fp "You know me, [fsName.informal]! I love rubbing it in!"
                $ statschangenotify("fs_aro",.5,True)
                $ statschangenotify("fs_rel",1)
                $ hacker_2 = False
                $ hacker_3 = True
                $ call_nr = True
                $ fse = True
                hide jules with dissolve
            elif scs_2:
                fp "How you doing today?"
                fs ahead "Oh, I'm good. Got a call from school the other day that they've figured out that I was right. No excuses or anything, just... \"You were right, you can take your exams\". Fuck 'em. But I'm happy I don't have to do summer-school or something like that!"
                fp "Yeah... I went to talk to the clerks. They know me. Got [clerk_talked_to] to look it over. Guess she found something"
                $ fse = True
                $ statschangenotify('fs_rel',1)

        else:
            if firstday_talk and not fse:
                show fp_pm_fs_after_intro_talk_closeup with Dissolve(.25)
                fp "Hi, [fsName.informal]. Can we talk?"
                hide fp_pm_fs_after_intro_talk_closeup
                show fp_pm_fs_after_intro_talk_fs_angry
                with Dissolve(.25)
                fs angry "{b}Fuck you!{/b}"
                fp "Look, I'm really sorry about this morning! I didn't mean to perv on you, [fsName.informal]."
                fs angry "So, you just happened to be leaning against my door because...?"
                fp "Well, that bit is true, but I was just trying to figure out what the sounds coming from your bedroom was. Honestly!"
                hide fp_pm_fs_after_intro_talk_fs_angry
                show fp_pm_fs_after_intro_talk_fs_annoyed
                with Dissolve(.25)
                fs annoyed "So... you heard noises coming from my bedroom, and your first instinct is \"Let's check out the sounds from [fsName.myformal]s bedroom\"?"
                fp "Yeah...\n{b}you muster a foolish grin{/b}\nWhen you put it like that, it sounds sort of stupid..."
                hide fp_pm_fs_after_intro_talk_fs_annoyed
                show fp_pm_fs_after_intro_talk_fs_less_annoyed
                with Dissolve(.25)
                fs ahead "Can we just agree that unless I'm screaming bloody murder... and even if I am, {i}check first!{/i}, that you do not go creeping about my door?"
                fp "Sure, [fsName.informal]. I am really sorry!"
                # fs ahead closed "Yeah, yeah... not as sorry as me..."
                fs ahead "Yeah, yeah... not as sorry as me..."
                fp "Huh?"
                hide fp_pm_fs_after_intro_talk_fs_less_annoyed
                show fp_pm_fs_after_intro_talk_fs_relaxed
                with Dissolve(.25)
                fs ahead "Your timing was beyond belief bad!"
                fp "Uhh... yeah, I get that... I stumbled in on you almost bare naked..."
                hide fp_pm_fs_after_intro_talk_fs_relaxed
                show fp_pm_fs_after_intro_talk_fs_blushing
                with Dissolve(.25)
                fs blushing "No, you idiot. I was about 5 seconds away from an awesome orgasm. Let's just say you ruined the mood."
                fp "{i}Oh, shit...\nDid she actually just say that?{/i}\nI'm really sorry? Look, I owe you one, okay. If you need anything, a ride, drinks, anything, just ask, okay?"
                hide fp_pm_fs_after_intro_talk_fs_blushing
                show fp_pm_fs_after_intro_talk_fs_relaxed
                with Dissolve(.25)
                fs smile "{b}Smiling now...{/b}\nOh, don't you worry. I will ask. You bet on it!"
                hide fp_pm_fs_after_intro_talk_fs_relaxed
                show fp_pm_fs_after_intro_talk_fs_half_turn
                with Dissolve(.25)
                fs smile "So, while you're there, how about you make yourself useful?"
                fp "Useful?"
                hide fp_pm_fs_after_intro_talk_fs_half_turn
                show fp_pm_fs_after_intro_talk_fs_full_turn_pan at diagonal_pan_up
                with Dissolve(.25)
                $ renpy.pause(6)
                fs smile "Yeah, how about you pick up that bottle of sunscreen, and put some on my back?"
                fp "Uhm... sure?"
                fs "Cool!"
                hide fp_pm_fs_after_intro_talk_fs_full_turn_pan
                show fp_pm_fs_after_intro_talk_fs_full_turn
                with Dissolve(.25)
                label put_on_sunscreen_back:
                    if first_sunscreen:
                        $ sunscreen_text = "So, you should put on some sunscreen - where to start?"
                    else:
                        $ sunscreen_text = "So, more sunscreen to put on - where to go from here?"
                menu:
                    # "So, you should put on some sunscreen - where to start?"
                    "[sunscreen_text]"
                    "Turn over":
                        fs "You wanna do the other side too?"
                        jump turned_over_intro
                    "Shoulders" if 'shoulders' not in i_s['pos_back']: # first / second
                        $ first_sunscreen = False
                        hide fp_pm_fs_after_intro_talk_fs_full_turn
                        hide fp_pm_fs_after_intro_talk_fs_butt_closeup_with_buttplug
                        hide fp_pm_fs_after_intro_talk_fs_back_closeup
                        hide fp_pm_fs_after_intro_talk_fs_legs_closeup
                        hide fp_pm_fs_after_intro_talk_fs_feet_closeup
                        hide fp_pm_fs_after_intro_talk_fs_shoulders_closeup
                        show fp_pm_fs_after_intro_talk_fs_shoulders_closeup
                        with Dissolve(.25)
                        if 'shoulders' not in i_s['pos_back']:
                            $ total_fs_sunscreen_points += 1
                            if not i_s['pos_back']:
                                "[fs] seems to like the shoulder-rub - maybe you can go a little further south?"
                            else:
                                "Time to do something else"
                            $ i_s['pos_back'].append('shoulders')
                        else:
                            "Time to do something else"
                        if -10 > total_fs_sunscreen_points < 0:
                            jump end_of_sunscreen_intro
                        elif total_fs_sunscreen_points > 0:
                            jump put_on_sunscreen_back
                        else:
                            jump turned_over_intro
                    "Legs" if 'legs' not in i_s['pos_back']: # third
                        $ first_sunscreen = False
                        hide fp_pm_fs_after_intro_talk_fs_full_turn
                        hide fp_pm_fs_after_intro_talk_fs_butt_closeup_with_buttplug
                        hide fp_pm_fs_after_intro_talk_fs_back_closeup
                        hide fp_pm_fs_after_intro_talk_fs_legs_closeup
                        hide fp_pm_fs_after_intro_talk_fs_feet_closeup
                        hide fp_pm_fs_after_intro_talk_fs_shoulders_closeup
                        show fp_pm_fs_after_intro_talk_fs_legs_closeup
                        with Dissolve(.25)
                        if 'legs' not in i_s['pos_back']:
                            if all(elem in i_s['pos_back'] for elem in ['shoulders']):
                                $ total_fs_sunscreen_points += 1
                                "[fsName.Yourformal] definitely likes you rubbing her legs. There are small cooing noises coming every few seconds"
                            else:
                                $ total_fs_sunscreen_points -= 1
                                "You have a feeling [fsName.yourformal] didn't really like that"
                            $ i_s['pos_back'].append('legs')
                        if -10 > total_fs_sunscreen_points < 0:
                            jump end_of_sunscreen_intro
                        elif total_fs_sunscreen_points > 0:
                            jump put_on_sunscreen_back
                        else:
                            jump turned_over_intro
                    "Feet" if 'feet' not in i_s['pos_back']: # fourth
                        $ first_sunscreen = False
                        hide fp_pm_fs_after_intro_talk_fs_full_turn
                        hide fp_pm_fs_after_intro_talk_fs_butt_closeup_with_buttplug
                        hide fp_pm_fs_after_intro_talk_fs_back_closeup
                        hide fp_pm_fs_after_intro_talk_fs_legs_closeup
                        hide fp_pm_fs_after_intro_talk_fs_feet_closeup
                        hide fp_pm_fs_after_intro_talk_fs_shoulders_closeup
                        show fp_pm_fs_after_intro_talk_fs_feet_closeup
                        with Dissolve(.25)
                        if 'feet' not in i_s['pos_back']:
                            if all(elem in i_s['pos_back'] for elem in ['legs','shoulders']):
                                $ total_fs_sunscreen_points += 1
                                "Rubbing her feet, you hear sighs of pleasure coming from [fs]"
                            else:
                                $ total_fs_sunscreen_points -= 1
                                "You end up tickling her feet more than massaging them - not very popular"
                            $ i_s['pos_back'].append('feet')
                        if -10 > total_fs_sunscreen_points < 0:
                            jump end_of_sunscreen_intro
                        elif total_fs_sunscreen_points > 0:
                            jump put_on_sunscreen_back
                        else:
                            jump turned_over_intro
                    "Butt" if 'butt' not in i_s['pos_back'] or 'butt_2' not in i_s['pos_back']: # fifth and seventh
                        $ first_sunscreen = False
                        hide fp_pm_fs_after_intro_talk_fs_full_turn
                        hide fp_pm_fs_after_intro_talk_fs_butt_closeup_with_buttplug
                        hide fp_pm_fs_after_intro_talk_fs_back_closeup
                        hide fp_pm_fs_after_intro_talk_fs_legs_closeup
                        hide fp_pm_fs_after_intro_talk_fs_feet_closeup
                        hide fp_pm_fs_after_intro_talk_fs_shoulders_closeup
                        if persistent.prefanal:
                            show fp_pm_fs_after_intro_talk_fs_butt_closeup_with_buttplug
                        else:
                            show fp_pm_fs_after_intro_talk_fs_butt_closeup_no_buttplug
                        with Dissolve(.25)
                        if 'butt' not in i_s['pos_back']:
                            if all(elem in i_s['pos_back'] for elem in ['shoulders','legs','feet']):
                                $ total_fs_sunscreen_points += 1
                                "[fsName.Yourformal] moans slightly, obviously liking what you're doing..."
                                if persistent.prefanal:
                                    "Wait... is that... no, you must be seeing things"
                            else:
                                $ total_fs_sunscreen_points = -5
                                fs "Hey! What the hell are you doing? Don't touch me there!"
                            $ i_s['pos_back'].append('butt')
                        elif 'butt' in i_s['pos_back']:
                            if all(elem in i_s['pos_back'] for elem in ['shoulders','legs','feet','butt','back']):
                                if total_fs_sunscreen_points < 3:
                                    "Stop doing that, please"
                                    $ total_fs_sunscreen_points -= 1
                                elif total_fs_sunscreen_points < 5:
                                    "You're not getting much of a response, but at least she's not yelling at you"
                                else:
                                    "The moaning gets louder, as you rub the sunscreen into her butt"
                                    $ total_fs_sunscreen_points += 1
                            else:
                                "[fp]! I told you to stay the fuck away from my ass!"
                                "Fuck off!"
                                $ total_fs_sunscreen_points = -10
                            $ i_s['pos_back'].append('butt_2')
                        if -10 > total_fs_sunscreen_points < 0:
                            jump end_of_sunscreen_intro
                        elif total_fs_sunscreen_points > 0:
                            jump put_on_sunscreen_back
                        else:
                            jump turned_over_intro
                    "Back" if 'back' not in i_s['pos_back']: #sixth
                        $ first_sunscreen = False
                        hide fp_pm_fs_after_intro_talk_fs_full_turn
                        hide fp_pm_fs_after_intro_talk_fs_butt_closeup_with_buttplug
                        hide fp_pm_fs_after_intro_talk_fs_back_closeup
                        hide fp_pm_fs_after_intro_talk_fs_legs_closeup
                        hide fp_pm_fs_after_intro_talk_fs_feet_closeup
                        hide fp_pm_fs_after_intro_talk_fs_shoulders_closeup
                        show fp_pm_fs_after_intro_talk_fs_back_closeup
                        with Dissolve(.25)
                        if 'back' not in i_s['pos_back']:
                            $ i_s['pos_back'].append('back')
                            if all(elem in i_s['pos_back'] for elem in ['shoulders','legs','feet','butt']):
                                fp "..."
                                if persistent.prefanal:
                                    menu:
                                        "Mention buttplug":
                                            fp "Uhm, [fsName.informal]..."
                                            fs "Yeah?"
                                            fp "Are you using a... buttplug?"
                                            fs "You noticed, huh?"
                                            fp "Yeah..."
                                            "You feel yourself getting rock hard. Nothing you can do about that, really..."
                                            $ statschangenotify('fs_aro',1,True)
                                            $ statschangenotify('fs_anal',1)
                                            $ total_fs_sunscreen_points += 1
                                        "Dont mention it":
                                            fp "So, this okay?"
                                            fs "Yup, it's great!"
                                            $ i_s['pos_back'].append('butt_2')
                                else:
                                    fp "So, this okay?"
                                    fs "Yup, it's great"
                                    # $ i_s['pos_back'].append('butt_2')
                                    $ total_fs_sunscreen_points += 1
                            elif total_fs_sunscreen_points >= 4:
                                "[fsName.Yourformal] sighs, content, while you work the sunscreen into her back"
                                $ total_fs_sunscreen_points += 1
                            elif any(elem in ['shoulders','arms','legs','feet'] for elem in i_s['pos_back']):
                                "[fsName.Yourformal] isn't protesting, but you get the message that you could have done better"
                                $ total_fs_sunscreen_points -= 1
                            else:
                                "[fsName.Yourformal] looks at you, clearly not entirely happy with your ministrations"
                                $ total_fs_sunscreen_points -= 1
                        if -10 > total_fs_sunscreen_points < 0:
                            jump end_of_sunscreen_intro
                        elif total_fs_sunscreen_points > 0:
                            jump put_on_sunscreen_back
                        else:
                            jump turned_over_intro
                $ addtime(False, 30)
                label turned_over_intro:
                if total_fs_sunscreen_points <= 0:
                    fs annoyed "You {b}ARE{/b} a perv! Go away!"
                    fp "Okay..."
                    fs "NOW!"
                    jump end_of_sunscreen_intro
                elif total_fs_sunscreen_points < 5:
                    fs ahead "Nah, we're good. Now go away, you're blocking my sun!"
                    fp "Okay, see you later"
                    jump end_of_sunscreen_intro
                elif total_fs_sunscreen_points <= 6:
                    show fp_pm_fs_after_intro_talk_fs_half_turn
                    $ renpy.pause(.35)
                    hide fp_pm_fs_after_intro_talk_fs_half_turn
                    show fp_pm_fs_after_intro_talk_fs_front_full_pan at diagonal_pan_down
                    with Dissolve(.25)
                    $ renpy.pause(6)
                    show fp_pm_fs_after_intro_talk_fs_front_full
                    with Dissolve(.25)
                    fs smile "So, do the front as well"
                    jump put_on_sunscreen_front
                else:
                    menu put_on_sunscreen_front:
                        "So... applying sunscreen up front..."
                        "Stomach" if 'stomach' not in i_s['pos_front']:
                            hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                            show fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                            with Dissolve(.25)
                            if 'stomach' not in i_s['pos_front']:
                                $ total_fs_sunscreen_points += 1
                            if all(elem in i_s['pos_front'] for elem in ['shoulders','legs','feet']):
                                fs "Oh, that feels nice..."
                            else:
                                "Time to lotion up something else"
                            $ i_s['pos_front'].append('stomach')
                            if all(elem in i_s['pos_front'] for elem in ['shoulders','stomach','legs','feet','breast']):
                                jump end_of_sunscreen_intro
                            elif -10 > total_fs_sunscreen_points <= 0:
                                jump end_of_sunscreen_intro
                            else:
                                jump put_on_sunscreen_front
                        "Shoulders" if 'shoulders' not in i_s['pos_front']: # first / second:
                            hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                            show fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                            with Dissolve(.25)
                            if 'shoulders' not in i_s['pos_front']:
                                $ total_fs_sunscreen_points += 1
                            if not i_s['pos_front']:
                                "[fs] seems to like the shoulder-rub - maybe you can go a little further south"
                            else:
                                "Time to do something else"
                            $ i_s['pos_front'].append('shoulders')
                            if all(elem in i_s['pos_front'] for elem in ['shoulders','stomach','legs','feet','breast']):
                                jump end_of_sunscreen_intro
                            elif -10 > total_fs_sunscreen_points <= 0:
                                jump end_of_sunscreen_intro
                            else:
                                jump put_on_sunscreen_front
                        "Legs" if 'legs' not in i_s['pos_front']:
                            hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                            show fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                            with Dissolve(.25)
                            if 'legs' not in i_s['pos_front']:
                                $ total_fs_sunscreen_points += 1
                            if all(elem in i_s['pos_front'] for elem in ['shoulders']):
                                "[fs] purrs content when you do her legs"
                            else:
                                "[fs] isn't quite happy with your work"
                            $ i_s['pos_front'].append('legs')
                            if all(elem in i_s['pos_front'] for elem in ['shoulders','stomach','legs','feet','breast']):
                                jump end_of_sunscreen_intro
                            elif -10 > total_fs_sunscreen_points <= 0:
                                jump end_of_sunscreen_intro
                            else:
                                jump put_on_sunscreen_front
                        "Feet" if 'feet' not in i_s['pos_front']:
                            hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                            show fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                            with Dissolve(.25)
                            if 'feet' not in i_s['pos_front']:
                                $ total_fs_sunscreen_points += 1
                            if all(elem in i_s['pos_front'] for elem in ['shoulders','legs']):
                                "You carefully massage the lotion into the top of her feet"
                            else:
                                fs "Hey, that tickles!"
                            $ i_s['pos_front'].append('feet')
                            if all(elem in i_s['pos_front'] for elem in ['shoulders','stomach','legs','feet','breast']):
                                jump end_of_sunscreen_intro
                            elif -10 > total_fs_sunscreen_points <= 0:
                                jump end_of_sunscreen_intro
                            else:
                                jump put_on_sunscreen_front
                        "Breasts" if 'breast' not in i_s['pos_front']:
                            if all(elem in i_s['pos_front'] for elem in ['shoulders','stomach','legs','feet']):
                                hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                                hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                                hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                                hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                                hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                                # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                                hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                                hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                                hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                                # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                                show fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                                with Dissolve(.25)
                            if not i_s['pos_front']:
                                $ total_fs_sunscreen_points = -10
                                fs "HEY! Don't go grabbing my boobs!"
                            elif all(elem in i_s['pos_front'] for elem in ['shoulders','stomach','legs','feet']):
                                menu:
                                    "Ask her to take off her top":
                                        if total_fs_sunscreen_points >= 10:
                                            $ total_fs_sunscreen_points += 1
                                            fs "... okay... {i}She's blushing... that's kinda cute{/i}"
                                            hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                                            show fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan at vertical_pan_from_bottom
                                            with Dissolve(.25)
                                            $ renpy.pause(4)
                                            hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                                            show fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                                            with Dissolve(.25)
                                            fp "Wow! You got beautiful boobs, [fsName.informal]!"
                                            hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                                            show fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                                            with Dissolve(.25)
                                            fs "Thanks... now... sunscreen?"
                                            fp "Oh, yeah, sorry!"
                                            show fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_boobs
                                            with Dissolve(.25)
                                            "You start rubbing the sunscreen on her breasts"
                                            fs "That... feels... nice {i}She moans under her breath, trying to keep it inaudible... and failing{/i}"
                                            "You finish rubbing her boobs, and just sit there for a little while..."
                                            fs "If you're done, you can move, you know..."
                                            # fp blushing "Yeah... uhm... trying to not embarrass myself here!"
                                            fp "Yeah... uhm... trying to not embarrass myself here!"
                                            "[fs] looks down, turning a shade of red again"
                                            fs "Oh!"
                                            fp "Yeah... but, fine, I'm gonna get off you now. And... go someplace else!"
                                        else:
                                            fs "No! You're not getting to see my boobs, you perv!"
                                            $ total_fs_sunscreen_points -5
                                        jump end_of_sunscreen_intro
                                    "Don't ask about her top":
                                        if total_fs_sunscreen_points >= 10:
                                            hide fp_pm_fs_after_intro_talk_fs_front_shoulders_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_legs_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_feet_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_stomach_closeup
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup
                                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_pan
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_unsure
                                            hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_remove_bra_face_smile
                                            # hide fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                                            # show fp_pm_fs_after_intro_talk_fs_front_breast_closeup_disappointed
                                            with Dissolve(.25)
                                            "She seems a bit... disappointed. Wonder what that was all about?"
                                        else:
                                            "You finish applying the sunscreen"
                                        jump end_of_sunscreen_intro
                            else:
                                "Well, that was that, then"
                            $ i_s['pos_front'].append('breast')
                            if all(elem in i_s['pos_front'] for elem in ['shoulders','stomach','legs','feet','breast']):
                                jump end_of_sunscreen_intro
                            elif -10 > total_fs_sunscreen_points <= 0:
                                jump end_of_sunscreen_intro
                            else:
                                jump put_on_sunscreen_front

                label end_of_sunscreen_intro:
                $ fse = True
                if total_fs_sunscreen_points > 0:
                    $ statschangenotify("fs_rel",total_fs_sunscreen_points,True)
                else:
                    $ statschangenotify("fs_rel",3,True)
                $ firstday_talk = False
                $ firstday_after_talk = True
                $ addtime(1,False,True,sec_call='after_talk_events')
                label after_talk_events(ate_called=False):
                    if ate_called:
                        $ ate_called = False
                        if fs_mad == 1:
                            $ fs_mad = 0
                            $ morning_event_done = True
                            $ fdtfs_after = False
                            if int(current_time[:2]) in night:
                                call end_of_day(True) from _call_end_of_day
                        else:
                            $ morning_event_done = True
                            $ fdtfs_after = False
                            if int(current_time[:2]) in night:
                                call end_of_day(True) from _call_end_of_day_1
            # elif day_week <= 4:
            #     if int(current_time[:2]) > 17:
            #         $ settime(22,False,True,'fs_where')
            #         label fs_where(fsw_called=False):
            #             if fsw_called:
            #                 fp "{i}Hmm... where did my damn [fsName.role] go?{/i}"
            #                 fp "{i}Oh, well. I'll find her tomorrow. Time for bed{/i}"
            #         call change_loc('fp_bedroom_fp') from _call_change_loc
            #     else:
            #         call change_loc(current_location) from _call_change_loc_1
            # else:
            #     $ settime(22,False,True,'fs_where')

