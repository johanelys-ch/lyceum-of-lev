label D2S1:
    label d2s1z1:
        show nextday with dissolve
        scene bg_school_front
    # maybe just a title card of some kind saying "DAY 2" or something, so we don't need to narrate "and then it was the next day"
        show colette_smile
        c "Best friend!"
        c "I need your help with the homework! I couldn't finish - I was up so late wrapping up my pieces for the art fair!"
        c "Which you had better be going to, by the way."
        m "Ok, calm down! This isn't like you to worry! How far did you get?"
        c "I {i}almost{/i} got to looking up what the assignment is."
        m "Ok… {i}that's{/i} more like you…"
        c "Why should I have to do the reading anyway? I already know how to read!"
        hide colette_smile
        show roger_serious
        r "What good is being able to read if you can't use your brain?"
        hide roger_serious
        show colette_serious
        c "I dunno, what good is being able to use your brain if you can't make anyone want to talk with you?"
        m "Ok, ok, let's just calm down, both of you."
        m "Colette, what do you need help with?"
        hide colette_serious
        show colette_confused
        c "Well, we needed to write a page about three questions about the reading, right? But they're, like… open-ended!"
        c "What did you get for the first question? \"Why do you think monsters disappeared without a trace 500 years ago?\""
        hide colette_confused
        show roger_smirk
        r "Oh, I {i}gotta{/i} hear this. What {i}did{/i} you get?"
        hide roger_smirk

        menu:
            "Humans probably killed them all.":
                    jump d2s1z2
            "Monsters probably decided to start over somewhere safer.":
                    jump d2s1z3
            "Monsters probably couldn't keep up with human weaponry.":
                    jump d2s1z2
            
    label d2s1z2:
        $ decrease_affinity("Roger", 1)
        $ decrease_affinity("Lalonde", 1) 
        show roger_serious
        r "Utter caca. I expected as much."
        hide roger_serious
        jump d2s1z4

    label d2s1z3:
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Lalonde", 1) 
        show roger_concerned
        r "Hm. Well, I've heard dumber."
        hide roger_concerned
        show colette_concerned
        c "Isn't [playerName] right, though? Isn't that what happened?"
        hide colette_concerned
        jump d2s1z4
    
    label d2s1z4:
        show roger_serious at left
        r "Humans 500 years ago didn't want humans {i}today{/i} to know the truth, butthead."
        r "There's no record. No one can ever know for certain."
        show enzo_smirk at right
        e "Oh, what repartee! I simply must get involved."
        r "Enzo, be honest. You didn't do the homework either."
        e "I can have many reasons to do the things I do."
        hide enzo_smirk
        show enzo_smile at right
        e "And tell me, [playerName], what did you get for question 2?"
        hide roger_serious
        show roger_angry at left
        r "None of you are going to learn anything if you don't do the work yourselves."
        e "But I thought the work {i}was{/i} to sort through the debate and draw our own conclusions."
        e "And here you are, debating right now!"
        e "Who would any of us be to gatekeep which debate gets to be part of {i}the{/i} debate?"
        r "You're still just justifying your own laziness!"
        hide enzo_smirk 
        hide roger_angry
        show colette_serious
        c "Um, tick tock! I don't have all day. [playerName], what do you think?"
        hide colette_serious
        
        menu:
            "Enzo's right, Roger. Quit gatekeeping.":
                jump d2s1z5
            "Roger's right, Enzo. You're not exactly arguing in good faith.":
                jump d2s1z6
            "Honestly, it does feel like everyone else is just benefiting from {i}my{/i} work…":
                jump d2s1z7

    label d2s1z5:
        $ decrease_affinity("Roger", 1)
        $ increase_affinity("Enzo", 1)
        show roger_angry
        r "You're all such f…"
        r "F…"
        r "Fartfaces."
        hide roger_angry
        show colette_concerned
        c "No! No! No!"
        hide colette_concerned
        jump d2s1z8

    label d2s1z6:
        $ decrease_affinity("Enzo", 1)
        $ increase_affinity("Roger", 1) 
        show enzo_confused
        e "Is that {i}truly{/i} what you think of me? After all we've been through!"
        hide enzo_confused
        show colette_concerned
        c "No! No! No!"
        hide colette_concerned
        jump d2s1z8

    label d2s1z7:
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Enzo", 1) 
        # +points for the good schools lol
        show enzo_smirk at right
        show roger_angry at left
        show colette_laugh
        e "Just say the word, and I'll abstain from leeching. I live by a code."
        r "(Roger just makes indecipherable angry sounds.)"
        c "Good for you, Enzo. I have no such code!"
        hide colette_laugh
        hide enzo_smirk
        hide roger_angry
        jump d2s1z8

    label d2s1z8:
        show colette_confused
        c "I {i}obviously{/i} meant about question 2!"
        hide colette_confused
        show roger_serious
        r "Well, I've had enough of this. Look, even if you start now, you don't have time to finish."
        m "(Despite there being a watch visible on his wrist, Roger lifted up his sleeve to check the time on a second watch…)"
        "(This kid's a character.)"
        r "See you in class if you ever finish literally the first assignment."
        hide roger_serious
        show colette_serious
        c "Second question. \"What do you think is the most likely explanation for the disappearing human children?\""
        hide colette_serious

        menu:
            "Maybe {i}some{/i} monsters with a grudge kidnapped them, even though all monsters took the fall.":
                jump d2s1z9
            "There's totally a cover-up, man! {i}Someone{/i} wanted to pit humans and monsters against each other.":
                jump d2s1z10
            "Humans probably just lost them.":
                jump d2s1z11

    label d2s1z9:
        $ decrease_affinity("Lalonde", 1)
        $ decrease_affinity("Enzo", 1) 
        jump d2s1z12

    label d2s1z10:
        $ increase_affinity("Lalonde", 1)
        $ increase_affinity("Enzo", 1) 
        jump d2s1z12

    label d2s1z11:
        $ increase_affinity("Enzo", 1) 
        jump d2s1z12

    label d2s1z12:
        show enzo_smirk
        e "What a fascinating insight."
        hide enzo_smirk
        show scylla_smile
        s "Hi everyone! What's fascinating?"
        c "That I didn't do the homework. Apparently it's all anyone wants to talk about this morning."
        c "Come on, best friend. I'm still going to write my page myself! I just need a little… help knowing what to write about!"
        c "It's not like I'm going to college anyway."
        hide scylla_smile
        show enzo_confused
        e "I thought we were going to community college together!"
        c "Well, yeah, duh, I'm not counting that. I mean like {i}fancy{/i} college for {i}rich{/i} people."
        e "...{i}you're{/i} rich."
        hide enzo_confused
        show colette_blush
        c "I know {i}that{/i}! That's not the point." 
        c "It's a political statement."
        m "Is that how that works?"
        hide colette_blush
        show scylla_confused at left
        show enzo_smile at right
        s "...are we still talking about the homework?"
        s "Because, honestly, I did struggle with a good answer for question three…"
        e "How convenient! [playerName] was just going to tell us all the correct answer for question three."
        m "I don't know about \"correct\"... it's kind of complicated…"
        e "Tell us the objective truth of the world!"
        hide enzo_smile
        hide scylla_confused
        show colette_serious
        c "Third and final question. \"Do you think humans and monsters were destined for conflict until one side won?\""
        hide colette_serious

        menu:
            "Probably. Sadly, people are more willing to be equitable in homogenous societies with people like themselves.":
                jump d2s1z13
            "There's no reason they couldn't all live together as long as everyone worked together, paid their rent, hustled to keep the economy going…":
                jump d2s1z14
            "It's a trick question. I wrote four whole pages about how all war is class war.":
                jump d2s1z15
            "Both sides had their points. Next time they should just not fight.":
                jump d2s1z16
        
    label d2s1z13:
        $ decrease_affinity("Roger", 1)
        $ decrease_affinity("Scylla", 1) 
        $ decrease_affinity("Lalonde", 1)
        show roger_angry
        r "Argh! You've got poop for brains, poopbrain."
        m "When did {i}you{/i} come back?"
        hide roger_angry
        jump d2s1z17

    label d2s1z14:
        $ decrease_affinity("Roger", 1)
        $ decrease_affinity("Enzo", 1) 
        show roger_serious
        r "Wow, {i}someone{/i} played {i}Disco Elysium{/i}."
        r "Let me guess, you complained on Reddit about how the game was too \"judgy.\""
        hide roger_serious
        show colette_angry
        c "I thought {i}you{/i} were leaving!"
        hide colette_angry
        jump d2s1z17

    label d2s1z15:
        $ increase_affinity("Lalonde", 1)
        $ increase_affinity("Enzo", 1) 
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Scylla", 1) 
        show colette_shocked
        c "But the assignment was to write {i}one{/i} page, you nerd!"
        hide colette_shocked
        jump d2s1z17

    label d2s1z16:
        $ decrease_affinity("Lalonde", 1)
        $ decrease_affinity("Enzo", 1)
        $ decrease_affinity("Roger", 1)
        show enzo_serious
        e "Ah, I see. History class is just one big lecture about what not to do."
        e "I will thus proceed to {i}not{/i} do this assignment."
        e "[playerName] has shown me that the point of the assignment is to determine that the only correct course of action is inaction."
        hide enzo_serious
        show scylla_confused
        s "...is that true? That can't be it, right?"
        s "Oh my god, what do I do? I need a good grade in this class…"
        hide scylla_confused
        jump d2s1z17

    label d2s1z17:
        show colette_concerned
        c "Ok, this was… helpful. By default, probably."
        c "Whatever. I'm only gonna write half a page anyway. I'm going to school for fashion."
        c "Staying up late studying and getting bags under my eyes actually works {i}against{/i} my goals for the future." 
        hide colette_concerned
        scene bg_hallway
        show colette_smirk
        c "So?"
        m "...so what?"
        c "So how was your little date after school last night?"
        m "...my little date?"
        hide colette_smirk

        if D1S3eB:
            jump D2S2e
        elif D1S3sB:
            jump D2S2s
        elif D1S3rB:
            jump D2S2r

    label D2S2e:
        show colette_serious
        c "Well, I know that {i}I{/i} was there too, but still. Can't rush these things."
        m "Hm… I'm not sure if you have quite the right idea…"
        hide colette_serious

        menu:
            "That was just three friends making costumes for chickens. Normal friend times.":
                jump D2S2e1
            "In fact, do you think you might be projecting?":
                jump D2S2e2
            "(What am I saying? She hasn't made a move! And Enzo's hot…)":
                jump D2S2e3

    label D2S2e1:
        show colette_laugh
        c "Sure, sure… you tell yourself that."
        hide colette_laugh
        jump D2S2fin

    label D2S2e3:
        show colette_smirk
        c "Mmmmmm your silence tells me {i}everything{/i}..."
        c "A little senior year romance is brewing, perhaps…"
        hide colette_smirk
        jump D2S2fin

    label D2S2e2:
        $ increase_affinity("Enzo", 1) 
        show colette_blush
        c "Ok, now you're being {i}crazy{/i}!"
        hide colette_blush
        jump D2S2fin

    label D2S2s:
        c "Come on… the classic \"shoulder to cry on\" with Scylla?"
        c "Who do you think you're talking to?"
        # z snaps
        c "I know all the moves."

        menu:
            "Any tips, then?":
                jump D2S2s1
            "I dunno, she seems too busy to be open to anything…":
                jump D2S2s2
            "Don't worry. I know plenty of moves myself.":
                jump D2S2s3

    label D2S2s1:
        c "Finally, you've come to the expert for guidance. Listen well, my student."
        m "Is it too late to change my mind?"
        c "Hush. Let me guide you to your heart's desire."
        c "If it were me… I'd try not to overwhelm her."
        c "Someone who's always trying so hard doesn't want to date someone who just feels like more expectations, you know?"
        jump D2S2fin

    label D2S2s2:
        c "Actually, I bet, more than anything else, she probably could use someone to talk to."
        c "I think she probably needs at least one person in her life who isn't telling her what to do all the time…"
        jump D2S2fin

    label D2S2s3:
        c "Well… I'd be careful about {i}which{/i} moves you use, player."
        c "Something tells me that Scylla isn't one to rush into things…"
        jump D2S2fin

    label D2S2r:
        c "I saw you waiting for Roger after class…"
        m "Yeah, I know you did. You took a photo of me falling down the stairs."
        c "I'm documenting your blossoming romance! What kind of friend would I be otherwise?"
        m "...{i}of me falling down the stairs???{/i}"
        c "Falling down the stairs… falling in {i}love{/i}...?"

        menu:
            "You got me. I like a bad boy.":
                jump D2S2r1
            "(Play it cool. I think if there were a {i}chance{/i} Roger overheard this, it'd just scare him off.)":
                jump D2S2r2
            "I don't know how this happened, but I need to make it extremely clear I am {i}not{/i} interested in Roger":
                jump D2S2r3

    label D2S2r1:
        show colette_smirk
        c "Who doesn't like to give themselves a challenge from time to time?"
        hide colette_smirk
        show colette_concerned
        c "I don't know how serious you are, but… he's definitely going to Vampire Academy next year."
        c "Somehow I don't see him settling for a long-distance relationship…"
        hide colette_concerned
        m "(Before I could say anything, the bell rang.)"
        jump D2S2fin

    label D2S2r2:
        show colette_smirk
        m "So, because I was waiting for someone in the hallway after class, it must mean I want to put my face on their face."
        c "Well, it doesn't {i}not{/i}."
        c "But I think I see what you're up to. Play it slow, make him want {i}you{/i}… your secret's safe with me."
        c "For now."
        hide colette_smirk
        m "(Before I could say anything, the bell rang.)"
        jump D2S2fin

    label D2S2r3:
        $ decrease_affinity("Roger", 1)
        show colette_concerned
        c "Ok, phew, honestly, I wasn't sure if this required an intervention or not."
        c "You really had me worried for a second there, best friend."
        c "I suppose you'll just have to keep your eyes open for opportunities to seek a different senior year romance…"
        hide colette_concerned
        jump D2S2fin

    label D2S2fin:
        show colette_serious
        c "Sigh. Alright. Let's get class over with."
        c "History class isn't going to help me with my modelling career. Why can't I learn something useful at this school?"
        hide colette_serious
        jump D2S3