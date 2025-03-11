import random

def winner(winningNums,randomNums):
    winner = winningNums.intersection(randomNums)
    matchNums = len(winner)
    if matchNums < 2:
        return "Sorry no win"
    elif matchNums == 2:
        return "Congratulations 2 numbers matched and you won a free play"
    elif matchNums == 3:
        return "Congratulations u won $10"
    elif matchNums == 4:
        return "Congratulations u won $90.50"
    elif matchNums == 5:
        return "Congratulations you won $5000"
    elif matchNums == 6:
        return "Congratiulations you hit the JACKPOT $13000000"
    else:
        return "Sorry no win"
    
def main():
    winningNums = {9,20,27,35,37,43}
    randomNums = set()
    while len(randomNums) < 6:
        i = random.randint(1,49)
        if i not in randomNums:
            randomNums.add(i)
    print(winner(winningNums,randomNums)) 

if __name__ == "__main__":
    main()

    