from solid import *
from solid.utils import *

from constants import *
from super_hole import *

def rear_leg():
  model = x2x4(leg_height)
  model += right(ACT2)(x2x4(leg_height - ACT2))

  return model

if __name__ == '__main__':
  model = rear_leg()
    
  scad_render_to_file(model, '_%s.scad'% __file__.split('/')[-1][:-3])
