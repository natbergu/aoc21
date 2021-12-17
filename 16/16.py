data = open("input.txt").readline().strip()
LENGTH = len(data)*4
data = f"{int(data, 16):0>{LENGTH}b}"

def nextpacket(bits):
    version = int(bits[:3], 2)
    typeid = bits[3:6]
    if typeid == "100":
        index = 6
        literal = ""
        done = False
        while not done and index < len(bits):
            if bits[index] == "0":
                done = True
            literal += bits[index+1:index+5]
            index += 5
        return version, index, typeid, int(literal, 2)
    else:
        if int(bits[6]):
            lentypeid = 11
            subpacknum = int(bits[7:7+lentypeid], 2)
            subpacks = bits[7+lentypeid:]
            lstpacks = []
            indexsum = 0
            while len(lstpacks) < subpacknum:
                next = nextpacket(subpacks)
                lstpacks.append(next)
                indexsum += next[1]
                subpacks = subpacks[next[1]:]
            return version, 7+lentypeid+indexsum, typeid, lstpacks
        else:
            lentypeid = 15
            subpacklen = int(bits[7:7+lentypeid], 2)
            subpacks = bits[7+lentypeid:7+lentypeid+subpacklen]
            lstpacks = []
            while len(subpacks) > 0:
                next = nextpacket(subpacks)
                lstpacks.append(next)
                subpacks = subpacks[next[1]:]
            return version, 7+lentypeid+subpacklen, typeid, lstpacks

def parsebits(bits):
    index = 0
    hierarchy = []
    datalen = len(bits.rstrip("0"))
    while index < datalen:
        next = nextpacket(bits[index:])
        hierarchy.append(next)
        index = next[1]
    return hierarchy

# test cases
# print(parsebits("110100101111111000101000"))
# print(parsebits("00111000000000000110111101000101001010010001001000000000"))
# print(parsebits("11101110000000001101010000001100100000100011000001100000"))
# print(parsebits("100010100000000001001010100000000001101010000000000000101111010001111000"))
# print(parsebits("01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100"))
# print(parsebits("1100000000000001010100000000000000000001011000010001010110100010111000001000000000101111000110000010001101000000"))
# print(parsebits("101000000000000101101100100010000000000101100010000000010111110000110110100001101011000110001010001111010100011110000000"))

def sumver(res):
    res = str(res).split("(")[1:]
    return sum(int(c[0]) for c in res)

def part1(bits):
    return sumver(parsebits(bits))

print(part1(data))

def evaluate(packet):
    res = []
    for p in packet:
        pid = int(p[2], 2)
        if pid == 4:
            res.append(p[3])
        else:
            inner = evaluate(p[3])
            if pid == 0:
                res.append(sum(inner))
            elif pid == 1:
                prod = 1
                for x in inner:
                    prod *= x
                res.append(prod)
            elif pid == 2:
                res.append(min(inner))
            elif pid == 3:
                res.append(max(inner))
            elif pid == 5:
                res.append(1 if inner[0] > inner[1] else 0)
            elif pid == 6:
                res.append(1 if inner[0] < inner[1] else 0)
            elif pid == 7:
                res.append(1 if inner[0] == inner[1] else 0)
    return res

print(evaluate(parsebits(data)))
