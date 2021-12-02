horizontal = 0
depth = 0
aim = 0
while(1):
   line = input().strip()
   if(line == ""): break
   op, dist = line.split()
   dist = int(dist)
   if (op == "forward"):
       horizontal += dist
       depth += aim*dist
   if (op == "down"):
       aim += dist
   if (op == "up"):
       aim -= dist
print("depth:", depth, "horizontal:",horizontal)
print(depth*horizontal)
