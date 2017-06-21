import sys

#https://www.hackerrank.com/challenges/2d-array/problem

arr = []

for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

x = len(arr)
y = len(arr[0])

tot = 0
hourCountTots = []

posX = 0
posY = 0

while posY <= y-3:

    while posX <= x-3:
        

        try:   

            for j in range(posY,posY+3,1):
                if j == posY+1:
                    tot += arr[j][posX+1]
                    continue

                for i in range(posX,posX+3,1):
                    tot += arr[j][i]
        except IndexError:
            print "IndexError in: ", posX, posY


        hourCountTots += tot,
        tot = 0
                
        posX += 1

    posX = 0
    posY += 1

print max(hourCountTots)



        
        
        
