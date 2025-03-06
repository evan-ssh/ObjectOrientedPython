import random

def winner(winningNums,randomNums):
    winner = winningNums.intersection(randomNums)
    matchNums = len(winner)
    return matchNums

def generateTicket():
    randomNums = set()
    while len(randomNums) < 6:
        i = random.randint(1,49)
        if i not in randomNums:
            randomNums.add(i)
    return randomNums
def main():
    while True:
        winningNums = {9,20,27,35,37,43}
        totalwon = 0
        totallost = 0
        tickets = int(input("How many tickets would u like to buy $2 each: "))
        totallost += 2 * tickets
        for _ in range(tickets):
            randomNums = generateTicket()
            matchNums = winner(winningNums,randomNums)
            if matchNums < 2:
                print ("Sorry no win")
            elif matchNums == 2:
                print("Congratulations 2 numbers matched and you won a free play")
                totalwon += 2
            elif matchNums == 3:
                print("Congratulations 3 numbers matched you won $10")
                totalwon += 10
            elif matchNums == 4:
                print("Congratulations 4 numbers matched you won $90.50")
                totalwon += 90.50
            elif matchNums == 5:
                print("Congratulations 5 numbers matched you won $5000") 
                totalwon += 5000
            elif matchNums == 6:
                print("Congratulations all numbers MATCHED you hit the JACKPOT $13000000")
                totalwon += 13000000
        overallEarnings = totalwon - totallost
        print(f"You bought ${tickets * 2} worth of tickets")
        print(f"Total Won: {totalwon}")
        print(f"Total Lost: {totallost}")
        print(f"Overall Earnings: {overallEarnings}")
        go_again = input("Would u like to buy more tickets?")
        if go_again != "y":
            break
if __name__ == "__main__":
    main()

    