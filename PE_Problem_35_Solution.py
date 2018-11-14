import time

start = time.time()

sieve = [True] * 1000000

def not_prime(sieve, n):
    for i in range(n+n, len(sieve), n):
        sieve[i] = False

for n in range(2, int(len(sieve)**0.5)+1):
    if sieve[n]:
        not_prime(sieve, n)
        
lt = [2,3,5,7]
for i in range(2, 1000000):
    if sieve[i]:
        lt1 = []
        for x in range(1,len(str(i))):
            j = (int(str(i)[x:]+str(i)[:x]))
            lt1.append(j)
        
        if all(sieve[k] for k in lt1) and i not in lt:
            lt.append(i)

print(len(lt))

end = time.time() - start

print(end)

