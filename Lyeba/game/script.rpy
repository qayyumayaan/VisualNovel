# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define piousman = Character("Pious Man")
define assassin = Character("Assassin")
define narrator = Character("Narrator")

image bgMosque = "mosque.jpg"
image bgOutside = "outside.jpg"
image black = "black.jpg"

image imagePiousman = "piousman.jpg"
image imageAssassin = "assassin.jpg"
# image cityInFlames = "cityInFlames.jpg"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # This ends the game.
    
    show bgOutside
    
    show imageAssassin at left
    
    assassin "I am going to go assassinate the man. I got paid a lot!"
    
    show bgMosque
    
    show imagePiousman at right
    
    assassin "Here I am! I see you, o pious man!"
    
    piousman "Hello, who are you?"
    
    assassin "I am here to kill you!"
    
    piousman "Please dont! It would only harm you more than it would harm me."
    
    assassin "What? How?"
    
    piousman "I don't want your status to decrease in society."
    
    assassin "Wow, that's so touching. Alright, fine. I will decide to kill you tomorrow. IF you see me tomorrow, you will die that day. If you do not, consider yourself spared."
    
    piousman "Alright, I accept."
    
    hide imagePiousman
    
    hide imageAssassin
    
    show black
    
    narrator "The assassin went to sleep in the cave."
    
    show bgOutside
    
    narrator "He was shown the city in flames. He was scared."
    
    show black
    
    narrator "He was so scared he decided not to kill the man."
    
    narrator "He found a cave on the outskirts of town and decided to rest there."
    
    show black
    
    narrator "Some time passed."
    
    show imagePiousman at left
    
    assassin "Wow, what a great nap!"
    
    show bgOutside
    
    assassin "Where is the pious man?"
    
    assassin "Wow! The city has changed so much!"
    
    narrator "Wonderful ending."

    return
