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

def genPods(numPlayers):
    return int(4 - numPlayers % 4), int((numPlayers - (4 - numPlayers % 4) * 3) / 4)

#LIST OF FUNCTIONS TO WRITE
#Prompt for players list
#Build pods
#Utility to start new season
#cEDH toggle?



main()
