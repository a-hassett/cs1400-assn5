import random

devilTurn = False
playerTurn = True
roll = 0
devilScore = 0
playerScore = 0
playerTempScore = 0
devilTempScore = 0
playerTurnRow = 0
playerScoreRow = 0
devilTurnRow = 0
devilScoreRow = 0


def printDie(roll):  # print pictures of dice value
    if roll == 0:
        return "\u2327"
    if roll == 1:
        return "\u2620"
    if roll == 2:
        return "\u2681"
    if roll == 3:
        return "\u2682"
    if roll == 4:
        return "\u2683"
    if roll == 5:
        return "\u2684"
    if roll == 6:
        return "\u2685"


def printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow):  # print scores and roll values
    playerTurnCol = str(playerTempScore + playerScore) + " => "
    playerScoreCol = " <= " + str(playerScore)
    devilTurnCol = str(devilTempScore + devilScore) + " => "
    devilScoreCol = " <= " + str(devilScore)

    playerScoreRow = playerScore - (playerScore % 5)
    if playerScoreRow > 100:
        playerScoreRow = 100

    playerTurnRow = playerScore + playerTempScore - ((playerScore + playerTempScore) % 5)
    if playerTurnRow > 100:
        playerTurnRow = 100

    devilScoreRow = devilScore - (devilScore % 5)
    if devilScoreRow > 100:
        devilScoreRow = 100

    devilTurnRow = devilScore + devilTempScore - ((devilScore + devilTempScore) % 5)
    if devilTurnRow > 100:
        devilTurnRow = 100

    print(format("Devil's Dice", ">80s"), "\n")
    print(format("****you****", ">41s"), format("devil", ">80s"))
    print(format("turn", ">20s"), format("score", ">35s"), format("turn", ">50s"), format("score", ">30s"))

    for i in range(100, -5, -5):
        if playerTurnRow == i:
            print(format(playerTurnCol, ">19s"), format(str(i), ">17s"), end="")
        else:
            print(format(str(i), ">37s"), end="")

        if playerScoreRow == i:
            print(format(playerScoreCol, ">18s"), end="")
        else:
            print(format(" ", ">18s"), end="")

        if devilTurnRow == i:  # print roll value on lines 70 and 60
            if i == 70:
                print(format("Roll: ", ">20s"), format(devilTurnCol, ">25s"), format(str(i), ">20s"), end="")
            elif i == 60:
                print(format(str(roll), ">16s"), printDie(roll), format(devilTurnCol, ">25s"), format(str(i), ">20s"), end="")
            else:
                print(format(devilTurnCol, ">45s"), format(str(i), ">20s"), end="")
        else:
            if i == 70:
                print(format("Roll: ", ">20s"), format(str(i), ">45s"), end="")
            elif i == 60:
                print(format(str(roll), ">16s"), printDie(roll), format(str(i), ">47s"), end="")
            else:
                print(format(str(i), ">66s"), end="")

        if devilScoreRow == i:
            print(format(devilScoreCol, ">17s"))
        else:
            print(" ")
    print("\n\n")


# print intro to game
print("Welcome to Devil's Dice!\nLet's play!")
printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)

while True:
    while playerTurn:  # what happens during the player's turn
        print("It's your turn!")
        d = input("[r]oll or [p]ass or [q]uit the game: ").lower()  # player choose their move

        if d == "r":  # player wants to roll the dice
            roll = random.randint(1, 6)

            if roll == 1:  # if the dice is 1, end the turn and print results
                # end player's turn and start devil's turn
                playerTurn = False
                devilTurn = True
                playerTempScore = 0
                printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)
                print("You lost your turn!")
            else:  # if dice is not 1, add it to their temporary points
                playerTempScore += roll
                printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)

        elif d == "p":  # player wants to end their turn and keep their points
            playerTurn = False
            devilTurn = True
            playerScore += playerTempScore
            playerTempScore = 0
            roll = 0
            printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)

        elif d == "q":  # player wants to quit the game
            playerTurn = False
            devilTurn = False
            print("You forfeited to the devil, ya wimp :|")
            break

        else:  # if player enters a letter that's not an option, give an error message
            print("?\nEnter y or n")

        if playerScore >= 100:  # if the player wins, end the game
            playerTurn = False
            devilTurn = False
            print("You win!")

    while devilTurn:  # what happens during the devil's turn
        if devilScore >= playerScore:  # if the devil is winning or tied, he will shoot for less points during his turn
            while devilTempScore < 21 and (devilScore + devilTempScore) < 100:  # wants 21 points unless he wins
                roll = random.randint(1, 6)

                if roll == 1:
                    devilTurn = False
                    playerTurn = True
                    printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)
                    break
                else:
                    devilTempScore += roll
                    printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)

            # end devil's turn and start player's turn
            devilTurn = False
            playerTurn = True

        elif devilScore < playerScore:  # if the devil is losing, he will shoot for more points
            while devilTempScore < 30 and (devilScore + devilTempScore) < 100:  # wants 30 points unless he wins
                roll = random.randint(1, 6)

                if roll == 1:
                    # devilTempScore = 0
                    devilTurn = False
                    playerTurn = True
                    printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)
                    break
                else:
                    devilTempScore += roll
                    printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)

            # end devil's turn and start player's turn
            devilTurn = False
            playerTurn = True

        # set devil's new score and reset the roll
        if roll == 1:
            devilTempScore = 0
        devilScore += devilTempScore
        devilTempScore = 0
        roll = 0
        printGameBoard(playerTurnRow, playerScoreRow, devilTurnRow, devilScoreRow)

        if devilScore >= 100:  # check if the devil won
            playerTurn = False
            devilTurn = False
            print("You lost!")

    if not devilTurn and not playerTurn:  # if both turns are ended because one player won, exit the game
        break
