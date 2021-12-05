def calculate_positions(lines):
  position, depth = (0,0)
  for line in lines:
    command, length = line.split(' ')
    if command == 'forward':
      position += int(length)
    if command == 'down':
      depth += int(length)
    if command == 'up':
      depth -= int(length)

  return (position, depth)

f = open("input.txt","r")
lines = f.readlines()
f.close()

position, depth = calculate_positions(lines)
print(position*depth)