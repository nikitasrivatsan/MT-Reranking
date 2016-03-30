#!/usr/bin/env python

import optparse
import sys

def main():
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], 'w')

    for line in input_file:
        line_length = len(line.split(' ||| ')[1].split())
        output_file.write(line.strip() + " sentence_length=" + str(line_length) + "\n")

if __name__ == "__main__":
    main()
