class Song:
    def __init__(self, artist: str, album: str, year: int, name: str) -> None:
        self.__artist = artist
        self.__album = album
        self.__year = year
        self.__name = name

    def __repr__(self) -> str:
        return "Name: {} - Album: {} - Artist: {} - Year: {}".format(self.__name, self.__album, self.__artist, self.__year)
