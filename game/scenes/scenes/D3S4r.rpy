label D3S4rz1:
    m "(The forest is peaceful, the perfect backdrop for a moment like this...)"
    m "(Nothing seemed that special about this spot that Colette recommended, though… some ruins of an old structure, maybe a well or a fountain?)"
    m "(I unpack the snacks, but Roger's gaze drifts toward the trees, as if he's lost in thought.)"
    m "Earth to Roger? Are you still with me?"
    r "Huh? Oh. Yeah, yeah, I'm here. Just... it's nice out here, isn't it?"
    m "It really is. I didn't think you were the \"forest date\" type, though."
    r "Pfft, what? I can be outdoorsy! I mean, I'm here, aren't I? You dragged me here, I guess."
    m "(His voice carries its usual bite, but there's a softness in his tone tonight.)"

    menu:
        "Here, try one of these. They're my favorite.":
            jump D3S4rz2

        "You're acting differently. Dare I say... soft?":
            jump D3S4rz3

label D3S4rz2:
    m "Here, try one of these. They're my favorite."
    r "...Sure. Not like I had a choice."
    jump D3S4rz4

label D3S4rz3:
    m "You're acting differently. Dare I say... soft?"
    r "Soft? Me? Ha! You wish, poopie."
    m "(Even as he says it, he can't meet my eyes.)"
    jump D3S4rz4

label D3S4rz4:
    m "(I hand him a snack, expecting his usual sarcastic comments, but he pauses after the first bite.)"
    r "..."
    m "Uh... Roger? You okay there?"
    r "Huh? Yeah, totally. Just—what do you call this thing?"
    m "(He's trying to act casual, but his eyes are wide like he's just discovered fire.)"
    m "(Wait a second... has he never had this before?)"
    m "You've never tried this, have you?"
    r "What? Of course I have! I just don't waste my time learning brand names. Food should be food, not proper nouns, man."
    m "(He's a terrible liar. I smile, watching as he takes another bite, this time slower, savoring it.)"
    r "...It's pretty good. You have decent taste, I guess."
    m "That's high praise coming from you."
    r "{size=*0.5}Maybe you just bring out the best in me.{/size}"
    m "What was that?"
    r "Nothing!"
    m "(He's blushing now, and I can't help but laugh. Roger might pretend to be tough, but moments like this give him away.)"
    jump D3S4rz5

label D3S4rz5:
    m "(After a while, Roger grows quiet again, his usual spark dimming. Something's clearly on his mind.)"
    r "...Hey, poopie. I need to tell you something, and it's kind of a big deal."
    m "Big deal? You're not about to confess to a crime, are you?"
    m "Oh, no... did you steal all of those watches?"
    r "What? No! This is... serious."
    m "(His tone makes me sit up straighter. Roger isn't usually this hesitant.)"
    r "Remember that chat we had on the stairs? About how history only reflects one side?"
    m "Yeah, you pointed out the narrative was anthropocentric. And called humans… poopies."
    r "And I stand by that. You poopies love your own story so much, you bury everything else. Other voices, other... beings. Monsters."
    m "(Beings?)"
    m "({i}You{/i}?)"
    r "See, the thing is... I care about history because I'm part of the side that got buried. We don't get the spotlight." 
    r "Nothing we did even gets a footnote except for the part where we stopped being around."
    m "(We...?)"
    m "Roger, what are you talking about?"
    m "(He sighs, running a hand through his hair like he's about to rip it out.)"
    r "I'm not human, poopie." 
    r "Never have been. I'm one of those \"Monsters\" your history books like to pretend don't exist anymore."
    m "(The world feels like it tilts for a second. Did he just say—?)"
    m "You're not... human?"
    r "Yeah, no. Shocker, right? Guess I hide it pretty well, huh?"
    m "(I stare at him, but he's not smirking like he usually does. This time, he looks... vulnerable.)"
    r "At some point, you humans came along and decided you were the center of the universe. The rest of us had to adapt or disappear."
    m "(This isn't just some history lecture for him. This is personal.)"
    r "You probably think I'm lying. Or crazy. That'd be easier, wouldn't it?"
    r "The real stories are still out there, but no one's looking for them. And maybe they'll never matter again."

    menu:
        "I don't think you're lying, Roger. I believe you.":
            jump D3S4rz6
        "Why are you telling me this now, Roger?":
            jump D3S4rz7

label D3S4rz6:
    m "I don't think you're lying, Roger. I believe you."
    r "...You do? Well, uh, good. Because I don't feel like proving it right now…" 
    r "Or, you know what? Maybe I do."
    m "(He looks away, but there's a hint of relief in his expression.)"
    jump D3S4rz7a

label D3S4rz7:
    m "Why are you telling me this now, Roger?"
    r "Because it's not just about me anymore. You're... ugh, forget it."
    m "(He groans, but I can tell he's struggling to say something more.)"
    jump D3S4rz7a

label D3S4rz7a:
    menu:
        "Okay, so, you're telling me monsters have been hiding among humans for a long time now? And no one noticed?":
            jump D3S4rz8
        "Alright, you've officially lost me. You're joking, right?":
            jump D3S4rz9

