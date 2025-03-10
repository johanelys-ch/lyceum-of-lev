label D1S2:
    label d1s2z1:
        show colette_smile
        c "[playerName]! What are you doing now?"
        m "I don't know yet. Although I really should start my college applications…"
        c "College! That's so funny!"
        c "Speaking of funny, Enzo and I are putting the finishing touches on a prank!"
        m "What a change of pace for Enzo."
        c "This one is so good though! Enzo is a {i}genius{/i}."
        c "They got three chickens, and we're going to make little volleyball team jerseys for them! But here's the best part! One will be numbered \"1\", another \"2\"..."
        m "Let me guess…"
        c "Oh, please do. You'll {i}never{/i} guess!"
        m "And the third one is numbered \"4\", so everybody will keep looking for the one with a \"3\", which doesn't exist."
        hide colette_smile
        show colette_shocked
        c "Whoa. You're a natural. How did you figure it out?"
        hide colette_shocked
        show colette_smile
        c "See? You're wasting your talent on college applications! You gotta come help!"
        m "...why would I want to do that?"
        c "Come on, best friend! It's fun!"
        c "...and we do need help making these little jerseys in time for next week's game."
        c "{size=*0.5}Wait, does Enzo even know how to sew?{/size}"
        c "But also, fun! You know, you could learn a thing or two about fun from Enzo!"
        m "(I bet Colette would like to learn a little something from Enzo. I don't think it's pranks...)"
        m "I can give you a solid maybe."
        c "I'll take it. We'll be in the home economics classroom! Come hang out!"
        hide colette_smile
        m "(That is surprising… I can't believe Enzo knows where the home ec classroom is.)"
        show scylla_concerned
        m "(Oh, Scylla's on the volleyball team. I wonder if I should… warn her?)"
        m "(Well, she noticed me staring at her, so I should at least say {i}something{/i}.)"
        hide scylla_concerned

        menu:
            "(I should give her a heads up about Enzo's prank.)":
                jump d1s2z2
            "(Maybe she likes pranks? I could subtly inquire…)":
                jump d1s2z3
            "(I'm overthinking it. Just say \"hi!\")":
                jump d1s2z4
            "(No, I should say \"hi\" in a {i}cool{/i} way.)":
                jump d1s2z5

    label d1s2z2:
        show scylla_smile
        m "Hey, Scylla. I think I should tell you something about Enzo-"
        s "Oh, hey, [playerName]. Are they doing the chicken prank again?"
        hide scylla_smile
        jump d1s2z6

    label d1s2z3:
        $ increase_affinity("Scylla", 1)
        show scylla_smile
        m "Hey, Scylla. What'd you think of class today?"
        s "What did {i}I{/i} think? I mean… it was fine. Monster history is always interesting."
        s "It's a… sad history."
        hide scylla_smile
        jump d1s2z6

    label d1s2z4:
        $ increase_affinity("Scylla", 1)
        show scylla_smile
        m "Hi, Scylla."
        s "Oh! Hey, [playerName]! What's up?"
        m "(...oh no, I still have to say things.)"
        m "(Crap.)"
        m "Uh, maybe you should know that Enzo's up to something…"
        s "Oh, are they doing the chicken prank again?"
        hide scylla_smile
        jump d1s2z6

    menu:
        "It's crazy there used to be monsters! Just walking around. Can you imagine?":
            jump d1s2z3a
        "History is always sad.":
            jump d1s2z3b
        "Yeah… but I bet there's still monsters out there somewhere.":
            jump d1s2z3c

    label d1s2z3a:
        show scylla_embarrassed
        s "It's certainly hard to, sometimes. Isn't it?"
        hide scylla_embarrassed
        jump d1s2z3d

    label d1s2z3b:
        show scylla_confused
        s "Hm, have you been spending time with Roger lately? Sounds like something he'd say."
        hide scylla_confused
        jump d1s2z3d

    label d1s2z3c:
        show scylla_embarrassed
        s "Perhaps you're right. It's hard to imagine they all just disappeared."
        hide scylla_embarrassed
        $ increase_affinity("Scylla", 1)
        jump d1s2z3d

    label d1s2z3d:
        show scylla_smile
        m "Well, I actually wanted to ask you about Enzo..."
        s "Oh, that goofball. They sure keep class interesting! It'll be strange next year going to school without them. I doubt Enzo's applying to Black Lagoon University."
        m "BLU? They have one of the best volleyball teams in the country!"
        s "They sure do!"
        hide scylla_smile
        show scylla _concerned
        s "Don't tell my parents, though…"
        hide scylla_concerned
        show scylla_embarrassed
        s "Um. But what about Enzo? Are they doing the chicken prank again?"
        hide scylla_embarrassed
        jump d1s2z6  

    label d1s2z5:
        m "Howdy, what's shakin'?"
        m "(Oh my god that was a mistake.)"
        m "(Good thing she didn't seem to notice.)"
        show scylla_surprised
        s "Oh! [playerName]! Sorry, did you say something?"
        m "...nope, nothing. How are you?"
        s "Whew… how am I?"
        s "..."
        hide scylla_surprised
        show scylla_embarrassed
        s "Sorry, I've been busy! I'm trying to remember what's all new!"
        s "Volleyball game this week… College applications… Family stuff…"
        s "The game should be… fine. I bet Enzo will do their chicken prank again, at least."
        hide scylla_embarrassed
        jump d1s2z6

    label d1s2z6:
        m "Oh, you already know?"
        m "... again?"
        show scylla_laugh
        s "Yeah, they did the same prank last year! Or, well, they tried to. Last year they used pigeons, but they just flew away."
        s "Honestly, I think {i}I{/i} suggested they use chickens next time."
        m "Huh, so it's no big deal then? You don't mind?"
        hide scylla_laugh
        show scylla_concerned
        s "Eh… I don't care."
        hide scylla_concerned
        show scylla_embarrassed
        s "Anyway, um, you should come watch practice! Lots of people watch us. No pressure!"
        s "Speaking of which, I gotta run. Nice talking with you, [playerName]!"
        hide scylla_embarrassed
        m "(Well, I guess I have two invitations then.)"
        m "(I could go see the prank that Colette and Enzo are working on.)"
        m "(Or I could go watch Scylla and the volleyball team practice.)"
        m "(Or I could stick around here and wait for Roger to show up. I could be interested in what's going on there…)"

        menu:
            "Go see Enzo and Colette":
                $ D1S3eB = True
                jump D1S3e
            "Go watch Scylla":
                $ D1S3sB = True
                jump D1S3s
            "Wait for Roger":
                $ D1S3rB = True 
                jump D1S3r