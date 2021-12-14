[polymer, rules] = open("input.txt").read().split("\n\n")
rules = {line[:2]:line[6] for line in rules.split("\n")[:-1]}
paircounts = {p:polymer.count(p) for p in rules}
counts = {c:polymer.count(c) for c in set(rules.values())}

def step(pcnts, lcnts):
    new = {p:0 for p in pcnts}
    for p in pcnts:
        cnt = pcnts[p]
        insert = rules[p]
        lcnts[insert] += cnt
        left = p[0] + insert
        right = insert + p[1]
        new[left] += cnt
        new[right] += cnt
    return new, lcnts

def part1():
    curpcounts = paircounts
    curlcounts = counts
    for i in range(10):
        (curpcounts, curlcounts) = step(curpcounts, curlcounts)
    most, least = max(curlcounts.values()), min(curlcounts.values())
    return most - least

def part2():
    curpcounts = paircounts
    curlcounts = counts
    for i in range(40):
        (curpcounts, curlcounts) = step(curpcounts, curlcounts)
    most, least = max(curlcounts.values()), min(curlcounts.values())
    return most - least

print(part1())

counts = {c:polymer.count(c) for c in set(rules.values())}
print(part2())