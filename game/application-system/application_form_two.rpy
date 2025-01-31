screen application_form_two():
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
            viewport:
                draggable True  
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 20  
                    vbox:
                        text "What’s your ideal weekend?"
                        vbox:
                            spacing 50
                            textbutton "Pool party! Beach party! Both!" action SetVariable("Answer_1", "1") xsize 800
                            textbutton "Reading outside with friends then sharing a meal" action SetVariable("Answer_1", "2") xsize 800
                            textbutton "Going to the opera, so long as they’re not performing something awful" action SetVariable("Answer_1", "3") xsize 800
                        vbox:
                            text "What’s your favorite type of movie?"
                        vbox: 
                            textbutton "Something with lots of jokes and action" action SetVariable("Answer_2", "1") xsize 800
                            textbutton "Something sad with subtitles" action SetVariable("Answer_2", "2") xsize 800
                            textbutton "Books" action SetVariable("Answer_2", "3") xsize 800
                    vbox:
                        text "What is your biggest weakness?"
                        vbox:
                            textbutton "I don’t try very hard" action SetVariable("Answer_3", "1") xsize 800
                            textbutton "I have a lot to learn" action SetVariable("Answer_3", "2") xsize 800
                            textbutton "I haven’t attained my most powerful form" action SetVariable("Answer_3", "3") xsize 800
                    vbox:
                        text "When learning a new hobby…"
                        vbox:   
                            textbutton "I just wing it. It’s just for fun!" action SetVariable("Answer_4", "1") xsize 800
                            textbutton "I’ll do some research about where to get started" action SetVariable("Answer_4", "2") xsize 800
                            textbutton "It’s honestly just to make important connections for later" action SetVariable("Answer_4", "3") xsize 800
                    vbox:
                        text "What is the color of your energy?"
                        vbox: 
                            textbutton "Desert rose" action SetVariable("Answer_5", "1") xsize 800
                            textbutton  "Um... Am I on the right website?" action SetVariable("Answer_5", "2") xsize 800
                            textbutton "Black, like my soul" action SetVariable("Answer_5", "3") xsize 800
                    vbox:
                        text "What is your favorite herb or spice?"
                        vbox:   
                            textbutton "basil" action None
                            textbutton "cilantro" action None
                            textbutton "paprika" action None
                    vbox:
                        text "Are you a dog person or a cat person?"   
                        vbox:
                            textbutton "Any cute animal, I don't care!" action SetVariable("Answer_7", "1") xsize 800 ysize 100
                            textbutton "Cats' independence is lovely, but dogs are great if you have time." action SetVariable("Answer_7", "2") xsize 800 ysize 100
                            textbutton "Dogs. You can train a dog. Cats are just, like, THERE. GET A JOB." action SetVariable("Answer_7", "3") xsize 800 ysize 100
                    textbutton "Submit" action Return(True) align (0.5, 0.5)

