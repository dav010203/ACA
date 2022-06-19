class Song:
    def __init__(self, artist, album, year, name) -> None:
        self.artist = artist
        self.album = album
        self.year = year
        self.name = name

    def __repr__(self):
        return "Song: '{}' - Album: '{}' - '{}', {}".format(self.name, self.album, self.artist, self.year)
