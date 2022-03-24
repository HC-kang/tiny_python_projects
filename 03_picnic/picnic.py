#!/usr/bin/env python3
"""
Author : heechankang <heechankang@localhost>
Date   : 2022-03-24
Purpose: Rock the Casbah
"""

import argparse
from operator import delitem


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs = '+',
                        help='Items to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    parser.add_argument('-o',
                        '--option',
                        action='store_true',
                        help='no comma before and')

    parser.add_argument('-d',
                        '--delimiter',
                        metavar = 'str',
                        type=str,
                        help='change delimeter')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    
    if args.sorted:
        items.sort()
        
    separator = ', '
    if args.delimiter:
        separator = args.delimiter+' '
        
    things = ''        
    if len(items) == 1:
        things = items[0]
    elif len(items) == 2:
        things = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        if args.option:
            tmp = items.pop()
            items[-1] = items[-1] + ' ' + tmp
        things = separator.join(items)

    print(f'You are bringing {things}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
