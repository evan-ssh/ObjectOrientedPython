class Games:
    def __init__(self,title,platform,value):
        self.title = title
        self.platform = platform
        self.value = value
    def __str__(self):
        return f"Game: {self.title} Platform: {self.platform} Value: {self.value}"
        