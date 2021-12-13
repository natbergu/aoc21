input = open("input.txt")
dots = []
line = input.readline()
while line != "\n":
    dots.append([int(i) for i in line.strip("\n").split(",")])
    line = input.readline()
instructions = []
for line in input:
    instructions.append([line[11:].split("=")[0], int(line[11:].split("=")[1])])

sheet = [[False for c in range(max([dot[0] for dot in dots])+1)] for r in range(max([dot[1] for dot in dots])+1)]

for dot in dots:
    sheet[dot[1]][dot[0]] = True

def foldx(sh, index):
    lefthalf = [sh[row][:index] for row in range(len(sh))]
    righthalf = [sh[row][index+1:] for row in range(len(sh))]
    for row in range(len(righthalf)):
        for col in range(len(righthalf[0])):
            if righthalf[row][col]:
                lefthalf[row][~col] = True
    return lefthalf

def part1():
    res = foldx(sheet, instructions[0][1])
    return sum([row.count(True) for row in res])

def foldy(sh, index):
    tophalf = sh[:index]
    bottomhalf = sh[index+1:]
    for row in range(len(bottomhalf)):
        for col in range(len(bottomhalf[0])):
            if bottomhalf[row][col]:
                tophalf[~row][col] = True
    return tophalf

def view(sh):
    for row in sh:
        for col in row:
            print("#" if col else ".", end="")
        print()

def part2():
    cur = sheet
    for i in instructions:
        if i[0] == "x":
            cur = foldx(cur, i[1])
        else:
            cur = foldy(cur, i[1])
    return cur

print(part1())
view(part2())