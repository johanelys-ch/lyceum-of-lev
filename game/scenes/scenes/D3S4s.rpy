image bg forest = "forest.png"

label d3s4s:
    scene bg forest with dissolve
    m "(The further I walked into the forest, the quieter it got. Yet I couldn't shake the feeling that I was not alone.)"
    m "(Nothing seemed that special about the spot… some ruins of an old structure, maybe a well or a fountain?)"
    m "Am I lost? Did I go to the right place…"
    s "You're not lost!"
    m "Scylla? You're here? Where are you?"
    s "Hang on a moment! I've, uh… got something to… show you…"

    menu:
        "Like a surprise?":
            jump d3s4sz1
        "Like a… cool rock?":
            jump d3s4sz2
        "(Just say anything that is {i}not{/i} a joke about her being naked.)":
            jump d3s4sz3

label d3s4sz1:
    s "Ohhhh yeah. It's a surprise, alright."
    jump d3s4sz4

label d3s4sz2:
    s "Uh, well, prepare yourself for something a bit bigger than that."
    jump d3s4sz4

label d3s4sz3:
    m "Uhhhhhhhhhh…"
    m "..."
    m "'Kay!"
    m "(Could have been worse.)"
    jump d3s4sz4

label d3s4sz4:
    s "Now, uh, ok, phew. Here we go…"
    s "{size=*0.5}You can do this. You can do this.{/size}"
    s "You, uh, remember history class?"
    m "...yeah?"
    s "So, this is… kind of related to that…"

    menu:
        "Is everything ok?":
            jump d3s4sz5
        "Do you need homework help or something?":
            jump d3s4sz5
        "Our date is related to history class?":
            jump d3s4sz5

label d3s4sz5:
    s "Oh god, ok here goes."
    s "Monstersarereal. Imeanliketheystillexist."
    s "{size=*0.5}Alsoiamkindofmmmmbllmumblemumble.{/size}"
    m "...sorry? I didn't catch that."
    m "This seems very important to you?"
    s "Gah…. OK."
    s "Monsters didn't disappear 500 years ago. They just went into hiding."
    s "I know this because…"
    show scylla_monster_blush with dissolve
    s "I'm kind of a sea monster."
    hide scylla_monster_blush

    menu: 
        "Only kind of, you say?":
            jump d3s4sz6
        "You're a WHAT?!":
            jump d3s4sz7

label d3s4sz6:
    $ increase_affinity("Scylla", 1)
    show scylla_monster_surprised  
    s "{i}That's{/i} your reaction? You're not shocked? You're just {i}teasing{/i} me?"
    hide scylla_monster_surprised

    menu:
        "But that's our thing!":
            jump d3s4sz8
        "Well, it's fair to say I'm shocked too, but… that's our thing.":
            jump d3s4sz7

label d3s4sz8:
    show scylla_monster_surprised
    s "Well… I suppose this is going well then…"
    s "But be serious! This is huge news to you, right?"
    hide scylla_monster_surprised
    jump d3s4szQ

label d3s4sz7:
    show scylla_monster_surprised
    s "Yeah, I'm sure it must be a lot to take in!"
    hide scylla_monster_surprised
    jump d3s4szQ

label d3s4szQ:
    show scylla_monster_surprised
    s "I bet you're full of questions!"
    hide scylla_monster_surprised

    menu: 
        "What do you mean by monsters have been in hiding?":
            jump d3s4szQ1
        "Am I allowed to know this? What are the rules here?":
            jump d3s4szQ2
        "Are you amphibious?":
            jump d3s4szQ3
        "I'm good for now, I think. Do you have any questions for me?":
            jump d3s4szsooo

label d3s4szQ1:
    s "Well, that's the big secret. We're not gone. Nor all living in secret towns away from the human world."
    s "Some of us preferred to stay in the society we'd built up alongside humans rather than start over elsewhere."
    s "And over 500 years, we've developed disguises or glamours for pretty much any monster to look human."
    jump d3s4szQ

label d3s4szQ2:
    s "Well, it's not frowned upon, but it is sensitive." 
    s "Some monsters feel like relations should eventually be rebuilt, and total secrecy is at odds with that."
    s "Others feel like too much time has passed to openly rejoin society, but it's not practical to be a total secret."
    s "So there's a... wariness around looping in humans. But, for lack of a better word, plenty of humans can hang, you know?"
    s "Not many humans know, though. It's a pretty big risk looping anyone in."
    jump d3s4szQ

label d3s4szQ3:
    s "Wow, I really had no idea what you'd be curious about. This is kind of fascinating…"
    s "Oh! But, uh, yes. I am. I can… breathe in the air and the water…"
    s "Wow, it's weird to just talk about how breathing works, isn't it? Have you ever thought about breathing?"
    s "So weird…"
    jump d3s4szQ

label d3s4szsooo:
    s "Well, I've got a question... one pretty big one obviously."
    s "I like you a lot. But are {i}you{/i}... ok with this?"
    
    menu: 
        "I'm into you, so, yeah.":
            jump d3s4sz8A
        "It's a surprise… but I like to take things slow regardless, so let's find out together?":
            jump d3s4sz9
        "I'm actually just scared for my life":
            jump d3s4sbad

