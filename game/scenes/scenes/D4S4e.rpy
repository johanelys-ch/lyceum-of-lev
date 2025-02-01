label D4S4e:
    scene bg_hallway with dissolve
    m "(After class, I found Enzo rummaging through their locker.)"
    m "(Not for books. For prank paraphernalia.)" 
    m "(Come to think of it, I've never seen them with a book for class…)"
    show enzo_smile
    e "Oh hello you! Moment of truth..."
    e "Did you decide where you're going to school?"
    hide enzo_smile

    menu:
        # code so that only the schools the player got into actually appear as options
        "Frights High Community College":
            jump D4S4esame
        "Black Lagoon University":
            jump D4S4eLD
        "Vampire Academy of Vermont":
            jump D4S4eLD

label D4S4esame:
    show enzo_smirk
    e "Wow, couldn't keep away, could you?"
    m "Someone's got to keep you in line."
    e "Truly. We'll be up to no good in no time." 
    e "In fact, I've got something cooking right now. Let me show you…"
    m "(Enzo told me their idea.)"
    hide enzo_smirk
    show enzo_surprise
    e "Well? Give me your feedback."
    m "It's a good start… but it's a good thing we're going to the same school."
    m "You've gotten sloppy. Clearly I've been distracting you."
    show enzo_shocked
    e "Sloppy?! How dare you! Do you see my mock outrage?"
    m "(We excitedly talked about the prank.)"
    e "Oh. Yeah, that {i}is{/i} better."
    show enzo_smirk
    e "Well, that's why I'm getting a higher education. The pranks won't get better if I don't put in the work."
    m "Yes, this is exactly why I'm going to college."
    e "Hey, I'm really glad you'll be right there by my side."
    hide enzo_surprise
    hide enzo_smirk
    hide enzo_shocked
    jump D4S4eend

label D4S4eLD:
    show enzo_smile
    e "Exciting! Now I'm going to have two places to play pranks instead of one!"
    m "Hang on… so you're saying you want to do long-distance? We haven't actually talked about it yet…"
    e "Hm… yes, perhaps we could stand to make time to talk about serious things rather than jokes all the time."
    e "But for me, of course I would. I'm happy you're pursuing your dreams, wherever that is."
    e "How are you feeling? Excited?"
    hide enzo_smile

menu:
    "Unsure. I've been fantasizing for so long that this day would come, but now that it has, I'm not sure how to feel!":
        jump D4S4eLD1
    "So excited! I'm glad you want to stay together. Even though we won't be too close, I'm sure we can make it work.":
        jump D4S4eLD2
    "Sad. I really wanted us to go to the same school. But I know this is the right choice.":
        jump D4S4eLD3

label D4S4eLD1:
    show enzo_smile
    e "It will be good, I am sure of it. I'm just so happy we got to be together for these last several months."
    show enzo_confused
    e "Don't get me wrong, I don't know the future. But aren't you just so very curious to see how our relationship will evolve?"
    hide enzo_smile
    hide enzo_confused
    jump D4S4eLD2

label D4S4eLD2:
    show enzo_smirk
    e "What have we done all this hard work for if not to prepare for this?"
    m "Hard work? What, our pranks? Our pranks were all just preparation for long-distance?"
    e "Think about it. Clever workarounds to silly mundane facts of life?"
    e "Finding the joy in the little moments you'd forget otherwise?"
    e "How is it not?"
    hide enzo_smirk
    jump D4S4eend

label D4S4eLD3:
    show enzo_smile
    e "I know it is! I believe in you. I believe in us. And after all…"
    hide enzo_smile
    jump D4S4eLD2


label D4S4eend:
    jump d4s4x
