import leds
import color
import utime
import display
import buttons

DELAY = 0.002 # time in seconds

cyber = [
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,0,0,0,1,1,1,1],
  [1,1,0,0,0,0,0,0,0,1,1],
  [1,0,0,0,1,1,1,0,0,0,1],
  [1,0,0,1,1,1,1,1,0,0,1],
  [1,0,0,1,1,1,1,1,0,0,1],
  [1,0,0,1,1,1,1,1,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,0,0,1],
  [1,1,1,1,1,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,1,1,1,1],
  [1,0,0,0,0,0,0,1,1,1,1],
  [1,1,1,1,1,0,0,0,0,0,1],
  [1,1,1,1,1,1,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,1,1,0,1,1,0,0,1],
  [1,0,0,1,1,0,1,1,0,0,1],
  [1,0,0,1,1,0,1,1,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,0,0,1,0,0,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,1,1,0,1,1,0,0,1],
  [1,0,0,1,1,0,1,1,0,0,1],
  [1,0,0,1,1,0,1,1,0,0,1],
  [1,0,0,1,1,1,1,1,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,0,0,0,1,0,0,1],
  [1,1,1,0,0,0,0,1,0,0,1],
  [1,0,0,0,0,1,0,0,0,0,1],
  [1,0,0,1,1,1,0,0,0,1,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1]
]

flip_vertical = False
flip_horizontal = False
with display.open() as d:
  d.backlight(0)
leds.dim_top(8)
while True:
  cyber_line = 0
  while not (buttons.read(buttons.TOP_RIGHT) | buttons.read(buttons.BOTTOM_RIGHT) | buttons.read(buttons.BOTTOM_LEFT)):
    for position, on in enumerate(cyber[cyber_line]):
      if flip_horizontal:
        if on:
          leds.prep(10-position, color.YELLOW)
        else:
          leds.prep(10-position, color.BLACK)
      else:
        if on:
          leds.prep(position, color.YELLOW)
        else:
          leds.prep(position, color.BLACK)
    leds.update()
    utime.sleep(DELAY)
    if flip_vertical == True:
      cyber_line = (cyber_line + 41)%42
    else:
      cyber_line = (cyber_line + 1)%42
    if buttons.read(buttons.BOTTOM_RIGHT):
      flip_vertical = not flip_vertical
    if buttons.read(buttons.BOTTOM_LEFT):
      flip_horizontal = not flip_horizontal
  leds.clear()
  leds.update()