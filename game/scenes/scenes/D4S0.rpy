label D4S0:
    scene bg_school_front with dissolve
    m "(Word spread fast about what happened in the forest.)"

    if dC:
        show colette_confused
        c "Roger was right when he said you were poopy caca."
        c "I guess we weren't such a dynamic duo in the end."
        hide colette_confused
        jump D4S0d
        
    else:
        show scylla_confused
        s "Roger was right when he said you were poopy caca."
        hide scylla_confused

        show enzo_angry
        show roger_angry
        e "*nods*"
        r "*nods*"
        hide enzo_angry
        hide roger_angry
        m "(People drew away from me… at first I assumed it must be the others… the monsters living in secret…)"
        m "(Then it was so many, I wondered, it can't be all of them, right? Then I stopped wondering.)"
        show colette_confused
        c "Hey… I know what happened in the forest."
        c "I… want to hear it from you. What happened?"
        hide colette_confused

        menu:
            "I freaked out. I didn't mean to hurt anyone.":
                jump D4S0a
            "I don't know… I don't think I'm attracted to monsters.":
                jump D4S0b
            "Monsters! Everywhere! We're surrounded!":
                jump D4S0c

label D4S0a:
    show colette_confused
    c "Well. Next time {i}don't{/i} hurt anyone."
    c "Think before you speak kinda thing."
    jump D4S0d

label D4S0b:
    show colette_confused
    c "But did you have to be a dick about it?"
    jump D4S0d

label D4S0c:
    show colette_confused
    c "..."
    c "I guess we weren't such a dynamic duo in the end."
    jump D4S0d  

label D4S0d:
    hide colette_confused
    scene bg_gym with dissolve
    m "(I went to the gym knowing that it was going to be empty.)"
    m "(It felt weird... being alone after all this time.)"
    m "(I heard a sound coming from the other side, and when I looked over...)"
    m "What the...?"
    scene bg_chickenkiss
    m "Am I... is this... What?"
    return