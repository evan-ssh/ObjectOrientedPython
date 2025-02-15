class Games:
    def __init__(self,title,platform,value):
        self.title = title
        self.platform = platform
        self.value = value
    def __str__(self):
        return f"{self.title} Platform: {self.platform} Value:{self.value}"
class Collection:
    def __init__(self):
        self.games = []
    def addGame(self,game):
        self.games.append(game)
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