label d3s4sbad:
    if not d4:
        $ d4 = True
        $ decrease_affinity("Scylla", 15)  
    show scylla_monster_angry
    s "...what the hell?"
    s "That's what you think? Even after getting to know me?"
    s "I should have listened to Roger… do you know how bad {i}that{/i} feels?"
    hide scylla_monster_angry
    # fade to black
    jump d4s0

label d3s4sz8A:
    $ increase_affinity("Scylla", 1)  
    show scylla_monster_blush
    s "[playerName]..."
    s "Can I kiss you?"
    hide scylla_monster_blush
    menu:
        "Oh my god, finally!":
            jump d3s4sSWAK
        "Yes! Wait. That means the same thing for sea monsters that it does for humans, right?":
            jump d3s4sz10

label d3s4sz9:
    $ decrease_affinity("Scylla", 1)  
    s "Slow is good… I'm sure this isn't what you were expecting…"
    s "Human-monster relationships aren't unheard of, but they do have challenges…"
    s "We can just… hang out if you like…"
    menu:
        "Can I kiss you?":
            jump d3s4sSWAK
        "Can I… sit next to you?":
            jump d3s4sz11

label d3s4sz10:
    show scylla_monster_blush
    s "Yes, dummy."
    hide scylla_monster_blush

    menu: 
        "Ok, cool, seemed good to communicate. Still yes!":
            jump d3s4sSWAK
        "For the record, I was open to hearing out if it was something else.":
            jump d3s4sz12

label d3s4sz11:
    s "Yeah, if you're nervous, we can just chat a bit…"
    s "To tell you the truth, I'm plenty nervous… about a lot of things right now…"
    m "No wonder. This seems like a really vulnerable position to be in…"
    m"It means a lot you'd do this for me…"
    m "(I graze her hand.)"
    s "What were you expecting? Slimy?"
    m "No idea what to expect! I just learned monsters still exist!"
    menu: 
        "And that one of them wanted to go on a date with me! Me!":
            jump d3s4sz8
        "Well, if we're both nervous… maybe we just dive right in…":
            jump d3s4sz13

label d3s4sz12:
    s "I guess it bodes well for us if you're a try-anything-once kinda human."
    jump d3s4sSWAK

label d3s4sz13:
    $ increase_affinity("Scylla", 1)  
    s "Yeah… we do have a lot in common… maybe even the things we don't totally love about ourselves."
    "That might not be a bad thing if we can support each other though…"
    menu:
        "I love that.":
            jump d3s4sz8
        "To be clear, I'm saying let's kiss…":
            jump d3s4sSWAK
        "To be clear, I'm saying let's kiss… wait, sorry, \"dive right in\" isn't, like, offensive to sea monsters, is it…":
            jump d3s4sz14

label d3s4sz14:
    $ increase_affinity("Scylla", 1)  
    s "HAHAHAHA! Oh my god, no!"
    s "No, it's not offensive. That's nothing. You're safe."
    s "Cute that you asked though… you really are in unfamiliar waters, huh…"
    m "Haha"
    s "Haha"
    s "...ok, we might be stalling now……"
    menu:
        "(Just lean in…)":
            jump d3s4sSWAK
        "(Hang on a second… what am I doing?)":
            jump d3s4syikes

label d3s4syikes:
    m "(What am I doing…)"
    menu:
        "(This is a MONSTER! What if she eats you? You should make sure she doesn't eat humans before you get any closer to that mouth!)":
            jump d3s4sbad
        "(Whoa, ok, that's just crazy brain. This is a little scary, but I know Scylla! Just kiss her already!)":
            jump d3s4sSWAK
        "(This is nowhere NEAR romantic enough! She deserves a serenade!)":
            jump d3s4sz15

label d3s4sz15:
    m "(Ok, champ. I know you're freaking out right now, but, really, how do you imagine that going?)"
    m "(Let's use the power of imagination for a moment. Because it'd be like…)"
    s "What are you doing?"
    s "Oh my god, please stop singing."
    m "Oh no, I was worried I killed the mood, but now I've just made it even worse!"
    m "(Yeah. See? It'd be like that.)"
    m "(Honestly, how did you even get this far with this girl?)"
    m "(Do you think she would like a spectacle like that? Go for the Enzo route next time if that's your thing!)"
    m "(Let's try this again. Think carefully this time.)"
    menu:
        "(This is a MONSTER! What if she eats you? You should make sure she doesn't eat humans before you get any closer to that mouth!)":
            jump d3s4sbad
        "(Whoa, ok, that's just crazy brain. This is a little scary, but I know Scylla! Just kiss her already!)":
            jump d3s4sSWAK

label d3s4sSWAK:
    $ increase_affinity("Scylla", 5)  
    s "Wow… it's really happening…"
    s "You have no idea how long I've wanted to do this…"
    scene bg_scylla_kiss with dissolve
    pause 3.5
# fade to black
    jump D3S5