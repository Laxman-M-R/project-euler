myList = []
for a in range(2,101):
    for b in range(2,101):
      if a**b not in myList:  
        myList.append(a**b)
      
myList.sort()

print(len(myList))
      