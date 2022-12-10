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
def puzzle4_1(f):
    pairs = [p.split(',') for p in f.read().split("\n")]
    splits = [(p1.split('-'), p2.split('-')) for p1,p2 in pairs]
    splits = [(int(l[0]), int(l[1]), int(r[0]), int(r[1])) for l,r in splits]
    count = sum(((a<=c and b>=d) | (c<=a and d>=b)) for a,b,c,d in splits)
    return count
def puzzle4_2(f):
    pairs = [p.split(',') for p in f.read().split("\n")]
    splits = [(p1.split('-'), p2.split('-')) for p1,p2 in pairs]
    splits = [(int(l[0]), int(l[1]), int(r[0]), int(r[1])) for l,r in splits]
    count = sum(((a<=c<=b) | (a<=d<=b) | (c<=a<=d) | (c<=b<=d)) for a,b,c,d in splits)
    return count
def puzzle5_1(f):
    from collections import deque

    pairs = f.read().split("\n")
    start = pairs.index('')
    crates = [[_char for _char in line[1::4]] for line in pairs[:start-1][::-1]]
    crates = [tuple(c for c in stack if c != ' ') for stack in list(zip(*crates))]
    stacks = [deque(lst) for lst in crates]

    for command in pairs[start+1:]:
        command = command.split(" ")
        how_many = int(command[1])
        from_where = int(command[3])-1
        to_where = int(command[5])-1
        for _ in range(how_many):
            stacks[to_where].append(stacks[from_where].pop()) 
    return "".join(stack.pop() for stack in stacks)

def puzzle5_2(f):

    from collections import deque

    pairs = f.read().split("\n")
    start = pairs.index('')
    crates = [[_char for _char in line[1::4]] for line in pairs[:start-1][::-1]]
    crates = [tuple(c for c in stack if c != ' ') for stack in list(zip(*crates))]
    stacks = [deque(lst) for lst in crates]

    for command in pairs[start+1:]:
        command = command.split(" ")
        how_many = int(command[1])
        from_where = int(command[3])-1
        to_where = int(command[5])-1
        to_move = [stacks[from_where].pop() for _ in range(how_many)]
        for val in to_move[::-1]:
            stacks[to_where].append(val) 


    return "".join(stack.pop() for stack in stacks)
def puzzle6_1(f):
    text = f.read()
    return next(i+4 for i,_ in enumerate(text) if len(set(text[i:i+4])) == 4)
def puzzle6_2(f):
    text = f.read()
    return next(i+14 for i,_ in enumerate(text) if len(set(text[i:i+14])) == 14)
def puzzle7_1(f):
    from collections import deque, Counter
    from rich import print as rprint
    lines = f.read().split("\n$ cd")
    lines = [line.split("\n") for line in lines if line != ' ..'] # ignore 'cd ..'

    class TreeRecurser():
        def __init__(self, total_size, threshold,lines):
            self.total_size = total_size
            self.threshold = threshold
            self.lines = lines
            self.jumping_index = 0

        def add_mappings(self):
            cur_index = self.jumping_index
            self.jumping_index += 1
            for i,cmd in enumerate(self.lines[cur_index]):
                if 'dir ' in cmd:
                    self.lines[cur_index][i] = self.jumping_index
                    self.add_mappings()

        def get_size(self, idx):
            dir_size = 0
            for sub_cmd in self.lines[idx][2:]:
                if isinstance(sub_cmd,int):
                    dir_size += self.get_size(sub_cmd) # point to index where to go
                else:
                    dir_size += int(sub_cmd.split(" ")[0])
            if dir_size < self.threshold:
                self.total_size += dir_size
            return dir_size
    
    rec = TreeRecurser(0,100000,lines)
    rec.add_mappings()
    rec.get_size(0)
    return rec.total_size

def puzzle7_2(f):
    from collections import deque, Counter
    from rich import print as rprint
    lines = f.read().split("\n$ cd")
    lines = [line.split("\n") for line in lines if line != ' ..'] # ignore 'cd ..'

    class TreeRecurser():
        def __init__(self, total_size, threshold, lines, max_space):
            self.dir_sizes = []
            self.total_size = total_size # total size is actually total size now
            self.threshold = threshold
            self.lines = lines
            self.max_space = max_space
            self.jumping_index = 0

        def set_total_size(self, val):
            self.total_size = val
        
        def get_closest_to_val(self, val):
            return min([dir_size for dir_size in self.dir_sizes if val < dir_size])

        def add_mappings(self):
            cur_index = self.jumping_index
            self.jumping_index += 1
            for i,cmd in enumerate(self.lines[cur_index]):
                if 'dir ' in cmd:
                    self.lines[cur_index][i] = self.jumping_index
                    self.add_mappings()

        def get_size(self, idx):
            dir_size = 0
            for sub_cmd in self.lines[idx][2:]:
                if isinstance(sub_cmd,int):
                    dir_size += self.get_size(sub_cmd) # point to index where to go
                else:
                    dir_size += int(sub_cmd.split(" ")[0])
            self.dir_sizes.append(dir_size)
            return dir_size
    
    rec = TreeRecurser(0, 100_000, lines, 70_000_000)
    rec.add_mappings()
    rec.set_total_size(rec.get_size(0))
    boundary = 30_000_000 - (rec.max_space - rec.total_size)


    return rec.get_closest_to_val(boundary)