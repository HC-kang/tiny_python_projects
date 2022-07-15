#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Say Hello")
parser.add_argument("-n", "--name", metavar="name", default="World", help="Name to greet")
args = parser.parse_args()
print("Hello, " + args.name + "!")