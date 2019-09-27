label nr_talk(event=False,callrand=False):
    if event == 'nr_intro' and not nre:
        $ hacker_3 = False
        "You decide to call [nr] to see if he's free to hang out"
        fp "Hey, [nr]"
        nr "Hey [fp]! What's up?"
        fp "Well... I have a couple things to run by you, was wondering if you could drop by? If not tonight, then tomorrow?"
        $ text = "Sure. {0}".format("I can be there around 18" if int(current_time[:2]) < 20 else "It's a bit late, but I can drop by tomorrow? Say around 19:00?")
        nr "[text]"
        fp "Cool. I'll be in the garage, so just meet me there"
        $ text = "Okay. See you {0}".format('soon' if int(current_time[:2]) < 20 else 'tomorrow')
        nr "[text]"
        $ hacker_4 = True
        $ nre = True
        call change_loc(current_location,prev_loc=current_location) from _call_change_loc_27

    if event == 'nr_first_visit':
        if current_location != 'garage':
            call change_loc('fp_garage',sec_call='nr_first_talk',prev_loc=current_location) from _call_change_loc_28
        label nr_first_talk(callcheck=False):
            nr "Hey, [fp]!"
            fp "Hey!"
            fp "{i}You're trying to figure out how to tell [nr] about the hacker, or whatever it is going on at school, preferably without dragging [fsName.yourformal] into it...{/i}"
            nr "Hey, how's [fsName.Name] doing?"
            fp "{i}Oh, right... [nr] had... or maybe the right phrasing is \"has\" a thing for [fsName.Name]{/i}"
            fp "What's it to you?{i}You have a slight mocking tone that you don't really mean to use, but still...{/i}"
            # nr blushing "Oh, well... uhm... I was just wondering! Nevermind..."
            nr "Oh, well... uhm... I was just wondering! Nevermind..."
            "[nr] is looking like he wouldn't mind sinking through the floor right now"
            fp "She's fine. Actually, she's sort of... part of the reason why I wanted to talk to you"
            # nr -blushing "Oh? {i}You can almost see his interest peaking{/i}"
            nr "Oh? {i}You can almost see his interest peaking{/i}"
            fp "She doesn't know I'm talking to you, and no, it's nothing like that. Chill!"
            nr "Oh... {i}He deflates, visibly{/i}"
            fp "Help me with this, and perhaps she'll remember you exist, at least"
            nr "That would be... cool, I guess. What's up?"
            "{i}You spend a bit of time telling [nr] about what happened with [fsName.name], and what [scn] told you{/i}"
            nr "Wow... that's actually... wow. What can I do?"
            fp "Well, I know you know about all this, so I was hoping you could figure something out..."
            nr "I'm gonna stop you right there. Yeah, I know computers, but I'm no genius hacker, or even a script-kiddie. I don't know jack about this shit"
            fp "Oh. {i}Crap, there goes that idea{/i}"
            nr "But I do know people who could probably shed some light on this. Problem is getting them to help"
            fp "Anyone you know-know, or just people on the www?"
            nr "First off... don't call it the www. You sound like a dumbass!"
            nr "Second, I do know someone. As in, personally"
            fp "That's grea..."
            nr "Third, she's never gonna help"
            fp "\"She\"?!? Are you serious?"
            nr "Yes...? Girls can play with computers too, you know"
            fp "Yes yes, I know that. Just... didn't expect you to know a girl who could hack. Didn't expect you to know {b}any{/b} girls, really"
            nr "Haha"
            fp "Kidding, but... why won't she help?"
            nr "Well..."
            fp "Oh... no! You can't be serioius?"
            nr "I know you..."
            fp "HELL NO!"
            nr "She knows her shit, man!"
            fp "Yes. I know that. I also know she's a raging psycho!"
            nr "Not... really. My mom had her tested, you know!"
            fp "Okay... so... you're suggesting your sister?"
            nr "Got it in one!"
            fp "Crap... I really didn't want to deal with [nc]... And I'm guessing you're not volunteering, huh?"
            nr "Oh, no, this is on you"
            fp "Do you at least have her number, email... address? Anything?"
            nr "Yeah... I think so. At least something she used last year or so"
            fp "Text it to me, okay? She might be what I need... even though I would prefer it if she wasn't"
            nr "Sure. Wouldn't count on her being happy, though... she's not very happy about her family, at the moment"
            fp "Well, I'm not family, so I should be safe, then!"
            $ text = "You turn your conversation to the bike standing in the middle of the garage, in pieces. After spending a few hours working on the bike, you decide to {0}".format('have a few beers to end the night' if backpack.has_item(beer_item) else 'call it a night')
            "[text]"
            if "You need to wait for "+nr.name+" to send you "+nc.name+"'s info" not in hints+read_hints+disabled_hints:
                $ set_hint("You need to wait for "+nr.name+" to send you "+nc.name+"'s info")
            $ hacker_4 = False
            $ set_message('nr',nr,"The number for "+nc.name+" is "+nc_number+"")
            $ nre = True
            call change_loc(current_location,loctrans=True,prev_loc=current_location) from _call_change_loc_29

    if event == 'nr_after_nc':
        if nc_after_ft:
            nr "Hey?"
            fp "Hey, man!"
            fp "I called [nc]..."
            nr "Didn't go well, huh?"
            fp "How did you know?"
            nr "Well... I know her. And I know you. Not a brilliant combo, really"
            fp "Jeez, thanks"
            nr "Well, I'm right, aren't I?"
            fp "... Yeah"
            fp "So, any ideas how I can make her actually talk to me?"
            nr "..."
            fp "Nothing?"
            nr "Well... I was gonna suggest you could try to talk to her at home, but... max creepy"
            nr "But she does hang out at [icafe]! Or, at least she used to"
            fp "[icafe]?"
            nr "Yeah, you know, that Internet café, slash dork-haven downtown?"
            fp "Oh, right, yeah I know where it is"
            nr "Best bet, man, best bet"
            fp "'kay, I'll see if she still hangs around. She still got the same look?"
            nr "Yeah... you probably can't miss her"
            $ icafe_discovered = True
            $ visit_icafe_1 = True
            $ calling = duringcall = False
        else:
            $ calling = duringcall = False
            fp "No answer. I'll try him again later"
        $ nre = True
        call change_loc(current_location,prev_loc=current_location) from _call_change_loc_56