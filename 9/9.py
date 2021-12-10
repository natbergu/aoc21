points = [[int(p) for p in line.strip()] for line in open("input.txt")]
# 100 rows by 100 columns
viewmode = [[("▓" if i == "9" else i) for i in line] for line in open("input.txt")]
def view():
    for line in viewmode:
        print("".join(line[:-1]))

def findadj(row, col):
    adjr = []
    adjc = []
    if row > 0:
        adjr += [row-1]
    if row < 99:
        adjr += [row+1]
    if col > 0:
        adjc += [col-1]
    if col < 99:
        adjc += [col+1]
    adj = []
    for c in adjc:
        adj += [(row, c)]
    for r in adjr:
        adj += [(r, col)]
    return adj

def findlows(points):
    lows = []
    for row in range(len(points)):
        for col in range(len(points[0])):
            p = points[row][col]
            adj = findadj(row, col)
            low = True
            for a in adj:
                if p >= points[a[0]][a[1]]:
                    low = False
            if low:
                lows += [points[row][col]]
    return lows

def part1(points):
    lows = findlows(points)
    return sum(lows) + len(lows)

def findlowpoints(points):
    lowpoints = []
    for row in range(len(points)):
        for col in range(len(points[0])):
            p = points[row][col]
            adj = findadj(row, col)
            low = True
            for a in adj:
                if p >= points[a[0]][a[1]]:
                    low = False
            if low:
                lowpoints += [(row,col)]
    return lowpoints

def filteradj(adj, points):
    return list(filter(lambda a: points[a[0]][a[1]] != 9, adj))

def basinset(points, point):
    frontier = [point]
    reached = {point}
    while len(frontier) > 0:
        cur = frontier.pop()
        for a in filteradj(findadj(cur[0], cur[1]), points):
            if a not in reached:
                frontier = [a] + frontier
                reached.add(a)
    return reached

def product(list):
    res = 1
    for n in list:
        res *= n
    return res

def part2(points):
    return product(sorted([len(basinset(points, p)) for p in findlowpoints(points)])[-3:])

print(part2(points))