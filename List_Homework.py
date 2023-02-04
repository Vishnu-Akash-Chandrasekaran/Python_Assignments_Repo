#Question 24:
l=['1','2','3','4','5','6','7','8','9','10']
l1=list(map(int,l))
print(sum(l1))    
temp=[]
for i in l:
    temp.append(int(i))
print(sum(temp))