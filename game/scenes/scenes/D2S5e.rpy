label d2s5ez1:
    scene bg_school_front with dissolve
    m "(Enzo and I sat on a bench in the front of the school. I couldn't quite tell how they were doing after that argument.)"
    m "So, {i}another{/i} prank? Putting a lot on your plate, aren't you?"
    show enzo_smirk
    e "Nothing I can't handle. I can't simply rest on my laurels, could I?"
    m "(Enzo's eye was caught by students walking by with a particularly large art project.)"
    e "Look at that lot. Carrying their hopes and dreams on poster board and duct tape." 
    e "You think anyone told them their masterpieces will end up in some storage closet next week?"
    m "That's rather harsh… you don't really sound like yourself."
    e "Maybe… but who am I to talk? My legacy is probably a trail of glitter and bad ideas."
    hide enzo_smirk

    menu: 
        "Genius isn't appreciated in its time, though, right?":
            jump d2s5ez1a
        "I didn't take you for a nihilist.":
            jump d2s5ez1b
        "And chicken feces. Don't sell yourself short.":
            jump d2s5ez1c

label d2s5ez1a:
    $ increase_affinity("Enzo", 1)
    show enzo_smirk
    e "Just where do you suppose flattery will get you with me?"
    hide enzo_smirk
    jump d2s5ez2

label d2s5ez1b:
    # code to allow for an option to appear later (see comments)
    e "Nihilist? Nonsense. I subscribe to \"realist with a flair for the dramatic.\""
    # idk a haughty expression, eyes closed, something?
    e "A \"dramarealist.\""
    # back to normal expression
    e "Is that a thing? I'll have to look this up later."
    jump d2s5ez2

label d2s5ez1c:
    $ decrease_affinity("Enzo", 1)
    show enzo_smirk
    e "Just where do you suppose flattery will get you with me?"
    hide enzo_smirk
    jump d2s5ez2

label d2s5ez2:
    show enzo_concerned
    e "Now look at those two."
    m "(Enzo pointed at two utterly normal-looking people.)"
    e "Classic lovebirds in denial."
    m "You think so?"
    e "It's all over their faces. He's too scared to admit he likes her. She's too stubborn to do anything first."
    e "Trapped in a sinking boat that neither one wants to rock."
    e "Isn't it fascinating how people complicate things for no reason?"
    hide enzo_concerned

    menu:
        "What would you do instead to {i}not{/i} complicate it?":
            jump d2s5ez2a
        "You liar, you would love the drama.":
            jump d2s5ez2b
        "Are you sure you're not… projecting?":
            jump d2s5etri
        "Wait, the boat is sinking? Why is the boat sinking in this metaphor?":
            jump d2s5ez2c

label d2s5ez2a:
    $ increase_affinity("Enzo", 1)
    show enzo_laugh
    e "I'd confess in the most ridiculous way possible. Grand gestures are my specialty." 
    e "A serenade with a ukulele while juggling flaming torches. Memorable, right?"
    e "Can't you see it?"
    hide enzo_laugh

    menu:
        "So long as the other person would actually like that.":
            jump d2s5ez3
        "Any reason you haven't done that yet?":
            jump d2s5etri
        "I thought you drew the line at arson. This sounds dangerously close to arson.":
            jump d2s5ez4

label d2s5ez2b:
    $ increase_affinity("Enzo", 1)
    show enzo_smile
    e "Tidy and orderly is for people who don't know how to live."
    e "Life is drama. Pretending otherwise is simply not living."
    e "I mean, if it were {i}me{/i}..."
    hide enzo_smile
    jump d2s5ez2a

label d2s5ez2c:
    e "Well, it certainly isn't going to stay afloat forever like that."
    e "It's not a sustainable situation."

    menu:
        "Hit a little close to home, Enzo?":
            jump d2s5etri
        "I guess some people would rather pretend they don't notice the ship is sinking.":
            jump d2s5ez4
        "They're probably queasy too.":
            jump d2s5ez5


