f = open("input.txt", "r")
n = int(f.readline(1))
health=2000
injuries=1
defeated = [0]
for i in range(1, (n/2)+1):
    for j in range(i, n):
        if(health<=0 or injuries>=1000000):
            break;
        damage=int(f.readline(j))
        health=health-damage
        injuries=injuries*damage
        max[i]=max[i]+1
maximum=max(defeated)
for i in defeated:
    if i==maximum:
        print(defeated.index(i))
