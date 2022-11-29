#! /bin/python3
from player import Player
import json

def main():
  global players
  players = []
  importDB()
  
def importDB():
  f = open("playerDB.json")
  db = json.load(f)

  for player in db['players']:
    players.append(Player(player['name'],player['MMR']))

  print(players)

#figure out how many 3 and 4 man pods are needed.
def numPods(numple):
  numple = int(numple)
  
  if (numple == 3):
    return [1,0]
  elif (numple == 4):
    return [0,1]
  elif(numple%4 == 0):
    return [0,numple/4]
  else:
    threes = 4-numple%4
    return [threes,numple-threes/4]

def genPods():
  if(len(players) == 1 or len(players) ==2):
    #TODO:Admonish TO for trying to make a pod with 1 or 2 players
  if(len(players) == 3 or len(players) == 4 or len(players) == 5):
    #TODO: Make one pod of size 3,4,5
  
  Pods = numPods(len(players))
  #TODO: make 3 and 4 person pods
  Pods[0] #3 person pods
  Pods[1] #4 person pods


#LIST OF FUNCTIONS TO WRITE
#Prompt for players list
#Build pods
#Utility to start new season
#cEDH toggle?



main()