f = open("input.txt","r")
lines = f.readlines()
f.close()

old_depth = None
count = 0
for line in lines:
  depth = int(line)
  if old_depth != None and depth > old_depth:
    count = count + 1
  old_depth = depth

print(count)