class Games:
    def __init__(self,title,platform,value):
        self.title = title
        self.platform = platform
        self.value = value
    def __str__(self):
        return f"{self.title} {self.platform} ${self.value}"
class Collection:
    def __init__(self):
        self.games = []
    def addGame(self,game):
        self.games.append(game)

    def calcValue(self):
        total = 0
        for game in collection:
            total += game.value
        print(f"Total Estimated value of collection: {total}")

    def highestValue(self):
        return max(self.games, key=lambda game: game.value)
    def __iter__(self):
        for game in self.games:
            yield game

g1 = Games("The Incredible Hulk","Nintendo Gamecube", 80)
g2 = Games("Enternal Darkness","Nintendo Gamecube",110)
g3 = Games("Metal Gear Solid: The Twin Snakes","Nintendo Gamecube",100)
g4 = Games("Unreal Tournament: Collectors Edition(NEW)", "Windows PC", 90)
collection = Collection()
collection.addGame(g1)
collection.addGame(g2)
collection.addGame(g3)
collection.addGame(g4)

print("Erics Epic Collection\n")
for game in collection:
    print(game)
# Total value of collection
collection.calcValue()
print(f"Most valuable game in collection - {collection.highestValue()}")


