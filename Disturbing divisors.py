n=int(input())
sum=0
cnt=0
for i in range(1,n+1):
    for j in range(1,i+1):
        if i %j==0:
            sum+=j
            cnt+=1
print(cnt,sum)
