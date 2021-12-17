target = [tuple(int(num) for num in c.strip()[2:].split("..")) for c in open("input.txt").read().strip()[13:].split(",")]

def step(position, vx, vy):
    (x, y) = position
    x += vx
    y += vy
    vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else 0
    vy -= 1
    return (x, y), vx, vy

def landed(pos, targ):
    if min(targ[0]) <= pos[0] <= max(targ[0]) and min(targ[1]) <= pos[1] <= max(targ[1]):
        return True
    else: return False

def shoot(vxi, vyi, targ):
    xvel, yvel = vxi, vyi
    pos = (0, 0)
    maxypos = 0
    while not landed(pos, targ):
        if abs(pos[0]) <= max(abs(i) for i in targ[0]) and pos[1] >= min(targ[1]):
            (pos, xvel, yvel) = step(pos, xvel, yvel)
            # print(pos, xvel, yvel)
            maxypos = max(maxypos, pos[1])
        else: return False, maxypos
    return True, maxypos

print(shoot(14, 146, target))

def part1(targ):
    best = 0
    for xval in range(14, 99):
        for yval in range(1, 500):
            shot = shoot(xval, yval, targ)
            if shot[0]:
                print(shot[1])
                best = max(best, shot[1])
    return best

# print(part1(target))

def part2(targ):
    lst = set()
    for xval in range(14, 200):
        for yval in range(-200, 200):
            shot = shoot(xval, yval, targ)
            if shot[0]:
                lst.add((xval, yval))
    return len(lst)

print(part2(target))