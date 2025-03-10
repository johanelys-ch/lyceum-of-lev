label d3s4c:
    scene bg forest with dissolve
    m "(Colette and I walked into the forest. She was skipping with joy.)"
    show colette_smirk
    c "Ok, I have a huge secret to tell you. HUGE."
    c "I've wanted to tell you for {i}forever{/i}."
    m "You've piqued my interest…"
    c "So, this spot in the forest. It's a special spot."
    m "It's beautiful."
    m "...aside from those ruins… actually, they're kind of pleasant, in a ruins sorta way."
    m "What do you think it used to be? It's pretty small. Maybe like… a fountain?"
    show colette_embarrassed
    c "Ok, you're getting too fixated on the wrong part about this spot."
    m "Sorry. Go on."
    show colette_smile
    c "So, as I was saying, it's an important place."
    c "This is where one of the first human-monster treaties was signed."
    m "Right here? In {i}our{/i} town?"
    c "Yeah! Something like thousands of years ago? I don't know. You're the one taking history classes."
    m "...with you. You are in my history class."
    c "So it's not a magical place or anything, not really. It has no real power."
    c "Maybe it did once. Who knows why they signed the treaty here."
    c "But now, it's a nice spot that many will come to to remember that, sometimes, a better world can be possible."
    c "It might not last, but sometimes people want to try."
    hide colette_smirk
    hide colette_embarrassed
    hide colette_smile

    menu:
        "I didn't take you for such a historian.":
            jump d3s4cz1
        "That's very hopeful.":
            jump d3s4cz2
        "But the monsters are all gone.":
            jump d3s4cz4

label d3s4cz1:
    show colette_smirk
    c "Some stuff is too important to not pick up on."
    hide colette_smirk
    jump d3s4cz3

label d3s4cz2:
    show colette_smile
    c "I like to think so."
    jump d3s4cz3

label d3s4cz3:
    show colette_smile
    m "That's so weird… I don't remember this coming up in Ms. Lalonde's class…"
    m "...am I doing really bad in history class?"
    hide colette_smile
    show colette_concerned
    c "No, this sort of thing isn't in human textbooks."
    m "But there aren't monster textbooks."
    hide colette_concerned
    show colette_embarrassed
    c "That's true. There aren't."
    m "And the monsters have been gone for 500 years."

label d3s4cz4:
    c "Well. They're not."
    show colette_monster_awe with flash
    c "Surprise, bitch! I'm a monster!"
    hide colette_monster_awe
    hide colette_embarrassed

    menu:
        "Siiiiick. (nonderogatory)":
            jump d3s4cz5
        "Sick! (derogatory)":
            jump d3s4cz6
        "I'm sorry, what's happening?":
            jump d3s4cz7

label d3s4cz5:
    m "(Colette z snaps)" 
    jump d3s4cz7

label d3s4cz6:
    show colette_monster
    c "Nope! I'm not sick! This is what I really am!"
    hide colette_monster
    jump d3s4cz7

label d3s4cz7:
    show colette_monster
    c "I'm a ghoul!"
    c "Monsters live all around us! There are so many different kinds, all hidden in plain sight using glamours, disguises, makeup…!"
    c "In fact, my parents' cosmetics company isn't just a normal cosmetics company."
    c "The {i}real{/i} clientele is monsters disguised as humans."
    c "It's a huge secret, obviously. Most humans would lose their minds right about now."
    hide colette_monster

    menu:
        "Uhhhhh you don't say…":
            jump d3s4cz8
        "Not me. I figured it out ages ago.":
            jump d3s4cz9
        "Have you told any other humans before?":
            jump d3s4cz10

label d3s4cz8:
    show colette_monster
    c "Well, this must all be pretty mind-blowing."
    c "I can only imagine what's going through your head right now!"
    hide colette_monster

    menu:
        "I feel like, in retrospect, this explains a lot.":
            jump d3s4cQ
        "I feel like you've kind of betrayed me.":
            jump d3s4cznotgoinggreat
        "I feel nothing but abject terror.":
            jump d3s4czbad

label d3s4cz9:
    show colette_monster
    c "I bet! You're the brains."
    hide colette_monster
    
    menu:
        "Girl, stop selling yourself short!":
            jump d3s4cz11
        "And do you… {i}eat{/i} brains?":
            jump d3s4cznotgoinggreat

label d3s4cz10:
    show colette_monster_awe
    c "No… you're the first. It's not exactly a safe thing to just go around telling people…"
    c "Aren't you special?"
    hide colette_monster_awe
    jump d3s4cQ

