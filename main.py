import os
import argparse

import puzzles

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', help='Select the puzzle\'s number to run', type=int)
    parser.add_argument('-p', '--part', help='Select which part of the puzzle to run', type=int)
    args = parser.parse_args()

    with open(f'inputs/{args.number}.txt') as f:

        puzzle = getattr(puzzles, f'puzzle{args.number}_{args.part}')
        print(puzzle(f))

