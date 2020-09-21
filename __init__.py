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

def anim(fn):
    utime.sleep(1)
    with open("./apps/lightpainter/anims/{}".format(fn)) as f:
        picdat = ujson.loads(f.read())

        with display.open() as d:
            d.backlight(0)
        leds.dim_top(BRIGHTNESS)

        while not buttons.read(buttons.TOP_RIGHT| buttons.BOTTOM_RIGHT | buttons.BOTTOM_LEFT): 
            for x in range(len(picdat)):
                for y in range(11):
                    leds.prep(10-y, clr(picdat[x][y]))
                leds.update()
                utime.sleep(DELAY)
        leds.clear()
        leds.update()
        return 

def showAnimEntry(fn):
    with display.open() as d:
        d.clear()
        d.backlight(1)
        d.print("Lightpainter", font=2)
        d.print("{}".format(fn[0:fn.rfind(".")]), posy=23, font=2)
        d.print("<         >", posy=52, font=3)
        d.update()

def main():
    fileList = os.listdir("./apps/lightpainter/anims")
    print(str(fileList))
    animIdx = 0

    while True: 
        showAnimEntry(fileList[animIdx])
        utime.sleep(.2)
        while True:
            pressed = buttons.read(
                buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT | buttons.TOP_RIGHT
            )
            if pressed != 0:
               break
        
        if pressed & buttons.BOTTOM_LEFT != 0:
            print("left")
            animIdx = animIdx-1
            if animIdx == -1:
                animIdx = len(fileList)-1
            print("idx:{}".format(animIdx))
        
        if pressed & buttons.BOTTOM_RIGHT != 0:
            print("right")
            animIdx = animIdx+1
            if animIdx == len(fileList):
                animIdx = 0
            print("idx:{}".format(animIdx))

        if pressed & buttons.TOP_RIGHT != 0:
            print("anim")
            anim(fileList[animIdx])

if __name__ == "__main__":
    main()
