#--coding:utf-8--
class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    
happy_bday=Song(["Happy birthday to you",
                 "I don't want to get sued",
                 "So I'll stop here"])

bull_on_paraed=Song(["They really around the family",
                     "with pockets full of shells"])

happy_bday.sing_me_a_song()

bull_on_paraed.sing_me_a_song()