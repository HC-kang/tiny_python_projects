#!/usr/bin/env python3
"""
Author : heechankang <heechankang@localhost>
Date   : 2022-03-28
Purpose: Rock the Casbah
"""

import argparse
import os
import io
import sys

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
    
    parser.add_argument('-e',
                        '--ee',
                        action='store_true',
                        help='to lower case')
    
    parser.add_argument('-d',
                        '--outdir',
                        action='store_true',
                        help='to lower case')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text)
    elif os.path.isdir(args.text):
        args.title = args.text
        args.files = os.listdir(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')
    
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.outdir:
        
        os.mkdir(args.text+"/new")
        for file in args.files:
            text = open(os.path.join(args.text, file))
            change_text(text, os.path.join(args.text+"/new", file), args.ee)
            text.close()
    else:
        change_text(args.text, args.outfile, args.ee)

# --------------------------------------------------
def change_text(text, outfile, ee):
    fh = open(outfile, 'wt') if outfile else sys.stdout
    
    for line in text:
        fh.write(line.lower()) if ee else fh.write(line.upper())
        
    fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
