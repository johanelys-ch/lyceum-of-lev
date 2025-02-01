label d3s4e:
    scene bg forest
    m "(The further I walked into the forest, the quieter it got. Yet I couldn't shake the feeling that I was not alone.)"
    m "(Not alone… but no Enzo anywhere either…)"
    m "(Was Enzo watching me?)"
    m "(Nothing seemed that special about the spot… some ruins of an old structure, maybe a well or a fountain?)"
    m "(Was this whole \"special spot in the forest\" thing just one of Enzo and Colette's pranks?)"
    e "[playerName]!" 
    m "(...where were they?)"
    e "I'm over here… But before you come any closer, I need to tell you something. Would you mind staying there?"

menu:
    "Enzo, is this another one of your pranks?":
        jump d3s4e1
    "Why? Are you naked?":
        jump d3s4e2

label d3s4e1:
    e "Believe it or not, no." 
    m "Alright, I trust you. What's the big mystery?"
    jump d3s4e3

label d3s4e2:
    e "Well, {i}someone{/i} had high hopes for this date."
    jump d3s4e3

label d3s4e3:
    e "You see, I've been keeping something from you, something really important."
    m "The punchline?"
    e "See, I love your sense of humor, but this is a serious moment I'm afraid."

menu:
    "Interesting… you've piqued my curiosity.":
        jump d3s4e4
    "Ok. I'll let you talk. Whatever this is, I'm listening.":
        jump d3s4e4
    "What kind of serious? Bad serious or… not necessarily bad serious?":
        jump d3s4e4

label d3s4e4:
    show enzo_embarrassed
    e "Look, I really like you, and I want you to know that keeping this from you hasn't been easy." 
    e "Let's say I'm used to it, though… you'll see…"
    e "Before we go any further in, whatever this is, you need to know. And I trust you."
    e "I'm not actually human, [playerName]." 
    e "In fact, I'm one of those monsters we've been talking about in history class. More specifically…"
    hide enzo_embarrassed
    show enzo_monster_embarrassed
    hide enzo_monster_embarrassed

menu:
    "Are you a kitsune?":
        jump d3s4e5
    "Are you a tanuki?":
        jump d3s4e5
    "Are you a werewolf?":
        jump d3s4e6
    "Are you going to kill me?":
        jump d3s4e7

label d3s4e6:
    e "Heavens, no. That's ridiculous."
    jump d3s4e5

label d3s4e7:
    $ decrease_affinity("Enzo", 1)
    e "I know this is a lot to take in… just give me a moment to explain what I am…"
    jump d3s4e5

label d3s4e5:
    show enzo_monster
    e "We've had many names… tanuki, kitsune, coyote… not to be confused with the other coyotes…"
    e "We personally prefer \"trickster gods\", but the other monsters get all {i}upset{/i} about that one for some reason."
    e "Monsters haven't disappeared. We've just gone into hiding. We live in secret. Well, many of us do."
    e "It's complicated, of course."
    e "Some live elsewhere, just among monsters. Many of us feel attached to the society we always lived in, despite its flaws."
    e "Those who do hide in plain sight, using glamours, disguises, makeup…"
    e "We've had 500 years to develop our methods after all. No wonder humans think we're extinct."
    e "It's a huge secret, obviously. Very few humans know the truth."
    e "Which… now includes…"
    e "You…"
    hide enzo_monster

    menu:
        "Is that all? Can we make out now?":
            jump d3s4e8
        "You're a trickster god? Huh, I would've guessed a devil, since you always want me to misbehave…":
            jump d3s4e9
        "There are monsters?! Just, like, {i}everywhere{/i}?":
            jump d3s4e10

label d3s4e8:
    $ increase_affinity("Enzo", 1)
    show enzo_monster_blush
    e "Well, I'm flattered. I had no idea how you'd react, but I'm relieved that you don't seem to mind."
    hide enzo_monster_blush

    menu:
        "Mind? This is a dream come true!":
            jump d3s4e11
        "Well, it's not what I was expecting, but you look good for a trickster god, I think?":
            jump d3s4e12
        "And you don't mind about… me?":
            jump d3s4e13

label d3s4e11:
    show enzo_monster
    e "{i}Someone's{/i} got a type. Guess it's your lucky day."
    hide enzo_monster
    jump d3s4eQ1

label d3s4e12:
    show enzo_monster_serious
    e "Hush, you don't know what you're saying. We're {i}all{/i} lookers."
    e "But how would you know? I'll take the compliment."    
    hide enzo_monster_serious
    jump d3s4eQ1

label d3s4e13:
    $ increase_affinity("Enzo", 1)
    show enzo_monster
    e "You're kind, thoughtful, and can hold your own against steep prank competition. What's there to mind?"
    e "And you're hot if you simply must hear it."
    hide enzo_monster
    jump d3s4eQ1