label D3S4rz8:
    m "Okay, so, you're telling me monsters have been hiding among humans for a long time now? And no one noticed?"
    r "Humans see what they want to see. Plus, we're good at blending in. It's not like I go around in my true form."
    m "(...)"
    r "Okay, can you close your eyes for a second?"
    r "You said you believed me. So don't freak out, okay?"
    m "(I nodded and closed my eyes. My brain only thinking the same thing over and over again, \"What's going on?\")"
    jump D3S4rz10

label D3S4rz9:
    $ decrease_affinity("Roger", 1)
    m "Alright, you've officially lost me. You're joking, right?"
    r "Ugh, poopie, I knew this would happen. Just watch. I'll prove it."
    r "Don't freak out, okay?"
    m "(I nodded and closed my eyes instinctively. Is he going to pop a balloon and say \"Gotcha!\"?)"
    jump D3S4rz10

label D3S4rz10:
    r "You can open your eyes now."
    # description of how roger looks like in his gremlin form lol
    r "...You're staring. It's weird."
    jump D3S4rQ

label D3S4rQ:
    r "I bet you have questions. Go ahead. Ask while you can."
    menu:
        "Are you allowed to tell me this? Oh my gosh, are {i}you{/i} breaking the rules?":
            jump D3S4rQ1
        "So you're like a werewolf, right?":
            jump D3S4rQ2
        "Is that why you wear so many watches? Is that a monster thing?":
            jump D3S4rQ3
        "I feel pretty caught up now.":
            jump D3S4rsooo
    
label D3S4rQ1:
    r "N-no! It's a… gray area."
    r "I mean, it'd be impossible for {i}no{/i} humans to know. It becomes necessary sometimes." 
    r "Besides, what's the alternative? Getting rid of inconvenient people is a real human move."
    r "There aren't a lot of humans who know the secret. Not many are worth bothering with."
    jump D3S4rsooo

label D3S4rQ2:
    r "Ha ha. I'm a gremlin."
    r "I don't know what preconceived notions you may have, but we're not, like, inherently evil or chaotic or anything."
    r "Like… my dad's actually an actuary..."
    m "Huh, I just assumed there was, like, a fancy family business you were in line to inherit."
    m "You're giving finance bro."
    r "Well, it's not cool to dream of being an actuary. It's way cooler to convince people I'm on track to being a stockbroker."
    m "...is it?"
    r "...is it not?"
    r "{size=*0.5}Wait… do people {i}not{/i} think I'm cool?{/size}"
    jump D3S4rsooo

label D3S4rQ3:
    r "No, dummy, that's just called {i}style{/i}."
    m "(Huh, so that's just a Roger thing then…)"
    jump D3S4rsooo

label D3S4rsooo:
    r "Cool. So. Yeah. This is me."
    r "I'm just a little guy."
    m "(Roger is quiet now… maybe he's still waiting for something…)"
    m "(This is... a lot.)"
    menu:
        "(But it's still Roger. The same snarky, weird guy I've come to like.)":
            jump D3S4rKissE1
        "(I can't handle this. Monsters? What if he wants to do something to me? This is too much.)":
            jump D3S4rE2

label D3S4rKissE1:
    $ increase_affinity("Roger", 5)
    m "I don't care what you look like. I like you for you, and your watches... and your amazing dancing skills."
    r "You're unbelievable."
    m "Thanks for telling me. Really."
    r "...Yeah. Whatever. Don't make me regret it, okay?"
    m "(He turns away slightly, but I reach out and grab his hand before I even realize what I'm doing.)"
    m "Roger, wait—"
    m "(He looks at me, startled, and in that moment, I lean in and kiss him.)"
    show bg_roger_kiss
    m "(For a second, he freezes. Then, he kisses me back.)"
    hide bg_roger_kiss
    r "[playerName], you're so strange."
    m "(He's blushing—blushing!—and for once, I don't think it's just from annoyance.)"
    m "You just called me weird? Wow!"
    r "You've got terrible taste, you know that? A kiss like that, and I almost don't want to scare you off."
    m "...Scare me off?"
    r "Yeah. Guess I can't back out now. Why would you even kiss a gremlin?"
    m "Now that I think about it, I don't know..."
    m "(We laughed for a second, tension finally going down.)"
    r "...Still think I'm cool?"
    m "Roger, you're... amazing."
    r "(He blinks, clearly not expecting that answer. Then he lets out a laugh—nervous, but genuine.)"
    r "Yeah, you're such a strange poopie, [playerName]. But... thanks. I suppose I can say the same thing about you."
    m "(Despite everything, I step closer. Roger's still Roger—whether he's human or not. And I kind of like him this way, too)"
    r "...Guess you're stuck with me now, poop— er, [playerName]."
    m "Yeah, I guess so."
    m "(And honestly? I'm okay with that.)"
    jump D3S5

label D3S4rE2:
    if not d4:
        $ d4 = True
        $ decrease_affinity("Roger", 15)  

    m "I'm sorry, Roger. I just... can't."
    r "...Figures. Whatever. Go on, poopie. Get lost."
    m "(I feel terrible, but what was I supposed to do? He's all green and... weird…)"
    m "I just don't get all of this, like, what are you really?"
    r "A monster? I literally explained all of this to you a couple of minutes ago."
    m "(There's pain in his voice, but also a strange kind of pride.)"
    r "You asked. Now you know. It's okay, just don't come near me ever again."
    r "Oh, and not that I'd care, but if you say anything to anyone…"
    r "One, no one will believe you."
    r "And two, werewolves will come eat you."
    r "Have a nice life."
    jump d4s0