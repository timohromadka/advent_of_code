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

def puzzle3_1(f):
    pairs = f.read().split("\n")
    splits = [(pair[0:len(pair)//2], pair[len(pair)//2:]) for pair in pairs]
    comms = [min(set(s1) & set(s2)) for s1,s2 in splits]
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alph_dict = {c:i for i,c in enumerate(alphabet, start=1)}
    return sum(alph_dict.get(letter) for letter in comms)

def puzzle3_2(f):
    pairs = f.read().split("\n")
    n = 3
    splits = [pairs[i:i+n] for i in range(0, len(pairs), n)]
    comms = [set(a) & set(b) & set(c) for a,b,c in splits]
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alph_dict = {c:i for i,c in enumerate(alphabet, start=1)}
    return sum(alph_dict.get(num) for num,*_ in comms)

