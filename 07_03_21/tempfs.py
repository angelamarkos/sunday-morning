import tempfile
import time
import os
import contextlib

tempfile.tempdir = '.'
file = tempfile.NamedTemporaryFile(mode='w+t', prefix='XFiles_', suffix='.doc',
                                   delete=False, dir='./temps')
file.write('text')

file.close()

with tempfile.NamedTemporaryFile(mode='w+t', prefix='File_', suffix='.csv') as file:
    file.write('1,2,4')


with tempfile.TemporaryDirectory(prefix='TempDir_', dir='./temps') as td:
    tfile = tempfile.NamedTemporaryFile(mode='w+t', prefix='DirectoryFile_', dir=td, delete=False)
    tfile.write('text')
    tfile.close()

class TempFile:
    def __init__(self, file_name):
        self.filename = file_name
        self.file = open(file_name, 'w+')

    def __enter__(self):
        return self.filename

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        os.remove(self.filename)


@contextlib.contextmanager
def inDir(path):
    current_path = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(current_path)

with inDir('./temps'):
    os.mkdir('temp_2')

print(os.getcwd())