label d3s4e9:
    show enzo_monster_smirk
    e "Please, devils are so straightforward. Clearly you've never flirted with a devil." 
    hide enzo_monster_smirk
    jump d3s4eQ1

label d3s4e10:
    show enzo_monster_serious
    e "More like \"all over.\" \"Everywhere\" makes it sound like we secretly run the world or something."
    hide enzo_monster_serious

menu:
    "But aren't we… enemies? I'm not sure I feel safe.": 
        jump d3s4ebad
    "Can this… work?": 
        jump d3s4enotgreat
    "This is a lot to take in.":
        jump d3s4eQ1

label d3s4eQ1:
    show enzo_monster
    e "You probably have about a million questions, right?"
    hide enzo_monster

    menu:
        "Are you the only monster at the school?":
            jump d3s4eQ2
        "A trickster spirit… who plays pranks… a little on the nose, don't you think?":
            jump d3s4eQ3
        "Are the chickens monsters or are they just chickens? Wait, {i}are{/i} there chickens?":
            jump d3s4eQ4

label d3s4eQ2:
    show enzo_monster
    e "Of course not! Although you understand we don't exactly go around telling on each other."
    e "Although I'm assuming since she told you about this place, she probably assumes you'll figure it out about now…"
    hide enzo_monster

    menu:
        "Hm… I can talk to her about it later. Let's talk about you right now.":
            jump d3s4eQ1
        "As long as we're being honest… you're sure you wouldn't rather date her?":
            jump d3s4eCOL
        "HAS EVERYONE BEEN LYING TO ME THE WHOLE TIME?!":
            jump d3s4enotgreat2
        "Nope. No further questions.":
            jump d3s4esoooo
        
label d3s4eQ3:
    $ increase_affinity("Enzo", 1)
    show enzo_monster
    e "Well, I'd hardly be the only one struggling with my parents' expectations, would I?"
    e "Maybe it's my nature, but I honestly just like to make people happy."
    hide enzo_monster
    jump d3s4eQ1

label d3s4eQ4:
    show enzo_monster_smirk
    e "...{i}that's{/i} what you're thinking about? Of course not!"
    show enzo_monster
    e "Well… I guess {i}I've{/i} never had my entire understanding of reality suddenly shattered…"
    e "I suppose that's a fair question, actually."
    hide enzo_monster_smirk
    hide enzo_monster
    jump d3s4eQ1

label d3s4eCOL:
    show enzo_monster_embarrassed
    e "Do you see her here now?"
    e "I can't lie… I had a hard time sorting through my feelings, but…"
    show enzo_monster_blush
    e "I'm yours if you want me."
    hide enzo_monster_embarrassed
    hide enzo_monster_blush
    jump d3s4esoooo

label d3s4esoooo:
    show enzo_monster_smirk
    e "So… now it's {i}my{/i} turn to ask a question."
    e "Can I kiss you?"
    hide enzo_monster_smirk
    
    menu: 
        "Me? Kiss a monster?":
            jump d3s4ebad
        "I thought you'd never ask.":
            jump d3s4eSWAK

label d3s4ebad:
    if not d4:
        $ d4 = True
        $ decrease_affinity("Enzo", 15)  
    show enzo_monster_serious
    e "…I see I've misjudged you…"
    hide enzo_monster_serious
    jump d4s0


label d3s4enotgreat:
    show enzo_monster_serious
    e "Human-monster relationships? It happens."
    e "It's not for everyone, for a variety of reasons."
    e "It requires a lot of trust, for one thing."
    e "So… how are you feeling, truly? Please… be honest."
    hide enzo_monster_serious

    menu:
        "I'm curious… let's take it slow?":
            jump d3s4elukewarm
        "Surprised. To be honest, a little scared. A little disoriented about the world…":
            jump d3s4enotgreat2
        "I am going to throw up.":
            jump d3s4ebad

label d3s4elukewarm:
    show enzo_monster_serious
    e "That'd be sensible regardless."
    e "Let's just let each other know if any of this becomes uncomfortable…"
    hide enzo_monster_serious
    jump D3S5

label d3s4enotgreat2:
    show enzo_monster_serious
    e "That's not unreasonable. That's exactly what humans want other humans to feel."
    e "...it's not too late to back out."
    hide enzo_monster_serious
    
    menu: 
        "Oh, no no no! I'm just… overwhelmed! I mean, where to even begin?":
            jump d3s4eQ1
        "Is it too late to take it slow?":
            jump d3s4elukewarm
        "(just run away screaming)":
            jump d3s4ebad

label d3s4eSWAK:
    $ increase_affinity("Enzo", 1)
    scene bg_enzo_kiss
    pause 3.5
    jump D3S5