label d3s2s:
    m "(I caught up with Scylla after class.)"
    s "Hi, [playerName]. What'd you think of class today?"

    menu:
        "itwasfinedoyouwannagooutonadate":
            jump d3s2scalc
        "I have no idea. Hey, are you doing anything later? Would you like to go on a date?":
            jump d3s2scalc
        "That's not important. I have a confession to make… What do you think of going on a date?":
            jump d3s2scalc

label d3s2scalc:
    if check_affinity_flexible("Scylla", 6):

        label d3s2syes:
            $ increase_affinity("Scylla", 1)
            s "Wha- with {i}me{/i}? I… wow… I mean, I'd love to!"
            s "Wow. Let me think. Ohhh… oh no, I have practice today. Well, not practice, technically, but I'm supposed to…"
            s "..."
            s "...You know what?"
            s "Yes. Tonight is good."
            m "That's great! But you're sure tonight works for you?"
            s "Yeah. I don't need to do this for the team. Leira and Carmilla can do it themselves. It's not even my responsibility."
            s "This is more important to me."

        menu: 
            "Wow, I'm proud of you!":
                jump d3s2sproud
            "Is it selfish of me to say I was hoping you'd say that?":
                jump d3s2sselfish
            "Great. The hell with them.":
                jump d3s2sheck

        label d3s2sproud:
            show scylla blush
            s "ohmygoddon'tsaythat"
            jump d3s2smind

        label d3s2sselfish:
            $ increase_affinity("Scylla", 1)  
            show scylla smirk
            s "Hmm I think I just might be ok with it."
            jump d3s2smind

        label d3s2sheck:
            $ decrease_affinity("Scylla", 1)  
            s "Oh hush, it's not {i}that{/i} big a deal…"
            jump d3s2smind

        label d3s2smind:
            s "Did you have something in mind?"
            m "Well… this might sound stupid, but I've heard there's a nice spot in the forest…"
            s "Oh! You've heard about {i}that{/i}?"
            m "Have you?"
            s "Hmmm… well, I should hope so."
            s "I'll explain later! I'm looking forward to it."
            s "See you after class…"
            $ dS = True
            jump d3s3

    else:
        label d3s2sno:
            s "Huh? With… {i}me{/i}?"
            s "I'm… flattered."
            s "But I can't tonight. I have practice."
            s "Maybe some other time? Sorry, I gotta go…"
            m "(She ran off…)"
            m "(I guess I misread that one…)"
            $ dC = True
            jump d3s3