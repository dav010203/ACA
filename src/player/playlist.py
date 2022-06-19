from song import Song

class Playlist:
    def __init__(self) -> None:
        self.__songs = []

    def load_songs(self, file_name) -> None:
        with open(file_name, "r") as songs_file:
            print()
            for s in songs_file:
                s = s.split("\t")
                song = Song(s[0], s[1], s[2], s[3].strip())
                self.__songs.append(song)
    
    @property
    def songs(self):
        return self.__songs
    
    def __repr__(self) -> str:
        s_names = ""
        for song in self.__songs:
            s_names += song.name + ", "
        return s_names[:-2]
