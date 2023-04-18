# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pi = Character("Pious Man")
define aas = Character("Assassin")
define nar = Character("Narrator")

image bgMosque = "mosque.jpg"
image bgOutside = "outside.jpg"
image black = "black.jpg"

image ipi = "piousman.jpg"
image iaas = "assassin.jpg"
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
    
    show iaas at left
    
    aas "I am going to go assassinate the man. I got paid a lot!"
    
    show bgMosque
    
    show ipi at right
    
    aas "Here I am! I see you, o pious man!"
    
    pi "Hello, who are you?"
    
    aas "I am here to kill you!"
    
    pi "Please dont! It would only harm you more than it would harm me."
    
    aas "What? How?"
    
    pi "I don't want your status to decrease in society."
    
    aas "Wow, that's so touching. Alright, fine. I will decide to kill you tomorrow. IF you see me tomorrow, you will die that day. If you do not, consider yourself spared."
    
    pi "Alright, I accept."
    
    hide ipi
    
    hide iaas
    
    show black
    
    nar "The assassin went to sleep in the cave."
    
    show bgOutside
    
    nar "He was shown the city in flames. He was scared."
    
    show black
    
    nar "He was so scared he decided not to kill the man."
    
    nar "He found a cave on the outskirts of town and decided to rest there."
    
    show black
    
    nar "Some time passed."
    
    show ipi at left
    
    aas "Wow, what a great nap!"
    
    show bgOutside
    
    aas "Where is the pious man?"
    
    aas "Wow! The city has changed so much!"
    
    nar "Wonderful ending."

    return
