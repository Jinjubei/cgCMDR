import json
import pandas as pd


players = []


def main():
    players = fetchPlayerDB()
    players = players.sample(frac=1)
    players = players.sort_values(by=[players.columns[-1]], ascending=True)
    genPods(players)


def fetchPlayerDB():
    f = open('.\cgCMDR\playerDB.json')
    jdata = json.load(f)
    df = pd.DataFrame(jdata["players"])
    return df


def numPods(numple):
    numple = int(numple)

    if (numple == 3):
        return [1, 0]
    elif (numple == 4):
        return [0, 1]
    elif (numple % 4 == 0):
        return [0, numple / 4]
    else:
        threes = 4 - numple % 4
        return [threes, int((numple - threes * 3) / 4)]


def genPods(players):
    if (len(players) == 1 or len(players) == 2):
        print("foo 1 or 2")
        # TODO:Admonish TO for trying to make a pod with 1 or 2 players
    elif (len(players) == 3 or len(players) == 4 or len(players) == 5):
        print("1 pod:")
        print(players)
    else:
        Pods = numPods(len(players))
        startIndexPos = 0
        print("3s:", Pods[0], ", 4s:", Pods[1])
        for t in range(0, Pods[0]):
            print(players[startIndexPos:startIndexPos + 3])
            startIndexPos += 3
        for f in range(0, Pods[1]):
            print(players[startIndexPos:startIndexPos + 4])
            startIndexPos += 4


# LIST OF FUNCTIONS TO WRITE
# Prompt for players list
# Build pods
# Utility to start new season
# cEDH toggle?


main()
