z = [0 for i in range(12)]
print(z)
len = 0
while(1):
    bin = input().strip()
    if(bin == ''): break
    len += 1
    for i in range(12):
        if(bin[i]=='1'): z[i]+=1
print(z)
fin_gamma = []
fin_epsilon = []
for i in z:
    if(i > len/2):
        fin_gamma.append('1')
        fin_epsilon.append('0')
    else:
        fin_gamma.append('0')
        fin_epsilon.append('1')

 
print("".join(fin_gamma))
g = int("".join(fin_gamma),2)
print(g)


print("".join(fin_epsilon))
e = int("".join(fin_epsilon),2)
print(e)

print(g*e)
