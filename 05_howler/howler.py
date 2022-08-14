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
                        help='A name of out_file',
                        metavar='str',
                        type=str,
                        default='')
    
    parser.add_argument('-e',
                        '--ee',
                        help='A boolean flag',
                        action='store_true')

    args = parser.parse_args()
    args.dir = False
    
    if os.path.isfile(args.text):
        args.text = open(args.text)
    elif os.path.isdir(args.text):
        args.dir = True
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    def logic(text, out_file, ee=False):
        out_fh = open(out_file, 'wt') if out_file else sys.stdout
        for line in text:
            out_fh.write(line.lower() if ee else line.upper())
        out_fh.close()
    
    args = get_args()
    if args.dir:
        os.mkdir('out-files')
        for file in os.listdir(args.text):
            logic(open(os.path.join(args.text, file)).read().strip(), os.path.join('./out-files', file), args.ee)
    else:
        logic(args.text, args.out_file, args.ee)


# --------------------------------------------------
if __name__ == '__main__':
    main()
