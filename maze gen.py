import random

n=int(input())
maze = [[0 for __ in range(n)] for _ in range(n)]
maze[0][0] = 1

def find_paths():
    choices = []
    if x >= 2 and maze[y][x-2] == 0:
        choices.append([x-2, y])
    if y >= 2 and maze[y-2][x] == 0:
        choices.append([x, y-2])
    if x <= n-3 and maze[y][x+2] == 0:
        choices.append([x+2, y])
    if y <= n-3 and maze[y+2][x] == 0:
        choices.append([x, y+2])

    return choices

x, y = 0, 0

stack = [[0, 0]]

while len(stack):
    px, py = x, y
    options = find_paths()
    if options:
        choice = options[random.randint(0, len(options)-1)]
        x, y = choice
        stack.append([x, y])
        if px == x:
            maze[(py+y)//2][x] = 1
            maze[y][x] = 1
        else:
            maze[y][(px+x)//2] = 1
            maze[y][x] = 1
    else:
        x, y = stack.pop()

print(*[''.join(["##" if y else "  " for y in x])for x in maze], sep='\n')
    
    
