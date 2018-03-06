label nc_talk(event=False,callrand=False):
    if event == 'first_talk':
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
                fp "{i}Okay... not the best start. Maybe I can figure out a way to get her to talk to me, at least...{/i}"
                $ nc_after_ft = True
                if "You need to figure out a way to get "+nc.name+" to talk to you. Perhaps talk to "+nr.name+" again, see if he knows anything else that might help" not in hints:
                    $ hints.append("You need to figure out a way to get "+nc.name+" to talk to you. Perhaps talk to "+nr.name+" again, see if he knows anything else that might help")
            else:
                $ calling = duringcall = False
                if nc_after_ft:
                    fp "No answer. No surprise there, after what she did when I called the first time..."
                else:
                    fp "No answer. I guess I'll have to try again later"            
        call change_loc(current_location)

    if event == 'icafe_visit':
        $ settime(20,00)
        if visit_icafe:
            "You arrive at [icafe]. Looking around, trying to let your eyes adjust to the dimly lit location, with glowing screens across the interior. Not the easiest place to find someone..."
            "Scanning the room, you try to spot [nc] in the crowd. Not that many girls in here, that you can see, but then half the crowd is wearing hoodies and headphones, making it hard to pinpoint gender"
            "Suddenly, you hear yelling from the far side of the cafe"
            unk_f "{b}Hell to the FUCK no!{/b}"
            unk_m "Listen..."
            unk_f "{b}Shut the FUCK UP!{/b}"
            unk_m "Calm U+2588U+2588U+2588n!"
            unk_f "{b}I will not \"calm down\"! I'm fucking pissed!{/b}"
            "You start heading for the commotion... knowing [nc], this... sorta sounds like her, even though you cannot really remember her voice"
            "When you approach them, they seem to at least have turned down the volume a little bit, but the tension is still palpable"
            "You hang back, trying to figure out if this is both something you want to get involved in, and also if this is even the girl you're looking for"
            "The girl rips off her headphones and throws them on the table, before pulling back the hoodie and releasing a mane of jet black hair"
            unk_f "{b}How the fuck can you manage to be this fucking clumsy, you idiot?{/b}"
            "You can see a laptop on the table, no lights or anything... and then you spot the Jolt-cup... oooooh, you get the anger now. That laptop looks like something in the $2000+ range"
            unk_m "I'm sorry, [nc]! I will get it fixed, I promise..."
            "{b}Score!{/b} You found her!"
            nc "The fuck you will. I'm not letting you anywhere near my laptop, you pathetic piece of shit"
            unk_m "I just wanted to help..."
            nc "Help? What you want is to get hold of my drives. Which would do you no good, since they're encrypted, and the only key is in my head. You would've gotten exactly nowhere!"
            "The guy slinks away without looking back. In the meantime, [nc] seems like she wants to kill someone, and you decide that you really don't wanna be that guy. You decide to come back and talk to her when she's in a slighlty less confrontational mood"
            $ visit_icafe = False
        else:
            fp "I should call [nr] and see if he knows where I might find [nc]..."
        call change_loc(current_location)

    if event == 'icafe_talk':
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
        fp "Fine. I'm looking for some help with what I suspect is a hacker-attack on HSS' systems"
        nc "You... suspect a \"hacker attack\"?!? {i}The mirth in her voice is not really endearing...{/i}"
        fp "Yeah, I do. I'm willing to pay, of course. Seems like you could use a new computer?"
        nc "Hm. How much?"
        fp "How much do you need?"
        nc "For a new laptop?"
        fp "Yeah"
        nc "A couple grand should do it"
        if fp_money > 2000:
            fp "No problem"
            "[nc] looks a little perplexed with your seeming indifference to the amount she asked for"
            nc "O... kay. Money up front, then tell me what you need"
        else:
            fp "I can't afford that right now"
            nc "Then get back to me when you can"
            "She gets up, and leave you sitting there, a little taken aback by her straight forwardness and boldness"
            fp "{i}2 grand. Holy shit... Where the fuck am I gonna get 2 grand?{/i}"