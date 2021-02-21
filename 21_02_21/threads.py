import threading
import time

def func_thread(a, b):
    print('Started func_thread')
    time.sleep(5)
    print(a + b)
    print('Ended func_thread')

def main_func():
    print('Started main_func')
    thread_1 = threading.Thread(target=func_thread, args=(1, 3), daemon=True)
    thread_1.start()
    print('End of main_func')


FILE_NAME = 'prcessed_words.txt'

def file_processing():
    time.sleep(5)
    with open(FILE_NAME, 'w') as f:
        f.write('Test')


if __name__ == '__main__':
    # main_func()
    # time.sleep(5)
    thread_file = threading.Thread(target=file_processing)
    thread_file.start()
    input_word = input('Input a word: ')
    thread_file.join(3)
    with open(FILE_NAME, 'r') as f:
        print(f.readline())


