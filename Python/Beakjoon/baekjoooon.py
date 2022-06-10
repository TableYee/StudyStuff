from multiprocessing import Process

def place(y,x,z):
     if y >= a-1 or x >= a-1 or y < 0 or x < 0:
          return

     yee = 0
     output = [[y-1,x],[y,x-1],[y,x+1],[y+1,x]]
     
     for y1,x1 in output:
          if lst[y1][x1] == '*':
               lst[y1][x1] = z
          else:
               output[yee][0],output[yee][1] = -1,-1
          yee+=1
     print(y,x,z,output)

     p1 = Process(target=place,args=(*args, *kwargs,output[0][0],output[0][1],z+1,))
     p2 = Process(target=place,args=(*args, *kwargs,output[1][0],output[1][1],z+1,))
     p3 = Process(target=place,args=(*args, *kwargs,output[2][0],output[2][1],z+1,))
     p4 = Process(target=place,args=(*args, *kwargs,output[3][0],output[3][1],z+1,))
     p1.start()
     p2.start()
     p3.start()
     p4.start()

a = int(input())
b, c = map(int,input().split())

lst = [['*' for i in range(j,a+j)] for j in range(1,a*a,a)]
lst[b-1][c-1] = 1
place(b,c,2)

for i in lst:
    print(*i)
