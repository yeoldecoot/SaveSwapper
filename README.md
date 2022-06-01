# SaveSwapper
A simple game manager for when you have multiple installations and save profiles of a game (i.e. modded and vanilla) when they share the same save location

# Installation
Video Guide: https://www.youtube.com/watch?v=EBFfORrAdOQ  
1: If you don't already have it, download python here: https://www.python.org/  
2: Download the latest release  
3: Extract it somewhere  
4: Create a shortcut for each instance of your game and place them in the shortcuts folder  
5: Move all of your profile backups into the profile folder  
6: launch the SaveSwapper.py file  
7: you will be prompted to enter the path to the profile that is actually loaded by the game (for x3 this is C:\Users\xxxxx\Documents\Egosoft\X3AP)  
NOTE: from then on there will be a new file (Data.json) where you launched SaveSwapper.py. currently the only way to refresh your profiles and shortcuts is to delete that file 

# What it does
1. If Path.json does not exist, prompt the user to enter the path to their default profile that they want to be swapped.
2. Unload the current profile if there is one. this will not run unless Loaded.json exists.
3. Prompt the user to select a game version.
4. Prompt the user to select a game profile.
5. If the user chooses to clear their active profile the program exits without launching a game version.
6. Load the selected profile.
7. Launch the selected game version.
8. update Loaded.json

# Future Plans
I would like to implement a GUI for the save swapper to make it look better. I've also toyed with the idea of wrapping it in an exe somehow so people can add the manager as a non-steam game to their steam library.
