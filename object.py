from solid import *
from solid.utils import *
import binpacking

from constants import *
from super_hole import *

from trestle import *
from front_stretcher import *
from rear_stretcher import *
from worktop import *

if __name__ == '__main__':
  model = forward(trestles_inset)(trestle())
  model += forward(total_length - leg_width - trestles_inset)(trestle(True))

  model += translate([
    total_width - (leg_width + ACT2) / 2,
    (total_length - strecher_length) / 2,
    strecher_offset
  ])(
    rotate(90, LEFT_VEC)(front_strecher())
  )
  
  model += translate([
    (leg_width - ACT2_LONG) / 2,
    (total_length - strecher_length) / 2,
    strecher_offset
  ])(
    rotate(90, LEFT_VEC)(rear_strecher())
  )

  model += translate([total_width, 0, total_height])(
    rotate(90, FORWARD_VEC)(
      rotate(90, LEFT_VEC)(worktop())
    )
  )
  
  scad_render_to_file(model, '_%s.scad'% __file__.split('/')[-1][:-3])

  print('**********Timber used**********')
  for name in timber_used:
    timber_used[name].sort()
    total = ceil(sum(timber_used[name]))
    lengths = map(lambda x: str(int(x)), timber_used[name])
    max_length = 3600 if name == "2x10" else 2400
    planks = binpacking.to_constant_volume(timber_used[name], max_length)
    print(f'{name}: {total} = {len(planks)}, remainder {max_length - int(total % max_length)}')
    for plank in planks:
      print(list(map(lambda x: str(ceil(x)), plank)))
  print('*******************************')

  print({
    "length": round(total_length / FT, 2),
    "width": round(total_width / IN, 2),
    "height": round(total_height / IN, 2),
    "trestles gap": round(strecher_length / IN, 2),
  })

