from song import Song

class Playlist:
    def __init__(self):
        self.playlist = []
    
    def load_songs(self, song_file):
        with open(song_file, "r") as file:
            for s in file:
                s = s.split("\t")
                song = Song(s[0], s[1], s[2], s[3].strip())
                self.playlist.append(song)

    def __repr__(self):
        s = ""
        for i in self.playlist:
            s += i.name + ", "
        return s[:-2]

p = Playlist()
p.load_songs('albums.txt')
print(p)
