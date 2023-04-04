from solid import *
from solid.utils import *

from constants import *
from super_hole import *

def rear_strecher():
  model = x2x6(strecher_length)

  return model

if __name__ == '__main__':
  model = rear_strecher()
  
  scad_render_to_file(model, '_%s.scad'% __file__.split('/')[-1][:-3])