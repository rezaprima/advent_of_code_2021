def calculate_positions(lines):
  position, depth, aim = (0,0,0)
  for line in lines:
    command, value = line.split(' ')
    if command == 'forward':
      position += int(value)
      depth += aim * int(value)
    if command == 'down':
      aim += int(value)
    if command == 'up':
      aim -= int(value)

  return (position, depth)

f = open("input.txt","r")
lines = f.readlines()
f.close()

position, depth = calculate_positions(lines)
print(position*depth)