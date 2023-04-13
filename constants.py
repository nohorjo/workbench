from solid import *
from solid.utils import *

import random

ACT2 = 38.0
ACT2_LONG = 45.0
ACT4 = 89.0
ACT6 = 145.0
ACT10 = 220.0
IN = 25.4
FT = 300.0

tool_well_width = ACT4 * 2
tool_well_shelf_thickness = 3.6

total_height = 30*IN
total_length = 6*FT
total_width = ACT10 + ACT6 + ACT2_LONG + tool_well_width

leg_height = total_height - ACT2_LONG
leg_width = 2 * ACT2

trestles_inset = 12*IN
trestle_stretcher_offset = 11*IN

strecher_length = total_length - (trestles_inset * 2) + 5.5*IN
strecher_offset = ACT6 + 3*IN

def randc():
    colours = [
        random.uniform(0.3, 1),
        random.uniform(0.3, 1),
        random.uniform(0.3, 1),u
    ]
    return lambda model : color(colours, 0.7)(model)

timber_used = {
    "2x4":[],
    "2x6":[],
    "2x10":[],
}

def _timber(x, y, length, name):
    model = color('#EED5AE')(cube([x, y, length]))

    t = 4
    tmp = cube([x, t, t])
    tmp += forward(y - t)(tmp)
    frame = tmp
    tmp = cube([t, y, t])
    tmp += right(x - t)(tmp)
    frame += tmp
    frame += up(length - t)(frame)
    tmp = cube([t, t, length])
    tmp += right(x - t)(tmp)
    tmp += forward(y - t)(tmp)
    frame += tmp
    frame = color('#7D533E')(frame)

    model += frame

    max_length = 4800 if name == "2x10" else (
        1200 if name.startswith('timber') else 2400
    )
    if length > max_length:
        model = _timber(x, y, max_length, name)
        model += up(max_length)(_timber(x, y, length - max_length, name))
    else:
        if name in timber_used:
            timber_used[name].append(length)
        else:
            timber_used[name] = [length]

    name_text = linear_extrude(3)(text(name, 14, halign = 'center'))
    model += translate([0, y / 2, length / 2])(rotate(90, FORWARD_VEC)(rotate(90, UP_VEC)(
        up(x)(name_text) + rotate(180, FORWARD_VEC)(name_text)
    )))

    return model

def timber(x, y, length):
    return _timber(x, y, length, f"timber ({x} x {y})")

def x2x4(length):
    return _timber(ACT2, ACT4, length, "2x4")

def x2x6(length):
    return _timber(ACT2_LONG, ACT6, length, "2x6")

def x2x10(length):
    return _timber(ACT2_LONG, ACT10, length, "2x10")

def x4x4(length):
    return _timber(ACT4, ACT4, length, "4x4")
