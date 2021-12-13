connections = [line.strip().split("-") for line in open("input.txt")]
graph = dict()
for c in connections:
    if c[0] in graph:
        graph[c[0]].append(c[1])
    else:
        graph[c[0]] = [c[1]]
    if c[1] in graph:
        graph[c[1]].append(c[0])
    else:
        graph[c[1]] = [c[0]]

visited = {k:False for k in graph}

def generatepaths(start):
    if start == "end":
        return ["end"]
    else:
        visited[start] = True
        paths = []
        for node in graph[start]:
            if node.isupper() or not visited[node]:
                new = [start] + generatepaths(node)
                if "end" in new:
                    paths += new
                visited[node] = False
        return paths

def part1():
    return generatepaths("start").count("end")

print(part1())

def generatepaths2():
    frontier = [(["start"], True)]
    complete = []
    while frontier:
        (cur, vis) = frontier.pop()
        for c in graph[cur[-1]]:
            if c == "end":
                complete.append((cur + [c], vis))
            elif c != "start":
                if c.isupper() or c not in cur:
                    frontier.append((cur + [c], vis))
                elif vis:
                    frontier.append((cur + [c], False))
    return len(complete)

def part2():
    return generatepaths2()

print(part2())