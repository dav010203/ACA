class Song:
    def __init__(self, artist, album, year, name):
        self.artist = artist
        self.album = album
        self.year = year
        self.name = name
        
    def __repr__(self):
        return "Name: {}, Album: {}, Artist: {} | {}".format(self.name, self.album, self.artist, self.year)

