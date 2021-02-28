import argparse

parser = argparse.ArgumentParser(prog='ArgTry',
                                 usage='%(prog)s [options]',
                                 description='Description for command parser.',
                                 epilog='End of message.',
                                 prefix_chars='+/-')

# parser.add_argument('first_num', type=float, help='First num for add.')
# parser.add_argument('second_num', type=float, help='Second num for add.')
# parser.add_argument('string_arg', help='Second num for add.')
parser.add_argument('-l', '--list', type=float, help='Optional l args', dest='whitelist')
parser.add_argument('-v', '--verbosity', action='store_false', help='Optional v args')
parser.add_argument('-q', '--quit', nargs=2, help='Optional q args')
parser.add_argument('-w', '--web', nargs='?', default=34, const=23, help='Optional w args')

parser.add_argument('-tp', '--type', choices={'basic', 'premium', 'simple'}, help='Optional tp args')
parser.add_argument('-f', '--face', action='append', help='Optional v args')
parser.add_argument('-z', '--zip', action='append_const', const=1, help='Optional v args', dest='zc')
parser.add_argument('-c', '--cut', action='append_const', const=2, help='Optional v args', dest='zc')

group = parser.add_mutually_exclusive_group()
group.add_argument('-t', '--take', nargs='*', default=[1], help='Optional t args')
group.add_argument('-e', '--exit', nargs='+', default=[1], help='Optional e args')

subparsers = parser.add_subparsers()
parser_sub =subparsers.add_parser('div')
parser_sub.add_argument('first_n', type=float, help='first num help div')
parser_sub.add_argument('second_n', type=float, help='second num help div')


args = parser.parse_args()

print(args.first_n/args.second_n)

# print(args.first_num)
# print(args.whitelist)
# print(args.first_num+args.second_num)
print(args.__dict__)


parent_parser = argparse.ArgumentParser(prog='parent', description='description for parent', add_help=False)

parent_parser.add_argument('path', help='help str for path')


parser_1 = argparse.ArgumentParser(prog='parser_1', description='Parser_1 description', parents=[parent_parser])
parser_1.add_argument('-a', type=int, help='help str for -a')

args_1 = parser_1.parse_args(['path/to/file_1', '-a', '1'])
# print(args_1.__dict__)

parser_2 = argparse.ArgumentParser(prog='parser_2', description='Parser_2 description', parents=[parent_parser])
parser_2.add_argument('-s', type=int, help='help str for -s')
args_2 = parser_2.parse_args(['path/to/file_2', '-s', '1'])
# print(args_2.__dict__)