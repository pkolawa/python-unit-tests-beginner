"""This is your first python scripe"t with docstrings included.
You can place here block of text as well as scripts.
"""

import os
import random

FIRST_TUPLE = (5,5)
firstObject = {'name': "Peter", 'age': 25}

def clear():
  """Clear the screen"""
  os.system('cls' if os.name == 'nt' else 'clear')

def build_from_tuple(x_axis, y_axis):
  """Create and return a grid from FIRST_TUPLE

  >>> cells = build_from_tuple(2, 2)
  >>> len(cells)
  4

  """
  cells = []
  for y in range(y_axis):
    for x in range(x_axis):
      cells.append((x,y))
  return cells


def get_locations(cells):
  """Randomly picked starting locations on 3x3 grid checking if they are free

  >>> cells = build_from_tuple(3,3)
  >>> cell_1, cell_2, cell_3 = get_locations(cells)
  >>> cell_1 != cell_2 and cell_2 != cell_3
  True
  >>> cell_3 in cells
  True

  """
  occupied_cell_1 = random.choice(cells)
  occupied_cell_2 = random.choice(cells)
  occupied_cell_3 = random.choice(cells)

  if occupied_cell_1 == occupied_cell_2 or occupied_cell_1 == occupied_cell_3 or occupied_cell_2 == occupied_cell_3:
    occupied_cell_1, occupied_cell_2, occupied_cell_3 = get_locations(cells)

  return occupied_cell_1, occupied_cell_2, occupied_cell_3
