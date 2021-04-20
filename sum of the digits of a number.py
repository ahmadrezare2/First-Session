n=int(input())
nums = str(n)
aa = []
for i in range(len(nums)):
    aa.append(int(nums[i]))
ss = sum(aa)
while ss > 9:
    bb = []
    for j in range(len(str(ss))):
        bb.append(int(str(ss)[j]))
    ss = sum(bb)
print(ss)




