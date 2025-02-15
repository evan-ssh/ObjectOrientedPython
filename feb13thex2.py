class Games:
    def __init__(self,title,platform,value):
        self.title = title
        self.platform = platform
        self.value = value
    def __str__(self):
        return f"Game: {self.title} Platform: {self.platform} Value: {self.value}"
class Collection:
    def __init__(self):
        self.games = []
    def addGame(self,game):
        self.games.append(game)
    def __iter__(self):
        for game in self.games:
            yield game