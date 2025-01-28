label D1S3r:
    label d1s3rz1:
        scene stairs
        show Roger

        m "(I did eventually run into Roger by the stairs. He noticed me, and he looked at me, but he didn't say anything.)" 
        "(Is he seriously just going to stare at me until I say something?)"
        "(Shoot… what did I want to talk to him about? Something about… anthropocentrism?)"

        menu:
            "You know, it's messed up how history only reflects one side.":
                jump d1s3rz2

            "People are going to think you're actually smart if you keep using words that no one understands.": 
                jump d1s3rz3

            "Are you always so passionate about history?":
                jump d1s3rz4

    label d1s3rz2:
        scene stairs

        r "Oh? A human that {i}isn't{/i} thoroughly brainwashed?"
        $ increase_affinity("Roger", 1)
        m "It's not that hard to notice. The whole anthropocentric media thing is pretty obvious."
        r "I guess so, but some of those poopies out there just don't have enough energy to think. Can't see what's right in front of them."
        m "And what about you? You think you're any different?"
        r "Me? Please. I'm {i}so{/i} different, I might as well be living on another planet. Poopies could never."
        m "(...)" 
        m "(Roger left without saying goodbye. It's hard to tell with Roger, but I don't think he was upset. I get the impression he just does that.)"
        m "(Also... poopies?)"
        jump d1s3rz5

    label d1s3rz3:
        scene stairs

        r "Well, then tell those people that there are free dictionaries in the library."
        $ decrease_affinity("Roger", 1)
        m "I was just saying, you might scare them off."
        r "Perfect! Less of you poopies to deal with."
        m "(Roger left without another word.)"
        m "(...he probably wouldn't want to hear that it's \"fewer of you poopies\"...)"
        m "(Also... poopies?)"
        jump d1s3rz5

    label d1s3rz4:
        scene stairs
        r "Well, if the topic at hand is worth my time, yes"

        menu:
            "And what kind of topic is worth your time?": 
                jump d1s3rz6
            "That's exactly how I see it. Want to study together?":
                jump d1s3rz8
            "...": 
                jump d1s3rz7

    label d1s3rz6:
        r "Anything that doesn't involve the brainless masses… the poopies."
        $ increase_affinity("Roger", 1)
        jump d1s3rz7

    label d1s3rz7:
        r "Well? Was there anything else? I've got places to be, buttface."
        m "(Roger left before I could say anything else.)"
        jump d1s3rz5

    label d1s3rz8:
        r "Why would I do that? So I can carry your dumb butt all semester?"
        m "Sometimes it's more effective to collaborate and learn together. And more fun."
        r "Yeah… no. You lost me at fun."
        $ decrease_affinity("Roger", 1)
        r "Actually you lost me way before that."
        r "But \"fun\" didn't help your case."
        r "I want you to know that."
        m "(Roger left without saying goodbye. Weirdly, I think that went… neutrally.)"

    label d1s3rz5:
        menu:
            "Well, that was... interesting…":
                jump d1s3rz9

            "Roger's definitely something else.":
                jump d1s3rz9

    label d1s3rz9:
        m "(Hang on… what's that on the floor? Did something fall out of Roger's bag?)"
        m "(I pick up a brochure for Vampire Academy and leaf through it quickly.)"
        m "(The number one monster history program in the country. Guess it's obvious why this is his top choice.)"
        m "(Gosh… they really do have a low acceptance rate… Roger's determined, if nothing else.)"
        m "(I can barely read his handwriting, but he does have notes scrawled all over this.)"
        m "(I should try to give it back. I wonder if I can catch him?)"
        m "Hey! Roger! You dropped- ACK!"
        # Some kind of flash effect for when Colette takes a photo of you
        r "[playerName]...?"
        m "You're holding out your hand for me… is this… a gesture of friendship…"
        show roger embarrassed
        r "N-no. You fell down the stairs is all…"
        show colette
        c "I got a great shot too!"
        m "...literally {i}why{/i}?"
        c "{size=*0.5}-crahhkerjknm so romantic ppplljghue-{/size}"
        m "(None of that made sense. I must be more injured than I thought.)"
        hide colette
        hide roger
        m "Hang on… I'm in the nurse's office?"
        show roger
        r "No doy. You fell down the stairs."
        m "And Roger's here too? Oh no, I'm hallucinating."
        show roger embarrassed
        r "{i}Obviously,{/i} I brought you here."
        r "{size=*0.5}I couldn't just leave you there...{/size}"
        r "The nurse said you'll be fine. You're just a little dizzy."
        m "(Roger got up to leave.)"
        m "Wait! This is yours!"
        m "(I reach into my pocket to grab the flier. I feel a lot better already, to my surprise…)"
        r "...you ran after me and fell down the stairs and got hurt just to give {i}this{/i} back to me?"

        menu:
            "It's no big deal. It was the decent thing to do.":
                jump d1s3rz10

            "Well, maybe if I knew I was going to {i}fall down the stairs…{/i}":
                jump d1s3rz11        

            "Anyone would have done it, even if you {i}are{/i} a poopface, Roger.":
                jump d1s3rz12

    label d1s3rz10:
        $ increase_affinity("Roger", 1)
        r "...thank you."
        jump d1s3rz13

    label d1s3rz11:
        # Neutral
        r "You're really bad at this whole \"graceful\" thing, huh?"
        jump d1s3rz13

    label d1s3rz12:
        $ increase_affinity("Roger", 1)
        r "...you're the poopface, poopface."
        jump d1s3rz13

    label d1s3rz13:
        m "(Roger looks perplexed. Did I give him the wrong thing?)"
        m "(No, it's definitely his brochure… He's fiddling with his watches...)"
        m "(Wait… how many watches is he wearing… {i}am{/i} I still hallucinating?)"
        r "...thank you. I have to go."
        m "(He ge`ts up but he pauses at the door.)"
        r "...I hope you feel better soon, poopface."
        m "(Roger leaves.)"
        m "(The nurse checks in on me again and clears me to go home too.)"

        # $ print(affinities["Roger"])
        # jump d2s4 still not implemented