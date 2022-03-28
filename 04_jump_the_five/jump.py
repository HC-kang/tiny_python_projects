#!/usr/bin/env python3
"""
Author : heechankang <heechankang@localhost>
Date   : 2022-03-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_text',
                        metavar='str',
                        help='Input messages')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # jumper = {
    #     '1': '9',
    #     '2': '8',
    #     '3': '7',
    #     '4': '6',
    #     '5': '0',
    #     '6': '4',
    #     '7': '3',
    #     '8': '2',
    #     '9': '1',
    #     '0': '5',
    # }
    jumper = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero',
    }
    print(args.input_text.translate(str.maketrans(jumper)))

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
