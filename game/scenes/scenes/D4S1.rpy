label D4:
    if d4:
        jump D4S0
        
label D4S1:
# title card saying day 4… but then it changes to day 84
# go to the front of the school
    c "I can't believe we're so close to graduation already…"
    m "Yeah, the semester really flew by."
    m "It's like the more exciting senior year got, the faster time went…"
    m "(It's definitely been an interesting last semester of school…)"

    if not dC:
        m "I can't believe I started dating someone right before we all go to college…"
        c "Yeah, you went {i}wild{/i}."
        # colette z snaps
        m "I don't feel very wild now…"
        jump D4S1b

    elif Colenzo:
        c "Oh my god, same… although I know we're going to the same school so…"
        c "Wow, what a sense of… stability… from dating {i}Enzo{/i}... unexpected…"
        m "Ahem."
        c "Sorry. I know you'll do what's best for you, best friend!"
        jump D4S1b

    else:
        jump D4S1b

label D4S1b:
    m "I mostly just feel… dread? Because I feel so happy? Like…"
    m "The birds are singing, but it's not ok that the birds are singing."
    c "Wow, dramatic."
    c "I'm here for it."
    jump D4S2

label D4S2:
    # classroom setting
    l "You've all worked so hard this semester. I'm excited how much I've gotten to see all of you grow and prepare to see the world."
    e "Even me?"
    l "Even you, Enzo."
    c "Even {i}me{/ii}?"

    if Colenzo:
        l "...god, you two are an annoying couple."
        c "Damn, girl, can you say that?"
        jump D4S2a
    if not Colenzo:
        l "Yes, obviously."
        jump D4S2a

label D4S2a:
    l "You're all pursuing such exciting things!"
    l "Colette is taking photography and business classes at Frights High Community College while she begins her modeling career with Morgue…"
    l "Enzo is also going to Frights High Community College and taking courses in education."
    e "My legacy will be to train a generation of even more powerful pranksters."
    l "Scylla is going to Black Lagoon University."
    
    if dS:
        s "I'm so excited about the volleyball team! I could go pro!"
        jump D4S2b
    if not dS:
        s "My parents really want me to do pre med. Gotta make them proud!"
        jump D4S2b

label D4S2b:
    l "And our very own Roger Rizz was accepted to Vampire Academy."
    r "My destiny is being fulfilled…"
    l "[playerName], you got into…"
    # code to list off all the schools player got into

    if Va:
        l "I {i}knew{/i} you could get into Vampire Academy, [PlayerName]. You should be very proud."
    
    if dS:
        jump D4S4s
    elif dR:
        jump D4S4rz1
    elif dE:
        jump D4S4e
    elif dC:
        jump d4s4x