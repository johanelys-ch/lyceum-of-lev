label D4:
    if d4:
        jump D4S0
        
label D4S1:
# title card saying day 4… but then it changes to day 84
    scene bg_school_front with fadehold
    show colette_confused
    c "I can't believe we're so close to graduation already…"
    m "Yeah, the semester really flew by."
    m "It's like the more exciting senior year got, the faster time went…"
    m "(It's definitely been an interesting last semester of school…)"
    hide colette_confused

    if not dC:
        show colette_laugh
        m "I can't believe I started dating someone right before we all go to college…"
        c "Yeah, you went {i}wild{/i}."
        m "(Colette z snaps)"
        m "I don't feel very wild now…"
        hide colette_laugh
        jump D4S1b

    elif Colenzo:
        show colette_smile
        c "Oh my god, same… although I know we're going to the same school so…"
        c "Wow, what a sense of… stability… from dating {i}Enzo{/i}... unexpected…"
        m "Ahem."
        show colette_blush
        c "Sorry. I know you'll do what's best for you, best friend!"
        hide colette_smile
        hide colette_blush
        jump D4S1b

    else:
        jump D4S1b

label D4S1b:
    show colette_smile
    m "I mostly just feel… dread? Because I feel so happy? Like…"
    m "The birds are singing, but it's not ok that the birds are singing."
    c "Wow, dramatic."
    show colette_smirk
    c "I'm here for it."
    hide colette_smile
    hide colette_smirk
    jump D4S2

label D4S2:
    scene bg classroom
    show lalonde_normal
    l "You've all worked so hard this semester. I'm excited how much I've gotten to see all of you grow and prepare to see the world."
    hide lalonde_normal
    show enzo_surprise
    e "Even me?"
    hide enzo_surprise
    show lalonde_normal
    l "Even you, Enzo."
    hide lalonde_normal
    show colette_awe
    c "Even {i}me{/ii}?"
    hide colette_awe

    if Colenzo:
        show lalonde_confused
        l "...god, you two are an annoying couple."
        hide lalonde_confused
        show colette_confused
        c "Damn, girl, can you say that?"
        hide colette_confused
        jump D4S2a
    if not Colenzo:
        show lalonde_normal
        l "Yes, obviously."
        jump D4S2a

label D4S2a:
    l "You're all pursuing such exciting things!"
    l "Colette is taking photography and business classes at Frights High Community College while she begins her modeling career with Morgue…"
    l "Enzo is also going to Frights High Community College and taking courses in education."
    hide lalonde_normal
    show enzo_smirk
    e "My legacy will be to train a generation of even more powerful pranksters."
    hide enzo_smirk
    show lalonde_normal
    l "Scylla is going to Black Lagoon University."
    hide lalonde_normal
    
    if dS:
        show scylla_laugh
        s "I'm so excited about the volleyball team! I could go pro!"
        hide scylla_laugh
        jump D4S2b
    if not dS:
        show scylla_smile
        s "My parents really want me to do pre med. Gotta make them proud!"
        hide scylla_smile
        jump D4S2b

label D4S2b:
    show lalonde_normal
    l "And our very own Roger Rizz was accepted to Vampire Academy."
    hide lalonde_normal
    show roger_smile
    r "My destiny is being fulfilled…"
    hide roger_smile
    show lalonde_normal
    l "[playerName], you got into…"
    hide lalonde_normal
    # code to list off all the schools player got into

    if Va:
        show lalonde_normal
        l "I {i}knew{/i} you could get into Vampire Academy, [playerName]. You should be very proud."
        hide lalonde_normal
    
    if dS:
        jump D4S4s
    elif dR:
        jump D4S4rz1
    elif dE:
        jump D4S4e
    elif dC:
        jump d4s4x