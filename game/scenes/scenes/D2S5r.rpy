label D2S5rz1:
    m "(I convinced Roger to go to the library with me by telling him it'd help him cool down after that disagreement.)" 
    m "(Or so he thought…)"
    m "(As we approached the doors, I couldn't help but smirk a little to myself.)"    
    m "Oh no, look at that. Closed at 6, and it's 6:50. Guess we're too late."
    r "Hmph. Time to get a watch, more like."
    m "You'd know!"
    m "(Roger rolled down his sleeve to cover up some of his watches.)"
    r "You {i}planned{/i} this, didn't you?"
    m "I'd never do that. Oh, hey, there's an arcade nearby. Why don't we check it out?"
    r "An arcade? Absolutely not. That's just a den of flashing lights and obnoxious noises for mindless poopies."

    menu:
        "It's either that or we just stand here awkwardly until it's time to go home. Your call.":
            jump D2S5rz2
        "And you wouldn't find it a {i}little{/i} fun to go judge them?":
            jump D2S5rz1a
        "You're just scared I'll kick your butt.":
            jump D2S5rz1b

label D2S5rz1a:
    $ increase_affinity("Roger", 1)
    jump D2S5rz2

label D2S5rz1b:
    $ decrease_affinity("Roger", 1)
    jump D2S5rz2

label D2S5rz2:
    m "(He's thinking too hard about this. Maybe I overplayed my hand…)"
    r "Fine. But this better not waste my time."
    r "(He's back to checking one of his many watches. Is it his favorite? Why isn't it more visible then?)"
    # arcade visuals
    m "(We walked into the arcade, the sound of games and laughter filling the air.)"
    m "(Roger looked unimpressed with it all.)"
    r "It's even worse than I imagined." 
    r "Why do poopies flock to places like this? Everything is overpriced, the floor is sticky, and there are kids screaming everywhere."

    menu: 
        "Because it's fun. You're not supposed to focus on the bad things.":
            jump D2S5rz2c
        "{i}You're{/i} a kid.":
            jump D2S5rz2b
        "Why {i}do{/i} poopies flock to places like this? Let's investigate.":
            jump D2S5rz2a

label D2S5rz2a:
    $ increase_affinity("Roger", 1)
    r "If you're trying to get on my good side through making fun of these idiots…"
    jump D2S5rz2c

label D2S5rz2b:
    $ decrease_affinity("Roger", 1)
    r "I mean {i}little{/i} kids."
    r "Must you always mock me? It's like spending time with Enzo…"
    jump D2S5rz2c

label D2S5rz2c:
    r "But the bad things are so {i}obvious{/i}. I don't get how they don't see it!"
    m "Come on, let's start with something simple."
    m "(I led Roger to an air hockey table and grabbed the paddle.)"
    m "How about air hockey? Simple enough, right?"
    r "Fine. But don't expect me to go easy on you."

    menu:
        "(Letting him score a few points is going to help him let loose, right?)":
            jump D2S5rz3a
        "(I'm definitely not losing. He's a big boy.)":
            jump D2S5rz3b

label D2S5rz3a:
    m "(I let him score a few points, hoping it would make him less tense.)"
    r "Thought I wouldn't notice? I'll win on my own terms, don't underestimate my abilities, poopie."
    jump D2S5rz4

label D2S5rz3b:
    $ increase_affinity("Roger", 1)
    m "(I matched his energy, determined not to lose.)"
    show roger smirk
    r "Impressive, for a poopie."
    jump D2S5rz4

label D2S5rz4:
    m "(Roger took the game way too seriously, analyzing every move like his life depended on it.)" 
    m "(Maybe air hockey is his passion? Or he's trying really hard not to suck at it.)"
    m "You know it's just air hockey, right? You don't have to overthink it."
    r "You brought me here. I might as well do it right."
    m "(I couldn't help but laugh. By the end, he actually seemed a little less tense.)"
    m "Ok, how about we try a shooting game now?"
    m "(Roger had to shoot at some weird-looking bats before they hid behind some small rocks. He surprised me by being ridiculously good at it.)"
    m "Wow, look at you. Saving the world from poopies one shot at a time."
    show roger smile
    r "This is nothing. The mechanics in this game are laughably bad. Everything is so predictable." 
    r "You don't have to try that hard to know where they are going to pop out from next."

    menu:
        "I guess you've got an eye for detail.":
            jump D2S5rz5
        "You know this is just a game, right? Relax a little!":
            jump D2S5rz6

label D2S5rz5:
    $ increase_affinity("Roger", 2)
    r "Naturally."
    jump D2S5rg3

label D2S5rz6:
    r "Says the one who dragged me here."
    jump D2S5rg3

label D2S5rg3:
    r "And bats aren't poopies, by the way."
    m "Oh. You like bats?"
    r "...never mind."
    m "What? Bats are cool! We don't have to play a game where you kill bats…"
    m "(I looked around for something else and grinned.)"
    m "Oh, we {i}have{/i} to do that."
    m "(Roger looked where I was pointing.)"
    show roger shocked
    r "Absolutely not."
    r "A dancing game?! You won't catch me dancing around like a poopie."
    m "You know, it's okay to let loose sometimes. You don't have to be in control and remain collected all the time."
    r "This isn't just about me. It's about avoiding... messes."
    m "Well, today you're allowed to make a mess. Also…"

    menu:
        "It's just for fun. Nobody's going to judge you.":
            jump D2S5rz8
        "You said you were good at everything. Prove it.":
            jump D2S5rz7
        "So you're a master of sports and firearms. It's ok if you suck at dancing.":
            jump D2S5rz7

label D2S5rz7:
    r "When did I say that?"
    m "You said it. I'm not good with dates, but you definitely said it."
    r "If you just want to see my dancing skills, just say it."
    jump D2S5rz9

label D2S5rz8:
    $ increase_affinity("Roger", 1)
    r "Is your name \"Nobody\"? I guess we'll see."
    jump D2S5rz9

label D2S5rz9:
    m "(Roger stepped onto the platform, his face full of doubt. At first, his movements were stiff and awkward, but as the game went on, he loosened up.)" 
    m "(By the end, he was laughing. Whether it was from fun or embarrassment, I couldn't tell.)"
    m "(I couldn't help but snap a photo. Definitely a moment to remember.)"
    m "(As we left the arcade, I couldn't resist teasing him.)"

    menu:
        "So, which game was your favorite?":
            jump D2S5rz11
        "So, any new insights about the mindless poopies?":
            jump D2S5rz12
        "So, was that a date?":
            jump D2S5rz10


label D2S5rz11:
    r "Oh, definitely {i}Dance D{/i}- I mean…"
    r "Games are dumb."
    r "It is beneath me to have a favorite."
    jump D2S5rz13

label D2S5rz10:
    $ increase_affinity("Roger", 1)
    show roger blush
    r "A {i}what{/i}? Don't be ridiculous!"
    jump D2S5rz13

label D2S5rz12:
    $ increase_affinity("Roger", 1)
    r "Hmmm. Yes… despite how much tedious, loud noise they always make, it seems they're numb to it themselves."
    m "A finding you only gathered spending time in the field."
    r "Yes, I suppose it wasn't a total waste of time."
    jump D2S5rz13

label D2S5rz13:
    m "(I laughed out loud. Maybe Roger isn't so bad after all.)"
    jump D2S6