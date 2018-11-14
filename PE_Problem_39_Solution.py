from collections import Counter
       
lt = []
for a in range(2,500):
    for b in range(2,500):
        c = (a**2 + b**2)**0.5
        if c == int(c):
            p = a + b + c
            if p <= 1000:
                lt.append(p)
            
data = Counter(lt)     
print(data.most_common(1))

        