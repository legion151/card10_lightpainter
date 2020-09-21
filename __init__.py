import leds
import color
import utime
import display
import buttons
import ujson
import os
import bhi160

DELAY = 0.001 # time in seconds
BRIGHTNESS=1

def checkOrientation():
    showOrientationMsg()
    result = False
    bhi = bhi160.BHI160Orientation()
    #give sensor some time 
    utime.sleep(1)
    data = bhi.read()
    if len(data)>0:
        # don't use value near 0 to be unambiguous
        result = data[-1].z > 20
    else: 
        print("Orientation sensor had no data")

    bhi.close()
    print("Orientation result: {}".format(result))
    return result
    


def clr(clr):
    return color.Color(clr[0], clr[1], clr[2])

def anim(fn):
    countDown()
    orientation = checkOrientation()
    with open("./apps/lightpainter/anims/{}".format(fn)) as f:
        picdat = ujson.loads(f.read())

        with display.open() as d:
            d.backlight(0)
        leds.dim_top(BRIGHTNESS)

        while not buttons.read(buttons.TOP_RIGHT| buttons.BOTTOM_RIGHT | buttons.BOTTOM_LEFT): 
            for x in range(len(picdat)):
                for y in range(11):
                    if orientation:
                        leds.prep(y, clr(picdat[x][y]))
                    else:
                        leds.prep(10-y, clr(picdat[x][y]))
                leds.update()
                utime.sleep(DELAY)
        leds.clear()
        leds.update()
        return 

def showOrientationMsg():
    with display.open() as d:
        d.clear()
        d.backlight(20)
        d.print("Checking", posx=15, posy=15, font=2)
        d.print("orientation...", posx=15, posy=30, font=2)
        d.update()

def showCountDownNbr(i):
    with display.open() as d:
        d.clear()
        d.backlight(20)
        d.print(str(i), posx=65, posy=25, font=4)
        d.update()


def countDown():
    for i in range(3,0,-1):
        showCountDownNbr(i)
        utime.sleep(1)


def showAnimEntry(fn):
    with display.open() as d:
        d.clear()
        d.backlight(20)
        d.print("Lightpainter", font=2)
        d.print("{}".format(fn[0:fn.rfind(".")]), posy=23, font=2)
        addPreview(d,fn)
        d.print("<         >", posy=55, font=3)
        d.update()

def addPreview(disp, fn):
    yOff = 40
    with open("./apps/lightpainter/anims/{}".format(fn)) as f:
        picdat = ujson.loads(f.read())
        for x in range(len(picdat)):
            if(x>159):
                return
            for y in range(11):
                disp.pixel(x,y+yOff,col=picdat[x][y])



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
