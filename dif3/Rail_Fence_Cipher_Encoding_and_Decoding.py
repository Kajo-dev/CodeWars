def encode_rail_fence_cipher(string, rails):
  # Create a list of empty strings to represent the rails
  rail_fence = [[] for _ in range(rails)]

  # Initialize the direction to be down
  direction = 'down'
  rail = 0

  # Iterate through the string and add each character to the appropriate rail
  for c in string:
    rail_fence[rail].append(c)
    if rail == 0:
      direction = 'down'
    elif rail == rails - 1:
      direction = 'up'
    if direction == 'down':
      rail += 1
    else:
      rail -= 1

  # Concatenate the characters in each rail to get the encoded string
  encoded = ''.join([''.join(rail) for rail in rail_fence])
  return encoded
