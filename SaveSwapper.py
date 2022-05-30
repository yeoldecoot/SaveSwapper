#imports
import os
import json
from os.path import exists
import shutil

#function that finds the difference between 2 arrays
#used in finding the last used profile and removing it

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

#return all of the paths from a certain directory
#includes root in path

def getDirPaths(Dir):
    d = os.listdir(Dir)
    dirPaths = []
    for i in range(len(d)):
        dirPaths.append(str(f"{Dir}\{d[i]}"))
    return dirPaths

#if the data.json file does not exist it is created here
#json contains: paths to each shortcut, path to each profile, and the path to the target profile that the program switches
def init():
    shortcutPaths = getDirPaths("Shortcuts")
    profilePaths = getDirPaths("Profiles")
    print("Please enter the path to the default profile i.e C:\\Users\\xxxx\\Documents\\Egosoft\X3AP")
    targetPath = input()
    data = {
        'shortcutPaths' : shortcutPaths,
        'profilePaths' : profilePaths,
        'targetPath' : targetPath
    }
    with open("Data.json", 'w') as f:
        json.dump(data,f)
        
#run init if Data.json doesn't exist
        
if not exists("Data.json"):
    init()
    
#read the data from Data.json
    
with open("Data.json",'r') as f:
    data = json.load(f)
    
#prompt the user to pick a game version from their list of versions
    
print("Select Game Version: ")
for i in range(len(data["shortcutPaths"])):
    print(f"{i+1}: {data['shortcutPaths'][i][10:][:-4]}")
gameVersion = input()

#prompt the user to pick a game profile from their list of profiles

print("Select Game Profile: ")
for i in range(len(data["profilePaths"])):
    print(f"{i+1}: {data['profilePaths'][i][9:]}")
gameProfile = input()

#get the last played profile from the difference between the total profiles and the current

currentProfiles = getDirPaths("Profiles")
totalProfiles = data['profilePaths']
lastProfile = Diff(totalProfiles, currentProfiles)

#return the last played profile to the profiles folder

if len(lastProfile) != 0:
    for i in data['profilePaths']:
        if lastProfile[0] == i:
            source = data['targetPath']
            destination = i
            shutil.move(source,destination)
            break
        
#move the selected profile to the target path
        
source = data['profilePaths'][int(gameProfile)-1]
destination = data['targetPath']
shutil.move(source,destination)
os.startfile(data['shortcutPaths'][int(gameVersion)-1])
