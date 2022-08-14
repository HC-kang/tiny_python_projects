from multiprocessing.sharedctypes import Value
import os
import sys
import argparse

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)')
    
    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    
    if not os.path.isfile(args.file):
        return ValueError('not a file')
    
    fh = open(args.file, 'rt')
    for line in fh:
        print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
