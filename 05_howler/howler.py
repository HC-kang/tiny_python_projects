#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import os
import io
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
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    out_fh = open(args.out_file, 'wt') if args.out_file else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()    



# --------------------------------------------------
if __name__ == '__main__':
    main()
