#!/usr/bin/env python3
# Purpose: Say hello
"""
Hi.
"""

import argparse


def get_args():
    """hi."""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """hi."""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
