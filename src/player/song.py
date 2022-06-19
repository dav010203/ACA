class Song:
    def __init__(self, artist: str, album: str, year: int, name: str) -> None:
        self.artist = artist
        self.album = album
        self.year = year
        self.name = name

    def __repr__(self) -> str:
        return "{} - {} - {} - {}".format(self.name, self.album, self.artist, self.year)
