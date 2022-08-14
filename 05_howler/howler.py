#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import os
import sys
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A text argument')

    parser.add_argument('-o',
                        '--out_file',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        in_fh = open(args.text)
        args.text = in_fh.read().strip()
        in_fh.close()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    result = args.text.upper().strip()
    if args.out_file:
        out_fh = open(args.out_file, 'wt')
        out_fh.write(result)
        out_fh.close()
    else:
        print(result)
        



# --------------------------------------------------
if __name__ == '__main__':
    main()
