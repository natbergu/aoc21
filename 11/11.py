def findadj(point):
    (row, col) = point
    adjr = []
    adjc = []
    if row > 0:
        adjr += [row-1]
    if row < 9:
        adjr += [row+1]
    if col > 0:
        adjc += [col-1]
    if col < 9:
        adjc += [col+1]
    adj = []
    for c in adjc:
        adj += [(row, c)]
    for r in adjr:
        adj += [(r, col)]
    for r in adjr:
        for c in adjc:
            adj += [(r, c)]
    return adj

def flash(point, flashed):
    flashed.add(point)
    adj = findadj(point)
    for p in adj:
        if p not in flashed:
            octopi[p[0]][p[1]] += 1
            if octopi[p[0]][p[1]] == 10:
                flash(p, flashed)

def reset():
    for row in range(10):
        for col in range(10):
            if octopi[row][col] > 9:
                octopi[row][col] = 0

def step():
    flashed = set()
    for row in range(10):
        for col in range(10):
            if (row, col) not in flashed:
                octopi[row][col] += 1
                if octopi[row][col] == 10:
                    flash((row, col), flashed)
    reset()
    return len(flashed)

def view():
    print()
    for line in octopi:
        print("".join(str(i) for i in line))

def part1():
    flashes = 0
    for i in range(100):
        flashes += step()
    return flashes

def part2():
    flashes = 0
    s = 0
    while flashes < 100:
        flashes = step()
        s += 1
    view()
    return s

octopi = [[int(i) for i in line.strip()] for line in open("input.txt")]
print(part1())

octopi = [[int(i) for i in line.strip()] for line in open("input.txt")]
print(part2())