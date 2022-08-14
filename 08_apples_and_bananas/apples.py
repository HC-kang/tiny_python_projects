#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

from genericpath import isfile
import os
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-v',
                        '--vowel',
                        help='A named string argument',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        with open(args.text) as fh:
            args.text = fh.read()
            
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    lookup = {}
    for c in 'aeiou':
        lookup[c] = args.vowel
    for C in 'AEIOU':
        lookup[C] = args.vowel.upper()
    
    for t in args.text.strip():
        print(lookup.get(t, t), end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
