import datetime
start = datetime.datetime.now()

def sum_of_divisors(n):
    sum1 = 1
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            sum1 += i + int(n/i)           
#           print (i, int(n/i))
    return(sum1)


# brute force   
#def amicable_numbers(l,m):
#    if (sum_of_divisors(l) == m and sum_of_divisors(m) == l) and l != m:
#        return (l,m)
#        
#lt = []
#for i in range(200,10000):
#    for j in range(200,10000):
#        if amicable_numbers(i,j) and i not in lt:
#            lt.append(i)
#            lt.append(j)
#            
#print (lt)

#optimal approach
lt = []
for i in range(2,10000):
    firstNum = sum_of_divisors(i)
    if firstNum != i and firstNum > 1:
        other_num = sum_of_divisors(firstNum)
        if other_num == i and firstNum not in lt and i not in lt:
            lt.extend([other_num, firstNum])
print(lt)
print(sum(lt))
end = datetime.datetime.now()
print('Executed in ' + str(end - start))


