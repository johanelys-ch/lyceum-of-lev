label D1S3s:
    label d1s3sz1:
        $ increase_affinity("Scylla", 1)
        m "(I went to the gym to watch practice. I'd watched practice after school before. It's fun to watch, and I'll do homework if no one I want to talk to is there.)"
        m "(Since Scylla kind of invited me, I decided to sit closer than I usually do.)"
        m "(I kind of wished I hadn't… Scylla seemed to be in the middle of a disagreement with her teammates... wait, are they twins?.)"
        show teammate_normal at right
        va "I don't remember this formation."
        show scylla_serious
        s "But it's the one we practiced last time! We spent time running through it."
        va "I didn't realize we were doing that today."
        s "We were talking about doing it all week!"
        show teammate_normal_c at left
        vb "Scylla, I have an idea for how to make it better."
        s "I mean, I'm open to ideas, but we still haven't really tried it to see if it works or not…"
        vb "Well, since Leira doesn't know it, I have this other thing we could try."
        va "Oh, show us!"
        hide teammate_normal
        hide scylla_serious
        m "(I don't know anything about volleyball, and I don't understand what they're talking about.)"
        m "(Scylla looked very frustrated throughout the rest of practice. I should say something.)"
        m "Hey, Scylla! How was practice?"
        show scylla_embarrassed
        s "Oh, [playerName]! Thanks for coming to- Leira!"
        s "Leira! The bus this weekend is at 9 am!"
        s "Sorry about that. I always have to remind her about these things. What did you say?" 
        show scylla_concerned
        s "Practice? Yeah, practice was… fine…"
        hide scylla_concerned

        menu:
            "Are you sure? You seem upset.":
                jump d1s3sz2
            "How are {i}you{/i}, though? You seem stressed.":
                jump d1s3sz3
            "Your teammates seemed kind of off today.":
                jump d1s3sz4
            "Your teammates are jerks!":
                jump d1s3sz5
            "You looked great out there!":
                jump d1s3sz6

    label d1s3sz2:
        show scylla_confused
        s "Sigh… is it that obvious?"
        s "It's fine."
        hide scylla_confused

    menu:
        "It's not fine for them to treat you like that!":
            jump d1s3sz8
        "You shouldn't put up with that!":
            jump d1s3sz9
        "But are {i}you{/i} fine?":
            jump d1s3sz9

    label d1s3sz3:
        $ increase_affinity("Scylla", 1)
        show scylla_confused
        s "I'm… ok. Annoyed, but ok."
        hide scylla_confused
        jump d1s3sz7

    label d1s3sz4:
        $ increase_affinity("Scylla", 2)
        show scylla_shocked
        s "Ha, today? They're always like that."
        s "No… that's mean. I shouldn't say that."
        hide scylla_shocked
        jump d1s3sz7

    label d1s3sz5:
        $ increase_affinity("Scylla", 1)
        show scylla_confused
        s "You could say that… They're not usually like {i}this{/i}."
        hide scylla_confused
        jump d1s3sz7

    label d1s3sz6:
        show scylla_surprised
        s "Thanks. You should come to the game. It's on… some day. I need to look it up."
        hide scylla_surprised
        jump d1s3sz13

    label d1s3sz8:
        show scylla_embarrassed
        $ increase_affinity("Scylla", 1)
        s "I guess you're right…"
        hide scylla_embarrassed
        jump d1s3sz7

    label d1s3sz9:
        show scylla_confused
        s "Probably not. But what am I gonna do? Join another volleyball team?"
        s "They're good friends most of the time. And it's only for another year anyway."
        hide scylla_confused
        jump d1s3sz7

    label d1s3sz7:
        show scylla_serious
        s "They're really good, but I do feel like they blow off my ideas."
        s "I don't think they do it on purpose or anything, but it's very frustrating."
        s "I can't tell if my ideas are bad or not because we never try them!"

        menu:
            "Have you talked to them about this?":
                jump d1s3sz10
            "Have you told them how this makes you feel?":
                jump d1s3sz11
            "Do you want me to tell Enzo to put the fourth chicken in Leira's locker?":
                jump d1s3sz12
            
    label d1s3sz11:
        $ increase_affinity("Scylla", 1)
        jump d1s3sz10

    label d1s3sz12:
        $ increase_affinity("Scylla", 1)
        show scylla_laugh
        s "HAHAHA!"
        s "Ah… but there {i}isn't{/i} a fourth chicken, is there?"
        m "Damn, that's deep."
        s "Why, thank you."
        hide scylla_laugh
        jump d1s3sz13

    label d1s3sz10:
        show scylla_smirk
        s "Not yet… I suppose I should. It's not sustainable like this, is it?"
        hide scylla_smirk
        jump d1s3sz13

    label d1s3sz13:
        show scylla_smile
        s "Well, I should get going. I have a bunch to do at home as well."
        s "Also... thanks for letting me vent. Sorry to dump all this on you!"
        s "See you in class tomorrow!"
        m "(...she keeps waving at me while she's leaving the gym.)"
        m "(She sure is enthusiastic… I wonder…)"
        hide scylla_smile
        # flash effect bc colette took a picture
        s "Ooooo this is a good one!"
        m "Of what?"
        show colette_laugh
        c "Of a {i}special moment{/i}. See for yourself!"
        m "Colette… look how far away we are! You got this as she was leaving!"
        c "Hm, so you don't deny it was a special moment…"
        m "Of her complaining about her teammates? Yeah, love is in the air."
        s "(...touché, Colette.)"
        hide colette_laugh
        jump D1S4