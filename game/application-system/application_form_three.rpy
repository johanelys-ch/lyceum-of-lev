screen application_form_three():
    frame:
        xsize 1920 
        ysize 1080  
        background "#FFFFFF"  
        align (0.5, 0.5)
    frame:
        
        align (0.5, 0.5) 
        xsize 800  
        ysize 1000
        background "#F4E1C1" 
        vbox:
            vbox:
                text "What’s your first school choice?"
                vbox:
                    textbutton "Vampire Academy Of Vermont" action SetVariable("First_choice", "Vampire Academy of Vermont") xsize 800
                    textbutton "Black Lagoon University" action SetVariable("First_Choice", "Black Lagoon University") xsize 800
                    textbutton "Frights High Community College" action SetVariable("First_Choice", "Frights High Community College") xsize 800
            vbox:
                text "What's your second school choice?"
                vbox: 
                    textbutton "Vampire Academy Of Vermont" action SetVariable("Second_Choice", "Vampire Academy of Vermont") xsize 800
                    textbutton "Black Lagoon University" action SetVariable("Second_Choice", "Black Lagoon University") xsize 800
                    textbutton "Frights High Community College" action SetVariable("Second_Choice", "Frights High Community College") xsize 800
            vbox:
                text "What's your third school choice?"
                vbox:
                    textbutton "Vampire Academy Of Vermont" action SetVariable("Third_Choice", "Vampire Academy of Vermont") xsize 800
                    textbutton "Black Lagoon University" action SetVariable("Third_Choice", "Black Lagoon University") xsize 800
                    textbutton "Frights High Community College" action SetVariable("Third_Choice", "Frights High Community College") xsize 800
            vbox:
                text "How do you feel about monsters?"
                vbox:   
                    textbutton "Monsters fascinate and excite me!" action SetVariable("Monster_Affinity", "High") xsize 800
                    textbutton "They're ok.. They're monsters, yah know?" action SetVariable("Monster_Affinity", "Medium") xsize 800
                    textbutton "Get em outta here! We don't need no stikin monsters." action SetVariable("Monster_Affinity", "Low") xsize 800
                    
            textbutton "Submit" action Return(True) align (0.5, 0.5)

