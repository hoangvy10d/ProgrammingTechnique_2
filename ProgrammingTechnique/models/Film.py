class Film:
    def __init__(self, FilmTitle, FilmCharacters, FilmDateReleased, FilmAuthor, LinkFilm):
        self.FilmTitle = FilmTitle
        self.FilmCharacters = FilmCharacters
        self.FilmDateReleased = FilmDateReleased
        self.FilmAuthor = FilmAuthor
        self.LinkFilm = LinkFilm

    def __str__(self):
        return f"{self.FilmTitle}\t{self.FilmCharacters}\t{self.FilmDateReleased}\t{self.FilmAuthor}\t{self.LinkFilm}"