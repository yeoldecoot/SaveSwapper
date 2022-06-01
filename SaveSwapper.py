#imports
import os
import json
from os.path import exists
import shutil

# return all of the paths from a certain directory
# includes root in path
def getDirPaths(Dir):
    d = os.listdir(Dir)
    dirPaths = []
    for i in range(len(d)):
        dirPaths.append(str(f"{Dir}\{d[i]}"))
    return dirPaths

# unloads the currently loaded profile
def unload(path):
    source = path
    with open("Loaded.json", 'r') as f:
        destination = json.load(f)
    shutil.move(source,destination)

# loads the selected profile
def load(data,gameProfile,gameVersion):
    source = data['profilePaths'][int(gameProfile)-1]
    destination = data['targetPath']
    shutil.move(source,destination)
    os.startfile(data['shortcutPaths'][int(gameVersion)-1])
    with open("Loaded.json", 'w') as f:
        json.dump(source, f)

# creates a Path.json file with the given string
def InitPath():
    print("Please enter the path to the default profile i.e C:\\Users\\xxxx\\Documents\\Egosoft\X3AP")
    path = input()
    with open("Path.json", 'w') as f:
        json.dump(path,f)

#DRIVER CODE

# if Path.json doesn't exist create it using InitPath()
if not exists("Path.json"):
    InitPath()

# loads the contents of Path.json into a string
with open("Path.json",'r') as f:
    path = json.load(f)

# unload current profile
if exists("Loaded.json") and exists(path):
    unload(path)

# stores important data into an easily referenceable dictionary
data = {
    'shortcutPaths' : getDirPaths("Shortcuts"),
    'profilePaths' : getDirPaths("Profiles"),
    'targetPath' : path
}

# prompt the user to pick a game version from their list of versions
print("Select Game Version: ")
for i in range(len(data["shortcutPaths"])):
    print(f"{i+1}: {data['shortcutPaths'][i][10:][:-4]}")
gameVersion = input()

# prompt the user to pick a game profile from their list of profiles
print("Select Game Profile: ")
for i in range(len(data["profilePaths"])):
    print(f"{i+1}: {data['profilePaths'][i][9:]}")
print(f"{i+2}: Clear Active Profile")
gameProfile = input()

# if the user chooses to clear their active profile, this code runs
if gameProfile == str(i+2):
    if exists("Loaded.json"):
        os.remove("Loaded.json")
    quit()

# load the selected profile
load(data,gameProfile,gameVersion)


