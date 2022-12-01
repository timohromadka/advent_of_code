def puzzle1_1(f):
    return max([sum([int(cal) for cal in cals.split("\n") if cal != '']) for cals in f.read().split("\n\n")])

def puzzle1_2(f):
    sums = [sum([int(cal) for cal in cals.split("\n") if cal != '']) for cals in f.read().split("\n\n")]
    return sum(sorted(sums, reverse=True)[:3])