school = list(map(int, open("input.txt").readline().strip().split(",")))
ocean = {i:0 for i in range(9)}
for fish in school:
    ocean[fish] += 1

def newday(ocean):
    end = ocean[0]
    for i in range(1,9):
        ocean[i-1] = ocean[i]
    ocean[6] += end
    ocean[8] = end
    return ocean

for i in range(256):
    newday(ocean)
    print("day", i+1, sum(ocean.values()))
