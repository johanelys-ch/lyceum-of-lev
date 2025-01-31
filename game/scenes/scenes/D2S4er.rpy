label D2S4er:
        m "(I started walking home and saw Roger and Enzo in front of the school.)"
        m "(Enzo looked a little too excited. Roger looked like he just wanted to leave.)"
        show enzo_angry at right
        show roger_serious at left
        e "Perfect timing! Tell Roger he's being a total killjoy."
        r "Or maybe you can tell Enzo that their so-called \"plan\" is a waste of everyone's time."
        m "(...What did I just walk into?)"
        m "What's going on?"
        e "What's going on is that I came up with the best prank ever, and Roger here hates fun."
        r "That's not true. I don't hate fun—I just hate {i}your{/i} version of it."
        e "Okay, hear me out, here's the plan: we fill Lalonde's classroom with balloons full of confetti—like, so many balloons." 
        e "First, everyone just thinks \"Whoa! So many balloons!\" or something to that effect."
        e "But {i}imagine{/i} what will happen once one or two were to pop. Legendary!"
        m "(Roger scoffed.)" 
        r "Legendary? You're just wasting everyone's time and resources for what? A few weary laughs and a detention?"
        e "Come on, Roggie! It's harmless, fun, and I just want to have a good time, okay? Don't kill the vibe like this."
        show roger_angry at left
        r "It's Roger, and someone has to be the voice of reason here. Can't let the poopies run astray." 
        r "This is starting to look like a madhouse."
        e "Whatever, you're just mad that someone here knows how to have real fun."
        r "Not mad. Just annoyed. You think you can get away with turning the school into your personal playground."
        show enzo_confused at left
        e "Lighten up, man. It's harmless!"
        e "Hey, what do you think, [playerName]? You're in, right?" 
        e "Just imagine Lalonde's face when she opens the door tomorrow and there are just a hundred balloons waiting to unleash the power of confetti."
        r "Don't encourage their mischief. I thought dealing with poopies was the worst but wow, Enzo, you're way up there."
        m "(They're both looking at me now. Do I really have to choose between them?)"
        hide enzo_confused
        hide roger_angry

        menu:
                "I don't know, Enzo… I think you need {i}two{/i} hundred balloons.":
                        jump d2s4erz4
                "I think Roger's right. It's not worth the trouble.":
                        jump d2s4erz5
                "Can't you two agree on something for once?":
                        jump d2s4erz6

        label d2s4erz4:
                $ increase_affinity("Enzo", 2)
                $ decrease_affinity("Roger", 1)
                show enzo_smirk at right
                show roger_concerned at left
                e "Now {i}that's{/i} a college-bound brain in action. Take notes, Roggie."
                r "Of course, I knew you'd side with the class clown. Poopies are so predictable."
                e "I knew I could count on you! Alright, Roggie, looks like you're outvoted."
                r "What voting?! This is a sham election."
                r "Ugh, this is why democracy doesn't work…"
                e "Which is it, Roggie? Am I mocking democracy or is democracy already a mockery? Can't be both."
                r "You know what I mean! Ugh!"
                r "Fine. Do whatever you want. Just don't come crying to me when it all goes to caca."
                r "You know what? You won't even be able to." 
                r "Because soon I'll be at Vampire Academy and doing something with my life."
                r "And you'll still be in this town, an aging has-been with a fanbase withering to nothing."
                m "(Roger stormed off, muttering something under his breath.)"
                hide roger_concerned
                show enzo_serious
                m "(I looked back at Enzo, who for once had nothing to say…)"
                hide enzo_serious
                jump d2s5ez1

        label d2s4erz5:
                $ increase_affinity("Enzo", 2)
                $ decrease_affinity("Roger", 1)
                show enzo_serious at right
                show roger_smirk at left
                e "What?! You're seriously siding with him?"
                r "At least there's one other person at this dumb school with some common sense…"
                e "Everyone's gonna wish they were in on it!"
                hide enzo_serious
                show roger_smirk
                m "(Enzo walked away, sulking. Roger looked... happy?)"
                hide roger_smirk
                jump D2S5rz1

        label d2s4erz6:
                $ decrease_affinity("Enzo", 1)
                $ decrease_affinity("Roger", 1)
                show enzo_serious at right
                show roger_concerned at left
                m "Can't you two agree on something for once?"
                e "Agree? With him? Not a chance."
                r "The day I agree with Enzo is the day I lose all faith in poopies. No, in the entire universe."
                m "(They both glared at each other before walking off in opposite directions.)"
                hide roger_concerned
                hide enzo_serious
                m "(...What just happened?)"
                m "(That was... tense.)"
                m "(I guess I should probably go after one of them to make sure they're ok…)"

        menu: 
                "Enzo":
                        jump D2S5ez1
                "Roger":
                        jump D2S5rz1