label d2s5ez3:
    show enzo_smirk
    e "Pity. Nothing like making a scene for someone who matters."
    show enzo_smirk
    jump d2s5ez6

label d2s5ez4:
    $ increase_affinity("Enzo", 2)
    show enzo_smirk
    e "Hmm… a fair point. I'm glad I've got you to challenge me to see things in another way."
    hide enzo_smirk
    jump d2s5ez6

label d2s5ez5:
    $ increase_affinity("Enzo", 1)
    show enzo_smile
    e "Yes… they {i}are{/i} probably a little sick of things in that situation…"
    hide enzo_smile
    jump d2s5ez6

label d2s5ez6:
    m "...do you want to talk about it?"
    jump d2s5etri

label d2s5etri:
    show enzo_shocked
    e "..."
    m "Have {i}I{/i} surprised the mighty Enzo? Have the tables so turned?"
    hide enzo_shocked
    show enzo_smirk
    e "Depends what you think I think you're thinking."
    hide enzo_smirk

    menu:
        "You have feelings for Colette.":
            jump d2s5etri2
        "You have feelings for me.":
            jump d2s5etri2
        "You have feelings for me {i}and{/i} Colette.":
            jump d2s5etri2

label d2s5etri2:
    show enzo_surprise
    e "WAIT!"
    m "(They cut me off before I could even say that!!!)"
    e "This is no place for a conversation this serious!"
    e "Come! I know what must be done."
    scene bg_arcade with dissolve
    hide enzo_surprise
    show enzo_laugh
    m "...the arcade?"
    e "Life is about contrasts! Isn't this {i}unexpected{/i}?"
    m "(Yeah… you can't hear a thing in here!)"
    m "I don't know… it sounds like you just don't want to have a serious conversation…"
    e "What was that? I couldn't hear you over the sound of all this merriment!"
    m "(Enzo dragged me over to a dancing game)"
    e "Tell you what… let's leave it up to a game of skill."
    e "You win, I confess all my secrets to you."
    e "And if I win…"
    hide enzo_laugh

    menu: 
        "It doesn't matter! Enzo! We were having a real conversation!.":
            jump d2s5etri5
        "It doesn't matter… because I'm going to kick your {i}butt{/i}.":
            jump d2s5etri3
        "What? Will I owe you a kiss?":
            jump d2s5etri4

label d2s5etri4:
    $ increase_affinity("Enzo", 2)
    show enzo_smile
    e "Oh, sunshine, don't write a check you can't cash."
    hide enzo_smile
    jump d2s5edance

label d2s5etri3:
    $ increase_affinity("Enzo", 1)
    show enzo_smirk
    m "(Enzo couldn't help but grin even wider at that.)"
    e "Challenge accepted."
    hide enzo_smirk
    jump d2s5edance

label d2s5etri5:
    m "(Enzo held their hand up to their ear.)"
    show enzo_smile
    e "What was that? I couldn't hear you over the sound of our dance-off."
    m "(Enzo started the game)."
    m "Hey! Wait!"
    hide enzo_smile
    jump d2s5edance

label d2s5edance:
    m "(...)"
    m "(........)"
    m "(Oh my god, Enzo is so good at this game…)"
    m "(They {i}destroyed{/i} me.)"
    show enzo_smirk
    e "Tell you what, I'm graceful in victory. You owe me nothing. In fact, allow me to treat you to ice cream while walking back to school."
    scene bg_hallway with dissolve
    m "The school art fair? I thought you said you were taking me for ice cream?"
    e "I would never lie about a matter of such import."
    m "(...somehow Enzo is holding two ice cream cones.)"
    m "Did you… {i}have{/i} these? This whole time?"
    m "How did they not melt?"
    e "Let's just call it one of my tricks."
    hide enzo_smirk
    show colette_serious
    c "You better not get {i}any{/i} of that on the art!"
    hide colette_serious
    show enzo_surprise
    e "What kind of slob do you take me for?"
    e "Besides, I brought enough to share."
    m "(How does Enzo have a {i}third{/i} ice cream cone??)"
    hide enzo_surprise
    show colette_smile
    c "Fine. I'll allow bribery this one time. So long as you come appreciate my art."
    hide colette_smile
    m "(I knew Colette's hobby was photography, but I was shocked how good these photos were.)"
    m "(All of the photos were of the three of us. Some me and Colette, some Colette and Enzo, some Enzo and me.)"
    m "(But never one of all three of us…)"

    menu:
        "Colette! These are so good!":
            jump d2s5ez7
        "Enzo! How dare you look so good in these!":
            jump d2s5ez7
        "(Well of course there aren't any of the three of us. Someone had to take the photo.)":
            jump d2s5ez8

