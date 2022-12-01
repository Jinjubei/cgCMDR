from datetime import datetime
import pandas as pd
from multielo import MultiElo

players = []
podAssignments = {}
gameDate = datetime.now().strftime("%Y%m%d")
melo = MultiElo()


def main():
    # get player db, sort by most recent rating
    players = fetchPlayerDB()
    players = players.sample(frac=1)
    players = players.sort_values(by=[players.columns[-1]], ascending=True)

    # if today's date is not one of the columns, add it as the last column
    if gameDate not in players.columns:
        players[gameDate] = ""
        print("added", gameDate)

    # generate pods
    podAssignments = genPods(players)

    # print pods to console
    for key in podAssignments.keys():
        print("\n" + "="*40)
        print(key)
        print("-"*40)
        print(podAssignments[key])
    print("="*40)

    # indicate winners and update rankings
    for key in podAssignments.keys():
        print("\n" + "="*40)
        print(key)
        print("-"*40)
        print(podAssignments[key])
        pWinner = input(
            "enter comma-separated indices, starting with winner: ")
        pWinner = [int(x) for x in ("".join(pWinner.split())).split(",")]

        match len(pWinner):
            case 3:
                rArr = [players.loc[pWinner[0]][players.columns[-2]], players.loc[pWinner[1]]
                        [players.columns[-2]], players.loc[pWinner[2]][players.columns[-2]]]
                winArr = [1, 2, 2]
            case 4:
                rArr = [players.loc[pWinner[0]][players.columns[-2]], players.loc[pWinner[1]]
                        [players.columns[-2]], players.loc[pWinner[2]][players.columns[-2]], players.loc[pWinner[3]][players.columns[-2]]]
                winArr = [1, 2, 2, 2]

        newRatings = [int(x) for x in melo.get_new_ratings(rArr, winArr)]

        for oR in range(0,len(pWinner)):
            players.at[pWinner[oR],gameDate]=newRatings[oR]


    print(players)
    players.to_csv('playerDB.csv', index=False)


def fetchPlayerDB():
    df = pd.read_csv('playerDB.csv')
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

    pA = {}
    match len(players):
        case 1 | 2:
            print("Admonish TO for trying to make a pod with 1 or 2 players")
            exit()
            # TODO:Admonish TO for trying to make a pod with 1 or 2 players
        case 3 | 4 | 5:
            print("1 pod:")
            print(players)
        case _:
            Pods = numPods(len(players))
            startIndexPos = 0
            totalPods = 1
            print("3s:", Pods[0], ", 4s:", Pods[1])

            for p3 in range(Pods[0]):
                podName = "Pod" + str(totalPods)
                pA[podName] = pd.DataFrame(
                    players.iloc[startIndexPos:startIndexPos + 3])
                startIndexPos += 3
                totalPods += 1
            for p4 in range(Pods[1]):
                podName = "Pod" + str(totalPods)
                pA[podName] = pd.DataFrame(
                    players.iloc[startIndexPos:startIndexPos + 4])
                startIndexPos += 4
                totalPods += 1

    return pA


# LIST OF FUNCTIONS TO WRITE
# Prompt for players list
# Utility to start new season
# cEDH toggle?

whatDo = str(input("Show, Play, eXit: ")).upper()

match whatDo:
    case "S":
        players = fetchPlayerDB()
        players = players.sample(frac=1)
        players = players.sort_values(by=[players.columns[-1]], ascending=True)
        print(players)
    case "P":
        main()
    case _:
        exit()
