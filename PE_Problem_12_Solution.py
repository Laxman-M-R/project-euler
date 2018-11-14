sum1 = 0
i = 1
arr = []

# find the sum of natural numbers 
while i > 0:
  sum1 += i
  
  
# find the divisors
  for j in range(1, int(sum1**0.5)+1):
    if sum1 % j == 0:
      arr.append(j)
      arr.append(int(sum1/j))
      
  
  if len(arr) > 500:
    break
  else:
    arr = []
  
  i += 1
  
print (sum1)    