label d2s5ez7:
    $ increase_affinity("Enzo", 1)
    show enzo_laugh
    e "Naturally."
    hide enzo_laugh
    jump d2s5ez9

label d2s5ez8:
    m "(Wait, no… that doesn't make sense. She's in some of her own photos anyway. Must be a timer.)"
    jump d2s5ez9

label d2s5ez9:
    m "(Then I notice something… a ribbon?)"
    m "Hang on… Colette, did this win second place? Like for the whole show?"
    show colette_laugh
    c "It sure did!"
    c "{size=*0.5}Appropriately enough…{/size}"
    hide colette_laugh
    show enzo_smile
    e "Congratulations, partner in crime. This is no small accomplishment."
    hide enzo_smile
    m "(Colette just smiles…)"
    m "(Enzo is at a loss for words too…)"
    m "(I'm not sure what to do…)"
    m "(I think it's become pretty obvious to everyone what's going on here…)"
    show colette_smile
    c "I have to stay until the end of the show, but, Enzo, maybe you show [playerName] {i}the thing{/i}."
    m "(Huh, maybe I {i}don't{/i} know what's going on.)"
    hide colette_smile
    show enzo_surprise
    e "Hmmmmm, I suppose [playerName] has proven their value to the team…"
    m "What are you two talking about?"
    hide enzo_surprise
    show colette_smirk
    c "You'll see…"
    hide colette_smirk
    scene bg classroom with dissolve
    m "Where are we {i}now{/i}?"
    show enzo_smirk
    e "This is the drama classroom."
    m "...let me guess. You have a prank to make the drama classroom more dramatic."
    m "(Enzo flicks the lightswitch. They have replaced all the lights with bulbs that cycle through different colors.)"
    e "Does this answer your question?"
    show enzo_confused
    e "It is missing a little something, though. It's not quite as impactful as I wanted…"
    hide enzo_smirk
    hide enzo_confused

    menu: 
        "What about a fog machine?":
            jump d2s5ez10
        "What about glitter? Confetti?":
            jump d2s5ez10
        "What about… a timer…":
            jump d2s5ez11

label d2s5ez10:
    $ increase_affinity("Enzo", 1)
    show enzo_smile
    e "Yes… yes, I could get that done tonight."
    hide enzo_smile
    jump d2s5ez15

label d2s5ez11:
    show enzo_serious
    e "I'm listening."
    m "So there's a timer, right? Class starts, the timer starts counting down." 
    m "And everyone's wondering what will happen when it hits zero, and…"
    hide enzo_serious

    menu:
        "The teacher's desk {i}explodes{/i}.":
            jump d2s5ez12
        "The teacher's desk {i}vanishes{/i}.":
            jump d2s5ez13
        "Nothing happens. The greatest prank of all.":
            jump d2s5ez14


label d2s5ez12:
    $ decrease_affinity("Enzo", 1)
    show enzo_serious
    e "Oh, I thought you had a real suggestion."
    m "Too much?"
    e "{i}Way{/i} too much!"
    e "{size=*0.5}Hmmm maybe I made a mistake…{/size=*0.5}"
    hide enzo_serious
    jump d2s5ez15

