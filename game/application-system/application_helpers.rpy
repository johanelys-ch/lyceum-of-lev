init python:
    def calculate_day_one():
        global American_Literature
        global British_Literature
        global Contemporary_Literature
        global Creative_Writing
        global Communication_Skills
        global Debate
        global English_Language_and_Composition
        global English_Literature_and_Composition
        global Humanities
        global Journalism
        global Literary_Analysis
        global Modern_Literature
        global Poetry
        global Popular_Literature
        global Rhetoric
        global Shakespeare
        global Technical_Writing
        global World_Literature
        global Written_and_Oral_Communication
        classes = [American_Literature,
        British_Literature,
        Contemporary_Literature,
        Creative_Writing,
        Communication_Skills,
        Debate,
        English_Language_and_Composition,
        English_Literature_and_Composition,
        Humanities,
        Journalism,
        Literary_Analysis,
        Modern_Literature,
        Poetry,
        Popular_Literature,
        Rhetoric,
        Shakespeare,
        Technical_Writing,
        World_Literature,
        Written_and_Oral_Communication]
        attended_classes = [classy for classy in classes if classy]
        global community_college_score
        global vampire_score
        global lagoon_score
        if len(attended_classes) > 15:
            vampire_score += 1
        elif len(attended_classes)>8:
            lagoon_score += 1
        else:
            community_college_score += 1
        
        if Drama_Club:
           community_college_score += 1
        if Figure_Skating or Debate_Club:
            vampire_score += 1
        if Track or Football:
            lagoon_score += 1

    def calculate_day_two():
        global community_college_score
        global vampire_score
        global lagoon_score
        answers = [Answer_1,Answer_2,Answer_3,Answer_4,Answer_5,Answer_7]
        for answer in answers:
            if answer == "1":
                community_college_score += 1
            if answer == "2":
                lagoon_score += 1
            if answer == "3":
                vampire_score += 1
    def calculate_day_three():
        global community_college_score
        global vampire_score
        global lagoon_score
        if First_Choice == "Vampire Academy of Vermont":
            vampire_score += 1
        elif First_Choice == "Black Lagoon University" or Second_Choice == "Black Lagoon University":
            lagoon_score += 1
        
        community_college_score += 1
        if Monster_Affinity == "Medium":
            vampire_score -= 1
        elif Monster_Affinity == "Low":
            vampire_score -= 3

    def calculate_academy_score():
        global community_college_score
        global vampire_score
        global lagoon_score
        if community_college_score > 2:
            Community_College_Acceptance = True
        

        if vampire_score > 7 and Monster_Affinity == "High":
            Vampire_Acceptance = True

        if lagoon_score > 5:
            Lagoon_Acceptance = True
