import time
from parameters import *
from random import randint

class Cell:
  def __init__(self, c1, c2, c3, x = None, y = None, aging = 0):
    self.id = int(time.time())
    self.c1, self.c2, self.c3 = c1, c2, c3
    self.x = x if x is not None else randint(MARGINS, width - MARGINS)
    self.y = y if y is not None else randint(MARGINS, height - MARGINS)
    self.birthTime = time.time()
    self.deathTime = self.birthTime + randint(MIN_LIFE_SECONDS, MAX_LIFE_SECONDS)
    self.aging = aging + randint(-RANDOM_DELTA_AGING, RANDOM_DELTA_AGING)
    # Avoid negative aging
    self.aging = self.aging if self.aging >= 0 else randint(START_MIN_AGING, START_MAX_AGING)
    # print("New cell, aging = ", self.aging, aging)

  def __str__(self):
    return "Cell #{}\nBirth: {}\nDeath: {}\nTTL: {} seconds\n".format(self.id, self.birthTime, self.deathTime, self.deathTime - self.birthTime)

  def liveAndReplicate(self, density = 0):
    self.deathTime -= (self.aging/100)

    # Solitude and Overpopulation
    if (density < MIN_DENSITY_IN_CELL or density > MAX_DENSITY_IN_CELL):
      # print("Too much density", density, MAX_DENSITY_IN_CELL)
      deltaAgingDEnsity = (DENSITY_AGING_WEIGHT * self.aging)
      # print("deltaAgingDEsnity = ", deltaAgingDEnsity)
      self.deathTime -= deltaAgingDEnsity

    if randint(0, 1000) > 995:
      return Cell(
        self.c1, self.c2, self.c3,
        self.x + (randint(-RANDOM_DELTA_POSITION, RANDOM_DELTA_POSITION)),
        self.y + (randint(-RANDOM_DELTA_POSITION, RANDOM_DELTA_POSITION)),
        self.aging
      )
    return None

  def isAlive(self):
    # True if alive, False otherwise
    return (
      time.time() < self.deathTime and
      width-MARGINS > self.x > MARGINS
      and height-MARGINS > self.y > MARGINS
    )

  def render(self):
    missingTime = self.deathTime - self.birthTime
    fill(self.c1 - missingTime, self.c2 - missingTime, self.c3 - missingTime)
    ellipse(self.x, self.y, missingTime, missingTime)
