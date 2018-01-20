# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define old_man = Character("Mysterious Old Man")

# Game Start
label start:

    # scene file_name: background file_name.png or file_name.jpg must be somewhere in images folder

    scene dark_school
    
    play music "sounds/music/night.mp3" fadeout 1

    # show file_name: character sprite file_name.png or file_name.jpg must be somewhere in images folder
    show kek:
        xalign 0.5
        yalign 0.4

    old_man "Uhhhhnn I sure do love me some fresh young kids."

    old_man "What's your name young man?"
    
    python:
        player_name = renpy.input("Your name: ")
        player_name = player_name.strip() or "Soot Taymem"
    
    old_man "Mmmm I see, I won't forget you [player_name]"
    
    define player = Character("[player_name]")
    
    player "..."
    
    # Game End
    return
