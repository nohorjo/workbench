
from solid import *
from solid.utils import *

from constants import *
from super_hole import *

def place(cuts):
  count = 1
  model = cube([89, 2400, count * 1])
  offset = 0
  for cut in cuts:
    model += forward(offset)(
      color('brown')(cube([89, cut, count * 10]))
    )
    offset = offset + cut
    count = count + 1
  
  print(2400 - offset)

  return model

def cut_check():
  gap = 100
  #2x4
  model = place([
    720,
    720,
    680,
  ])
  model = left(95)(model)
  model += place([
    720,
    720,
    680,
  ])
  model = left(95)(model)
  model += place([
    630,
    630,
    500,
    500,
  ])
  model = left(95)(model)
  model = right(gap * 3)(model)

  # return model

  #2x6
  model = place([
    1800,
    590,
  ])
  model = left(95)(model)
  model += place([
    1800,
    590,
  ])
  model = left(95)(model)
  model += place([
    1330,
    590,
  ])
  model = left(95)(model)
  model += place([
    1330,
  ])
  model = right(gap * 3)(model)

  return model

if __name__ == '__main__':
  model = cut_check()

  scad_render_to_file(model, '_%s.scad'% __file__.split('/')[-1][:-3])


