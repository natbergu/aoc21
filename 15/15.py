cave = [[int(i) for i in line.strip()] for line in open("input.txt")]
HEIGHT, WIDTH = len(cave), len(cave[0])
GOAL = (HEIGHT-1, WIDTH-1)
START = (0, 0)

def findadj(point, height, width):
    (row, col) = point
    adjr = []
    adjc = []
    if row > 0:
        adjr += [row-1]
    if row < height-1:
        adjr += [row+1]
    if col > 0:
        adjc += [col-1]
    if col < width-1:
        adjc += [col+1]
    adj = []
    for c in adjc:
        adj += [(row, c)]
    for r in adjr:
        adj += [(r, col)]
    return adj

def distancetoend(point):
    return abs(point[0] - GOAL[0]) + abs(point[1] - GOAL[1])

def sortfrontier(frontier):
    return sorted(frontier, key=lambda lst: lst[1])[::-1]

def findpath(map, goal):
    height, width = len(map), len(map[0])
    frontier = [(START, 0)]
    prev = {START:None}
    totalcost = {START:map[0][0]}
    while len(frontier) > 0:
        frontier = sortfrontier(frontier)
        cur = frontier.pop()
        point = cur[0]
        if point != goal:
            for a in findadj(point, height, width):
                newcost = totalcost[point] + map[a[0]][a[1]]
                if a not in totalcost or newcost < totalcost[a]:
                    totalcost[a] = newcost
                    priority = newcost + distancetoend(a)
                    frontier.append((a, priority))
                    prev[a] = point
    return prev

def tallycost(lstprev, map, goal):
    cur = goal
    path = [goal]
    while lstprev[cur] != None:
        cur = lstprev[cur]
        path = [cur] + path
    risk = 0
    for point in path:
        if point != START:
            risk += map[point[0]][point[1]]
    return risk

print(tallycost(findpath(cave, GOAL), cave, GOAL))

def newboard(old):
    depth1 = [[i+1 if i+1 < 10 else i+1-9 for i in row] for row in old]
    depth2 = [[i+2 if i+2 < 10 else i+2-9 for i in row] for row in old]
    depth3 = [[i+3 if i+3 < 10 else i+3-9 for i in row] for row in old]
    depth4 = [[i+4 if i+4 < 10 else i+4-9 for i in row] for row in old]
    depth5 = [[i+5 if i+5 < 10 else i+5-9 for i in row] for row in old]
    depth6 = [[i+6 if i+6 < 10 else i+6-9 for i in row] for row in old]
    depth7 = [[i+7 if i+7 < 10 else i+7-9 for i in row] for row in old]
    depth8 = [[i+8 if i+8 < 10 else i+8-9 for i in row] for row in old]
    new = [[0 for j in range(WIDTH*5)] for i in range(HEIGHT*5)]
    for line in range(HEIGHT*5):
        if line < HEIGHT:
            new[line] = old[line] + depth1[line] + depth2[line] + depth3[line] + depth4[line]
        elif line < HEIGHT*2:
            new[line] = depth1[line-HEIGHT] + depth2[line-HEIGHT] + depth3[line-HEIGHT] + depth4[line-HEIGHT] + depth5[line-HEIGHT]
        elif line < HEIGHT*3:
            new[line] = depth2[line-HEIGHT*2] + depth3[line-HEIGHT*2] + depth4[line-HEIGHT*2] + depth5[line-HEIGHT*2] + depth6[line-HEIGHT*2]
        elif line < HEIGHT*4:
            new[line] = depth3[line-HEIGHT*3] + depth4[line-HEIGHT*3] + depth5[line-HEIGHT*3] + depth6[line-HEIGHT*3] + depth7[line-HEIGHT*3]
        else:
            new[line] = depth4[line-HEIGHT*4] + depth5[line-HEIGHT*4] + depth6[line-HEIGHT*4] + depth7[line-HEIGHT*4] + depth8[line-HEIGHT*4]
    return new

timesfive = newboard(cave)
NEWGOAL = (HEIGHT*5 - 1, WIDTH*5 - 1)

print(tallycost(findpath(timesfive, NEWGOAL), timesfive, NEWGOAL))