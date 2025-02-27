class Fanfic:
    def __init__(self, FanficTitle, FanficCharacters, FanficDateReleased, FanficAuthor, LinkFilm):
        self.FanficTitle = FanficTitle
        self.FanficCharacters = FanficCharacters
        self.FanficDateReleased = FanficDateReleased
        self.FanficAuthor = FanficAuthor
        self.LinkFilm = LinkFilm

    def __str__(self):
        return f"{self.FanficTitle}\t{self.FanficCharacters}\t{self.FanficDateReleased}\t{self.FanficAuthor}\t{self.LinkFilm}"