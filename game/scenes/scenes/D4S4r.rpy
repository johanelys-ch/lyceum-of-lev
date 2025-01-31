label D4S4rz1:
    scene bg bg_stairs with dissolve
    m "(After class, I met Roger in the stairs, our usual spot. His expression is hard to read, but there's something softer in his eyes when he looks at me.)"
    m "(It's been on my mind since the forest—our kiss, our future, everything. My heart feels like it's racing, even now.)"
    r "Hey, poopie. You came."
    m "Of course. Why wouldn't I?"
    m "Because you still call me \"poopie?\""
    m "(He smiles weakly. He looks lost, just how he did in the forest.)"
    m "What's going on?"
    r "..."
    r "I've been thinking about what's next for us after... well, the school year."
    m "(My cheeks warm as I think about the last few months. He's not making this easy for me.)"
    r "And I think we've got to figure it out—like, where we go from here. Together, or... not."
    m "What are you talking about?"
    m "(My heart skips. What does he mean by this?)"
    r "Do you know what you're doing after high school?"
    r "Have you decided which school you're going to?"

menu:
    # code so that only the schools the player got into actually appear as options
    "Frights High Community College":
        jump OP
    "Black Lagoon University":
        jump OP
    "Vampire Academy of Vermont":
        jump OP

# i have to review this logic again now that i have info on the Affinity System

label OP:
    if (affinities["Roger"] <= 5) or (affinities["Roger"] <= 5 and school != "Vampire Academy"):
        jump D4S4rBC

    elif school == "Vampire Academy":
        jump D4S4rVA

    elif affinities["Roger"] >= 6:
        jump D4S4rLD

label D4S4rBC:
    r "It's not just the schools or the change. It's us, poopie."
    m "What are you saying?"
    r "I'm saying... I don't think long-distance would work. Not with us, not like this."
    m "(I can't bring myself to argue. He's made up his mind and, honestly, I'm kind of in the same boat.)"
    m "I get it. Long-distance is probably not going to work."
    r "Yeah, this wouldn't be fair—not to you, not to me."
    m "(Even if it doesn't feel like it now, I know he's being honest. It doesn't make it easier, but it's a good thing we feel the same way.)"
    m "It was a great moment, though. No regrets here."
    m "(A shadow of a smile passes through Roger's lips, but he doesn't say anything back.)"
    m "(Maybe if we both made some choices differently this would've been a very different story.)"
    m "(Even though we part ways, I can feel his words lingering. It's not easy, but maybe it's for the best…)"
    m "(Even if it feels like my heart's stuck back on those stairs with him.)"
    jump D4S4end

label D4S4rVA:
    r "What? Seriously?"
    m "(My heart leaps. He can't hide the amusement in his face.)"
    m "I didn't want to say anything just in case I didn't get in. Especially since, you know…"
    m "It's sort of monsters-only over there. Mostly."
    r "I guess it turns out it's a good thing they let some humans in…"
    r "Guess you're stuck with me now, huh?"
    m "(I can't help but laugh. His grin is contagious.)"
    r "Wow, we're only getting started! You better be ready, [playerName]."
    m "With you? Always."
    m "Wait, what happened to calling me poopie?"
    r "Well, maybe someone showed me that some humans can actually care about monsters."
    r "And maybe I… well, this is embarrassing, but…"
    r "I use too much profanity."
    m "...uh huh."
    r "But if you like it so much, I guess I'll just need to keep calling you that."
    m "(It's always fun teasing Roger.)"
    m "(We smile at each other, knowing this is the beginning of something that could be amazing, or disastrous.)"
    m "(Either way, we're both happy we get to spend another stage of life together.)"
    jump D4S4end

label D4S4rLD:
    r "I mean the academy stuff. I'm going to Vampire Academy. And... well, you're not."
    m "But... maybe this doesn't have to be goodbye?"
    m "(He blinks, caught off guard by my suggestion… even though he said way back when he'd never do long-distance.)"
    m "(Way back when… the old Roger…)"
    r "Look…"
    r "..."
    r "I'm not great at this whole feelings thing, but I care about you. Enough to try long-distance, if you're up for it."
    r "I know I said I didn't want to, but hey, people change their minds all the time."
    m "(His voice is softer than usual, and I can feel how much this means to him.)"
    m "Of course I want to, Roger. "
    m "(His face lights up, though he tries to play it cool.)"
    r "I hope you really mean that. Don't think you're off the hook just because you're far away."
    r "Oh, you better not ghost me. I'll haunt you forever if you do."
    m "Ha, trust me. You're not getting rid of me that easily."
    m "Also, I know gremlins don't do hauntings. Your threats are {i}hollow{/i}."
    m "(He grins, his usual playfulness shining through, but I know this moment matters to him just as much as it does to me.)"
    m "I know we'll make it work... somehow."
    jump D4S4end

label D4S4end:
    return
