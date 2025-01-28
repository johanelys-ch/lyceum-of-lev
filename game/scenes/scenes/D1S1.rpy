# not game ready
label D1S1:
    label d1s1z1:
    scene classroom

    $ playerName = renpy.input("What's your name?", default = playerName)
    if playerName.strip() == "":
        $ playerName = "Micah"
        m "Alright, [playerName], let's get started."
#     l "As we all know, until about 500 years ago, there were monsters."
#     l "Villages, cities, entire countries where humans and monsters lived and worked together."
#     l "As is often the case, they had their conflicts. Disputes over resources and land. Cultural clashes. But despite their differences, the two largely coexisted peacefully."
#     l "Of course, now the monsters are gone."
#     l "You already know this. You're all going to graduate high school this year. This is not new information."
#     l "But, of course, the events surrounding why the humans drove the monsters away and how the monsters disappeared is a matter of debate, and will be a major focus of our class this semester."
#     e "What does it mean about history that sometimes we have these holes in the record of what happened? And does that only apply to the holes?"
#     l "..."
#     l "...Enzo, I heard that."

#      e "I didn't say anything! I'm excited to learn about getting holes filled this semester!"
#      m "(Everybody immediately groans at that one.)"
#      l "Enzo, do you want detention? Again?"
#      c "Aw, Ms. Lalonde! They aren't bothering anyone!" 
#      "Take them, for instance. Are they bothering you?"
#      m "(Crap. Thanks for getting me involved, best friend...)"
#      "(She's the one with a dumb soft spot for the class clown! What am I supposed to say to fix this?)"
     
#      $ increase_affinity("Enzo",5)
#     #  $ print(check_affinity("Enzo"))
#     #  $ print(check_enzo_friend()) 
#     #  $ print(check_affinity_max("Enzo")) 
#      $ print(check_affinity_flexible("Enzo",3))
#      $ print(check_affinity_flexible("Enzo",6))

# menu:
#     "...girl. Obviously.":
#         jump d1s1z3
#     "The innuendo is an improvement over the fart jokes.":
#         jump d1s1z2
#     "I don't understand what's happening. Can we please get back to the holes?":
#         jump d1s1z2

# label d1s1z2:
#      l "Oh… it's going to be a long year."
#      jump d1s1z3

# label d1s1z3:
#      m "It looks like Ms. Lalonde has decided to ignore all of this and get on with it."
#      "(She's really cool, though. She's happy to let us goof around a bit, and Enzo usually doesn't push it too far.)"
#      "(Usually.)"
#      m "(She's got such a crush on Enzo. I think she's still in denial about it… but it's obvious.)"
#      "(I might have to decide whether to encourage her or not… but they're both such goofballs, I don't know if they'd be perfect for each other or terrible for each other.)"
#      l "What we do know is that, 500 years ago, humans drove monsters out of the civilization they had shared and built together."
#      "Usually this is attributed to a single event: a series of high-profile disappearances of human children. What we don't know, and is still a matter of debate, is what happened to these children."
#      "But we do know that humans found a common enemy in monsters."
#      r "Friggin' humans, man."
#      s "But how could humans just force monsters out? I mean, in comparison to monsters, wouldn't humans be…"
#      e "Squishier?"
#      l "Society is complicated, and there are forms of power aside from just brute force."
#      "We do know that humans had fought amongst themselves for centuries – even before the disappearances – about how much they wanted to share the world with monsters."
#      "Some humans were content to share the world with monsters. Some weren't. And many simply didn't care all that much."
#      "Governments can pass laws that make it harder or easier to find housing, employment, or health care. Even if they don't, systems that maintain social order can choose what rules they do or do not enforce."
#      "Even if blatant discrimination is illegal, if it becomes too difficult to obtain recourse, people become discouraged. At that point, does it even matter what the law actually says?"

