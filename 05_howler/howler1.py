#!/usr/bin/env python3
"""
Author : heechankang <heechankang@localhost>
Date   : 2022-03-28
Purpose: Rock the Casbah
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type = str,
                        help='text message or filename')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        type = str,
                        default = '',
                        help='out_file name')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    
    
    if args.outfile:
        fh = open(args.outfile, 'wt')
        fh.write(text.upper())
        fh.close()
    else:
        print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
