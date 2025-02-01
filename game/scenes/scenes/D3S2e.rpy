label d3s2e:
    scene bg_hallway with dissolve
    m "(I caught up with Enzo after class.)"
    show enzo_laugh
    e "I think I manifested you, [playerName]. Was just thinking about you…"
    hide enzo_laugh
    jump d3s2ez1

label d3s2ez1:
    menu:
        "I've been thinking about you, Enzo. I was wondering if you might… want to go on a date?":
            jump d3s2ez2
        "Enzo, you're adorable. Would you go out on a date with me?":
            jump d3s2ez2
        "I've been wondering… Would you like to go on an adventure with me?":
            jump d3s2ez3
        "Enzo, I was talking with Collette, and you should know… she likes you. Like like likes you.":
            jump d3s2ez4

label d3s2ez2:
    if check_affinity_flexible("Enzo", 6):
        show enzo_smirk
        e "Ok, mind-reader. That's exactly what I was thinking. High time."
        e "My, aren't you full of surprises…"
        e "How about the forest, tonight?" 
        m "Huh, wild, I was going to suggest that…"
        e "Must be something in the water. Oh, and make sure you're late, ok? It's VERRRY important."
        hide enzo_smirk
        $ dE = True
        jump d3s3

    else:
        show enzo_serious
        e "Wait, a date? Ohhh, I think I must have given you the wrong idea." 
        e "Really, I'm flattered, but it's a no."
        e "You're swell and all, but… I don't get the impression we're looking for the same thing."
        hide enzo_serious
        m "(Enzo left…)"
        m "(I guess I misread that one…)"
        $ dC = True
        jump d3s3

label d3s2ez3:
    if check_affinity_flexible("Enzo", 6):
        show enzo_smirk
        e "My my my, you have no idea how much I've wanted to go on an adventure."
        m "Great. I got a hot tip about this spot in the forest that's just the talk of the town."
        e "You don't say…"
        e "Look I'll be honest, I thought you'd never ask. Like really, really never thought."
        e "It's a date. Oh, and make sure you're late, ok? It's VERRRY important."
        hide enzo_smirk
        $ dE = True
        jump d3s3

    else:
        show enzo_smile
        e "An adventure? What is this a reality dating show?"
        show enzo_serious
        e "Wait… you {i}do{/i} mean like a date…" 
        e "Ohhh, I think I must have given you the wrong idea." 
        e "Really, I'm flattered, but it's a no."
        e "You're swell and all, but… I don't get the impression we're looking for the same thing."
        hide enzo_smile
        hide enzo_serious
        m "(Enzo left…)"
        m "(I guess I misread that one…)"
        $ dC = True
        jump d3s3

label d3s2ez4:
    $ dC = True

    if check_affinity_flexible("Enzo", 6):
        $ Colenzo = True
        show enzo_surprise
        e "You're kidding me…"
        e"I mean, I had my suspicions, but…"
        e "Well, it's a little silly, I guess, but I'll be honest. I thought {i}you{/i} did!"
        e "But if it's her, well… I'd better go talk to her."
        show enzo_smile
        e "You're a good friend, [playerName]. Thanks for giving me the push I needed."
        hide enzo_smile
        hide enzo_surprise
        m "(Enzo left.)"

        menu:
            "I'm happy for them.":
                jump d3s3
            "I kind of regret that… but too late now…":
                jump d3s3
            "Gosh, what if they become {i}more{/i} insufferable?":
                jump d3s3
    else:
        show enzo_angry
        e "You're kidding me…"
        e "No offense, but it isn't your business."
        e "If she really feels that way, tell her to talk to me herself!"
        hide enzo_angry
        m "(Enzo left…)"
        m "(I wonder if I ruined things for Colette…)"
        m "(...maybe she dodged a bullet, actually.)"
        m "(Hard to say… I guess I don't really know Enzo that well after all.)"
    jump d3s3