from song import Song

class Playlist:
    def __init__(self) -> None:
        self.playlist = []

    def load_songs(self, playlist_f):
        with open(playlist_f, "r") as songs:
            for s in songs:
                s = s.split("\t")
                song = Song(s[0], s[1], s[2], s[3].strip())
                self.playlist.append(song)

    
    def __repr__(self) -> str:
        string = ""
        for song in self.playlist:
            string += song.name + ", "
        return string[:-2]

