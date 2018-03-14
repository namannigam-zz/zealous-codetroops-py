hiddenfield =  [[0, 0, 0, 0, 0, 'M', 0, 0, 0, 'M'],
            [0, 0, 0, 'M', 0, 0, 0, 'M', 'M', 'M'],
            [0, 0, 'M', 0, 'M', 0, 0, 'M', 0, 'M'],
            [0, 0, 0, 0, 'M', 0, 0, 0, 0, 0],
            [0, 0, 'M', 0, 'M', 0, 0, 0, 0, 0],
            [0, 0, 0, 'M', 0, 'M', 'M', 0, 0, 0],
            ['M', 0, 0, 'M', 0, 0, 0, 'M', 0, 0],
            [0, 0, 0, 'M', 0, 0, 0, 0, 0, 0],
            [0, 'M', 'M', 0, 'M', 0, 0, 0, 0, 'M'],
            ['M', 0, 0, 'M', 0, 0, 0, 0, 'M', 0]]



def update_numbers(x, y, hiddenfield):
    try:
        if hiddenfield[x][y] != 'M':
            hiddenfield[x][y] += 1
    except IndexError:
        pass

def numbersinhiddefield(indexes):
    indexes = [[i,j] for i,row in enumerate(indexes) for j,elem in enumerate(row) if elem == 'M']
    loop = 0
    while loop < len(indexes):
        update_numbers(indexes[loop][i-1,j-1,hiddenfield);
        update_numbers(i-1,j,hiddenfield);
        update_numbers(i-1,j+1,hiddenfield);
        update_numbers(i,j-1,hiddenfield);
        update_numbers(i,j+1,hiddenfield);
        update_numbers(i+1,j-1,hiddenfield);
        update_numbers(i+1,j,hiddenfield);
        update_numbers(i+1,j+1,hiddenfield);
        loop += 1

def showMineFieldHidden(hiddenfield):
    border = list(range(0,len(hiddenfield)))
    row = [' ']+border
    i = 0
    for rows in [border]+hiddenfield:
        print(row[i])
        i += 1
        for lines in rows:
            print(lines)
        print()

numbersinhiddefield(hiddenfield)

showMineFieldHidden(hiddenfield)