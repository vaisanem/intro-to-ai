NUMBER_OF_PIXELS = 28 * 28

class Nn:

  def __init__(self, data):
    self.data = data

  def classify(self, char):
    diff = NUMBER_OF_PIXELS+1
    label = -1
    for one in self.data:
      alt = 0
      for i in range(NUMBER_OF_PIXELS):
        if char[i] != one["vector"][i]:
          alt += 1
      if alt < diff:
        diff = alt
        label = one["char"]
    return label