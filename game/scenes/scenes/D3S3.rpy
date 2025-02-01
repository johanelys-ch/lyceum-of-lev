label d3s3:
    scene bg_school_front
    if Colenzo:
        m "(I had a hunch Colette would read it on my face if she saw me before Enzo asked her out.)"
        m "(Enzo didn't wait very long, it seems… she caught me right as I was about to head home.)"
        show colette_laugh
        c "[playerName], you won't believe what happened!"
        c "Enzo asked me out!"
        m "WHAAAAAT?"
        show colette_smile
        c "Ok, stop, I know you know. You're a terrible liar."
        c "I honestly didn't know Enzo felt that way…"
        c "I thought they were just flirty with {i}everyone{/i}."
        m "So are {i}you{/i}, Colette."
        show colette_blush
        c "I know! We never would have gotten anywhere if it weren't for you!"
        c "Thanks for… sorting out our feelings for all of us, [playerName]."
        c "You're free tonight, right? How about I take you to that spot in the forest instead? The one I was telling you about?"
        m "Oh! I mean… isn't that a date spot? That's how you made it sound."
        c "Nope. It's a {i}special{/i} spot. You'll see."
        c "I'd just like to spend some time with my best friend, who just did something incredible for me."
        c "Plus, I feel like I got you all worked up about some big secret, after all!"
        m "Delightful. It's not a date."
        c "Not a date! See you later!"
        hide colette_laugh
        hide colette_smile
        hide colette_blush
        jump d3s4c

    elif dC:
        m "(I ran back to Colette. I needed a shoulder to cry on.)"
        show colette_concerned
        c "Oh… I can see it didn't go very well…"
        m "I feel so stupid. I don't know how I was so wrong."
        hide colette_concerned
        show colette_smile
        c "Don't beat yourself up! I know it hurts now, but if they don't know how special you are, that's on them."
        c "You're free tonight, right? How about I take you to that spot in the forest instead? The one I was telling you about?"
        hide colette_smile

        menu:
            "So I can remember how I failed?":
                jump d3s3sadboi
            "Will you bring my weight in ice cream?":
                jump d3s3sadboi
            "Can't I just die instead?":
                jump d3s3sadboi

        label d3s3sadboi:
            show colette_confused
            c "Oh, don't be so dramatic."
            show colette_smile
            c "I think I've got something that'll take your mind off things…"
            c "Plus, I feel like I got you all worked up about some big secret, after all!"
            m "Fine. But I {i}won't{/i} be fun."
            c "I'm sure."
            m "I mean it. I'm gonna be so grumpy."
            c "Of course you will."
            m "SAAAAAAD."
            c "There, there."
            jump d3s4c
    
    else:
        m "(I ran back to Colette. I couldn't wait to tell her the good news.)"
        show colette_smile
        c "Well, don't you look happy? I take it it went well?"
        m "I got a date!"
        c "Of course you do! A catch like you?-"
        c "Wait, I won't keep you here any longer, go get ready!"
        show colette_serious
        c "And be prepared for {i}anything{/i}."
        m "Anything?"
        hide colette_smile
        hide colette_serious

        menu:
            "Is everything ok?":
                jump d3s3happylad
            "It's a first date! How crazy could it get?":
                jump d3s3happylad
            "Are you about to give me \"the talk?\"":
                jump d3s3happylad

        label d3s3happylad:
            show colette_smile
            c "Just, you know, be a good listener!"
            c "Which I know you are! You came this far!"
            c "I gotta go. Good luck!"
            hide colette_smile

label enzodate:
    if dE:
        jump d3s4e

    else:
        show colette_smile
        m "Wait, one more thing."
        show colette_surprise
        c "Oh? Something {i}else{/i} on your mind? Don't you need to get ready?"
        hide colette_smile
        hide colette_surprise

        menu:
            "What's this \"special spot\" all about? Is there something I don't know?":
                jump d3s3z2
            "What do you even {i}do{/i} on a date?":
                jump d3s3z3
            "You know… Enzo {i}like{/i} likes you…":
                jump d3s3wingman

label d3s3z2:
    show colette_smirk
    c "Well, {i}I'm{/i} not going to tell you! Wait for your date, you eager beaver."
    m "Ok… I trust you."
    c "Don't be nervous! You'll have a great time!"
    c "Now go get ready!"
    hide colette_smirk
    jump d3s3zend

label d3s3z3:
    show colette_concerned
    c "{size=*0.5}Oh no, it's worse than I thought...{/size}"
    m "Hm?"
    hide colette_concerned
    show colette_smile
    c "Nothing! Uh… ok, look. Try not to overthink it. If you're right for each other, it'll unfold naturally."
    m "Do we… hold hands?"
    c "...you're messing with me right?"
    c "You're such a goofball, [playerName]. I swear, you could give Enzo a run for their money."
    c "Now go get ready!"
    hide colette_smile
    jump d3s3zend
    
label d3s3wingman:
    if check_affinity_flexible("Enzo", 6):
        show colette_embarrassed
        c "..."
        c "You're being serious."
        c "I don't know… does Enzo really feel that way… I thought they were just flirty with {i}everyone{/i}."
        m "So are {i}you{/i}, Colette."
        show colette_shocked
        c "Oh my god, you're right."
        c "I {i}am{/i} flirty with everyone."
        c "HOW COULD THEY KNOW?"
        show colette_blush
        c "Ok, I need to go think about some stuff… {i}you{/i}..."
        c "You go get ready for your date!"
        hide colette_embarrassed
        hide colette_shocked
        hide colette_blush
        m "(She must have known deep down, right?)"
        m "(Guess I'll have to wait and see…)"
        jump d3s3zend

    else:
        show colette_surprise
        c "Oh, wow, [playerName]. You really had me going there for a second!"
        c "They're just like that. They're a flirty person. You can't take them seriously!"
        c "Ok, quit goofing around. You have a date to get ready for!"
        hide colette_surprise
        m "(...)"
        m "(I wonder if there's any way those two will ever figure it out…)"
        jump d3s3zend

label d3s3zend:
    if dS:
        jump d3s4s
    elif dR:
        jump D3S4rz1
    else:
        jump d3s4c