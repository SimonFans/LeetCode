def findMinMoves(s):
  if len(s) < 3:
    return 0
  s = [elem for elem in s]
  moves = 0
  index = 2
  while index < len(s):
    tempVal = s[index]
    if tempVal == s[index - 1] and tempVal == s[index - 2]:
        if (index + 2) < len(s) and tempVal == s[index + 1] and tempVal == s[index + 2]:
            s[index] = 'a' if tempVal == 'b' else 'b'
        else:
            s[index - 1] = 'a' if tempVal == 'b' else 'b'
        moves += 1
    index += 1

return moves
