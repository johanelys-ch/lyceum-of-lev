

style button_text:
    size 25

style button:
    padding(10,10)
    xsize 40
    ysize 50
screen application_form_one():
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
            ypos 0.1
            spacing 20  
            xpos 0.2

            text "Select the classes you attended" color "#000000"
            text "over the last 4 years:" color "#000000"

            viewport:
                xsize 550
                ysize 150 
                draggable True  
                mousewheel True
                scrollbars "vertical"
                
                vbox:
                    text "Scroll to see more" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("American_Literature")
                        text "American Literature" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("British_Literature") 
                        text "British Literature" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Contemporary_Literature")
                        text  "Contemporary Literature" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Creative_Writing") 
                        text "Creative Writing" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Communication_Skills") 
                        text  "Communication Skills" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Debate") 
                        text "Debate" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("English_Language_and_Composition") 
                        text "English Language and Composition" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("English_Literature_and_Composition") 
                        text "English Literature and Composition" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Humanities") 
                        text "Humanities" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Journalism") 
                        text "Journalism" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Literary_Analysis") 
                        text "Literary Analysis" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Modern Literature") 
                        text "Modern_Literature" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Poetry") 
                        text  "Poetry" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Popular_Literature") 
                        text "Popular Literature" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Rhetoric") 
                        text  "Rhetoric" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Shakespeare") 
                        text  "Shakespeare" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Technical_Writing") 
                        text  "Technical Writing" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("World_Literature") 
                        text  "World Literature" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Written_and_Oral_Communication") 
                        text  "Written and Oral Communication" color "#000000"
            # Checkbox Section
            text "What were your" color "#000000"
            text "extracurriculars?" color "#000000"
            grid 2 3:
                    top_margin 25
                    hbox:
                        textbutton "✓" action ToggleVariable("Football")
                        text "Football" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Track")
                        text "Track" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Figure_Skating")
                        text "Figure Skating" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Drama_Club")
                        text "Drama Club" color "#000000"
                    hbox:
                        textbutton "✓" action ToggleVariable("Debate_Club")
                        text "Debate Club" color "#000000"
            text "Who was your guidance counselor?:"  xalign 0.5 color "#000000"
            grid 2 2:
                top_margin 10
                xspacing 200
                yspacing 40
                style_prefix "button_form_textbutton_prefix_button"
                textbutton ("✓ Harry Wolf" if guidance_counselor == "Harry Wolf" else "Harry Wolf?") action SetVariable("guidance_counselor", "Harry Wolf") 
                textbutton ("✓ Mr. Goolishvilli" if guidance_counselor == "Mr. Goolishvilli" else "Mr. Goolishvilli?") action SetVariable("guidance_counselor", "Mr. Goolishvilli") 
                textbutton ("✓ Dr. Funklestein" if guidance_counselor == "Dr. Funklestein" else "Dr. Funklestein?") action SetVariable("guidance_counselor", "Dr. Funklestein") 
                textbutton ("✓ Miss Luvsblud" if guidance_counselor == "Miss Luvsblud" else "Miss Luvsblud?") action SetVariable("guidance_counselor", "Miss Luvsblud")
            textbutton "Submit" action Return(True) xpos .2 top_margin 15

# Dropdown Menu
screen dropdown_menu():
    frame:
        background "#F4E1C1"
        vbox:
            for option in dropdown_options:
                textbutton option action [SetVariable("dropdown_selection", option), Hide("dropdown_menu")] text_color "#000000"
