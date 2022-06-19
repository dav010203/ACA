from playlist import Playlist

class Player:
    def __init__(self, playlist: Playlist) -> None:
        self.__power = False
        self.__playlist = playlist
        self.__song_N = 0
    
    def play(self) -> None:
        if self.__power == False:
            self.__power = True
        else:
            print("It is already turned on!")

    def stop(self) -> None:
        if self.__power == True:
            self.__power = False
        else:
            print("It is already turned off!")
        pass

    def next_song(self) -> None:
        if self.__power:
            self.__song_N += 1
            if self.__song_N > len(self.__playlist.songs) - 1:
                self.__song_N = 0
        else:
            print("At first, turn on the player")

    def previous_song(self) -> None:
        if self.__power:
            self.__song_N -= 1
            if self.__song_N < 0 :
                self.__song_N = len(self.__playlist.songs) - 1
        else:
            print("At first, turn on the player")

    def __show_current_song(self):
        return self.__playlist.songs[self.__song_N]

    def __repr__(self) -> str:
        if self.__power == False:
            return "The player is turned off"
        else:
            return "Current song is --> ({})".format(self.__show_current_song())


plist = Playlist()
plist.load_songs('albums.txt')

pl = Player(plist)
pl.play()
pl.previous_song()
pl.next_song()

print(pl)
