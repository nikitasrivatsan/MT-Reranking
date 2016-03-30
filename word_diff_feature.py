#!/usr/bin/env python

import sys

def main():
    best = open(sys.argv[1])
    source = open(sys.argv[2])
    outfile = open(sys.argv[3], 'w')

    i = -1
    for line in best:
        i += 1
        best_words = len(line.split(' ||| ')[1].split())
        if i % 100 == 0:
            source_line = source.readline()
        source_words = len(source_line.split(' ||| ')[1].split())
        outfile.write(line.strip() + " word_diff=" + str(source_words - best_words) + "\n")

if __name__ == "__main__":
    main()
