import leds
import color
import utime
import display
import buttons
import ujson
import os

DELAY = 0.002 # time in seconds
BRIGHTNESS=1


#with display.open() as d:
#  d.print(str(os.listdir("./apps/lightpainter/anims")))
#  d.update()

def clr(clr):
    return color.Color(clr[0], clr[1], clr[2])

picdat = []
with open("./apps/lightpainter/anims/hello.json") as f:
    dat = ujson.loads(f.read())
    picdat = dat['pxs']

with display.open() as d:
  d.backlight(0)
leds.dim_top(BRIGHTNESS)

while True:
  x = 0
  while not (buttons.read(buttons.TOP_RIGHT) | buttons.read(buttons.BOTTOM_RIGHT) | buttons.read(buttons.BOTTOM_LEFT)):

    for y in range(11):
      leds.prep(10-y, clr(picdat[x][y]))

    leds.update()
    utime.sleep(DELAY)
    x = (x + 1)%len(picdat)
  leds.clear()
  leds.update()
