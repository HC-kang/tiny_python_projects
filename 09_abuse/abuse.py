#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)
    
    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)
    
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')
    
    args = parser.parse_args()
    
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
        
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # str_arg = args.arg
    # int_arg = args.int
    # file_arg = args.file
    # flag_arg = args.on
    # pos_arg = args.positional

    # print(f'str_arg = "{str_arg}"')
    # print(f'int_arg = "{int_arg}"')
    # print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    # print(f'flag_arg = "{flag_arg}"')
    # print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
