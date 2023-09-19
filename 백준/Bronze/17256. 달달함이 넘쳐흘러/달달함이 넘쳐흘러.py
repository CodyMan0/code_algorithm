(ax,ay,az) = list(map(int,input().split()))
(bx,by,bz)= (0,0,0)
(cx,cy,cz) = list(map(int,input().split()))

t = ((az + bx), (ay*(by+1)), (ax + bz))
result = (abs(cx - t[0]) , abs(int(cy/t[1])) ,abs(t[2] -cz))
print(*result)