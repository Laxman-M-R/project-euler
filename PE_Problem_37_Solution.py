import time

start = time.time()

sieve = [True] * 1000000

def not_prime(sieve, n):
    for i in range(n+n, len(sieve), n):
        sieve[i] = False

for n in range(2, int(len(sieve)**0.5)+1):
    if sieve[n]:
        not_prime(sieve, n)

lt = []        
for i in range(10, 1000000):
    if str(i)[0] != '1' and str(i)[-1] != '1' and sieve[i]:
        lt1 = []
        for x in range(1, len(str(i))):
            lt1.append(int(str(i)[x:]))
            lt1.append(int(str(i)[:x]))
            
        if all(sieve[k] for k in lt1):
            lt.append(i)
            
    else:
        continue
          
print(sum(lt))

end = time.time() - start

print(end)

