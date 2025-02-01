label D3S2rz1:
    scene bg_hallway with dissolve
    m "(Alright, deep breaths. I've got to ask Roger out… but knowing him, this might not go as planned.)"
    m "(Still, I've got to try.)"
    m "Hey, Roger. So, I was thinking… maybe we could hang out sometime?"
    show roger_confused
    m "(Roger simply stares at me with an inscrutable expression. Maybe that's good?)"
    m "Like, you know…just the two of us?"
    r "Hang out? You mean, like, a date? With me?"
    hide roger_confused

    menu:
        "Yeah, a date. What do you say?":
            jump D3S2rz2

        "No, no! I mean… yeah, maybe?":
            jump D3S2rz3

label D3S2rz2:
    if check_affinity_flexible("Roger", 6):
        show roger_surprise
        r "Pfft. What's wrong with you, poopie? Did you hit your head or something?"
        m "(...)"
        show roger_smirk
        r "...Alright, fine. If you're that desperate to waste your time with me, I guess I can grace you with my presence."
        r "It could be amusing."
        hide roger_smirk
        jump D3S2rz4

        label D3S2rz3:
            show roger_smile
            r "You've got a funny way of saying you want to go on a date with me, poopie."
            r "But fine, I'll humor you. Just don't get weird about it."
            hide roger_smile
            jump D3S2rz4

        label D3S2rz4:
            show roger_smile
            r "But don't think I'm doing this for free! You're responsible for buying all the snacks. And I'm not sitting through any mushy garbage, got it?"
            m "(Wait, did he just say yes? {i}The{/i} Roger said yes?)"
            hide roger_smile

            menu:
                "Okay! Sure, I'll bring the snacks. Any preferences?":
                    jump D3S2rz5

                "Fine, but you'd better not complain about the snacks I pick.":
                    jump D3S2rz6

        label D3S2rz5:
            show roger_concerned
            r "Yeah, just bring one of everything. You poopies are good at that kind of thing."
            hide roger_concerned
            jump D3S2rz7

        label D3S2rz6:
            $ increase_affinity("Roger", 1)  
            show roger_concerned
            r "Picky? Me? You're the one trying to impress me here, poopie! Don't forget about that."
            hide roger_concerned
            jump D3S2rz7

        label D3S2rz7:
            show roger_blush
            r "Oh, last but not least, don't look so happy about it, it's… weird."
            m "(That's the closest I'll get to enthusiasm from him…and I'll take it!)"
            m "(The audacity to call me weird while he looks like a tomato...)"
            m "(...and from someone who, as far as I can tell, thinks that \"poopie\" is actual profanity.)"
            m "(...why does this work for me exactly?)"
            show roger_concerned
            r "So where are we going? What's your brilliant idea this time?"
            r "Another trip to the arcade? A bowling alley? An amusement park?"
            m "Well, even if you're making fun of it, wouldn't it still count as an amusement park? Since you're all {i}amused{/i}?"
            m "I'm messing with you, it's not that."
            m "(Roger looks appalled, but in a… friendly way?)"
            m "No, something with fewer humans, since I know how you feel about those. I've heard about this spot in the forest…"
            show roger_awe
            m "(Huh, suddenly Roger looks {i}fascinated{/i}. What is this forest spot Colette told me about???)"
            show roger_smirk
            r "Heh."
            r "Well, you're more perceptive than the average human aren't you?"
            m "I guess? Honestly, Colette told me about it…"
            r "Oh, I assumed."
            m "(He doesn't seem upset by my admission that it's not an original idea…)"
            m "(Is this one of Colette's pranks? No… even if Roger secretly hates me… he hates pranks even more.)"
            r "I guess I'll see you there tonight."
            m "On our date."
            r "...right."
            hide roger_blush
            hide roger_awe
            hide roger_concerned
            hide roger_smirk
            m "(Roger ran away.)"
            m "(Nervous energy, I guess.)"
            $ dR = True
            jump d3s3
    else:
        show roger_confused
        r "What? A date? With you?"
        m "Yeah, a date. What do you say?"
        r "Do I look like the kind of guy who does dates? Newsflash, poopie: I don't."
        m "(Ouch. That was harsh...)"
        m "Are you sure? It could be fun."
        show roger_angry
        r "Do I look like the kind of guy who'd date someone like {i}you{/i}?"
        r "Nope. I've got better things to do. Like... literally anything else."
        m "Okay... sorry for bothering you."
        r "Yeah, yeah. Now get lost, poopie."
        hide roger_confused
        hide roger_angry
        m "(I should've known better...)"
        $ dC = True
        jump d3s3