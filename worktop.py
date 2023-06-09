
from solid import *
from solid.utils import *

from constants import *
from super_hole import *

def support():
  model = x2x6((total_width - (0 * ACT2_LONG)))
  model = rotate(90, FORWARD_VEC)(model)
  model = rotate(90, UP_VEC)(model)
  model = translate([
    ACT2_LONG + ACT6,
    0,
    (total_length + ACT2_LONG) / 2
  ])(model)

  return model

def worktop():
  model = x2x6(total_length)
  model += forward(ACT6)(x2x10(total_length))

  model += translate([ACT2_LONG, ACT2_LONG])(
    rotate(90, DOWN_VEC)(
      x2x10(total_length)
    )
  )

  support_offset = FT
  supports = support()
  supports += up(FT)(support())
  supports += down(FT)(support())

  model += supports

  model += translate([0, total_width])(
    rotate(90, DOWN_VEC)(
      x2x6(total_length)
    )
  )

  model += translate([ACT2_LONG - tool_well_shelf_thickness, total_width - tool_well_width - ACT2_LONG])(
    timber(tool_well_shelf_thickness, tool_well_width, total_length)
  )

  return model

if __name__ == '__main__':
  model = worktop()

  scad_render_to_file(model, '_%s.scad'% __file__.split('/')[-1][:-3])