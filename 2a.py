horizontal = 0
depth = 0
while(1):
   line = input().strip()
   if(line == ""): break
   op, dist = line.split()
   dist = int(dist)
   if (op == "forward"):
       horizontal += dist
   if (op == "down"):
       depth += dist
   if (op == "up"):
       depth -= dist
print("depth:", depth, "horizontal:",horizontal)
print(depth*horizontal)