#      e "A world without rules…"
# menu: 
#     "Heck yeah! Rules are fake!":
#         jump d1s1z4
#     "It doesn't sound like monsters got to ignore the rules, though.":
#         jump d1s1z5
#     "But Enzo, if there are no rules, then there's nowhere to put the holes!":
#         jump d1s1z6

# label d1s1z4:
#     c "*z snaps*"
#     jump d1s1z7

# label d1s1z5:
#     l "Exactly."
#     jump d1s1z7

# label d1s1z6:
#     e "Oh no. What a conundrum."
#     e "Are rules… good?"
#     e "I guess if there are no rules… then there are no pranks…"
#     l "...you know what? I'll take it."
#     l "Yes, for instance, pranks are funny because they're a lighthearted breaking of the rules. If there are no rules to break, then how can you do a prank?"
#     l "And if your pranks never got a reaction from anyone, how long would you put in the effort before giving up on pranks?"
#     e "This is blowing my mind."
#     jump d1s1z7

# label d1s1z7:
#     r "Is this whole class just going to be about what humans did?"
#     "That's so anthropocentric, man! That's caca!"

# menu: 
#     "...anthropocentric?":
#         jump d1s1z8
#     "...caca?":
#         jump d1s1z9
#     "...Roger? Wait, are you even in this class?":
#         jump d1s1z10

# label d1s1z8:
#     r "It means that everything is framed in terms of what it means to humans. If humans have nothing to do with it, it doesn't make it into the history books."
#     "It's a system of oppression, man!"
#     jump d1s1z11

# label d1s1z9:
#      r "I'm just saying, man."
#      "It means that everything is framed in terms of what it means to humans. If humans have nothing to do with it, it doesn't make it into the history books."
#      "It's a system of oppression, man!"
#      jump d1s1z11

# label d1s1z10:

#      r "I, uh, I just transferred."

#      m "(Ms. Lalonde seems to be looking at some papers on her desk…)"
#      "(She seems to have decided not to bother right now.)"
#      jump d1s1z11

# label d1s1z11:
#      s "So, wait, humans did all that to kick monsters out before the disappearances?"
#      "Then what did they do when the disappearances began…"
#      l "Well, this is what's still a matter of debate. And maybe it always will be."
#      "All we know for certain is that human children began to disappear, then humans blamed the monsters, and then, shortly after that, the monsters vanished."
#      "The only written records we have are from humans. And it's not like there are monsters around to talk to today."
#      r "So, what, we're just gonna read a bunch of propaganda in this class?"
#      l "Not exactly. We're not just going to read. We're also going to ask why."

# menu:
#     'Like "Why are we doing this?"':
#         jump d1s1z12
#     'Like ”Why did the person who wrote this conclude this?”':
#         jump d1s1z13
#     'Like "Why did the person who wrote this want people to think this?”':
#         jump d1s1z13 
#     "(This sounds so hard. I'm gonna smooch someone eventually, right?)":
#         jump d1s1z14

# label d1s1z12:
#      jump d1s1z15

# label d1s1z13:
#      l "You have the right idea."
#      jump d1s1z15

# label d1s1z14:
#      m "(Yeah, I mean, this is my last year of high school. I might never see most of these people again in my life.) (Who could I smooch?)"
#      m "(No. Too weird. Way too weird.)"
#      m "(I mean… they are cute…)"
# # hide Enzo
# # show Scylla
#      m "(She's cute…)"
#      m "He could be cute if he weren't such a bummer all the time…"
#      m "(...)NOPE. NOPE. Let's think about something else now. What were we talking about?"

# menu:
#     'Like "Why are we doing this?"':
#         jump d1s1z12
#     'Like ”Why did the person who wrote this conclude this?"':
#         jump d1s1z13
#     'Like "Why did the person who wrote this want people to think this?"':
#         jump d1s1z13 

# label d1s1z15:
#      m "(For the rest of the class, we talked about a few different historians we'll be studying the rest of the semester.)"
#      "(Roger only complained about most of them.)"

    jump D1S2