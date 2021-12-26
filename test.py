

import io
import sys




_INPUT = u"""\
5 5
.....
.....
.....
.....
.....
"""
if __file__ == "test.py":
    sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]



h, w = map(int, lines[0].split())
maze = [list(l) for l in lines[1:]]
sentaku = [(1, 0), (0, 1)]
step_list = []

def dfs(A):
    global maze, step_list
    # global step_list
    # result = []
    # いまのポジションが壁もしくは場外なら打ち切り
    i, j = A[-1]
    if (maze[i][j]=="$"):
        return
    
    if (i == h) | (j == w):
        step_list.append(A)
        return
    if (maze[i][j]=="#"):
        # step_list.append(step_list)
        step_list.append(A)
        return
    
    
    # C = A
    # result.append(A)
    # print(step_list)
    # 迷路なら重複枝刈り
    maze[i][j]=="$"
    # print(maze)
    # step_list.append(A)
    # print(maze[i][j])
    # res = 0
    for a, b in sentaku:
        # print((i+a, j+b))

        # print(step_list)
        # print(A)
        dfs(A+[(i+a, j+b)])
    A.pop()
    # print(step_list)
    # return len(A)

# def test():
#     step_list.append("test")
# test()
dfs([(0,0)])
print(len(step_list))