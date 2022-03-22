#!/usr/bin/env python3
"""
Author : heechankang <heechankang@localhost>
Date   : 2022-03-22
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    
    parser.add_argument('-s',
                        '--side',
                        help='which side',
                        metavar='side',
                        type=str,
                        default='larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side

    if not word[0].isalpha():
        print('cannot do this. please insert callable name')
        return

    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    article = article.title() if word[0].isupper() else article

    string = f'Ahoy, Captain, {article} {word} off the larboard bow!'
    
    if side is not None:
        string = string.replace('larboard', side)

    print(string)
    return 


# --------------------------------------------------
if __name__ == '__main__':
    main()
