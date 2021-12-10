lines = [line.strip() for line in open("input.txt")]

charmap = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}

def check(line):
    cur = []
    for c in line:
        if c in charmap:
            cur.append(charmap[c])
        elif c in cur[-1:]:
            cur.pop()
        else:
            return False, c
    return True, "".join(reversed(cur)) # comes in handy for part 2

completelines = list(filter(lambda line: check(line)[0] == False, lines))

scores = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

def part1(clines):
    score = 0
    for line in clines:
        score += scores[check(line)[1]]
    return score

print(part1(completelines))

incompletelines = list(filter(lambda line: check(line)[0] == True, lines))

scores2 = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}

def part2(iclines):
    lstscores = []
    for line in iclines:
        score = 0
        for c in check(line)[1]:
            score *= 5
            score += scores2[c]
        lstscores.append(score)
    return sorted(lstscores)[len(lstscores)//2]

print(part2(incompletelines))