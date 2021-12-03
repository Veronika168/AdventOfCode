z = 0
len = 0
inp = [] #input data
while(1):
    bin = input().strip()
    if(bin == ''): break
    len += 1
    inp.append(bin)
    
    

for line in inp:
    if (len(inp) == 1): break
    if(line[0]=='1'): z+=1

    print(z)
    inx_to_pop = []

    if(z > len/2):
        for i in range(len(inp)):
            if(inp[i] == '0'): inx_to_remove.append(line)
    else:
        for i in range(len(inp)):
            if(inp[i] == '1'): inx_to_remove.append(line)

    for line in inx_to_remove:
        inp.remove(line)
