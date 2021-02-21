from string import (
    digits,
    ascii_lowercase,
    ascii_uppercase,
    punctuation
)
from time import time
import os

CHAR_SET_LIST = (digits, ascii_lowercase, ascii_uppercase, punctuation)

class CustomUser:
    DATA_PATH = os.path.normpath('./data/CustomUser.txt')
    """
    Class
    
    """
    ATTRIBUTES = ['first_name', ]
    def __init__(self, first_name,
                 last_name,
                 email,
                 password=None,
                 birth_date=None,
                 prof_pic=None):
        """

        :param first_name:
        :param last_name:
        :param email:
        :param password:
        :param birth_date:
        :param prof_pic:
        """
        self.validate(first_name=first_name, last_name=last_name, email=email, password=password,
                      birth_date=birth_date, prof_pic=prof_pic)
        self.first_name = first_name
        self.last_name = last_name
        self.primary_email = email
        self.emails = [email]
        self.__password = password
        self.birth_date = birth_date
        self.prof_pic = prof_pic
        self.__is_active = False

        self.validate()

    def validate(self,*args, **kwargs):
        # for attr_name, value in zip(CustomUser.ATTRIBUTES, args):
        #     pass

        for k, v in kwargs.items():
            if k == 'email' and not '@' in v:
                raise Exception('Not valid email.')
            if k == 'password' and v:
                pass_set = set(v)
                if not all(any(it in str_it for str_it in CHAR_SET_LIST) for it in pass_set) or len(v) < 8:
                    raise Exception('Not Secure password!')


    def edit(self,*args, **kwargs):
        for key, value in kwargs.items():
            if getattr(CustomUser, key):
                setattr(CustomUser, key, value)

    def activate(self):
        self.__is_active = True

    def deactivate(self):
        self.__is_active = False

    def save(self):
        with open(CustomUser.DATA_PATH, 'a') as df:
            df.write(str(self.__dict__) + '\n')

    @staticmethod
    def get(email):
        with open(CustomUser.DATA_PATH, 'r') as df:
            line = eval(df.readline())

            while line:
                if line.get('email') == email:
                    return CustomUser(**line)

            raise Exception(f'Can\'t find user with email {email}')

    def filter(self, **kwargs):
        pass

    def __del__(self):
        pass

class Song:
    def __init__(self, title, artist, duration, genre=None, album=None):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.album = album

        self.__played_count = 0



    @property
    def played_count(self):
        return self.__played_count

    @played_count.setter
    def played_count(self, value):
        self.__played_count = value


class Artist:
    def __init__(self, songs):
        self.songs = songs

class UserSong:
    def __init__(self, user, song):
        self.user = user
        self.song = song
        self.start_time = 0
        self.end_time = 0

    def play(self):
        self.start_time = time()

    def stop(self):
        self.end_time = time()
        if self.play_duration > self.song.duration/2:
            self.song.played_count +=1

    @property
    def play_duration(self):
        return self.end_time - self.start_time

class Playlist:
    def __init__(self, title, songs, created_by):
        self.title = title
        self.songs = songs
        self.created_by = created_by
        self.songs_count = len(songs)

