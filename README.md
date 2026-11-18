# airotracestj

some generalised bits as of 17/11/26 -> will supplement once working model coded

    expansion of capabilities long term
        1. Machine Learning based gesture recognition
            The system can propose a "menu" of gestures (swipe across, up and down etc.)
            The user then chooses a gesture and is asked to preform the gesture several times (akin to "hey siri" voice recognition)
            The system then, through machine learning, can identify the different signals, tuning a pretrained dataset
            Interestig video by 'Mark Rober' on youtube explains the basics -> search 'Mark Rober Baseball Sign Stealing" -> not going to teach you entirely (if at all) but is a good start conceptually
        
        2. Direct to PC connection
            Microbit (or other microcontroller like ESP32) connects directly to PC, eliminating intermediary microbit
            likely a library for this!



working model as of 18/11/26 functionality:
    slide switching wirelessly

future capabilities for 1-2 month timeframe of work
    
    1. back switching ie -> going forward and backwards in slide
        to implement this functionality, instead of taking the "strength" of acceleration from the microbits, you will have to take the actual acceleration data in mg. This will be a bit tricky to implement especially if      you are unfamiliar with python but I have attached some useful resources to get you started if you desire!!


useful resources:

https://stackoverflow.com/questions -> online forum for coding help
https://youtube.com/@brocodez?si=TWe3qHCbfQipiH4B -> great youtube channel for not just python but most coding languages if it interests you
https://www.youtube.com/watch?v=PmlRbfSavbI -> mark rober sign stealing video to understand basics of machine learning
https://www.w3schools.com/ -> great for coding resources


i'd recommend if you want to develop the project further, try to keep as much of the work/learning done by hand (non-ai) unless you are totally stumped. helps with future ease of debugging etc. and is arguably more fun!

go n-éirí an t-ádh leat!
