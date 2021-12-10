lines = [i.strip().split("|") for i in open("input.txt")]
lines = [[lines[i][j].strip().split() for j in range(2)] for i in range(len(lines))]

def part1(lines):
    count = 0
    for i in range(len(lines)):
        for code in lines[i][1]:
            if len(code) in [2, 3, 4, 7]:
                count += 1
    return count

lenmap = {2:1, 3:7, 4:4, 7:8}

def lmap(line):
    letters = {} # like 1:{"a","b"}
    line = line[0] + line[1]
    for code in line:
        if len(code) in lenmap:
            number = lenmap[len(code)]
            letters[number] = set(code)
    for code in line:
        l, c = len(code), set(code)
        if l == 5: # so for numbers 2, 3, 5
            if len(c - letters[7]) == 2:
                # i.e. if 2 of the 5 segments aren't covered by 7 -> number is 3
                letters[3] = c
            elif len(c - letters[4]) == 3:
                # i.e. if 3 of the 5 segments aren't covered by 4 -> number is 2
                letters[2] = c
            else:
                letters[5] = c
        if l == 6: # so for numbers 0, 6, 9
            if len(c - letters[1]) == 5:
                # i.e. if 5 of the 6 segments aren't covered by 1 -> number is 6
                letters[6] = c
            elif len(c - letters[4]) == 3:
                # i.e. if 3 of the 6 segments aren't covered by 4 -> number is 0
                letters[0] = c
            else:
                letters[9] = c
    return letters

def part2(lines):
    count = 0
    for line in lines:
        [inp, out] = line
        letters = lmap(line)
        codes = {"".join(sorted(letters[num])):num for num in letters}
        start = 0
        for code in out:
            code = "".join(sorted(code))
            start = 10*start + codes[code]
        count += start
    return count
