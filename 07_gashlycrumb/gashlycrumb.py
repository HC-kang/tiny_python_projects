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

    parser.add_argument('positional',
                        metavar='str',
                        nargs='*',
                        help='A positional argument')
    
    parser.add_argument('-f',
                        '--file',
                        help='A named string argument',
                        metavar='str',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    lookup = {line[0].upper(): line.strip() for line in args.file}
    pos_arg = args.positional
    for p in pos_arg:
        print(lookup.get(p.upper(), f'I do not know "{p}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
