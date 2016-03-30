#!/usr/bin/env python

import sys

def main():
    100best = open(sys.argv[1])
    source = open(sys.argv[2])
    outfile = open(sys.argv[3], 'w')

    for line in 100best:
        100best_words = len(line.split('|||')[1].split())
        source_line = source.readline()
        source_words = len(source_line.split('|||')[1].split())
        outfile.write(line.strip() + " word_diff=" + str(source_words - 100best_words) + "\n")

if __name__ == "__main__":
    main()
