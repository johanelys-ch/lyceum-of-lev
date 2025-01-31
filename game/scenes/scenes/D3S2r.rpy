label D3S2rz1:
    m "(Alright, deep breaths. I've got to ask Roger out… but knowing him, this might not go as planned.)"
    m "(Still, I've got to try.)"
    m "Hey, Roger. So, I was thinking… maybe we could hang out sometime?" 
    m "(Roger simply stares at me with an inscrutable expression. Maybe that's good?)"
    m "Like, you know…just the two of us?"
    r "Hang out? You mean, like, a date? With me?"

    menu:
        "Yeah, a date. What do you say?":
            jump D3S2rz2

        "No, no! I mean… yeah, maybe?":
            jump D3S2rz3

label D3S2rz2:
    if check_affinity_flexible("Roger", 6):
        r "Pfft. What's wrong with you, poopie? Did you hit your head or something?"
        m "(...)"
        r "...Alright, fine. If you're that desperate to waste your time with me, I guess I can grace you with my presence."
        "It could be amusing."
        jump D3S2rz4


label D3S2rz3:
    r "You've got a funny way of saying you want to go on a date with me, poopie."
    r "But fine, I'll humor you. Just don't get weird about it."
    jump D3S2rz4

label D3S2rz4:
    r "But don't think I'm doing this for free! You're responsible for buying all the snacks. And I'm not sitting through any mushy garbage, got it?"
    m "(Wait, did he just say yes? {i}The{/i} Roger said yes?)"

    menu:
        "Okay! Sure, I'll bring the snacks. Any preferences?":
            jump D3S2rz5

        "Fine, but you'd better not complain about the snacks I pick.":
            jump D3S2rz6

label D3S2rz5:
    "Yeah, just bring one of everything. You poopies are good at that kind of thing."
    jump D3S2rz7

label D3S2rz6:
    $ increase_affinity("Roger", 1)  
    r "Picky? Me? You're the one trying to impress me here, poopie! Don't forget about that."
    jump D3S2rz7

label D3S2rz7:
    r "Oh, last but not least, don't look so happy about it, it's…weird."
    m "(That's the closest I'll get to enthusiasm from him…and I'll take it!)"
    m "(The audacity to call me weird while he looks like a tomato...)"
    m "(...and from someone who, as far as I can tell, thinks that \"poopie\" is actual profanity.)"
    m "(...why does this work for me exactly?)"
    r "So where are we going? What's your brilliant idea this time?"
    r "Another trip to the arcade? A bowling alley? An amusement park?"
    m "Well, even if you're making fun of it, wouldn't it still count as an amusement park? Since you're all {i}amused{/i}?"
    m "I'm messing with you, it's not that."
    m "(Roger looks appalled, but in a… friendly way?)"
    m "No, something with fewer humans, since I know how you feel about those. I've heard about this spot in the forest…"
    m "(Huh, suddenly Roger looks {i}fascinated{/i}. What is this forest spot Colette told me about???)"
    r "Heh."
    r "Well, you're more perceptive than the average human aren't you?"
    m "I guess? Honestly, Colette told me about it…"
    r "Oh, I assumed."
    m "(He doesn't seem upset by my admission that it's not an original idea…)"
    m "(Is this one of Colette's pranks? No… even if Roger secretly hates me… he hates pranks even more.)"
    r "I guess I'll see you there tonight."
    m "On our date."
    r "...right."
    m "(Roger ran away.)"
    m "(Nervous energy, I guess.)"
    $ dR = True
    jump d3s3


    jump d3s3