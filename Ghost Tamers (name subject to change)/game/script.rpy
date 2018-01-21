# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define old_man = Character("Mysterious Old Man")

# Game Start
label start:
    # scene file_name: background file_name.png or file_name.jpg must be somewhere in images folder
    # show file_name: character sprite file_name.png or file_name.jpg must be somewhere in images folder
    # play music file_path: play looping music file file_path (path starts in game folder), add fadeout x to fadeout in x sec when next music plays
    # play sound file_path: play sound file file_path once (path starts in game folder)
    scene dark_school
    play music "sounds/music/night.mp3" fadeout 1
    
    show kek:
        xalign 0.5
        yalign 0.4

    old_man "Uhhhhnn I sure do love me some fresh young kids."

    old_man "What's your name young man?"
    
    python:
        player_firstname = renpy.input("Enter your first name: ")
        player_firstname = player_firstname.strip() or "Soot Taymem" # Default if player enters no name

        player_lastname = renpy.input("Enter your last name: ")
        player_lastname = player_lastname.strip() or "Soot Taymem" # Default if player enters no name
    
    old_man "Mmmm I see, I won't forget you [player_firstname] [player_lastname]"
    
    define player = Character("[player_firstname]")
    
    player "..."
    
    # Game End
    return
