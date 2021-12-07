li = [[[int(k) for k in j.split(",")] for j in i.strip().split("->")] for i in open("input.txt")]

def ishv(line):
    return True if line[0][0] == line[1][0] or line[0][1] == line[1][1] else False

hvlines = list(filter(ishv, li))

plot = [[0]*1000 for i in range(1000)]

def coveringhv(line):
    covering = []
    if line[0][0] != line[1][0]:
        xvals = [line[0][0], line[1][0]]
        start, end = min(xvals), max(xvals)
        covering += [[i, line[0][1]] for i in range(start,end+1)]
    else:
        yvals = [line[0][1], line[1][1]]
        start, end = min(yvals), max(yvals)
        covering += [[line[0][0], i] for i in range(start,end+1)]
    return covering

def covering(line):
    covering = []
    if ishv(line):
        covering = coveringhv(line)
    else:
        xvals, yvals = [line[0][0], line[1][0]], [line[0][1], line[1][1]]
        xsign = ysign = 1
        xdiff = xvals[1] - xvals[0]
        ydiff = yvals[1] - yvals[0]
        if xdiff < 0:
            xsign = -1
        if ydiff < 0:
            ysign = -1
        for i in range(abs(xdiff)+1):
            covering += [[xvals[0] + i*xsign, yvals[0] + i*ysign]]
    return covering

for line in li:
    for point in covering(line):
        [x, y] = point
        plot[y][x] += 1

dangerous = 0
for row in range(1000):
    for col in range(1000):
        if plot[row][col] >= 2:
            dangerous += 1

print(dangerous)
