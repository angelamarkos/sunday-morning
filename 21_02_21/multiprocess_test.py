import multiprocessing
import threading
import time
import datetime
import sys


class Song:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def play(self):
        print(f'Started song {self.name}')
        print(datetime.datetime.now())
        self.process = multiprocessing.Process(target=self.__play)
        self.process.start()

    def _play(self):
        time.sleep(self.duration)
        self.stop(from_thread=True)

    def stop(self, from_thread=False):
        if not from_thread:
            self.process.terminate()
        print(datetime.datetime.now())
        print(f'Stoped song {self.name}')


class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def play(self):
        print(f'Stared playlist {self.name}')
        self.starttime = time.time()
        print(f'Start time of playlist {datetime.datetime.now()}')
        self.process = multiprocessing.Process(target=self.__play)
        self.process.start()

    def __play(self):
        for song in self.songs:
            song._play()


    def stop(self):
        played_duration = time.time() - self.starttime
        for song in self.songs:
            played_duration -= song.duration
            if played_duration < 0:
                song.stop(from_thread=True)
                break
        self.process.terminate()
        print(f'End of playlist {datetime.datetime.now()}')


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

def log_factorial(n):
    print(f'Startime {datetime.datetime.now()}')
    factorial(n)
    print(f'Endtime {datetime.datetime.now()}')

def threads_execution_duration():
    start_time = time.time()
    print(f'Started threads Thread')
    thread_1 = threading.Thread(target=log_factorial, args=(25,))
    thread_2 = threading.Thread(target=log_factorial, args=(26,))
    thread_3 = threading.Thread(target=log_factorial, args=(27,))
    thread_4 = threading.Thread(target=log_factorial, args=(28,))
    thread_5 = threading.Thread(target=log_factorial, args=(29,))

    # thread_5 = threading.Thread(target=factorial, args=(15,))
    # thread_6 = threading.Thread(target=factorial, args=(20,))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()
    # thread_5.start()
    # thread_6.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    thread_5.join()
    print(f"Thread execution time \n {time.time() - start_time}")

def process_execution_duration():
    start_time = time.time()
    print(f'Started threads Process')
    thread_1 = multiprocessing.Process(target=factorial, args=(25,))
    thread_2 = multiprocessing.Process(target=factorial, args=(26,))
    thread_3 = multiprocessing.Process(target=factorial, args=(27,))
    thread_4 = multiprocessing.Process(target=factorial, args=(28,))
    thread_5 = multiprocessing.Process(target=factorial, args=(29,))
    # thread_5 = threading.Thread(target=factorial, args=(15,))
    # thread_6 = threading.Thread(target=factorial, args=(20,))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()
    # thread_5.start()
    # thread_6.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    thread_5.join()
    print(f"Thread execution time \n {time.time() - start_time}")

if __name__ == '__main__':
    threads_execution_duration()
    process_execution_duration()
    # song_1 = Song('Song 1', 12)
    # song_2 = Song('Song 2', 4)
    # playlist = Playlist('Playlist 1', [song_2, song_1])
    # playlist.play()
    # time.sleep(5)
    # playlist.stop()

