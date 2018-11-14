myList = []
for i in range(2, 1000000):
    sums = 0
    for j in str(i):
        sums += (int(j))**5
    if sums == i:
        myList.append(i)
        
print(sum(myList))
            
