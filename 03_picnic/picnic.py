#!/usr/bin/env python3
"""
Author : Ford <weston0713@gmail.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
template = 'You are bringing {}.'


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')
    
    parser.add_argument('-s',
                        '--sorted',
                        help='sort flag',
                        action='store_true')
    
    parser.add_argument('-u',
                        '--unacceptable',
                        help='sort flag',
                        action='store_true')
    
    parser.add_argument('-m',
                        '--modify',
                        help='A char to modify comma',
                        metavar='str',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    items = args.item
    sep = args.modify
    
    if args.sorted:
        items.sort()
    
    bringing = ''
    
    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else:
        if args.unacceptable:
            bringing = f'{sep} '.join(items[:-1]) + ' and ' + items[-1]
        else:
            bringing = f'{sep} '.join(items[:-1]) + f'{sep} and ' + items[-1]

    print(template.format(bringing))


# --------------------------------------------------
if __name__ == '__main__':
    main()
