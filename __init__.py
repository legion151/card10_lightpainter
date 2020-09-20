import leds
import color
import utime
import display
import buttons
import ujson
import os

DELAY = 0.001 # time in seconds
BRIGHTNESS=1



def clr(clr):
    return color.Color(clr[0], clr[1], clr[2])

def anim(picdat):
    with display.open() as d:
        d.backlight(0)
    leds.dim_top(BRIGHTNESS)

    while not (buttons.read(buttons.TOP_RIGHT) | buttons.read(buttons.BOTTOM_RIGHT) | buttons.read(buttons.BOTTOM_LEFT)): 
        for x in range(len(picdat)):
            for y in range(11):
                leds.prep(10-y, clr(picdat[x][y]))
            leds.update()
            utime.sleep(DELAY)
    leds.clear()
    leds.update()
    return 

def main():
    
#    with display.open() as d:
#        d.print(str(os.listdir("./apps/lightpainter/anims")))
#        d.update()

    with open("./apps/lightpainter/anims/hello.json") as f:
        picdat = ujson.loads(f.read())
        anim(picdat)

if __name__ == "__main__":
    main()
