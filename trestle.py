from solid import *
from solid.utils import *

from constants import *
from super_hole import *

from rear_leg import *
from front_leg import *

def trestle(isRight = False):
  gap_between_legs = total_width - (2 * leg_width) + ACT2

  model = rear_leg()
  model += right(total_width - leg_width)(front_leg())

  model += translate([leg_width - ACT2, 0, leg_height])(
    rotate(90, FORWARD_VEC)(
      x2x4(gap_between_legs + (ACT2 / 2))
    )
  )
  model += translate([0, ACT2_LONG * (1 if isRight else 2), ACT10 + trestle_stretcher_offset])(
    rotate(90, FORWARD_VEC)(rotate(90, DOWN_VEC)(
      x2x10(total_width)
    ))
  )
  return model

if __name__ == '__main__':
  model = trestle()
  
  scad_render_to_file(model, '_%s.scad'% __file__.split('/')[-1][:-3])
