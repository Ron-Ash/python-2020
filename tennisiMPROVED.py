import os
import random
import functools 
import itertools
import xlwt 
from xlwt import Workbook 
import math

def GetRandomSetOfPlayers(Players, Rounds):
    playersCombination = set({}) 
    while len(playersCombination) < Rounds:
        playerIndex = random.randrange(0,len(Players),1)
        playersCombination.add(Players[playerIndex])
    return(playersCombination)

def CreateRandomSetsOfPlayers(Players, Rounds, SetsNumber):
    listOfCombinations = []
    while len(listOfCombinations) < SetsNumber:
        newCombination = GetRandomSetOfPlayers(Players, Rounds)
        identical = False
        for combination in listOfCombinations:
            if combination.difference(newCombination) == set():
                identical = True
                break
        if not identical:
            listOfCombinations.append(newCombination)
    return (listOfCombinations)


def Winning(ATP_RankingOfPlayer, Number_of_players, rounds):
    opponents_ATP = []
    _chance_of_winning_competition = []
    Average_chance_of_winning_competition = []
    players_stronger_than_you = (Number_of_players - 1)/2 + 1
    players_weaker_than_you = (Number_of_players - 1)/2 

    for i in range(int(players_stronger_than_you)):
        opponents_ATP.append(random.randint(ATP_RankingOfPlayer,16790))
    for i in range(int(players_weaker_than_you)):
        opponents_ATP.append(random.randint(20, ATP_RankingOfPlayer))
    print(f"________________\tThis is all of the possible players ATP rankings : \t{opponents_ATP}\t________________")


    listOfCombinations = CreateRandomSetsOfPlayers(opponents_ATP, rounds, 100)
    print(listOfCombinations)
    
    #print(f"________________\nAll of the possible combinations of the round winners you will play against: \n:{ListOfLists}\n________________")
    for playerOrder in listOfCombinations:
        for ATP_RankingOfOponent in playerOrder:
            print(f"------\nPlaying aginst: {ATP_RankingOfOponent}\n")
            if(ATP_RankingOfOponent > ATP_RankingOfPlayer):
                differenceInRank = (ATP_RankingOfOponent - ATP_RankingOfPlayer)/33500
                if(differenceInRank > 0.5):
                    ProbabilityOfWinningAGame = 0.1**5
                if(differenceInRank < 0.5):
                    ProbabilityOfWinningAGame = 0.5 - differenceInRank
                ProbabilityOfLosingAGame = 1 - ProbabilityOfWinningAGame

            elif(ATP_RankingOfOponent < ATP_RankingOfPlayer):
                differenceInRank = (ATP_RankingOfPlayer - ATP_RankingOfOponent)/33500
                if(differenceInRank > 0.5):
                    ProbabilityOfLosingAGame = 0.1**5
                if(differenceInRank < 0.5):
                    ProbabilityOfLosingAGame = 0.5 - differenceInRank
                ProbabilityOfWinningAGame = 1 - ProbabilityOfLosingAGame
 
            ProbabilityOfWinningOverallAGame = ((ProbabilityOfWinningAGame**3) + (3*(ProbabilityOfWinningAGame**3)*(ProbabilityOfLosingAGame)) + (6*(ProbabilityOfWinningAGame**3)*(ProbabilityOfLosingAGame**2)))
            _chance_of_winning_competition.append(ProbabilityOfWinningOverallAGame)
            ProbabilityOfWinningOverallAGame


        winningComp =   functools.reduce(lambda x, y: x*y, _chance_of_winning_competition)

        Average_chance_of_winning_competition.append(winningComp)
        print(winningComp)
        del _chance_of_winning_competition[:]

    return(Average_chance_of_winning_competition)

def Simulation():
    simulation_results = []
    ATP_RankingOfPlayer = float(input("what is your player's ATP Ranking?"))
    Number_of_players = float(input("how many players are there in the tournament(excluding your player)?"))
    run_simulation = int(input("how many times whould you like to run the simulation?"))


    Number_of_players += 1
    rounds = int(math.log(Number_of_players, 2))
    print(rounds)

    for i in range(run_simulation):
        simulation_results.extend(Winning(ATP_RankingOfPlayer, Number_of_players, rounds))

    wb = Workbook() 
    sheet1 = wb.add_sheet('Sheet 1') 
    print(simulation_results)
    for i in range(len(simulation_results)):
        sheet1.write(i, 0, simulation_results[i])
        sheet1.write(i, 1, rounds)
    wb.save('M&M.xls') 
    return(simulation_results)

print(f"--------------------\nthe Probability of winning a Game is :{Simulation()}")