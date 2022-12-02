"""
For each subproblem, the TextWrapper object of the .txt file is passed
"""

def puzzle1_1(f):
    return max([sum([int(cal) for cal in cals.split("\n") if cal != '']) for cals in f.read().split("\n\n")])

def puzzle1_2(f):
    sums = [sum([int(cal) for cal in cals.split("\n") if cal != '']) for cals in f.read().split("\n\n")]
    return sum(sorted(sums, reverse=True)[:3])

def puzzle2_1(f):
    left = ('A','B','C') # rock paper scissors
    right = ('X','Y','Z') # rock paper scissors
    scores = (3,6,0) # draw win loss
    points = (1,2,3) # rock paper scissors
    pairs = f.read().split("\n")
    return sum(scores[(right.index(r) - left.index(l)) % 3] + points[right.index(r)] for l,_,r in pairs)

def puzzle2_2(f):
    left = ('A','B','C') # rock paper scissors
    right = ('X','Y','Z') # loss draw win
    scores = (0,3,6) # loss draw win
    points = (1,2,3) # rock paper scissors
    pairs = f.read().split("\n")
    return sum(scores[right.index(r)] + points[(left.index(l) + right.index(r) - 1) % 3] for l,_,r in pairs)