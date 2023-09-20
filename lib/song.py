# class Song:
#     count=0 #class attribute
#     artists=[]
#     def __init__(self,name,artist,genre):
#         self.name=name
#         self._name=artist
#         self.genre=genre
#         Song.song_count()
    
#     @classmethod
#     def song_count(cls):
#         cls.count+=1

#     @classmethod
#     def add_artist(self,artist):
#         pass


# me=Song('mercy','her','pop')
# print(me.name)
# print(me.count)

# me=Song('mercy','her','pop')
# print(me.name)
# print(Song.count)

class Song:
    count=0
    artists=[]
    genres=[]
    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        self.song_count()
        self.add_artist(self.artist)
        self.add_genre(self.genre)
       
        
    @classmethod
    def song_count(cls):
        cls.count+=1

    @classmethod
    def add_artist(cls,artist):
        cls.artists.append(artist)
    
    @classmethod
    def add_genre(cls,genre):
        cls.genres.append(genre)
    


