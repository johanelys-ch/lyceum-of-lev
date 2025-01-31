image bg classroom = "classroom.png"

label D1S1:
    label d1s1z1:
        scene bg classroom
        pause 1

        $ playerName = renpy.input("What's your name?", default = playerName)
        if playerName.strip() == "":
            $ playerName = "Micah"
        m "Alright, [playerName], let's get started."

        play music "history.mp3"
        # [can we get like a slow zoom out on the cover of a history textbook, so the scene starts off looking like an illustrated history, but then it's revealed it's the cover of a textbook - it's a slow reveal this is diegetic, baby!]
        show lalonde_normal
        l "As we all know, until about 500 years ago, there were monsters."
        l "Villages, cities, entire countries where humans and monsters lived and worked together."
        l "As is often the case, they had their conflicts. Disputes over resources and land. Cultural clashes. But despite their differences, the two largely coexisted peacefully."
        l "Of course, now the monsters are gone."
        l "You already know this. You're all going to graduate high school this year. This is not new information."
        l "But, of course, the events surrounding why the humans drove the monsters away and how the monsters disappeared is a matter of debate. This will be a major focus of our class this semester."
        l "What does it mean about history that sometimes we have these holes in the record of what happened? And what does it mean when there {i}isn't{/i} a hole?"
        stop music fadeout 1.0 
        l "..."
        l "...Enzo, I heard that."
        # [ok now we got the classroom and the normal VN visuals]
        play music "classroom.mp3"
        hide lalonde_normal
        show enzo_laugh
        e "I didn't say anything! I'm excited to learn about getting holes filled this semester!"
        m "(Everybody immediately groans at that one.)"
        hide enzo_laugh
        show lalonde_confused
        l "Enzo, do you {i}want{/i} detention? Again?"
        hide lalonde_confused
        show colette_embarrassed
        c "Aw, Ms. Lalonde! They aren't bothering anyone!" 
        c "Take [playerName], for instance. Are they bothering {i}you{/i}?"
        m "(Crap. Thanks for getting me involved, best friend...)"
        m "(She's the one with a dumb soft spot for the class clown! What am I supposed to say to fix this?)"
        hide colette_embarrassed

        menu:
            "...girl. {i}Obviously{/i}.":
                $ increase_affinity("Roger", 1)
                $ increase_affinity("Scylla", 1) 
                jump d1s1z3
            
            "The innuendo {i}is{/i} an improvement over the fart jokes.":
                $ increase_affinity("Enzo", 1)
                $ increase_affinity("Scylla", 1)
                jump d1s1z2

            "I don't understand what's happening. Can we please get back to the holes?":
                $ increase_affinity("Enzo", 2)
                jump d1s1z2

    label d1s1z2:
        show lalonde_confused
        l "Oh… it's going to be a long year."
        hide lalonde_confused
        jump d1s1z3

    label d1s1z3:
        m "(It looks like Ms. Lalonde has decided to ignore all of this and get on with it.)"
        m "(She's really cool, though. She's happy to let us goof around a bit, and Enzo usually doesn't push it too far.)"
        m "(Usually.)"
        # [something something colette winking or z-snapping at you]
        m "(She's got {i}such{/i} a crush on Enzo. I think she's still in denial about it… but it's obvious.)"
        m "(I might have to decide whether to encourage her or not… but they're both such goofballs, I don't know if they'd be perfect for each other or terrible for each other.)"
        show lalonde_normal
        l "What we {i}do{/i} know is that, 500 years ago, humans drove monsters out of the civilization they had shared and built together."
        l "Usually this is attributed to a single event: a series of high-profile disappearances of human children. What we don't know, and is still a matter of debate, is what happened to these children."
        l "But we do know that humans found a common enemy in monsters."
        hide lalonde_normal
        show roger_serious 
        r "Friggin' {i}humans{/i}, man."
        hide roger_serious
        show scylla_confused
        s "But how could humans just force monsters out? I mean, in comparison to monsters, wouldn't humans be…"
        hide scylla_confused
        show enzo_confused
        e "Squishier?"
        hide enzo_confused

        show lalonde_normal
        l "Society is complicated, and there are forms of power aside from just brute force."
        l "We do know that humans had fought amongst themselves for centuries - even before the disappearances - about how much they wanted to share the world with monsters."
        l "Some humans were content to share the world with monsters. Some weren't. And many simply didn't care all that much."
        l "Governments can pass laws that make it harder or easier to find housing, employment, or health care. Even if they don't, systems that maintain social order can choose what rules they do or do not enforce."
        l "Even if blatant discrimination is illegal, if it becomes too difficult to obtain recourse, people become discouraged. At that point, does it even matter what the law actually says?"
        hide lalonde_normal
        show enzo_shocked
        e "A world without rules…"
        hide enzo_shocked

        menu:
            "Heck yeah! Rules are fake!":
                jump d1s1z4
            "It doesn't sound like monsters got to ignore the rules, though.":
                jump d1s1z5
            "But Enzo, if there are no rules, then there's nowhere to put the holes!":
                jump d1s1z6

    label d1s1z4:
        $ increase_affinity("Enzo", 1)
        $ decrease_affinity("Roger", 1)
        show colette_laugh
        c "*z snaps*"
        hide colette_laugh
        jump d1s1z7

    label d1s1z5:
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Scylla", 1)
        $ increase_affinity("Lalonde", 1)
        show lalonde_normal
        l "Exactly."
        hide lalonde_normal
        jump d1s1z7

    label d1s1z6:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Scylla", 1)
        show enzo_smile
        e "Oh no. What a conundrum."
        e "Are rules… good?"
        e "I guess if there are no rules… then there are no pranks…"
        hide enzo_smile
        show lalonde_normal
        l "...you know what? I'll take it."
        l "Yes, for instance, pranks are funny because they're a lighthearted breaking of the rules. If there are no rules to break, then how can you do a prank?"
        l "And if your pranks never got a reaction from anyone, how long would you put in the effort before giving up on pranks?"
        hide lalonde_normal
        show enzo_confused
        e "This is blowing my mind."
        hide enzo_confused
        jump d1s1z7

    label d1s1z7:
        show roger_serious
        r "Is this whole class just going to be about what humans did?"
        r "That's so anthropocentric, man! That's caca!"
        hide roger_serious

        menu: 
            "...anthropocentric?":
                jump d1s1z8

            "...caca?":
                jump d1s1z9

            "...Roger? Wait, are you even in this class?":
                jump d1s1z10

    label d1s1z8:
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Lalonde", 1)
        show roger_smirk
        r "It means that everything is framed in terms of what it means to humans. If humans have nothing to do with it, it doesn't make it into the history books."
        r "It's a system of oppression, man!"
        hide roger_smirk
        jump d1s1z11

    label d1s1z9:
        $ increase_affinity("Enzo", 1)
        $ decrease_affinity("Roger", 1)
        show roger_embarrassed
        r "I'm just saying, man."
        r "It means that everything is framed in terms of what it means to humans. If humans have nothing to do with it, it doesn't make it into the history books."
        r "It's a system of oppression, man!"
        hide roger_embarrassed
        jump d1s1z11

    label d1s1z10:
        $ decrease_affinity("Enzo", 1)
        show roger_embarrassed
        r "I, uh, I just transferred."
        hide roger_embarrassed
        show lalonde_confused
        m "(Ms. Lalonde seems to be looking at some papers on her desk…)"
        m "(She seems to have decided not to bother right now.)"
        hide lalonde_confused
        jump d1s1z11

    label d1s1z11:
        show scylla_confused
        s "So, wait, humans did all that to kick monsters out {i}before{/i} the disappearances?"
        s "Then what did they do when the disappearances began…"
        hide scylla_confused
        show lalonde_normal
        l "Well, this is what's still a matter of debate. And maybe it always will be."
        l "All we know for certain is that human children began to disappear, then humans blamed the monsters, and then, shortly after that, the monsters vanished."
        l "The only written records we have are from humans. And it's not like there are monsters around to talk to today."
        hide lalonde_normal
        show roger_serious
        r "So, what, we're just gonna read a bunch of propaganda in this class?"
        hide roger_serious
        show lalonde_normal
        l "Not exactly. We're not just going to read. We're also going to ask why."
        hide lalonde_normal

        menu:
            "Like \"why are we doing this?\"":
                jump d1s1z12
            "Like \"why did the person who wrote this conclude this?\"":
                jump d1s1z13
            "Like \"why did the person who wrote this want people to think this?\"":
                jump d1s1z13 
            "(This sounds so hard. I'm gonna smooch someone eventually, right?)":
                jump d1s1z14

    label d1s1z12:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Roger", 1)
        jump d1s1z15

    label d1s1z13:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Scylla", 1)
        $ increase_affinity("Lalonde", 1)
        show lalonde_normal
        l "You have the right idea, [playerName]."
        hide lalonde_normal
        jump d1s1z15

    label d1s1z14:
        m "(Yeah, I mean, this is my last year of high school. I might never see most of these people again in my life.)"
        m "(Who could I smooch?)"
        show colette_blush
        m "(No. Too weird. Way too weird.)"
        hide colette_blush
        show enzo_blush
        m "(I mean… they {i}are{/i} cute…)"
        hide enzo_blush
        show scylla_blush
        m "(She's cute…)"
        hide scylla_blush
        show roger_blush
        m "(He {i}could{/i} be cute if, I don't know, he didn't have such a one-track mind.)"
        hide roger_blush
        show lalonde_confused
        m "(...)"
        m "(NOPE. NOPE. Let's think about something else now.)"
        hide lalonde_confused
        m "(What were we talking about?)"

        menu:
            "Like \"why are we doing this?\"":
                jump d1s1z12
            "Like \"why did the person who wrote this conclude this?\"":
                jump d1s1z13
            "Like \"why did the person who wrote this want people to think this?\"":
                jump d1s1z13 

    label d1s1z15:
        m "(For the rest of the class, we talked about a few different historians we'll be studying the rest of the semester.)"
        m "(Roger only complained about most of them.)"
        jump D1S2