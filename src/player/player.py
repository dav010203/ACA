from playlist import Playlist

class Player:
    def __init__(self, playlist: Playlist) -> None:
        self.power = False
        self.playlist = playlist
        self.song_N = 0
    
    def play(self) -> None:
        if self.power == False:
            self.power = True
        else:
            print("It is already turned on!")

    def stop(self) -> None:
        if self.power == True:
            self.power = False
        else:
            print("It is already turned off!")
        pass

    def next_song(self) -> None:
        if self.power:
            self.song_N += 1
            if self.song_N > len(self.playlist.songs) - 1:
                self.song_N = 0
        else:
            print("At first, turn on the player")

    def previous_song(self) -> None:
        if self.power:
            self.song_N -= 1
            if self.song_N < 0 :
                self.song_N = len(self.playlist.songs) - 1
        else:
            print("At first, turn on the player")

    def show_current_song(self):
        return self.playlist.songs[self.song_N]

    def __repr__(self) -> str:
        return "Current - {}".format(self.show_current_song())

plist = Playlist()
plist.load_songs('albums.txt')

pl = Player(plist)
pl.play()
pl.previous_song()
pl.next_song()

print(pl)

    