label d2s5sz1:
    scene bg_gym with dissolve
    $ increase_affinity("Scylla", 2)
    if D2S4rB:
        show scylla_embarrassed
        s "Thanks for sticking up for me back there. I'm stressed out enough as it is without Roger's… Rogerness."
        hide scylla_embarrassed
        jump conv
    elif D2S4eB:
        show scylla_embarrassed
        s "Thanks for sticking up for me back there. Enzo's just… they gotta learn you can't always make everybody happy."
        hide scylla_embarrassed
        jump conv

label conv:
    show scylla_surprised
    s "You'll be happy I put my foot down somewhere, though."
    s "I did have a talk with my teammates about how they're treating me and my ideas too, but it didn't go very well."
    s "Carmilla kept talking about her own strategies. She barely apologized for talking over mine."
    s "And Leira just said that she wasn't interested in my ideas! Just like that!"
    m "Oh no… I'm sorry, Scylla…"
    hide scylla_surprised

    menu:
        "Are you going to quit?":
            jump d2s5sz9
        "Did they offer you {i}anything{/i}?":
            jump d2s5sz3
        "Maybe Roger should take your place at the next game…":
            jump d2s5sz4

label d2s5sz2:
    show scylla_concerned
    s "No… I still love playing volleyball, even if I don't want to spend time with my teammates right now."
    hide scylla_concerned
    jump d2s5sz6

label d2s5sz3:
    $ increase_affinity("Scylla", 1)
    show scylla_concerned
    s "Yeah. Don't get me wrong. They didn't, you know, {i}not{/i} care."
    s "Carmilla said she wants to help work on my ideas with me."
    s "And Leira said she'd be more honest with me instead of pretending she forgot…"
    s "I don't really believe any of that will actually happen, though."
    hide scylla_concerned
    jump d2s5sz6

label d2s5sz4:
    $ increase_affinity("Scylla", 1)
    show scylla_smile
    s "Well, that'd totally solve all my problems."
    hide scylla_smile

    menu: 
        "Maybe these aren't {i}your{/i} problems.":
            jump d2s5sz8
        "Do you want to cause them {i}more{/i} problems?":
            jump d2s5sz7
        "Did you all talk about any solutions?":
            jump d2s5sz3

label d2s5sz7:
    $ decrease_affinity("Scylla", 1)
    show scylla_confused
    s "I mean, I'm feeling petty, but I don't think that approach would be productive."
    hide scylla_confused
    jump d2s5sz2

label d2s5sz8:
    show scylla_confused
    s "Hm… how do you mean?"
    hide scylla_confused

    menu: 
        "Put yourself first! Do you really owe them anything?":
            jump d2s5sz7
        "You could just quit. Let them handle everything.":
            jump d2s5sz2

label d2s5sz6:
    menu: 
        "I guess some of that sounds like progress":
            jump d2s5sz7A
        "It sounds like they're looking out for you, in their own way.":
            jump d2s5sz8A
        "So what if your idea {i}is{/i} bad? Would it kill them to show up for their friend?":
            jump d2s5sz8A
        "Honesty feels like a low bar.":
            jump d2s5sz7A

label d2s5sz7A:
    show scylla_concerned
    s "Yeah, I guess."
    hide scylla_concerned
    jump d2s5sz9

label d2s5sz8A:
    $ increase_affinity("Scylla", 1)
    show scylla_surprised
    s "Hm, I hadn't thought of it like that."
    s "I guess I'm also upset because they were my friends. But lately I feel like I'm just someone on their volleyball team."
    hide scylla_surprised
    jump d2s5sz9

label d2s5sz9:
    show scylla_serious
    s "I'll have to sleep on it. It still feels very raw."
    s "I don't really want to think about it right now…"
    m "(I feel like this would be a good moment to…)"
    hide scylla_serious

    menu: 
        "Touch her shoulder and say something reassuring.":
            jump d2s5sz10
        "Suggest going somewhere else, like the art fair.":
            jump d2s5sz11
        "Ask her about her family.":
            jump d2s5sz12
        "Daydream about {i}our{/i} family <3":
            jump d2s5sz13

label d2s5sz13:
    m "(Oooookay, that's getting a little ahead of ourselves, champ. Let's try that again.)"

    menu:
        "Touch her shoulder and say something reassuring.":
            jump d2s5sz10
        "Suggest going somewhere else, like the art fair.":
            jump d2s5sz11
        "Ask her about her family.":
            jump d2s5sz12

