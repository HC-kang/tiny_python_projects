#!/usr/bin/env python3
"""
Author : Ford <weston0713@gmail.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse

template = 'Ahoy, Captain, {} {} off the {} bow!'

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    
    parser.add_argument('-s',
                        '--side',
                        help='which side',
                        metavar='str',
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
        raise ValueError('please enter proper word.')
    
    if side not in ['larboard', 'starboard']:
        raise ValueError('please select "larboard" or "starboard"')

    article = 'A' if word[0].isupper() else 'a'
    article = article+'n' if word[0].lower() in 'aeiou' else article

    print(template.format(article, word, side))


# --------------------------------------------------
if __name__ == '__main__':
    main()