label d3s4cz11:
    show colette_monster
    c "Ughhhhh. Seriously, [playerName]! You're the best!"
    c "I'm sorry everyone at this school was too dumb to see that."
    c "Don't worry, you're gonna get so laid in college."
    m "Colette!"
    scene bg forest with flash
    show colette_monster_awe
    c "Oh, that reaction was priceless!"
    c "Hahaaaaaaa"
    c "Well, I bet your mind is totally racing right now."
    hide colette_monster
    hide colette_monster_awe
    jump d3s4cQ

label d3s4cQ0:
    show colette_monster_confused
    c "Well… I know this is hard for you too…"
    hide colette_monster_confused
    jump d3s4cQ

label d3s4cQ:
    show colette_monster
    c "Come on, you must have plenty more questions."
    hide colette_monster

    if not Colenzo and check_affinity_flexible("Enzo", 6):
        menu: 
            "How many monsters are there?":
                jump d3s4cQ1
            "This might be a really dumb question. If you're a ghoul… are you, like, dead?":
                jump d3s4cQ2
            "Do you want to be a… human model? Or are there monster models?":
                jump d3s4cQ3
            "Nope. No further questions.":
                jump d3s4csoooo
            "You know that Enzo has a huge crush on you, right?":
                jump d3s4czenzo

    else:
        menu: 
            "How many monsters are there?":
                jump d3s4cQ1
            "This might be a really dumb question. If you're a ghoul… are you, like, dead?":
                jump d3s4cQ2
            "Do you want to be a… human model? Or are there monster models?":
                jump d3s4cQ3
            "Nope. No further questions.":
                jump d3s4csoooo

label d3s4cQ1:
    show colette_monster
    c "No one knows! How many birds are there? How many stars in the sky?"
    c "We're all pretty scattered. Different types of monsters tend to live in different places, some not among humans at all."
    c "I mean, individual monsters have their preferences and all. Don't go thinking each monster is, like, a monolith."
    c "But in general, you'll find fewer sea monsters and yetis who want to live in the desert."
    hide colette_monster
    jump d3s4cQ

label d3s4cQ2:
    show colette_monster_concerned
    c "Honestly? I don't know!"
    c "Like you said, it's not like there are monster textbooks around."
    c "Huge swaths of our understanding of ourselves is gone forever…"
    c "...due not to a single agency or structure, but by episodic and sovereign acts of domination and coercion."
    c "...huh, I'm sitting too close to Roger in class, aren't I?"
    hide colette_monster_concerned
    jump d3s4cQ

label d3s4cQ3:
    show colette_monster_awe
    c "Ooooo, that's a good question."
    c "More than anything, I want to be a fashion model for the top agency in the monster world, Morgue."
    show colette_monster
    c "But honestly I'm worried if I get it, I'm worried it would just be because of my family's cosmetics connections."
    c "So that's why I got into photography too. I want to have {i}something{/i} going for me that isn't my looks or my parents."
    hide colette_monster_awe
    hide colette_monster
    jump d3s4cQ

label d3s4czenzo:
    if not Colenzo:
        $ Colenzo = True
    show colette_monster_awe
    c "{i}That's{/i} what you're thinking right now?"
    c "Wait… are you {i}serious{/i}?"
    c "How could I have missed this?"
    m "Well, Enzo's flirty with everyone."
    m "...and you're flirty with everyone."
    m "So I can see how it was unclear."
    c "Oh wow… a prison of my own design…"
    c "Do {i}I{/i} have a crush on Enzo?"
    m "Girl, obviously."
    c "I have much to ponder…"
    show colette_monster
    c "Ok, my love life aside, anything else regarding the whole monster thing?"
    hide colette_monster_awe
    hide colette_monster
    jump d3s4cQ

label d3s4cznotgoinggreat:
    show colette_monster_confused
    c "Of course not! Is that really what you think? Are you feeling ok, best friend?"
    hide colette_monster_confused
    
    menu: 
        "Are you?! How long have you been lying to me?!":
            jump d3s4czbad
        "It's… a lot to take in is all…":
            jump d3s4cQ0
        "Sorry! I didn't mean to hurt you!":
            jump d3s4cQ0

label d3s4czbad:
    show colette_monster_confused
    c "...I thought we were friends."
    hide colette_monster_confused
    m "(Colette ran away crying.)"
    m "(The only person I had…)"
    m "(What if… {i}I'm{/i} the monster?)"
    $ d4 = True
    jump D3S5

label d3s4csoooo:
    show colette_monster
    c "So… we're cool, right?"
    hide colette_monster

    menu:
        "I'm honored you trust me with this!":
            jump d3s4cyay
        "I mean… our entire friendship is based on lies. With a monster.":
            jump d3s4czbad

label d3s4cyay:
    show colette_monster
    c "I'm so glad you finally know!"
    c "Now let's enjoy the rest of this year!"
    hide colette_monster
    jump D3S5