label d2s5ez13:
    $ increase_affinity("Enzo", 2)
    show enzo_smile
    e "Ok. I love it. I don't know how I'd do that, but I love it."
    m "Yeah… sorry, it got away from me."
    e "Don't apologize. Don't let something so silly as the laws of reality get in the way of your vision."
    e "I'll make a prankster out of you yet."
    hide enzo_smile
    jump d2s5ez15

label d2s5ez14:
    $ increase_affinity("Enzo", 1)
    show enzo_smile
    e "Not bad at all…"
    e "Pretty sneaky, [playerName]."
    show enzo_smirk
    e "I can see you've drawn inspiration from my mysterious chicken number three, in fact."
    m "Oh yeah… I guess it's kind of the same idea you're already doing."
    e "Don't worry. A for effort."
    e "And you know a grade means a lot coming from {i}me{/i}."
    hide enzo_smile
    hide enzo_smirk
    jump d2s5ez15

label d2s5ez15:
    show enzo_smile
    e "Nonetheless… thanks for today, [playerName]."
    e "I was… in a bit of a funk earlier."
    e "You know why I do these pranks?"
    hide enzo_smile

    menu:
        "To make others happy?":
            jump d2s5ez16
        "To fill the void?":
            jump d2s5ez17
        "Because your parents expect it of you?":
            jump d2s5ez18

label d2s5ez16:
    $ increase_affinity("Enzo", 1)
    show enzo_smile
    e "Precisely."
    show enzo_smile
    jump d2s5ez19

label d2s5ez17:
    show enzo_smile
    e "Har de har har."
    hide enzo_smile
    jump d2s5ez19

label d2s5ez18:
    $ increase_affinity("Enzo", 1)
    show enzo_embarrassed
    e "...sort of, actually."
    m "Hm? I was kidding…"
    e "Yes, of course. As was I. Got you."
    hide enzo_embarrassed
    jump d2s5ez19

label d2s5ez19:
    show enzo_smile
    e "When I make others happy, I'm happy."
    e "A little light-hearted fun is a surefire way to make others happy."
    e "Others who matter, anyway. You'll always have the Rogers of the world."
    e"But lately I've felt like…"
    e "Sometimes making one person happy might make another person unhappy."
    hide enzo_smile

    menu:
        "Life might not be like your pranks.":
            jump d2s5ez19A
        "I thought life is drama and pretending otherwise is simply not living?":
            jump d2s5ez21
        "Maybe your pranks are also a way to create a world where no one really gets hurt.":
            jump d2s5ez20
        "Sounds like a central conflict of dramarealist philosophy.":
            jump d2s5ez21

label d2s5ez19A:
    show enzo_smile
    e "Huge design flaw, if you ask me."
    hide enzo_smile
    jump d2s5ezfin

label d2s5ez20:
    $ increase_affinity("Enzo", 1)
    show enzo_smile
    e "Hm, food for thought."
    e "I suppose I {i}am{/i} a kind soul."
    e "Although personally I don't desire to change the world. I much prefer to decorate it."
    hide enzo_smile
    jump d2s5ezfin

label d2s5ez21:
    $ increase_affinity("Enzo", 2)
    show enzo_embarrassed
    e "I see I've left an impression on you."
    e "I suppose that {i}is{/i} what I said…"
    hide enzo_embarrassed
    jump d2s5ezfin

label d2s5ezfin:
    $ increase_affinity("Enzo", 1)
    show enzo_smile
    e "I suppose I must get going if I'm going to get this prank ready."
    e "It's always a pleasure to spend time with you, [playerName]."
    m "(...Enzo didn't make any move to leave.)"
    e "Heh."
    e "I do so hate to leave a party."
    e "(...)"
    show enzo_embarrassed
    e "Don't be a stranger."
    hide enzo_embarrassed
    hide enzo_smile
    m "(Enzo left.)"
    m "(...I think I have to talk with Colette.)"
    jump D2S6