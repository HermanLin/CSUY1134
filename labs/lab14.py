from ChainingHashTableMap import ChainingHashTableMap
from DoublyLInkedList import DoublyLinkedList

class Playlist:
    def __init__(self):
        songs = ChainingHashTableMap()
        playlist = DoublyLinkedList()
        
    def add_song(self, new_song_name):
        if songs.is_empty():
            k = self.songs.hash_function(new_song_name)
            song[k] = None
            playlist.add_last(new_song_name)
        else:
            last_song = playlist.last_node.data
            p = self.songs.hash_function(last_song)
            

    def add_song_after(self, song_name, new_song_name):
        k = self.hash_function(new_song_name)
        

    def play_song(self, song_name):

    def play_list(self):