label d2s5sz12:
    $ decrease_affinity("Scylla", 1)
    show scylla_surprised
    s "...what makes you ask?"
    m "(I dunno, it seemed like a good idea at the time.)"
    m "(But maybe I just reminded her of more stress…)"
    s "My parents don't care that I could get into Black Lagoon University. They think it's too far."
    s "They just want me to go to Frights High Community College so I'll be close to home."
    s "That's just even more people who want me to do whatever they want."
    show scylla_confused
    s "{size=*0.5}But if my perfect little sister wanted to go, that'd be a different story…{/size}"
    s "Sigh…"
    hide scylla_confused
    s "Speaking of which, I should be getting home…"
    m "(...she said that, but she's not moving.)"
    m "(She seems to be in no hurry at all.)"
    m "(Is she waiting for me to say something?)"
    hide scylla_surprised

    menu:
        "Could I convince you to stick around for the art fair?":
            jump d2s5sz12A
        "I don't want to hold you up.":
            jump d2s5syablewit

label d2s5syablewit:
    show scylla_embarrassed
    s "Thanks for chatting with me. Sorry to dump all that on you."
    hide scylla_embarrassed
    show colette_smile at right
    c "You two better be on your way to the art show now!"
    show scylla_smile at left
    s "Oh, right! That's today! Do you have art in there, Colette?"
    # [Colette takes a picture, maybe we have a flash effect or something? Is there a Colette with camera pose?]
    c "I do now!"
    hide colette_smile
    hide scylla_smile
    show colette_smile
    m "Wait, you're not seriously going to display {i}that{/i}!"
    c "No… not {i}today{/i} at least."
    "But I think it'll be perfect for a series I'm putting together."
    m "(What's the series? Awkward moments???)"
    c "Move your butts, dorks. It's art o'clock."
    hide colette_smile
    jump arttime1

label d2s5sz10:
    $ increase_affinity("Scylla", 1)
    show scylla_shocked
    m "(Well, given her reaction, I bet I could say literally anything and she would {i}not{/i} register it.)"
    m "I know it'll work out. You work so hard, and even if this specific thing doesn't work out, you'll only do better next time."
    show scylla_embarrassed
    s "{size=*0.5}........thaaaaaaaaaaaanks……..{/size}"
    m "Did you say something?"
    s "AHEM. THANK YOU."
    s "I mean thank you."
    s "I mean, ah, hey! School's over! Let's go to that art fair. I mean, if you want to see art. Do you want art? To look at?"
    m "(...I don't think she'd hear me say no even if I wanted to say no.)"
    hide scylla_shocked
    hide scylla_embarrassed
    jump arttime1

label d2s5sz11:
    $ increase_affinity("Scylla", 1)
    # BLU points
    m "Hey! Isn't the student art fair going on right now? Let's go check it out!"
    show scylla_smile
    s "Oh! That sounds fun, but I should go home and… well, I'm already here. I can be a little late."
    s "Let's see some art!"
    s "I hope you've got your art critic pants on today."
    hide scylla_smile
    jump arttime1

label d2s5sz12A:
    show scylla_smile
    s "That sounds fun, but I should go home and… well, I'm already here. I can be a little late."
    s "Let's see some art!"
    s "I hope you've got your art critic pants on today."
    hide scylla_smile
    jump arttime1

label arttime1:
    m "Oh, I'm ready."
    scene bg_hallway with dissolve
    show scylla_surprised
    s "Hmmmm…."
    s "[playerName], tell me what you make of this piece."
    hide scylla_surprised

    menu:
        "Incredible. Klimt inspiration, certainly, but in conversation with the neodadaists…":
            jump arttime1a
        "I've got it. It's a statement on increasing wealth inequality.":
            jump arttime1b
        "I prefer their earlier work. Back when their medium was macaroni and glue.":
            jump arttime1c

label arttime1a:
    show scylla_smile
    s "Wow, look at you, smartypants."
    s "Who knew you know so much about this stuff?"
    hide scylla_smile
    jump arttime2

label arttime1b:
    $ increase_affinity("Scylla", 2)
    show scylla_smile
    s "My thoughts exactly. It's so obvious."
    m "Obvious to the trained eye, at least."
    s "Yes. Yes. A bold statement."
    m "A profound achievement."
    s "Indeed." 
    hide scylla_smile
    jump arttime2

label arttime1c:
    $ increase_affinity("Scylla", 1)
    show scylla_surprised
    s "Goodness, I have no idea I was in the company of such a historian."
    m "Yes, yes, a shame the artist sold out…"
    s "Such a loss for innovation in the medium."
    m "Indubitably."
    s "Quite."
    hide scylla_surprised
    jump arttime2

