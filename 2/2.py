directions = [line.strip("\n").split(" ") for line in open("input.txt")]
depth = hpos = aim = 0
for di in directions:
    diff = int(di[1])
    if di[0] == "forward":
        hpos += diff
        depth += aim*diff
    elif di[0] == "up":
        aim -= diff
    elif di[0] == "down":
        aim += diff
