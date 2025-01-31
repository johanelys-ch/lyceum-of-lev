label D4S4s:
    m "(After class, I found Scylla rummaging through her locker.)"
    s "Hi there, sweetiebutt."
    m "Sweetiebutt?"
    s "Oh, you know how I'm not good at pet names? I'm leaning into it."
    s "I've accepted who I am. Only the absolute worst pet names for you."
    m "In that context, I'm extremely flattered."
    m "(She's got some books on volleyball strategy.)" 
    m "Another book?"
    s "Yeah! One of the BLU girls recommended this one. It sounded so cool, I bought it right away."
    m "(She's been talking with other volleyball players starting at Black Lagoon University next semester.)"
    m "(It really got her excited about volleyball again.)"
    s "Well, speaking of which… we might as well rip off the band-aid."
    s "Have you decided which school you're going to?"

    if affinities[Scylla] >= 7:
        menu:
            # code so that only the schools the player got into actually appear as options
            "Frights High Community College":
                jump D4S4sLD
            "Black Lagoon University":
                jump D4S4ssame
            "Vampire Academy of Vermont":
                jump D4S4sLD

    else:
        jump D4S4sbad

label D4S4ssame:
    s "Really?! That… gosh, you don't know how happy that makes me."
    s "I'm so glad this is the start of something."
    m "(We'd talked about it a little bit over the year. Scylla didn't want to do long-distance.)"
    m "(She felt that, after all, our relationship helped her realize that it's important to put yourself first.)"
    s "I know you picked this because it's what's right for you, not just because of me."
    m "Yeah, I like a lot of their programs… and I've heard they've got cute girls there."
    s "Me???"
    s "You better mean me."
    m "Yes, that was indeed the joke."
    s "Aaaaaaahhhhhh I can't wait!"
    jump D4S4send

label D4S4sLD:
    s "I see…"
    s "Don't get me wrong, I'm happy for you."
    m "I know what this means though…"
    s "Yeah."
    m "(We'd talked about it a little bit over the year. Scylla didn't want to do long-distance.)"
    s "I've been prepared for this… after all, it's you who helped me realize that, for the big stuff, you have to put yourself first."
    s "I know your choice is because it's what's right for you, not because of me."
    m "We had a good run, didn't we?"
    s "No complaints here."
    s "Well… one complaint. It's bittersweet, isn't it?"
    m "It is…"
    m "But we don't know the future. Our paths could cross again."
    m "You'll be a volleyball professional… your team will be playing an away game in the capital…"
    s "The capital? What, are you going into politics?"
    m "Maybe! I've learned quite a lot about monster-human relations this year."
    s "Hmmm… I don't know if {i}that's{/i} the kind of monster-human relations they're looking for."
    m "Couldn't hurt though."
    s "Well, shucks, I'd hate to cause a national scandal!"
    s "Well… if we don't cause this scandal someday… the time we did have will always mean so much to me."
    s "I wish I met you {i}before{/i} senior year."
    s "But I'm glad we got there eventually, brief as it may have been."
    jump D4S4send
        
label D4S4sbad:
    s "I don't think this is working out…"
    s "I need to be honest about what I need. You helped me learn that, at least, even if actually dating you…"
    m "(Scylla trails off…)" 
    m "So we're breaking up?"
    s "Yeah. This didn't exactly go the way I expected… to be honest… I didn't feel like your heart was really in it…"
    m "(I wonder where things went wrong…)"
    m "(I guess we just hadn't made much progress since things were a little… lukewarm in the forest.)"
    m "(Still, Scylla learned something about herself from all this… what have {i}I{/i} learned about myself?)" 
    jump D4S4send

label D4S4send:
    return