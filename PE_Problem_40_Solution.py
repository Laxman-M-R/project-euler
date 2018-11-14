str1 = ''

for i in range(1,1000000):
    str1 = str1 + str(i)
    
c = int(str1[0])*int(str1[9])*int(str1[99])*int(str1[999])*int(str1[9999])*int(str1[99999])*int(str1[999999])

print(c)
