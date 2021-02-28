import argparse
import os
import stat
import pwd
import grp
from datetime import datetime

parser = argparse.ArgumentParser(prog='myls', description='LS implemented by python',
                                 conflict_handler='resolve')

parser.add_argument('paths', nargs='*', default=['.'], help='paths where to show files')
parser.add_argument('-l', action='store_true', help='help for -l')
parser.add_argument('-h', action='store_true', help='help for -h')

args = parser.parse_args()


def convert_to_human_readable(size):
    sizes = ['', 'K', 'M', 'G']
    for i in range(4):
        if size < 1024 or i==3:
            return f'{round(size, 1)}{sizes[i]}'
        else:
            size = size / 1024


len_paths = len(args.paths)
for path in args.paths:
    if len_paths != 1:
        print(path)

    _, file_names, directory_names = next(os.walk(path))
    total_names = file_names + directory_names

    if args.l:
        for file_name in total_names:
            row = []
            stat_info = os.stat(f'{path}/{file_name}')
            row.append(stat.filemode(stat_info.st_mode))
            row.append(stat_info.st_nlink)
            row.append(pwd.getpwuid(stat_info.st_uid).pw_name)
            row.append(grp.getgrgid(stat_info.st_gid).gr_name)
            file_size = stat_info.st_size if not args.h else convert_to_human_readable(stat_info.st_size)
            row.append(file_size)
            row.append(datetime.fromtimestamp(stat_info.st_mtime).strftime('%m %d %H:%M'))
            row.append(file_name)
            formatting = '{: <2} '* len(row)
            print(formatting.format(*row))
    else:
        print(*total_names, sep=' ')