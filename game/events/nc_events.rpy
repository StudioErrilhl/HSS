label nc_talk(event=False,callrand=False):
    if event == 'first_talk' and not nce:
        if callrand:
            if callrand > .35 and not nc_after_ft:
                nc "Hello?"
                fp "Hi. Dunno if you remember me..."
                nc "I remember you, [fp]!"
                "You can sense... not hostility... just... sceptisism? in her voice"
                fp "Even remember my name..."
                nc "Don't flatter yourself! Caller ID! Ever heard of it?"
                fp "Right..."
                nc "Dumbass"
                fp "Well, perhaps. I didn't call you out of the blue, though"
                nc "I'm sure you didn't. I don't really give a shit!"
                fp "I..."
                $ calling = duringcall = False
                "{b}beeeeeep...{/b}"
                fp "{i}She hung up on me! The bitch... hung up on me!{/i}"
                menu:
                    "What a bitch, huh?" (cs="evil"):
                        # $ fp_alignment -= 1
                        $ statschangenotify('lil_bad',1,True)
                        $ statschangenotify('fp_alignment',-1)
                    "What a... oh, well, I guess she had her reasons" (cs="good"):
                        # $ fp_alignment += 1
                        $ statschangenotify('aro_good',1,True)
                        $ statschangenotify('fp_alignment',1)
                fp "{i}Okay... not the best start. Maybe I can figure out a way to get her to talk to me, at least...{/i}"
                $ nc_after_ft = True
                if "You need to figure out a way to get "+nc.name+" to talk to you. Perhaps talk to "+nr.name+" again, see if he can give you a few pointers" not in hints+read_hints+disabled_hints:
                    $ renpy.notify("You need to find a way to get "+nc.name+" to talk to you")
                    $ set_hint("You need to figure out a way to get "+nc.name+" to talk to you. Perhaps talk to "+nr.name+" again, see if he can give you a few pointers")
            else:
                $ calling = duringcall = False
                if nc_after_ft:
                    fp "No answer. No surprise there, after what she did when I called the first time..."
                else:
                    fp "No answer. I guess I'll have to try again later"
            $ nce = True
        call change_loc(current_location,prev_loc=current_location) from _call_change_loc_25

    if event == 'icafe_visit':
        $ settime(20,00)
        if visit_icafe_1:
            $ addtime(False,30)
            "You arrive at [icafe]. Looking around, trying to let your eyes adjust to the dimly lit location, with glowing screens across the interior. Not the easiest place to find someone..."
            "Scanning the room, you try to spot [nc] in the crowd. Not that many girls in here, that you can see, but then half the crowd is wearing hoodies and headphones, making it hard to pinpoint gender"
            "Suddenly, you hear yelling from the far side of the cafe"
            unk_f "{b}Hell to the FUCK no!{/b}"
            unk_m "... uuhhh..."
            unk_f "{b}Shut the FUCK UP!{/b}"
            unk_m "I'm sorry...!"
            unk_f "{b}You better be sorry, you little idiot! You're a fucking moron!{/b}"
            "You start heading for the commotion... knowing [nc], this... sorta sounds like her, even though you cannot really remember her voice"
            "When you approach them, they seem to at least have turned down the volume a little bit, but the tension is still palpable"
            "You hang back, trying to figure out if this is both something you want to get involved in, and also if this is even the girl you're looking for"
            "The girl rips off her headphones and throws them on the table, before turning back to the much younger kid standing in front of her"
            unk_f "{b}How the fuck can you manage to be this fucking clumsy, you idiot?{/b}"
            "You can see a laptop on the table, no lights or anything... and then you spot the Jolt-cup... oooooh, you get the anger now. That laptop looks like something in the $2000+ range"
            unk_m "I'm sorry, [nc]! I will get it fixed, I promise..."
            "{b}Score!{/b} You found her!"
            nc "The fuck you will. How the fuck are you gonna afford to fix this? And I'm not letting you anywhere near my laptop, you pathetic piece of shit"
            unk_m "Look, I'm sorry, and if I can do anything to help..."
            nc "Help? What would help is if you watched where you were going, and stopped running around with damn accident waiting to happen... {b}she points to the spilt Jolt{/b}. There's a reason why the rest of us have capped bottles when we are here, you dimwit."
            unk_m "Well, I can ask my brother to help fix it, he's..."
            nc "{i}Ice cold voice now{/i} Your brother, huh? I know who your brother is! And no way in hell am I letting him near my laptop. You can tell him that he'll need to figure out some better if he wants to get a hold of my drives. Not that they would do him any good anyway, they're encrypted. But of course, the moron didn't think that far. Now scram!"
            "She takes a step towards the boy, who couldn't be more than 14, and he steps back, turns and hurries away"
            "In the meantime, [nc] looks like she wants to kill someone, and you decide that you really don't wanna be that guy. You decide to come back and talk to her when she's in a slighlty less confrontational mood"
            $ visit_icafe_1 = False
            $ visit_icafe_2 = True
            $ addtime(False,20)
        else:
            fp "I should call [nr] and see if he knows where I might find [nc]..."
        $ nce = True
        call change_loc(current_location,prev_loc=current_location) from _call_change_loc_55

    if event == 'icafe_talk' and not nce:
        $ addtime(False, 30)
        "You decide to go try to get a hold of [nc]. Hopefully she's calmed down after the accident with her laptop"
        "Arriving at [icafe], slightly earlier in the day this time around, you head to the back, to see if you can find [nc] anywhere"
        fp "{i}There she is...{/i}"
        fp "Hey, [nc]!"
        "She looks a bit startled. If it's just that you suddenly show up, or that you know her name, is up for grabs"
        nc "[fp]... You should really learn to take a hint!"
        fp "Oh, well, I just couldn't stay away! And I figured you were just having a bad day!"
        nc "You figured wrong!"
        fp "Did you get your laptop fixed?"
        nc "My... laptop...? How the fuck did you know my laptop got fried?"
        fp "Well, I was in here looking for you the other day... Found you too, but decided against talking to you. Seemed you were a bit... cross, with whomever the idiot was who spilled on your box"
        nc "Yeah... don't say it like that"
        fp "Huh? Oh, right! \"Your laptop\". Better?"
        nc "Slightly. What do you want?"
        fp "Would you believe me if I said I just wanted to see how you were doing?"
        nc "No, I would not"
        fp "Fine. I need someone with a little bit of knowledge about computer systems and hacking"
        nc "Do you now. And exactly for what purpose do you need this knowledge? {i}The mirth in her voice is not really endearing...{/i}"
        fp "That is a matter of some complexity, so it would take a bit of explaining. I'm willing to pay, of course. Seems like you could use a new computer?"
        nc "Hm. How much?"
        fp "How much do you need?"
        nc "For a new laptop?"
        fp "Yeah"
        nc "A couple grand should do it"
        $ nc_owed = 2000
        if fp_money > 2000:
            fp "No problem"
            "[nc] looks a little perplexed with your seeming indifference to the amount she asked for"
            nc "O... kay. Money up front, then tell me what you need"
            $ fp_money -= nc_owed
            $ nc_owed = 0
            $ visit_icafe_2 = False
            $ visit_icafe_3 = True
            call nc_talk(event='icafe_talk_after_payment') from _call_nc_talk
        else:
            fp "I can't afford that right now"
            nc "Then get back to me when you can"
            "She gets up, and leave you sitting there, a little taken aback by her straight forwardness and boldness"
            fp "{i}2 grand. Holy fuck... Where the fuck am I gonna get 2 grand?{/i}"
            $ parsedjobs = ", ".join(fp_jobs)
            $ set_hint("You can earn money via different methods - currently you can do "+parsedjobs+"")
            $ nc_owed = 2000
            $ visit_icafe_2 = False
            $ visit_icafe_3 = True
        $ addtime(False,30)
        $ nce = True

    if event == 'icafe_talk_after_payment' and not nce:
        if nc_owed <= 2000 and nc_owed != 0:
            $ nctext = "So, "+str(fp)+"... {0}".format("you got the rest of my cash?" if nc_payment_made else "you got my cash?")
            nc "[nctext]"
            if fp_money > nc_owed:
                fp "Yeah, I do..."
                $ tmp_nc_owed = nc_owed-(max(nc_owed-fp_money,0))
            else:
                fp "Well, I got some of it..."
                $ tmp_nc_owed = nc_owed-(max(nc_owed-fp_money,0))
                $ nc_payment_made = True
            label give_nc_money():
                menu:
                    "Give [nc] the $[tmp_nc_owed]":
                        $ fp_money -= tmp_nc_owed
                        $ nc_owed -= tmp_nc_owed
                        jump after_money_exchange
                    "How much do you want to give?":
                        python:
                            try:
                                give_cash = int(renpy.input("Input the amount you want to give"))
                                if not isinstance(give_cash,int):
                                    raise ValueError()
                            except ValueError:
                                renpy.say(None,"Please input only numbers")
                                renpy.jump('give_nc_money')
                            else:
                                if fp_money > int(give_cash):
                                    fp_money -= int(give_cash)
                                    nc_owed -= int(give_cash)
                                    renpy.jump('after_money_exchange')
                                else:
                                    "You don't have that much money"
                                    renpy.jump('give_nc_money')
        else:
            label after_money_exchange():
                if not nc_owed:
                    nc "Nice... I should've asked for more"
                    fp "No, you really shouldn't - I don't mind paying, but I won't be taken advantage of!"
                    "She looks at you for a short while, trying to discern your motives, perhaps?"
                    fp "So... about what I asked you"
                    nc "Yeah... you think someone hacked the school. So, why do you think that?"
                    fp "{i}This was a bad idea...{/i}"
                    fp "I don't know computers, or the systems, but word from employees at the school is that there are things happening with the school systems that would mean that there is either a hacker somewhere, modifying records and abusing the system, or the system is just so fucked that it messes with records without leaving traces"
                    nc "Hmm... did he mess with you?"
                    fp "What? No! And we're assuming it's a he, are we?"
                    nc "Yeah, we are. No reason, but most hackers are guys. And if not you, why do you care?"
                    fp "Because... he messed with [fsName.shortname], okay?"
                    nc "Jules... oh, [fsName.yourformal]"
                    fp "Yeah..."
                    nc "Hm, okay. So you're suddenly her knight in shining armor?"
                    fp "Uh? Noone messes with [fsName.myformal]"
                    nc "Fine. What do you want me to do about it?"
                    fp "Well... I would like for you to check out the system. Maybe you can find something, or at least figure out if it's just the system being crappy, or if someone is actually messing with it"
                    nc "I can probably do that... I'm guessing this isn't sanctioned by the school, hm?"
                    fp "Haha. You're funny. The school just wanna sweep this under the rug"
                    nc "Okay, I'm gonna need a bit of time to set this up. Gimme a week or so. I'll contact you via text"
                    $ nc_action_started = 1
                    $ visit_icafe_3 = False
                    $ addtime(1)
                else:
                    nc "You still owe me $[nc_owed]"
                    fp "I know. I was hoping you could perhaps start, and I will get the rest of the..."
                    nc "No!"
                    nc "You need my help, not the other way around. You pay me, up front, and I help. Until that happens, no help"
                    fp "Fine..."
                    $ addtime(False,30)
        $ nce = True

        call change_loc(current_location,prev_loc=current_location) from _call_change_loc_68

    if event == 'icafe_talk_7_days' and not nce:
        fp "{i}Now, where is she...{/i}"
        nc "Hey, [fp]!"
        "She caught you off guard, and you catch yourself jumping a little bit. Maybe she didn't notice"
        fp "Uhm... eh... heyu..."
        "Or not..."
        nc "You scare easily"
        "You can hear the grin even though you can't really see her face in the dark cafe"
        fp "Yeah, well... fine, you scared me. You're a scary chick, okay?"
        "[nc] looks a bit taken aback by that statement"
        nc "Well, at least you showed up. I've figured out a couple things, although nothing really conclusive"
        fp "What you got?"
        nc "I did run a few checks on the systems. They're secured with gaffa and safety pins, it'll take the average script kiddie about 2 minutes to get access"
        fp "So what you're saying anyone could've done this?"
        nc "Nah, you didn't let me finish. Access is easy. Getting away with what this guy did, however, isn't quite as straight forward. Mostly, the system is fairly automated, especially the logs of who does what. Without proper access, you would trigger between 3 and 5 fail-safes"
        fp "But... nothing like that showed up?"
        nc "Exactly! That means that this guy knows what he's doing. Which also means that he didn't really leave much of a trace"
        fp "So... I basically wasted $2000 on you, huh?"
        "Again, she looks at you with contempt"
        nc "I didn't fail. I just didn't find out much. Noone else would be able to find more"
        fp "Easy... did you find anything at all, anything that can be of help?"
        nc "Well... there was one thing. I dunno if it's of any use, but the way I think he got a hold of the info he needed to manipulate the system is sort of a signature for [hj]"
        fp "[hj]? You're kidding now, right?"
        nc "No, I'm not. I know the name is dorky as fuck, but the guy is legit one of the best hackers in the wild. Which sort of makes me wonder why the hell he would bother with this. It's way beneath him and his usual bravado, and with no obvious gain"
        fp "Yeah, that was sort of one of the things I was wondering about as well. It didn't seem to serve any purpose at all, apart from messing with students"
        fp "Do you know anything about this guy? Where I might find him, or anything useful to track him down?"
        "She looks away for a bit..."
        nc "No... no, not really"
        fp "Oh, come on. You clearly know {b}something{/b}! Tell me!"
        nc "I don't take orders from you. I don't even think I like you. So don't come here and demand information about my... {i}She cuts herself off, before finishing the sentence{/i}"
        fp "Your... wait. [hj] is your... what? Boyfriend?"
        nc "NO! He's just... "
        "She looks flustered... not embarrassed, just... unsure of what she should tell you, maybe?"
        nc "He's a guy I used to hook up with, okay? Then... shit happened, and we had to stop doing that. It's... sorta weird, and not something I wanna share. Okay?"
        fp "Okay, no problem. I don't really care who you fuck, what I do care about is whether or not I can get a hold of him"
        nc "I can probably get him here..."
        fp "Okay. Have him show up, then text me. I can be here in 30 minutes max!"
        nc "I'll text you when I get a hold of him. No promises though"
        "You head out, going back home seems like a good plan for now"
        $ nc_action_started = 1
        $ hacker_5 = True
        $ nce = True
        call change_loc('fp_outside',prev_loc=current_location) from _call_change_loc_69

    if event == 'nc_text' and hacker_5 and not nce:
        $ hacker_5 = False
        $ set_message('nc',nc,"Hey! I've got him. He agreed to meet me at [icafe] tomorrow, around 23")
        $ hacker_6 = True

    if event == 'nc_meet_hacker' and hacker_6 and (int(current_time[:2]) >= 22 and int(current_time[:2]) <= 23) and not nce:
        $ hacker_6 = False
        "Heading into the darkest, inner corners of [icafe], you scan the surroundings, trying to spot [nc], and more importantly, her friend, before they spot you"
        fp "{i}Hm... can't see them anywhere...{/i}"
        $ settime(23,00)
        "You stay for a few minutes, thinking they might be running late, or just messing with you, for that matter"
        $ addtime(False, 15)
        fp "{i}This isn't like her... telling me to meet her at 23:00 and not showing up... and no message, nothing{/i}"
        fp "{i}Let's send her a message and see if she replies...{/i}"
        $ nc_call_after_hacker = True

    if event == 'nc_call_after_hacker' and nc_call_after_hacker:
         show screen phone_call_show('nc','nc_talk', False, 'nc_call_after_hacker_2')

    if event == 'nc_call_after_hacker_2' and nc_call_after_hacker:
        "this is a test"

    if event == 'icafe_talk_hj' and not nce:
        "This is as far as this story goes for now"

        $ nce = True