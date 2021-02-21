import sys
import os

def convert_ownership_to_string(ownerships, is_folder):
    permission = ['r', 'w', 'x']
    permission_string = ''
    for ownership in ownerships:
        ownership_bin = bin(int(ownership))[2:]
        for i, bin_num in enumerate(ownership_bin):
            if bin_num != '0':
                permission_string = f'{permission_string}{permission[i]}'
            else:
                permission_string = f'{permission_string}-'

    folder_lit = 'd' if is_folder else '-'
    return f'{folder_lit}{permission_string}'

if __name__ == '__main__':
    args = sys.argv[1:]
    paths = []
    tags = []
    for arg in args:
        if arg.startswith('-'):
            tags.append(arg)
        else:
            paths.append(arg)
    if not paths:
        paths = ['.']

    for path in paths:
        print(f'{path}:')
        _, folder_names, file_names = next(os.walk(path))
        files_folders = zip(file_names + folder_names, [False]*len(file_names) + [True]*len(folder_names))
        if not any('a' in tag for tag in tags):
            files_folders = [file_folder for file_folder in files_folders if not file_folder[0].startswith('.')]

        used_l_tag = any('l' in tag for tag in tags)
        for file_name, is_folder in files_folders:
            if used_l_tag:
                ownership = convert_ownership_to_string(oct(os.stat(file_name).st_mode)[-3:], is_folder)
                string_to_print = f'{ownership}  {file_name}'
            else:
                string_to_print = file_name
            print(string_to_print)


