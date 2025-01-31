label D2S4es:
    m "(After class, I ran into Scylla and Enzo.)"
    m"(They usually get along just fine, but something seemed tense.)"
    show scylla_confused at left
    show enzo_serious at right
    s "I'm sorry, I just don't think this one's fun."
    s "The chickens? Hilarious. This one? I dunno. I just don't wanna do it."
    e "But it was your idea!"
    s "\"Was.\" Colette totally changed it. That's fine. Maybe it {i}is{/i} better. But that doesn't mean I still care about it."
    e "And you're out because you're, what, pouting?"
    s "No, I'm out because nobody wanted my input."
    s "Don't say it's not true. You always put Colette's feelings above everyone else's."
    s "I know the lay of the land."
    show scylla_surprised at left
    show enzo_surprise at right
    m "(They just noticed me. What did I just walk in on?)"
    m "(Ohhhh this is so awkward.)"
    show scylla_confused at left
    show enzo_smirk at right
    e "Maybe a neutral third party can weigh in on which version of the prank is best?"
    s "Enzo, that's not what I'm upset about. I don't care about one prank."
    e "Tell me, [playerName]. What's funnier? A surprise disco party? Or graffiti?"
    s "That's not even a fair way to put it. My idea was to leave a message."
    s "The sort of thing you claim to care about until your girlfriend has a better idea."
    e "Girlfriend? Now who's being unreasonable?"

    menu:
        "Scylla, Enzo might have a point about the prank being funnier now.":
            jump D2S4es3
        "Enzo, Scylla might have a point about the old prank being more meaningful.":
            jump D2S4es4
        "Enzo, I think Scylla's saying she's upset about how you treat her, not about the prank.":
            jump D2S4es2
        
    label D2S4es2:
        $ increase_affinity("Scylla", 2)
        show scylla_blush at left
        show enzo_embarrassed at right
        s "Thank you. I thought I was going crazy."
        e "…fine. I'm sorry."
        e "I was being a jerk. Next time, I promise I'll-"
        s "Like there's going to be a next time. Why would I bother?"
        hide scylla_blush
        show enzo_embarrassed
        m "(Scylla stormed off…)"
        e "I'll be fine. You should go after her."
        e "I think she'd prefer some [playerName] magic over some Enzo magic at the moment."
        hide enzo_embarrassed
        $ D2S4eB = True
        jump d2s5sz1


    label D2S4es3:
        $ increase_affinity("Enzo", 2)
        $ decrease_affinity("Scylla", 1)
        show scylla_concerned at left
        show enzo_smile at right
        e "See? It's nothing personal! I'm just the expert."
        e "Tell you what… next time, I promise I'll-"
        s "Like there's going to be a next time. Why would I bother?"
        hide scylla_concerned
        show enzo_confused
        m "(Scylla stormed off…)"
        e "Everyone's a critic…"
        e "What? It's not my fault she can't handle feedback."
        m "Is that really what happened here?"
        e "..."
        e "Ok… maybe I'm… not blameless…"
        e "Ugh."
        m "(Enzo stormed off. I decided to go after them.)"
        hide enzo_confused
        jump D2S5ez1


    label D2S4es4:
        show scylla_concerned at left
        show enzo_confused at right
        e "Hmph. Amateurs, all of you."
        s "Sorry to upset the expert. Do whatever you want. I don't care."
        m "(Both of them stormed off in opposite directions.)"
        m "(...What just happened?)"
        m "(That was... tense.)"
        m "(I guess I should probably go after one of them to make sure they're ok…)"
        hide scylla_concerned
        hide enzo_confused

        menu: 
            "Scylla":
                $ D2S4eB = True
                jump d2s5sz1
            "Enzo":
                jump D2S5ez1
