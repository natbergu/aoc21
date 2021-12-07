file = open("input.txt")
numbers = [int(i) for i in file.readline().split(",")]
rows = [row.split(" ") for row in file]

def validitem(item):
    if item in ["\n", ""]:
        return False
    else:
        return True
def validrow(row):
    if len(row) == 0:
        return False
    else:
        return True

rows = list(filter(validrow, [list(filter(validitem, row)) for row in rows]))
rows = [[int(i) for i in row] for row in rows]
boards = [rows[i:i+5] for i in range(0, len(rows), 5)]
marks = [[[False]*5 for i in range(5)] for j in range(len(boards))]

def updatemarks(boards, marks, numbers, index):
    for board in range(len(boards)):
        for row in range(5):
            for item in range(5):
                if boards[board][row][item] == numbers[index]:
                    marks[board][row][item] = True

def winningboard(marks, boardindex):
    board = marks[boardindex]
    cols = list(zip(board[0], board[1], board[2], board[3], board[4]))
    winning = False
    for col in cols:
        if all(col):
            winning = True
    for row in board:
        if all(row):
            winning = True
    return winning

def tally(boards, marks, boardindex, numbers, turn):
    board = boards[boardindex]
    bm = marks[boardindex]
    unmarked = 0
    for row in range(5):
        for item in range(5):
            if not bm[row][item]:
                unmarked += board[row][item]
    return numbers[turn] * unmarked

turn = 0
winners = []
while turn < len(numbers) and len(winners) < len(boards):
    updatemarks(boards, marks, numbers, turn)
    for boardindex in range(len(marks)):
        if winningboard(marks, boardindex) and boardindex not in winners:
            winners.append(boardindex)
    turn += 1

i = winners[-1]
turn -= 1
print(f"the board at index {i} has won last on turn {turn+1}!")
print(boards[i])
print(marks[i])
print(numbers[:turn+1])
print("total score:", tally(boards, marks, i, numbers, turn))

