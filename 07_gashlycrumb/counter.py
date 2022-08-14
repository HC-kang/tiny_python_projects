import os
import collections
import argparse

# --------------------------------------------------
def get_args():

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('filename',
                        metavar='str',
                        help='A positional argument')
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    
    args = get_args()
    
    if not os.path.isfile(args.filename):
        ValueError('Not a file')
    
    dict = collections.defaultdict(int)
    fh = open(args.filename)
    for line in fh.readlines():
        for word in line.split():
            dict[word] += 1
    
    sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    print(sorted_dict[:10])


# --------------------------------------------------
if __name__ == '__main__':
    main()