import time

start = time.time()

def fact(n):
   prod = 1
   for i in range(2,n+1):
       prod *= i
   return (prod)
   
    
myList = []
for i in range(10, 10000000):
    sums = 0
    for j in str(i):
        sums += fact(int(j))
    if sums == i:
        print(i)
        myList.append(i)
        
print(sum(myList))
        
end = time.time() - start
print(end)
