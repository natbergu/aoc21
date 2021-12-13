input = open("input2.txt")
dots = []
line = input.readline()
while line != "\n":
    dots.append(line.strip("\n"))
    line = input.readline()
instructions = []
for line in input:
    instructions.append([line[11:].split("=")[0], int(line[11:].split("=")[1])])

def fold(dots, axis, index):
    for i in range(len(dots)):
        dot = [int(n) for n in dots[i].split(",")]
        if dot[axis] > index:
            dot[axis] = index*2 - dot[axis]
        dots[i] = ",".join(str(n) for n in dot)
    return dots

def part1():
    return len(set(fold(dots, 0, instructions[0][1])))

def part2():
    cur = dots
    for i in instructions:
        if i[0] == "x":
            cur = fold(cur, 0, i[1])
        else:
            cur = fold(cur, 1, i[1])
    return cur

def view(coords):
    coords = [[int(i) for i in c.split(",")] for c in coords]
    sheet = [[" " for c in range(max([int(c[0]) for c in coords])+1)] for r in range(max([int(c[1]) for c in coords])+1)]
    for c in coords:
        sheet[c[1]][c[0]] = "#"
    for line in sheet:
        print("".join(line))


view(set(part2()))