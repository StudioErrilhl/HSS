label fs_talk(fst_called=False):
    if fst_called:
        $ fst_called = False
        if not fs_mad:
            if fs_si and day_week <= 4 and not fse:
                show fs_standing ahead
                fp "How you doing today?"
                show fs_standing annoyed
                $ text = "Bah. It's a crappy day, and I have to go to school {0}and talk to my teacher. Something about maybe not being allowed to take one of my finals".format('tomorrow ' if int(current_time[:2]) > 15 else '')
                show fs_standing sad
                fs sad "[text]"
                fp "Seriously? That sounds bad"
                show fs_standing annoyed
                fs annoyed "It's an error on their part, not on mine. I've been good all year, done all my work, behaved. But for some reason their system says I've gotten a written warning, and that I've gotten 3 or 4 calls home. I've gotten [fmName.informal] to come with, so she can tell them in person that it's wrong"
                show fs_standing crying
                fs crying "It's bloody annoying! I've been good. Done everything, behaved, been nice. Nothing to deserve this, not one single thing! And nobody wants to listen to me, claiming that their system is fail-proof. I hope bringing [fmName.informal] will at least make them look over it again."
                fp "I'm sorry that you have so much trouble. It's probably just a computer-glitch, or something like that. Somebody hit the wrong button for an ID, or something."
                show fs_standing sad
                fs sad "Yeah... Thanks, [fp] {i}She sounds defeated...{/i}"
                fp "Don't let it get you down, [fsName.informal]"
                fp "You'll get it fixed, I'm sure of it!"
                show fs_standing ahead
                fs ahead "I hope so. Thanks, [fp]"
                $ statschangenotify("fs_rel",1)
                $ fse = True                
                $ fs_si = False
                $ fs_si_2 = True
                hide fs_standing
                return
            if fs_si_2 and not fse:
                show fs_standing ahead
                fp "How did it go with the issue you had with the school?"
                if p.first_playthrough:
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
                    hide fs_standing
                else:
                    fs mad "Oh, the damn idiots didn't even wanna listen to me. Or [fmName.informal], for that matter. Just went on about how their system didn't make mistakes."
                    fp "Okay...? So, they're still threathening with disallowing you for your finals?"
                    fs mad "Yeah. Bloody [se] had the audacity to say, to my face, that if I wasn't causing so much trouble, she wouldn't need to make such a harsh judgement. I think she's getting senile - I haven't even raised my voice in her classroom {b}once{/b}!"
                    fp "Did you have a talk to [scn] or [scm] at the principal's office?"
                    fs annoyed "No. Don't even know who they are, [fp]!"
                    fp "Okay, sorry... they're both on the office staff. They're the ones keeping the books, doing all the grunt-work. They would normally know if anything fishy was going on"
                    "{i}Hm... maybe I can score some points with [fsName.myformal], if I figure this out?{/i}"
                    $ fs_si_2 = False
                    $ scs = True
                    hide fs_standing
                $ fse = True
                return
            label school_hacker_talk(sht_called=False):
                if hacker_1 and day_week <= 4 and current_location == 'schoolbuilding_loc':
                    if hacker_first_thought:
                        "{i}You've been thinking about what happened with [fsName.yourformal], and you were almost sure that it wouldn't be possible to manage that many mistakes by accident. Also, they hadn't found out who had updated the records... that's usually registered...{/i}"
                        $ hacker_first_thought = False
                        fp "I should go talk to [scn]. She adores me, and I'm sure I'd be able to get some information out of her!"
                        menu:
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
                                fp "{i}So, there {b}is{/b} a chance someone did this on purpose - or, maybe even just by accident, messing with the internal systems. Damn, I wish I was a computer geek... No idea how this could be done. I need to talk to [nr]. If he doesn't know, I'm sure he'll know someone who does.{/i}"
                                $ hacker_1 = False
                                $ hacker_2 = True
                                return
                            "Nah, not today, I'll do it tomorrow instead":
                                call evening_home(True) from _call_evening_home
            if hacker_2 and not fse:
                show fs_standing ahead with dissolve
                fp "How you doing today?"
                fs sad "Okay, I guess. A bit worried about finals"
                fp "Well, at least you get to take them!"
                fs ahead "Oh, shut it. You know I didn't do anything wrong!"
                fp "I know, I know! But unless you had gotten in their face about it, it would've probably not ended well, and you might have had to take summer-school or something to make it up"
                fs ahead "Yeah. That would have totally sucked!"
                fp "Well, I'm glad that all you have to worry about now is your exams"
                show fs_standing smile with dissolve
                fs smile "You can't help it, can you. Just have to rub it in!"
                fp "You know me, [fsName.informal]! I love rubbing it in!"
                $ statschangenotify("fs_aro",.5,True)
                $ statschangenotify("fs_rel",1)
                $ hacker_2 = False
                $ hacker_3 = True
                $ call_nr = True
                $ fse = True
                hide fs_standing with dissolve
            elif scs_2:
                fp "How you doing today?"
                fs ahead "Oh, I'm good. Got a call from school the other day that they've figured out that I was right. No excuses or anything, just... \"You were right, you can take your exams\". Fuck 'em. But I'm happy I don't have to do summer-school or something like that!"
                fp "Yeah... I went to talk to the clerks. They know me. Got [clerk_talked_to] to look it over. Guess she found something"
                $ fse = True                

        else:
            if (firstday_talk or talk_later) and not fse:
                show fs_standing annoyed with dissolve
                if talk_later:
                    if int(current_time[:2]) < 15:
                        $ addtime(5)
                    elif int(current_time[:2]) < 20:
                        $ settime(20)
                else:
                    $ addtime(False,30)
                fp "Hi, [fsName.informal]. Can we talk?"
                show fs_standing mad with dissolve
                fs mad "{b}Fuck you!{/b}"
                show fs_standing ahead with dissolve
                $ text = "Look, I'm really sorry about {0}! I didn't mean to perv on you, {1}.".format("this morning" if first_day else "the other day", fsName.informal )
                fp "[text]"
                show fs_standing mad with dissolve
                fs mad "So, you just happened to be leaning against my door because...?"
                fp "Well, that bit is true, but I was just trying to figure out what the sounds coming from your bedroom was. Honestly!"
                show fs_standing annoyed with dissolve
                fs annoyed "So... you heard noises coming from my bedroom, and your first instinct is \"Let's check out the sounds from [fsName.myformal]s bedroom\"?"
                fp "Yeah...\n{b}you muster a foolish grin{/b}\nWhen you put it like that, it sounds sort of stupid..."
                show fs_standing ahead with dissolve
                $ addtime(False, 30)
                fs ahead "Can we just agree that unless I'm screaming bloody murder... and even if I am, {i}check first!{/i}, that you do not go creeping about my door?"
                fp "Sure, [fsName.informal]. I am really sorry!"
                fs ahead_eyes_closed "Yeah, yeah... not as sorry as me..."
                fp "Huh?"
                show fs_standing ahead with dissolve
                fs ahead "Your timing was beyond belief bad!"
                fp "Uhh... yeah, I get that... I stumbled in on you almost bare naked..."
                show fs_standing blushing with dissolve
                fs blushing "No, you idiot. I was about 5 seconds away from an awesome orgasm. Let's just say you ruined the mood."
                show fs_standing blushing with dissolve
                fp "{i}Oh, shit...\nDid she actually just say that?{/i}\nI'm really sorry? Look, I owe you one, okay. If you need anything, a ride, drinks, anything, just ask, okay?"
                show fs_standing smile_open with dissolve
                fs smile "{b}Smiling now...{/b}\nOh, don't you worry. I will ask. You bet on it!"
                if renpy.get_screen('livingroom'):
                    "With that, she picks herself off the couch, and wanders off"
                else:
                    "With that, she wanders off"
                $ fse = True
                hide fs_standing with dissolve
                $ statschangenotify("fs_rel",3,True)
                $ firstday_talk = False
                $ firstday_after_talk = True
                $ addtime(1,False,True,sec_call='after_talk_events')
                label after_talk_events(ate_called=False):
                    if ate_called:
                        $ ate_called = False
                        if fs_mad:
                            $ fs_mad = False
                            $ morning_event_done = True
                            $ fdtfs_after = False
                            if int(current_time[:2]) in night:
                                call end_of_day(True)
                        else:
                            $ morning_event_done = True
                            $ fdtfs_after = False
                            if int(current_time[:2]) in night:
                                call end_of_day(True)
            elif day_week <= 4:
                if int(current_time[:2]) > 17:
                    $ settime(22,False,True,'fs_where')
                    label fs_where(fsw_called=False):
                        if fsw_called:
                            fp "{i}Hmm... where did my damn [fsName.role] go?{/i}"
                            fp "{i}Oh, well. I'll find her tomorrow. Time for bed{/i}"
                    call change_loc('fp bedroom') from _call_change_loc
                else:
                    call change_loc(current_location) from _call_change_loc_1
            else:
                $ settime(22,False,True,'fs_where')
