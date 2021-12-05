def depth_count(lines):
  old_depth = None
  count = 0
  window=[0,0,0]
  for idx,line in enumerate(lines):
    depth = int(line)
    window[idx%3]=depth
    if idx < 2:
      continue

    total_depth = sum(window)
    if old_depth != None and total_depth > old_depth:
      count = count + 1
    old_depth = total_depth

  return count

f = open("input.txt","r")
lines = f.readlines()
f.close()

count = depth_count(lines)
print(count)