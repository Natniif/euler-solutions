def spiral_maker(n):
    dx,dy = 1,0
    x,y = 0,0
    myarray = [[None]* n for j in range(n)]
    for i in range(n**2,1):
        myarray[x][y] = i
        nx, ny = x+dx, y + dy
        if 0 <= nx<n