label arttime2:
    m "(We walked around more talking about other students' pieces, until…)"
    show colette_embarrassed
    c "Ah, I see you've finally made it to the best work at the show."
    m "Colette, this is {i}your{/i} art."
    hide colette_embarrassed
    show scylla_surprised
    s "I thought your medium was photography, but this piece is… are these feathers?"
    hide scylla_surprised

    c "Chicken feathers! I had a bunch lying around, and I got inspired!" 
    m "I'll say. Is this a self-portrait?"
    c "Of course not! Can't you tell?"
    m "(Scylla suddenly burst out into laughter.)"
    m "(What am I missing?)"
    c "[playerName], it's {i}you{/i}!"
    m "That's supposed to be {i}me{/i}?"
    s "Bingo! Now, tell me what you think, best friend."
    s "Be brutally honest."

    menu:
        "I look so enigmatic.":
            jump arttime2a
        "I look so startled… frightened by a world to come… you could even say… chicken":
            jump arttime2b
        "If nothing else, I'm flattered to be your muse.":
            jump arttime2c

label arttime2a:
    c "Oh, stop, you're just being nice."
    m "No, seriously! Look! No matter where I go, my eyes follow!"
    s "Eerie!"
    c "That's the power of art, nerds."
    jump arttime3

label arttime2b:
    $ increase_affinity("Scylla", 1)
    s "Haaaaaaa!"
    c "Ah, so you see why this was the perfect medium for capturing you."
    m "Touché."
    jump arttime3

label arttime2c:
    c "You're welcome to use it on your dating profile."
    show colette smirk
    c "That is if you still need one…"
    s "Hm?"
    m "WOW LOOK AT THIS OTHER THING WOW"
    jump arttime3

label arttime3:
    m "(Scylla and I left the art show.)"
    scene bg_stairs with dissolve
    show scylla_smile
    s "That was a fun distraction. I needed that."
    show scylla_concerned
    s "A bummer there were no performing artists this year. Do you remember the interpretive dance last year?"
    m "Dance? No, I don't think I went last year."
    m "Colette was mad…"
    s "Oh, you missed out. Not to be mean. I don't really {i}get{/i} dance. But, oh boy, the dance was so silly."
    s "It was like… and then it was like…"
    s "No. You have to take this all in. You won't {i}get it{/i} otherwise."
    hide scylla_smile
    hide scylla_concerned
    m "(Scylla made me sit down at the top of the stairs and stood a few steps down.)"
    m "(She began doing… {i}something{/i} with her arms.)"
    m "It's very… evocative?"
    m "Is this safe?"
    show scylla_embarrassed
    s "Don't worry, just watch."
    hide scylla_embarrassed
    m "(Scylla's arm gestures were still wild, but became slower and slower.)"
    m "(While she made {i}horrible{/i} eye contact.)"
    show scylla_smirk
    s "Everyone was trying {i}very{/i} hard not to laugh."
    s "Thankfully, they switched their focus to music. They do saxophone in band now."
    s "Although they still do the eye contact thing…"
    s "Well, what do you think? Hilarious? Misunderstood masterpiece?"
    hide scylla_smirk
    
    menu:
        "I guess the meaning is lost on us philistines.":
            jump arttime3a
        "It was supposed to be extremely cute, right?":
            jump arttime3b
        "Maybe it's just the wrong medium. What if you tried the arms thing during volleyball?":
            jump arttime3c

label arttime3a:
    $ increase_affinity("Scylla", 1)
    show scylla_surprised
    s "Maybe they'll teach future generations about the dance. We could be on the wrong side of history."
    m "The wrong side of art history."
    s "The worst kind of wrong side to be on."
    m "We must keep our ignorance between us."
    s "This never leaves this staircase."
    hide scylla_surprised
    jump arttime4

label arttime3b:
    $ increase_affinity("Scylla", 2)
    show scylla_blush
    s "I don't know about {i}supposed{/i} to…"
    hide scylla_blush
    jump arttime4

label arttime3c:
    show scylla_serious
    s "Ah, of course, why didn't I see it before?"
    hide scylla_serious
    jump arttime4

label arttime4:
    show scylla_smile
    s "Ok. I {i}definitely{/i} need to head home now."
    s "This was… a lot of fun."
    m "(I felt like I was supposed to say something, but I couldn't break the silence.)"
    m "(The silence felt like…)"
    scene bg_hallway with flash
    m "Colette!"
    s "See you tomorrow, [playerName]!"
    hide scylla_smile
    m "(Scylla gave me a hug and ran away.)"
    jump D2S6