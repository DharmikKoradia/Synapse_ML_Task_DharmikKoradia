#Problem Statement
"""
3. Bombarding the region
You are a fighter jet pilot and have been given a map of the region (n x n) with multiple small
islands on it. The water is indicated by 0 and land is indicated by 1. Your chief commander, Sgt.
Valdimir Tupin, declared a war with the people on these islands, and has assigned you to drop
bombs on these islands. However, you are only left with 1 bomb, which has the blast region of
(m x m), and you aim to cause maximum damage to your enemies.
However, the bomb will only detonate if it lands on the ground; else the area of detonation goes
down to 0. The bomb is dropped from the center of the blast region.
Once you complete your mission, your job is to inform your Sgt. about the attack and provide
him the coordinates of the islands which have been destroyed.
Constraints:
'n' ≥ 'm'
'm'  is guaranteed to be an odd number
Note:
The bottom-left of the map signifies (0,0) coordinate
You have to drop the bomb as quickly as possible, you can't stay over enemy region for too long
(else you going down)
E.g:
[
[1,0,0,0,1],
[1,0,1,1,1],
[1,1,0,1,1],
[1,0,1,1,0],
[0,1,0,1,1]
]
For m=3, blast region is 3x3 matrix. The bomb would be dropped from the center of 3x3.
At coordinates (3,2), dropping a bomb would have the most impact, damaging 7 islands.
(These are coordinates and NOT INDEX)
Consider conventional x and y axes for coordinates
"""
def check_area(row,col, radius):
    half=radius//2 # This is floor division because normal division would give floating value
    destroyed_loc=[]
    for i in range(row-half,row+half+1):
        if i<0:  continue
        elif i>=n: break
        for j in range(col-half,col+half+1):
            if j<0:  continue
            elif j>=n: break
            if(grid[i][j]==1):
                destroyed_loc.append([j,n-1-i]) # we have to store it in the format of x,y
                # here i corresponds to row which is y co-ords and x corresponds to col which is j
    
    return len(destroyed_loc),destroyed_loc


    
n=int(input("Enter the size of the grid: "))
m=int(input("Enter the blast radius: "))

grid=[]
for _ in range(n):
    row=list(map(int,input().split()))
    grid.append(row)

max_damage=0
dropping_loc=[-1,-1]
max_area=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            damage,damaged_area=check_area(i,j,m)
            if(damage>max_damage):
                max_damage=damage
                max_area=damaged_area
                dropping_loc=[j,n-1-i]

print(f"The bomb should be dropped on {dropping_loc} for maximum damage")
print(f"The bomb affects {max_damage} locations and the co-ors affected are {max_area}")



        