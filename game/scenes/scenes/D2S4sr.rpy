label D2S4sr:
    m "(After class, I ran into Scylla and Roger having an argument on the stairs.)"
    m "(Roger looked upset. Scylla just looked annoyed.)"
    show roger_concerned at right
    show scylla_anger at left
    s "Look, I'm sorry I asked. You could just say no."
    r "It's the principle of the thing! You're just perpetrating these societal norms that are all poopy!"
    s "That's more than a little unfair. And it's \"perpetuating\", genius."
    r "...well, you know what I meant. It doesn't magically make my point not true just because I misspoke."
    m "(They just noticed me. What did I just walk in on?)"
    s "[playerName], I'm sorry you have to see this pointless debate."
    r "It's not a debate if you're just wrong."
    s "Roger, this is a fight over nothing. I bet [playerName] could see that."
    r "Well, of course that poop-for-brains will take {i}your{/i} side."
    s "Oh? I thought there were no sides because I'm just a complicit moron who was always wrong all the time."
    s "I don't have time for this! It's a fight over nothing!"
    s "Roger's telling me that {i}I'm{/i} \"perpetuating\" oppressive social norms by playing {i}volleyball{/i}."
    m "...volleyball?"
    r "It just enshrines a societal norm that there's a \"normal\" height. It's discrimination!"
    hide scylla_anger
    hide roger_concerned

    menu:
        "You might be overreacting, Roger.":
            jump D2S4sr2
        "He might have a point, Scylla.":
            jump D2S4sr3
        "Oh my god, who cares? It's just a dumb game.":
            jump D2S4sr4

label D2S4sr2:
    $ decrease_affinity("Roger", 1)
    $ increase_affinity("Scylla", 2)
    show roger_confused
    r "Big surprise. Why do I even bother?"
    hide roger_confused
    m "(Roger stormed off.)"
    show scylla_confused
    s "Ughhhhhhhhh! I {i}can't{/i} with this sort of stuff! Like this is {i}my{/i} fault?"
    hide scylla_confused
    $ D2S4rB = True
    jump d2s5sz1

label D2S4sr3:
    $ decrease_affinity("Scylla", 1)
    $ increase_affinity("Roger", 2)
    show roger_smirk
    r "Wow, must feel bad when even the poopies can tell you're full of poop."
    hide roger_smirk
    show scylla_confused
    s "This has been such a waste of time."
    hide scylla_confused
    m "(Scylla stormed off.)"
    show roger_smirk
    r "Well, well, well, [playerName]... perhaps you have some worth after all…"
    hide roger_smirk
    jump D2S5rz1

label D2S4sr4:
    $ decrease_affinity("Roger", 1)
    $ decrease_affinity("Scylla", 1)
    show roger_concerned at right
    show scylla_anger at left
    s "See? It's just a dumb game. You're dumb for caring. I'm dumb for caring. Everything is dumb."
    r "No surprises. Neither of you see an issue because it doesn't affect you personally."
    m "(They both glared at each other before walking off in opposite directions.)"
    m "(...What just happened?)"
    m "(That was... tense.)"
    m "(I guess I should probably go after one of them to make sure they're ok…)"
    hide scylla_anger
    hide roger_concerned

    menu: 
        "Scylla":
            $ D2S4rB = True
            jump d2s5sz1
        "Roger":
            jump D2S5rz1