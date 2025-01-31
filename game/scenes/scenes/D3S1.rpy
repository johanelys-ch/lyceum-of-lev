label D3S1:

# maybe just a title card of some kind saying "DAY 3" or something, so we don't need to narrate "and then it was the next day"

# just PC and colette in the hallway before class
    m "(The first thing I did at school the next day was find Colette and tell her everything.)"
    c "Interesting…"
    c "...was that a date?"
    m "I don't know! I wanted to ask you that!"
    m "...oh my god, do you think {i}they{/i} thought it was a date?"
    c "Ok, calm down. You can fix this…"
    c "Because there's nothing to fix!"
    m "Huh?"
    c "It sounds like it's going well, you buffoon! Just ask them out."
    m "(The words landed like a foreign language.)"
    m "(I understood it in theory, like vocabulary I'd read in a textbook. But hearing it out loud, I had no idea what it meant.)"
    c "Hmmmmm. You know what…"
    m "(Colette looked at me. She looked surprisingly thoughtful.)"
    c "Yes… yes, I think you should…"
    m "Should what?"
    c "Why don't you ask your special friend to go to the forest after school?"
    m "...the forest?"
    c "Yeah! Don't you know? It's {i}the{/i} hot spot for only the coolest young teens."
    m "..........the forest?"
    c "There's a special spot in there. It's like a hidden little nook, with… well, I don't want to spoil the surprise."
    c "Just ask them. I think they'll know exactly what it is."

    menu: 
        "Ok. Just asking them to a cool spot in the forest. Alone. And they won't think I'm going to murder them?":
            jump d3s1a
        "Am I still asking them out if I told them my best friend told me to ask them to take me somewhere?":
            jump d3s1b
        "I have no questions about this plan at all. How's my breath?":
            jump d3s1c
    # can we code in a fourth option that only appears if top affinity is enzo?
        "And… {i}you're{/i} cool with… you know?":
            jump d3s1enzo

    label d3s1a:
        c "...maybe find a less creepy way to say it."
        jump d3s1d

    label d3s1b:
        c "Nobody does anything in this life alone, champ."
        jump d3s1d

    label d3s1c:
        c "Confident [playerName]... I like this version of [playerName]..."
        jump d3s1d

    label d3s1enzo:
        c "I think so. At the end of the day, I care so much about both of you."
        c "I'm being sappy, and this won't last long, so pay attention."
        c "I think you two could be great for each other. I don't want to get in the way of that."
        c "I'm not {i}that{/i} self-centered."
        c "You're good, best friend. I promise."
        jump d3s1d

    label d3s1d:
        c "It'll be fiiiiine."
        c "You got this, best friend."
        # lil time skip
        m "(I could barely pay attention in class. I was shaking with nervous energy.)"
        m "(Moment of truth… after class, I'm asking out…)"

    menu:
        "Enzo":
            jump d3s2e
        "Scylla":
            jump d3s2s
        "Roger":
            jump D3S2rz1
        "No one… there's someone else I need to talk to…":
            jump d3s1bff

    label d3s1bff:
        c "Hm? [playerName], isn't there someone else you're supposed to be talking to right now?"
        m "I decided not to."
        c "I see…"
        c "Say no more."
        c "Tell you what. How about you and I go?"
        c "Not like a date!"
        c "Let's just celebrate our friendship. High school won't last forever. I want to focus on the people who matter."
        c "Also, I feel like I got you all worked up about some big secret, after all!"
        jump D3S4c