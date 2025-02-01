label d4s4x:
    scene bg classroom
    show colette_confused
    c "Well, best friend? Where did you decide to go?"
    hide colette_confused
    menu:
        # code so that only the schools the player got into actually appear as options
        "Frights High Community College":
            jump D4S4x1
        "Black Lagoon University":
            jump D4S4x2
        "Vampire Academy of Vermont":
            jump D4S4x3

label D4S4x1:
    show colette_awe
    c "What?! No way! We're going to the same school?"
    m "{i}You're{\i} going?"
    show colette_smile
    c "Yeah, duh. I may not care about school, but I'm not missing out on the social life. That's the real education!"
    m "Fair enough!"
    hide colette_awe
    hide colette_smile
    show enzo_surprise
    e "Do my ears deceive me? You'll be joining us at Frights High?"
    hide enzo_surprise

    if Colenzo:
        m "Yep, I'm your constant third wheel!"
        show colette_blush at right
        c "Oh stop it."
        show enzo_smirk at left
        e "Perhaps setting you up is {i}kind of{\i} like a prank…"
        e "I'm up for the challenge!"
        m "H-hey!"
        show colette_smile at right
        c "Quit complaining, that's what friends are for."
        e "Gotta run. I'll be seeing my prankster trio soon enough."
        hide colette_blush
        hide colette_smile
        hide enzo_smirk

    elif not Colenzo and check_affinity_flexible("Enzo", 6):
        m "Yep! What will you two do without your prank leader?"
        show enzo_surprise
        e "I didn't realize my enrollment was ever in doubt."
        hide enzo_surprise
        show colette_smile
        c "Ok you two, stop sparring for two seconds. Let's just celebrate the good news!"
        hide colette_smile
        show enzo_smile
        e "Yes, let's! Let's do something later, ok? I'll catch up with you later."
        e "I can't miss one of these last opportunities to prank Roger…"
        hide enzo_smile

    else:
        show enzo_smirk
        m "Yeah!"
        e "Well, well, how exciting. Another chance to convince you to see things my way."
        hide enzo_smirk

    show colette_surprise
    c "OH MY GOD! LET'S BE ROOMMATES!!!"
    hide colette_surprise
    jump D4S4xend

label D4S4x2:
    show colette_smile
    c "There's my smartypants BFF."
    hide colette_smile

    if Colenzo:
        show enzo_concerned
        e "Most lamentable! What will we do without our third wheel?"
        hide enzo_concerned
        show colette_confused
        c "Babe! You're going to hurt [playerName]'s feelings!"
        m "No, see, {i}that's{/i} what annoys me."
        c "Aw… sorry, babe two…"
        m "Never mind, I forgot about that…"
        m "Well, you two will just have to learn how to do good pranks without me."
        hide colette_confused
        show enzo_concerned
        e "With that kind of education? You better!"
        e "Well, I've got somewhere to be now. I can't miss one of these last opportunities to prank Roger…"
        hide enzo_concerned

    elif check_affinity_flexible("Scylla", 6):
        show scylla_laugh
        s "Hey! Did I hear you're going to BLU too?"
        m "Yeah! I'm so excited"
        s "Cool! Don't be a stranger, ok? Let's hang out when we're there!"
        hide scylla_laugh

    elif check_affinity_flexible("Scylla", 4):
        show scylla_concerned
        m "(Scylla walked past without saying anything.)"
        hide scylla_concerned

    show colette_smile
    c "You know Scylla thinks you're hot, right?"
    m "What???"
    c "Yeah, years ago. She saw you and mentioned it."
    m "Huh… wonder why she never acted on it…"
    show colette_shocked
    c "Oh, she's just always so busy doing things for other people. I hope she puts her foot down more in college."
    c "Well! Maybe it's not too late? Do you think she's a cutie?"
    m "Well, uh…"
    c "Relax, tiger. I'm just goofing. You should see your face."
    hide colette_smile
    hide colette_shocked
    jump D4S4xend

label D4S4x3:
    m "(Roger's eyes popped out of his skull.)"
    show roger_shocked
    r "YOU? How did YOU get in THERE?"
    r "This is a joke, right?"
    hide roger_shocked

    if Colenzo:
        show enzo_smile
        e "If it is, then [playerName] has nothing more to learn from me."
        e "I tip my hat to you."
        hide enzo_smile
        show colette_smile at right
        show enzo_smile at left
        c "Babe, I didn't buy you that hat so you would {i} actually{\i} go around tipping it."
        e "Where else can I tip it? Let the tipping commence!"
        hide enzo_smile
        hide colette_smile
        show colette_smirk
        c "That's my special person…"
        c "I hope we get married one day..."
        hide colette_smirk

    m "Guess I'll see you there, Roger!"
    show roger_serious
    r "What's wrong with the world… Poopies going to Vampire Academy…"
    hide roger_serious
    show colette_smile
    c "I'm so proud of you, best friend. I know you know why."
    c "This is a huge achievement!"
    hide colette_smile
    jump D4S4xend

label D4S4xend:
    show colette_concerned
    c "Hang on… do you hear that? It's like a…"
    m "Clucking noise?"
    c "Yeah… that's weird. I thought Enzo said you took them back."
    m "Why would I do that?"
    c "I don't know. That's just what Enzo said!"
    m "Enzo said that {i}you{/i} recovered the chickens…"
    c "Why would…"
    m "Oh no…"
    show colette_confused
    c "Classic Enzo…"
    m "The chickens have been loose in the school this whole time? It's been months!"
    c "Wait! [playerName]! Look!"
    m "Are they…"
    hide colette_concerned
    hide colette_confused
    scene bg_chickenkiss with dissolve
    pause 2.5
    scene bg classroom with dissolve
    show colette_smile
    c "Have you ever seen anything so beautiful?"
    m "Honestly?"
    m "I have not."
    m "Hey… you should take a picture of this moment!"
    c "Good call, best friend."
    show colette_smile with flash
    return