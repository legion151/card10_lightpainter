#!/usr/bin/python3

import sys
from PIL import Image
import ujson


def getPxs(filenameIn):
    srcImg = Image.open(filenameIn)
    pxs = srcImg.load()
    if(srcImg.height != 11):
        raise Exception("Image has to have a size of 11")
    pxsar = []
    for x in range(srcImg.width):
        col = []
        for y in range(srcImg.height):
            col.append(pxs[x,y])
        pxsar.append(col)
    return pxsar

        

if __name__ == "__main__": 
    if(len(sys.argv) < 3):
        print("Usage: python3 {} pathToImageFile name".format(sys.argv[0]))
        exit()
    filenameIn = sys.argv[1]
    filenameOut = sys.argv[2]

    pxs = getPxs(filenameIn)
    with open("{}.json".format(filenameOut), "w") as fo:
        fo.write(ujson.dumps(pxs))



