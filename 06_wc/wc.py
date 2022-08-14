#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import sys
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'),
                        help='Input file(s)')
    
    parser.add_argument('-l',
                        '--line',
                        help='A boolean flag',
                        action='store_true')
    
    parser.add_argument('-w',
                        '--word',
                        help='A boolean flag',
                        action='store_true')
    
    parser.add_argument('-b',
                        '--byte',
                        help='A boolean flag',
                        action='store_true')

    args = parser.parse_args()
    if (args.line or args.word or args.byte) == False:
        args.line = args.word = args.byte = True
        
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    total_lines, total_bytes, total_words = 0, 0, 0
    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_bytes += len(line)
            num_words += len(line.split())
        
        total_lines += num_lines
        total_bytes += num_bytes
        total_words += num_words
        
        num_result_line = f'{num_lines:8}' if args.line else ''
        num_result_word = f'{num_words:8}' if args.word else ''
        num_result_byte = f'{num_bytes:8}' if args.byte else ''
        num_result = f'{num_result_line}{num_result_word}{num_result_byte} {fh.name}'
        print(num_result)
    
    if len(args.file) > 1:
        total_result_line = f'{total_lines:8}' if args.line else ''
        total_result_word = f'{total_words:8}' if args.word else ''
        total_result_byte = f'{total_bytes:8}' if args.byte else ''
        total_result = f'{total_result_line}{total_result_word}{total_result_byte} total'
        print(total_result)


# --------------------------------------------------
if __name__ == '__main__':
    main()
