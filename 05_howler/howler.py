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
                        '--out',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    out_file = args.out
    pos_arg = args.text

    if os.path.isfile(pos_arg):
        if (out_file):
            out_fh = open(out_file, 'wt')
            in_fh = open(pos_arg)
            out_fh.write(in_fh.read().upper().strip())
            out_fh.close()
        else:
            in_fh = open(pos_arg)
            print(in_fh.read().upper().strip())
    else:
        if (out_file):
            out_fh = open(out_file, 'wt')
            out_fh.write(pos_arg.upper())
            out_fh.close()
        else:
            print(pos_arg.upper())




# --------------------------------------------------
if __name__ == '__main__':
    main()
