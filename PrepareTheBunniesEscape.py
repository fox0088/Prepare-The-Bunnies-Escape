import queue

def solution(maze):
    global bomb_avail
    bomb_avail=True
    ttl_steps=len(maze)*len(maze[0])
    numOf1s=sum(sum(maze,[]))
    min_steps=len(maze)+len(maze[0])-1
    maze[len(maze)-1][len(maze[0])-1]=-1
    bombed_q=queue.Queue()
    for z in range(numOf1s):
        bomb_avail=True
        visited=[]
        start_que=queue.Queue()
        start_que.put((0,0))
        cnt_que=queue.Queue()
        cnt_que.put(1)
        BFS_res=BFS(maze,start_que,visited,cnt_que,bombed_q)
        if BFS_res == min_steps: break
        if BFS_res < ttl_steps: ttl_steps=BFS_res
    return min(ttl_steps,BFS_res)

def BFS(maze,que,visited,cnt,bombed_q=None):
    global bomb_avail
    bombed_x=bombed_y=None
    cur_idx=que.get()
    counter=cnt.get()
    visited.append(cur_idx)
    cur_x,cur_y = cur_idx[0],cur_idx[1]
    element=maze[cur_x][cur_y]
    if element==-1:
        if not (bomb_avail) and bombed_x!=None:
            maze[bombed_x][bombed_y]=1
        return counter
    for i in range(cur_x-1,cur_x+2):
        for j in range(cur_y-1,cur_y+2):
            if not (i==cur_x and j==cur_y) \
               and not (abs(i-cur_x) and abs(j-cur_y)) \
               and (i>=0 and j>=0) \
               and i<len(maze) and j<len(maze[0]) \
               and (i,j) not in que.queue \
               and (i,j) not in visited \
               and (maze[i][j]!=1 or (maze[i][j]==1 and bomb_avail and (i,j) not in bombed_q.queue)):
                if maze[i][j]==1:
                    bomb_avail=False
                    bombed_q.put((i,j))
                    bombed_x=i
                    bombed_y=j
                que.put((i,j))
                cnt.put(counter+1)
    if que.qsize()==0: return 4000
    return BFS(maze,que,visited,cnt,bombed_q)

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))  #=> 7
print(solution([[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]]))  #=> 7
print(solution([[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]]))   #=> 7
print(solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]))  #=> 11
print(solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]))  #=> 21