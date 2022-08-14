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
    
    parser.add_argument('-n',
                        '--num',
                        help='number of lines to show',
                        metavar='int',
                        type=int,
                        default=0)
    
    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    
    if not os.path.isfile(args.file):
        return ValueError('not a file')
    
    fh = open(args.file, 'rt')
    if args.num:
        for line in fh.readlines()[-args.num:]:
            print(line.rstrip())    
    else:    
        for line in fh.readlines():
            print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
