crabs = list(map(int, open("input.txt").readline().strip().split(",")))

def calcfuel(pos, crabs):
    fuel = 0
    nzcrabs = list(filter(lambda x: x != pos, crabs))
    numcrabs = {i:0 for i in range(max(nzcrabs)+1)}
    for crab in nzcrabs:
        numcrabs[crab] += 1
    for i in range(max(nzcrabs)+1):
        fuel += numcrabs[i]*abs(i - pos) 
    return fuel

def calcfuel2(pos, crabs):
    fuel = 0
    nzcrabs = list(filter(lambda x: x != pos, crabs))
    numcrabs = {i:0 for i in range(max(nzcrabs)+1)}
    for crab in nzcrabs:
        numcrabs[crab] += 1
    for i in range(max(nzcrabs)+1):
        n = abs(i - pos)
        fuel += numcrabs[i]*(n*(n+1)//2)
    return fuel

lstfuel = [calcfuel2(i, crabs) for i in range(max(crabs)+1)]
print(min(lstfuel))
