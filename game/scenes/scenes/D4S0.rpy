label D4S0:
    m "(Word spread fast about what happened in the forest.)"

    if dC:
        show colette
        c "Roger was right when he said you were poopy caca."
        c "I guess we weren't such a dynamic duo in the end."
        hide colette
        jump D4S0d
        
    else:
        show scylla
        s "Roger was right when he said you were poopy caca."
        hide scylla

        show enzo
        show roger
        e "*nods*"
        r "*nods*"
        hide enzo
        hide roger
        m "(People drew away from me… at first I assumed it must be the others… the monsters living in secret…)"
        m "(Then it was so many, I wondered, it can't be all of them, right? Then I stopped wondering.)"
        c "Hey… I know what happened in the forest."
        c "I… want to hear it from you. What happened?"

        menu:
            "I freaked out. I didn't mean to hurt anyone.":
                jump D4S0a
            "I don't know… I don't think I'm attracted to monsters.":
                jump D4S0b
            "Monsters! Everywhere! We're surrounded!":
                jump D4S0c

label D4S0a:
    c "Well. Next time {i}don't{/i} hurt anyone."
    c "Think before you speak kinda thing."
    jump D4S0d

label D4S0b:
    c "But did you have to be a dick about it?"
    jump D4S0d

label D4S0c:
    c "..."
    c "I guess we weren't such a dynamic duo in the end."
    jump D4S0d  

label D4S0d:
    return