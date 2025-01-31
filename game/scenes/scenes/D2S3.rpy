label D2S3:
    label d2s3z1:
        scene bg classroom
        show lalonde_normal
        l "Today, we're going to introduce a few major theories about what happened 500 years ago."
        l "This is difficult stuff. Historians dedicate their entire lives to this. We're not asking you to solve our society's biggest mystery."
        l "But it's important to learn about this because of the ways that our society is informed by this little dark age. Perhaps the most consequential event in history is a complete mystery to us."
        l "To start, let's break this down into two different questions."
        l "First, what happened to the human children who disappeared?"
        l "Second, what caused the monsters to disappear after that?"
        hide lalonde_normal
        show roger_serious
        r "Why does it matter {i}why{/i} some stupid kids disappeared? What matters is what humans did to monsters afterward."
        r "Does any explanation change that what humans did was wrong?"
        hide roger_serious
        show lalonde_confused
        l "That's a good question, Roger. But history isn't about who did the right thing and the wrong thing. It's about learning why people {i}thought{/i} they were doing the right thing."
        hide lalonde_confused
        show enzo_smirk
        e "For instance, the wrong question to ask is \"was whoever filled all the lockers with ball pit balls right or wrong to do so…\""
        m "(How {i}did{/i} Enzo get so many ball pit balls? They were rolling around for weeks…)"
        hide enzo_smirk
        show lalonde_confused at left
        l "Sure, let's go with that. History isn't just about how Enzo got detention for that prank."
        show enzo_embarrassed at right
        e "History is about why the school was justified in accusing me of such a misdeed!"
        show colette_concerned
        c "But you definitely did do that, Enzo..."
        hide colette_concerned
        hide enzo_embarrassed
        hide lalonde_confused
        show lalonde_confused
        l "Maybe we need a different example."
        hide lalonde_confused
        show scylla_confused at left
        s "But that's a good point, though. What does it change if some monsters kidnapped some human children like humans said or if those human children just got lost and disappeared if humans forced monsters out anyway?"
        show roger_serious at right
        r "Well, it tells us that humans didn't care one way or another."
        hide scylla_confused
        hide roger_serious

        menu:
            "Yeah, sounds like humans screwed up no matter what.":
                jump d2s3z1mor
            "It matters if monsters had it coming!":
                jump d2s3z1fac
            "Wouldn't it matter why a local issue became a catalyst for a global response?":
                jump d2s3z1maz
            "Were these, like, famous children? Is that why anyone even cared?":
                jump d2s3z1ult

    label d2s3z1mor:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Roger", 1)
        show roger_concerned
        r "That's what I've been saying! Even [playerName] gets it! That's how obvious it is!"
        hide roger_concerned
        jump d2s3z2

    label d2s3z1fac:
        $ decrease_affinity("Roger", 1)
        $ decrease_affinity("Lalonde", 1)
        show roger_serious
        r "I mean, sure, in theory, but there's no way that's what happened."
        hide roger_serious
        jump d2s3z2

    label d2s3z1maz:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Lalonde", 1)
        show lalonde_normal
        l "That's a very interesting question."
        hide lalonde_normal
        show roger_confused
        r "Hmph. I mean… it's still just because of poopy nonsense at the end of the day… but I see your point…"
        hide roger_confused
        jump d2s3z2

    label d2s3z1ult:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Scylla", 1)
        show enzo_surprise
        e "Good question. Ms. Lalonde, is it only official records that were lost? Do we have any 500-year-old gossip rags?"
        hide enzo_surprise
        jump d2s3z2

    label d2s3z2:
        show lalonde_normal
        l "Let's just start going through some of the major theories."
        l "As Roger has reminded us, there are plenty of theories that cast monsters as the aggressors of history."
        l "Theories that monsters kidnapped the children for one reason or another. Revenge. Prisoners. Maybe they ate them."
        l "Some theories suggest these were simple isolated incidents. Some suggest something organized."
        l "But there are other theories that suggest humans are to blame." 
        l "The children could have gone missing entirely on accident. Or some humans themselves did it just to frame monsters."
        l "Either way, monsters became the scapegoat."
        hide lalonde_normal
        show colette_confused
        c "This is starting to sound very conspiracy theory… is this really history class?"
        hide colette_confused

        menu:
            "I guess if we learn how to stop some kidnapping scum from doing it again, then, yeah.":
                jump d2s3z2ult
            "Who cares? No way the man wants us to know about this! Don't say anything!":
                jump d2s3z2maz
            "Right? Monsters are gone, so we know they must've done {i}something.{/i}":
                jump d2s3z2fac
            "Of course it's history class. It's all old stuff, isn't it?":
                jump d2s3z2mor

    label d2s3z2ult:
        $ increase_affinity("Scylla", 1)
        $ increase_affinity("Lalonde", 5)
        show roger_serious
        r "Humans {i}would{/i} say that monsters are just scum."
        hide roger_serious
        show scylla_concerned
        s "But what if monsters {i}weren't{/i} the kidnappers, Roger? Kidnapping is bad!"
        hide scylla_concerned
        show enzo_smirk
        e "I for one would never kidnap someone."
        hide enzo_smirk
        show roger_concerned
        r "Aren't we relieved."
        hide roger_concerned
        jump d2s3z3

    label d2s3z2maz:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Lalonde", 1)
        $ increase_affinity("Scylla", 1)
        show enzo_smirk
        e "Heck yeah, now we're getting to the good stuff."
        hide enzo_smirk
        jump d2s3z3

    label d2s3z2fac:
        $ decrease_affinity("Enzo", 1)
        $ decrease_affinity("Roger", 1)
        $ decrease_affinity("Lalonde", 1)
        $ decrease_affinity("Scylla", 1)
        show roger_angry
        r "Are you even trying to learn anything?"
        hide roger_angry
        jump d2s3z3

    label d2s3z2mor:
        $ increase_affinity("Enzo", 1)
        show enzo_smirk
        e "The logic is flawless."
        hide enzo_smirk
        jump d2s3z3

    label d2s3z3:
        show lalonde_normal
        l "You know what they say. \"Those who don't know their history are doomed to repeat it.\""
        hide lalonde_normal
        show enzo_serious
        e "But I thought the whole point was we {i}don't{/i} know our history."
        hide enzo_serious
        
        menu:
            "Whoa.":
                jump d2s3z4
            "Whoaaa.":
                jump d2s3z4
            "Whoaaaaaaaa.":
                jump d2s3z4
            "Whoaaaaaaaaaaaaaaaaaaaaaa.":
                jump d2s3z4

    label d2s3z4:
        show colette_serious
        c "Are we going to talk about the fountain theory?"
        m "The what?"
        hide colette_serious
        show scylla_surprised
        s "It's a theory that the human children didn't really disappear, but they were changed into monsters."
        show roger_serious at left
        r "Can we not waste time on fairy tales? I'm trying to get into a {i}good{/i} college."
        s "I mean, it's a little far-fetched, but there's pretty interesting evidence for it…"
        s "The census records don't line up… we know some monsters had some degree of magical powers…"
        s "So it's not inconceivable that {i}something{/i} out there in the world - doesn't have to be a fountain, specifically - also had magical properties."
        r "We'd have found such a thing by now if it existed."
        show enzo_serious at right
        e "But, Roger, we know monsters existed even though we haven't found any, haven't we?"
        e "You're mistaking the null hypothesis for evidence."
        r "The {i}what?{/i} Ugh, did you just get that from a book on the fountain theory?"
        e "Well, of course. It's certainly the theory with the most charm to it, is it not?"
        r "History isn't about charm!"
        r "I bet even poopie [playerName] knows {i}that{/i}."
        hide roger_serious
        hide enzo_serious
        hide scylla_surprised

        menu:
            "There's no way such a thing would stay secret; it'd transform the economy!":
                jump d2s3z4ult
            "It does sound like something humans would make up to get off the hook…":
                jump d2s3z4maz
            "If humans could kill all the monsters, they could destroy all the magic fountains for sure. Smash smash.":
                jump d2s3z4fac
            "Hard to say. I don't know a lot of things.":
                jump d2s3z4mor
        
    label d2s3z4ult:
        $ increase_affinity("Roger", 1)
        show roger_serious
        r "Yeah. Pure fantasy."
        hide roger_serious
        jump d2s3z5

    label d2s3z4maz:
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Lalonde", 1)
        show roger_serious
        r "Yeah. Pure fantasy."
        hide roger_serious
        jump d2s3z5

    label d2s3z4fac:
        $ increase_affinity("Enzo", 1)
        show roger_confused
        r "Cool, I'm glad we're spending a whole class on how good humans are at destroying crap."
        hide roger_confused
        jump d2s3z5

    label d2s3z4mor:
        $ increase_affinity("Enzo", 1)
        show roger_concerned
        r "...I don't know what I expected."
        hide roger_concerned
        jump d2s3z5

    label d2s3z5:
        show roger_concerned
        r "Look, if we're going to spend class time on the fountain theory, what else? Do we spend time on the werewolf theory?"
        hide roger_concerned
        m "(A bunch of people groaned.)"
        show lalonde_normal
        l "Ah, an old controversial one."
        l "The werewolf theory is another theory where monsters took an active role in human child disappearances."
        l "There are two branches of the theory. One is that it was politically motivated and organized, the other is that individual werewolves, for whatever reason, broke some treaties."
        l "And it's not dissimilar from the fountain theory, in that it suggests the human children were transformed…"
        hide lalonde_normal

        menu:
            "Why's that controversial? It's just saying werewolves did werewolf stuff. That's plausible.":
                jump d2s3z5fac
            "It's a real monster infighting kind of theory. Convenient for humans…":
                jump d2s3z5maz
            "Well, we'll never know for sure, so I suppose it's as worth spending time on as anything else.":
                jump d2s3z5mor
            "Were there not, like, police back then?":
                jump d2s3z5ult

    label d2s3z5fac:
        $ decrease_affinity("Roger", 1)
        show roger_serious
        r "And what exactly is \"werewolf stuff?\""
        m "Biting humans and turning {i}them{/i} into werewolves?"
        r "Are you basing your understanding of werewolves on what you've seen in movies?"
        m "...is that not right?"
        hide roger_serious
        show scylla_concerned
        s "I suppose we don't know for sure."
        hide scylla_concerned
        show roger_serious
        r "So we shouldn't assume."
        hide roger_serious
        jump d2s3z6

    label d2s3z5maz:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Lalonde", 1)
        
        e "Yes… see how they pit the proletariat against each other."
        s "Enzo, some of the humans would have been proletariat too."
        s "And possibly not even all of the monsters who may or may not have been involved…"
        e "I'm just saying."
        s "...saying {i}what{/i}?" 
        jump d2s3z6

    label d2s3z5mor:
        $ increase_affinity("Scylla", 1)
        s "Yeah, we shouldn't write anything off until we know more."
        jump d2s3z6

    label d2s3z5ult:
        $ increase_affinity("Roger", 1)
        r "Yeah, hang on, why isn't one of the questions why did the {i}humans{/i} get kidnapped?"
        r "What were they doing?"
        s "Your new theory is that the {i}children{/i} are responsible for being kidnapped?"
        r "I'm just saying, all anyone talks about with this subject is \"Did monsters do this?\" \"Did monsters do that?\""
        r "What about the humans? What about personal responsibility?"
        s "For being {i}kidnapped{/i}?"
        jump d2s3z6

    label d2s3z6:
        l "I probably should be upset about how off-topic we've gotten, but asking questions about how the debate is framed {i}is{/i} what I'm trying to teach you."
        l "Look how much you're arguing without any actual evidence. Just based on your feelings."
        l "Without any certainty over what happened, you see how heated debates get."
        l "Now let's turn to the second half of the question: what caused the monsters to disappear after that?"
        s "I thought yesterday you said it was a combination of things."
        l "Certainly. It likely was. But just because it can be more than one thing, it doesn't make any of those factors any less important."
        l "There's no evidence that war broke out, but, again, we don't know for certain."
        l "But the lack of evidence of widespread violence raises different questions."
        l "Did the monsters leave willingly? Were they forcibly removed?"
        l "Was there an agreement? And if so, between whom?"
        l "All we really know now is that human society treats the whole thing fairly somberly."
        l "This is why so many institutions - the prestigious Vampire Academy, our very own town of Frights High, and the nearby Black Lagoon University - are named after monsters or what we remember of their culture."
        r "Big whoop."

        menu:
            "Hey, a land acknowledgment is the least we can do.":
                jump d2s3z6ult
            "I guess we could name {i}more{/i} things after monsters.":
                jump d2s3z6mor
            "Yeah, we should really rename all this after human stuff by now.":
                jump d2s3z6fas
            "And who named all this stuff? Rich people. What do {i}they{/i} have to hide?":
                jump d2s3z6maz

    label d2s3z6ult:
        $ decrease_affinity("Roger", 1)
        $ increase_affinity("Lalonde", 1)
        m "(Roger just makes a fart noise.)"
        jump d2s3z7

    label d2s3z6mor:
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Lalonde", 1)
        m "(Roger just makes a fart noise, but it might have been a slightly more amused fart.)"
        jump d2s3z7

    label d2s3z6fas:
        $ decrease_affinity("Roger", 1)
        $ decrease_affinity("Lalonde", 1)
        m "(Roger makes a really, really, really long fart noise.)"
        jump d2s3z7

    label d2s3z6maz:
        $ increase_affinity("Enzo", 1)
        $ increase_affinity("Lalonde", 1)
        m "(Roger rolls his eyes. Could be worse. You feel like if you said anything else, he might've just made a fart noise.)"
        jump d2s3z7

    label d2s3z7:
        l "One last theory for class today is a relatively new one based on new research out of Vampire Academy."
        l "Going through the archaeological records and trying to determine if a monster migration {i}had{/i} taken place, and comparing it to personal correspondences from the era, we get the coalition theory."
        l "This suggests that different humans with different viewpoints - pacifists, monster-relations activists, and so on - but a common goal of avoiding violence came together and met with monster leaders for an extrajudicial arrangement."
        c "That's too many words. What does that mean?"
        e "A secret society of humans and monsters did something {i}secret{/i}."
        c "Oh, then just say that."
        s "A few humans got {i}all{/i} monsters on board with some unofficial plan? And that's why no one knows what happened?"
        r "As if humans could pull something like that off."
        s "Well, wouldn't it have been humans {i}and{/i} monsters working together?"
        e "How romantic."
        r "History isn't about romance!"
        e "Hmm… [playerName] hasn't weighed in for a minute…"

        menu:
            "About the coalition theory?":
                jump d2s3z7disco
            "About romance?":
                jump d2s3z7toki
            "Yeah, I'm just gonna listen, actually.":
                jump d2s3z7nope

    label d2s3z7nope:
        $ increase_affinity("Roger", 1)
        $ increase_affinity("Lalonde", 1)
        $ increase_affinity("Scylla", 1)
        e "Oh, boo. You're no fun."
        m "I just think that maybe, as a human, I should spend some time listening to monster history first."
        e "Oh, very well, be {i}responsible{/i}."
        jump d2s3z8

    label d2s3z7toki:
        r "Oh please don't. One is bad enough."
        e "Well, I don't mean romantic like love. I mean like Romanticism, like a rejection of individualism, an appreciation for imagination and and passion and beauty…"
        r "What does {i}that{/i} have to do with anything?"

        menu:
            "Who cares what \"the rules\" are? Human or monster, everyone's just looking for a partner in crime.":
                jump d2s3z7tokie
            "It's inspiring to think humans and monsters could work together for the greater good.":
                jump d2s3z7tokis
            "Not much. If humans protected monsters, it was still probably in their own self-interest":
                jump d2s3z7tokir

    label d2s3z7tokie:
        $ increase_affinity("Lalonde", 1)
        $ increase_affinity("Enzo", 1)
        e "Precisely."
        jump d2s3z8

    label d2s3z7tokis:
        $ increase_affinity("Lalonde", 1)
        $ increase_affinity("Scylla", 1)
        s "Yeah!"
        jump d2s3z8

    label d2s3z7tokir:
        $ increase_affinity("Roger", 1)
        r "Exactly."
        jump d2s3z8

    label d2s3z7disco:
        c "Yeah, say something smart, best friend. Get us back on track!"
        m "(Oh, sure, easier said than done!)"

        menu:
                "It's a little far-fetched. Working in secret without state institutions?":
                    jump d2s3z7morA
                "I love it! The will of the people in defiance of a ruling class thirsting for war!":
                    jump d2s3z7mazA
                "A much simpler explanation is just that they all got killed, right?":
                    jump d2s3z7fasA
                "It doesn't matter if the state was involved or not. Money's what makes these things happen.":
                    jump d2s3z7ultA

    label d2s3z6morA:
        $ increase_affinity("Scylla", 1)
        s "Yeah… good point. I can't even get my volleyball team to do things they said they'd do."
        jump d2s3z8

    label d2s3z6fasA:
        $ decrease_affinity("Roger", 1)
        $ decrease_affinity("Lalonde", 1)
        $ decrease_affinity("Scylla", 1)
        r "Wow, don't sound too excited about it."
        jump d2s3z8

    label d2s3z6ultA:
        $ increase_affinity("Roger", 1)
        r "Not wrong there."
        jump d2s3z8
            
    label d2s3z6mazA:
        $ increase_affinity("Lalonde", 1)
        $ increase_affinity("Enzo", 1)
        r "Oh for crap's sake…"
        e "THE REVOLUTION IS AT HAND!"
        jump d2s3z8

    label d2s3z8:
        m "(Class continued somewhat chaotically until the bell rang.)"

    if check_affinity_flexible("Lalonde", 6):
        l "[playerName], do you have a moment?"
        l "I'm curious where you're thinking about applying to college."
        l "Based on your interests in class… I think you might be a good candidate for Vampire Academy."
        m "Wow! You think so? Isn't it impossible to get in, though?"
        l "It {i}does{/i} have a low acceptance rate."
        m "Yeah… the lowest."
        l "Well, that's nothing that hard work and a letter of recommendation can't help with."
        m "Are you saying you'd be willing to recommend me for Vampire Academy? {i}Me?{/i} {i}The{/i} Vampire Academy?" 
        m "It would be really cool to get in there…"
        l "Keep working hard! A letter alone won't get you in there, I assume you know."
        jump PaS

    label PaS:
        $ lowest_affinity = min(affinities, key=affinities.get)

        if lowest_affinity == "Roger":
            jump D2S4es
        elif lowest_affinity == "Scylla":
            jump D2S4er
        elif lowest_affinity == "Enzo":
            jump D2S4sr