label D1S3e:
    label d1s3ez1:
        scene bg classroom
        m "(I went to the home economics classroom.)"
        show colette_shocked
        c "Oh my god, you actually came! I didn't think you would!"
        c "...Enzo, don't."
        hide colette_shocked
        show enzo_smirk
        e "I didn't even have to say it."
        e "Well hello, [playerName]. What a lovely surprise!"
        e "Did you come to join the fun?"
        hide enzo_smirk

        menu: 
            "What exactly are you doing?":
                jump d1s3ez2
            "Fun? Yes, please. I've been dying for some fun.":
                jump d1s3ez3
            "I came to put a stop to this.":
                jump d1s3ez4
            "I came to put a stop to this… this prank will get {i}nowhere{/i} if I don't help immediately.":
                jump d1s3ez5

    label d1s3ez2:
        show enzo_smile at left
        e "Arson. What does it look like we're doing? We're making little jerseys for chickens in time for the big game."
        e "It's not exactly rocket science."
        m "(Sure enough, Enzo already has one little, chicken-sized volleyball jersey. And they're halfway through another.)"
        m "(I can't help but wonder if Enzo learned how to sew just for this prank…)"
        show colette_awe at right
        c "Can't you see it now? The little chickens…"
        c "In their little jerseys!"
        e "Doesn't that sound exciting?"
        m "Didn't you do this same prank last year?"
        e "That's why it's so good! {i}No one{/i} will expect it to happen a {i}second{/i} time!"
        hide colette_awe
        hide enzo_smile

    menu: 
        "You'll really get 'em good next year when it happens a third time.":
            jump d1s3ez2a
        "Are you going to teach the chickens how to play volleyball too?":
            jump d1s3ez2b
        "But won't this ruin the game? The team works hard too!":
            jump d1s3eruin


    label d1s3ez2a:
        $ increase_affinity("Enzo", 1)
        show enzo_smirk
        e "If only I could be around to see it…"
        e "But that only strengthens my resolve! I have a legacy to consider!"
        e "Come, [playerName]. Join us. Let us become as {i}gods{/i} in the history of high school pranks."
        hide enzo_smirk

    menu: 
        "I hadn't thought of it that way…":
            jump d1s3ez4b
        "I guess it'd be cool if Ms. Lalonde had to teach the next generation about us.":
            jump d1s3ez2c
        "I'm still worried this is just going to ruin the game.":
            jump d1s3eruin
        "Which god will you be? The god of chicken feces?":
            jump d1s3epooper

    label d1s3ez2b:
        show enzo_smile at left
        show colette_smile at right
        e "Come on, that's just ridiculous. Now come help us sew these tiny little chicken jerseys together!"
        c "Come on, [playerName]! It'll be fun! No one's going to get hurt or anything."
        c "Why don't you just blow off some steam before cracking down on those college applications?"
        e "Yeah! Come on, college! Helping us would actually make you a more well-rounded applicant, if you think about it."
        hide colette_smile
        hide enzo_smile

    menu: 
        "I hadn't thought of it that way…":
            jump d1s3ez4b
        "I'm worried this is just going to ruin the game.":
            jump d1s3eruin
        "I assume you're going to clean up after the chickens poop everywhere, right?":
            jump d1s3epoop


    label d1s3ez2c:
        $ increase_affinity("Enzo", 2)
        show enzo_surprise
        e "Could I even dare to dream that big…"
        hide enzo_surprise
        jump d1s3ez6

    label d1s3ez3:
        show enzo_smile at left
        show colette_smile at right
        e "Delightful."
        $ increase_affinity("Enzo", 1)
        c "(z-snaps)"
        e "Welcome aboard, [playerName]. It is [playerName], right? Colette talks about you a lot, but we've not really spent much time together."
        c "(z-snaps)"
        e "I take it that's a yes."
        hide colette_smile
        hide enzo_smile
        m "(While Enzo and Colette do their Enzo and Colette thing, I take a look at what they've done so far.)" 
        m "(Sure enough, Enzo already has one little, chicken-sized volleyball jersey. And they're halfway through another.)"
        m "(I can't help but wonder if Enzo learned how to sew just for this prank…)"

    menu:
        "That's… impressive, actually.":
            jump d1s3ez4b
        "Honestly, I love it. But shouldn't you do it for, you know, {i}not{/i} a home game?":
            jump d1s3ez5a
        "But won't this ruin the game? The team works hard too!":
            jump d1s3eruin
        "So, I can't help but notice there's a chicken missing.":
            jump d1s3ez5b

    label d1s3ez4:
        show enzo_smirk
        e "Ahh, well, Colette and I will just continue as we were. Hang around if you like. I do love an audience!"
        m "...didn't you hear me?"
        e "Dearest [playerName], we've come too far to turn back now!"
        e "Look how hard I've worked on this!"
        hide enzo_smirk
        m "(Sure enough, Enzo already has one little, chicken-sized volleyball jersey. And they're halfway through another.)"
        m "(I can't help but wonder if Enzo learned how to sew just for this prank…)"

    menu:
        "That's… impressive, actually.":
            jump d1s3ez4b
        "But won't this ruin the game? The team works hard too!":
            jump d1s3eruin
        "I'm not kidding. This is wrong.":
            jump d1s3epooper

    label d1s3ez5:
        show enzo_smile
        e "Now it's a {i}surprising{/i} surprise."
        $ increase_affinity("Enzo", 2)
        hide enzo_smile
        show colette_laugh
        c "Heck yeah, [playerName] has come to {i}play{/i}."
        hide colette_laugh
        show enzo_confused
        e "Tell me. Where do you see room for improvement?"
        hide enzo_confused
        m "(I look around the room. It's definitely the prank Colette described.)" 
        m "(Enzo already has one little, chicken-sized volleyball jersey. And they're halfway through another.)"
        m "(I can't help but wonder if Enzo learned how to sew just for this prank…)"

    menu:
        "Honestly, I love it. But shouldn't you do it for, you know, {i}not{/i} a home game?":
            jump d1s3ez5a
        "So, I can't help but notice there's a chicken missing.":
            jump d1s3ez5b
        "How married are you to chickens? Won't they create… a mess…?":
            jump d1s3epoop
        "This seems complicated. Can't we ruin the game by just setting a fire somewhere?":
            jump d1s3eruin

    label d1s3ez5a:
        show enzo_embarrassed
        e "Huh. That isn't a bad point."
        $ increase_affinity("Enzo", 1)
        e "I'm not such a fool as to think I have no room for personal development."
        e "Tell you what, though… next time? Prank happens at the {i}other{/i} school."
        e "I… must admit I have a bit of a deadline vis a vis the chickens…"
        hide enzo_embarrassed
        show colette_serious
        c "Yeah, how much longer do I have to keep them at my house?" 
        c "They are {i}not{/i} easy to clean up after, and I think my parents are starting to get suspicious."
        hide colette_serious
        jump d1s3ez6

    label d1s3ez5b:
        show colette_laugh
        c "...that's the joke, [playerName]! I thought you were better than this."
        m "But… but, doctor, {i}I{/i} was joking."
        hide colette_laugh
        show enzo_smirk
        e "Bold of you to come into my place of work and tell me how to do my job, [playerName]."
        m "(They're not {i}really{/i} mad at me. Actually, I think that they're… hm…)"
        m "Okay. You got me. I can't make sense of your scheme. It's beyond me."
        hide enzo_smirk
        jump d1s3ez4c

    label d1s3ez4b:
        show enzo_laugh
        e "I knew you could be corrupted."
        hide enzo_laugh
        $ increase_affinity("Enzo", 1)
        jump d1s3ez6

    label d1s3eruin:
        show enzo_embarrassed at left
        show colette_embarrassed at right
        e "Who said anything about ruining the game? We're just complementing the game!"
        c "Yeah! It's a compliment!"
        m "That's not what that… never mind…"
        e "Think of it as a message for the world to see."
        m "...the {i}chickens{/i} are a message?"
        hide colette_embarrassed
        hide enzo_embarrassed
        show enzo_smile
        e "Consider the volleyball players. What drives them to volley the ball?"
        e "If it weren't for the volley, whenceforth the ball? Forsooth, our paths are twixt."
        e "As the volleyballers tell the world, \"Look, world! Here we are, volleying!\", mustn't we all speak our truth?"
        hide enzo_smile

    menu: 
        "Ok, parts of that made sense, I guess.":
            jump d1s3ez4a
        "I still don't see what the chicken's truth is.":
            jump d1s3ez4c
        "Is this… an environmental thing? I'm lost.":
            jump d1s3ez4c
        "No, you're wrong, and I {i}will{/i} die on this hill. I'm getting a teacher.":
            jump d1s3epooper

    label d1s3ez4a:
        show enzo_smile
        e "That's {i}exactly{/i} the right amount."
        $ increase_affinity("Enzo", 1)
        e "It wouldn't be funny if it made more sense, you know?"
        hide enzo_smile
        show colette_laugh at right
        show enzo_laugh at left
        c "Yes, [playerName]... Turn off your brain…"
        e "Turn it off…"
        c "Offffffffffff…"
        m "Oh my god, I'll help if you just stop talking."
        e "..."
        m "(Fair enough.)"
        c "Thank you, best friend!"
        hide colette_laugh
        hide enzo_laugh
        jump d1s3ez6

    label d1s3ez4c:
        show enzo_serious
        e "Ha! Don't worry. It'll all make sense in time."
        e "I assume if you're still here by this point, you intend to help."
        hide enzo_serious
        show colette_angry
        c "Sure [playerName] is!"
        c "And I won't hear a word otherwise."
        hide colette_angry
        jump d1s3ez6

    label d1s3epoop:
        show enzo_confused
        e "Hm…"
        m "(Enzo seems deep in thought.)"
        m "(It makes me nervous.)"
        e "Colette… how would you describe your experience with the chickens, poop-wise?"
        hide enzo_confused
        show enzo_confused at left
        show colette_concerned at right
        c "...bad."
        e "Funny bad or bad bad?"
        m "I'm just saying, is the prank still funny if it's just creating more work for the custodial staff?"
        hide enzo_confused
        hide colette_concerned
        show enzo_smirk at left
        show colette_confused at right
        e "Oh, no, I'm {i}assuming{/i} I'll get caught and cleanup will be my punishment."
        e "I'll have to sleep on whether I'm overestimating how much chickens can poop."
        e "Can't say I've thought about it before."
        c "{size=*0.5}I have thought about chicken poop {i}extensively{/i} in recent days…{/size}"
        e "I'm no sociopath. I'll take the poop on the chin."
        c "Ew, please don't…"
        e "Metaphorically."
        hide colette_confused
        hide enzo_smirk

    menu: 
        "Alright, then I have no objections. Let's bring the chicken team together.":
            jump d1s3ez4b
        "Ok. I'm not gonna say anything, but I was never here.":
            jump d1s3ez6
        "Look, I can't let this happen. I'm getting a teacher.":
            jump d1s3epooper


    label d1s3epooper:
        $ decrease_affinity("Enzo", 1)
        show enzo_angry at left
        show colette_serious at right
        e "I see, in that case, I suppose we must all go our separate ways. I love an audience… but a critic? Not so much."
        c "Don't be a party pooper, [playerName]!"
        m "(Out of nowhere, Enzo clasps my hand.)"
        e "We'll always have Paris."
        m  "(Enzo and Colette left.)"
        hide colette_serious
        hide enzo_angry

    label d1s3ez6:
        show enzo_smirk
        e "I'm ok to keep working on the jerseys…"
        m "(I look down. Somehow they've already completed the second jersey in the time we've been talking.)"
        e "Colette, would you show our newest ne'er-do-well the necessary…"
        show enzo_confused
        e "...needed things…"
        e "Ok, that one got away from me."
        e "I can't be on the clock all the time."
        hide enzo_confused
        hide enzo_smirk
        show colette_smile
        c "We're just cutting out the numbers and attaching them to the jerseys."
        c "I'm doing this job because I'm the one who's good at math."
        m "(I barely helped at all, Enzo was so fast at everything.)"
        m "(Did they really get this good at a new skill just for a prank?)"
        # flash effect bc colette took a picture
        c "Oooo… this is a cute photo of you two making these little jerseys!"
        c "Ugh, wait… I can't use this at tomorrow's art show! That'll give away the prank!"
        m "Colette! I look terrible!"
        m "Worse, I look like I'm not even helping! I'm just staring while Enzo does all the work!"
        hide colette_smile
        show enzo_smile
        e "Nonsense! You're invaluable! Thanks for your help today, [playerName]."
        e "Really! I'm glad to finally get to spend some time with you!"
        m "Charmed, I'm sure."
        hide enzo_smile
        show enzo_embarrassed at left
        show colette_serious at right
        c "Ok, lovebirds, calm down."
        m "(...I can't help but notice Enzo had nothing witty to say about {i}that{/i}.)"
        m "(Hmmm…)"
        hide colette_serious
        hide enzo_embarrassed

        jump D1S4
